

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AccessPolicyRole', 'DataStringComparisonBehavior', 'EnvironmentKind', 'EventSourceKind', 'IngressStartAtType', 'LocalTimestampFormat', 'PropertyType', 'ReferenceDataKeyPropertyType', 'SkuName', 'StorageLimitExceededBehavior']
@pulumi.type_token("azure-native:timeseriesinsights:AccessPolicyRole")
class AccessPolicyRole(_builtins.str, Enum):
    
    READER = ...
    CONTRIBUTOR = ...


@pulumi.type_token(...)
class DataStringComparisonBehavior(_builtins.str, Enum):
    
    ORDINAL = ...
    ORDINAL_IGNORE_CASE = ...


@pulumi.type_token("azure-native:timeseriesinsights:EnvironmentKind")
class EnvironmentKind(_builtins.str, Enum):
    
    GEN1 = ...
    GEN2 = ...


@pulumi.type_token("azure-native:timeseriesinsights:EventSourceKind")
class EventSourceKind(_builtins.str, Enum):
    
    MICROSOFT_EVENT_HUB = ...
    MICROSOFT_IO_T_HUB = ...


@pulumi.type_token("azure-native:timeseriesinsights:IngressStartAtType")
class IngressStartAtType(_builtins.str, Enum):
    
    EARLIEST_AVAILABLE = ...
    EVENT_SOURCE_CREATION_TIME = ...
    CUSTOM_ENQUEUED_TIME = ...


@pulumi.type_token(...)
class LocalTimestampFormat(_builtins.str, Enum):
    
    EMBEDDED = ...


@pulumi.type_token("azure-native:timeseriesinsights:PropertyType")
class PropertyType(_builtins.str, Enum):
    
    STRING = ...


@pulumi.type_token(...)
class ReferenceDataKeyPropertyType(_builtins.str, Enum):
    
    STRING = ...
    DOUBLE = ...
    BOOL = ...
    DATE_TIME = ...


@pulumi.type_token("azure-native:timeseriesinsights:SkuName")
class SkuName(_builtins.str, Enum):
    
    S1 = ...
    S2 = ...
    P1 = ...
    L1 = ...


@pulumi.type_token(...)
class StorageLimitExceededBehavior(_builtins.str, Enum):
    
    PURGE_OLD_DATA = ...
    PAUSE_INGRESS = ...


