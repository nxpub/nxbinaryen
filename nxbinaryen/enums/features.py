# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.capi import BinaryenFeatures
from nxbinaryen.binaryen import lib

__all__ = [
    'Feature',
]


@unique
class Feature(IntFlag):
    All: BinaryenFeatures = lib.BinaryenFeatureAll()
    Atomics: BinaryenFeatures = lib.BinaryenFeatureAtomics()
    BulkMemory: BinaryenFeatures = lib.BinaryenFeatureBulkMemory()
    ExceptionHandling: BinaryenFeatures = lib.BinaryenFeatureExceptionHandling()
    ExtendedConst: BinaryenFeatures = lib.BinaryenFeatureExtendedConst()
    GC: BinaryenFeatures = lib.BinaryenFeatureGC()
    MVP: BinaryenFeatures = lib.BinaryenFeatureMVP()
    Memory64: BinaryenFeatures = lib.BinaryenFeatureMemory64()
    MultiMemories: BinaryenFeatures = lib.BinaryenFeatureMultiMemories()
    Multivalue: BinaryenFeatures = lib.BinaryenFeatureMultivalue()
    MutableGlobals: BinaryenFeatures = lib.BinaryenFeatureMutableGlobals()
    NontrappingFPToInt: BinaryenFeatures = lib.BinaryenFeatureNontrappingFPToInt()
    ReferenceTypes: BinaryenFeatures = lib.BinaryenFeatureReferenceTypes()
    RelaxedSIMD: BinaryenFeatures = lib.BinaryenFeatureRelaxedSIMD()
    SIMD128: BinaryenFeatures = lib.BinaryenFeatureSIMD128()
    SignExt: BinaryenFeatures = lib.BinaryenFeatureSignExt()
    Strings: BinaryenFeatures = lib.BinaryenFeatureStrings()
    TailCall: BinaryenFeatures = lib.BinaryenFeatureTailCall()
