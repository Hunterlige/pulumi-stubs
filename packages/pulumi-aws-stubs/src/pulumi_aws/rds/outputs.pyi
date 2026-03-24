

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterMasterUserSecret', 'ClusterParameterGroupParameter', 'ClusterRestoreToPointInTime', 'ClusterS3Import', 'ClusterScalingConfiguration', 'ClusterServerlessv2ScalingConfiguration', 'ClusterSnapshotCopyTimeouts', 'ExportTaskTimeouts', 'GlobalClusterGlobalClusterMember', 'InstanceBlueGreenUpdate', 'InstanceDesiredStateTimeouts', 'InstanceListenerEndpoint', 'InstanceMasterUserSecret', 'InstanceRestoreToPointInTime', 'InstanceS3Import', 'IntegrationTimeouts', 'OptionGroupOption', 'OptionGroupOptionOptionSetting', 'ParameterGroupParameter', 'ProxyAuth', 'ProxyDefaultTargetGroupConnectionPoolConfig', 'ReservedInstanceRecurringCharge', 'ShardGroupTimeouts', 'GetClusterMasterUserSecretResult', 'GetClustersFilterResult', 'GetEngineVersionFilterResult', 'GetGlobalClusterMemberResult', 'GetInstanceMasterUserSecretResult', 'GetInstancesFilterResult', 'GetProxyAuthResult']
@pulumi.output_type
class ClusterMasterUserSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_id: Optional[_builtins.str] = ..., secret_arn: Optional[_builtins.str] = ..., secret_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterParameterGroupParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, apply_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterRestoreToPointInTime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, restore_to_time: Optional[_builtins.str] = ..., restore_type: Optional[_builtins.str] = ..., source_cluster_identifier: Optional[_builtins.str] = ..., source_cluster_resource_id: Optional[_builtins.str] = ..., use_latest_restorable_time: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceClusterResourceId")
    def source_cluster_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterS3Import(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, ingestion_role: _builtins.str, source_engine: _builtins.str, source_engine_version: _builtins.str, bucket_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_pause: Optional[_builtins.bool] = ..., max_capacity: Optional[_builtins.int] = ..., min_capacity: Optional[_builtins.int] = ..., seconds_before_timeout: Optional[_builtins.int] = ..., seconds_until_auto_pause: Optional[_builtins.int] = ..., timeout_action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsBeforeTimeout")
    def seconds_before_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterServerlessv2ScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_capacity: _builtins.float, min_capacity: _builtins.float, seconds_until_auto_pause: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterSnapshotCopyTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExportTaskTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GlobalClusterGlobalClusterMember(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, db_cluster_arn: Optional[_builtins.str] = ..., is_writer: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceBlueGreenUpdate(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceDesiredStateTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceListenerEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., hosted_zone_id: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceMasterUserSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_id: Optional[_builtins.str] = ..., secret_arn: Optional[_builtins.str] = ..., secret_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceRestoreToPointInTime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, restore_time: Optional[_builtins.str] = ..., source_db_instance_automated_backups_arn: Optional[_builtins.str] = ..., source_db_instance_identifier: Optional[_builtins.str] = ..., source_dbi_resource_id: Optional[_builtins.str] = ..., use_latest_restorable_time: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTime")
    def restore_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceAutomatedBackupsArn")
    def source_db_instance_automated_backups_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceIdentifier")
    def source_db_instance_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbiResourceId")
    def source_dbi_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceS3Import(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, ingestion_role: _builtins.str, source_engine: _builtins.str, source_engine_version: _builtins.str, bucket_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntegrationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptionGroupOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, option_name: _builtins.str, db_security_group_memberships: Optional[Sequence[_builtins.str]] = ..., option_settings: Optional[Sequence[outputs.OptionGroupOptionOptionSetting]] = ..., port: Optional[_builtins.int] = ..., version: Optional[_builtins.str] = ..., vpc_security_group_memberships: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionName")
    def option_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSecurityGroupMemberships")
    def db_security_group_memberships(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> Optional[Sequence[outputs.OptionGroupOptionOptionSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupMemberships")
    def vpc_security_group_memberships(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class OptionGroupOptionOptionSetting(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ParameterGroupParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, apply_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProxyAuth(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_scheme: Optional[_builtins.str] = ..., client_password_auth_type: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., iam_auth: Optional[_builtins.str] = ..., secret_arn: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authScheme")
    def auth_scheme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientPasswordAuthType")
    def client_password_auth_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamAuth")
    def iam_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProxyDefaultTargetGroupConnectionPoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_borrow_timeout: Optional[_builtins.int] = ..., init_query: Optional[_builtins.str] = ..., max_connections_percent: Optional[_builtins.int] = ..., max_idle_connections_percent: Optional[_builtins.int] = ..., session_pinning_filters: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionBorrowTimeout")
    def connection_borrow_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initQuery")
    def init_query(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConnectionsPercent")
    def max_connections_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleConnectionsPercent")
    def max_idle_connections_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPinningFilters")
    def session_pinning_filters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ReservedInstanceRecurringCharge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recurring_charge_amount: Optional[_builtins.int] = ..., recurring_charge_frequency: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringChargeAmount")
    def recurring_charge_amount(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringChargeFrequency")
    def recurring_charge_frequency(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ShardGroupTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterMasterUserSecretResult(dict):
    def __init__(__self__, *, kms_key_id: _builtins.str, secret_arn: _builtins.str, secret_status: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetClustersFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetEngineVersionFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetGlobalClusterMemberResult(dict):
    def __init__(__self__, *, db_cluster_arn: _builtins.str, is_writer: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetInstanceMasterUserSecretResult(dict):
    def __init__(__self__, *, kms_key_id: _builtins.str, secret_arn: _builtins.str, secret_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstancesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetProxyAuthResult(dict):
    def __init__(__self__, *, auth_scheme: _builtins.str, client_password_auth_type: _builtins.str, description: _builtins.str, iam_auth: _builtins.str, secret_arn: _builtins.str, username: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authScheme")
    def auth_scheme(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientPasswordAuthType")
    def client_password_auth_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamAuth")
    def iam_auth(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        ...
    


