import builtins as _builtins
import pulumi
from enum import Enum

__all__ = [
    "FilterType",
    "ManagedServiceIdentityType",
    "PublicNetworkAccessOption",
    "SelectorType",
    "TargetReferenceType",
]

@pulumi.type_token("azure-native:chaos:FilterType")
class FilterType(_builtins.str, Enum):
    SIMPLE = ...

@pulumi.type_token("azure-native:chaos:ManagedServiceIdentityType")
class ManagedServiceIdentityType(_builtins.str, Enum):
    NONE = ...
    SYSTEM_ASSIGNED = ...
    USER_ASSIGNED = ...
    SYSTEM_ASSIGNED_USER_ASSIGNED = ...

@pulumi.type_token("azure-native:chaos:PublicNetworkAccessOption")
class PublicNetworkAccessOption(_builtins.str, Enum):
    ENABLED = ...
    DISABLED = ...

@pulumi.type_token("azure-native:chaos:SelectorType")
class SelectorType(_builtins.str, Enum):
    LIST = ...
    QUERY = ...

@pulumi.type_token("azure-native:chaos:TargetReferenceType")
class TargetReferenceType(_builtins.str, Enum):
    CHAOS_TARGET = ...
