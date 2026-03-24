

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['IscsiTargetAclMode']
@pulumi.type_token("azure-native:storagepool:IscsiTargetAclMode")
class IscsiTargetAclMode(_builtins.str, Enum):
    
    DYNAMIC = ...
    STATIC = ...


