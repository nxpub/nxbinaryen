# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.capi import BinaryenTypeSystem
from nxbinaryen.binaryen import lib

__all__ = [
    'TypeSystem',
]


@unique
class TypeSystem(IntEnum):
    Isorecursive: BinaryenTypeSystem = lib.BinaryenTypeSystemIsorecursive()
    Nominal: BinaryenTypeSystem = lib.BinaryenTypeSystemNominal()
