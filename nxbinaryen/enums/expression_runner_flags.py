# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.capi import ExpressionRunnerFlags
from nxbinaryen.binaryen import lib

__all__ = [
    'ExpressionRunnerFlag',
]


@unique
class ExpressionRunnerFlag(IntFlag):
    Default: ExpressionRunnerFlags = lib.ExpressionRunnerFlagsDefault()
    PreserveSideeffects: ExpressionRunnerFlags = lib.ExpressionRunnerFlagsPreserveSideeffects()
    TraverseCalls: ExpressionRunnerFlags = lib.ExpressionRunnerFlagsTraverseCalls()
