import typing

import re
import json
import tempfile
import subprocess
import black

from pathlib import Path
from typing import List, Optional

from pycparser.c_parser import CParser
from pycparser.c_generator import CGenerator

from nxbindgen.c99 import PyGenerator, config

BINARYEN_PATH = Path('/home/nxpub/dev/nxbinaryen/binaryen/')
OUTPUT_PATH = Path('/home/nxpub/dev/nxbinaryen/tests/')


def preprocess(c_path: Path, *, keep_comments: bool = False, cpp_args: Optional[List[str]] = None) -> str:
    lines = []
    run_line = ['cpp', '-nostdinc', '-E', '-P', *(cpp_args or []), str(c_path)] + (['-CC'] if keep_comments else [])
    print(' '.join(run_line))
    for line in map(lambda x: x.strip(), subprocess.Popen(
        run_line, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    ).stdout.read().decode('utf-8').splitlines()):
        lines.append(line)
    return '\n'.join(lines)


def remove_comments(cdef: str) -> str:
    raise NotImplementedError


class CPyGenerator(PyGenerator):

    # @staticmethod
    # def _wrap_api(orig, default: bool = False):
    #     if orig.startswith('_Py'):
    #         return f'env.api.private.{orig[1:]}'
    #     elif orig.startswith('Py'):
    #         return f'env.api.{orig}'
    #     if default and not orig.startswith('env') and not orig.startswith('assert'):
    #         return f'env.api.{orig}'
    #     return orig
    #
    # def visit_FuncCall(self, n):
    #     return self._wrap_api(super().visit_FuncCall(n), default=True)
    #
    # def visit_ID(self, n):
    #     orig = super().visit_ID(n)
    #     if orig in ('tstate', 'cframe', 'call_shape', 'frame', 'eval_breaker'):
    #         return f'env.{orig}'
    #     if orig in ('next_instr',):
    #         return f'env.flow.{orig}'
    #     return self._wrap_api(orig)
    pass


class PythonConverter:

    def __init__(
        self, *,
        imports: Optional[List[str]] = None,
        includes: Optional[List[str]] = None,
        defines: Optional[dict] = None,
    ) -> None:
        self._ast = None
        self._imports = imports or []
        self._defines = defines or {}
        self._includes = includes or []

    # Specifically for 3.11 version
    # RE_BEGIN_MARKER = re.compile(r'/\* BEWARE!(\s+.*){3}?\*/', re.MULTILINE)
    # RE_END_MARKER = re.compile(r'#if USE_COMPUTED_GOTOS\s+TARGET_DO_TRACING:', re.MULTILINE)

    def crop(self, source: str) -> str:
        # begin_match = self.RE_BEGIN_MARKER.search(source)
        # end_match = self.RE_END_MARKER.search(source)
        # return source[begin_match.span()[1]:end_match.span()[0]]
        return source

    RE_ECL_CAST = re.compile(r'\(\w+?\[(?P<dim>\d+)\]\)\{\}')

    # https://github.com/eliben/pycparser/issues/503
    def _fix_empty_compound_literal_cast(self, line: str) -> str:
        for match in self.RE_ECL_CAST.finditer(line):
            dim = int(match.groupdict()['dim'])
            _, e_pos = match.span()
            line = line[:e_pos - 1] + ', '.join('0' * dim) + line[e_pos - 1:]
        return line

    def apply_fixes(self, fp, header_path: Path) -> None:
        for macro_src, macro_dst in {
            # https://github.com/eliben/pycparser/wiki/FAQ#what-do-i-do-about-__attribute__
            '__attribute__(x)': '',
            '__typeof__(x)': '',
            # https://github.com/eliben/pycparser/issues/430, https://github.com/eliben/pycparser/issues/476
            '_Atomic(x)': 'x',
        }.items():
            fp.write(f'#define {macro_src} {macro_dst}'.strip() + '\n')
        for include_name in self._includes:
            fp.write(f'#include "{include_name}"\n')
        for macro_src, macro_dst in self._defines.items():
            fp.write(f'#define {macro_src} {macro_dst}'.strip() + '\n')
        with open(header_path) as h_file:
            lines = self.crop(h_file.read()).splitlines()
            for idx, line in enumerate(lines):
                clean = line.strip()
                if not clean:
                    fp.write('//\n')
                else:
                    # https://github.com/eliben/pycparser/issues/484
                    if clean.endswith(':') and lines[idx + 1].strip() == '}':
                        line = f'{line};'
                    # https://github.com/eliben/pycparser/issues/503
                    line = self._fix_empty_compound_literal_cast(line)
                    fp.write(line + '\n')
        fp.flush()

    def load_c(
        self, path: Path,
        flags: List[str],
        includes: List[Path],
        save_processed: bool = False,
    ) -> None:
        with tempfile.NamedTemporaryFile('w+', dir=path.parent) as temp_file:
            self.apply_fixes(temp_file, path)
            processed = preprocess(Path(temp_file.name), cpp_args=[
                *map(lambda f: f'-D{f}', flags),
                *map(lambda p: f'-I{p}', includes)
            ])
        # processed = remove_comments(processed)
        if save_processed:
            with open(OUTPUT_PATH / f'{path.name}.processed', 'w') as pr_file:
                pr_file.write(processed)
        self._ast = CParser().parse(processed, filename=str(path))

    RE_REPLACERS = {
        # r'^(\s{0,})env\.stack\.peek\((.*?)\) = (.*)(\s{0,})$': r'\1env.stack.poke(\2, \3)\4'
    }

    REPLACERS = {
        # 'env.frame.get_item(names, ': 'env.frame.get_name(',
        # 'env.frame.get_item(consts, ': 'env.frame.get_const(',
        # # '"': '\'', TODO: Requires a proper escaping
    }

    FILTERS = [
        # 'env.flow.predicted',
    ]

    def _fix_line(self, line: str) -> Optional[str]:
        for src, dst in self.RE_REPLACERS.items():
            line = re.sub(src, dst, line)
        for src, dst in self.REPLACERS.items():
            line = line.replace(src, dst)
        clear = line.strip()
        for src in self.FILTERS:
            if clear.startswith(src):
                return None
        return line

    def _fix_calls(self, content: str) -> str:
        import ast
        from nxbinaryen import capi
        from scripts.utils import load_config

        c_params = load_config()['api']['calculated_params']
        tree = ast.parse(content)

        def fix_type(obj, t_type) -> [bool, typing.Any]:
            if (origin := typing.get_origin(t_type)) is typing.Union:
                t_args = typing.get_args(t_type)
                if obj == 0 and type(None) in t_args:
                    return True, None
                for sub_type in t_args:
                    fixed, new_v = fix_type(obj, sub_type)
                    if fixed:
                        return fixed, new_v
            elif origin is list:  # typing.List
                if isinstance(obj, list):
                    sub_type = typing.get_args(t_type)[0]
                    new_obj = []
                    for item in obj:
                        fixed, new_v = fix_type(item, sub_type)
                        if fixed:
                            new_obj.append(new_v)
                        else:
                            new_obj.append(item)
            elif isinstance(t_type, typing.NewType):
                return fix_type(obj, t_type.__supertype__)
            else:
                # TODO: A little bit ugly, refactor at some point
                if t_type is type(None):
                    if obj == 0:
                        return True, None
                if t_type is bool:
                    if obj == 1:
                        return True, True
                    if obj == 0:
                        return True, False
                try:
                    if isinstance(obj, t_type):
                        return True, obj
                    print(f'Unknown case {obj} [{t_type}]')
                except TypeError:
                    # This is the case for typing.List[...], for example, we just ignore
                    return False, None
            return False, None

        class Transformer(ast.NodeTransformer):
            def visit_Call(self, node: ast.Call):
                if api_func := getattr(capi, func_name := node.func.id, None):
                    # TODO: Check prefix just in case? Not necessary now
                    # First of all, we want to remove calculated params entirely
                    if params := c_params.get(func_name, None):
                        offset = 0
                        for param_id in sorted(params.values()):
                            node.args.pop(param_id - offset)
                            offset += 1
                    # Now we can do types test
                    for idx, (arg_name, arg_type) in enumerate(api_func.__annotations__.items()):
                        if arg_name == 'return':
                            continue
                        if isinstance(pair := node.args[idx], ast.Constant):
                            fixed, new_value = fix_type(pair.value, arg_type)
                            if fixed:
                                # print(f'Mismatch({func_name}) {arg_name}={pair.value} [{arg_type}] -> {new_value}')
                                pair.value = new_value
                    # TODO: We can try to support pair as ast.List to convert [1] -> [True] or [0, ...] to bytes([0, ...])
                return self.generic_visit(node)

        tree = Transformer().visit(tree)
        return ast.unparse(tree)

    def render_py(self, path: Path, *, autoformat: bool = False) -> None:
        generator = CPyGenerator(keep_empty_declarations=False, type_hint_declarations=False, use_type_hints=True)
        with open(path, 'w') as py_file:
            if self._imports:
                for imp in self._imports:
                    py_file.write(imp + '\n')
                py_file.write('\n\n')
            content = self._fix_calls(generator.visit(self._ast, parent=None))
            if autoformat:
                content = black.format_file_contents(content, fast=False, mode=black.FileMode(
                    line_length=120,
                    string_normalization=False,
                ))
            for line in content.splitlines():
                if (line := self._fix_line(line)) is not None:
                    py_file.write(line + '\n')

    def render_c(self, path: Path) -> None:
        generator = CGenerator()
        with open(path, 'w') as c_file:
            c_file.write(generator.visit(self._ast))


if __name__ == '__main__':
    with open('./pygen.config.json') as json_file:
        config = json.load(json_file)

    bc = PythonConverter(
        imports=[
            'from nxbinaryen.capi import *',
            'from tests.utils import *',
        ],
        includes=config['INCLUDES'],
        defines=config['DEFINES'],
    )
    bc.load_c(
        BINARYEN_PATH / 'test/example/c-api-kitchen-sink.c',
        flags=[
        ],
        includes=[
            Path('./fake_libc_include').resolve(),
            BINARYEN_PATH / 'src',
        ]
    )
    # bc.render_c(OUTPUT_PATH / 'test_kitchen_sink.gen.c')
    bc.render_py(OUTPUT_PATH / 'test_kitchen_sink.gen.py', autoformat=True)
