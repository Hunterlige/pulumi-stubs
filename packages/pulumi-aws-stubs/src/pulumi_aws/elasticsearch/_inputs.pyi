

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import iam

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainAdvancedSecurityOptionsArgs', 'DomainAdvancedSecurityOptionsArgsDict', 'DomainAdvancedSecurityOptionsMasterUserOptionsArgs', ..., 'DomainAutoTuneOptionsArgs', 'DomainAutoTuneOptionsArgsDict', 'DomainAutoTuneOptionsMaintenanceScheduleArgs', 'DomainAutoTuneOptionsMaintenanceScheduleArgsDict', ..., ..., 'DomainClusterConfigArgs', 'DomainClusterConfigArgsDict', 'DomainClusterConfigColdStorageOptionsArgs', 'DomainClusterConfigColdStorageOptionsArgsDict', 'DomainClusterConfigZoneAwarenessConfigArgs', 'DomainClusterConfigZoneAwarenessConfigArgsDict', 'DomainCognitoOptionsArgs', 'DomainCognitoOptionsArgsDict', 'DomainDomainEndpointOptionsArgs', 'DomainDomainEndpointOptionsArgsDict', 'DomainEbsOptionsArgs', 'DomainEbsOptionsArgsDict', 'DomainEncryptAtRestArgs', 'DomainEncryptAtRestArgsDict', 'DomainLogPublishingOptionArgs', 'DomainLogPublishingOptionArgsDict', 'DomainNodeToNodeEncryptionArgs', 'DomainNodeToNodeEncryptionArgsDict', 'DomainSamlOptionsSamlOptionsArgs', 'DomainSamlOptionsSamlOptionsArgsDict', 'DomainSamlOptionsSamlOptionsIdpArgs', 'DomainSamlOptionsSamlOptionsIdpArgsDict', 'DomainSnapshotOptionsArgs', 'DomainSnapshotOptionsArgsDict', 'DomainVpcOptionsArgs', 'DomainVpcOptionsArgsDict', 'PolicyDocumentArgs', 'PolicyDocumentArgsDict', 'VpcEndpointVpcOptionsArgs', 'VpcEndpointVpcOptionsArgsDict']
class DomainAdvancedSecurityOptionsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    internal_user_database_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    master_user_options: NotRequired[pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgsDict]]


@pulumi.input_type
class DomainAdvancedSecurityOptionsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], internal_user_database_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., master_user_options: Optional[pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @internal_user_database_enabled.setter
    def internal_user_database_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserOptions")
    def master_user_options(self) -> Optional[pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]]:
        
        ...
    
    @master_user_options.setter
    def master_user_options(self, value: Optional[pulumi.Input[DomainAdvancedSecurityOptionsMasterUserOptionsArgs]]): # -> None:
        ...
    


class DomainAdvancedSecurityOptionsMasterUserOptionsArgsDict(TypedDict):
    master_user_arn: NotRequired[pulumi.Input[_builtins.str]]
    master_user_name: NotRequired[pulumi.Input[_builtins.str]]
    master_user_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainAdvancedSecurityOptionsMasterUserOptionsArgs:
    def __init__(__self__, *, master_user_arn: Optional[pulumi.Input[_builtins.str]] = ..., master_user_name: Optional[pulumi.Input[_builtins.str]] = ..., master_user_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserArn")
    def master_user_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_user_arn.setter
    def master_user_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_user_name.setter
    def master_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserPassword")
    def master_user_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_user_password.setter
    def master_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainAutoTuneOptionsArgsDict(TypedDict):
    desired_state: pulumi.Input[_builtins.str]
    maintenance_schedules: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgsDict]]]]
    rollback_on_disable: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainAutoTuneOptionsArgs:
    def __init__(__self__, *, desired_state: pulumi.Input[_builtins.str], maintenance_schedules: Optional[pulumi.Input[Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]]] = ..., rollback_on_disable: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]]]:
        
        ...
    
    @maintenance_schedules.setter
    def maintenance_schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollbackOnDisable")
    def rollback_on_disable(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rollback_on_disable.setter
    def rollback_on_disable(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainAutoTuneOptionsMaintenanceScheduleArgsDict(TypedDict):
    cron_expression_for_recurrence: pulumi.Input[_builtins.str]
    duration: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgsDict]
    start_at: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainAutoTuneOptionsMaintenanceScheduleArgs:
    def __init__(__self__, *, cron_expression_for_recurrence: pulumi.Input[_builtins.str], duration: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs], start_at: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cron_expression_for_recurrence.setter
    def cron_expression_for_recurrence(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[DomainAutoTuneOptionsMaintenanceScheduleDurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainAutoTuneOptionsMaintenanceScheduleDurationArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainAutoTuneOptionsMaintenanceScheduleDurationArgs:
    def __init__(__self__, *, unit: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainClusterConfigArgsDict(TypedDict):
    cold_storage_options: NotRequired[pulumi.Input[DomainClusterConfigColdStorageOptionsArgsDict]]
    dedicated_master_count: NotRequired[pulumi.Input[_builtins.int]]
    dedicated_master_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    dedicated_master_type: NotRequired[pulumi.Input[_builtins.str]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    warm_count: NotRequired[pulumi.Input[_builtins.int]]
    warm_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    warm_type: NotRequired[pulumi.Input[_builtins.str]]
    zone_awareness_config: NotRequired[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgsDict]]
    zone_awareness_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DomainClusterConfigArgs:
    def __init__(__self__, *, cold_storage_options: Optional[pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]] = ..., dedicated_master_count: Optional[pulumi.Input[_builtins.int]] = ..., dedicated_master_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., dedicated_master_type: Optional[pulumi.Input[_builtins.str]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., warm_count: Optional[pulumi.Input[_builtins.int]] = ..., warm_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., warm_type: Optional[pulumi.Input[_builtins.str]] = ..., zone_awareness_config: Optional[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]] = ..., zone_awareness_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coldStorageOptions")
    def cold_storage_options(self) -> Optional[pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]]:
        
        ...
    
    @cold_storage_options.setter
    def cold_storage_options(self, value: Optional[pulumi.Input[DomainClusterConfigColdStorageOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterCount")
    def dedicated_master_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dedicated_master_count.setter
    def dedicated_master_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterEnabled")
    def dedicated_master_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @dedicated_master_enabled.setter
    def dedicated_master_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedMasterType")
    def dedicated_master_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dedicated_master_type.setter
    def dedicated_master_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmCount")
    def warm_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @warm_count.setter
    def warm_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmEnabled")
    def warm_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @warm_enabled.setter
    def warm_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmType")
    def warm_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @warm_type.setter
    def warm_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessConfig")
    def zone_awareness_config(self) -> Optional[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]]:
        
        ...
    
    @zone_awareness_config.setter
    def zone_awareness_config(self, value: Optional[pulumi.Input[DomainClusterConfigZoneAwarenessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneAwarenessEnabled")
    def zone_awareness_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zone_awareness_enabled.setter
    def zone_awareness_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DomainClusterConfigColdStorageOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DomainClusterConfigColdStorageOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DomainClusterConfigZoneAwarenessConfigArgsDict(TypedDict):
    availability_zone_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainClusterConfigZoneAwarenessConfigArgs:
    def __init__(__self__, *, availability_zone_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneCount")
    def availability_zone_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @availability_zone_count.setter
    def availability_zone_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainCognitoOptionsArgsDict(TypedDict):
    identity_pool_id: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    user_pool_id: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DomainCognitoOptionsArgs:
    def __init__(__self__, *, identity_pool_id: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], user_pool_id: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DomainDomainEndpointOptionsArgsDict(TypedDict):
    custom_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    custom_endpoint_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    custom_endpoint_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    enforce_https: NotRequired[pulumi.Input[_builtins.bool]]
    tls_security_policy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDomainEndpointOptionsArgs:
    def __init__(__self__, *, custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., custom_endpoint_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., enforce_https: Optional[pulumi.Input[_builtins.bool]] = ..., tls_security_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customEndpoint")
    def custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_endpoint.setter
    def custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_endpoint_certificate_arn.setter
    def custom_endpoint_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customEndpointEnabled")
    def custom_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @custom_endpoint_enabled.setter
    def custom_endpoint_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce_https.setter
    def enforce_https(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tls_security_policy.setter
    def tls_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainEbsOptionsArgsDict(TypedDict):
    ebs_enabled: pulumi.Input[_builtins.bool]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainEbsOptionsArgs:
    def __init__(__self__, *, ebs_enabled: pulumi.Input[_builtins.bool], iops: Optional[pulumi.Input[_builtins.int]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ..., volume_size: Optional[pulumi.Input[_builtins.int]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsEnabled")
    def ebs_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @ebs_enabled.setter
    def ebs_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainEncryptAtRestArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainEncryptAtRestArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainLogPublishingOptionArgsDict(TypedDict):
    cloudwatch_log_group_arn: pulumi.Input[_builtins.str]
    log_type: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DomainLogPublishingOptionArgs:
    def __init__(__self__, *, cloudwatch_log_group_arn: pulumi.Input[_builtins.str], log_type: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DomainNodeToNodeEncryptionArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class DomainNodeToNodeEncryptionArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class DomainSamlOptionsSamlOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    idp: NotRequired[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgsDict]]
    master_backend_role: NotRequired[pulumi.Input[_builtins.str]]
    master_user_name: NotRequired[pulumi.Input[_builtins.str]]
    roles_key: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    subject_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainSamlOptionsSamlOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., idp: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]] = ..., master_backend_role: Optional[pulumi.Input[_builtins.str]] = ..., master_user_name: Optional[pulumi.Input[_builtins.str]] = ..., roles_key: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ..., subject_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def idp(self) -> Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]]:
        
        ...
    
    @idp.setter
    def idp(self, value: Optional[pulumi.Input[DomainSamlOptionsSamlOptionsIdpArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterBackendRole")
    def master_backend_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_backend_role.setter
    def master_backend_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserName")
    def master_user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_user_name.setter
    def master_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolesKey")
    def roles_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @roles_key.setter
    def roles_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutMinutes")
    def session_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout_minutes.setter
    def session_timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectKey")
    def subject_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject_key.setter
    def subject_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainSamlOptionsSamlOptionsIdpArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    metadata_content: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainSamlOptionsSamlOptionsIdpArgs:
    def __init__(__self__, *, entity_id: pulumi.Input[_builtins.str], metadata_content: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataContent")
    def metadata_content(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @metadata_content.setter
    def metadata_content(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainSnapshotOptionsArgsDict(TypedDict):
    automated_snapshot_start_hour: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainSnapshotOptionsArgs:
    def __init__(__self__, *, automated_snapshot_start_hour: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @automated_snapshot_start_hour.setter
    def automated_snapshot_start_hour(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainVpcOptionsArgsDict(TypedDict):
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainVpcOptionsArgs:
    def __init__(__self__, *, availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PolicyDocumentArgsDict(TypedDict):
    
    statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgsDict]]]
    version: pulumi.Input[iam.PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(__self__, *, statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]], version: pulumi.Input[iam.PolicyDocumentVersion], id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(self) -> pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]:
        ...
    
    @statement.setter
    def statement(self, value: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[iam.PolicyDocumentVersion]:
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[iam.PolicyDocumentVersion]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcEndpointVpcOptionsArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcEndpointVpcOptionsArgs:
    def __init__(__self__, *, subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


