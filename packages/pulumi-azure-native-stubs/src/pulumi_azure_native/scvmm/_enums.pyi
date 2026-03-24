

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AllocationMethod', 'CreateDiffDisk', 'DynamicMemoryEnabled', 'IdentityType', 'InventoryType', 'LimitCpuForMigration', 'ProvisioningAction']
@pulumi.type_token("azure-native:scvmm:AllocationMethod")
class AllocationMethod(_builtins.str, Enum):
    
    DYNAMIC = ...
    STATIC = ...


@pulumi.type_token("azure-native:scvmm:CreateDiffDisk")
class CreateDiffDisk(_builtins.str, Enum):
    
    FALSE = ...
    TRUE = ...


@pulumi.type_token("azure-native:scvmm:DynamicMemoryEnabled")
class DynamicMemoryEnabled(_builtins.str, Enum):
    
    FALSE = ...
    TRUE = ...


@pulumi.type_token("azure-native:scvmm:IdentityType")
class IdentityType(_builtins.str, Enum):
    
    NONE = ...
    SYSTEM_ASSIGNED = ...


@pulumi.type_token("azure-native:scvmm:InventoryType")
class InventoryType(_builtins.str, Enum):
    
    CLOUD = ...
    VIRTUAL_NETWORK = ...
    VIRTUAL_MACHINE_TEMPLATE = ...
    VIRTUAL_MACHINE = ...


@pulumi.type_token("azure-native:scvmm:LimitCpuForMigration")
class LimitCpuForMigration(_builtins.str, Enum):
    
    FALSE = ...
    TRUE = ...


@pulumi.type_token("azure-native:scvmm:ProvisioningAction")
class ProvisioningAction(_builtins.str, Enum):
    
    INSTALL = ...
    UNINSTALL = ...
    REPAIR = ...


