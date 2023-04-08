# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.capi import BinaryenType
from nxbinaryen.binaryen import lib

__all__ = [
    'Type',
]


@unique
class Type(IntEnum):
    Anyref: BinaryenType = lib.BinaryenTypeAnyref()
    Arrayref: BinaryenType = lib.BinaryenTypeArrayref()
    Auto: BinaryenType = lib.BinaryenTypeAuto()
    Eqref: BinaryenType = lib.BinaryenTypeEqref()
    Externref: BinaryenType = lib.BinaryenTypeExternref()
    Float32: BinaryenType = lib.BinaryenTypeFloat32()
    Float64: BinaryenType = lib.BinaryenTypeFloat64()
    Funcref: BinaryenType = lib.BinaryenTypeFuncref()
    I31ref: BinaryenType = lib.BinaryenTypeI31ref()
    Int32: BinaryenType = lib.BinaryenTypeInt32()
    Int64: BinaryenType = lib.BinaryenTypeInt64()
    None_: BinaryenType = lib.BinaryenTypeNone()
    NullExternref: BinaryenType = lib.BinaryenTypeNullExternref()
    NullFuncref: BinaryenType = lib.BinaryenTypeNullFuncref()
    Nullref: BinaryenType = lib.BinaryenTypeNullref()
    Stringref: BinaryenType = lib.BinaryenTypeStringref()
    StringviewIter: BinaryenType = lib.BinaryenTypeStringviewIter()
    StringviewWTF16: BinaryenType = lib.BinaryenTypeStringviewWTF16()
    StringviewWTF8: BinaryenType = lib.BinaryenTypeStringviewWTF8()
    Structref: BinaryenType = lib.BinaryenTypeStructref()
    Unreachable: BinaryenType = lib.BinaryenTypeUnreachable()
    Vec128: BinaryenType = lib.BinaryenTypeVec128()
