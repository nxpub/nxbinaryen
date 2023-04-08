# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.capi import BinaryenHeapType
from nxbinaryen.binaryen import lib

__all__ = [
    'HeapType',
]


@unique
class HeapType(IntEnum):
    Any: BinaryenHeapType = lib.BinaryenHeapTypeAny()
    Array: BinaryenHeapType = lib.BinaryenHeapTypeArray()
    Eq: BinaryenHeapType = lib.BinaryenHeapTypeEq()
    Ext: BinaryenHeapType = lib.BinaryenHeapTypeExt()
    Func: BinaryenHeapType = lib.BinaryenHeapTypeFunc()
    I31: BinaryenHeapType = lib.BinaryenHeapTypeI31()
    Noext: BinaryenHeapType = lib.BinaryenHeapTypeNoext()
    Nofunc: BinaryenHeapType = lib.BinaryenHeapTypeNofunc()
    None_: BinaryenHeapType = lib.BinaryenHeapTypeNone()
    String: BinaryenHeapType = lib.BinaryenHeapTypeString()
    StringviewIter: BinaryenHeapType = lib.BinaryenHeapTypeStringviewIter()
    StringviewWTF16: BinaryenHeapType = lib.BinaryenHeapTypeStringviewWTF16()
    StringviewWTF8: BinaryenHeapType = lib.BinaryenHeapTypeStringviewWTF8()
    Struct: BinaryenHeapType = lib.BinaryenHeapTypeStruct()
