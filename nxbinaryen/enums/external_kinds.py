# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.capi import BinaryenExternalKind
from nxbinaryen.binaryen import lib

__all__ = [
    'ExternalKind',
]


@unique
class ExternalKind(IntEnum):
    Function: BinaryenExternalKind = lib.BinaryenExternalFunction()
    Global: BinaryenExternalKind = lib.BinaryenExternalGlobal()
    Memory: BinaryenExternalKind = lib.BinaryenExternalMemory()
    Table: BinaryenExternalKind = lib.BinaryenExternalTable()
    Tag: BinaryenExternalKind = lib.BinaryenExternalTag()
