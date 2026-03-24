

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['SkuTier']
@pulumi.type_token("azure-native:community:SkuTier")
class SkuTier(_builtins.str, Enum):
    
    FREE = ...
    BASIC = ...
    STANDARD = ...
    PREMIUM = ...


