

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['B2CResourceSKUName', 'B2CResourceSKUTier', 'CIAMResourceSKUName', 'CIAMResourceSKUTier']
@pulumi.type_token(...)
class B2CResourceSKUName(_builtins.str, Enum):
    
    STANDARD = ...
    PREMIUM_P1 = ...
    PREMIUM_P2 = ...


@pulumi.type_token(...)
class B2CResourceSKUTier(_builtins.str, Enum):
    
    A0 = ...


@pulumi.type_token(...)
class CIAMResourceSKUName(_builtins.str, Enum):
    
    STANDARD = ...
    PREMIUM_P1 = ...
    PREMIUM_P2 = ...


@pulumi.type_token(...)
class CIAMResourceSKUTier(_builtins.str, Enum):
    
    A0 = ...


