

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['DomainManagement', 'ManagedServiceIdentityType', 'UserEngagementTracking']
@pulumi.type_token("azure-native:communication:DomainManagement")
class DomainManagement(_builtins.str, Enum):
    
    AZURE_MANAGED = ...
    CUSTOMER_MANAGED = ...
    CUSTOMER_MANAGED_IN_EXCHANGE_ONLINE = ...


@pulumi.type_token(...)
class ManagedServiceIdentityType(_builtins.str, Enum):
    
    NONE = ...
    SYSTEM_ASSIGNED = ...
    USER_ASSIGNED = ...
    SYSTEM_ASSIGNED_USER_ASSIGNED = ...


@pulumi.type_token("azure-native:communication:UserEngagementTracking")
class UserEngagementTracking(_builtins.str, Enum):
    
    DISABLED = ...
    ENABLED = ...


