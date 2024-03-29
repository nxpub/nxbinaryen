import re
import importlib
import inspect
import keyword

from pathlib import Path

from scripts.utils import load_config, temp_sys_path, BINARYEN_ROOT


def _lookup_enum_funcs(module, b_type):
    # Yes, this is slow, but reduces interdependencies
    def _predicate(obj) -> bool:
        return (
            inspect.isfunction(obj) and
            not inspect.signature(obj).parameters and
            inspect.getsourcelines(obj)[0][0].strip().endswith(f'-> {b_type}:')
        )
    for name, func in inspect.getmembers(module, _predicate):
        if not name.startswith('Binaryen'):
            yield name


def _validate_item_name(name: str) -> str:
    if keyword.iskeyword(name):
        return f'{name}_'
    return name


def _make_item_name(b_name, name, b_type, rule) -> str | None:
    if rule:
        item_name = re.search(rule, b_name).groupdict()['name']
    elif b_name.startswith(b_type):
        item_name = b_name[len(b_type):]
    elif b_name.startswith(name):
        item_name = b_name[len(name):]
    else:
        return None
    return _validate_item_name(item_name)


# TODO: I hate this, better to use pycparser at some point
RE_ENUM = re.compile(r'enum\s+(?P<enum>\w+)\s*\{(?P<items>(?:\s*\w*\s*,?)+)\};', re.MULTILINE)
RE_COMMENTS = re.compile(r'(\/\/[^\n]*|\/\*[\s\S]*?\*\/)')


def _make_map(path: Path) -> dict:
    with open(path) as h_file:
        content = RE_COMMENTS.sub('', h_file.read())
    enum_map = {}
    for match in RE_ENUM.finditer(content):
        enum_name = match.group('enum').strip()
        for item in filter(None, map(lambda x: x.strip(), match.group('items').split(','))):
            if prev := enum_map.get(item):
                raise Exception(f'Same enum item "{item}" in multiple enums ({enum_name}, {prev})')
            enum_map[item] = enum_name
    return enum_map


def generate_enums(capi_path: Path, output_path: Path, enums: list[dict]):
    with temp_sys_path(capi_path.parent.parent):
        capi_module = importlib.import_module('nxbinaryen.capi')
    init_source = []
    for enum in enums:
        module, name, base, b_type = enum['module'], enum['py_enum_name'], enum['base'], enum['binaryen_type']
        enum_names, enum_map, prefixed = [name], {}, b_type.startswith('Binaryen')
        capi_funcs = list(_lookup_enum_funcs(capi_module, b_type))
        if '/' in name:  # TODO: This is ugly, but solves 2 problems at once for now
            capi_funcs_set = set(capi_funcs)
            enum_map = {
                k: v
                for k, v in _make_map(BINARYEN_ROOT / name).items()
                if k in capi_funcs_set
            }
            enum_names = sorted(set(enum_map.values()))
        py_source = []
        if len(enum_names) > 1:
            init_source.append(f'from .{module} import (')
            for enum_name in enum_names:
                init_source.append(f'    {enum_name},')
            init_source.append(')')
        else:
            init_source.append(f'from .{module} import {enum_names[0]}')
        with open(output_path / f'{module}.py', 'w') as py_file:
            name_rule = enum.get('item_name_rule')
            py_source.append(f'# *** DO NOT EDIT ***')
            py_source.append(f'# Auto-generated from binaryen-c.h')  # TODO: Versioning?
            py_source.append(f'from enum import {base}, unique\n')
            py_source.append(f'from nxbinaryen.capi import {b_type}')
            py_source.append(f'from nxbinaryen.binaryen import lib\n')
            py_source.append(f'__all__ = [')
            for enum_name in enum_names:
                py_source.append(f'    \'{enum_name}\',')
            py_source.append(f']')
            for enum_name in enum_names:
                py_source.append('\n')
                py_source.append('@unique')
                py_source.append(f'class {enum_name}({base}):')
                for func_name in capi_funcs:
                    if enum_map:
                        if enum_map.get(func_name) != enum_name:
                            continue
                        item_name = func_name
                    else:
                        item_name = _make_item_name(func_name, enum_name, b_type, name_rule)
                    if item_name:
                        py_source.append(f'    {item_name}: {b_type} = lib.{"Binaryen" if prefixed else ""}{func_name}()')
                    else:
                        print(f'Ignored: {enum_name}.{func_name}')
            py_file.write('\n'.join(py_source + ['']))
    with open(output_path / '__init__.py', 'w') as py_file:
        py_file.write('\n'.join(init_source + ['']))


if __name__ == '__main__':
    generate_enums(
        capi_path=Path('../nxbinaryen/capi/api.py').resolve(),
        output_path=Path('../nxbinaryen/enums').resolve(),
        enums=load_config()['enums']
    )
