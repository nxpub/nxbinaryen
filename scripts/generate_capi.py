import tempfile

from pathlib import Path
from enum import IntFlag, auto
from typing import Tuple, List, Optional

from pycparser import c_ast, CParser

from scripts.utils import (
    preprocess_header, remove_comments, pythonize,
    PY_LIBRARY_PATH, BINARYEN_C_HEADER_PATH
)

PY_PROLOGUE = [
    '# *** DO NOT EDIT ***',
    '# Auto-generated from binaryen-c.h',  # TODO: Versioning?
    'from nxbinaryen._binaryen_capi import ffi, lib',
    ''
    'from typing import List, Any',
    '\n',
]


class ParamFlag(IntFlag):
    Ok = auto()
    String = auto()
    List = auto()
    Pointer = auto()
    Struct = auto()


TYPES_MAP = {
    'uint8_t': 'int',
    'int32_t': 'int',
    'uint32_t': 'int',
    'int64_t': 'int',
    'size_t': 'int',
    'uintptr_t': 'int',
    'double': 'float',
    'void': 'None',
}


def to_python_type(c_type, ptr_as_list: bool) -> Tuple[Optional[str], Optional[ParamFlag]]:
    if isinstance(c_type, c_ast.TypeDecl):
        return to_python_type(c_type.type, ptr_as_list)
    if isinstance(c_type, c_ast.PtrDecl):
        if isinstance(c_type.type, c_ast.TypeDecl):
            if (next_type := getattr(c_type.type, 'type', None)) and getattr(next_type, 'names', None):
                if next_type.names[0] == 'char':
                    return 'str', ParamFlag.String
        if ptr_as_list:
            internal, flag = to_python_type(c_type.type, ptr_as_list)
            return f'List[{internal}]', flag | ParamFlag.List
        return TYPES_MAP['uintptr_t'], ParamFlag.Pointer
    if isinstance(c_type, c_ast.ArrayDecl):
        # TODO: dimension = int(c_type.dim.value), can be applied via typing.Annotated
        internal, flag = to_python_type(c_type.type, ptr_as_list)
        return f'List[{internal}]', flag | ParamFlag.List
    if isinstance(c_type, c_ast.Struct):
        return c_type.name, ParamFlag.Struct
    if isinstance(c_type, c_ast.IdentifierType):
        assert len(c_type.names) == 1
        fc_type = c_type.names[0]
        return TYPES_MAP.get(fc_type, fc_type), ParamFlag.Ok
    raise NotImplementedError(f'Unsupported type {type(c_type)}')


class PyWriter(c_ast.NodeVisitor):

    def __init__(self, source_lines):
        self.lines = []
        self._source_lines = source_lines

    def emit(self, value: str):
        self.lines.append(value)


class PyFunctionsWriter(PyWriter):

    @staticmethod
    def _get_start_line(func_node) -> int:
        start_line, node = func_node.coord.line, func_node
        while node := getattr(node, 'type', None):
            if node.coord.line < start_line:
                start_line = node.coord.line
        return start_line

    @staticmethod
    def _parse_proto(func_node) -> Tuple[str, str]:
        return_type, flag = to_python_type((node := func_node).type, ptr_as_list=True)
        while not (func_name := getattr(node, 'declname', None)):
            node = node.type
        return return_type, func_name

    def _render_params(self, params) -> str:
        str_builder = []
        for idx, (param_name, param_flag) in enumerate(params):
            if param_name.startswith('num') and len(param_name) > 3 and param_name[3].isupper():
                if ParamFlag.List in params[idx - 1][1]:
                    str_builder.append(f'len({params[idx - 1][0]})')
                    continue
            # TODO: Refactor, simplify
            if param_flag == ParamFlag.Ok:
                str_builder.append(param_name)
            elif ParamFlag.String in param_flag:
                if ParamFlag.List in param_flag:
                    str_builder.append(f'[item.encode() for item in {param_name}]')
                else:
                    str_builder.append(f'{param_name}.encode()')
            elif ParamFlag.List in param_flag or ParamFlag.Struct in param_flag:
                str_builder.append(param_name)
            else:
                raise NotImplementedError
        return ', '.join(str_builder)

    def _get_doc_strings(self, line_idx: int) -> List[str]:
        result = []
        while (line := self._source_lines[line_idx - 1].strip()).startswith('//') and (line != '//'):
            result.insert(0, line[2:].strip())
            line_idx -= 1
        return result

    def visit_FuncDecl(self, node):
        return_type, func_name = self._parse_proto(node)
        if (
            (remove_prefix := func_name.startswith('Binaryen'))
            or func_name.startswith('Relooper')
            or func_name.startswith('ExpressionRunner')
            or func_name.startswith('TypeBuilder')
        ):
            self.emit('\n')
            params, py_func_name = [], func_name[8:] if remove_prefix else func_name
            # Let's skip params parsing for cases, like () and (void)
            if node.args and node.args.params and node.args.params[0].name:
                self.emit(f'def {py_func_name}(')
                for idx, param in enumerate(node.args.params):
                    param_name, (param_type, flag) = None, to_python_type(param.type, ptr_as_list=True)
                    if param_type:
                        param_name = pythonize(param.name)
                        self.emit(f'    {param_name}: {param_type},')
                    params.append((param_name, flag))
                # TODO: Some _render_proto here?
                self.emit(f') -> {return_type}:')
            else:
                self.emit(f'def {py_func_name}() -> {return_type}:')

            # Let's recover some docstrings
            # TODO: We sometimes capture the comment from region separation, seems fixable
            start_line = self._get_start_line(node)
            if doc_strings := self._get_doc_strings(start_line - 1):
                if len(doc_strings) == 1:
                    self.emit(f'    """ {doc_strings[0]} """')
                else:
                    self.emit('    """')
                    for line in doc_strings:
                        self.emit(f'    {line}')
                    self.emit('    """')

            # TODO: Looks like we should do return lib.xxx anyway, no?
            return_prefix = '' if return_type == 'None' else 'return '
            self.emit(f'    {return_prefix}lib.{func_name}({self._render_params(params)})')

            if remove_prefix:
                self.emit('\n')
                self.emit(f'{func_name} = {py_func_name}')
        else:
            raise NotImplementedError(f'Unsupported func prefix {func_name}')


class PyTypesWriter(PyWriter):

    def _render_struct(self, c_type):
        # TODO: We can try to render the struct properly, but I'm not sure how to interact w/ CFFI in this way
        self.emit(f'{c_type.declname} = Any  # struct')

    def visit_Struct(self, node):
        if node.name.startswith('Binaryen') and node.decls:
            self.emit(f'{node.name} = Any  # struct')

    def visit_Typedef(self, node):
        type_name = node.name
        if (
            type_name.startswith('Binaryen')
            or type_name.startswith('Relooper')
            or type_name.startswith('ExpressionRunner')
            or type_name.startswith('TypeBuilder')
        ):
            py_type, flag = to_python_type(node.type, ptr_as_list=False)
            if ParamFlag.Struct in flag:
                self._render_struct(node.type)
            else:
                self.emit(f'{node.name} = {py_type}')


def enforce_empty_lines(header_path: Path, fp) -> None:
    with open(header_path) as h_file:
        for idx, line in enumerate(h_file):
            if not line.strip():
                fp.write('//\n')
            else:
                fp.write(line)
    fp.flush()


def generate_capi(header_path: Path, output_path: Path) -> None:
    parser = CParser()
    # TODO: Revisit?
    with tempfile.NamedTemporaryFile('w+', dir=header_path.parent) as temp_file:
        enforce_empty_lines(header_path, temp_file)
        processed_header = preprocess_header(
            Path(temp_file.name),
            strip_deprecated=True, cpp_args=['-Ifake_libc_include', '-CC']
        )
    ast = parser.parse(remove_comments(processed_header))
    type_writer = PyTypesWriter(processed_header.splitlines())
    type_writer.visit(ast)
    func_writer = PyFunctionsWriter(processed_header.splitlines())
    func_writer.visit(ast)
    with open(output_path, 'w') as py_file:
        py_file.write('\n'.join(
            PY_PROLOGUE + type_writer.lines + func_writer.lines + ['']
        ))


if __name__ == '__main__':
    generate_capi(BINARYEN_C_HEADER_PATH, PY_LIBRARY_PATH / 'capi.py')
