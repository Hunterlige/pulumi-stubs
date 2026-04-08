import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["CapacitySkuTier", "Mode", "VCoreSkuTier"]

@pulumi.type_token("azure-native:powerbidedicated:CapacitySkuTier")
class CapacitySkuTier(_builtins.str, Enum):
    PBI_E_AZURE = ...
    PREMIUM = ...
    AUTO_PREMIUM_HOST = ...

@pulumi.type_token("azure-native:powerbidedicated:Mode")
class Mode(_builtins.str, Enum):
    GEN1 = ...
    GEN2 = ...

@pulumi.type_token("azure-native:powerbidedicated:VCoreSkuTier")
class VCoreSkuTier(_builtins.str, Enum):
    AUTO_SCALE = ...
