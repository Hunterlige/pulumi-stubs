import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterInstanceArgs", "ClusterInstance"]

@pulumi.input_type
class ClusterInstanceArgs:
    def __init__(
        __self__,
        *,
        cluster_identifier: pulumi.Input[_builtins.str],
        engine: pulumi.Input[EngineType],
        instance_class: pulumi.Input[Union[_builtins.str, InstanceType]],
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        promotion_tier: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Input[EngineType]: ...
    @engine.setter
    def engine(self, value: pulumi.Input[EngineType]): ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Input[Union[_builtins.str, InstanceType]]: ...
    @instance_class.setter
    def instance_class(
        self, value: pulumi.Input[Union[_builtins.str, InstanceType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="customIamInstanceProfile")
    def custom_iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_iam_instance_profile.setter
    def custom_iam_instance_profile(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_parameter_group_name.setter
    def db_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identifierPrefix")
    def identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier_prefix.setter
    def identifier_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitoring_interval.setter
    def monitoring_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_role_arn.setter
    def monitoring_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsEnabled")
    def performance_insights_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @performance_insights_enabled.setter
    def performance_insights_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_insights_kms_key_id.setter
    def performance_insights_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @performance_insights_retention_period.setter
    def performance_insights_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="promotionTier")
    def promotion_tier(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @promotion_tier.setter
    def promotion_tier(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ClusterInstanceState:
    def __init__(
        __self__,
        *,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dbi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[EngineType]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        promotion_tier: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        writer: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="customIamInstanceProfile")
    def custom_iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_iam_instance_profile.setter
    def custom_iam_instance_profile(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_parameter_group_name.setter
    def db_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbiResourceId")
    def dbi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dbi_resource_id.setter
    def dbi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[EngineType]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[EngineType]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version_actual.setter
    def engine_version_actual(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identifierPrefix")
    def identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier_prefix.setter
    def identifier_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]: ...
    @instance_class.setter
    def instance_class(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitoring_interval.setter
    def monitoring_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_role_arn.setter
    def monitoring_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsEnabled")
    def performance_insights_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @performance_insights_enabled.setter
    def performance_insights_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_insights_kms_key_id.setter
    def performance_insights_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @performance_insights_retention_period.setter
    def performance_insights_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="promotionTier")
    def promotion_tier(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @promotion_tier.setter
    def promotion_tier(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def writer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @writer.setter
    def writer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:rds/clusterInstance:ClusterInstance")
class ClusterInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[EngineType]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        promotion_tier: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        db_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dbi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[EngineType]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        promotion_tier: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        writer: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> ClusterInstance: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="customIamInstanceProfile")
    def custom_iam_instance_profile(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbiResourceId")
    def dbi_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[EngineType]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identifierPrefix")
    def identifier_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsEnabled")
    def performance_insights_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promotionTier")
    def promotion_tier(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def writer(self) -> pulumi.Output[_builtins.bool]: ...
