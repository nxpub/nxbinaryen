# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'PackedType',
]


@unique
class PackedType(IntEnum):
    Int16 = lib.BinaryenPackedTypeInt16()
    Int8 = lib.BinaryenPackedTypeInt8()
    NotPacked = lib.BinaryenPackedTypeNotPacked()
