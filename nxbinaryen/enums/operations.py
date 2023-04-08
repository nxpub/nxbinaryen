# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'BinaryOp',
    'BrOnOp',
    'RefAsOp',
    'SIMDExtractOp',
    'SIMDLoadOp',
    'SIMDLoadStoreLaneOp',
    'SIMDReplaceOp',
    'SIMDShiftOp',
    'SIMDTernaryOp',
    'StringAsOp',
    'StringEncodeOp',
    'StringEqOp',
    'StringIterMoveOp',
    'StringMeasureOp',
    'StringNewOp',
    'StringSliceWTFOp',
    'UnaryOp',
]


@unique
class BinaryOp(IntEnum):
    AddFloat32 = lib.BinaryenAddFloat32()
    AddFloat64 = lib.BinaryenAddFloat64()
    AddInt32 = lib.BinaryenAddInt32()
    AddInt64 = lib.BinaryenAddInt64()
    AddSatSVecI16x8 = lib.BinaryenAddSatSVecI16x8()
    AddSatSVecI8x16 = lib.BinaryenAddSatSVecI8x16()
    AddSatUVecI16x8 = lib.BinaryenAddSatUVecI16x8()
    AddSatUVecI8x16 = lib.BinaryenAddSatUVecI8x16()
    AddVecF32x4 = lib.BinaryenAddVecF32x4()
    AddVecF64x2 = lib.BinaryenAddVecF64x2()
    AddVecI16x8 = lib.BinaryenAddVecI16x8()
    AddVecI32x4 = lib.BinaryenAddVecI32x4()
    AddVecI64x2 = lib.BinaryenAddVecI64x2()
    AddVecI8x16 = lib.BinaryenAddVecI8x16()
    AndInt32 = lib.BinaryenAndInt32()
    AndInt64 = lib.BinaryenAndInt64()
    AndNotVec128 = lib.BinaryenAndNotVec128()
    AndVec128 = lib.BinaryenAndVec128()
    AvgrUVecI16x8 = lib.BinaryenAvgrUVecI16x8()
    AvgrUVecI8x16 = lib.BinaryenAvgrUVecI8x16()
    CopySignFloat32 = lib.BinaryenCopySignFloat32()
    CopySignFloat64 = lib.BinaryenCopySignFloat64()
    DivFloat32 = lib.BinaryenDivFloat32()
    DivFloat64 = lib.BinaryenDivFloat64()
    DivSInt32 = lib.BinaryenDivSInt32()
    DivSInt64 = lib.BinaryenDivSInt64()
    DivUInt32 = lib.BinaryenDivUInt32()
    DivUInt64 = lib.BinaryenDivUInt64()
    DivVecF32x4 = lib.BinaryenDivVecF32x4()
    DivVecF64x2 = lib.BinaryenDivVecF64x2()
    DotI8x16I7x16SToVecI16x8 = lib.BinaryenDotI8x16I7x16SToVecI16x8()
    DotSVecI16x8ToVecI32x4 = lib.BinaryenDotSVecI16x8ToVecI32x4()
    EqFloat32 = lib.BinaryenEqFloat32()
    EqFloat64 = lib.BinaryenEqFloat64()
    EqInt32 = lib.BinaryenEqInt32()
    EqInt64 = lib.BinaryenEqInt64()
    EqVecF32x4 = lib.BinaryenEqVecF32x4()
    EqVecF64x2 = lib.BinaryenEqVecF64x2()
    EqVecI16x8 = lib.BinaryenEqVecI16x8()
    EqVecI32x4 = lib.BinaryenEqVecI32x4()
    EqVecI64x2 = lib.BinaryenEqVecI64x2()
    EqVecI8x16 = lib.BinaryenEqVecI8x16()
    ExtMulHighSVecI16x8 = lib.BinaryenExtMulHighSVecI16x8()
    ExtMulHighSVecI32x4 = lib.BinaryenExtMulHighSVecI32x4()
    ExtMulHighSVecI64x2 = lib.BinaryenExtMulHighSVecI64x2()
    ExtMulHighUVecI16x8 = lib.BinaryenExtMulHighUVecI16x8()
    ExtMulHighUVecI32x4 = lib.BinaryenExtMulHighUVecI32x4()
    ExtMulHighUVecI64x2 = lib.BinaryenExtMulHighUVecI64x2()
    ExtMulLowSVecI16x8 = lib.BinaryenExtMulLowSVecI16x8()
    ExtMulLowSVecI32x4 = lib.BinaryenExtMulLowSVecI32x4()
    ExtMulLowSVecI64x2 = lib.BinaryenExtMulLowSVecI64x2()
    ExtMulLowUVecI16x8 = lib.BinaryenExtMulLowUVecI16x8()
    ExtMulLowUVecI32x4 = lib.BinaryenExtMulLowUVecI32x4()
    ExtMulLowUVecI64x2 = lib.BinaryenExtMulLowUVecI64x2()
    GeFloat32 = lib.BinaryenGeFloat32()
    GeFloat64 = lib.BinaryenGeFloat64()
    GeSInt32 = lib.BinaryenGeSInt32()
    GeSInt64 = lib.BinaryenGeSInt64()
    GeSVecI16x8 = lib.BinaryenGeSVecI16x8()
    GeSVecI32x4 = lib.BinaryenGeSVecI32x4()
    GeSVecI64x2 = lib.BinaryenGeSVecI64x2()
    GeSVecI8x16 = lib.BinaryenGeSVecI8x16()
    GeUInt32 = lib.BinaryenGeUInt32()
    GeUInt64 = lib.BinaryenGeUInt64()
    GeUVecI16x8 = lib.BinaryenGeUVecI16x8()
    GeUVecI32x4 = lib.BinaryenGeUVecI32x4()
    GeUVecI8x16 = lib.BinaryenGeUVecI8x16()
    GeVecF32x4 = lib.BinaryenGeVecF32x4()
    GeVecF64x2 = lib.BinaryenGeVecF64x2()
    GtFloat32 = lib.BinaryenGtFloat32()
    GtFloat64 = lib.BinaryenGtFloat64()
    GtSInt32 = lib.BinaryenGtSInt32()
    GtSInt64 = lib.BinaryenGtSInt64()
    GtSVecI16x8 = lib.BinaryenGtSVecI16x8()
    GtSVecI32x4 = lib.BinaryenGtSVecI32x4()
    GtSVecI64x2 = lib.BinaryenGtSVecI64x2()
    GtSVecI8x16 = lib.BinaryenGtSVecI8x16()
    GtUInt32 = lib.BinaryenGtUInt32()
    GtUInt64 = lib.BinaryenGtUInt64()
    GtUVecI16x8 = lib.BinaryenGtUVecI16x8()
    GtUVecI32x4 = lib.BinaryenGtUVecI32x4()
    GtUVecI8x16 = lib.BinaryenGtUVecI8x16()
    GtVecF32x4 = lib.BinaryenGtVecF32x4()
    GtVecF64x2 = lib.BinaryenGtVecF64x2()
    LeFloat32 = lib.BinaryenLeFloat32()
    LeFloat64 = lib.BinaryenLeFloat64()
    LeSInt32 = lib.BinaryenLeSInt32()
    LeSInt64 = lib.BinaryenLeSInt64()
    LeSVecI16x8 = lib.BinaryenLeSVecI16x8()
    LeSVecI32x4 = lib.BinaryenLeSVecI32x4()
    LeSVecI64x2 = lib.BinaryenLeSVecI64x2()
    LeSVecI8x16 = lib.BinaryenLeSVecI8x16()
    LeUInt32 = lib.BinaryenLeUInt32()
    LeUInt64 = lib.BinaryenLeUInt64()
    LeUVecI16x8 = lib.BinaryenLeUVecI16x8()
    LeUVecI32x4 = lib.BinaryenLeUVecI32x4()
    LeUVecI8x16 = lib.BinaryenLeUVecI8x16()
    LeVecF32x4 = lib.BinaryenLeVecF32x4()
    LeVecF64x2 = lib.BinaryenLeVecF64x2()
    LtFloat32 = lib.BinaryenLtFloat32()
    LtFloat64 = lib.BinaryenLtFloat64()
    LtSInt32 = lib.BinaryenLtSInt32()
    LtSInt64 = lib.BinaryenLtSInt64()
    LtSVecI16x8 = lib.BinaryenLtSVecI16x8()
    LtSVecI32x4 = lib.BinaryenLtSVecI32x4()
    LtSVecI64x2 = lib.BinaryenLtSVecI64x2()
    LtSVecI8x16 = lib.BinaryenLtSVecI8x16()
    LtUInt32 = lib.BinaryenLtUInt32()
    LtUInt64 = lib.BinaryenLtUInt64()
    LtUVecI16x8 = lib.BinaryenLtUVecI16x8()
    LtUVecI32x4 = lib.BinaryenLtUVecI32x4()
    LtUVecI8x16 = lib.BinaryenLtUVecI8x16()
    LtVecF32x4 = lib.BinaryenLtVecF32x4()
    LtVecF64x2 = lib.BinaryenLtVecF64x2()
    MaxFloat32 = lib.BinaryenMaxFloat32()
    MaxFloat64 = lib.BinaryenMaxFloat64()
    MaxSVecI16x8 = lib.BinaryenMaxSVecI16x8()
    MaxSVecI32x4 = lib.BinaryenMaxSVecI32x4()
    MaxSVecI8x16 = lib.BinaryenMaxSVecI8x16()
    MaxUVecI16x8 = lib.BinaryenMaxUVecI16x8()
    MaxUVecI32x4 = lib.BinaryenMaxUVecI32x4()
    MaxUVecI8x16 = lib.BinaryenMaxUVecI8x16()
    MaxVecF32x4 = lib.BinaryenMaxVecF32x4()
    MaxVecF64x2 = lib.BinaryenMaxVecF64x2()
    MinFloat32 = lib.BinaryenMinFloat32()
    MinFloat64 = lib.BinaryenMinFloat64()
    MinSVecI16x8 = lib.BinaryenMinSVecI16x8()
    MinSVecI32x4 = lib.BinaryenMinSVecI32x4()
    MinSVecI8x16 = lib.BinaryenMinSVecI8x16()
    MinUVecI16x8 = lib.BinaryenMinUVecI16x8()
    MinUVecI32x4 = lib.BinaryenMinUVecI32x4()
    MinUVecI8x16 = lib.BinaryenMinUVecI8x16()
    MinVecF32x4 = lib.BinaryenMinVecF32x4()
    MinVecF64x2 = lib.BinaryenMinVecF64x2()
    MulFloat32 = lib.BinaryenMulFloat32()
    MulFloat64 = lib.BinaryenMulFloat64()
    MulInt32 = lib.BinaryenMulInt32()
    MulInt64 = lib.BinaryenMulInt64()
    MulVecF32x4 = lib.BinaryenMulVecF32x4()
    MulVecF64x2 = lib.BinaryenMulVecF64x2()
    MulVecI16x8 = lib.BinaryenMulVecI16x8()
    MulVecI32x4 = lib.BinaryenMulVecI32x4()
    MulVecI64x2 = lib.BinaryenMulVecI64x2()
    NarrowSVecI16x8ToVecI8x16 = lib.BinaryenNarrowSVecI16x8ToVecI8x16()
    NarrowSVecI32x4ToVecI16x8 = lib.BinaryenNarrowSVecI32x4ToVecI16x8()
    NarrowUVecI16x8ToVecI8x16 = lib.BinaryenNarrowUVecI16x8ToVecI8x16()
    NarrowUVecI32x4ToVecI16x8 = lib.BinaryenNarrowUVecI32x4ToVecI16x8()
    NeFloat32 = lib.BinaryenNeFloat32()
    NeFloat64 = lib.BinaryenNeFloat64()
    NeInt32 = lib.BinaryenNeInt32()
    NeInt64 = lib.BinaryenNeInt64()
    NeVecF32x4 = lib.BinaryenNeVecF32x4()
    NeVecF64x2 = lib.BinaryenNeVecF64x2()
    NeVecI16x8 = lib.BinaryenNeVecI16x8()
    NeVecI32x4 = lib.BinaryenNeVecI32x4()
    NeVecI64x2 = lib.BinaryenNeVecI64x2()
    NeVecI8x16 = lib.BinaryenNeVecI8x16()
    OrInt32 = lib.BinaryenOrInt32()
    OrInt64 = lib.BinaryenOrInt64()
    OrVec128 = lib.BinaryenOrVec128()
    PMaxVecF32x4 = lib.BinaryenPMaxVecF32x4()
    PMaxVecF64x2 = lib.BinaryenPMaxVecF64x2()
    PMinVecF32x4 = lib.BinaryenPMinVecF32x4()
    PMinVecF64x2 = lib.BinaryenPMinVecF64x2()
    Q15MulrSatSVecI16x8 = lib.BinaryenQ15MulrSatSVecI16x8()
    RelaxedMaxVecF32x4 = lib.BinaryenRelaxedMaxVecF32x4()
    RelaxedMaxVecF64x2 = lib.BinaryenRelaxedMaxVecF64x2()
    RelaxedMinVecF32x4 = lib.BinaryenRelaxedMinVecF32x4()
    RelaxedMinVecF64x2 = lib.BinaryenRelaxedMinVecF64x2()
    RelaxedQ15MulrSVecI16x8 = lib.BinaryenRelaxedQ15MulrSVecI16x8()
    RelaxedSwizzleVecI8x16 = lib.BinaryenRelaxedSwizzleVecI8x16()
    RemSInt32 = lib.BinaryenRemSInt32()
    RemSInt64 = lib.BinaryenRemSInt64()
    RemUInt32 = lib.BinaryenRemUInt32()
    RemUInt64 = lib.BinaryenRemUInt64()
    RotLInt32 = lib.BinaryenRotLInt32()
    RotLInt64 = lib.BinaryenRotLInt64()
    RotRInt32 = lib.BinaryenRotRInt32()
    RotRInt64 = lib.BinaryenRotRInt64()
    ShlInt32 = lib.BinaryenShlInt32()
    ShlInt64 = lib.BinaryenShlInt64()
    ShrSInt32 = lib.BinaryenShrSInt32()
    ShrSInt64 = lib.BinaryenShrSInt64()
    ShrUInt32 = lib.BinaryenShrUInt32()
    ShrUInt64 = lib.BinaryenShrUInt64()
    SubFloat32 = lib.BinaryenSubFloat32()
    SubFloat64 = lib.BinaryenSubFloat64()
    SubInt32 = lib.BinaryenSubInt32()
    SubInt64 = lib.BinaryenSubInt64()
    SubSatSVecI16x8 = lib.BinaryenSubSatSVecI16x8()
    SubSatSVecI8x16 = lib.BinaryenSubSatSVecI8x16()
    SubSatUVecI16x8 = lib.BinaryenSubSatUVecI16x8()
    SubSatUVecI8x16 = lib.BinaryenSubSatUVecI8x16()
    SubVecF32x4 = lib.BinaryenSubVecF32x4()
    SubVecF64x2 = lib.BinaryenSubVecF64x2()
    SubVecI16x8 = lib.BinaryenSubVecI16x8()
    SubVecI32x4 = lib.BinaryenSubVecI32x4()
    SubVecI64x2 = lib.BinaryenSubVecI64x2()
    SubVecI8x16 = lib.BinaryenSubVecI8x16()
    SwizzleVecI8x16 = lib.BinaryenSwizzleVecI8x16()
    XorInt32 = lib.BinaryenXorInt32()
    XorInt64 = lib.BinaryenXorInt64()
    XorVec128 = lib.BinaryenXorVec128()


@unique
class BrOnOp(IntEnum):
    BrOnCast = lib.BinaryenBrOnCast()
    BrOnCastFail = lib.BinaryenBrOnCastFail()
    BrOnNonNull = lib.BinaryenBrOnNonNull()
    BrOnNull = lib.BinaryenBrOnNull()


@unique
class RefAsOp(IntEnum):
    RefAsNonNull = lib.BinaryenRefAsNonNull()


@unique
class SIMDExtractOp(IntEnum):
    ExtractLaneSVecI16x8 = lib.BinaryenExtractLaneSVecI16x8()
    ExtractLaneSVecI8x16 = lib.BinaryenExtractLaneSVecI8x16()
    ExtractLaneUVecI16x8 = lib.BinaryenExtractLaneUVecI16x8()
    ExtractLaneUVecI8x16 = lib.BinaryenExtractLaneUVecI8x16()
    ExtractLaneVecF32x4 = lib.BinaryenExtractLaneVecF32x4()
    ExtractLaneVecF64x2 = lib.BinaryenExtractLaneVecF64x2()
    ExtractLaneVecI32x4 = lib.BinaryenExtractLaneVecI32x4()
    ExtractLaneVecI64x2 = lib.BinaryenExtractLaneVecI64x2()


@unique
class SIMDLoadOp(IntEnum):
    Load16SplatVec128 = lib.BinaryenLoad16SplatVec128()
    Load16x4SVec128 = lib.BinaryenLoad16x4SVec128()
    Load16x4UVec128 = lib.BinaryenLoad16x4UVec128()
    Load32SplatVec128 = lib.BinaryenLoad32SplatVec128()
    Load32ZeroVec128 = lib.BinaryenLoad32ZeroVec128()
    Load32x2SVec128 = lib.BinaryenLoad32x2SVec128()
    Load32x2UVec128 = lib.BinaryenLoad32x2UVec128()
    Load64SplatVec128 = lib.BinaryenLoad64SplatVec128()
    Load64ZeroVec128 = lib.BinaryenLoad64ZeroVec128()
    Load8SplatVec128 = lib.BinaryenLoad8SplatVec128()
    Load8x8SVec128 = lib.BinaryenLoad8x8SVec128()
    Load8x8UVec128 = lib.BinaryenLoad8x8UVec128()


@unique
class SIMDLoadStoreLaneOp(IntEnum):
    Load16LaneVec128 = lib.BinaryenLoad16LaneVec128()
    Load32LaneVec128 = lib.BinaryenLoad32LaneVec128()
    Load64LaneVec128 = lib.BinaryenLoad64LaneVec128()
    Load8LaneVec128 = lib.BinaryenLoad8LaneVec128()
    Store16LaneVec128 = lib.BinaryenStore16LaneVec128()
    Store32LaneVec128 = lib.BinaryenStore32LaneVec128()
    Store64LaneVec128 = lib.BinaryenStore64LaneVec128()
    Store8LaneVec128 = lib.BinaryenStore8LaneVec128()


@unique
class SIMDReplaceOp(IntEnum):
    ReplaceLaneVecF32x4 = lib.BinaryenReplaceLaneVecF32x4()
    ReplaceLaneVecF64x2 = lib.BinaryenReplaceLaneVecF64x2()
    ReplaceLaneVecI16x8 = lib.BinaryenReplaceLaneVecI16x8()
    ReplaceLaneVecI32x4 = lib.BinaryenReplaceLaneVecI32x4()
    ReplaceLaneVecI64x2 = lib.BinaryenReplaceLaneVecI64x2()
    ReplaceLaneVecI8x16 = lib.BinaryenReplaceLaneVecI8x16()


@unique
class SIMDShiftOp(IntEnum):
    ShlVecI16x8 = lib.BinaryenShlVecI16x8()
    ShlVecI32x4 = lib.BinaryenShlVecI32x4()
    ShlVecI64x2 = lib.BinaryenShlVecI64x2()
    ShlVecI8x16 = lib.BinaryenShlVecI8x16()
    ShrSVecI16x8 = lib.BinaryenShrSVecI16x8()
    ShrSVecI32x4 = lib.BinaryenShrSVecI32x4()
    ShrSVecI64x2 = lib.BinaryenShrSVecI64x2()
    ShrSVecI8x16 = lib.BinaryenShrSVecI8x16()
    ShrUVecI16x8 = lib.BinaryenShrUVecI16x8()
    ShrUVecI32x4 = lib.BinaryenShrUVecI32x4()
    ShrUVecI64x2 = lib.BinaryenShrUVecI64x2()
    ShrUVecI8x16 = lib.BinaryenShrUVecI8x16()


@unique
class SIMDTernaryOp(IntEnum):
    DotI8x16I7x16AddSToVecI32x4 = lib.BinaryenDotI8x16I7x16AddSToVecI32x4()
    LaneselectI16x8 = lib.BinaryenLaneselectI16x8()
    LaneselectI32x4 = lib.BinaryenLaneselectI32x4()
    LaneselectI64x2 = lib.BinaryenLaneselectI64x2()
    LaneselectI8x16 = lib.BinaryenLaneselectI8x16()
    RelaxedFmaVecF32x4 = lib.BinaryenRelaxedFmaVecF32x4()
    RelaxedFmaVecF64x2 = lib.BinaryenRelaxedFmaVecF64x2()
    RelaxedFmsVecF32x4 = lib.BinaryenRelaxedFmsVecF32x4()
    RelaxedFmsVecF64x2 = lib.BinaryenRelaxedFmsVecF64x2()


@unique
class StringAsOp(IntEnum):
    StringAsIter = lib.BinaryenStringAsIter()
    StringAsWTF16 = lib.BinaryenStringAsWTF16()
    StringAsWTF8 = lib.BinaryenStringAsWTF8()


@unique
class StringEncodeOp(IntEnum):
    StringEncodeUTF8 = lib.BinaryenStringEncodeUTF8()
    StringEncodeUTF8Array = lib.BinaryenStringEncodeUTF8Array()
    StringEncodeWTF16 = lib.BinaryenStringEncodeWTF16()
    StringEncodeWTF16Array = lib.BinaryenStringEncodeWTF16Array()
    StringEncodeWTF8 = lib.BinaryenStringEncodeWTF8()
    StringEncodeWTF8Array = lib.BinaryenStringEncodeWTF8Array()


@unique
class StringEqOp(IntEnum):
    StringEqCompare = lib.BinaryenStringEqCompare()
    StringEqEqual = lib.BinaryenStringEqEqual()


@unique
class StringIterMoveOp(IntEnum):
    StringIterMoveAdvance = lib.BinaryenStringIterMoveAdvance()
    StringIterMoveRewind = lib.BinaryenStringIterMoveRewind()


@unique
class StringMeasureOp(IntEnum):
    StringMeasureIsUSV = lib.BinaryenStringMeasureIsUSV()
    StringMeasureUTF8 = lib.BinaryenStringMeasureUTF8()
    StringMeasureWTF16 = lib.BinaryenStringMeasureWTF16()
    StringMeasureWTF16View = lib.BinaryenStringMeasureWTF16View()
    StringMeasureWTF8 = lib.BinaryenStringMeasureWTF8()


@unique
class StringNewOp(IntEnum):
    StringNewFromCodePoint = lib.BinaryenStringNewFromCodePoint()
    StringNewReplace = lib.BinaryenStringNewReplace()
    StringNewReplaceArray = lib.BinaryenStringNewReplaceArray()
    StringNewUTF8 = lib.BinaryenStringNewUTF8()
    StringNewUTF8Array = lib.BinaryenStringNewUTF8Array()
    StringNewWTF16 = lib.BinaryenStringNewWTF16()
    StringNewWTF16Array = lib.BinaryenStringNewWTF16Array()
    StringNewWTF8 = lib.BinaryenStringNewWTF8()
    StringNewWTF8Array = lib.BinaryenStringNewWTF8Array()


@unique
class StringSliceWTFOp(IntEnum):
    StringSliceWTF16 = lib.BinaryenStringSliceWTF16()
    StringSliceWTF8 = lib.BinaryenStringSliceWTF8()


@unique
class UnaryOp(IntEnum):
    AbsFloat32 = lib.BinaryenAbsFloat32()
    AbsFloat64 = lib.BinaryenAbsFloat64()
    AbsVecF32x4 = lib.BinaryenAbsVecF32x4()
    AbsVecF64x2 = lib.BinaryenAbsVecF64x2()
    AbsVecI16x8 = lib.BinaryenAbsVecI16x8()
    AbsVecI32x4 = lib.BinaryenAbsVecI32x4()
    AbsVecI64x2 = lib.BinaryenAbsVecI64x2()
    AbsVecI8x16 = lib.BinaryenAbsVecI8x16()
    AllTrueVecI16x8 = lib.BinaryenAllTrueVecI16x8()
    AllTrueVecI32x4 = lib.BinaryenAllTrueVecI32x4()
    AllTrueVecI64x2 = lib.BinaryenAllTrueVecI64x2()
    AllTrueVecI8x16 = lib.BinaryenAllTrueVecI8x16()
    AnyTrueVec128 = lib.BinaryenAnyTrueVec128()
    BitmaskVecI16x8 = lib.BinaryenBitmaskVecI16x8()
    BitmaskVecI32x4 = lib.BinaryenBitmaskVecI32x4()
    BitmaskVecI64x2 = lib.BinaryenBitmaskVecI64x2()
    BitmaskVecI8x16 = lib.BinaryenBitmaskVecI8x16()
    CeilFloat32 = lib.BinaryenCeilFloat32()
    CeilFloat64 = lib.BinaryenCeilFloat64()
    CeilVecF32x4 = lib.BinaryenCeilVecF32x4()
    CeilVecF64x2 = lib.BinaryenCeilVecF64x2()
    ClzInt32 = lib.BinaryenClzInt32()
    ClzInt64 = lib.BinaryenClzInt64()
    ConvertLowSVecI32x4ToVecF64x2 = lib.BinaryenConvertLowSVecI32x4ToVecF64x2()
    ConvertLowUVecI32x4ToVecF64x2 = lib.BinaryenConvertLowUVecI32x4ToVecF64x2()
    ConvertSInt32ToFloat32 = lib.BinaryenConvertSInt32ToFloat32()
    ConvertSInt32ToFloat64 = lib.BinaryenConvertSInt32ToFloat64()
    ConvertSInt64ToFloat32 = lib.BinaryenConvertSInt64ToFloat32()
    ConvertSInt64ToFloat64 = lib.BinaryenConvertSInt64ToFloat64()
    ConvertSVecI32x4ToVecF32x4 = lib.BinaryenConvertSVecI32x4ToVecF32x4()
    ConvertUInt32ToFloat32 = lib.BinaryenConvertUInt32ToFloat32()
    ConvertUInt32ToFloat64 = lib.BinaryenConvertUInt32ToFloat64()
    ConvertUInt64ToFloat32 = lib.BinaryenConvertUInt64ToFloat32()
    ConvertUInt64ToFloat64 = lib.BinaryenConvertUInt64ToFloat64()
    ConvertUVecI32x4ToVecF32x4 = lib.BinaryenConvertUVecI32x4ToVecF32x4()
    CtzInt32 = lib.BinaryenCtzInt32()
    CtzInt64 = lib.BinaryenCtzInt64()
    DemoteFloat64 = lib.BinaryenDemoteFloat64()
    DemoteZeroVecF64x2ToVecF32x4 = lib.BinaryenDemoteZeroVecF64x2ToVecF32x4()
    EqZInt32 = lib.BinaryenEqZInt32()
    EqZInt64 = lib.BinaryenEqZInt64()
    ExtAddPairwiseSVecI16x8ToI32x4 = lib.BinaryenExtAddPairwiseSVecI16x8ToI32x4()
    ExtAddPairwiseSVecI8x16ToI16x8 = lib.BinaryenExtAddPairwiseSVecI8x16ToI16x8()
    ExtAddPairwiseUVecI16x8ToI32x4 = lib.BinaryenExtAddPairwiseUVecI16x8ToI32x4()
    ExtAddPairwiseUVecI8x16ToI16x8 = lib.BinaryenExtAddPairwiseUVecI8x16ToI16x8()
    ExtendHighSVecI16x8ToVecI32x4 = lib.BinaryenExtendHighSVecI16x8ToVecI32x4()
    ExtendHighSVecI32x4ToVecI64x2 = lib.BinaryenExtendHighSVecI32x4ToVecI64x2()
    ExtendHighSVecI8x16ToVecI16x8 = lib.BinaryenExtendHighSVecI8x16ToVecI16x8()
    ExtendHighUVecI16x8ToVecI32x4 = lib.BinaryenExtendHighUVecI16x8ToVecI32x4()
    ExtendHighUVecI32x4ToVecI64x2 = lib.BinaryenExtendHighUVecI32x4ToVecI64x2()
    ExtendHighUVecI8x16ToVecI16x8 = lib.BinaryenExtendHighUVecI8x16ToVecI16x8()
    ExtendLowSVecI16x8ToVecI32x4 = lib.BinaryenExtendLowSVecI16x8ToVecI32x4()
    ExtendLowSVecI32x4ToVecI64x2 = lib.BinaryenExtendLowSVecI32x4ToVecI64x2()
    ExtendLowSVecI8x16ToVecI16x8 = lib.BinaryenExtendLowSVecI8x16ToVecI16x8()
    ExtendLowUVecI16x8ToVecI32x4 = lib.BinaryenExtendLowUVecI16x8ToVecI32x4()
    ExtendLowUVecI32x4ToVecI64x2 = lib.BinaryenExtendLowUVecI32x4ToVecI64x2()
    ExtendLowUVecI8x16ToVecI16x8 = lib.BinaryenExtendLowUVecI8x16ToVecI16x8()
    ExtendS16Int32 = lib.BinaryenExtendS16Int32()
    ExtendS16Int64 = lib.BinaryenExtendS16Int64()
    ExtendS32Int64 = lib.BinaryenExtendS32Int64()
    ExtendS8Int32 = lib.BinaryenExtendS8Int32()
    ExtendS8Int64 = lib.BinaryenExtendS8Int64()
    ExtendSInt32 = lib.BinaryenExtendSInt32()
    ExtendUInt32 = lib.BinaryenExtendUInt32()
    FloorFloat32 = lib.BinaryenFloorFloat32()
    FloorFloat64 = lib.BinaryenFloorFloat64()
    FloorVecF32x4 = lib.BinaryenFloorVecF32x4()
    FloorVecF64x2 = lib.BinaryenFloorVecF64x2()
    NearestFloat32 = lib.BinaryenNearestFloat32()
    NearestFloat64 = lib.BinaryenNearestFloat64()
    NearestVecF32x4 = lib.BinaryenNearestVecF32x4()
    NearestVecF64x2 = lib.BinaryenNearestVecF64x2()
    NegFloat32 = lib.BinaryenNegFloat32()
    NegFloat64 = lib.BinaryenNegFloat64()
    NegVecF32x4 = lib.BinaryenNegVecF32x4()
    NegVecF64x2 = lib.BinaryenNegVecF64x2()
    NegVecI16x8 = lib.BinaryenNegVecI16x8()
    NegVecI32x4 = lib.BinaryenNegVecI32x4()
    NegVecI64x2 = lib.BinaryenNegVecI64x2()
    NegVecI8x16 = lib.BinaryenNegVecI8x16()
    NotVec128 = lib.BinaryenNotVec128()
    PopcntInt32 = lib.BinaryenPopcntInt32()
    PopcntInt64 = lib.BinaryenPopcntInt64()
    PopcntVecI8x16 = lib.BinaryenPopcntVecI8x16()
    PromoteFloat32 = lib.BinaryenPromoteFloat32()
    PromoteLowVecF32x4ToVecF64x2 = lib.BinaryenPromoteLowVecF32x4ToVecF64x2()
    ReinterpretFloat32 = lib.BinaryenReinterpretFloat32()
    ReinterpretFloat64 = lib.BinaryenReinterpretFloat64()
    ReinterpretInt32 = lib.BinaryenReinterpretInt32()
    ReinterpretInt64 = lib.BinaryenReinterpretInt64()
    RelaxedTruncSVecF32x4ToVecI32x4 = lib.BinaryenRelaxedTruncSVecF32x4ToVecI32x4()
    RelaxedTruncUVecF32x4ToVecI32x4 = lib.BinaryenRelaxedTruncUVecF32x4ToVecI32x4()
    RelaxedTruncZeroSVecF64x2ToVecI32x4 = lib.BinaryenRelaxedTruncZeroSVecF64x2ToVecI32x4()
    RelaxedTruncZeroUVecF64x2ToVecI32x4 = lib.BinaryenRelaxedTruncZeroUVecF64x2ToVecI32x4()
    SplatVecF32x4 = lib.BinaryenSplatVecF32x4()
    SplatVecF64x2 = lib.BinaryenSplatVecF64x2()
    SplatVecI16x8 = lib.BinaryenSplatVecI16x8()
    SplatVecI32x4 = lib.BinaryenSplatVecI32x4()
    SplatVecI64x2 = lib.BinaryenSplatVecI64x2()
    SplatVecI8x16 = lib.BinaryenSplatVecI8x16()
    SqrtFloat32 = lib.BinaryenSqrtFloat32()
    SqrtFloat64 = lib.BinaryenSqrtFloat64()
    SqrtVecF32x4 = lib.BinaryenSqrtVecF32x4()
    SqrtVecF64x2 = lib.BinaryenSqrtVecF64x2()
    TruncFloat32 = lib.BinaryenTruncFloat32()
    TruncFloat64 = lib.BinaryenTruncFloat64()
    TruncSFloat32ToInt32 = lib.BinaryenTruncSFloat32ToInt32()
    TruncSFloat32ToInt64 = lib.BinaryenTruncSFloat32ToInt64()
    TruncSFloat64ToInt32 = lib.BinaryenTruncSFloat64ToInt32()
    TruncSFloat64ToInt64 = lib.BinaryenTruncSFloat64ToInt64()
    TruncSatSFloat32ToInt32 = lib.BinaryenTruncSatSFloat32ToInt32()
    TruncSatSFloat32ToInt64 = lib.BinaryenTruncSatSFloat32ToInt64()
    TruncSatSFloat64ToInt32 = lib.BinaryenTruncSatSFloat64ToInt32()
    TruncSatSFloat64ToInt64 = lib.BinaryenTruncSatSFloat64ToInt64()
    TruncSatSVecF32x4ToVecI32x4 = lib.BinaryenTruncSatSVecF32x4ToVecI32x4()
    TruncSatUFloat32ToInt32 = lib.BinaryenTruncSatUFloat32ToInt32()
    TruncSatUFloat32ToInt64 = lib.BinaryenTruncSatUFloat32ToInt64()
    TruncSatUFloat64ToInt32 = lib.BinaryenTruncSatUFloat64ToInt32()
    TruncSatUFloat64ToInt64 = lib.BinaryenTruncSatUFloat64ToInt64()
    TruncSatUVecF32x4ToVecI32x4 = lib.BinaryenTruncSatUVecF32x4ToVecI32x4()
    TruncSatZeroSVecF64x2ToVecI32x4 = lib.BinaryenTruncSatZeroSVecF64x2ToVecI32x4()
    TruncSatZeroUVecF64x2ToVecI32x4 = lib.BinaryenTruncSatZeroUVecF64x2ToVecI32x4()
    TruncUFloat32ToInt32 = lib.BinaryenTruncUFloat32ToInt32()
    TruncUFloat32ToInt64 = lib.BinaryenTruncUFloat32ToInt64()
    TruncUFloat64ToInt32 = lib.BinaryenTruncUFloat64ToInt32()
    TruncUFloat64ToInt64 = lib.BinaryenTruncUFloat64ToInt64()
    TruncVecF32x4 = lib.BinaryenTruncVecF32x4()
    TruncVecF64x2 = lib.BinaryenTruncVecF64x2()
    WrapInt64 = lib.BinaryenWrapInt64()
