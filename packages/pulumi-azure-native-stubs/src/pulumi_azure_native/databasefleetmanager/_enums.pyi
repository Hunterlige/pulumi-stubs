

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['DatabaseCreateMode', 'IdentityType', 'PrincipalType', 'ZoneRedundancy']
@pulumi.type_token(...)
class DatabaseCreateMode(_builtins.str, Enum):
    
    DEFAULT = ...
    COPY = ...
    POINT_IN_TIME_RESTORE = ...


@pulumi.type_token("azure-native:databasefleetmanager:IdentityType")
class IdentityType(_builtins.str, Enum):
    
    NONE = ...
    USER_ASSIGNED = ...


@pulumi.type_token("azure-native:databasefleetmanager:PrincipalType")
class PrincipalType(_builtins.str, Enum):
    
    APPLICATION = ...
    USER = ...


@pulumi.type_token("azure-native:databasefleetmanager:ZoneRedundancy")
class ZoneRedundancy(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


