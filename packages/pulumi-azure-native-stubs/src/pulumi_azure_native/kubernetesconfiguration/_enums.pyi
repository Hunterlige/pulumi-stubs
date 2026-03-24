

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AKSIdentityType', 'LevelType', 'OperatorScopeType', 'OperatorType', 'PrivateEndpointServiceConnectionStatus', 'PublicNetworkAccessType', 'ResourceIdentityType', 'ScopeType', 'SourceKindType']
@pulumi.type_token(...)
class AKSIdentityType(_builtins.str, Enum):
    
    SYSTEM_ASSIGNED = ...
    USER_ASSIGNED = ...


@pulumi.type_token("azure-native:kubernetesconfiguration:LevelType")
class LevelType(_builtins.str, Enum):
    
    ERROR = ...
    WARNING = ...
    INFORMATION = ...


@pulumi.type_token(...)
class OperatorScopeType(_builtins.str, Enum):
    
    CLUSTER = ...
    NAMESPACE = ...


@pulumi.type_token("azure-native:kubernetesconfiguration:OperatorType")
class OperatorType(_builtins.str, Enum):
    
    FLUX = ...


@pulumi.type_token(...)
class PrivateEndpointServiceConnectionStatus(_builtins.str, Enum):
    
    PENDING = ...
    APPROVED = ...
    REJECTED = ...


@pulumi.type_token(...)
class PublicNetworkAccessType(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token(...)
class ResourceIdentityType(_builtins.str, Enum):
    
    SYSTEM_ASSIGNED = ...


@pulumi.type_token("azure-native:kubernetesconfiguration:ScopeType")
class ScopeType(_builtins.str, Enum):
    
    CLUSTER = ...
    NAMESPACE = ...


@pulumi.type_token(...)
class SourceKindType(_builtins.str, Enum):
    
    GIT_REPOSITORY = ...
    BUCKET = ...
    AZURE_BLOB = ...


