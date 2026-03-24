

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['Distro', 'Provider', 'ResourceIdentityType']
@pulumi.type_token("azure-native:resourceconnector:Distro")
class Distro(_builtins.str, Enum):
    
    AKS_EDGE = ...


@pulumi.type_token("azure-native:resourceconnector:Provider")
class Provider(_builtins.str, Enum):
    
    VM_WARE = ...
    HCI = ...
    SCVMM = ...


@pulumi.type_token(...)
class ResourceIdentityType(_builtins.str, Enum):
    
    SYSTEM_ASSIGNED = ...
    NONE = ...


