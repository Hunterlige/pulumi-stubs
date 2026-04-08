import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["SkuName"]

@pulumi.type_token("azure-native:enterpriseknowledgegraph:SkuName")
class SkuName(_builtins.str, Enum):
    F0 = ...
    S1 = ...
