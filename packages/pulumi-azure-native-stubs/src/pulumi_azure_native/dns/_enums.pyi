import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["ZoneType"]

@pulumi.type_token("azure-native:dns:ZoneType")
class ZoneType(_builtins.str, Enum):
    PUBLIC = ...
    PRIVATE = ...
