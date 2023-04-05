import re
import json
import keyword
import subprocess

from pathlib import Path
from typing import Optional, List

__all__ = [
    'preprocess_header', 'remove_comments', 'pythonize', 'load_config', 'save_config',
    'PY_LIBRARY_PATH', 'BINARYEN_ROOT', 'BINARYEN_C_HEADER_PATH',
]

SCRIPTS_ROOT = Path(__file__).parent

BINARYEN_ROOT = SCRIPTS_ROOT.parent / 'binaryen'
BINARYEN_SRC_PATH = BINARYEN_ROOT / 'src'
BINARYEN_C_HEADER_PATH = BINARYEN_SRC_PATH / 'binaryen-c.h'

PY_LIBRARY_PATH = SCRIPTS_ROOT.parent / 'nxbinaryen'
DEFAULT_CONFIG_PATH = SCRIPTS_ROOT / 'capi.config.json'

DEPRECATION_PREFIX = '__attribute__((deprecated))'

SHADOW_NAMES = {'type', 'bytes', 'id', 'max', 'input', 'tuple'}


def load_config(config_path: Path = DEFAULT_CONFIG_PATH) -> dict:
    with open(config_path) as json_file:
        return json.load(json_file)


def save_config(config_obj: dict, config_path: Path = DEFAULT_CONFIG_PATH) -> None:
    with open(config_path, 'w') as json_file:
        json.dump(config_obj, json_file)


def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def pythonize(name: str) -> str:
    name = name.replace(' ', '_').replace('/', '').replace('__', '_')
    if keyword.iskeyword(name) or keyword.issoftkeyword(name) or name in SHADOW_NAMES:
        return f'_{name}'
    return to_snake_case(name)


def preprocess_header(header_path: Path, *, strip_deprecated: bool, cpp_args: Optional[List[str]] = None) -> str:
    lines, deprecated = [], False
    for line in map(lambda x: x.strip(), subprocess.Popen(
        ['cpp', '-nostdinc', '-E', '-P', str(header_path), *(cpp_args or [])],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    ).stdout.read().decode('utf-8').splitlines()):
        if strip_deprecated and line.startswith(DEPRECATION_PREFIX):
            deprecated = True
        if not deprecated:
            lines.append(line)
        if deprecated and line.endswith(';'):
            deprecated = False
    return '\n'.join(lines)


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
