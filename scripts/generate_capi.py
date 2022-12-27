import re
import tempfile

from pathlib import Path
from enum import IntFlag, auto
from typing import Tuple, List, Optional

from pycparser import c_ast, CParser

from scripts.utils import (
    preprocess_header, remove_comments, pythonize, load_config,
    PY_LIBRARY_PATH, BINARYEN_C_HEADER_PATH
)

PY_PROLOGUE = [
    '# *** DO NOT EDIT ***',
    '# Auto-generated from binaryen-c.h',  # TODO: Versioning?
    'from typing import List, Any, Optional, Tuple',
    '',
    'from nxbinaryen.binaryen import ffi, lib',
    'from nxbinaryen.capi.utils import *',
    '',
]


class ParamFlag(IntFlag):
    Ok = auto()
    String = auto()
    List = auto()
    Pointer = auto()
    Struct = auto()
    CalcLen = auto()
    Optional = auto()


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

    def __init__(self, source_lines: list[str]):
        self.lines = []
        self._source_lines = source_lines

    def emit(self, value: str):
        self.lines.append(value)


class PyFunctionsWriter(PyWriter):

    def __init__(self, source_lines: list[str], config: dict):
        super().__init__(source_lines)
        self._optional_params = set(config['optional_params'])
        self._overriden_types = config['overriden_types']
        self._params_config = config['params']

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

    def _render_call_params(self, params) -> str:
        str_builder = []
        for idx, (param_name, param_flag) in enumerate(params):
            if param_flag == ParamFlag.CalcLen:
                str_builder.append(f'_len({params[idx - 1][0]})')
            elif param_flag == ParamFlag.Ok:
                str_builder.append(param_name)
            elif ParamFlag.String in param_flag:
                if ParamFlag.List in param_flag:
                    str_builder.append(f'_enc_seq({param_name})')
                else:
                    # TODO: Use some utils.str_encode(param_name) instead to handle None as ffi.NULL
                    str_builder.append(f'_enc({param_name})')
            elif ParamFlag.Optional in param_flag:
                if ParamFlag.List in param_flag:
                    str_builder.append(f'_opt_seq({param_name})')
                else:
                    str_builder.append(f'_opt({param_name})')
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

    RE_POSSIBLE_NULL = re.compile(r'\b(?P<param>[a-zA-Z0-9]+)\s+(can|should)\s+be\s+NULL', re.MULTILINE | re.IGNORECASE)

    def _get_optional_params(self, doc_strings: list[str]) -> list[str]:
        result = []
        for match in self.RE_POSSIBLE_NULL.finditer(' '.join(doc_strings)):
            result.append(match.groupdict()['param'])
        return result

    RE_RETURNS_NULL = re.compile(r'returns\sNULL', re.MULTILINE | re.IGNORECASE)

    def _is_optional_return(self, doc_strings: list[str]) -> bool:
        return bool(self.RE_RETURNS_NULL.search(' '.join(doc_strings)))

    @staticmethod
    def _is_num_param(param):
        return (
            param.name.startswith('num') and
            len(param.name) > 3 and
            param.name[3].isupper()
        )

    # TODO: Wrap out params properly

    def visit_FuncDecl(self, node):
        return_type, func_name = self._parse_proto(node)
        if (
            (remove_prefix := func_name.startswith('Binaryen'))
            or func_name.startswith('Relooper')
            or func_name.startswith('ExpressionRunner')
            or func_name.startswith('TypeBuilder')
        ):
            # Let's recover some docstrings and extract some info
            optional_params, optional_return = [], False
            start_line = self._get_start_line(node)
            if doc_strings := self._get_doc_strings(start_line - 1):
                optional_params.extend(self._get_optional_params(doc_strings))
                optional_return = self._is_optional_return(doc_strings)

            self.emit('\n')
            params, py_func_name = [], func_name[8:] if remove_prefix else func_name
            # Let's skip params parsing for cases, like () and (void)
            if node.args and node.args.params and node.args.params[0].name:
                self.emit(f'def {py_func_name}(')
                for idx, param in enumerate(node.args.params):
                    param_path = f'{func_name}.{param.name}'
                    param_meta = self._params_config.get(param_path) or {}
                    # TODO: out_param = param_meta.get('out_param', False)?
                    # Process the param
                    param_name = pythonize(param.name)
                    param_type, flag = to_python_type(param.type, ptr_as_list=True)
                    if overriden_type := self._overriden_types.get(param_path):
                        param_type, flag = overriden_type, ParamFlag.Ok
                    param_type = param_meta.get('type', param_type)  # TODO: Keep only this way to override!
                    if param.name in optional_params or param_path in self._optional_params:
                        flag |= ParamFlag.Optional
                        param_type = f'Optional[{param_type}]'
                    # Let's reduce num* params and calculated them in _render_call_params later
                    calculated_param = (
                        self._is_num_param(param) and
                        ParamFlag.List in params[idx - 1][1]
                    )
                    if not calculated_param:
                        self.emit(f'    {param_name}: {param_type},')
                    params.append((param_name, flag if not calculated_param else ParamFlag.CalcLen))
                # TODO: Some _render_proto here?
                if optional_return:
                    self.emit(f') -> Optional[{return_type}]:')
                else:
                    self.emit(f') -> {return_type}:')
            else:
                self.emit(f'def {py_func_name}() -> {return_type}:')

            # Let's render the docstrings
            if doc_strings:
                if len(doc_strings) == 1:
                    self.emit(f'    """ {doc_strings[0]} """')
                else:
                    self.emit('    """')
                    for line in doc_strings:
                        self.emit(f'    {line}')
                    self.emit('    """')

            if return_type == 'str':
                self.emit(f'    return _dec(lib.{func_name}({self._render_call_params(params)}))')
            else:
                # TODO: Looks like we should do return lib.xxx anyway, no?
                return_prefix = '' if return_type == 'None' else 'return '
                self.emit(f'    {return_prefix}lib.{func_name}({self._render_call_params(params)})')

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


def enforce_empty_lines(fp, header_path: Path) -> None:
    with open(header_path) as h_file:
        for idx, line in enumerate(h_file):
            if not line.strip():
                fp.write('//\n')
            else:
                fp.write(line)
    fp.flush()


# TODO: Probably remove, deprecated due to abnormal region size distribution (1st region >3k lines)
# RE_REGION_NAME = re.compile(r'// =+\s(?P<name>.*?)\s=+')
#
#
# def markup_regions(cdef: str, region_config: dict) -> dict:
#     region_map, pattern_start, region_name, region_start_pos = {}, False, None, 0
#     for idx, line in enumerate(map(lambda x: x.strip(), cdef.splitlines())):
#         if line == '//':
#             pattern_start = True
#         elif pattern_start and line.startswith('// ==='):
#             # Previous region ends
#             if region_name:
#                 region_map[region_name] = (region_start_pos, idx - 2)
#             # New region starts
#             region_start_pos = idx + 2
#             region_name = RE_REGION_NAME.search(line).groupdict()['name']
#             region_name = region_config.get(region_name, pythonize(region_name))
#             print('->', region_name)
#         elif pattern_start and line == '//':
#             pattern_start = False
#     region_map[region_name] = (region_start_pos, idx)
#     return region_map


def generate_capi(header_path: Path, output_path: Path) -> None:
    parser = CParser()
    config = load_config()
    # TODO: Revisit?
    with tempfile.NamedTemporaryFile('w+', dir=header_path.parent) as temp_file:
        enforce_empty_lines(temp_file, header_path)
        processed_header = preprocess_header(
            Path(temp_file.name),
            strip_deprecated=True, cpp_args=['-Ifake_libc_include', '-CC']
        )
        # region_map = markup_regions(processed_header, region_config=config['regions'])
    ast = parser.parse(remove_comments(processed_header))
    type_writer = PyTypesWriter(processed_header.splitlines())
    type_writer.visit(ast)
    func_writer = PyFunctionsWriter(processed_header.splitlines(), config=config['api'])
    func_writer.visit(ast)
    with open(output_path, 'w') as py_file:
        py_file.write('\n'.join(
            PY_PROLOGUE + type_writer.lines + func_writer.lines + ['']
        ))


if __name__ == '__main__':
    generate_capi(BINARYEN_C_HEADER_PATH, PY_LIBRARY_PATH / 'capi.py')
