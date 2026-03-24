

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AuthCredentialsKind', 'PrivateEndpointServiceConnectionStatus', 'PublicNetworkAccess', 'ResourceIdentityType']
@pulumi.type_token("azure-native:agfoodplatform:AuthCredentialsKind")
class AuthCredentialsKind(_builtins.str, Enum):
    
    O_AUTH_CLIENT_CREDENTIALS = ...
    API_KEY_AUTH_CREDENTIALS = ...


@pulumi.type_token(...)
class PrivateEndpointServiceConnectionStatus(_builtins.str, Enum):
    
    PENDING = ...
    APPROVED = ...
    REJECTED = ...


@pulumi.type_token("azure-native:agfoodplatform:PublicNetworkAccess")
class PublicNetworkAccess(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:agfoodplatform:ResourceIdentityType")
class ResourceIdentityType(_builtins.str, Enum):
    
    SYSTEM_ASSIGNED = ...


