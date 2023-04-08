# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'TypeSystem',
]


@unique
class TypeSystem(IntEnum):
    Isorecursive = lib.BinaryenTypeSystemIsorecursive()
    Nominal = lib.BinaryenTypeSystemNominal()
