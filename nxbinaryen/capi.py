# Auto-generated from binaryen-c.h
from nxbinaryen._binaryen_capi import ffi, lib
from typing import List, Any


BinaryenType = Any
BinaryenHeapType = BinaryenPackedType = BinaryenBasicHeapType = Any
BinaryenIndex = BinaryenOp = Any
BinaryenModuleAllocateAndWriteResult = Any
BinaryenTypeSystem = BinaryenBufferSizes = Any
BinaryenExpressionId = BinaryenExternalKind = BinaryenFeatures = BinaryenSideEffects = Any
BinaryenLiteral = Any
BinaryenModuleRef = BinaryenExpressionRef = TypeBuilderRef = BinaryenGlobalRef = BinaryenTagRef = Any
BinaryenTableRef = BinaryenFunctionRef = BinaryenExportRef = BinaryenElementSegmentRef = Any
RelooperRef = RelooperBlockRef = Any
TypeBuilderErrorReason = Any
ExpressionRunnerFlags = ExpressionRunnerRef = Any


def TypeNone() -> BinaryenType:
    return lib.BinaryenTypeNone()


def TypeInt32() -> BinaryenType:
    return lib.BinaryenTypeInt32()


def TypeInt64() -> BinaryenType:
    return lib.BinaryenTypeInt64()


def TypeFloat32() -> BinaryenType:
    return lib.BinaryenTypeFloat32()


def TypeFloat64() -> BinaryenType:
    return lib.BinaryenTypeFloat64()


def TypeVec128() -> BinaryenType:
    return lib.BinaryenTypeVec128()


def TypeFuncref() -> BinaryenType:
    return lib.BinaryenTypeFuncref()


def TypeExternref() -> BinaryenType:
    return lib.BinaryenTypeExternref()


def TypeAnyref() -> BinaryenType:
    return lib.BinaryenTypeAnyref()


def TypeEqref() -> BinaryenType:
    return lib.BinaryenTypeEqref()


def TypeI31ref() -> BinaryenType:
    return lib.BinaryenTypeI31ref()


def TypeDataref() -> BinaryenType:
    return lib.BinaryenTypeDataref()


def TypeArrayref() -> BinaryenType:
    return lib.BinaryenTypeArrayref()


def TypeStringref() -> BinaryenType:
    return lib.BinaryenTypeStringref()


def TypeStringviewWTF8() -> BinaryenType:
    return lib.BinaryenTypeStringviewWTF8()


def TypeStringviewWTF16() -> BinaryenType:
    return lib.BinaryenTypeStringviewWTF16()


def TypeStringviewIter() -> BinaryenType:
    return lib.BinaryenTypeStringviewIter()


def TypeNullref() -> BinaryenType:
    return lib.BinaryenTypeNullref()


def TypeNullExternref() -> BinaryenType:
    return lib.BinaryenTypeNullExternref()


def TypeNullFuncref() -> BinaryenType:
    return lib.BinaryenTypeNullFuncref()


def TypeUnreachable() -> BinaryenType:
    return lib.BinaryenTypeUnreachable()


def TypeAuto() -> BinaryenType:
    """
    Not a real type. Used as the last parameter to BinaryenBlock to let
    the API figure out the type instead of providing one.
    """
    return lib.BinaryenTypeAuto()


def TypeCreate(
    value_types: List[BinaryenType],
) -> BinaryenType:
    return lib.BinaryenTypeCreate(value_types, len(value_types))


def TypeArity(
    t: BinaryenType,
) -> int:
    return lib.BinaryenTypeArity(t)


def TypeExpand(
    t: BinaryenType,
    buf: List[BinaryenType],
) -> None:
    lib.BinaryenTypeExpand(t, buf)


def PackedTypeNotPacked() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeNotPacked()


def PackedTypeInt8() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeInt8()


def PackedTypeInt16() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeInt16()


def HeapTypeExt() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeExt()


def HeapTypeFunc() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeFunc()


def HeapTypeAny() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeAny()


def HeapTypeEq() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeEq()


def HeapTypeI31() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeI31()


def HeapTypeData() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeData()


def HeapTypeArray() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeArray()


def HeapTypeString() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeString()


def HeapTypeStringviewWTF8() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewWTF8()


def HeapTypeStringviewWTF16() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewWTF16()


def HeapTypeStringviewIter() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewIter()


def HeapTypeNone() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNone()


def HeapTypeNoext() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNoext()


def HeapTypeNofunc() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNofunc()


def HeapTypeIsBasic(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsBasic(heap_type)


def HeapTypeIsSignature(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsSignature(heap_type)


def HeapTypeIsStruct(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsStruct(heap_type)


def HeapTypeIsArray(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsArray(heap_type)


def HeapTypeIsBottom(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsBottom(heap_type)


def HeapTypeGetBottom(
    heap_type: BinaryenHeapType,
) -> BinaryenHeapType:
    return lib.BinaryenHeapTypeGetBottom(heap_type)


def HeapTypeIsSubType(
    left: BinaryenHeapType,
    right: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsSubType(left, right)


def StructTypeGetNumFields(
    heap_type: BinaryenHeapType,
) -> BinaryenIndex:
    return lib.BinaryenStructTypeGetNumFields(heap_type)


def StructTypeGetFieldType(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> BinaryenType:
    return lib.BinaryenStructTypeGetFieldType(heap_type, index)


def StructTypeGetFieldPackedType(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> BinaryenPackedType:
    return lib.BinaryenStructTypeGetFieldPackedType(heap_type, index)


def StructTypeIsFieldMutable(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> bool:
    return lib.BinaryenStructTypeIsFieldMutable(heap_type, index)


def ArrayTypeGetElementType(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenArrayTypeGetElementType(heap_type)


def ArrayTypeGetElementPackedType(
    heap_type: BinaryenHeapType,
) -> BinaryenPackedType:
    return lib.BinaryenArrayTypeGetElementPackedType(heap_type)


def ArrayTypeIsElementMutable(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenArrayTypeIsElementMutable(heap_type)


def SignatureTypeGetParams(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenSignatureTypeGetParams(heap_type)


def SignatureTypeGetResults(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenSignatureTypeGetResults(heap_type)


def TypeGetHeapType(
    _type: BinaryenType,
) -> BinaryenHeapType:
    return lib.BinaryenTypeGetHeapType(_type)


def TypeIsNullable(
    _type: BinaryenType,
) -> bool:
    return lib.BinaryenTypeIsNullable(_type)


def TypeFromHeapType(
    heap_type: BinaryenHeapType,
    nullable: bool,
) -> BinaryenType:
    return lib.BinaryenTypeFromHeapType(heap_type, nullable)


def TypeSystemEquirecursive() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemEquirecursive()


def TypeSystemNominal() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemNominal()


def TypeSystemIsorecursive() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemIsorecursive()


def GetTypeSystem() -> BinaryenTypeSystem:
    return lib.BinaryenGetTypeSystem()


def SetTypeSystem(
    type_system: BinaryenTypeSystem,
) -> None:
    lib.BinaryenSetTypeSystem(type_system)


def InvalidId() -> BinaryenExpressionId:
    return lib.BinaryenInvalidId()


def NopId() -> BinaryenExpressionId:
    return lib.BinaryenNopId()


def BlockId() -> BinaryenExpressionId:
    return lib.BinaryenBlockId()


def IfId() -> BinaryenExpressionId:
    return lib.BinaryenIfId()


def LoopId() -> BinaryenExpressionId:
    return lib.BinaryenLoopId()


def BreakId() -> BinaryenExpressionId:
    return lib.BinaryenBreakId()


def SwitchId() -> BinaryenExpressionId:
    return lib.BinaryenSwitchId()


def CallId() -> BinaryenExpressionId:
    return lib.BinaryenCallId()


def CallIndirectId() -> BinaryenExpressionId:
    return lib.BinaryenCallIndirectId()


def LocalGetId() -> BinaryenExpressionId:
    return lib.BinaryenLocalGetId()


def LocalSetId() -> BinaryenExpressionId:
    return lib.BinaryenLocalSetId()


def GlobalGetId() -> BinaryenExpressionId:
    return lib.BinaryenGlobalGetId()


def GlobalSetId() -> BinaryenExpressionId:
    return lib.BinaryenGlobalSetId()


def LoadId() -> BinaryenExpressionId:
    return lib.BinaryenLoadId()


def StoreId() -> BinaryenExpressionId:
    return lib.BinaryenStoreId()


def AtomicRMWId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicRMWId()


def AtomicCmpxchgId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicCmpxchgId()


def AtomicWaitId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicWaitId()


def AtomicNotifyId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicNotifyId()


def AtomicFenceId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicFenceId()


def SIMDExtractId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDExtractId()


def SIMDReplaceId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDReplaceId()


def SIMDShuffleId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDShuffleId()


def SIMDTernaryId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDTernaryId()


def SIMDShiftId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDShiftId()


def SIMDLoadId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDLoadId()


def SIMDLoadStoreLaneId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDLoadStoreLaneId()


def MemoryInitId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryInitId()


def DataDropId() -> BinaryenExpressionId:
    return lib.BinaryenDataDropId()


def MemoryCopyId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryCopyId()


def MemoryFillId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryFillId()


def ConstId() -> BinaryenExpressionId:
    return lib.BinaryenConstId()


def UnaryId() -> BinaryenExpressionId:
    return lib.BinaryenUnaryId()


def BinaryId() -> BinaryenExpressionId:
    return lib.BinaryenBinaryId()


def SelectId() -> BinaryenExpressionId:
    return lib.BinaryenSelectId()


def DropId() -> BinaryenExpressionId:
    return lib.BinaryenDropId()


def ReturnId() -> BinaryenExpressionId:
    return lib.BinaryenReturnId()


def MemorySizeId() -> BinaryenExpressionId:
    return lib.BinaryenMemorySizeId()


def MemoryGrowId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryGrowId()


def UnreachableId() -> BinaryenExpressionId:
    return lib.BinaryenUnreachableId()


def PopId() -> BinaryenExpressionId:
    return lib.BinaryenPopId()


def RefNullId() -> BinaryenExpressionId:
    return lib.BinaryenRefNullId()


def RefIsId() -> BinaryenExpressionId:
    return lib.BinaryenRefIsId()


def RefFuncId() -> BinaryenExpressionId:
    return lib.BinaryenRefFuncId()


def RefEqId() -> BinaryenExpressionId:
    return lib.BinaryenRefEqId()


def TableGetId() -> BinaryenExpressionId:
    return lib.BinaryenTableGetId()


def TableSetId() -> BinaryenExpressionId:
    return lib.BinaryenTableSetId()


def TableSizeId() -> BinaryenExpressionId:
    return lib.BinaryenTableSizeId()


def TableGrowId() -> BinaryenExpressionId:
    return lib.BinaryenTableGrowId()


def TryId() -> BinaryenExpressionId:
    return lib.BinaryenTryId()


def ThrowId() -> BinaryenExpressionId:
    return lib.BinaryenThrowId()


def RethrowId() -> BinaryenExpressionId:
    return lib.BinaryenRethrowId()


def TupleMakeId() -> BinaryenExpressionId:
    return lib.BinaryenTupleMakeId()


def TupleExtractId() -> BinaryenExpressionId:
    return lib.BinaryenTupleExtractId()


def I31NewId() -> BinaryenExpressionId:
    return lib.BinaryenI31NewId()


def I31GetId() -> BinaryenExpressionId:
    return lib.BinaryenI31GetId()


def CallRefId() -> BinaryenExpressionId:
    return lib.BinaryenCallRefId()


def RefTestId() -> BinaryenExpressionId:
    return lib.BinaryenRefTestId()


def RefCastId() -> BinaryenExpressionId:
    return lib.BinaryenRefCastId()


def BrOnId() -> BinaryenExpressionId:
    return lib.BinaryenBrOnId()


def StructNewId() -> BinaryenExpressionId:
    return lib.BinaryenStructNewId()


def StructGetId() -> BinaryenExpressionId:
    return lib.BinaryenStructGetId()


def StructSetId() -> BinaryenExpressionId:
    return lib.BinaryenStructSetId()


def ArrayNewId() -> BinaryenExpressionId:
    return lib.BinaryenArrayNewId()


def ArrayNewSegId() -> BinaryenExpressionId:
    return lib.BinaryenArrayNewSegId()


def ArrayInitId() -> BinaryenExpressionId:
    return lib.BinaryenArrayInitId()


def ArrayGetId() -> BinaryenExpressionId:
    return lib.BinaryenArrayGetId()


def ArraySetId() -> BinaryenExpressionId:
    return lib.BinaryenArraySetId()


def ArrayLenId() -> BinaryenExpressionId:
    return lib.BinaryenArrayLenId()


def ArrayCopyId() -> BinaryenExpressionId:
    return lib.BinaryenArrayCopyId()


def RefAsId() -> BinaryenExpressionId:
    return lib.BinaryenRefAsId()


def StringNewId() -> BinaryenExpressionId:
    return lib.BinaryenStringNewId()


def StringConstId() -> BinaryenExpressionId:
    return lib.BinaryenStringConstId()


def StringMeasureId() -> BinaryenExpressionId:
    return lib.BinaryenStringMeasureId()


def StringEncodeId() -> BinaryenExpressionId:
    return lib.BinaryenStringEncodeId()


def StringConcatId() -> BinaryenExpressionId:
    return lib.BinaryenStringConcatId()


def StringEqId() -> BinaryenExpressionId:
    return lib.BinaryenStringEqId()


def StringAsId() -> BinaryenExpressionId:
    return lib.BinaryenStringAsId()


def StringWTF8AdvanceId() -> BinaryenExpressionId:
    return lib.BinaryenStringWTF8AdvanceId()


def StringWTF16GetId() -> BinaryenExpressionId:
    return lib.BinaryenStringWTF16GetId()


def StringIterNextId() -> BinaryenExpressionId:
    return lib.BinaryenStringIterNextId()


def StringIterMoveId() -> BinaryenExpressionId:
    return lib.BinaryenStringIterMoveId()


def StringSliceWTFId() -> BinaryenExpressionId:
    return lib.BinaryenStringSliceWTFId()


def StringSliceIterId() -> BinaryenExpressionId:
    return lib.BinaryenStringSliceIterId()


def ExternalFunction() -> BinaryenExternalKind:
    return lib.BinaryenExternalFunction()


def ExternalTable() -> BinaryenExternalKind:
    return lib.BinaryenExternalTable()


def ExternalMemory() -> BinaryenExternalKind:
    return lib.BinaryenExternalMemory()


def ExternalGlobal() -> BinaryenExternalKind:
    return lib.BinaryenExternalGlobal()


def ExternalTag() -> BinaryenExternalKind:
    return lib.BinaryenExternalTag()


def FeatureMVP() -> BinaryenFeatures:
    return lib.BinaryenFeatureMVP()


def FeatureAtomics() -> BinaryenFeatures:
    return lib.BinaryenFeatureAtomics()


def FeatureBulkMemory() -> BinaryenFeatures:
    return lib.BinaryenFeatureBulkMemory()


def FeatureMutableGlobals() -> BinaryenFeatures:
    return lib.BinaryenFeatureMutableGlobals()


def FeatureNontrappingFPToInt() -> BinaryenFeatures:
    return lib.BinaryenFeatureNontrappingFPToInt()


def FeatureSignExt() -> BinaryenFeatures:
    return lib.BinaryenFeatureSignExt()


def FeatureSIMD128() -> BinaryenFeatures:
    return lib.BinaryenFeatureSIMD128()


def FeatureExceptionHandling() -> BinaryenFeatures:
    return lib.BinaryenFeatureExceptionHandling()


def FeatureTailCall() -> BinaryenFeatures:
    return lib.BinaryenFeatureTailCall()


def FeatureReferenceTypes() -> BinaryenFeatures:
    return lib.BinaryenFeatureReferenceTypes()


def FeatureMultivalue() -> BinaryenFeatures:
    return lib.BinaryenFeatureMultivalue()


def FeatureGC() -> BinaryenFeatures:
    return lib.BinaryenFeatureGC()


def FeatureMemory64() -> BinaryenFeatures:
    return lib.BinaryenFeatureMemory64()


def FeatureRelaxedSIMD() -> BinaryenFeatures:
    return lib.BinaryenFeatureRelaxedSIMD()


def FeatureExtendedConst() -> BinaryenFeatures:
    return lib.BinaryenFeatureExtendedConst()


def FeatureStrings() -> BinaryenFeatures:
    return lib.BinaryenFeatureStrings()


def FeatureMultiMemories() -> BinaryenFeatures:
    return lib.BinaryenFeatureMultiMemories()


def FeatureAll() -> BinaryenFeatures:
    return lib.BinaryenFeatureAll()


def ModuleCreate() -> BinaryenModuleRef:
    return lib.BinaryenModuleCreate()


def ModuleDispose(
    module: BinaryenModuleRef,
) -> None:
    lib.BinaryenModuleDispose(module)


def LiteralInt32(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralInt32(x)


def LiteralInt64(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralInt64(x)


def LiteralFloat32(
    x: float,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat32(x)


def LiteralFloat64(
    x: float,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat64(x)


def LiteralVec128(
    x: List[int],
) -> BinaryenLiteral:
    return lib.BinaryenLiteralVec128(x)


def LiteralFloat32Bits(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat32Bits(x)


def LiteralFloat64Bits(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat64Bits(x)


def ClzInt32() -> BinaryenOp:
    return lib.BinaryenClzInt32()


def CtzInt32() -> BinaryenOp:
    return lib.BinaryenCtzInt32()


def PopcntInt32() -> BinaryenOp:
    return lib.BinaryenPopcntInt32()


def NegFloat32() -> BinaryenOp:
    return lib.BinaryenNegFloat32()


def AbsFloat32() -> BinaryenOp:
    return lib.BinaryenAbsFloat32()


def CeilFloat32() -> BinaryenOp:
    return lib.BinaryenCeilFloat32()


def FloorFloat32() -> BinaryenOp:
    return lib.BinaryenFloorFloat32()


def TruncFloat32() -> BinaryenOp:
    return lib.BinaryenTruncFloat32()


def NearestFloat32() -> BinaryenOp:
    return lib.BinaryenNearestFloat32()


def SqrtFloat32() -> BinaryenOp:
    return lib.BinaryenSqrtFloat32()


def EqZInt32() -> BinaryenOp:
    return lib.BinaryenEqZInt32()


def ClzInt64() -> BinaryenOp:
    return lib.BinaryenClzInt64()


def CtzInt64() -> BinaryenOp:
    return lib.BinaryenCtzInt64()


def PopcntInt64() -> BinaryenOp:
    return lib.BinaryenPopcntInt64()


def NegFloat64() -> BinaryenOp:
    return lib.BinaryenNegFloat64()


def AbsFloat64() -> BinaryenOp:
    return lib.BinaryenAbsFloat64()


def CeilFloat64() -> BinaryenOp:
    return lib.BinaryenCeilFloat64()


def FloorFloat64() -> BinaryenOp:
    return lib.BinaryenFloorFloat64()


def TruncFloat64() -> BinaryenOp:
    return lib.BinaryenTruncFloat64()


def NearestFloat64() -> BinaryenOp:
    return lib.BinaryenNearestFloat64()


def SqrtFloat64() -> BinaryenOp:
    return lib.BinaryenSqrtFloat64()


def EqZInt64() -> BinaryenOp:
    return lib.BinaryenEqZInt64()


def ExtendSInt32() -> BinaryenOp:
    return lib.BinaryenExtendSInt32()


def ExtendUInt32() -> BinaryenOp:
    return lib.BinaryenExtendUInt32()


def WrapInt64() -> BinaryenOp:
    return lib.BinaryenWrapInt64()


def TruncSFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSFloat32ToInt32()


def TruncSFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSFloat32ToInt64()


def TruncUFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncUFloat32ToInt32()


def TruncUFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncUFloat32ToInt64()


def TruncSFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSFloat64ToInt32()


def TruncSFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSFloat64ToInt64()


def TruncUFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncUFloat64ToInt32()


def TruncUFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncUFloat64ToInt64()


def ReinterpretFloat32() -> BinaryenOp:
    return lib.BinaryenReinterpretFloat32()


def ReinterpretFloat64() -> BinaryenOp:
    return lib.BinaryenReinterpretFloat64()


def ConvertSInt32ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertSInt32ToFloat32()


def ConvertSInt32ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertSInt32ToFloat64()


def ConvertUInt32ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertUInt32ToFloat32()


def ConvertUInt32ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertUInt32ToFloat64()


def ConvertSInt64ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertSInt64ToFloat32()


def ConvertSInt64ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertSInt64ToFloat64()


def ConvertUInt64ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertUInt64ToFloat32()


def ConvertUInt64ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertUInt64ToFloat64()


def PromoteFloat32() -> BinaryenOp:
    return lib.BinaryenPromoteFloat32()


def DemoteFloat64() -> BinaryenOp:
    return lib.BinaryenDemoteFloat64()


def ReinterpretInt32() -> BinaryenOp:
    return lib.BinaryenReinterpretInt32()


def ReinterpretInt64() -> BinaryenOp:
    return lib.BinaryenReinterpretInt64()


def ExtendS8Int32() -> BinaryenOp:
    return lib.BinaryenExtendS8Int32()


def ExtendS16Int32() -> BinaryenOp:
    return lib.BinaryenExtendS16Int32()


def ExtendS8Int64() -> BinaryenOp:
    return lib.BinaryenExtendS8Int64()


def ExtendS16Int64() -> BinaryenOp:
    return lib.BinaryenExtendS16Int64()


def ExtendS32Int64() -> BinaryenOp:
    return lib.BinaryenExtendS32Int64()


def AddInt32() -> BinaryenOp:
    return lib.BinaryenAddInt32()


def SubInt32() -> BinaryenOp:
    return lib.BinaryenSubInt32()


def MulInt32() -> BinaryenOp:
    return lib.BinaryenMulInt32()


def DivSInt32() -> BinaryenOp:
    return lib.BinaryenDivSInt32()


def DivUInt32() -> BinaryenOp:
    return lib.BinaryenDivUInt32()


def RemSInt32() -> BinaryenOp:
    return lib.BinaryenRemSInt32()


def RemUInt32() -> BinaryenOp:
    return lib.BinaryenRemUInt32()


def AndInt32() -> BinaryenOp:
    return lib.BinaryenAndInt32()


def OrInt32() -> BinaryenOp:
    return lib.BinaryenOrInt32()


def XorInt32() -> BinaryenOp:
    return lib.BinaryenXorInt32()


def ShlInt32() -> BinaryenOp:
    return lib.BinaryenShlInt32()


def ShrUInt32() -> BinaryenOp:
    return lib.BinaryenShrUInt32()


def ShrSInt32() -> BinaryenOp:
    return lib.BinaryenShrSInt32()


def RotLInt32() -> BinaryenOp:
    return lib.BinaryenRotLInt32()


def RotRInt32() -> BinaryenOp:
    return lib.BinaryenRotRInt32()


def EqInt32() -> BinaryenOp:
    return lib.BinaryenEqInt32()


def NeInt32() -> BinaryenOp:
    return lib.BinaryenNeInt32()


def LtSInt32() -> BinaryenOp:
    return lib.BinaryenLtSInt32()


def LtUInt32() -> BinaryenOp:
    return lib.BinaryenLtUInt32()


def LeSInt32() -> BinaryenOp:
    return lib.BinaryenLeSInt32()


def LeUInt32() -> BinaryenOp:
    return lib.BinaryenLeUInt32()


def GtSInt32() -> BinaryenOp:
    return lib.BinaryenGtSInt32()


def GtUInt32() -> BinaryenOp:
    return lib.BinaryenGtUInt32()


def GeSInt32() -> BinaryenOp:
    return lib.BinaryenGeSInt32()


def GeUInt32() -> BinaryenOp:
    return lib.BinaryenGeUInt32()


def AddInt64() -> BinaryenOp:
    return lib.BinaryenAddInt64()


def SubInt64() -> BinaryenOp:
    return lib.BinaryenSubInt64()


def MulInt64() -> BinaryenOp:
    return lib.BinaryenMulInt64()


def DivSInt64() -> BinaryenOp:
    return lib.BinaryenDivSInt64()


def DivUInt64() -> BinaryenOp:
    return lib.BinaryenDivUInt64()


def RemSInt64() -> BinaryenOp:
    return lib.BinaryenRemSInt64()


def RemUInt64() -> BinaryenOp:
    return lib.BinaryenRemUInt64()


def AndInt64() -> BinaryenOp:
    return lib.BinaryenAndInt64()


def OrInt64() -> BinaryenOp:
    return lib.BinaryenOrInt64()


def XorInt64() -> BinaryenOp:
    return lib.BinaryenXorInt64()


def ShlInt64() -> BinaryenOp:
    return lib.BinaryenShlInt64()


def ShrUInt64() -> BinaryenOp:
    return lib.BinaryenShrUInt64()


def ShrSInt64() -> BinaryenOp:
    return lib.BinaryenShrSInt64()


def RotLInt64() -> BinaryenOp:
    return lib.BinaryenRotLInt64()


def RotRInt64() -> BinaryenOp:
    return lib.BinaryenRotRInt64()


def EqInt64() -> BinaryenOp:
    return lib.BinaryenEqInt64()


def NeInt64() -> BinaryenOp:
    return lib.BinaryenNeInt64()


def LtSInt64() -> BinaryenOp:
    return lib.BinaryenLtSInt64()


def LtUInt64() -> BinaryenOp:
    return lib.BinaryenLtUInt64()


def LeSInt64() -> BinaryenOp:
    return lib.BinaryenLeSInt64()


def LeUInt64() -> BinaryenOp:
    return lib.BinaryenLeUInt64()


def GtSInt64() -> BinaryenOp:
    return lib.BinaryenGtSInt64()


def GtUInt64() -> BinaryenOp:
    return lib.BinaryenGtUInt64()


def GeSInt64() -> BinaryenOp:
    return lib.BinaryenGeSInt64()


def GeUInt64() -> BinaryenOp:
    return lib.BinaryenGeUInt64()


def AddFloat32() -> BinaryenOp:
    return lib.BinaryenAddFloat32()


def SubFloat32() -> BinaryenOp:
    return lib.BinaryenSubFloat32()


def MulFloat32() -> BinaryenOp:
    return lib.BinaryenMulFloat32()


def DivFloat32() -> BinaryenOp:
    return lib.BinaryenDivFloat32()


def CopySignFloat32() -> BinaryenOp:
    return lib.BinaryenCopySignFloat32()


def MinFloat32() -> BinaryenOp:
    return lib.BinaryenMinFloat32()


def MaxFloat32() -> BinaryenOp:
    return lib.BinaryenMaxFloat32()


def EqFloat32() -> BinaryenOp:
    return lib.BinaryenEqFloat32()


def NeFloat32() -> BinaryenOp:
    return lib.BinaryenNeFloat32()


def LtFloat32() -> BinaryenOp:
    return lib.BinaryenLtFloat32()


def LeFloat32() -> BinaryenOp:
    return lib.BinaryenLeFloat32()


def GtFloat32() -> BinaryenOp:
    return lib.BinaryenGtFloat32()


def GeFloat32() -> BinaryenOp:
    return lib.BinaryenGeFloat32()


def AddFloat64() -> BinaryenOp:
    return lib.BinaryenAddFloat64()


def SubFloat64() -> BinaryenOp:
    return lib.BinaryenSubFloat64()


def MulFloat64() -> BinaryenOp:
    return lib.BinaryenMulFloat64()


def DivFloat64() -> BinaryenOp:
    return lib.BinaryenDivFloat64()


def CopySignFloat64() -> BinaryenOp:
    return lib.BinaryenCopySignFloat64()


def MinFloat64() -> BinaryenOp:
    return lib.BinaryenMinFloat64()


def MaxFloat64() -> BinaryenOp:
    return lib.BinaryenMaxFloat64()


def EqFloat64() -> BinaryenOp:
    return lib.BinaryenEqFloat64()


def NeFloat64() -> BinaryenOp:
    return lib.BinaryenNeFloat64()


def LtFloat64() -> BinaryenOp:
    return lib.BinaryenLtFloat64()


def LeFloat64() -> BinaryenOp:
    return lib.BinaryenLeFloat64()


def GtFloat64() -> BinaryenOp:
    return lib.BinaryenGtFloat64()


def GeFloat64() -> BinaryenOp:
    return lib.BinaryenGeFloat64()


def AtomicRMWAdd() -> BinaryenOp:
    return lib.BinaryenAtomicRMWAdd()


def AtomicRMWSub() -> BinaryenOp:
    return lib.BinaryenAtomicRMWSub()


def AtomicRMWAnd() -> BinaryenOp:
    return lib.BinaryenAtomicRMWAnd()


def AtomicRMWOr() -> BinaryenOp:
    return lib.BinaryenAtomicRMWOr()


def AtomicRMWXor() -> BinaryenOp:
    return lib.BinaryenAtomicRMWXor()


def AtomicRMWXchg() -> BinaryenOp:
    return lib.BinaryenAtomicRMWXchg()


def TruncSatSFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat32ToInt32()


def TruncSatSFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat32ToInt64()


def TruncSatUFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat32ToInt32()


def TruncSatUFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat32ToInt64()


def TruncSatSFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat64ToInt32()


def TruncSatSFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat64ToInt64()


def TruncSatUFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat64ToInt32()


def TruncSatUFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat64ToInt64()


def SplatVecI8x16() -> BinaryenOp:
    return lib.BinaryenSplatVecI8x16()


def ExtractLaneSVecI8x16() -> BinaryenOp:
    return lib.BinaryenExtractLaneSVecI8x16()


def ExtractLaneUVecI8x16() -> BinaryenOp:
    return lib.BinaryenExtractLaneUVecI8x16()


def ReplaceLaneVecI8x16() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI8x16()


def SplatVecI16x8() -> BinaryenOp:
    return lib.BinaryenSplatVecI16x8()


def ExtractLaneSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtractLaneSVecI16x8()


def ExtractLaneUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtractLaneUVecI16x8()


def ReplaceLaneVecI16x8() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI16x8()


def SplatVecI32x4() -> BinaryenOp:
    return lib.BinaryenSplatVecI32x4()


def ExtractLaneVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecI32x4()


def ReplaceLaneVecI32x4() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI32x4()


def SplatVecI64x2() -> BinaryenOp:
    return lib.BinaryenSplatVecI64x2()


def ExtractLaneVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecI64x2()


def ReplaceLaneVecI64x2() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI64x2()


def SplatVecF32x4() -> BinaryenOp:
    return lib.BinaryenSplatVecF32x4()


def ExtractLaneVecF32x4() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecF32x4()


def ReplaceLaneVecF32x4() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecF32x4()


def SplatVecF64x2() -> BinaryenOp:
    return lib.BinaryenSplatVecF64x2()


def ExtractLaneVecF64x2() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecF64x2()


def ReplaceLaneVecF64x2() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecF64x2()


def EqVecI8x16() -> BinaryenOp:
    return lib.BinaryenEqVecI8x16()


def NeVecI8x16() -> BinaryenOp:
    return lib.BinaryenNeVecI8x16()


def LtSVecI8x16() -> BinaryenOp:
    return lib.BinaryenLtSVecI8x16()


def LtUVecI8x16() -> BinaryenOp:
    return lib.BinaryenLtUVecI8x16()


def GtSVecI8x16() -> BinaryenOp:
    return lib.BinaryenGtSVecI8x16()


def GtUVecI8x16() -> BinaryenOp:
    return lib.BinaryenGtUVecI8x16()


def LeSVecI8x16() -> BinaryenOp:
    return lib.BinaryenLeSVecI8x16()


def LeUVecI8x16() -> BinaryenOp:
    return lib.BinaryenLeUVecI8x16()


def GeSVecI8x16() -> BinaryenOp:
    return lib.BinaryenGeSVecI8x16()


def GeUVecI8x16() -> BinaryenOp:
    return lib.BinaryenGeUVecI8x16()


def EqVecI16x8() -> BinaryenOp:
    return lib.BinaryenEqVecI16x8()


def NeVecI16x8() -> BinaryenOp:
    return lib.BinaryenNeVecI16x8()


def LtSVecI16x8() -> BinaryenOp:
    return lib.BinaryenLtSVecI16x8()


def LtUVecI16x8() -> BinaryenOp:
    return lib.BinaryenLtUVecI16x8()


def GtSVecI16x8() -> BinaryenOp:
    return lib.BinaryenGtSVecI16x8()


def GtUVecI16x8() -> BinaryenOp:
    return lib.BinaryenGtUVecI16x8()


def LeSVecI16x8() -> BinaryenOp:
    return lib.BinaryenLeSVecI16x8()


def LeUVecI16x8() -> BinaryenOp:
    return lib.BinaryenLeUVecI16x8()


def GeSVecI16x8() -> BinaryenOp:
    return lib.BinaryenGeSVecI16x8()


def GeUVecI16x8() -> BinaryenOp:
    return lib.BinaryenGeUVecI16x8()


def EqVecI32x4() -> BinaryenOp:
    return lib.BinaryenEqVecI32x4()


def NeVecI32x4() -> BinaryenOp:
    return lib.BinaryenNeVecI32x4()


def LtSVecI32x4() -> BinaryenOp:
    return lib.BinaryenLtSVecI32x4()


def LtUVecI32x4() -> BinaryenOp:
    return lib.BinaryenLtUVecI32x4()


def GtSVecI32x4() -> BinaryenOp:
    return lib.BinaryenGtSVecI32x4()


def GtUVecI32x4() -> BinaryenOp:
    return lib.BinaryenGtUVecI32x4()


def LeSVecI32x4() -> BinaryenOp:
    return lib.BinaryenLeSVecI32x4()


def LeUVecI32x4() -> BinaryenOp:
    return lib.BinaryenLeUVecI32x4()


def GeSVecI32x4() -> BinaryenOp:
    return lib.BinaryenGeSVecI32x4()


def GeUVecI32x4() -> BinaryenOp:
    return lib.BinaryenGeUVecI32x4()


def EqVecI64x2() -> BinaryenOp:
    return lib.BinaryenEqVecI64x2()


def NeVecI64x2() -> BinaryenOp:
    return lib.BinaryenNeVecI64x2()


def LtSVecI64x2() -> BinaryenOp:
    return lib.BinaryenLtSVecI64x2()


def GtSVecI64x2() -> BinaryenOp:
    return lib.BinaryenGtSVecI64x2()


def LeSVecI64x2() -> BinaryenOp:
    return lib.BinaryenLeSVecI64x2()


def GeSVecI64x2() -> BinaryenOp:
    return lib.BinaryenGeSVecI64x2()


def EqVecF32x4() -> BinaryenOp:
    return lib.BinaryenEqVecF32x4()


def NeVecF32x4() -> BinaryenOp:
    return lib.BinaryenNeVecF32x4()


def LtVecF32x4() -> BinaryenOp:
    return lib.BinaryenLtVecF32x4()


def GtVecF32x4() -> BinaryenOp:
    return lib.BinaryenGtVecF32x4()


def LeVecF32x4() -> BinaryenOp:
    return lib.BinaryenLeVecF32x4()


def GeVecF32x4() -> BinaryenOp:
    return lib.BinaryenGeVecF32x4()


def EqVecF64x2() -> BinaryenOp:
    return lib.BinaryenEqVecF64x2()


def NeVecF64x2() -> BinaryenOp:
    return lib.BinaryenNeVecF64x2()


def LtVecF64x2() -> BinaryenOp:
    return lib.BinaryenLtVecF64x2()


def GtVecF64x2() -> BinaryenOp:
    return lib.BinaryenGtVecF64x2()


def LeVecF64x2() -> BinaryenOp:
    return lib.BinaryenLeVecF64x2()


def GeVecF64x2() -> BinaryenOp:
    return lib.BinaryenGeVecF64x2()


def NotVec128() -> BinaryenOp:
    return lib.BinaryenNotVec128()


def AndVec128() -> BinaryenOp:
    return lib.BinaryenAndVec128()


def OrVec128() -> BinaryenOp:
    return lib.BinaryenOrVec128()


def XorVec128() -> BinaryenOp:
    return lib.BinaryenXorVec128()


def AndNotVec128() -> BinaryenOp:
    return lib.BinaryenAndNotVec128()


def BitselectVec128() -> BinaryenOp:
    return lib.BinaryenBitselectVec128()


def AnyTrueVec128() -> BinaryenOp:
    return lib.BinaryenAnyTrueVec128()


def PopcntVecI8x16() -> BinaryenOp:
    return lib.BinaryenPopcntVecI8x16()


def AbsVecI8x16() -> BinaryenOp:
    return lib.BinaryenAbsVecI8x16()


def NegVecI8x16() -> BinaryenOp:
    return lib.BinaryenNegVecI8x16()


def AllTrueVecI8x16() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI8x16()


def BitmaskVecI8x16() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI8x16()


def ShlVecI8x16() -> BinaryenOp:
    return lib.BinaryenShlVecI8x16()


def ShrSVecI8x16() -> BinaryenOp:
    return lib.BinaryenShrSVecI8x16()


def ShrUVecI8x16() -> BinaryenOp:
    return lib.BinaryenShrUVecI8x16()


def AddVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddVecI8x16()


def AddSatSVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddSatSVecI8x16()


def AddSatUVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddSatUVecI8x16()


def SubVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubVecI8x16()


def SubSatSVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubSatSVecI8x16()


def SubSatUVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubSatUVecI8x16()


def MinSVecI8x16() -> BinaryenOp:
    return lib.BinaryenMinSVecI8x16()


def MinUVecI8x16() -> BinaryenOp:
    return lib.BinaryenMinUVecI8x16()


def MaxSVecI8x16() -> BinaryenOp:
    return lib.BinaryenMaxSVecI8x16()


def MaxUVecI8x16() -> BinaryenOp:
    return lib.BinaryenMaxUVecI8x16()


def AvgrUVecI8x16() -> BinaryenOp:
    return lib.BinaryenAvgrUVecI8x16()


def AbsVecI16x8() -> BinaryenOp:
    return lib.BinaryenAbsVecI16x8()


def NegVecI16x8() -> BinaryenOp:
    return lib.BinaryenNegVecI16x8()


def AllTrueVecI16x8() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI16x8()


def BitmaskVecI16x8() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI16x8()


def ShlVecI16x8() -> BinaryenOp:
    return lib.BinaryenShlVecI16x8()


def ShrSVecI16x8() -> BinaryenOp:
    return lib.BinaryenShrSVecI16x8()


def ShrUVecI16x8() -> BinaryenOp:
    return lib.BinaryenShrUVecI16x8()


def AddVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddVecI16x8()


def AddSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddSatSVecI16x8()


def AddSatUVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddSatUVecI16x8()


def SubVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubVecI16x8()


def SubSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubSatSVecI16x8()


def SubSatUVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubSatUVecI16x8()


def MulVecI16x8() -> BinaryenOp:
    return lib.BinaryenMulVecI16x8()


def MinSVecI16x8() -> BinaryenOp:
    return lib.BinaryenMinSVecI16x8()


def MinUVecI16x8() -> BinaryenOp:
    return lib.BinaryenMinUVecI16x8()


def MaxSVecI16x8() -> BinaryenOp:
    return lib.BinaryenMaxSVecI16x8()


def MaxUVecI16x8() -> BinaryenOp:
    return lib.BinaryenMaxUVecI16x8()


def AvgrUVecI16x8() -> BinaryenOp:
    return lib.BinaryenAvgrUVecI16x8()


def Q15MulrSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenQ15MulrSatSVecI16x8()


def ExtMulLowSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI16x8()


def ExtMulHighSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI16x8()


def ExtMulLowUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI16x8()


def ExtMulHighUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI16x8()


def AbsVecI32x4() -> BinaryenOp:
    return lib.BinaryenAbsVecI32x4()


def NegVecI32x4() -> BinaryenOp:
    return lib.BinaryenNegVecI32x4()


def AllTrueVecI32x4() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI32x4()


def BitmaskVecI32x4() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI32x4()


def ShlVecI32x4() -> BinaryenOp:
    return lib.BinaryenShlVecI32x4()


def ShrSVecI32x4() -> BinaryenOp:
    return lib.BinaryenShrSVecI32x4()


def ShrUVecI32x4() -> BinaryenOp:
    return lib.BinaryenShrUVecI32x4()


def AddVecI32x4() -> BinaryenOp:
    return lib.BinaryenAddVecI32x4()


def SubVecI32x4() -> BinaryenOp:
    return lib.BinaryenSubVecI32x4()


def MulVecI32x4() -> BinaryenOp:
    return lib.BinaryenMulVecI32x4()


def MinSVecI32x4() -> BinaryenOp:
    return lib.BinaryenMinSVecI32x4()


def MinUVecI32x4() -> BinaryenOp:
    return lib.BinaryenMinUVecI32x4()


def MaxSVecI32x4() -> BinaryenOp:
    return lib.BinaryenMaxSVecI32x4()


def MaxUVecI32x4() -> BinaryenOp:
    return lib.BinaryenMaxUVecI32x4()


def DotSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenDotSVecI16x8ToVecI32x4()


def ExtMulLowSVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI32x4()


def ExtMulHighSVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI32x4()


def ExtMulLowUVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI32x4()


def ExtMulHighUVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI32x4()


def AbsVecI64x2() -> BinaryenOp:
    return lib.BinaryenAbsVecI64x2()


def NegVecI64x2() -> BinaryenOp:
    return lib.BinaryenNegVecI64x2()


def AllTrueVecI64x2() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI64x2()


def BitmaskVecI64x2() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI64x2()


def ShlVecI64x2() -> BinaryenOp:
    return lib.BinaryenShlVecI64x2()


def ShrSVecI64x2() -> BinaryenOp:
    return lib.BinaryenShrSVecI64x2()


def ShrUVecI64x2() -> BinaryenOp:
    return lib.BinaryenShrUVecI64x2()


def AddVecI64x2() -> BinaryenOp:
    return lib.BinaryenAddVecI64x2()


def SubVecI64x2() -> BinaryenOp:
    return lib.BinaryenSubVecI64x2()


def MulVecI64x2() -> BinaryenOp:
    return lib.BinaryenMulVecI64x2()


def ExtMulLowSVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI64x2()


def ExtMulHighSVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI64x2()


def ExtMulLowUVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI64x2()


def ExtMulHighUVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI64x2()


def AbsVecF32x4() -> BinaryenOp:
    return lib.BinaryenAbsVecF32x4()


def NegVecF32x4() -> BinaryenOp:
    return lib.BinaryenNegVecF32x4()


def SqrtVecF32x4() -> BinaryenOp:
    return lib.BinaryenSqrtVecF32x4()


def AddVecF32x4() -> BinaryenOp:
    return lib.BinaryenAddVecF32x4()


def SubVecF32x4() -> BinaryenOp:
    return lib.BinaryenSubVecF32x4()


def MulVecF32x4() -> BinaryenOp:
    return lib.BinaryenMulVecF32x4()


def DivVecF32x4() -> BinaryenOp:
    return lib.BinaryenDivVecF32x4()


def MinVecF32x4() -> BinaryenOp:
    return lib.BinaryenMinVecF32x4()


def MaxVecF32x4() -> BinaryenOp:
    return lib.BinaryenMaxVecF32x4()


def PMinVecF32x4() -> BinaryenOp:
    return lib.BinaryenPMinVecF32x4()


def PMaxVecF32x4() -> BinaryenOp:
    return lib.BinaryenPMaxVecF32x4()


def CeilVecF32x4() -> BinaryenOp:
    return lib.BinaryenCeilVecF32x4()


def FloorVecF32x4() -> BinaryenOp:
    return lib.BinaryenFloorVecF32x4()


def TruncVecF32x4() -> BinaryenOp:
    return lib.BinaryenTruncVecF32x4()


def NearestVecF32x4() -> BinaryenOp:
    return lib.BinaryenNearestVecF32x4()


def AbsVecF64x2() -> BinaryenOp:
    return lib.BinaryenAbsVecF64x2()


def NegVecF64x2() -> BinaryenOp:
    return lib.BinaryenNegVecF64x2()


def SqrtVecF64x2() -> BinaryenOp:
    return lib.BinaryenSqrtVecF64x2()


def AddVecF64x2() -> BinaryenOp:
    return lib.BinaryenAddVecF64x2()


def SubVecF64x2() -> BinaryenOp:
    return lib.BinaryenSubVecF64x2()


def MulVecF64x2() -> BinaryenOp:
    return lib.BinaryenMulVecF64x2()


def DivVecF64x2() -> BinaryenOp:
    return lib.BinaryenDivVecF64x2()


def MinVecF64x2() -> BinaryenOp:
    return lib.BinaryenMinVecF64x2()


def MaxVecF64x2() -> BinaryenOp:
    return lib.BinaryenMaxVecF64x2()


def PMinVecF64x2() -> BinaryenOp:
    return lib.BinaryenPMinVecF64x2()


def PMaxVecF64x2() -> BinaryenOp:
    return lib.BinaryenPMaxVecF64x2()


def CeilVecF64x2() -> BinaryenOp:
    return lib.BinaryenCeilVecF64x2()


def FloorVecF64x2() -> BinaryenOp:
    return lib.BinaryenFloorVecF64x2()


def TruncVecF64x2() -> BinaryenOp:
    return lib.BinaryenTruncVecF64x2()


def NearestVecF64x2() -> BinaryenOp:
    return lib.BinaryenNearestVecF64x2()


def ExtAddPairwiseSVecI8x16ToI16x8() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseSVecI8x16ToI16x8()


def ExtAddPairwiseUVecI8x16ToI16x8() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseUVecI8x16ToI16x8()


def ExtAddPairwiseSVecI16x8ToI32x4() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseSVecI16x8ToI32x4()


def ExtAddPairwiseUVecI16x8ToI32x4() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseUVecI16x8ToI32x4()


def TruncSatSVecF32x4ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatSVecF32x4ToVecI32x4()


def TruncSatUVecF32x4ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatUVecF32x4ToVecI32x4()


def ConvertSVecI32x4ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenConvertSVecI32x4ToVecF32x4()


def ConvertUVecI32x4ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenConvertUVecI32x4ToVecF32x4()


def Load8SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad8SplatVec128()


def Load16SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad16SplatVec128()


def Load32SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad32SplatVec128()


def Load64SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad64SplatVec128()


def Load8x8SVec128() -> BinaryenOp:
    return lib.BinaryenLoad8x8SVec128()


def Load8x8UVec128() -> BinaryenOp:
    return lib.BinaryenLoad8x8UVec128()


def Load16x4SVec128() -> BinaryenOp:
    return lib.BinaryenLoad16x4SVec128()


def Load16x4UVec128() -> BinaryenOp:
    return lib.BinaryenLoad16x4UVec128()


def Load32x2SVec128() -> BinaryenOp:
    return lib.BinaryenLoad32x2SVec128()


def Load32x2UVec128() -> BinaryenOp:
    return lib.BinaryenLoad32x2UVec128()


def Load32ZeroVec128() -> BinaryenOp:
    return lib.BinaryenLoad32ZeroVec128()


def Load64ZeroVec128() -> BinaryenOp:
    return lib.BinaryenLoad64ZeroVec128()


def Load8LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad8LaneVec128()


def Load16LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad16LaneVec128()


def Load32LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad32LaneVec128()


def Load64LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad64LaneVec128()


def Store8LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore8LaneVec128()


def Store16LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore16LaneVec128()


def Store32LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore32LaneVec128()


def Store64LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore64LaneVec128()


def NarrowSVecI16x8ToVecI8x16() -> BinaryenOp:
    return lib.BinaryenNarrowSVecI16x8ToVecI8x16()


def NarrowUVecI16x8ToVecI8x16() -> BinaryenOp:
    return lib.BinaryenNarrowUVecI16x8ToVecI8x16()


def NarrowSVecI32x4ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenNarrowSVecI32x4ToVecI16x8()


def NarrowUVecI32x4ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenNarrowUVecI32x4ToVecI16x8()


def ExtendLowSVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI8x16ToVecI16x8()


def ExtendHighSVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI8x16ToVecI16x8()


def ExtendLowUVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI8x16ToVecI16x8()


def ExtendHighUVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI8x16ToVecI16x8()


def ExtendLowSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI16x8ToVecI32x4()


def ExtendHighSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI16x8ToVecI32x4()


def ExtendLowUVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI16x8ToVecI32x4()


def ExtendHighUVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI16x8ToVecI32x4()


def ExtendLowSVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI32x4ToVecI64x2()


def ExtendHighSVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI32x4ToVecI64x2()


def ExtendLowUVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI32x4ToVecI64x2()


def ExtendHighUVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI32x4ToVecI64x2()


def ConvertLowSVecI32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenConvertLowSVecI32x4ToVecF64x2()


def ConvertLowUVecI32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenConvertLowUVecI32x4ToVecF64x2()


def TruncSatZeroSVecF64x2ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatZeroSVecF64x2ToVecI32x4()


def TruncSatZeroUVecF64x2ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatZeroUVecF64x2ToVecI32x4()


def DemoteZeroVecF64x2ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenDemoteZeroVecF64x2ToVecF32x4()


def PromoteLowVecF32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenPromoteLowVecF32x4ToVecF64x2()


def SwizzleVecI8x16() -> BinaryenOp:
    return lib.BinaryenSwizzleVecI8x16()


def RefIsNull() -> BinaryenOp:
    return lib.BinaryenRefIsNull()


def RefIsFunc() -> BinaryenOp:
    return lib.BinaryenRefIsFunc()


def RefIsData() -> BinaryenOp:
    return lib.BinaryenRefIsData()


def RefIsI31() -> BinaryenOp:
    return lib.BinaryenRefIsI31()


def RefAsNonNull() -> BinaryenOp:
    return lib.BinaryenRefAsNonNull()


def RefAsFunc() -> BinaryenOp:
    return lib.BinaryenRefAsFunc()


def RefAsData() -> BinaryenOp:
    return lib.BinaryenRefAsData()


def RefAsI31() -> BinaryenOp:
    return lib.BinaryenRefAsI31()


def RefAsExternInternalize() -> BinaryenOp:
    return lib.BinaryenRefAsExternInternalize()


def RefAsExternExternalize() -> BinaryenOp:
    return lib.BinaryenRefAsExternExternalize()


def BrOnNull() -> BinaryenOp:
    return lib.BinaryenBrOnNull()


def BrOnNonNull() -> BinaryenOp:
    return lib.BinaryenBrOnNonNull()


def BrOnCast() -> BinaryenOp:
    return lib.BinaryenBrOnCast()


def BrOnCastFail() -> BinaryenOp:
    return lib.BinaryenBrOnCastFail()


def BrOnFunc() -> BinaryenOp:
    return lib.BinaryenBrOnFunc()


def BrOnNonFunc() -> BinaryenOp:
    return lib.BinaryenBrOnNonFunc()


def BrOnData() -> BinaryenOp:
    return lib.BinaryenBrOnData()


def BrOnNonData() -> BinaryenOp:
    return lib.BinaryenBrOnNonData()


def BrOnI31() -> BinaryenOp:
    return lib.BinaryenBrOnI31()


def BrOnNonI31() -> BinaryenOp:
    return lib.BinaryenBrOnNonI31()


def StringNewUTF8() -> BinaryenOp:
    return lib.BinaryenStringNewUTF8()


def StringNewWTF8() -> BinaryenOp:
    return lib.BinaryenStringNewWTF8()


def StringNewReplace() -> BinaryenOp:
    return lib.BinaryenStringNewReplace()


def StringNewWTF16() -> BinaryenOp:
    return lib.BinaryenStringNewWTF16()


def StringNewUTF8Array() -> BinaryenOp:
    return lib.BinaryenStringNewUTF8Array()


def StringNewWTF8Array() -> BinaryenOp:
    return lib.BinaryenStringNewWTF8Array()


def StringNewReplaceArray() -> BinaryenOp:
    return lib.BinaryenStringNewReplaceArray()


def StringNewWTF16Array() -> BinaryenOp:
    return lib.BinaryenStringNewWTF16Array()


def StringMeasureUTF8() -> BinaryenOp:
    return lib.BinaryenStringMeasureUTF8()


def StringMeasureWTF8() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF8()


def StringMeasureWTF16() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF16()


def StringMeasureIsUSV() -> BinaryenOp:
    return lib.BinaryenStringMeasureIsUSV()


def StringMeasureWTF16View() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF16View()


def StringEncodeUTF8() -> BinaryenOp:
    return lib.BinaryenStringEncodeUTF8()


def StringEncodeWTF8() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF8()


def StringEncodeWTF16() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF16()


def StringEncodeUTF8Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeUTF8Array()


def StringEncodeWTF8Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF8Array()


def StringEncodeWTF16Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF16Array()


def StringAsWTF8() -> BinaryenOp:
    return lib.BinaryenStringAsWTF8()


def StringAsWTF16() -> BinaryenOp:
    return lib.BinaryenStringAsWTF16()


def StringAsIter() -> BinaryenOp:
    return lib.BinaryenStringAsIter()


def StringIterMoveAdvance() -> BinaryenOp:
    return lib.BinaryenStringIterMoveAdvance()


def StringIterMoveRewind() -> BinaryenOp:
    return lib.BinaryenStringIterMoveRewind()


def StringSliceWTF8() -> BinaryenOp:
    return lib.BinaryenStringSliceWTF8()


def StringSliceWTF16() -> BinaryenOp:
    return lib.BinaryenStringSliceWTF16()


def Block(
    module: BinaryenModuleRef,
    name: str,
    children: List[BinaryenExpressionRef],
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    Block: name can be NULL. Specifying BinaryenUndefined() as the 'type'
    parameter indicates that the block's type shall be figured out
    automatically instead of explicitly providing it. This conforms
    to the behavior before the 'type' parameter has been introduced.
    """
    return lib.BinaryenBlock(module, name.encode(), children, len(children), _type)


def If(
    module: BinaryenModuleRef,
    condition: BinaryenExpressionRef,
    if_true: BinaryenExpressionRef,
    if_false: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ If: ifFalse can be NULL """
    return lib.BinaryenIf(module, condition, if_true, if_false)


def Loop(
    module: BinaryenModuleRef,
    _in: str,
    body: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenLoop(module, _in.encode(), body)


def Break(
    module: BinaryenModuleRef,
    name: str,
    condition: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Break: value and condition can be NULL """
    return lib.BinaryenBreak(module, name.encode(), condition, value)


def Switch(
    module: BinaryenModuleRef,
    names: List[str],
    default_name: str,
    condition: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Switch: value can be NULL """
    return lib.BinaryenSwitch(module, [item.encode() for item in names], len(names), default_name.encode(), condition, value)


def Call(
    module: BinaryenModuleRef,
    target: str,
    operands: List[BinaryenExpressionRef],
    return_type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    Call: Note the 'returnType' parameter. You must declare the
    type returned by the function being called, as that
    function might not have been created yet, so we don't
    know what it is.
    """
    return lib.BinaryenCall(module, target.encode(), operands, len(operands), return_type)


def CallIndirect(
    module: BinaryenModuleRef,
    table: str,
    target: BinaryenExpressionRef,
    operands: List[BinaryenExpressionRef],
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallIndirect(module, table.encode(), target, operands, len(operands), params, results)


def ReturnCall(
    module: BinaryenModuleRef,
    target: str,
    operands: List[BinaryenExpressionRef],
    return_type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenReturnCall(module, target.encode(), operands, len(operands), return_type)


def ReturnCallIndirect(
    module: BinaryenModuleRef,
    table: str,
    target: BinaryenExpressionRef,
    operands: List[BinaryenExpressionRef],
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenReturnCallIndirect(module, table.encode(), target, operands, len(operands), params, results)


def LocalGet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    LocalGet: Note the 'type' parameter. It might seem redundant, since the
    local at that index must have a type. However, this API lets you
    build code "top-down": create a node, then its parents, and so
    on, and finally create the function at the end. (Note that in fact
    you do not mention a function when creating ExpressionRefs, only
    a module.) And since LocalGet is a leaf node, we need to be told
    its type. (Other nodes detect their type either from their
    type or their opcode, or failing that, their children. But
    LocalGet has no children, it is where a "stream" of type info
    begins.)
    Note also that the index of a local can refer to a param or
    a var, that is, either a parameter to the function or a variable
    declared when you call BinaryenAddFunction. See BinaryenAddFunction
    for more details.
    """
    return lib.BinaryenLocalGet(module, index, _type)


def LocalSet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenLocalSet(module, index, value)


def LocalTee(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenLocalTee(module, index, value, _type)


def GlobalGet(
    module: BinaryenModuleRef,
    name: str,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenGlobalGet(module, name.encode(), _type)


def GlobalSet(
    module: BinaryenModuleRef,
    name: str,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenGlobalSet(module, name.encode(), value)


def Load(
    module: BinaryenModuleRef,
    _bytes: int,
    signed_: bool,
    offset: int,
    align: int,
    _type: BinaryenType,
    ptr: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    """
    Load: align can be 0, in which case it will be the natural alignment (equal
    to bytes)
    """
    return lib.BinaryenLoad(module, _bytes, signed_, offset, align, _type, ptr, memory_name.encode())


def Store(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    align: int,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    """
    Store: align can be 0, in which case it will be the natural alignment (equal
    to bytes)
    """
    return lib.BinaryenStore(module, _bytes, offset, align, ptr, value, _type, memory_name.encode())


def Const(
    module: BinaryenModuleRef,
    value: BinaryenLiteral,
) -> BinaryenExpressionRef:
    return lib.BinaryenConst(module, value)


def Unary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenUnary(module, op, value)


def Binary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenBinary(module, op, left, right)


def Select(
    module: BinaryenModuleRef,
    condition: BinaryenExpressionRef,
    if_true: BinaryenExpressionRef,
    if_false: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenSelect(module, condition, if_true, if_false, _type)


def Drop(
    module: BinaryenModuleRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenDrop(module, value)


def Return(
    module: BinaryenModuleRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Return: value can be NULL """
    return lib.BinaryenReturn(module, value)


def MemorySize(
    module: BinaryenModuleRef,
    memory_name: str,
    memory_is64: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemorySize(module, memory_name.encode(), memory_is64)


def MemoryGrow(
    module: BinaryenModuleRef,
    delta: BinaryenExpressionRef,
    memory_name: str,
    memory_is64: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryGrow(module, delta, memory_name.encode(), memory_is64)


def Nop(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenNop(module)


def Unreachable(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenUnreachable(module)


def AtomicLoad(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    _type: BinaryenType,
    ptr: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicLoad(module, _bytes, offset, _type, ptr, memory_name.encode())


def AtomicStore(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicStore(module, _bytes, offset, ptr, value, _type, memory_name.encode())


def AtomicRMW(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    _bytes: BinaryenIndex,
    offset: BinaryenIndex,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicRMW(module, op, _bytes, offset, ptr, value, _type, memory_name.encode())


def AtomicCmpxchg(
    module: BinaryenModuleRef,
    _bytes: BinaryenIndex,
    offset: BinaryenIndex,
    ptr: BinaryenExpressionRef,
    expected: BinaryenExpressionRef,
    replacement: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicCmpxchg(module, _bytes, offset, ptr, expected, replacement, _type, memory_name.encode())


def AtomicWait(
    module: BinaryenModuleRef,
    ptr: BinaryenExpressionRef,
    expected: BinaryenExpressionRef,
    timeout: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicWait(module, ptr, expected, timeout, _type, memory_name.encode())


def AtomicNotify(
    module: BinaryenModuleRef,
    ptr: BinaryenExpressionRef,
    notify_count: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicNotify(module, ptr, notify_count, memory_name.encode())


def AtomicFence(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicFence(module)


def SIMDExtract(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    index: int,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDExtract(module, op, vec, index)


def SIMDReplace(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    index: int,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDReplace(module, op, vec, index, value)


def SIMDShuffle(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
    mask: List[int],
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDShuffle(module, left, right, mask)


def SIMDTernary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    a: BinaryenExpressionRef,
    b: BinaryenExpressionRef,
    c: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDTernary(module, op, a, b, c)


def SIMDShift(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    shift: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDShift(module, op, vec, shift)


def SIMDLoad(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    offset: int,
    align: int,
    ptr: BinaryenExpressionRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDLoad(module, op, offset, align, ptr, name.encode())


def SIMDLoadStoreLane(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    offset: int,
    align: int,
    index: int,
    ptr: BinaryenExpressionRef,
    vec: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDLoadStoreLane(module, op, offset, align, index, ptr, vec, memory_name.encode())


def MemoryInit(
    module: BinaryenModuleRef,
    segment: int,
    dest: BinaryenExpressionRef,
    offset: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryInit(module, segment, dest, offset, size, memory_name.encode())


def DataDrop(
    module: BinaryenModuleRef,
    segment: int,
) -> BinaryenExpressionRef:
    return lib.BinaryenDataDrop(module, segment)


def MemoryCopy(
    module: BinaryenModuleRef,
    dest: BinaryenExpressionRef,
    source: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    dest_memory: str,
    source_memory: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryCopy(module, dest, source, size, dest_memory.encode(), source_memory.encode())


def MemoryFill(
    module: BinaryenModuleRef,
    dest: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryFill(module, dest, value, size, memory_name.encode())


def RefNull(
    module: BinaryenModuleRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefNull(module, _type)


def RefIs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefIs(module, op, value)


def RefAs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefAs(module, op, value)


def RefFunc(
    module: BinaryenModuleRef,
    func: str,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefFunc(module, func.encode(), _type)


def RefEq(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefEq(module, left, right)


def TableGet(
    module: BinaryenModuleRef,
    name: str,
    index: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableGet(module, name.encode(), index, _type)


def TableSet(
    module: BinaryenModuleRef,
    name: str,
    index: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableSet(module, name.encode(), index, value)


def TableSize(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableSize(module, name.encode())


def TableGrow(
    module: BinaryenModuleRef,
    name: str,
    value: BinaryenExpressionRef,
    delta: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableGrow(module, name.encode(), value, delta)


def Try(
    module: BinaryenModuleRef,
    name: str,
    body: BinaryenExpressionRef,
    catch_tags: List[str],
    catch_bodies: List[BinaryenExpressionRef],
    delegate_target: str,
) -> BinaryenExpressionRef:
    """ Try: name can be NULL. delegateTarget should be NULL in try-catch. """
    return lib.BinaryenTry(module, name.encode(), body, [item.encode() for item in catch_tags], len(catch_tags), catch_bodies, len(catch_bodies), delegate_target.encode())


def Throw(
    module: BinaryenModuleRef,
    tag: str,
    operands: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenThrow(module, tag.encode(), operands, len(operands))


def Rethrow(
    module: BinaryenModuleRef,
    target: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenRethrow(module, target.encode())


def TupleMake(
    module: BinaryenModuleRef,
    operands: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenTupleMake(module, operands, len(operands))


def TupleExtract(
    module: BinaryenModuleRef,
    _tuple: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenTupleExtract(module, _tuple, index)


def Pop(
    module: BinaryenModuleRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenPop(module, _type)


def I31New(
    module: BinaryenModuleRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenI31New(module, value)


def I31Get(
    module: BinaryenModuleRef,
    i31: BinaryenExpressionRef,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenI31Get(module, i31, signed_)


def CallRef(
    module: BinaryenModuleRef,
    target: BinaryenExpressionRef,
    operands: List[BinaryenExpressionRef],
    _type: BinaryenType,
    is_return: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRef(module, target, operands, len(operands), _type, is_return)


def RefTest(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefTest(module, ref, intended_type)


def RefCast(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefCast(module, ref, intended_type)


def BrOn(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    name: str,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenBrOn(module, op, name.encode(), ref, intended_type)


def StructNew(
    module: BinaryenModuleRef,
    operands: List[BinaryenExpressionRef],
    _type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNew(module, operands, len(operands), _type)


def StructGet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    ref: BinaryenExpressionRef,
    _type: BinaryenType,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructGet(module, index, ref, _type, signed_)


def StructSet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    ref: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSet(module, index, ref, value)


def ArrayNew(
    module: BinaryenModuleRef,
    _type: BinaryenHeapType,
    size: BinaryenExpressionRef,
    init: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayNew(module, _type, size, init)


def ArrayInit(
    module: BinaryenModuleRef,
    _type: BinaryenHeapType,
    values: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    """ TODO: BinaryenArrayNewSeg """
    return lib.BinaryenArrayInit(module, _type, values, len(values))


def ArrayGet(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    index: BinaryenExpressionRef,
    _type: BinaryenType,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayGet(module, ref, index, _type, signed_)


def ArraySet(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    index: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySet(module, ref, index, value)


def ArrayLen(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayLen(module, ref)


def ArrayCopy(
    module: BinaryenModuleRef,
    dest_ref: BinaryenExpressionRef,
    dest_index: BinaryenExpressionRef,
    src_ref: BinaryenExpressionRef,
    src_index: BinaryenExpressionRef,
    length: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopy(module, dest_ref, dest_index, src_ref, src_index, length)


def StringNew(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ptr: BinaryenExpressionRef,
    length: BinaryenExpressionRef,
    start: BinaryenExpressionRef,
    end: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNew(module, op, ptr, length, start, end)


def StringConst(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConst(module, name.encode())


def StringMeasure(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringMeasure(module, op, ref)


def StringEncode(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    ptr: BinaryenExpressionRef,
    start: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncode(module, op, ref, ptr, start)


def StringConcat(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConcat(module, left, right)


def StringEq(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEq(module, left, right)


def StringAs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringAs(module, op, ref)


def StringWTF8Advance(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    pos: BinaryenExpressionRef,
    _bytes: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8Advance(module, ref, pos, _bytes)


def StringWTF16Get(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    pos: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF16Get(module, ref, pos)


def StringIterNext(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterNext(module, ref)


def StringIterMove(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    num: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMove(module, op, ref, num)


def StringSliceWTF(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    start: BinaryenExpressionRef,
    end: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTF(module, op, ref, start, end)


def StringSliceIter(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    num: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceIter(module, ref, num)


def ExpressionGetId(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionId:
    """
    Expression
    Gets the id (kind) of the given expression.
    """
    return lib.BinaryenExpressionGetId(expr)


def ExpressionGetType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the type of the given expression. """
    return lib.BinaryenExpressionGetType(expr)


def ExpressionSetType(
    expr: BinaryenExpressionRef,
    _type: BinaryenType,
) -> None:
    """ Sets the type of the given expression. """
    lib.BinaryenExpressionSetType(expr, _type)


def ExpressionPrint(
    expr: BinaryenExpressionRef,
) -> None:
    """ Prints text format of the given expression to stdout. """
    lib.BinaryenExpressionPrint(expr)


def ExpressionFinalize(
    expr: BinaryenExpressionRef,
) -> None:
    """ Re-finalizes an expression after it has been modified. """
    lib.BinaryenExpressionFinalize(expr)


def ExpressionCopy(
    expr: BinaryenExpressionRef,
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    """ Makes a deep copy of the given expression. """
    return lib.BinaryenExpressionCopy(expr, module)


def BlockGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Block
    Gets the name (label) of a `block` expression.
    """
    return lib.BinaryenBlockGetName(expr)


def BlockSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `block` expression. """
    lib.BinaryenBlockSetName(expr, name.encode())


def BlockGetNumChildren(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of child expressions of a `block` expression. """
    return lib.BinaryenBlockGetNumChildren(expr)


def BlockGetChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the child expression at the specified index of a `block` expression. """
    return lib.BinaryenBlockGetChildAt(expr, index)


def BlockSetChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    child_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets (replaces) the child expression at the specified index of a `block`
    expression.
    """
    lib.BinaryenBlockSetChildAt(expr, index, child_expr)


def BlockAppendChild(
    expr: BinaryenExpressionRef,
    child_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends a child expression to a `block` expression, returning its insertion
    index.
    """
    return lib.BinaryenBlockAppendChild(expr, child_expr)


def BlockInsertChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    child_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts a child expression at the specified index of a `block` expression,
    moving existing children including the one previously at that index one index
    up.
    """
    lib.BinaryenBlockInsertChildAt(expr, index, child_expr)


def BlockRemoveChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the child expression at the specified index of a `block` expression,
    moving all subsequent children one index down. Returns the child expression.
    """
    return lib.BinaryenBlockRemoveChildAt(expr, index)


def IfGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    If
    Gets the condition expression of an `if` expression.
    """
    return lib.BinaryenIfGetCondition(expr)


def IfSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of an `if` expression. """
    lib.BinaryenIfSetCondition(expr, cond_expr)


def IfGetIfTrue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the ifTrue (then) expression of an `if` expression. """
    return lib.BinaryenIfGetIfTrue(expr)


def IfSetIfTrue(
    expr: BinaryenExpressionRef,
    if_true_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the ifTrue (then) expression of an `if` expression. """
    lib.BinaryenIfSetIfTrue(expr, if_true_expr)


def IfGetIfFalse(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the ifFalse (else) expression, if any, of an `if` expression. """
    return lib.BinaryenIfGetIfFalse(expr)


def IfSetIfFalse(
    expr: BinaryenExpressionRef,
    if_false_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the ifFalse (else) expression, if any, of an `if` expression. """
    lib.BinaryenIfSetIfFalse(expr, if_false_expr)


def LoopGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Loop
    Gets the name (label) of a `loop` expression.
    """
    return lib.BinaryenLoopGetName(expr)


def LoopSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `loop` expression. """
    lib.BinaryenLoopSetName(expr, name.encode())


def LoopGetBody(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the body expression of a `loop` expression. """
    return lib.BinaryenLoopGetBody(expr)


def LoopSetBody(
    expr: BinaryenExpressionRef,
    body_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the body expression of a `loop` expression. """
    lib.BinaryenLoopSetBody(expr, body_expr)


def BreakGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Break
    Gets the name (target label) of a `br` or `br_if` expression.
    """
    return lib.BinaryenBreakGetName(expr)


def BreakSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (target label) of a `br` or `br_if` expression. """
    lib.BinaryenBreakSetName(expr, name.encode())


def BreakGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the condition expression, if any, of a `br_if` expression. No condition
    indicates a `br` expression.
    """
    return lib.BinaryenBreakGetCondition(expr)


def BreakSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the condition expression, if any, of a `br_if` expression. No condition
    makes it a `br` expression.
    """
    lib.BinaryenBreakSetCondition(expr, cond_expr)


def BreakGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression, if any, of a `br` or `br_if` expression. """
    return lib.BinaryenBreakGetValue(expr)


def BreakSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, of a `br` or `br_if` expression. """
    lib.BinaryenBreakSetValue(expr, value_expr)


def SwitchGetNumNames(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Switch
    Gets the number of names (target labels) of a `br_table` expression.
    """
    return lib.BinaryenSwitchGetNumNames(expr)


def SwitchGetNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Gets the name (target label) at the specified index of a `br_table`
    expression.
    """
    return lib.BinaryenSwitchGetNameAt(expr, index)


def SwitchSetNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """
    Sets the name (target label) at the specified index of a `br_table`
    expression.
    """
    lib.BinaryenSwitchSetNameAt(expr, index, name.encode())


def SwitchAppendName(
    expr: BinaryenExpressionRef,
    name: str,
) -> BinaryenIndex:
    """ Appends a name to a `br_table` expression, returning its insertion index. """
    return lib.BinaryenSwitchAppendName(expr, name.encode())


def SwitchInsertNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """
    Inserts a name at the specified index of a `br_table` expression, moving
    existing names including the one previously at that index one index up.
    """
    lib.BinaryenSwitchInsertNameAt(expr, index, name.encode())


def SwitchRemoveNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Removes the name at the specified index of a `br_table` expression, moving
    all subsequent names one index down. Returns the name.
    """
    return lib.BinaryenSwitchRemoveNameAt(expr, index)


def SwitchGetDefaultName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the default name (target label), if any, of a `br_table` expression. """
    return lib.BinaryenSwitchGetDefaultName(expr)


def SwitchSetDefaultName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the default name (target label), if any, of a `br_table` expression. """
    lib.BinaryenSwitchSetDefaultName(expr, name.encode())


def SwitchGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the condition expression of a `br_table` expression. """
    return lib.BinaryenSwitchGetCondition(expr)


def SwitchSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of a `br_table` expression. """
    lib.BinaryenSwitchSetCondition(expr, cond_expr)


def SwitchGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression, if any, of a `br_table` expression. """
    return lib.BinaryenSwitchGetValue(expr)


def SwitchSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, of a `br_table` expression. """
    lib.BinaryenSwitchSetValue(expr, value_expr)


def CallGetTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Call
    Gets the target function name of a `call` expression.
    """
    return lib.BinaryenCallGetTarget(expr)


def CallSetTarget(
    expr: BinaryenExpressionRef,
    target: str,
) -> None:
    """ Sets the target function name of a `call` expression. """
    lib.BinaryenCallSetTarget(expr, target.encode())


def CallGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `call` expression. """
    return lib.BinaryenCallGetNumOperands(expr)


def CallGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand expression at the specified index of a `call` expression. """
    return lib.BinaryenCallGetOperandAt(expr, index)


def CallSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand expression at the specified index of a `call` expression. """
    lib.BinaryenCallSetOperandAt(expr, index, operand_expr)


def CallAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `call` expression, returning its insertion
    index.
    """
    return lib.BinaryenCallAppendOperand(expr, operand_expr)


def CallInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `call` expression,
    moving existing operands including the one previously at that index one index
    up.
    """
    lib.BinaryenCallInsertOperandAt(expr, index, operand_expr)


def CallRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `call` expression,
    moving all subsequent operands one index down. Returns the operand
    expression.
    """
    return lib.BinaryenCallRemoveOperandAt(expr, index)


def CallIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether the specified `call` expression is a tail call. """
    return lib.BinaryenCallIsReturn(expr)


def CallSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    """ Sets whether the specified `call` expression is a tail call. """
    lib.BinaryenCallSetReturn(expr, is_return)


def CallIndirectGetTarget(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    CallIndirect
    Gets the target expression of a `call_indirect` expression.
    """
    return lib.BinaryenCallIndirectGetTarget(expr)


def CallIndirectSetTarget(
    expr: BinaryenExpressionRef,
    target_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the target expression of a `call_indirect` expression. """
    lib.BinaryenCallIndirectSetTarget(expr, target_expr)


def CallIndirectGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the table name of a `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetTable(expr)


def CallIndirectSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the table name of a `call_indirect` expression. """
    lib.BinaryenCallIndirectSetTable(expr, table.encode())


def CallIndirectGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetNumOperands(expr)


def CallIndirectGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Gets the operand expression at the specified index of a `call_indirect`
    expression.
    """
    return lib.BinaryenCallIndirectGetOperandAt(expr, index)


def CallIndirectSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the operand expression at the specified index of a `call_indirect`
    expression.
    """
    lib.BinaryenCallIndirectSetOperandAt(expr, index, operand_expr)


def CallIndirectAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `call_indirect` expression, returning its
    insertion index.
    """
    return lib.BinaryenCallIndirectAppendOperand(expr, operand_expr)


def CallIndirectInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `call_indirect`
    expression, moving existing operands including the one previously at that
    index one index up.
    """
    lib.BinaryenCallIndirectInsertOperandAt(expr, index, operand_expr)


def CallIndirectRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `call_indirect`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenCallIndirectRemoveOperandAt(expr, index)


def CallIndirectIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether the specified `call_indirect` expression is a tail call. """
    return lib.BinaryenCallIndirectIsReturn(expr)


def CallIndirectSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    """ Sets whether the specified `call_indirect` expression is a tail call. """
    lib.BinaryenCallIndirectSetReturn(expr, is_return)


def CallIndirectGetParams(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the parameter types of the specified `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetParams(expr)


def CallIndirectSetParams(
    expr: BinaryenExpressionRef,
    params: BinaryenType,
) -> None:
    """ Sets the parameter types of the specified `call_indirect` expression. """
    lib.BinaryenCallIndirectSetParams(expr, params)


def CallIndirectGetResults(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the result types of the specified `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetResults(expr)


def CallIndirectSetResults(
    expr: BinaryenExpressionRef,
    params: BinaryenType,
) -> None:
    """ Sets the result types of the specified `call_indirect` expression. """
    lib.BinaryenCallIndirectSetResults(expr, params)


def LocalGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    LocalGet
    Gets the local index of a `local.get` expression.
    """
    return lib.BinaryenLocalGetGetIndex(expr)


def LocalGetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the local index of a `local.get` expression. """
    lib.BinaryenLocalGetSetIndex(expr, index)


def LocalSetIsTee(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    LocalSet
    Gets whether a `local.set` tees its value (is a `local.tee`). True if the
    expression has a type other than `none`.
    """
    return lib.BinaryenLocalSetIsTee(expr)


def LocalSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the local index of a `local.set` or `local.tee` expression. """
    return lib.BinaryenLocalSetGetIndex(expr)


def LocalSetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the local index of a `local.set` or `local.tee` expression. """
    lib.BinaryenLocalSetSetIndex(expr, index)


def LocalSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `local.set` or `local.tee` expression. """
    return lib.BinaryenLocalSetGetValue(expr)


def LocalSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `local.set` or `local.tee` expression. """
    lib.BinaryenLocalSetSetValue(expr, value_expr)


def GlobalGetGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    GlobalGet
    Gets the name of the global being accessed by a `global.get` expression.
    """
    return lib.BinaryenGlobalGetGetName(expr)


def GlobalGetSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name of the global being accessed by a `global.get` expression. """
    lib.BinaryenGlobalGetSetName(expr, name.encode())


def GlobalSetGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    GlobalSet
    Gets the name of the global being accessed by a `global.set` expression.
    """
    return lib.BinaryenGlobalSetGetName(expr)


def GlobalSetSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name of the global being accessed by a `global.set` expression. """
    lib.BinaryenGlobalSetSetName(expr, name.encode())


def GlobalSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `global.set` expression. """
    return lib.BinaryenGlobalSetGetValue(expr)


def GlobalSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `global.set` expression. """
    lib.BinaryenGlobalSetSetValue(expr, value_expr)


def TableGetGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """
    TableGet
    Gets the name of the table being accessed by a `table.get` expression.
    """
    return lib.BinaryenTableGetGetTable(expr)


def TableGetSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.get` expression. """
    lib.BinaryenTableGetSetTable(expr, table.encode())


def TableGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the index expression of a `table.get` expression. """
    return lib.BinaryenTableGetGetIndex(expr)


def TableGetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the index expression of a `table.get` expression. """
    lib.BinaryenTableGetSetIndex(expr, index_expr)


def TableSetGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """
    TableSet
    Gets the name of the table being accessed by a `table.set` expression.
    """
    return lib.BinaryenTableSetGetTable(expr)


def TableSetSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.set` expression. """
    lib.BinaryenTableSetSetTable(expr, table.encode())


def TableSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the index expression of a `table.set` expression. """
    return lib.BinaryenTableSetGetIndex(expr)


def TableSetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the index expression of a `table.set` expression. """
    lib.BinaryenTableSetSetIndex(expr, index_expr)


def TableSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `table.set` expression. """
    return lib.BinaryenTableSetGetValue(expr)


def TableSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `table.set` expression. """
    lib.BinaryenTableSetSetValue(expr, value_expr)


def TableSizeGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """
    TableSize
    Gets the name of the table being accessed by a `table.size` expression.
    """
    return lib.BinaryenTableSizeGetTable(expr)


def TableSizeSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.size` expression. """
    lib.BinaryenTableSizeSetTable(expr, table.encode())


def TableGrowGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """
    TableGrow
    Gets the name of the table being accessed by a `table.grow` expression.
    """
    return lib.BinaryenTableGrowGetTable(expr)


def TableGrowSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.grow` expression. """
    lib.BinaryenTableGrowSetTable(expr, table.encode())


def TableGrowGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `table.grow` expression. """
    return lib.BinaryenTableGrowGetValue(expr)


def TableGrowSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `table.grow` expression. """
    lib.BinaryenTableGrowSetValue(expr, value_expr)


def TableGrowGetDelta(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the delta of a `table.grow` expression. """
    return lib.BinaryenTableGrowGetDelta(expr)


def TableGrowSetDelta(
    expr: BinaryenExpressionRef,
    delta_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the delta of a `table.grow` expression. """
    lib.BinaryenTableGrowSetDelta(expr, delta_expr)


def MemoryGrowGetDelta(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    MemoryGrow
    Gets the delta of a `memory.grow` expression.
    """
    return lib.BinaryenMemoryGrowGetDelta(expr)


def MemoryGrowSetDelta(
    expr: BinaryenExpressionRef,
    delta_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the delta of a `memory.grow` expression. """
    lib.BinaryenMemoryGrowSetDelta(expr, delta_expr)


def LoadIsAtomic(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    Load
    Gets whether a `load` expression is atomic (is an `atomic.load`).
    """
    return lib.BinaryenLoadIsAtomic(expr)


def LoadSetAtomic(
    expr: BinaryenExpressionRef,
    is_atomic: bool,
) -> None:
    """ Sets whether a `load` expression is atomic (is an `atomic.load`). """
    lib.BinaryenLoadSetAtomic(expr, is_atomic)


def LoadIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `load` expression operates on a signed value (`_s`). """
    return lib.BinaryenLoadIsSigned(expr)


def LoadSetSigned(
    expr: BinaryenExpressionRef,
    is_signed: bool,
) -> None:
    """ Sets whether a `load` expression operates on a signed value (`_s`). """
    lib.BinaryenLoadSetSigned(expr, is_signed)


def LoadGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a `load` expression. """
    return lib.BinaryenLoadGetOffset(expr)


def LoadSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a `load` expression. """
    lib.BinaryenLoadSetOffset(expr, offset)


def LoadGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes loaded by a `load` expression. """
    return lib.BinaryenLoadGetBytes(expr)


def LoadSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes loaded by a `load` expression. """
    lib.BinaryenLoadSetBytes(expr, _bytes)


def LoadGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a `load` expression. """
    return lib.BinaryenLoadGetAlign(expr)


def LoadSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a `load` expression. """
    lib.BinaryenLoadSetAlign(expr, align)


def LoadGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a `load` expression. """
    return lib.BinaryenLoadGetPtr(expr)


def LoadSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a `load` expression. """
    lib.BinaryenLoadSetPtr(expr, ptr_expr)


def StoreIsAtomic(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    Store
    Gets whether a `store` expression is atomic (is an `atomic.store`).
    """
    return lib.BinaryenStoreIsAtomic(expr)


def StoreSetAtomic(
    expr: BinaryenExpressionRef,
    is_atomic: bool,
) -> None:
    """ Sets whether a `store` expression is atomic (is an `atomic.store`). """
    lib.BinaryenStoreSetAtomic(expr, is_atomic)


def StoreGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes stored by a `store` expression. """
    return lib.BinaryenStoreGetBytes(expr)


def StoreSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes stored by a `store` expression. """
    lib.BinaryenStoreSetBytes(expr, _bytes)


def StoreGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a `store` expression. """
    return lib.BinaryenStoreGetOffset(expr)


def StoreSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a `store` expression. """
    lib.BinaryenStoreSetOffset(expr, offset)


def StoreGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a `store` expression. """
    return lib.BinaryenStoreGetAlign(expr)


def StoreSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a `store` expression. """
    lib.BinaryenStoreSetAlign(expr, align)


def StoreGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a `store` expression. """
    return lib.BinaryenStoreGetPtr(expr)


def StoreSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a `store` expression. """
    lib.BinaryenStoreSetPtr(expr, ptr_expr)


def StoreGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `store` expression. """
    return lib.BinaryenStoreGetValue(expr)


def StoreSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `store` expression. """
    lib.BinaryenStoreSetValue(expr, value_expr)


def StoreGetValueType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the value type of a `store` expression. """
    return lib.BinaryenStoreGetValueType(expr)


def StoreSetValueType(
    expr: BinaryenExpressionRef,
    value_type: BinaryenType,
) -> None:
    """ Sets the value type of a `store` expression. """
    lib.BinaryenStoreSetValueType(expr, value_type)


def ConstGetValueI32(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Const
    Gets the 32-bit integer value of an `i32.const` expression.
    """
    return lib.BinaryenConstGetValueI32(expr)


def ConstSetValueI32(
    expr: BinaryenExpressionRef,
    value: int,
) -> None:
    """ Sets the 32-bit integer value of an `i32.const` expression. """
    lib.BinaryenConstSetValueI32(expr, value)


def ConstGetValueI64(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the 64-bit integer value of an `i64.const` expression. """
    return lib.BinaryenConstGetValueI64(expr)


def ConstSetValueI64(
    expr: BinaryenExpressionRef,
    value: int,
) -> None:
    """ Sets the 64-bit integer value of an `i64.const` expression. """
    lib.BinaryenConstSetValueI64(expr, value)


def ConstGetValueI64Low(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the low 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    return lib.BinaryenConstGetValueI64Low(expr)


def ConstSetValueI64Low(
    expr: BinaryenExpressionRef,
    value_low: int,
) -> None:
    """
    Sets the low 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    lib.BinaryenConstSetValueI64Low(expr, value_low)


def ConstGetValueI64High(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the high 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    return lib.BinaryenConstGetValueI64High(expr)


def ConstSetValueI64High(
    expr: BinaryenExpressionRef,
    value_high: int,
) -> None:
    """
    Sets the high 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    lib.BinaryenConstSetValueI64High(expr, value_high)


def ConstGetValueF32(
    expr: BinaryenExpressionRef,
) -> float:
    """ Gets the 32-bit float value of a `f32.const` expression. """
    return lib.BinaryenConstGetValueF32(expr)


def ConstSetValueF32(
    expr: BinaryenExpressionRef,
    value: float,
) -> None:
    """ Sets the 32-bit float value of a `f32.const` expression. """
    lib.BinaryenConstSetValueF32(expr, value)


def ConstGetValueF64(
    expr: BinaryenExpressionRef,
) -> float:
    """ Gets the 64-bit float (double) value of a `f64.const` expression. """
    return lib.BinaryenConstGetValueF64(expr)


def ConstSetValueF64(
    expr: BinaryenExpressionRef,
    value: float,
) -> None:
    """ Sets the 64-bit float (double) value of a `f64.const` expression. """
    lib.BinaryenConstSetValueF64(expr, value)


def ConstGetValueV128(
    expr: BinaryenExpressionRef,
    out: List[int],
) -> None:
    """ Reads the 128-bit vector value of a `v128.const` expression. """
    lib.BinaryenConstGetValueV128(expr, out)


def ConstSetValueV128(
    expr: BinaryenExpressionRef,
    value: List[int],
) -> None:
    """ Sets the 128-bit vector value of a `v128.const` expression. """
    lib.BinaryenConstSetValueV128(expr, value)


def UnaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    Unary
    Gets the operation being performed by a unary expression.
    """
    return lib.BinaryenUnaryGetOp(expr)


def UnarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a unary expression. """
    lib.BinaryenUnarySetOp(expr, op)


def UnaryGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a unary expression. """
    return lib.BinaryenUnaryGetValue(expr)


def UnarySetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a unary expression. """
    lib.BinaryenUnarySetValue(expr, value_expr)


def BinaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    Binary
    Gets the operation being performed by a binary expression.
    """
    return lib.BinaryenBinaryGetOp(expr)


def BinarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a binary expression. """
    lib.BinaryenBinarySetOp(expr, op)


def BinaryGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the left expression of a binary expression. """
    return lib.BinaryenBinaryGetLeft(expr)


def BinarySetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a binary expression. """
    lib.BinaryenBinarySetLeft(expr, left_expr)


def BinaryGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a binary expression. """
    return lib.BinaryenBinaryGetRight(expr)


def BinarySetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a binary expression. """
    lib.BinaryenBinarySetRight(expr, right_expr)


def SelectGetIfTrue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Select
    Gets the expression becoming selected by a `select` expression if the
    condition turns out true.
    """
    return lib.BinaryenSelectGetIfTrue(expr)


def SelectSetIfTrue(
    expr: BinaryenExpressionRef,
    if_true_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression becoming selected by a `select` expression if the
    condition turns out true.
    """
    lib.BinaryenSelectSetIfTrue(expr, if_true_expr)


def SelectGetIfFalse(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression becoming selected by a `select` expression if the
    condition turns out false.
    """
    return lib.BinaryenSelectGetIfFalse(expr)


def SelectSetIfFalse(
    expr: BinaryenExpressionRef,
    if_false_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression becoming selected by a `select` expression if the
    condition turns out false.
    """
    lib.BinaryenSelectSetIfFalse(expr, if_false_expr)


def SelectGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the condition expression of a `select` expression. """
    return lib.BinaryenSelectGetCondition(expr)


def SelectSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of a `select` expression. """
    lib.BinaryenSelectSetCondition(expr, cond_expr)


def DropGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Drop
    Gets the value expression being dropped by a `drop` expression.
    """
    return lib.BinaryenDropGetValue(expr)


def DropSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression being dropped by a `drop` expression. """
    lib.BinaryenDropSetValue(expr, value_expr)


def ReturnGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Return
    Gets the value expression, if any, being returned by a `return` expression.
    """
    return lib.BinaryenReturnGetValue(expr)


def ReturnSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, being returned by a `return` expression. """
    lib.BinaryenReturnSetValue(expr, value_expr)


def AtomicRMWGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    AtomicRMW
    Gets the operation being performed by an atomic read-modify-write expression.
    """
    return lib.BinaryenAtomicRMWGetOp(expr)


def AtomicRMWSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetOp(expr, op)


def AtomicRMWGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes affected by an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetBytes(expr)


def AtomicRMWSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes affected by an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetBytes(expr, _bytes)


def AtomicRMWGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetOffset(expr)


def AtomicRMWSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetOffset(expr, offset)


def AtomicRMWGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetPtr(expr)


def AtomicRMWSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetPtr(expr, ptr_expr)


def AtomicRMWGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetValue(expr)


def AtomicRMWSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetValue(expr, value_expr)


def AtomicCmpxchgGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """
    AtomicCmpxchg
    Gets the number of bytes affected by an atomic compare and exchange
    expression.
    """
    return lib.BinaryenAtomicCmpxchgGetBytes(expr)


def AtomicCmpxchgSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """
    Sets the number of bytes affected by an atomic compare and exchange
    expression.
    """
    lib.BinaryenAtomicCmpxchgSetBytes(expr, _bytes)


def AtomicCmpxchgGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetOffset(expr)


def AtomicCmpxchgSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetOffset(expr, offset)


def AtomicCmpxchgGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetPtr(expr)


def AtomicCmpxchgSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetPtr(expr, ptr_expr)


def AtomicCmpxchgGetExpected(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression representing the expected value of an atomic compare and
    exchange expression.
    """
    return lib.BinaryenAtomicCmpxchgGetExpected(expr)


def AtomicCmpxchgSetExpected(
    expr: BinaryenExpressionRef,
    expected_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression representing the expected value of an atomic compare and
    exchange expression.
    """
    lib.BinaryenAtomicCmpxchgSetExpected(expr, expected_expr)


def AtomicCmpxchgGetReplacement(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the replacement expression of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetReplacement(expr)


def AtomicCmpxchgSetReplacement(
    expr: BinaryenExpressionRef,
    replacement_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the replacement expression of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetReplacement(expr, replacement_expr)


def AtomicWaitGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    AtomicWait
    Gets the pointer expression of an `memory.atomic.wait` expression.
    """
    return lib.BinaryenAtomicWaitGetPtr(expr)


def AtomicWaitSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetPtr(expr, ptr_expr)


def AtomicWaitGetExpected(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression representing the expected value of an
    `memory.atomic.wait` expression.
    """
    return lib.BinaryenAtomicWaitGetExpected(expr)


def AtomicWaitSetExpected(
    expr: BinaryenExpressionRef,
    expected_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression representing the expected value of an
    `memory.atomic.wait` expression.
    """
    lib.BinaryenAtomicWaitSetExpected(expr, expected_expr)


def AtomicWaitGetTimeout(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the timeout expression of an `memory.atomic.wait` expression. """
    return lib.BinaryenAtomicWaitGetTimeout(expr)


def AtomicWaitSetTimeout(
    expr: BinaryenExpressionRef,
    timeout_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the timeout expression of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetTimeout(expr, timeout_expr)


def AtomicWaitGetExpectedType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the expected type of an `memory.atomic.wait` expression. """
    return lib.BinaryenAtomicWaitGetExpectedType(expr)


def AtomicWaitSetExpectedType(
    expr: BinaryenExpressionRef,
    expected_type: BinaryenType,
) -> None:
    """ Sets the expected type of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetExpectedType(expr, expected_type)


def AtomicNotifyGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    AtomicNotify
    Gets the pointer expression of an `memory.atomic.notify` expression.
    """
    return lib.BinaryenAtomicNotifyGetPtr(expr)


def AtomicNotifySetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an `memory.atomic.notify` expression. """
    lib.BinaryenAtomicNotifySetPtr(expr, ptr_expr)


def AtomicNotifyGetNotifyCount(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the notify count expression of an `memory.atomic.notify` expression. """
    return lib.BinaryenAtomicNotifyGetNotifyCount(expr)


def AtomicNotifySetNotifyCount(
    expr: BinaryenExpressionRef,
    notify_count_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the notify count expression of an `memory.atomic.notify` expression. """
    lib.BinaryenAtomicNotifySetNotifyCount(expr, notify_count_expr)


def AtomicFenceGetOrder(
    expr: BinaryenExpressionRef,
) -> int:
    """
    AtomicFence
    Gets the order of an `atomic.fence` expression.
    """
    return lib.BinaryenAtomicFenceGetOrder(expr)


def AtomicFenceSetOrder(
    expr: BinaryenExpressionRef,
    order: int,
) -> None:
    """ Sets the order of an `atomic.fence` expression. """
    lib.BinaryenAtomicFenceSetOrder(expr, order)


def SIMDExtractGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDExtract
    Gets the operation being performed by a SIMD extract expression.
    """
    return lib.BinaryenSIMDExtractGetOp(expr)


def SIMDExtractSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD extract expression. """
    lib.BinaryenSIMDExtractSetOp(expr, op)


def SIMDExtractGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression a SIMD extract expression extracts from. """
    return lib.BinaryenSIMDExtractGetVec(expr)


def SIMDExtractSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression a SIMD extract expression extracts from. """
    lib.BinaryenSIMDExtractSetVec(expr, vec_expr)


def SIMDExtractGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the index of the extracted lane of a SIMD extract expression. """
    return lib.BinaryenSIMDExtractGetIndex(expr)


def SIMDExtractSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the index of the extracted lane of a SIMD extract expression. """
    lib.BinaryenSIMDExtractSetIndex(expr, index)


def SIMDReplaceGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDReplace
    Gets the operation being performed by a SIMD replace expression.
    """
    return lib.BinaryenSIMDReplaceGetOp(expr)


def SIMDReplaceSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD replace expression. """
    lib.BinaryenSIMDReplaceSetOp(expr, op)


def SIMDReplaceGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression a SIMD replace expression replaces in. """
    return lib.BinaryenSIMDReplaceGetVec(expr)


def SIMDReplaceSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression a SIMD replace expression replaces in. """
    lib.BinaryenSIMDReplaceSetVec(expr, vec_expr)


def SIMDReplaceGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the index of the replaced lane of a SIMD replace expression. """
    return lib.BinaryenSIMDReplaceGetIndex(expr)


def SIMDReplaceSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the index of the replaced lane of a SIMD replace expression. """
    lib.BinaryenSIMDReplaceSetIndex(expr, index)


def SIMDReplaceGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression a SIMD replace expression replaces with. """
    return lib.BinaryenSIMDReplaceGetValue(expr)


def SIMDReplaceSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression a SIMD replace expression replaces with. """
    lib.BinaryenSIMDReplaceSetValue(expr, value_expr)


def SIMDShuffleGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    SIMDShuffle
    Gets the left expression of a SIMD shuffle expression.
    """
    return lib.BinaryenSIMDShuffleGetLeft(expr)


def SIMDShuffleSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetLeft(expr, left_expr)


def SIMDShuffleGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a SIMD shuffle expression. """
    return lib.BinaryenSIMDShuffleGetRight(expr)


def SIMDShuffleSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetRight(expr, right_expr)


def SIMDShuffleGetMask(
    expr: BinaryenExpressionRef,
    mask: List[int],
) -> None:
    """ Gets the 128-bit mask of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleGetMask(expr, mask)


def SIMDShuffleSetMask(
    expr: BinaryenExpressionRef,
    mask: List[int],
) -> None:
    """ Sets the 128-bit mask of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetMask(expr, mask)


def SIMDTernaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDTernary
    Gets the operation being performed by a SIMD ternary expression.
    """
    return lib.BinaryenSIMDTernaryGetOp(expr)


def SIMDTernarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetOp(expr, op)


def SIMDTernaryGetA(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the first operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetA(expr)


def SIMDTernarySetA(
    expr: BinaryenExpressionRef,
    a_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the first operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetA(expr, a_expr)


def SIMDTernaryGetB(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the second operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetB(expr)


def SIMDTernarySetB(
    expr: BinaryenExpressionRef,
    b_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the second operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetB(expr, b_expr)


def SIMDTernaryGetC(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the third operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetC(expr)


def SIMDTernarySetC(
    expr: BinaryenExpressionRef,
    c_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the third operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetC(expr, c_expr)


def SIMDShiftGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDShift
    Gets the operation being performed by a SIMD shift expression.
    """
    return lib.BinaryenSIMDShiftGetOp(expr)


def SIMDShiftSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetOp(expr, op)


def SIMDShiftGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the expression being shifted by a SIMD shift expression. """
    return lib.BinaryenSIMDShiftGetVec(expr)


def SIMDShiftSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the expression being shifted by a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetVec(expr, vec_expr)


def SIMDShiftGetShift(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the expression representing the shift of a SIMD shift expression. """
    return lib.BinaryenSIMDShiftGetShift(expr)


def SIMDShiftSetShift(
    expr: BinaryenExpressionRef,
    shift_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the expression representing the shift of a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetShift(expr, shift_expr)


def SIMDLoadGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDLoad
    Gets the operation being performed by a SIMD load expression.
    """
    return lib.BinaryenSIMDLoadGetOp(expr)


def SIMDLoadSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD load expression. """
    lib.BinaryenSIMDLoadSetOp(expr, op)


def SIMDLoadGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetOffset(expr)


def SIMDLoadSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetOffset(expr, offset)


def SIMDLoadGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetAlign(expr)


def SIMDLoadSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetAlign(expr, align)


def SIMDLoadGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetPtr(expr)


def SIMDLoadSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetPtr(expr, ptr_expr)


def SIMDLoadStoreLaneGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    SIMDLoadStoreLane
    Gets the operation being performed by a SIMD load/store lane expression.
    """
    return lib.BinaryenSIMDLoadStoreLaneGetOp(expr)


def SIMDLoadStoreLaneSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetOp(expr, op)


def SIMDLoadStoreLaneGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetOffset(expr)


def SIMDLoadStoreLaneSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetOffset(expr, offset)


def SIMDLoadStoreLaneGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetAlign(expr)


def SIMDLoadStoreLaneSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetAlign(expr, align)


def SIMDLoadStoreLaneGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the lane index of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetIndex(expr)


def SIMDLoadStoreLaneSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the lane index of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetIndex(expr, index)


def SIMDLoadStoreLaneGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetPtr(expr)


def SIMDLoadStoreLaneSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetPtr(expr, ptr_expr)


def SIMDLoadStoreLaneGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetVec(expr)


def SIMDLoadStoreLaneSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetVec(expr, vec_expr)


def SIMDLoadStoreLaneIsStore(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    Gets whether a SIMD load/store lane expression performs a store. Otherwise it
    performs a load.
    """
    return lib.BinaryenSIMDLoadStoreLaneIsStore(expr)


def MemoryInitGetSegment(
    expr: BinaryenExpressionRef,
) -> int:
    """
    MemoryInit
    Gets the index of the segment being initialized by a `memory.init`
    expression.
    """
    return lib.BinaryenMemoryInitGetSegment(expr)


def MemoryInitSetSegment(
    expr: BinaryenExpressionRef,
    segment_index: int,
) -> None:
    """
    Sets the index of the segment being initialized by a `memory.init`
    expression.
    """
    lib.BinaryenMemoryInitSetSegment(expr, segment_index)


def MemoryInitGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the destination expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetDest(expr)


def MemoryInitSetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetDest(expr, dest_expr)


def MemoryInitGetOffset(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the offset expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetOffset(expr)


def MemoryInitSetOffset(
    expr: BinaryenExpressionRef,
    offset_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the offset expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetOffset(expr, offset_expr)


def MemoryInitGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the size expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetSize(expr)


def MemoryInitSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the size expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetSize(expr, size_expr)


def DataDropGetSegment(
    expr: BinaryenExpressionRef,
) -> int:
    """
    DataDrop
    Gets the index of the segment being dropped by a `data.drop` expression.
    """
    return lib.BinaryenDataDropGetSegment(expr)


def DataDropSetSegment(
    expr: BinaryenExpressionRef,
    segment_index: int,
) -> None:
    """ Sets the index of the segment being dropped by a `data.drop` expression. """
    lib.BinaryenDataDropSetSegment(expr, segment_index)


def MemoryCopyGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    MemoryCopy
    Gets the destination expression of a `memory.copy` expression.
    """
    return lib.BinaryenMemoryCopyGetDest(expr)


def MemoryCopySetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.copy` expression. """
    lib.BinaryenMemoryCopySetDest(expr, dest_expr)


def MemoryCopyGetSource(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the source expression of a `memory.copy` expression. """
    return lib.BinaryenMemoryCopyGetSource(expr)


def MemoryCopySetSource(
    expr: BinaryenExpressionRef,
    source_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the source expression of a `memory.copy` expression. """
    lib.BinaryenMemoryCopySetSource(expr, source_expr)


def MemoryCopyGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the size expression (number of bytes copied) of a `memory.copy`
    expression.
    """
    return lib.BinaryenMemoryCopyGetSize(expr)


def MemoryCopySetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the size expression (number of bytes copied) of a `memory.copy`
    expression.
    """
    lib.BinaryenMemoryCopySetSize(expr, size_expr)


def MemoryFillGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    MemoryFill
    Gets the destination expression of a `memory.fill` expression.
    """
    return lib.BinaryenMemoryFillGetDest(expr)


def MemoryFillSetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.fill` expression. """
    lib.BinaryenMemoryFillSetDest(expr, dest_expr)


def MemoryFillGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `memory.fill` expression. """
    return lib.BinaryenMemoryFillGetValue(expr)


def MemoryFillSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `memory.fill` expression. """
    lib.BinaryenMemoryFillSetValue(expr, value_expr)


def MemoryFillGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the size expression (number of bytes filled) of a `memory.fill`
    expression.
    """
    return lib.BinaryenMemoryFillGetSize(expr)


def MemoryFillSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the size expression (number of bytes filled) of a `memory.fill`
    expression.
    """
    lib.BinaryenMemoryFillSetSize(expr, size_expr)


def RefIsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    RefIs
    Gets the operation performed by a `ref.is_*` expression.
    """
    return lib.BinaryenRefIsGetOp(expr)


def RefIsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation performed by a `ref.is_*` expression. """
    lib.BinaryenRefIsSetOp(expr, op)


def RefIsGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression tested by a `ref.is_*` expression. """
    return lib.BinaryenRefIsGetValue(expr)


def RefIsSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression tested by a `ref.is_*` expression. """
    lib.BinaryenRefIsSetValue(expr, value_expr)


def RefAsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """
    RefAs
    Gets the operation performed by a `ref.as_*` expression.
    """
    return lib.BinaryenRefAsGetOp(expr)


def RefAsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation performed by a `ref.as_*` expression. """
    lib.BinaryenRefAsSetOp(expr, op)


def RefAsGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression tested by a `ref.as_*` expression. """
    return lib.BinaryenRefAsGetValue(expr)


def RefAsSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression tested by a `ref.as_*` expression. """
    lib.BinaryenRefAsSetValue(expr, value_expr)


def RefFuncGetFunc(
    expr: BinaryenExpressionRef,
) -> str:
    """
    RefFunc
    Gets the name of the function being wrapped by a `ref.func` expression.
    """
    return lib.BinaryenRefFuncGetFunc(expr)


def RefFuncSetFunc(
    expr: BinaryenExpressionRef,
    func_name: str,
) -> None:
    """ Sets the name of the function being wrapped by a `ref.func` expression. """
    lib.BinaryenRefFuncSetFunc(expr, func_name.encode())


def RefEqGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    RefEq
    Gets the left expression of a `ref.eq` expression.
    """
    return lib.BinaryenRefEqGetLeft(expr)


def RefEqSetLeft(
    expr: BinaryenExpressionRef,
    left: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a `ref.eq` expression. """
    lib.BinaryenRefEqSetLeft(expr, left)


def RefEqGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a `ref.eq` expression. """
    return lib.BinaryenRefEqGetRight(expr)


def RefEqSetRight(
    expr: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a `ref.eq` expression. """
    lib.BinaryenRefEqSetRight(expr, right)


def TryGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Try
    Gets the name (label) of a `try` expression.
    """
    return lib.BinaryenTryGetName(expr)


def TrySetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `try` expression. """
    lib.BinaryenTrySetName(expr, name.encode())


def TryGetBody(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the body expression of a `try` expression. """
    return lib.BinaryenTryGetBody(expr)


def TrySetBody(
    expr: BinaryenExpressionRef,
    body_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the body expression of a `try` expression. """
    lib.BinaryenTrySetBody(expr, body_expr)


def TryGetNumCatchTags(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Gets the number of catch blocks (= the number of catch tags) of a `try`
    expression.
    """
    return lib.BinaryenTryGetNumCatchTags(expr)


def TryGetNumCatchBodies(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of catch/catch_all blocks of a `try` expression. """
    return lib.BinaryenTryGetNumCatchBodies(expr)


def TryGetCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """ Gets the catch tag at the specified index of a `try` expression. """
    return lib.BinaryenTryGetCatchTagAt(expr, index)


def TrySetCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_tag: str,
) -> None:
    """ Sets the catch tag at the specified index of a `try` expression. """
    lib.BinaryenTrySetCatchTagAt(expr, index, catch_tag.encode())


def TryAppendCatchTag(
    expr: BinaryenExpressionRef,
    catch_tag: str,
) -> BinaryenIndex:
    """ Appends a catch tag to a `try` expression, returning its insertion index. """
    return lib.BinaryenTryAppendCatchTag(expr, catch_tag.encode())


def TryInsertCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_tag: str,
) -> None:
    """
    Inserts a catch tag at the specified index of a `try` expression, moving
    existing catch tags including the one previously at that index one index up.
    """
    lib.BinaryenTryInsertCatchTagAt(expr, index, catch_tag.encode())


def TryRemoveCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Removes the catch tag at the specified index of a `try` expression, moving
    all subsequent catch tags one index down. Returns the tag.
    """
    return lib.BinaryenTryRemoveCatchTagAt(expr, index)


def TryGetCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the catch body expression at the specified index of a `try` expression. """
    return lib.BinaryenTryGetCatchBodyAt(expr, index)


def TrySetCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the catch body expression at the specified index of a `try` expression. """
    lib.BinaryenTrySetCatchBodyAt(expr, index, catch_expr)


def TryAppendCatchBody(
    expr: BinaryenExpressionRef,
    catch_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends a catch expression to a `try` expression, returning its insertion
    index.
    """
    return lib.BinaryenTryAppendCatchBody(expr, catch_expr)


def TryInsertCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts a catch expression at the specified index of a `try` expression,
    moving existing catch bodies including the one previously at that index one
    index up.
    """
    lib.BinaryenTryInsertCatchBodyAt(expr, index, catch_expr)


def TryRemoveCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the catch expression at the specified index of a `try` expression,
    moving all subsequent catch bodies one index down. Returns the catch
    expression.
    """
    return lib.BinaryenTryRemoveCatchBodyAt(expr, index)


def TryHasCatchAll(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `try` expression has a catch_all clause. """
    return lib.BinaryenTryHasCatchAll(expr)


def TryGetDelegateTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the target label of a `delegate`. """
    return lib.BinaryenTryGetDelegateTarget(expr)


def TrySetDelegateTarget(
    expr: BinaryenExpressionRef,
    delegate_target: str,
) -> None:
    """ Sets the target label of a `delegate`. """
    lib.BinaryenTrySetDelegateTarget(expr, delegate_target.encode())


def TryIsDelegate(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `try` expression is a try-delegate. """
    return lib.BinaryenTryIsDelegate(expr)


def ThrowGetTag(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Throw
    Gets the name of the tag being thrown by a `throw` expression.
    """
    return lib.BinaryenThrowGetTag(expr)


def ThrowSetTag(
    expr: BinaryenExpressionRef,
    tag_name: str,
) -> None:
    """ Sets the name of the tag being thrown by a `throw` expression. """
    lib.BinaryenThrowSetTag(expr, tag_name.encode())


def ThrowGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `throw` expression. """
    return lib.BinaryenThrowGetNumOperands(expr)


def ThrowGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand at the specified index of a `throw` expression. """
    return lib.BinaryenThrowGetOperandAt(expr, index)


def ThrowSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand at the specified index of a `throw` expression. """
    lib.BinaryenThrowSetOperandAt(expr, index, operand_expr)


def ThrowAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `throw` expression, returning its
    insertion index.
    """
    return lib.BinaryenThrowAppendOperand(expr, operand_expr)


def ThrowInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `throw` expression,
    moving existing operands including the one previously at that index one index
    up.
    """
    lib.BinaryenThrowInsertOperandAt(expr, index, operand_expr)


def ThrowRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `throw`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenThrowRemoveOperandAt(expr, index)


def RethrowGetTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """
    Rethrow
    Gets the target catch's corresponding try label of a `rethrow` expression.
    """
    return lib.BinaryenRethrowGetTarget(expr)


def RethrowSetTarget(
    expr: BinaryenExpressionRef,
    target: str,
) -> None:
    """ Sets the target catch's corresponding try label of a `rethrow` expression. """
    lib.BinaryenRethrowSetTarget(expr, target.encode())


def TupleMakeGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    TupleMake
    Gets the number of operands of a `tuple.make` expression.
    """
    return lib.BinaryenTupleMakeGetNumOperands(expr)


def TupleMakeGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand at the specified index of a `tuple.make` expression. """
    return lib.BinaryenTupleMakeGetOperandAt(expr, index)


def TupleMakeSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand at the specified index of a `tuple.make` expression. """
    lib.BinaryenTupleMakeSetOperandAt(expr, index, operand_expr)


def TupleMakeAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `tuple.make` expression, returning its
    insertion index.
    """
    return lib.BinaryenTupleMakeAppendOperand(expr, operand_expr)


def TupleMakeInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `tuple.make`
    expression, moving existing operands including the one previously at that
    index one index up.
    """
    lib.BinaryenTupleMakeInsertOperandAt(expr, index, operand_expr)


def TupleMakeRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `tuple.make`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenTupleMakeRemoveOperandAt(expr, index)


def TupleExtractGetTuple(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    TupleExtract
    Gets the tuple extracted from of a `tuple.extract` expression.
    """
    return lib.BinaryenTupleExtractGetTuple(expr)


def TupleExtractSetTuple(
    expr: BinaryenExpressionRef,
    tuple_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the tuple extracted from of a `tuple.extract` expression. """
    lib.BinaryenTupleExtractSetTuple(expr, tuple_expr)


def TupleExtractGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the index extracted at of a `tuple.extract` expression. """
    return lib.BinaryenTupleExtractGetIndex(expr)


def TupleExtractSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the index extracted at of a `tuple.extract` expression. """
    lib.BinaryenTupleExtractSetIndex(expr, index)


def I31NewGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    I31New
    Gets the value expression of an `i31.new` expression.
    """
    return lib.BinaryenI31NewGetValue(expr)


def I31NewSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of an `i31.new` expression. """
    lib.BinaryenI31NewSetValue(expr, value_expr)


def I31GetGetI31(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    I31Get
    Gets the i31 expression of an `i31.get` expression.
    """
    return lib.BinaryenI31GetGetI31(expr)


def I31GetSetI31(
    expr: BinaryenExpressionRef,
    i31_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the i31 expression of an `i31.get` expression. """
    lib.BinaryenI31GetSetI31(expr, i31_expr)


def I31GetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether an `i31.get` expression returns a signed value (`_s`). """
    return lib.BinaryenI31GetIsSigned(expr)


def I31GetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    """ Sets whether an `i31.get` expression returns a signed value (`_s`). """
    lib.BinaryenI31GetSetSigned(expr, signed_)


def CallRefGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ CallRef """
    return lib.BinaryenCallRefGetNumOperands(expr)


def CallRefGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefGetOperandAt(expr, index)


def CallRefSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefSetOperandAt(expr, index, operand_expr)


def CallRefAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenCallRefAppendOperand(expr, operand_expr)


def CallRefInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefInsertOperandAt(expr, index, operand_expr)


def CallRefRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefRemoveOperandAt(expr, index)


def CallRefGetTarget(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefGetTarget(expr)


def CallRefSetTarget(
    expr: BinaryenExpressionRef,
    target_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefSetTarget(expr, target_expr)


def CallRefIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenCallRefIsReturn(expr)


def CallRefSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    lib.BinaryenCallRefSetReturn(expr, is_return)


def RefTestGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ RefTest """
    return lib.BinaryenRefTestGetRef(expr)


def RefTestSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenRefTestSetRef(expr, ref_expr)


def RefTestGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenRefTestGetIntendedType(expr)


def RefTestSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenRefTestSetIntendedType(expr, intended_type)


def RefCastGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ RefCast """
    return lib.BinaryenRefCastGetRef(expr)


def RefCastSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenRefCastSetRef(expr, ref_expr)


def RefCastGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenRefCastGetIntendedType(expr)


def RefCastSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenRefCastSetIntendedType(expr, intended_type)


def BrOnGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ BrOn """
    return lib.BinaryenBrOnGetOp(expr)


def BrOnSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenBrOnSetOp(expr, op)


def BrOnGetName(
    expr: BinaryenExpressionRef,
) -> str:
    return lib.BinaryenBrOnGetName(expr)


def BrOnSetName(
    expr: BinaryenExpressionRef,
    name_str: str,
) -> None:
    lib.BinaryenBrOnSetName(expr, name_str.encode())


def BrOnGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenBrOnGetRef(expr)


def BrOnSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenBrOnSetRef(expr, ref_expr)


def BrOnGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenBrOnGetIntendedType(expr)


def BrOnSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenBrOnSetIntendedType(expr, intended_type)


def StructNewGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ StructNew """
    return lib.BinaryenStructNewGetNumOperands(expr)


def StructNewGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNewGetOperandAt(expr, index)


def StructNewSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructNewSetOperandAt(expr, index, operand_expr)


def StructNewAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenStructNewAppendOperand(expr, operand_expr)


def StructNewInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructNewInsertOperandAt(expr, index, operand_expr)


def StructNewRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNewRemoveOperandAt(expr, index)


def StructGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ StructGet """
    return lib.BinaryenStructGetGetIndex(expr)


def StructGetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    lib.BinaryenStructGetSetIndex(expr, index)


def StructGetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructGetGetRef(expr)


def StructGetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructGetSetRef(expr, ref_expr)


def StructGetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenStructGetIsSigned(expr)


def StructGetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    lib.BinaryenStructGetSetSigned(expr, signed_)


def StructSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ StructSet """
    return lib.BinaryenStructSetGetIndex(expr)


def StructSetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    lib.BinaryenStructSetSetIndex(expr, index)


def StructSetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSetGetRef(expr)


def StructSetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructSetSetRef(expr, ref_expr)


def StructSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSetGetValue(expr)


def StructSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructSetSetValue(expr, value_expr)


def ArrayNewGetInit(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ ArrayNew """
    return lib.BinaryenArrayNewGetInit(expr)


def ArrayNewSetInit(
    expr: BinaryenExpressionRef,
    init_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayNewSetInit(expr, init_expr)


def ArrayNewGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayNewGetSize(expr)


def ArrayNewSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayNewSetSize(expr, size_expr)


def ArrayInitGetNumValues(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ ArrayInit """
    return lib.BinaryenArrayInitGetNumValues(expr)


def ArrayInitGetValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayInitGetValueAt(expr, index)


def ArrayInitSetValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayInitSetValueAt(expr, index, value_expr)


def ArrayInitAppendValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenArrayInitAppendValue(expr, value_expr)


def ArrayInitInsertValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayInitInsertValueAt(expr, index, value_expr)


def ArrayInitRemoveValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayInitRemoveValueAt(expr, index)


def ArrayGetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ ArrayGet """
    return lib.BinaryenArrayGetGetRef(expr)


def ArrayGetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayGetSetRef(expr, ref_expr)


def ArrayGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayGetGetIndex(expr)


def ArrayGetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayGetSetIndex(expr, index_expr)


def ArrayGetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenArrayGetIsSigned(expr)


def ArrayGetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    lib.BinaryenArrayGetSetSigned(expr, signed_)


def ArraySetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ ArraySet """
    return lib.BinaryenArraySetGetRef(expr)


def ArraySetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetRef(expr, ref_expr)


def ArraySetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySetGetIndex(expr)


def ArraySetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetIndex(expr, index_expr)


def ArraySetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySetGetValue(expr)


def ArraySetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetValue(expr, value_expr)


def ArrayLenGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ ArrayLen """
    return lib.BinaryenArrayLenGetRef(expr)


def ArrayLenSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayLenSetRef(expr, ref_expr)


def ArrayCopyGetDestRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ ArrayCopy """
    return lib.BinaryenArrayCopyGetDestRef(expr)


def ArrayCopySetDestRef(
    expr: BinaryenExpressionRef,
    dest_ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetDestRef(expr, dest_ref_expr)


def ArrayCopyGetDestIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetDestIndex(expr)


def ArrayCopySetDestIndex(
    expr: BinaryenExpressionRef,
    dest_index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetDestIndex(expr, dest_index_expr)


def ArrayCopyGetSrcRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetSrcRef(expr)


def ArrayCopySetSrcRef(
    expr: BinaryenExpressionRef,
    src_ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetSrcRef(expr, src_ref_expr)


def ArrayCopyGetSrcIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetSrcIndex(expr)


def ArrayCopySetSrcIndex(
    expr: BinaryenExpressionRef,
    src_index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetSrcIndex(expr, src_index_expr)


def ArrayCopyGetLength(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetLength(expr)


def ArrayCopySetLength(
    expr: BinaryenExpressionRef,
    length_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetLength(expr, length_expr)


def StringNewGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringNew """
    return lib.BinaryenStringNewGetOp(expr)


def StringNewSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringNewSetOp(expr, op)


def StringNewGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetPtr(expr)


def StringNewSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetPtr(expr, ptr_expr)


def StringNewGetLength(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetLength(expr)


def StringNewSetLength(
    expr: BinaryenExpressionRef,
    length_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetLength(expr, length_expr)


def StringNewGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetStart(expr)


def StringNewSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetStart(expr, start_expr)


def StringNewGetEnd(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetEnd(expr)


def StringNewSetEnd(
    expr: BinaryenExpressionRef,
    end_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetEnd(expr, end_expr)


def StringConstGetString(
    expr: BinaryenExpressionRef,
) -> str:
    """ StringConst """
    return lib.BinaryenStringConstGetString(expr)


def StringConstSetString(
    expr: BinaryenExpressionRef,
    string_str: str,
) -> None:
    lib.BinaryenStringConstSetString(expr, string_str.encode())


def StringMeasureGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringMeasure """
    return lib.BinaryenStringMeasureGetOp(expr)


def StringMeasureSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringMeasureSetOp(expr, op)


def StringMeasureGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringMeasureGetRef(expr)


def StringMeasureSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringMeasureSetRef(expr, ref_expr)


def StringEncodeGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringEncode """
    return lib.BinaryenStringEncodeGetOp(expr)


def StringEncodeSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringEncodeSetOp(expr, op)


def StringEncodeGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetRef(expr)


def StringEncodeSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetRef(expr, ref_expr)


def StringEncodeGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetPtr(expr)


def StringEncodeSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetPtr(expr, ptr_expr)


def StringEncodeGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetStart(expr)


def StringEncodeSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetStart(expr, start_expr)


def StringConcatGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringConcat """
    return lib.BinaryenStringConcatGetLeft(expr)


def StringConcatSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringConcatSetLeft(expr, left_expr)


def StringConcatGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConcatGetRight(expr)


def StringConcatSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringConcatSetRight(expr, right_expr)


def StringEqGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringEq """
    return lib.BinaryenStringEqGetLeft(expr)


def StringEqSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEqSetLeft(expr, left_expr)


def StringEqGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEqGetRight(expr)


def StringEqSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEqSetRight(expr, right_expr)


def StringAsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringAs """
    return lib.BinaryenStringAsGetOp(expr)


def StringAsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringAsSetOp(expr, op)


def StringAsGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringAsGetRef(expr)


def StringAsSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringAsSetRef(expr, ref_expr)


def StringWTF8AdvanceGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringWTF8Advance """
    return lib.BinaryenStringWTF8AdvanceGetRef(expr)


def StringWTF8AdvanceSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetRef(expr, ref_expr)


def StringWTF8AdvanceGetPos(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8AdvanceGetPos(expr)


def StringWTF8AdvanceSetPos(
    expr: BinaryenExpressionRef,
    pos_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetPos(expr, pos_expr)


def StringWTF8AdvanceGetBytes(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8AdvanceGetBytes(expr)


def StringWTF8AdvanceSetBytes(
    expr: BinaryenExpressionRef,
    bytes_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetBytes(expr, bytes_expr)


def StringWTF16GetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringWTF16Get """
    return lib.BinaryenStringWTF16GetGetRef(expr)


def StringWTF16GetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF16GetSetRef(expr, ref_expr)


def StringWTF16GetGetPos(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF16GetGetPos(expr)


def StringWTF16GetSetPos(
    expr: BinaryenExpressionRef,
    pos_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF16GetSetPos(expr, pos_expr)


def StringIterNextGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringIterNext """
    return lib.BinaryenStringIterNextGetRef(expr)


def StringIterNextSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterNextSetRef(expr, ref_expr)


def StringIterMoveGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringIterMove """
    return lib.BinaryenStringIterMoveGetOp(expr)


def StringIterMoveSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringIterMoveSetOp(expr, op)


def StringIterMoveGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMoveGetRef(expr)


def StringIterMoveSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterMoveSetRef(expr, ref_expr)


def StringIterMoveGetNum(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMoveGetNum(expr)


def StringIterMoveSetNum(
    expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterMoveSetNum(expr, len(expr))


def StringSliceWTFGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ StringSliceWTF """
    return lib.BinaryenStringSliceWTFGetOp(expr)


def StringSliceWTFSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringSliceWTFSetOp(expr, op)


def StringSliceWTFGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetRef(expr)


def StringSliceWTFSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetRef(expr, ref_expr)


def StringSliceWTFGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetStart(expr)


def StringSliceWTFSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetStart(expr, start_expr)


def StringSliceWTFGetEnd(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetEnd(expr)


def StringSliceWTFSetEnd(
    expr: BinaryenExpressionRef,
    end_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetEnd(expr, end_expr)


def StringSliceIterGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ StringSliceIter """
    return lib.BinaryenStringSliceIterGetRef(expr)


def StringSliceIterSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceIterSetRef(expr, ref_expr)


def StringSliceIterGetNum(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceIterGetNum(expr)


def StringSliceIterSetNum(
    expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceIterSetNum(expr, len(expr))


def AddFunction(
    module: BinaryenModuleRef,
    name: str,
    params: BinaryenType,
    results: BinaryenType,
    var_types: List[BinaryenType],
    body: BinaryenExpressionRef,
) -> BinaryenFunctionRef:
    """
    Adds a function to the module. This is thread-safe.
    @varTypes: the types of variables. In WebAssembly, vars share
    an index space with params. In other words, params come from
    the function type, and vars are provided in this call, and
    together they are all the locals. The order is first params
    and then vars, so if you have one param it will be at index
    0 (and written $0), and if you also have 2 vars they will be
    at indexes 1 and 2, etc., that is, they share an index space.
    """
    return lib.BinaryenAddFunction(module, name.encode(), params, results, var_types, len(var_types), body)


def GetFunction(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenFunctionRef:
    """
    Gets a function reference by name. Returns NULL if the function does not
    exist.
    """
    return lib.BinaryenGetFunction(module, name.encode())


def RemoveFunction(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a function by name. """
    lib.BinaryenRemoveFunction(module, name.encode())


def GetNumFunctions(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of functions in the module. """
    return lib.BinaryenGetNumFunctions(module)


def GetFunctionByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenFunctionRef:
    """ Gets the function at the specified index. """
    return lib.BinaryenGetFunctionByIndex(module, index)


def AddFunctionImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> None:
    """
    Imports
    These either create a new entity (function/table/memory/etc.) and
    mark it as an import, or, if an entity already exists with internalName then
    the existing entity is turned into an import.
    """
    lib.BinaryenAddFunctionImport(module, internal_name.encode(), external_module_name.encode(), external_base_name.encode(), params, results)


def AddTableImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
) -> None:
    lib.BinaryenAddTableImport(module, internal_name.encode(), external_module_name.encode(), external_base_name.encode())


def AddMemoryImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    shared: int,
) -> None:
    lib.BinaryenAddMemoryImport(module, internal_name.encode(), external_module_name.encode(), external_base_name.encode(), shared)


def AddGlobalImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    global_type: BinaryenType,
    mutable_: bool,
) -> None:
    lib.BinaryenAddGlobalImport(module, internal_name.encode(), external_module_name.encode(), external_base_name.encode(), global_type, mutable_)


def AddTagImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> None:
    lib.BinaryenAddTagImport(module, internal_name.encode(), external_module_name.encode(), external_base_name.encode(), params, results)


def AddFunctionExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a function export to the module. """
    return lib.BinaryenAddFunctionExport(module, internal_name.encode(), external_name.encode())


def AddTableExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a table export to the module. """
    return lib.BinaryenAddTableExport(module, internal_name.encode(), external_name.encode())


def AddMemoryExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a memory export to the module. """
    return lib.BinaryenAddMemoryExport(module, internal_name.encode(), external_name.encode())


def AddGlobalExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a global export to the module. """
    return lib.BinaryenAddGlobalExport(module, internal_name.encode(), external_name.encode())


def AddTagExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a tag export to the module. """
    return lib.BinaryenAddTagExport(module, internal_name.encode(), external_name.encode())


def GetExport(
    module: BinaryenModuleRef,
    external_name: str,
) -> BinaryenExportRef:
    """
    Gets an export reference by external name. Returns NULL if the export does
    not exist.
    """
    return lib.BinaryenGetExport(module, external_name.encode())


def RemoveExport(
    module: BinaryenModuleRef,
    external_name: str,
) -> None:
    """ Removes an export by external name. """
    lib.BinaryenRemoveExport(module, external_name.encode())


def GetNumExports(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of exports in the module. """
    return lib.BinaryenGetNumExports(module)


def GetExportByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenExportRef:
    """ Gets the export at the specified index. """
    return lib.BinaryenGetExportByIndex(module, index)


def AddGlobal(
    module: BinaryenModuleRef,
    name: str,
    _type: BinaryenType,
    mutable_: bool,
    init: BinaryenExpressionRef,
) -> BinaryenGlobalRef:
    """ Adds a global to the module. """
    return lib.BinaryenAddGlobal(module, name.encode(), _type, mutable_, init)


def GetGlobal(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenGlobalRef:
    """ Gets a global reference by name. Returns NULL if the global does not exist. """
    return lib.BinaryenGetGlobal(module, name.encode())


def RemoveGlobal(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a global by name. """
    lib.BinaryenRemoveGlobal(module, name.encode())


def GetNumGlobals(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of globals in the module. """
    return lib.BinaryenGetNumGlobals(module)


def GetGlobalByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenGlobalRef:
    """ Gets the global at the specified index. """
    return lib.BinaryenGetGlobalByIndex(module, index)


def AddTag(
    module: BinaryenModuleRef,
    name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenTagRef:
    """ Adds a tag to the module. """
    return lib.BinaryenAddTag(module, name.encode(), params, results)


def GetTag(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenTagRef:
    """ Gets a tag reference by name. Returns NULL if the tag does not exist. """
    return lib.BinaryenGetTag(module, name.encode())


def RemoveTag(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a tag by name. """
    lib.BinaryenRemoveTag(module, name.encode())


def AddTable(
    module: BinaryenModuleRef,
    table: str,
    initial: BinaryenIndex,
    maximum: BinaryenIndex,
    table_type: BinaryenType,
) -> BinaryenTableRef:
    return lib.BinaryenAddTable(module, table.encode(), initial, maximum, table_type)


def RemoveTable(
    module: BinaryenModuleRef,
    table: str,
) -> None:
    lib.BinaryenRemoveTable(module, table.encode())


def GetNumTables(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    return lib.BinaryenGetNumTables(module)


def GetTable(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenTableRef:
    return lib.BinaryenGetTable(module, name.encode())


def GetTableByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenTableRef:
    return lib.BinaryenGetTableByIndex(module, index)


def AddActiveElementSegment(
    module: BinaryenModuleRef,
    table: str,
    name: str,
    func_names: List[str],
    offset: BinaryenExpressionRef,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenAddActiveElementSegment(module, table.encode(), name.encode(), [item.encode() for item in func_names], len(func_names), offset)


def AddPassiveElementSegment(
    module: BinaryenModuleRef,
    name: str,
    func_names: List[str],
) -> BinaryenElementSegmentRef:
    return lib.BinaryenAddPassiveElementSegment(module, name.encode(), [item.encode() for item in func_names], len(func_names))


def RemoveElementSegment(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    lib.BinaryenRemoveElementSegment(module, name.encode())


def GetNumElementSegments(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    return lib.BinaryenGetNumElementSegments(module)


def GetElementSegment(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenGetElementSegment(module, name.encode())


def GetElementSegmentByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenGetElementSegmentByIndex(module, index)


def SetMemory(
    module: BinaryenModuleRef,
    initial: BinaryenIndex,
    maximum: BinaryenIndex,
    export_name: str,
    segments: List[str],
    segment_passive: List[bool],
    segment_offsets: List[BinaryenExpressionRef],
    segment_sizes: List[BinaryenIndex],
    shared: bool,
    memory64: bool,
    name: str,
) -> None:
    """
    This will create a memory, overwriting any existing memory
    Each memory has data in segments, a start offset in segmentOffsets, and a
    size in segmentSizes. exportName can be NULL
    """
    lib.BinaryenSetMemory(module, initial, maximum, export_name.encode(), [item.encode() for item in segments], segment_passive, segment_offsets, segment_sizes, len(segment_sizes), shared, memory64, name.encode())


def HasMemory(
    module: BinaryenModuleRef,
) -> bool:
    return lib.BinaryenHasMemory(module)


def MemoryGetInitial(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenIndex:
    return lib.BinaryenMemoryGetInitial(module, name.encode())


def MemoryHasMax(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryHasMax(module, name.encode())


def MemoryGetMax(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenIndex:
    return lib.BinaryenMemoryGetMax(module, name.encode())


def MemoryImportGetModule(
    module: BinaryenModuleRef,
    name: str,
) -> str:
    return lib.BinaryenMemoryImportGetModule(module, name.encode())


def MemoryImportGetBase(
    module: BinaryenModuleRef,
    name: str,
) -> str:
    return lib.BinaryenMemoryImportGetBase(module, name.encode())


def MemoryIsShared(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryIsShared(module, name.encode())


def MemoryIs64(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryIs64(module, name.encode())


def GetNumMemorySegments(
    module: BinaryenModuleRef,
) -> int:
    """ Memory segments. Query utilities. """
    return lib.BinaryenGetNumMemorySegments(module)


def GetMemorySegmentByteOffset(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> int:
    return lib.BinaryenGetMemorySegmentByteOffset(module, _id)


def GetMemorySegmentByteLength(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> int:
    return lib.BinaryenGetMemorySegmentByteLength(module, _id)


def GetMemorySegmentPassive(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> bool:
    return lib.BinaryenGetMemorySegmentPassive(module, _id)


def CopyMemorySegmentData(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
    buffer: str,
) -> None:
    lib.BinaryenCopyMemorySegmentData(module, _id, buffer.encode())


def SetStart(
    module: BinaryenModuleRef,
    start: BinaryenFunctionRef,
) -> None:
    """ Start function. One per module """
    lib.BinaryenSetStart(module, start)


def ModuleGetFeatures(
    module: BinaryenModuleRef,
) -> BinaryenFeatures:
    """
    Features
    These control what features are allowed when validation and in passes.
    """
    return lib.BinaryenModuleGetFeatures(module)


def ModuleSetFeatures(
    module: BinaryenModuleRef,
    features: BinaryenFeatures,
) -> None:
    lib.BinaryenModuleSetFeatures(module, features)


def ModuleParse(
    text: str,
) -> BinaryenModuleRef:
    """
    
    ========== Module Operations ==========
    
    Parse a module in s-expression text format
    """
    return lib.BinaryenModuleParse(text.encode())


def ModulePrint(
    module: BinaryenModuleRef,
) -> None:
    """ Print a module to stdout in s-expression text format. Useful for debugging. """
    lib.BinaryenModulePrint(module)


def ModulePrintStackIR(
    module: BinaryenModuleRef,
    optimize: bool,
) -> None:
    """ Print a module to stdout in stack IR text format. Useful for debugging. """
    lib.BinaryenModulePrintStackIR(module, optimize)


def ModulePrintAsmjs(
    module: BinaryenModuleRef,
) -> None:
    """ Print a module to stdout in asm.js syntax. """
    lib.BinaryenModulePrintAsmjs(module)


def ModuleValidate(
    module: BinaryenModuleRef,
) -> bool:
    """
    Validate a module, showing errors on problems.
    @return 0 if an error occurred, 1 if validated succesfully
    """
    return lib.BinaryenModuleValidate(module)


def ModuleOptimize(
    module: BinaryenModuleRef,
) -> None:
    """
    Runs the standard optimization passes on the module. Uses the currently set
    global optimize and shrink level.
    """
    lib.BinaryenModuleOptimize(module)


def ModuleUpdateMaps(
    module: BinaryenModuleRef,
) -> None:
    """
    Updates the internal name mapping logic in a module. This must be called
    after renaming module elements.
    """
    lib.BinaryenModuleUpdateMaps(module)


def GetOptimizeLevel() -> int:
    """
    Gets the currently set optimize level. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
    """
    return lib.BinaryenGetOptimizeLevel()


def SetOptimizeLevel(
    level: int,
) -> None:
    """
    Sets the optimization level to use. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
    """
    lib.BinaryenSetOptimizeLevel(level)


def GetShrinkLevel() -> int:
    """
    Gets the currently set shrink level. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -Os (default), -Oz.
    """
    return lib.BinaryenGetShrinkLevel()


def SetShrinkLevel(
    level: int,
) -> None:
    """
    Sets the shrink level to use. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -Os (default), -Oz.
    """
    lib.BinaryenSetShrinkLevel(level)


def GetDebugInfo() -> bool:
    """
    Gets whether generating debug information is currently enabled or not.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetDebugInfo()


def SetDebugInfo(
    on: bool,
) -> None:
    """
    Enables or disables debug information in emitted binaries.
    Applies to all modules, globally.
    """
    lib.BinaryenSetDebugInfo(on)


def GetLowMemoryUnused() -> bool:
    """
    Gets whether the low 1K of memory can be considered unused when optimizing.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetLowMemoryUnused()


def SetLowMemoryUnused(
    on: bool,
) -> None:
    """
    Enables or disables whether the low 1K of memory can be considered unused
    when optimizing. Applies to all modules, globally.
    """
    lib.BinaryenSetLowMemoryUnused(on)


def GetZeroFilledMemory() -> bool:
    """ Gets whether to assume that an imported memory is zero-initialized. """
    return lib.BinaryenGetZeroFilledMemory()


def SetZeroFilledMemory(
    on: bool,
) -> None:
    """
    Enables or disables whether to assume that an imported memory is
    zero-initialized.
    """
    lib.BinaryenSetZeroFilledMemory(on)


def GetFastMath() -> bool:
    """
    Gets whether fast math optimizations are enabled, ignoring for example
    corner cases of floating-point math like NaN changes.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetFastMath()


def SetFastMath(
    value: bool,
) -> None:
    """
    Enables or disables fast math optimizations, ignoring for example
    corner cases of floating-point math like NaN changes.
    Applies to all modules, globally.
    """
    lib.BinaryenSetFastMath(value)


def GetPassArgument(
    name: str,
) -> str:
    """
    Gets the value of the specified arbitrary pass argument.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetPassArgument(name.encode())


def SetPassArgument(
    name: str,
    value: str,
) -> None:
    """
    Sets the value of the specified arbitrary pass argument. Removes the
    respective argument if `value` is NULL. Applies to all modules, globally.
    """
    lib.BinaryenSetPassArgument(name.encode(), value.encode())


def ClearPassArguments() -> None:
    """
    Clears all arbitrary pass arguments.
    Applies to all modules, globally.
    """
    lib.BinaryenClearPassArguments()


def GetAlwaysInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size at which we always inline.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetAlwaysInlineMaxSize()


def SetAlwaysInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size at which we always inline.
    Applies to all modules, globally.
    """
    lib.BinaryenSetAlwaysInlineMaxSize(size)


def GetFlexibleInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size which we inline when functions are lightweight.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetFlexibleInlineMaxSize()


def SetFlexibleInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size which we inline when functions are lightweight.
    Applies to all modules, globally.
    """
    lib.BinaryenSetFlexibleInlineMaxSize(size)


def GetOneCallerInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size which we inline when there is only one caller.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetOneCallerInlineMaxSize()


def SetOneCallerInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size which we inline when there is only one caller.
    Applies to all modules, globally.
    """
    lib.BinaryenSetOneCallerInlineMaxSize(size)


def GetAllowInliningFunctionsWithLoops() -> bool:
    """
    Gets whether functions with loops are allowed to be inlined.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetAllowInliningFunctionsWithLoops()


def SetAllowInliningFunctionsWithLoops(
    enabled: bool,
) -> None:
    """
    Sets whether functions with loops are allowed to be inlined.
    Applies to all modules, globally.
    """
    lib.BinaryenSetAllowInliningFunctionsWithLoops(enabled)


def ModuleRunPasses(
    module: BinaryenModuleRef,
    passes: List[str],
) -> None:
    """
    Runs the specified passes on the module. Uses the currently set global
    optimize and shrink level.
    """
    lib.BinaryenModuleRunPasses(module, [item.encode() for item in passes], len(passes))


def ModuleAutoDrop(
    module: BinaryenModuleRef,
) -> None:
    """
    Auto-generate drop() operations where needed. This lets you generate code
    without worrying about where they are needed. (It is more efficient to do it
    yourself, but simpler to use autodrop).
    """
    lib.BinaryenModuleAutoDrop(module)


def ModuleWrite(
    module: BinaryenModuleRef,
    output: str,
    output_size: int,
) -> int:
    """
    Serialize a module into binary form. Uses the currently set global debugInfo
    option.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWrite(module, output.encode(), output_size)


def ModuleWriteText(
    module: BinaryenModuleRef,
    output: str,
    output_size: int,
) -> int:
    """
    Serialize a module in s-expression text format.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWriteText(module, output.encode(), output_size)


def ModuleWriteStackIR(
    module: BinaryenModuleRef,
    output: str,
    output_size: int,
    optimize: bool,
) -> int:
    """
    Serialize a module in stack IR text format.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWriteStackIR(module, output.encode(), output_size, optimize)


def ModuleWriteWithSourceMap(
    module: BinaryenModuleRef,
    url: str,
    output: str,
    output_size: int,
    source_map: str,
    source_map_size: int,
) -> BinaryenBufferSizes:
    """
    Serialize a module into binary form including its source map. Uses the
    currently set global debugInfo option.
    @returns how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWriteWithSourceMap(module, url.encode(), output.encode(), output_size, source_map.encode(), source_map_size)


def ModuleAllocateAndWrite(
    module: BinaryenModuleRef,
    source_map_url: str,
) -> BinaryenModuleAllocateAndWriteResult:
    """
    Serializes a module into binary form, optionally including its source map if
    sourceMapUrl has been specified. Uses the currently set global debugInfo
    option. Differs from BinaryenModuleWrite in that it implicitly allocates
    appropriate buffers using malloc(), and expects the user to free() them
    manually once not needed anymore.
    """
    return lib.BinaryenModuleAllocateAndWrite(module, source_map_url.encode())


def ModuleAllocateAndWriteText(
    module: BinaryenModuleRef,
) -> str:
    """
    Serialize a module in s-expression form. Implicity allocates the returned
    char* with malloc(), and expects the user to free() them manually
    once not needed anymore.
    """
    return lib.BinaryenModuleAllocateAndWriteText(module)


def ModuleAllocateAndWriteStackIR(
    module: BinaryenModuleRef,
    optimize: bool,
) -> str:
    """
    Serialize a module in stack IR form. Implicitly allocates the returned
    char* with malloc(), and expects the user to free() them manually
    once not needed anymore.
    """
    return lib.BinaryenModuleAllocateAndWriteStackIR(module, optimize)


def ModuleRead(
    _input: str,
    input_size: int,
) -> BinaryenModuleRef:
    """ Deserialize a module from binary form. """
    return lib.BinaryenModuleRead(_input.encode(), input_size)


def ModuleInterpret(
    module: BinaryenModuleRef,
) -> None:
    """
    Execute a module in the Binaryen interpreter. This will create an instance of
    the module, run it in the interpreter - which means running the start method
    - and then destroying the instance.
    """
    lib.BinaryenModuleInterpret(module)


def ModuleAddDebugInfoFileName(
    module: BinaryenModuleRef,
    filename: str,
) -> BinaryenIndex:
    """ Adds a debug info file name to the module and returns its index. """
    return lib.BinaryenModuleAddDebugInfoFileName(module, filename.encode())


def ModuleGetDebugInfoFileName(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> str:
    """
    Gets the name of the debug info file at the specified index. Returns `NULL`
    if it does not exist.
    """
    return lib.BinaryenModuleGetDebugInfoFileName(module, index)


def FunctionGetName(
    func: BinaryenFunctionRef,
) -> str:
    """
    
    ========== Function Operations ==========
    
    Gets the name of the specified `Function`.
    """
    return lib.BinaryenFunctionGetName(func)


def FunctionGetParams(
    func: BinaryenFunctionRef,
) -> BinaryenType:
    """
    Gets the type of the parameter at the specified index of the specified
    `Function`.
    """
    return lib.BinaryenFunctionGetParams(func)


def FunctionGetResults(
    func: BinaryenFunctionRef,
) -> BinaryenType:
    """ Gets the result type of the specified `Function`. """
    return lib.BinaryenFunctionGetResults(func)


def FunctionGetNumVars(
    func: BinaryenFunctionRef,
) -> BinaryenIndex:
    """ Gets the number of additional locals within the specified `Function`. """
    return lib.BinaryenFunctionGetNumVars(func)


def FunctionGetVar(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> BinaryenType:
    """
    Gets the type of the additional local at the specified index within the
    specified `Function`.
    """
    return lib.BinaryenFunctionGetVar(func, index)


def FunctionGetNumLocals(
    func: BinaryenFunctionRef,
) -> BinaryenIndex:
    """ Gets the number of locals within the specified function. Includes parameters. """
    return lib.BinaryenFunctionGetNumLocals(func)


def FunctionHasLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> bool:
    """ Tests if the local at the specified index has a name. """
    return lib.BinaryenFunctionHasLocalName(func, index)


def FunctionGetLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> str:
    """ Gets the name of the local at the specified index. """
    return lib.BinaryenFunctionGetLocalName(func, index)


def FunctionSetLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """ Sets the name of the local at the specified index. """
    lib.BinaryenFunctionSetLocalName(func, index, name.encode())


def FunctionGetBody(
    func: BinaryenFunctionRef,
) -> BinaryenExpressionRef:
    """ Gets the body of the specified `Function`. """
    return lib.BinaryenFunctionGetBody(func)


def FunctionSetBody(
    func: BinaryenFunctionRef,
    body: BinaryenExpressionRef,
) -> None:
    """ Sets the body of the specified `Function`. """
    lib.BinaryenFunctionSetBody(func, body)


def FunctionOptimize(
    func: BinaryenFunctionRef,
    module: BinaryenModuleRef,
) -> None:
    """
    Runs the standard optimization passes on the function. Uses the currently set
    global optimize and shrink level.
    """
    lib.BinaryenFunctionOptimize(func, module)


def FunctionRunPasses(
    func: BinaryenFunctionRef,
    module: BinaryenModuleRef,
    passes: List[str],
) -> None:
    """
    Runs the specified passes on the function. Uses the currently set global
    optimize and shrink level.
    """
    lib.BinaryenFunctionRunPasses(func, module, [item.encode() for item in passes], len(passes))


def FunctionSetDebugLocation(
    func: BinaryenFunctionRef,
    expr: BinaryenExpressionRef,
    file_index: BinaryenIndex,
    line_number: BinaryenIndex,
    column_number: BinaryenIndex,
) -> None:
    """
    Sets the debug location of the specified `Expression` within the specified
    `Function`.
    """
    lib.BinaryenFunctionSetDebugLocation(func, expr, file_index, line_number, column_number)


def TableGetName(
    table: BinaryenTableRef,
) -> str:
    """
    
    ========== Table Operations ==========
    
    Gets the name of the specified `Table`.
    """
    return lib.BinaryenTableGetName(table)


def TableSetName(
    table: BinaryenTableRef,
    name: str,
) -> None:
    """ Sets the name of the specified `Table`. """
    lib.BinaryenTableSetName(table, name.encode())


def TableGetInitial(
    table: BinaryenTableRef,
) -> BinaryenIndex:
    """ Gets the initial number of pages of the specified `Table`. """
    return lib.BinaryenTableGetInitial(table)


def TableSetInitial(
    table: BinaryenTableRef,
    initial: BinaryenIndex,
) -> None:
    """ Sets the initial number of pages of the specified `Table`. """
    lib.BinaryenTableSetInitial(table, initial)


def TableHasMax(
    table: BinaryenTableRef,
) -> bool:
    """ Tests whether the specified `Table` has a maximum number of pages. """
    return lib.BinaryenTableHasMax(table)


def TableGetMax(
    table: BinaryenTableRef,
) -> BinaryenIndex:
    """ Gets the maximum number of pages of the specified `Table`. """
    return lib.BinaryenTableGetMax(table)


def TableSetMax(
    table: BinaryenTableRef,
    _max: BinaryenIndex,
) -> None:
    """ Sets the maximum number of pages of the specified `Table`. """
    lib.BinaryenTableSetMax(table, _max)


def ElementSegmentGetName(
    elem: BinaryenElementSegmentRef,
) -> str:
    """
    
    ========== Elem Segment Operations ==========
    
    Gets the name of the specified `ElementSegment`.
    """
    return lib.BinaryenElementSegmentGetName(elem)


def ElementSegmentSetName(
    elem: BinaryenElementSegmentRef,
    name: str,
) -> None:
    """ Sets the name of the specified `ElementSegment`. """
    lib.BinaryenElementSegmentSetName(elem, name.encode())


def ElementSegmentGetTable(
    elem: BinaryenElementSegmentRef,
) -> str:
    """ Gets the table name of the specified `ElementSegment`. """
    return lib.BinaryenElementSegmentGetTable(elem)


def ElementSegmentSetTable(
    elem: BinaryenElementSegmentRef,
    table: str,
) -> None:
    """ Sets the table name of the specified `ElementSegment`. """
    lib.BinaryenElementSegmentSetTable(elem, table.encode())


def ElementSegmentGetOffset(
    elem: BinaryenElementSegmentRef,
) -> BinaryenExpressionRef:
    """ Gets the segment offset in case of active segments """
    return lib.BinaryenElementSegmentGetOffset(elem)


def ElementSegmentGetLength(
    elem: BinaryenElementSegmentRef,
) -> BinaryenIndex:
    """ Gets the length of items in the segment """
    return lib.BinaryenElementSegmentGetLength(elem)


def ElementSegmentGetData(
    elem: BinaryenElementSegmentRef,
    data_id: BinaryenIndex,
) -> str:
    """ Gets the item at the specified index """
    return lib.BinaryenElementSegmentGetData(elem, data_id)


def ElementSegmentIsPassive(
    elem: BinaryenElementSegmentRef,
) -> bool:
    """ Returns true if the specified elem segment is passive """
    return lib.BinaryenElementSegmentIsPassive(elem)


def GlobalGetName(
    _global: BinaryenGlobalRef,
) -> str:
    """
    
    ========== Global Operations ==========
    
    Gets the name of the specified `Global`.
    """
    return lib.BinaryenGlobalGetName(_global)


def GlobalGetType(
    _global: BinaryenGlobalRef,
) -> BinaryenType:
    """
    Gets the name of the `GlobalType` associated with the specified `Global`. May
    be `NULL` if the signature is implicit.
    """
    return lib.BinaryenGlobalGetType(_global)


def GlobalIsMutable(
    _global: BinaryenGlobalRef,
) -> bool:
    """ Returns true if the specified `Global` is mutable. """
    return lib.BinaryenGlobalIsMutable(_global)


def GlobalGetInitExpr(
    _global: BinaryenGlobalRef,
) -> BinaryenExpressionRef:
    """ Gets the initialization expression of the specified `Global`. """
    return lib.BinaryenGlobalGetInitExpr(_global)


def TagGetName(
    tag: BinaryenTagRef,
) -> str:
    """
    
    ========== Tag Operations ==========
    
    Gets the name of the specified `Tag`.
    """
    return lib.BinaryenTagGetName(tag)


def TagGetParams(
    tag: BinaryenTagRef,
) -> BinaryenType:
    """ Gets the parameters type of the specified `Tag`. """
    return lib.BinaryenTagGetParams(tag)


def TagGetResults(
    tag: BinaryenTagRef,
) -> BinaryenType:
    """ Gets the results type of the specified `Tag`. """
    return lib.BinaryenTagGetResults(tag)


def FunctionImportGetModule(
    _import: BinaryenFunctionRef,
) -> str:
    """
    
    ========== Import Operations ==========
    
    Gets the external module name of the specified import.
    """
    return lib.BinaryenFunctionImportGetModule(_import)


def TableImportGetModule(
    _import: BinaryenTableRef,
) -> str:
    return lib.BinaryenTableImportGetModule(_import)


def GlobalImportGetModule(
    _import: BinaryenGlobalRef,
) -> str:
    return lib.BinaryenGlobalImportGetModule(_import)


def TagImportGetModule(
    _import: BinaryenTagRef,
) -> str:
    return lib.BinaryenTagImportGetModule(_import)


def FunctionImportGetBase(
    _import: BinaryenFunctionRef,
) -> str:
    """ Gets the external base name of the specified import. """
    return lib.BinaryenFunctionImportGetBase(_import)


def TableImportGetBase(
    _import: BinaryenTableRef,
) -> str:
    return lib.BinaryenTableImportGetBase(_import)


def GlobalImportGetBase(
    _import: BinaryenGlobalRef,
) -> str:
    return lib.BinaryenGlobalImportGetBase(_import)


def TagImportGetBase(
    _import: BinaryenTagRef,
) -> str:
    return lib.BinaryenTagImportGetBase(_import)


def ExportGetKind(
    export_: BinaryenExportRef,
) -> BinaryenExternalKind:
    """
    
    ========== Export Operations ==========
    
    Gets the external kind of the specified export.
    """
    return lib.BinaryenExportGetKind(export_)


def ExportGetName(
    export_: BinaryenExportRef,
) -> str:
    """ Gets the external name of the specified export. """
    return lib.BinaryenExportGetName(export_)


def ExportGetValue(
    export_: BinaryenExportRef,
) -> str:
    """ Gets the internal name of the specified export. """
    return lib.BinaryenExportGetValue(export_)


def AddCustomSection(
    module: BinaryenModuleRef,
    name: str,
    contents: str,
    contents_size: BinaryenIndex,
) -> None:
    """
    
    ========= Custom sections =========
    
    """
    lib.BinaryenAddCustomSection(module, name.encode(), contents.encode(), contents_size)


def SideEffectNone() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectNone()


def SideEffectBranches() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectBranches()


def SideEffectCalls() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectCalls()


def SideEffectReadsLocal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsLocal()


def SideEffectWritesLocal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesLocal()


def SideEffectReadsGlobal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsGlobal()


def SideEffectWritesGlobal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesGlobal()


def SideEffectReadsMemory() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsMemory()


def SideEffectWritesMemory() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesMemory()


def SideEffectReadsTable() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsTable()


def SideEffectWritesTable() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesTable()


def SideEffectImplicitTrap() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectImplicitTrap()


def SideEffectTrapsNeverHappen() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectTrapsNeverHappen()


def SideEffectIsAtomic() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectIsAtomic()


def SideEffectThrows() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectThrows()


def SideEffectDanglingPop() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectDanglingPop()


def SideEffectAny() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectAny()


def ExpressionGetSideEffects(
    expr: BinaryenExpressionRef,
    module: BinaryenModuleRef,
) -> BinaryenSideEffects:
    return lib.BinaryenExpressionGetSideEffects(expr, module)


def RelooperCreate(
    module: BinaryenModuleRef,
) -> RelooperRef:
    """ Create a relooper instance """
    return lib.RelooperCreate(module)


def RelooperAddBlock(
    relooper: RelooperRef,
    code: BinaryenExpressionRef,
) -> RelooperBlockRef:
    """ Create a basic block that ends with nothing, or with some simple branching """
    return lib.RelooperAddBlock(relooper, code)


def RelooperAddBranch(
    _from: RelooperBlockRef,
    to: RelooperBlockRef,
    condition: BinaryenExpressionRef,
    code: BinaryenExpressionRef,
) -> None:
    """
    Create a branch to another basic block
    The branch can have code on it, that is executed as the branch happens. this
    is useful for phis. otherwise, code can be NULL
    """
    lib.RelooperAddBranch(_from, to, condition, code)


def RelooperAddBlockWithSwitch(
    relooper: RelooperRef,
    code: BinaryenExpressionRef,
    condition: BinaryenExpressionRef,
) -> RelooperBlockRef:
    """ Create a basic block that ends a switch on a condition """
    return lib.RelooperAddBlockWithSwitch(relooper, code, condition)


def RelooperAddBranchForSwitch(
    _from: RelooperBlockRef,
    to: RelooperBlockRef,
    indexes: List[BinaryenIndex],
    code: BinaryenExpressionRef,
) -> None:
    """
    Create a switch-style branch to another basic block. The block's switch table
    will have these indexes going to that target
    """
    lib.RelooperAddBranchForSwitch(_from, to, indexes, len(indexes), code)


def RelooperRenderAndDispose(
    relooper: RelooperRef,
    entry: RelooperBlockRef,
    label_helper: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Generate structed wasm control flow from the CFG of blocks and branches that
    were created on this relooper instance. This returns the rendered output, and
    also disposes of the relooper and its blocks and branches, as they are no
    longer needed.
    @param labelHelper To render irreducible control flow, we may need a helper
    variable to guide us to the right target label. This value should be
    an index of an i32 local variable that is free for us to use.
    """
    return lib.RelooperRenderAndDispose(relooper, entry, label_helper)


def ExpressionRunnerFlagsDefault() -> ExpressionRunnerFlags:
    """
    By default, just evaluate the expression, i.e. all we want to know is whether
    it computes down to a concrete value, where it is not necessary to preserve
    side effects like those of a `local.tee`.
    """
    return lib.ExpressionRunnerFlagsDefault()


def ExpressionRunnerFlagsPreserveSideeffects() -> ExpressionRunnerFlags:
    """
    Be very careful to preserve any side effects. For example, if we are
    intending to replace the expression with a constant afterwards, even if we
    can technically evaluate down to a constant, we still cannot replace the
    expression if it also sets a local, which must be preserved in this scenario
    so subsequent code keeps functioning.
    """
    return lib.ExpressionRunnerFlagsPreserveSideeffects()


def ExpressionRunnerFlagsTraverseCalls() -> ExpressionRunnerFlags:
    """
    Traverse through function calls, attempting to compute their concrete value.
    Must not be used in function-parallel scenarios, where the called function
    might be concurrently modified, leading to undefined behavior. Traversing
    another function reuses all of this runner's flags.
    """
    return lib.ExpressionRunnerFlagsTraverseCalls()


def ExpressionRunnerCreate(
    module: BinaryenModuleRef,
    flags: ExpressionRunnerFlags,
    max_depth: BinaryenIndex,
    max_loop_iterations: BinaryenIndex,
) -> ExpressionRunnerRef:
    """ Creates an ExpressionRunner instance """
    return lib.ExpressionRunnerCreate(module, flags, max_depth, max_loop_iterations)


def ExpressionRunnerSetLocalValue(
    runner: ExpressionRunnerRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
) -> bool:
    """
    Sets a known local value to use. Order matters if expressions have side
    effects. For example, if the expression also sets a local, this side effect
    will also happen (not affected by any flags). Returns `true` if the
    expression actually evaluates to a constant.
    """
    return lib.ExpressionRunnerSetLocalValue(runner, index, value)


def ExpressionRunnerSetGlobalValue(
    runner: ExpressionRunnerRef,
    name: str,
    value: BinaryenExpressionRef,
) -> bool:
    """
    Sets a known global value to use. Order matters if expressions have side
    effects. For example, if the expression also sets a local, this side effect
    will also happen (not affected by any flags). Returns `true` if the
    expression actually evaluates to a constant.
    """
    return lib.ExpressionRunnerSetGlobalValue(runner, name.encode(), value)


def ExpressionRunnerRunAndDispose(
    runner: ExpressionRunnerRef,
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Runs the expression and returns the constant value expression it evaluates
    to, if any. Otherwise returns `NULL`. Also disposes the runner.
    """
    return lib.ExpressionRunnerRunAndDispose(runner, expr)


def TypeBuilderErrorReasonSelfSupertype() -> TypeBuilderErrorReason:
    """ Indicates a cycle in the supertype relation. """
    return lib.TypeBuilderErrorReasonSelfSupertype()


def TypeBuilderErrorReasonInvalidSupertype() -> TypeBuilderErrorReason:
    """ Indicates that the declared supertype of a type is invalid. """
    return lib.TypeBuilderErrorReasonInvalidSupertype()


def TypeBuilderErrorReasonForwardSupertypeReference() -> TypeBuilderErrorReason:
    """ Indicates that the declared supertype is an invalid forward reference. """
    return lib.TypeBuilderErrorReasonForwardSupertypeReference()


def TypeBuilderErrorReasonForwardChildReference() -> TypeBuilderErrorReason:
    """ Indicates that a child of a type is an invalid forward reference. """
    return lib.TypeBuilderErrorReasonForwardChildReference()


def TypeBuilderCreate(
    size: BinaryenIndex,
) -> TypeBuilderRef:
    """
    Constructs a new type builder that allows for the construction of recursive
    types. Contains a table of `size` mutable heap types.
    """
    return lib.TypeBuilderCreate(size)


def TypeBuilderGrow(
    builder: TypeBuilderRef,
    count: BinaryenIndex,
) -> None:
    """ Grows the backing table of the type builder by `count` slots. """
    lib.TypeBuilderGrow(builder, count)


def TypeBuilderGetSize(
    builder: TypeBuilderRef,
) -> BinaryenIndex:
    """ Gets the size of the backing table of the type builder. """
    return lib.TypeBuilderGetSize(builder)


def TypeBuilderSetBasicHeapType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    basic_heap_type: BinaryenBasicHeapType,
) -> None:
    """
    Sets the heap type at index `index` to a basic heap type. Must not be used in
    nominal mode.
    """
    lib.TypeBuilderSetBasicHeapType(builder, index, basic_heap_type)


def TypeBuilderSetSignatureType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    param_types: BinaryenType,
    result_types: BinaryenType,
) -> None:
    """
    Sets the heap type at index `index` to a concrete signature type. Expects
    temporary tuple types if multiple parameter and/or result types include
    temporary types.
    """
    lib.TypeBuilderSetSignatureType(builder, index, param_types, result_types)


def TypeBuilderSetStructType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    field_types: List[BinaryenType],
    field_packed_types: List[BinaryenPackedType],
    field_mutables: List[bool],
) -> None:
    """ Sets the heap type at index `index` to a concrete struct type. """
    lib.TypeBuilderSetStructType(builder, index, field_types, field_packed_types, field_mutables, len(field_mutables))


def TypeBuilderSetArrayType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    element_type: BinaryenType,
    element_packed_type: BinaryenPackedType,
    element_mutable: int,
) -> None:
    """ Sets the heap type at index `index` to a concrete array type. """
    lib.TypeBuilderSetArrayType(builder, index, element_type, element_packed_type, element_mutable)


def TypeBuilderIsBasic(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> bool:
    """ Tests if the heap type at index `index` is a basic heap type. """
    return lib.TypeBuilderIsBasic(builder, index)


def TypeBuilderGetBasic(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> BinaryenBasicHeapType:
    """ Gets the basic heap type at index `index`. """
    return lib.TypeBuilderGetBasic(builder, index)


def TypeBuilderGetTempHeapType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> BinaryenHeapType:
    """
    Gets the temporary heap type to use at index `index`. Temporary heap types
    may only be used to construct temporary types using the type builder.
    """
    return lib.TypeBuilderGetTempHeapType(builder, index)


def TypeBuilderGetTempTupleType(
    builder: TypeBuilderRef,
    types: List[BinaryenType],
) -> BinaryenType:
    """ Gets a temporary tuple type for use with and owned by the type builder. """
    return lib.TypeBuilderGetTempTupleType(builder, types, len(types))


def TypeBuilderGetTempRefType(
    builder: TypeBuilderRef,
    heap_type: BinaryenHeapType,
    nullable: int,
) -> BinaryenType:
    """ Gets a temporary reference type for use with and owned by the type builder. """
    return lib.TypeBuilderGetTempRefType(builder, heap_type, nullable)


def TypeBuilderSetSubType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    super_type: BinaryenHeapType,
) -> None:
    """ Sets the type at `index` to be a subtype of the given super type. """
    lib.TypeBuilderSetSubType(builder, index, super_type)


def TypeBuilderCreateRecGroup(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    length: BinaryenIndex,
) -> None:
    """
    Creates a new recursion group in the range `index` inclusive to `index +
    length` exclusive. Recursion groups must not overlap.
    """
    lib.TypeBuilderCreateRecGroup(builder, index, length)


def TypeBuilderBuildAndDispose(
    builder: TypeBuilderRef,
    heap_types: List[BinaryenHeapType],
    error_index: List[BinaryenIndex],
    error_reason: List[TypeBuilderErrorReason],
) -> bool:
    """
    Builds the heap type hierarchy and disposes the builder. Returns `false` and
    populates `errorIndex` and `errorReason` on failure.
    """
    return lib.TypeBuilderBuildAndDispose(builder, heap_types, error_index, error_reason)


def ModuleSetTypeName(
    module: BinaryenModuleRef,
    heap_type: BinaryenHeapType,
    name: str,
) -> None:
    """
    Sets the textual name of a compound `heapType`. Has no effect if the type
    already has a canonical name.
    """
    lib.BinaryenModuleSetTypeName(module, heap_type, name.encode())


def ModuleSetFieldName(
    module: BinaryenModuleRef,
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
    name: str,
) -> None:
    """ Sets the field name of a struct `heapType` at index `index`. """
    lib.BinaryenModuleSetFieldName(module, heap_type, index, name.encode())


def SetColorsEnabled(
    enabled: bool,
) -> None:
    """
    
    ========= Utilities =========
    
    Enable or disable coloring for the Wasm printer
    """
    lib.BinaryenSetColorsEnabled(enabled)


def AreColorsEnabled() -> bool:
    """ Query whether color is enable for the Wasm printer """
    return lib.BinaryenAreColorsEnabled()
