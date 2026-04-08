import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["RpSkuTier"]

@pulumi.type_token("azure-native:fabric:RpSkuTier")
class RpSkuTier(_builtins.str, Enum):
    FABRIC = ...
