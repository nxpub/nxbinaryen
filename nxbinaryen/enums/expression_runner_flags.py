# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'ExpressionRunnerFlag',
]


@unique
class ExpressionRunnerFlag(IntFlag):
    Default = lib.ExpressionRunnerFlagsDefault()
    PreserveSideeffects = lib.ExpressionRunnerFlagsPreserveSideeffects()
    TraverseCalls = lib.ExpressionRunnerFlagsTraverseCalls()
