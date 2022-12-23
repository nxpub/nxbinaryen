import re
import keyword

from pathlib import Path
from enum import IntFlag, auto
from typing import Tuple, List, Optional

from pycparser import c_ast, CParser

from scripts.utils import preprocess_header, SCRIPTS_ROOT, BINARYEN_C_HEADER_PATH

PY_LIBRARY_PATH = SCRIPTS_ROOT.parent / 'nxbinaryen'

PY_PROLOGUE = [
    f'# Auto-generated from binaryen-c.h',  # TODO: Versioning?
    'from nxbinaryen._binaryen_capi import ffi, lib',
    ''
    'from typing import List, Any',
    '\n',
    'BinaryenType = Any',
    'BinaryenHeapType = BinaryenPackedType = BinaryenBasicHeapType = Any',
    'BinaryenIndex = BinaryenOp = Any',
    'BinaryenModuleAllocateAndWriteResult = Any',
    'BinaryenTypeSystem = BinaryenBufferSizes = Any',
    'BinaryenExpressionId = BinaryenExternalKind = BinaryenFeatures = BinaryenSideEffects = Any',
    'BinaryenLiteral = Any',
    'BinaryenModuleRef = BinaryenExpressionRef = TypeBuilderRef = BinaryenGlobalRef = BinaryenTagRef = Any',
    'BinaryenTableRef = BinaryenFunctionRef = BinaryenExportRef = BinaryenElementSegmentRef = Any',
    'RelooperRef = RelooperBlockRef = Any',
    'TypeBuilderErrorReason = Any',
    'ExpressionRunnerFlags = ExpressionRunnerRef = Any',
]


class ParamFlag(IntFlag):
    Ok = auto()
    CalcLen = auto()
    String = auto()
    List = auto()


def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


SHADOW_NAMES = {'type', 'bytes', 'id', 'max', 'input', 'tuple'}


def pythonize(name: str) -> str:
    if keyword.iskeyword(name) or keyword.issoftkeyword(name) or name in SHADOW_NAMES:
        return f'_{name}'
    return to_snake_case(name)


class PyWriter(c_ast.NodeVisitor):

    def __init__(self, source_lines):
        self.lines = []
        self._source_lines = source_lines

    def emit(self, value: str):
        self.lines.append(value)


class PyFunctionsWriter(PyWriter):

    TYPES_MAP = {
        'uint8_t': 'int',
        'int32_t': 'int',
        'uint32_t': 'int',
        'int64_t': 'int',
        'size_t': 'int',
        'double': 'float',
        'void': 'None',
    }

    def _get_param_type(self, c_type) -> Tuple[Optional[str], Optional[ParamFlag]]:
        if isinstance(c_type, c_ast.TypeDecl):
            if c_type.declname.startswith('num') and len(c_type.declname) > 3 and c_type.declname[3].isupper():
                return None, ParamFlag.CalcLen
            return self._get_param_type(c_type.type)
        if isinstance(c_type, c_ast.PtrDecl):
            if isinstance(c_type.type, c_ast.TypeDecl):
                if (next_type := getattr(c_type.type, 'type', None)) and getattr(next_type, 'names', None):
                    if next_type.names[0] == 'char':
                        return 'str', ParamFlag.String
            internal, flag = self._get_param_type(c_type.type)
            return f'List[{internal}]', flag | ParamFlag.List
        if isinstance(c_type, c_ast.ArrayDecl):
            # TODO: dimension = int(c_type.dim.value), can be applied via typing.Annotated
            internal, flag = self._get_param_type(c_type.type)
            return f'List[{internal}]', flag | ParamFlag.List
        if isinstance(c_type, c_ast.Struct):
            return c_type.name, ParamFlag.Ok
        if isinstance(c_type, c_ast.IdentifierType):
            assert len(c_type.names) == 1
            fc_type = c_type.names[0]
            return self.TYPES_MAP.get(fc_type, fc_type), ParamFlag.Ok
        raise NotImplementedError(f'Unsupported type {type(c_type)}')

    def _get_start_line(self, func_node) -> int:
        start_line, node = func_node.coord.line, func_node
        while node := getattr(node, 'type', None):
            if node.coord.line < start_line:
                start_line = node.coord.line
        return start_line

    def _parse_proto(self, func_node) -> Tuple[str, str]:
        return_type, flag = self._get_param_type((node := func_node).type)
        while not (func_name := getattr(node, 'declname', None)):
            node = node.type
        return return_type, func_name

    def _render_params(self, params) -> str:
        str_builder = []
        for idx, (param_name, param_flag) in enumerate(params):
            if param_flag == ParamFlag.Ok:
                str_builder.append(param_name)
            elif ParamFlag.CalcLen in param_flag:
                str_builder.append(f'len({params[idx - 1][0]})')
            elif ParamFlag.String in param_flag:
                if ParamFlag.List in param_flag:
                    str_builder.append(f'[item.encode() for item in {param_name}]')
                else:
                    str_builder.append(f'{param_name}.encode()')
            elif ParamFlag.List in param_flag:
                str_builder.append(param_name)
            else:
                raise NotImplementedError
        return ', '.join(str_builder)

    def _get_doc_strings(self, line_idx: int) -> List[str]:
        result = []
        while (line := self._source_lines[line_idx - 1].strip()).startswith('//'):
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
                    param_name, (param_type, flag) = None, self._get_param_type(param.type)
                    if param_type:
                        param_name = pythonize(param.name)
                        self.emit(f'    {param_name}: {param_type},')
                    params.append((param_name, flag))
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
            self.emit(f'    {return_prefix}lib.{func_name}({self._render_params(params)})')  # ", ".join(params)
        else:
            raise NotImplementedError(f'Unsupported func prefix {func_name}')


def remove_comments(cdef: str) -> str:
    lines, cpp_comment = [], False
    cdef_lines = cdef.splitlines()
    for line in cdef_lines:
        clean_line = line.strip()
        if clean_line.startswith('//'):
            lines.append('')
        elif clean_line.startswith('/*'):
            if not clean_line.endswith('*/'):
                cpp_comment = True
            lines.append('')
        elif clean_line.endswith('*/'):
            cpp_comment = False
            lines.append('')
        elif cpp_comment:
            lines.append('')
        else:
            lines.append(line)
    assert len(cdef_lines) == len(lines)
    return '\n'.join(lines)


def generate_capi(header_path: Path, output_path: Path) -> None:
    parser = CParser()
    processed_header = preprocess_header(header_path, strip_deprecated=True, cpp_args=['-Ifake_libc_include', '-CC'])
    ast = parser.parse(remove_comments(processed_header))
    func_writer = PyFunctionsWriter(processed_header.splitlines())
    func_writer.visit(ast)
    with open(output_path, 'w') as py_file:
        py_file.write('\n'.join(
            PY_PROLOGUE + func_writer.lines + ['']
        ))


if __name__ == '__main__':
    generate_capi(BINARYEN_C_HEADER_PATH, PY_LIBRARY_PATH / 'capi.py')
