

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['SkuName', 'SkuTier']
@pulumi.type_token("azure-native:devspaces:SkuName")
class SkuName(_builtins.str, Enum):
    
    S1 = ...


@pulumi.type_token("azure-native:devspaces:SkuTier")
class SkuTier(_builtins.str, Enum):
    
    STANDARD = ...


