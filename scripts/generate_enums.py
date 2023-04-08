import re
import importlib
import inspect
import keyword

from pathlib import Path

from scripts.utils import load_config, temp_sys_path


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


def _make_item_name(b_name, name, b_type, rule) -> str:
    if rule:
        item_name = re.search(rule, b_name).groupdict()['name']
    elif b_name.startswith(b_type):
        item_name = b_name[len(b_type):]
    elif b_name.startswith(name):
        item_name = b_name[len(name):]
    else:
        item_name = b_name
    return _validate_item_name(item_name)


def generate_enums(capi_path: Path, output_path: Path, enums: list[dict]):
    with temp_sys_path(capi_path.parent.parent):
        capi_module = importlib.import_module('nxbinaryen.capi')
    init_source = []
    for enum in enums:
        prefixed = enum.get('prefixed', True)
        module, name, base, b_type = enum['module'], enum['py_enum_name'], enum['base'], enum['binaryen_type']
        py_source = []
        init_source.append(f'from .{module} import {name}')
        with open(output_path / f'{module}.py', 'w') as py_file:
            name_rule = enum.get('item_name_rule')
            py_source.append(f'# *** DO NOT EDIT ***')
            py_source.append(f'# Auto-generated from binaryen-c.h')  # TODO: Versioning?
            py_source.append(f'from enum import {base}, unique\n')
            py_source.append(f'from nxbinaryen.binaryen import lib\n')
            py_source.append(f'__all__ = [')
            py_source.append(f'    \'{name}\',')
            py_source.append(f']\n\n')
            py_source.append('@unique')
            py_source.append(f'class {name}({base}):')
            for func_name in _lookup_enum_funcs(capi_module, b_type):
                item_name = _make_item_name(func_name, name, b_type, name_rule)
                py_source.append(f'    {item_name} = lib.{"Binaryen" if prefixed else ""}{func_name}()')
            py_file.write('\n'.join(py_source + ['']))
    with open(output_path / '__init__.py', 'w') as py_file:
        py_file.write('\n'.join(init_source + ['']))


if __name__ == '__main__':
    generate_enums(
        capi_path=Path('../nxbinaryen/capi/api.py').resolve(),
        output_path=Path('../nxbinaryen/enums').resolve(),
        enums=load_config()['enums']
    )
