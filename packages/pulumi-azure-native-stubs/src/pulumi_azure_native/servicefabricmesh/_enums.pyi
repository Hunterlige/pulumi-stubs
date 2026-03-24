

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ApplicationScopedVolumeKind', 'AutoScalingMechanismKind', 'AutoScalingMetricKind', 'AutoScalingResourceMetricName', 'AutoScalingTriggerKind', 'DiagnosticsSinkKind', 'HeaderMatchType', 'NetworkKind', 'OperatingSystemType', 'PathMatchType', 'SecretKind', 'SizeTypes', 'VolumeProvider']
@pulumi.type_token(...)
class ApplicationScopedVolumeKind(_builtins.str, Enum):
    
    SERVICE_FABRIC_VOLUME_DISK = ...


@pulumi.type_token(...)
class AutoScalingMechanismKind(_builtins.str, Enum):
    
    ADD_REMOVE_REPLICA = ...


@pulumi.type_token(...)
class AutoScalingMetricKind(_builtins.str, Enum):
    
    RESOURCE = ...


@pulumi.type_token(...)
class AutoScalingResourceMetricName(_builtins.str, Enum):
    
    CPU = ...
    MEMORY_IN_GB = ...


@pulumi.type_token(...)
class AutoScalingTriggerKind(_builtins.str, Enum):
    
    AVERAGE_LOAD = ...


@pulumi.type_token("azure-native:servicefabricmesh:DiagnosticsSinkKind")
class DiagnosticsSinkKind(_builtins.str, Enum):
    
    INVALID = ...
    AZURE_INTERNAL_MONITORING_PIPELINE = ...


@pulumi.type_token("azure-native:servicefabricmesh:HeaderMatchType")
class HeaderMatchType(_builtins.str, Enum):
    
    EXACT = ...


@pulumi.type_token("azure-native:servicefabricmesh:NetworkKind")
class NetworkKind(_builtins.str, Enum):
    
    LOCAL = ...


@pulumi.type_token("azure-native:servicefabricmesh:OperatingSystemType")
class OperatingSystemType(_builtins.str, Enum):
    
    LINUX = ...
    WINDOWS = ...


@pulumi.type_token("azure-native:servicefabricmesh:PathMatchType")
class PathMatchType(_builtins.str, Enum):
    
    PREFIX = ...


@pulumi.type_token("azure-native:servicefabricmesh:SecretKind")
class SecretKind(_builtins.str, Enum):
    
    INLINED_VALUE = ...


@pulumi.type_token("azure-native:servicefabricmesh:SizeTypes")
class SizeTypes(_builtins.str, Enum):
    
    SMALL = ...
    MEDIUM = ...
    LARGE = ...


@pulumi.type_token("azure-native:servicefabricmesh:VolumeProvider")
class VolumeProvider(_builtins.str, Enum):
    
    SF_AZURE_FILE = ...


