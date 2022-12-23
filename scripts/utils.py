import subprocess

from pathlib import Path
from typing import Optional, List

__all__ = [
    'preprocess_header', 'SCRIPTS_ROOT', 'BINARYEN_C_HEADER_PATH',
]

SCRIPTS_ROOT = Path(__file__).parent

BINARYEN_ROOT = SCRIPTS_ROOT.parent / 'binaryen'
BINARYEN_SRC_PATH = BINARYEN_ROOT / 'src'
BINARYEN_C_HEADER_PATH = BINARYEN_SRC_PATH / 'binaryen-c.h'

DEPRECATION_PREFIX = '__attribute__((deprecated))'


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
