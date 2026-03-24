

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['CatalogItemSyncEnableStatus', 'CatalogItemType', 'CatalogSyncType', 'DevboxDisksEncryptionEnableStatus', 'DomainJoinType', 'EnvironmentTypeEnableStatus', 'HibernateSupport', 'IdentityType', 'LicenseType', 'LocalAdminStatus', 'ManagedServiceIdentityType', 'PlanMemberType', 'ScheduleEnableStatus', 'ScheduledFrequency', 'ScheduledType', 'SingleSignOnStatus', 'SkuTier', 'StopOnDisconnectEnableStatus', 'VirtualNetworkType']
@pulumi.type_token("azure-native:devcenter:CatalogItemSyncEnableStatus")
class CatalogItemSyncEnableStatus(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:devcenter:CatalogItemType")
class CatalogItemType(_builtins.str, Enum):
    
    ENVIRONMENT_DEFINITION = ...


@pulumi.type_token("azure-native:devcenter:CatalogSyncType")
class CatalogSyncType(_builtins.str, Enum):
    
    MANUAL = ...
    SCHEDULED = ...


@pulumi.type_token(...)
class DevboxDisksEncryptionEnableStatus(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:devcenter:DomainJoinType")
class DomainJoinType(_builtins.str, Enum):
    
    HYBRID_AZURE_AD_JOIN = ...
    AZURE_AD_JOIN = ...


@pulumi.type_token("azure-native:devcenter:EnvironmentTypeEnableStatus")
class EnvironmentTypeEnableStatus(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:devcenter:HibernateSupport")
class HibernateSupport(_builtins.str, Enum):
    
    DISABLED = ...
    ENABLED = ...


@pulumi.type_token("azure-native:devcenter:IdentityType")
class IdentityType(_builtins.str, Enum):
    
    SYSTEM_ASSIGNED_IDENTITY = ...
    USER_ASSIGNED_IDENTITY = ...
    DELEGATED_RESOURCE_IDENTITY = ...


@pulumi.type_token("azure-native:devcenter:LicenseType")
class LicenseType(_builtins.str, Enum):
    
    WINDOWS_CLIENT = ...


@pulumi.type_token("azure-native:devcenter:LocalAdminStatus")
class LocalAdminStatus(_builtins.str, Enum):
    
    DISABLED = ...
    ENABLED = ...


@pulumi.type_token("azure-native:devcenter:ManagedServiceIdentityType")
class ManagedServiceIdentityType(_builtins.str, Enum):
    
    NONE = ...
    SYSTEM_ASSIGNED = ...
    USER_ASSIGNED = ...
    SYSTEM_ASSIGNED_USER_ASSIGNED = ...


@pulumi.type_token("azure-native:devcenter:PlanMemberType")
class PlanMemberType(_builtins.str, Enum):
    
    USER = ...
    GROUP = ...


@pulumi.type_token("azure-native:devcenter:ScheduleEnableStatus")
class ScheduleEnableStatus(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:devcenter:ScheduledFrequency")
class ScheduledFrequency(_builtins.str, Enum):
    
    DAILY = ...


@pulumi.type_token("azure-native:devcenter:ScheduledType")
class ScheduledType(_builtins.str, Enum):
    
    STOP_DEV_BOX = ...


@pulumi.type_token("azure-native:devcenter:SingleSignOnStatus")
class SingleSignOnStatus(_builtins.str, Enum):
    
    DISABLED = ...
    ENABLED = ...


@pulumi.type_token("azure-native:devcenter:SkuTier")
class SkuTier(_builtins.str, Enum):
    
    FREE = ...
    BASIC = ...
    STANDARD = ...
    PREMIUM = ...


@pulumi.type_token(...)
class StopOnDisconnectEnableStatus(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:devcenter:VirtualNetworkType")
class VirtualNetworkType(_builtins.str, Enum):
    
    MANAGED = ...
    UNMANAGED = ...


