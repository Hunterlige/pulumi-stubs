import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["ProcessNameFilterOperator", "SourceType"]

@pulumi.type_token(...)
class ProcessNameFilterOperator(_builtins.str, Enum):
    CONTAINS = ...
    NOT_CONTAINS = ...

@pulumi.type_token("azure-native:dependencymap:SourceType")
class SourceType(_builtins.str, Enum):
    OFF_AZURE = ...
