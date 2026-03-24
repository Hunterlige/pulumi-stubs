import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainAdvancedSecurityOptions",
    "DomainAdvancedSecurityOptionsMasterUserOptions",
    "DomainAutoTuneOptions",
    "DomainAutoTuneOptionsMaintenanceSchedule",
    "DomainAutoTuneOptionsMaintenanceScheduleDuration",
    "DomainClusterConfig",
    "DomainClusterConfigColdStorageOptions",
    "DomainClusterConfigZoneAwarenessConfig",
    "DomainCognitoOptions",
    "DomainDomainEndpointOptions",
    "DomainEbsOptions",
    "DomainEncryptAtRest",
    "DomainLogPublishingOption",
    "DomainNodeToNodeEncryption",
    "DomainSamlOptionsSamlOptions",
    "DomainSamlOptionsSamlOptionsIdp",
    "DomainSnapshotOptions",
    "DomainVpcOptions",
    "VpcEndpointVpcOptions",
    "GetDomainAdvancedSecurityOptionResult",
    "GetDomainAutoTuneOptionResult",
    "GetDomainAutoTuneOptionMaintenanceScheduleResult",
    ...,
    "GetDomainClusterConfigResult",
    "GetDomainClusterConfigColdStorageOptionResult",
    "GetDomainClusterConfigZoneAwarenessConfigResult",
    "GetDomainCognitoOptionResult",
    "GetDomainEbsOptionResult",
    "GetDomainEncryptionAtRestResult",
    "GetDomainLogPublishingOptionResult",
    "GetDomainNodeToNodeEncryptionResult",
    "GetDomainSnapshotOptionResult",
    "GetDomainVpcOptionResult",
]

@pulumi.output_type
class DomainAdvancedSecurityOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        internal_user_database_enabled: Optional[_builtins.bool] = ...,
        master_user_options: Optional[
            outputs.DomainAdvancedSecurityOptionsMasterUserOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserOptions")
    def master_user_options(
        self,
    ) -> Optional[outputs.DomainAdvancedSecurityOptionsMasterUserOptions]: ...

@pulumi.output_type
class DomainAdvancedSecurityOptionsMasterUserOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        master_user_arn: Optional[_builtins.str] = ...,
        master_user_name: Optional[_builtins.str] = ...,
        master_user_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="masterUserArn")
    def master_user_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAutoTuneOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        maintenance_schedules: Optional[
            Sequence[outputs.DomainAutoTuneOptionsMaintenanceSchedule]
        ] = ...,
        rollback_on_disable: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> Optional[Sequence[outputs.DomainAutoTuneOptionsMaintenanceSchedule]]: ...
    @_builtins.property
    @pulumi.getter(name="rollbackOnDisable")
    def rollback_on_disable(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAutoTuneOptionsMaintenanceSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cron_expression_for_recurrence: _builtins.str,
        duration: outputs.DomainAutoTuneOptionsMaintenanceScheduleDuration,
        start_at: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> outputs.DomainAutoTuneOptionsMaintenanceScheduleDuration: ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> _builtins.str: ...

@pulumi.output_type
class DomainAutoTuneOptionsMaintenanceScheduleDuration(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class DomainClusterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cold_storage_options: Optional[
            outputs.DomainClusterConfigColdStorageOptions
        ] = ...,
        dedicated_master_count: Optional[_builtins.int] = ...,
        dedicated_master_enabled: Optional[_builtins.bool] = ...,
        dedicated_master_type: Optional[_builtins.str] = ...,
        instance_count: Optional[_builtins.int] = ...,
        instance_type: Optional[_builtins.str] = ...,
        warm_count: Optional[_builtins.int] = ...,
        warm_enabled: Optional[_builtins.bool] = ...,
        warm_type: Optional[_builtins.str] = ...,
        zone_awareness_config: Optional[
            outputs.DomainClusterConfigZoneAwarenessConfig
        ] = ...,
        zone_awareness_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> Optional[outputs.DomainClusterConfigColdStorageOptions]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterCount")
    def dedicated_master_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterType")
    def dedicated_master_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="warmCount")
    def warm_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="warmEnabled")
    def warm_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="warmType")
    def warm_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> Optional[outputs.DomainClusterConfigZoneAwarenessConfig]: ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DomainClusterConfigColdStorageOptions(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DomainClusterConfigZoneAwarenessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_zone_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneCount")
    def availability_zone_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainCognitoOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_pool_id: _builtins.str,
        role_arn: _builtins.str,
        user_pool_id: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DomainDomainEndpointOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_endpoint: Optional[_builtins.str] = ...,
        custom_endpoint_certificate_arn: Optional[_builtins.str] = ...,
        custom_endpoint_enabled: Optional[_builtins.bool] = ...,
        enforce_https: Optional[_builtins.bool] = ...,
        tls_security_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customEndpoint")
    def custom_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customEndpointEnabled")
    def custom_endpoint_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainEbsOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ebs_enabled: _builtins.bool,
        iops: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_size: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsEnabled")
    def ebs_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainEncryptAtRest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, kms_key_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainLogPublishingOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_log_group_arn: _builtins.str,
        log_type: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DomainNodeToNodeEncryption(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class DomainSamlOptionsSamlOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        idp: Optional[outputs.DomainSamlOptionsSamlOptionsIdp] = ...,
        master_backend_role: Optional[_builtins.str] = ...,
        master_user_name: Optional[_builtins.str] = ...,
        roles_key: Optional[_builtins.str] = ...,
        session_timeout_minutes: Optional[_builtins.int] = ...,
        subject_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def idp(self) -> Optional[outputs.DomainSamlOptionsSamlOptionsIdp]: ...
    @_builtins.property
    @pulumi.getter(name="masterBackendRole")
    def master_backend_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rolesKey")
    def roles_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutMinutes")
    def session_timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="subjectKey")
    def subject_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainSamlOptionsSamlOptionsIdp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, entity_id: _builtins.str, metadata_content: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataContent")
    def metadata_content(self) -> _builtins.str: ...

@pulumi.output_type
class DomainSnapshotOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, automated_snapshot_start_hour: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> _builtins.int: ...

@pulumi.output_type
class DomainVpcOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VpcEndpointVpcOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_ids: Sequence[_builtins.str],
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetDomainAdvancedSecurityOptionResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        internal_user_database_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDomainAutoTuneOptionResult(dict):
    def __init__(
        __self__,
        *,
        desired_state: _builtins.str,
        maintenance_schedules: Sequence[
            outputs.GetDomainAutoTuneOptionMaintenanceScheduleResult
        ],
        rollback_on_disable: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> Sequence[outputs.GetDomainAutoTuneOptionMaintenanceScheduleResult]: ...
    @_builtins.property
    @pulumi.getter(name="rollbackOnDisable")
    def rollback_on_disable(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainAutoTuneOptionMaintenanceScheduleResult(dict):
    def __init__(
        __self__,
        *,
        cron_expression_for_recurrence: _builtins.str,
        durations: Sequence[
            outputs.GetDomainAutoTuneOptionMaintenanceScheduleDurationResult
        ],
        start_at: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def durations(
        self,
    ) -> Sequence[outputs.GetDomainAutoTuneOptionMaintenanceScheduleDurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainAutoTuneOptionMaintenanceScheduleDurationResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetDomainClusterConfigResult(dict):
    def __init__(
        __self__,
        *,
        cold_storage_options: Sequence[
            outputs.GetDomainClusterConfigColdStorageOptionResult
        ],
        dedicated_master_count: _builtins.int,
        dedicated_master_enabled: _builtins.bool,
        dedicated_master_type: _builtins.str,
        instance_count: _builtins.int,
        instance_type: _builtins.str,
        warm_count: _builtins.int,
        warm_enabled: _builtins.bool,
        warm_type: _builtins.str,
        zone_awareness_configs: Sequence[
            outputs.GetDomainClusterConfigZoneAwarenessConfigResult
        ],
        zone_awareness_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> Sequence[outputs.GetDomainClusterConfigColdStorageOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterCount")
    def dedicated_master_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterType")
    def dedicated_master_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="warmCount")
    def warm_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="warmEnabled")
    def warm_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="warmType")
    def warm_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessConfigs")
    def zone_awareness_configs(
        self,
    ) -> Sequence[outputs.GetDomainClusterConfigZoneAwarenessConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDomainClusterConfigColdStorageOptionResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDomainClusterConfigZoneAwarenessConfigResult(dict):
    def __init__(__self__, *, availability_zone_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneCount")
    def availability_zone_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetDomainCognitoOptionResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        identity_pool_id: _builtins.str,
        role_arn: _builtins.str,
        user_pool_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainEbsOptionResult(dict):
    def __init__(
        __self__,
        *,
        ebs_enabled: _builtins.bool,
        iops: _builtins.int,
        throughput: _builtins.int,
        volume_size: _builtins.int,
        volume_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsEnabled")
    def ebs_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainEncryptionAtRestResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, kms_key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainLogPublishingOptionResult(dict):
    def __init__(
        __self__,
        *,
        cloudwatch_log_group_arn: _builtins.str,
        enabled: _builtins.bool,
        log_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDomainNodeToNodeEncryptionResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDomainSnapshotOptionResult(dict):
    def __init__(__self__, *, automated_snapshot_start_hour: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> _builtins.int: ...

@pulumi.output_type
class GetDomainVpcOptionResult(dict):
    def __init__(
        __self__,
        *,
        availability_zones: Sequence[_builtins.str],
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
