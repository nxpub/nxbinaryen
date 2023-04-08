# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.capi import BinaryenPackedType
from nxbinaryen.binaryen import lib

__all__ = [
    'PackedType',
]


@unique
class PackedType(IntEnum):
    Int16: BinaryenPackedType = lib.BinaryenPackedTypeInt16()
    Int8: BinaryenPackedType = lib.BinaryenPackedTypeInt8()
    NotPacked: BinaryenPackedType = lib.BinaryenPackedTypeNotPacked()
