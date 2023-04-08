# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.capi import BinaryenSideEffects
from nxbinaryen.binaryen import lib

__all__ = [
    'SideEffect',
]


@unique
class SideEffect(IntFlag):
    Any: BinaryenSideEffects = lib.BinaryenSideEffectAny()
    Branches: BinaryenSideEffects = lib.BinaryenSideEffectBranches()
    Calls: BinaryenSideEffects = lib.BinaryenSideEffectCalls()
    DanglingPop: BinaryenSideEffects = lib.BinaryenSideEffectDanglingPop()
    ImplicitTrap: BinaryenSideEffects = lib.BinaryenSideEffectImplicitTrap()
    IsAtomic: BinaryenSideEffects = lib.BinaryenSideEffectIsAtomic()
    None_: BinaryenSideEffects = lib.BinaryenSideEffectNone()
    ReadsGlobal: BinaryenSideEffects = lib.BinaryenSideEffectReadsGlobal()
    ReadsLocal: BinaryenSideEffects = lib.BinaryenSideEffectReadsLocal()
    ReadsMemory: BinaryenSideEffects = lib.BinaryenSideEffectReadsMemory()
    ReadsTable: BinaryenSideEffects = lib.BinaryenSideEffectReadsTable()
    Throws: BinaryenSideEffects = lib.BinaryenSideEffectThrows()
    TrapsNeverHappen: BinaryenSideEffects = lib.BinaryenSideEffectTrapsNeverHappen()
    WritesGlobal: BinaryenSideEffects = lib.BinaryenSideEffectWritesGlobal()
    WritesLocal: BinaryenSideEffects = lib.BinaryenSideEffectWritesLocal()
    WritesMemory: BinaryenSideEffects = lib.BinaryenSideEffectWritesMemory()
    WritesTable: BinaryenSideEffects = lib.BinaryenSideEffectWritesTable()
