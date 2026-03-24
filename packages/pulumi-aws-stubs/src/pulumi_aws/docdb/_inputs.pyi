

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterMasterUserSecretArgs', 'ClusterMasterUserSecretArgsDict', 'ClusterParameterGroupParameterArgs', 'ClusterParameterGroupParameterArgsDict', 'ClusterRestoreToPointInTimeArgs', 'ClusterRestoreToPointInTimeArgsDict', 'ClusterServerlessV2ScalingConfigurationArgs', 'ClusterServerlessV2ScalingConfigurationArgsDict', 'ElasticClusterTimeoutsArgs', 'ElasticClusterTimeoutsArgsDict', 'GlobalClusterGlobalClusterMemberArgs', 'GlobalClusterGlobalClusterMemberArgsDict']
class ClusterMasterUserSecretArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterMasterUserSecretArgs:
    def __init__(__self__, *, kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., secret_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secret_status.setter
    def secret_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    apply_method: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterParameterGroupParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str], apply_method: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @apply_method.setter
    def apply_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterRestoreToPointInTimeArgsDict(TypedDict):
    source_cluster_identifier: pulumi.Input[_builtins.str]
    restore_to_time: NotRequired[pulumi.Input[_builtins.str]]
    restore_type: NotRequired[pulumi.Input[_builtins.str]]
    use_latest_restorable_time: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ClusterRestoreToPointInTimeArgs:
    def __init__(__self__, *, source_cluster_identifier: pulumi.Input[_builtins.str], restore_to_time: Optional[pulumi.Input[_builtins.str]] = ..., restore_type: Optional[pulumi.Input[_builtins.str]] = ..., use_latest_restorable_time: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_cluster_identifier.setter
    def source_cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_to_time.setter
    def restore_to_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_type.setter
    def restore_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_latest_restorable_time.setter
    def use_latest_restorable_time(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ClusterServerlessV2ScalingConfigurationArgsDict(TypedDict):
    max_capacity: pulumi.Input[_builtins.float]
    min_capacity: pulumi.Input[_builtins.float]


@pulumi.input_type
class ClusterServerlessV2ScalingConfigurationArgs:
    def __init__(__self__, *, max_capacity: pulumi.Input[_builtins.float], min_capacity: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @max_capacity.setter
    def max_capacity(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @min_capacity.setter
    def min_capacity(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class ElasticClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ElasticClusterTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GlobalClusterGlobalClusterMemberArgsDict(TypedDict):
    db_cluster_arn: NotRequired[pulumi.Input[_builtins.str]]
    is_writer: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class GlobalClusterGlobalClusterMemberArgs:
    def __init__(__self__, *, db_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ..., is_writer: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_cluster_arn.setter
    def db_cluster_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_writer.setter
    def is_writer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


