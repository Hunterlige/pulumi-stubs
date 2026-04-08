import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterMasterUserSecretArgs",
    "ClusterMasterUserSecretArgsDict",
    "ClusterParameterGroupParameterArgs",
    "ClusterParameterGroupParameterArgsDict",
    "ClusterRestoreToPointInTimeArgs",
    "ClusterRestoreToPointInTimeArgsDict",
    "ClusterS3ImportArgs",
    "ClusterS3ImportArgsDict",
    "ClusterScalingConfigurationArgs",
    "ClusterScalingConfigurationArgsDict",
    "ClusterServerlessv2ScalingConfigurationArgs",
    "ClusterServerlessv2ScalingConfigurationArgsDict",
    "ClusterSnapshotCopyTimeoutsArgs",
    "ClusterSnapshotCopyTimeoutsArgsDict",
    "ExportTaskTimeoutsArgs",
    "ExportTaskTimeoutsArgsDict",
    "GlobalClusterGlobalClusterMemberArgs",
    "GlobalClusterGlobalClusterMemberArgsDict",
    "InstanceBlueGreenUpdateArgs",
    "InstanceBlueGreenUpdateArgsDict",
    "InstanceDesiredStateTimeoutsArgs",
    "InstanceDesiredStateTimeoutsArgsDict",
    "InstanceListenerEndpointArgs",
    "InstanceListenerEndpointArgsDict",
    "InstanceMasterUserSecretArgs",
    "InstanceMasterUserSecretArgsDict",
    "InstanceRestoreToPointInTimeArgs",
    "InstanceRestoreToPointInTimeArgsDict",
    "InstanceS3ImportArgs",
    "InstanceS3ImportArgsDict",
    "IntegrationTimeoutsArgs",
    "IntegrationTimeoutsArgsDict",
    "OptionGroupOptionArgs",
    "OptionGroupOptionArgsDict",
    "OptionGroupOptionOptionSettingArgs",
    "OptionGroupOptionOptionSettingArgsDict",
    "ParameterGroupParameterArgs",
    "ParameterGroupParameterArgsDict",
    "ProxyAuthArgs",
    "ProxyAuthArgsDict",
    "ProxyDefaultTargetGroupConnectionPoolConfigArgs",
    ...,
    "ReservedInstanceRecurringChargeArgs",
    "ReservedInstanceRecurringChargeArgsDict",
    "ShardGroupTimeoutsArgs",
    "ShardGroupTimeoutsArgsDict",
    "GetClustersFilterArgs",
    "GetClustersFilterArgsDict",
    "GetEngineVersionFilterArgs",
    "GetEngineVersionFilterArgsDict",
    "GetInstancesFilterArgs",
    "GetInstancesFilterArgsDict",
]

class ClusterMasterUserSecretArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMasterUserSecretArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_status.setter
    def secret_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    apply_method: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterParameterGroupParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        apply_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apply_method.setter
    def apply_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterRestoreToPointInTimeArgsDict(TypedDict):
    restore_to_time: NotRequired[pulumi.Input[_builtins.str]]
    restore_type: NotRequired[pulumi.Input[_builtins.str]]
    source_cluster_identifier: NotRequired[pulumi.Input[_builtins.str]]
    source_cluster_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    use_latest_restorable_time: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterRestoreToPointInTimeArgs:
    def __init__(
        __self__,
        *,
        restore_to_time: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use_latest_restorable_time: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @restore_to_time.setter
    def restore_to_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @restore_type.setter
    def restore_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_cluster_identifier.setter
    def source_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceClusterResourceId")
    def source_cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_cluster_resource_id.setter
    def source_cluster_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterS3ImportArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    ingestion_role: pulumi.Input[_builtins.str]
    source_engine: pulumi.Input[_builtins.str]
    source_engine_version: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterS3ImportArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        ingestion_role: pulumi.Input[_builtins.str],
        source_engine: pulumi.Input[_builtins.str],
        source_engine_version: pulumi.Input[_builtins.str],
        bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> pulumi.Input[_builtins.str]: ...
    @ingestion_role.setter
    def ingestion_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> pulumi.Input[_builtins.str]: ...
    @source_engine.setter
    def source_engine(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> pulumi.Input[_builtins.str]: ...
    @source_engine_version.setter
    def source_engine_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterScalingConfigurationArgsDict(TypedDict):
    auto_pause: NotRequired[pulumi.Input[_builtins.bool]]
    max_capacity: NotRequired[pulumi.Input[_builtins.int]]
    min_capacity: NotRequired[pulumi.Input[_builtins.int]]
    seconds_before_timeout: NotRequired[pulumi.Input[_builtins.int]]
    seconds_until_auto_pause: NotRequired[pulumi.Input[_builtins.int]]
    timeout_action: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        auto_pause: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds_before_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds_until_auto_pause: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_pause.setter
    def auto_pause(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secondsBeforeTimeout")
    def seconds_before_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds_before_timeout.setter
    def seconds_before_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds_until_auto_pause.setter
    def seconds_until_auto_pause(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout_action.setter
    def timeout_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterServerlessv2ScalingConfigurationArgsDict(TypedDict):
    max_capacity: pulumi.Input[_builtins.float]
    min_capacity: pulumi.Input[_builtins.float]
    seconds_until_auto_pause: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterServerlessv2ScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_capacity: pulumi.Input[_builtins.float],
        min_capacity: pulumi.Input[_builtins.float],
        seconds_until_auto_pause: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Input[_builtins.float]: ...
    @max_capacity.setter
    def max_capacity(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> pulumi.Input[_builtins.float]: ...
    @min_capacity.setter
    def min_capacity(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds_until_auto_pause.setter
    def seconds_until_auto_pause(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ClusterSnapshotCopyTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterSnapshotCopyTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExportTaskTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExportTaskTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GlobalClusterGlobalClusterMemberArgsDict(TypedDict):
    db_cluster_arn: NotRequired[pulumi.Input[_builtins.str]]
    is_writer: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GlobalClusterGlobalClusterMemberArgs:
    def __init__(
        __self__,
        *,
        db_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        is_writer: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_arn.setter
    def db_cluster_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_writer.setter
    def is_writer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceBlueGreenUpdateArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class InstanceBlueGreenUpdateArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceDesiredStateTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceDesiredStateTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceListenerEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    hosted_zone_id: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InstanceListenerEndpointArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceMasterUserSecretArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceMasterUserSecretArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_status.setter
    def secret_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceRestoreToPointInTimeArgsDict(TypedDict):
    restore_time: NotRequired[pulumi.Input[_builtins.str]]
    source_db_instance_automated_backups_arn: NotRequired[pulumi.Input[_builtins.str]]
    source_db_instance_identifier: NotRequired[pulumi.Input[_builtins.str]]
    source_dbi_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    use_latest_restorable_time: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class InstanceRestoreToPointInTimeArgs:
    def __init__(
        __self__,
        *,
        restore_time: Optional[pulumi.Input[_builtins.str]] = ...,
        source_db_instance_automated_backups_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        source_db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_dbi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use_latest_restorable_time: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restoreTime")
    def restore_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @restore_time.setter
    def restore_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceAutomatedBackupsArn")
    def source_db_instance_automated_backups_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_instance_automated_backups_arn.setter
    def source_db_instance_automated_backups_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceIdentifier")
    def source_db_instance_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_instance_identifier.setter
    def source_db_instance_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbiResourceId")
    def source_dbi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_dbi_resource_id.setter
    def source_dbi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class InstanceS3ImportArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    ingestion_role: pulumi.Input[_builtins.str]
    source_engine: pulumi.Input[_builtins.str]
    source_engine_version: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceS3ImportArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        ingestion_role: pulumi.Input[_builtins.str],
        source_engine: pulumi.Input[_builtins.str],
        source_engine_version: pulumi.Input[_builtins.str],
        bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> pulumi.Input[_builtins.str]: ...
    @ingestion_role.setter
    def ingestion_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> pulumi.Input[_builtins.str]: ...
    @source_engine.setter
    def source_engine(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> pulumi.Input[_builtins.str]: ...
    @source_engine_version.setter
    def source_engine_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IntegrationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IntegrationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptionGroupOptionArgsDict(TypedDict):
    option_name: pulumi.Input[_builtins.str]
    db_security_group_memberships: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    option_settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptionGroupOptionOptionSettingArgsDict]]]
    ]
    port: NotRequired[pulumi.Input[_builtins.int]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    vpc_security_group_memberships: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class OptionGroupOptionArgs:
    def __init__(
        __self__,
        *,
        option_name: pulumi.Input[_builtins.str],
        db_security_group_memberships: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        option_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptionGroupOptionOptionSettingArgs]]]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_memberships: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optionName")
    def option_name(self) -> pulumi.Input[_builtins.str]: ...
    @option_name.setter
    def option_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbSecurityGroupMemberships")
    def db_security_group_memberships(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @db_security_group_memberships.setter
    def db_security_group_memberships(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optionSettings")
    def option_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptionGroupOptionOptionSettingArgs]]]
    ]: ...
    @option_settings.setter
    def option_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptionGroupOptionOptionSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupMemberships")
    def vpc_security_group_memberships(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_memberships.setter
    def vpc_security_group_memberships(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OptionGroupOptionOptionSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class OptionGroupOptionOptionSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    apply_method: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ParameterGroupParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        apply_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apply_method.setter
    def apply_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProxyAuthArgsDict(TypedDict):
    auth_scheme: NotRequired[pulumi.Input[_builtins.str]]
    client_password_auth_type: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    iam_auth: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProxyAuthArgs:
    def __init__(
        __self__,
        *,
        auth_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        client_password_auth_type: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_auth: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authScheme")
    def auth_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_scheme.setter
    def auth_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientPasswordAuthType")
    def client_password_auth_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_password_auth_type.setter
    def client_password_auth_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamAuth")
    def iam_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_auth.setter
    def iam_auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProxyDefaultTargetGroupConnectionPoolConfigArgsDict(TypedDict):
    connection_borrow_timeout: NotRequired[pulumi.Input[_builtins.int]]
    init_query: NotRequired[pulumi.Input[_builtins.str]]
    max_connections_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_idle_connections_percent: NotRequired[pulumi.Input[_builtins.int]]
    session_pinning_filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ProxyDefaultTargetGroupConnectionPoolConfigArgs:
    def __init__(
        __self__,
        *,
        connection_borrow_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        init_query: Optional[pulumi.Input[_builtins.str]] = ...,
        max_connections_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        max_idle_connections_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        session_pinning_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionBorrowTimeout")
    def connection_borrow_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_borrow_timeout.setter
    def connection_borrow_timeout(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initQuery")
    def init_query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @init_query.setter
    def init_query(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConnectionsPercent")
    def max_connections_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_connections_percent.setter
    def max_connections_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIdleConnectionsPercent")
    def max_idle_connections_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_idle_connections_percent.setter
    def max_idle_connections_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionPinningFilters")
    def session_pinning_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @session_pinning_filters.setter
    def session_pinning_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ReservedInstanceRecurringChargeArgsDict(TypedDict):
    recurring_charge_amount: NotRequired[pulumi.Input[_builtins.int]]
    recurring_charge_frequency: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReservedInstanceRecurringChargeArgs:
    def __init__(
        __self__,
        *,
        recurring_charge_amount: Optional[pulumi.Input[_builtins.int]] = ...,
        recurring_charge_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeAmount")
    def recurring_charge_amount(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recurring_charge_amount.setter
    def recurring_charge_amount(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeFrequency")
    def recurring_charge_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recurring_charge_frequency.setter
    def recurring_charge_frequency(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ShardGroupTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ShardGroupTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetClustersFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetClustersFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetEngineVersionFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetEngineVersionFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetInstancesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetInstancesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
