import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["SkuType"]

@pulumi.type_token("azure-native:datacatalog:SkuType")
class SkuType(_builtins.str, Enum):
    FREE = ...
    STANDARD = ...
