import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        engine: pulumi.Input[Union[_builtins.str, EngineType]],
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backtrack_window: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_scalability_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_global_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_local_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_mode: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
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
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_source_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[ClusterRestoreToPointInTimeArgs]
        ] = ...,
        s3_import: Optional[pulumi.Input[ClusterS3ImportArgs]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[ClusterScalingConfigurationArgs]
        ] = ...,
        serverlessv2_scaling_configuration: Optional[
            pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Input[Union[_builtins.str, EngineType]]: ...
    @engine.setter
    def engine(self, value: pulumi.Input[Union[_builtins.str, EngineType]]): ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backtrack_window.setter
    def backtrack_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_identifier.setter
    def ca_certificate_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier_prefix.setter
    def cluster_identifier_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_members.setter
    def cluster_members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterScalabilityType")
    def cluster_scalability_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_scalability_type.setter
    def cluster_scalability_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_insights_mode.setter
    def database_insights_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterInstanceClass")
    def db_cluster_instance_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_instance_class.setter
    def db_cluster_instance_class(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceParameterGroupName")
    def db_instance_parameter_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_parameter_group_name.setter
    def db_instance_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_system_id.setter
    def db_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteAutomatedBackups")
    def delete_automated_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_automated_backups.setter
    def delete_automated_backups(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_iam_role_name.setter
    def domain_iam_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableGlobalWriteForwarding")
    def enable_global_write_forwarding(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_global_write_forwarding.setter
    def enable_global_write_forwarding(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http_endpoint.setter
    def enable_http_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableLocalWriteForwarding")
    def enable_local_write_forwarding(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_local_write_forwarding.setter
    def enable_local_write_forwarding(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_lifecycle_support.setter
    def engine_lifecycle_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineMode")
    def engine_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EngineMode]]]: ...
    @engine_mode.setter
    def engine_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @iam_database_authentication_enabled.setter
    def iam_database_authentication_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_user_password.setter
    def manage_master_user_password(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @master_password_wo_version.setter
    def master_password_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecretKmsKeyId")
    def master_user_secret_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_secret_kms_key_id.setter
    def master_user_secret_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_source_identifier.setter
    def replication_source_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]: ...
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(
        self, value: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> Optional[pulumi.Input[ClusterS3ImportArgs]]: ...
    @s3_import.setter
    def s3_import(self, value: Optional[pulumi.Input[ClusterS3ImportArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[ClusterScalingConfigurationArgs]]: ...
    @scaling_configuration.setter
    def scaling_configuration(
        self, value: Optional[pulumi.Input[ClusterScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverlessv2ScalingConfiguration")
    def serverlessv2_scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]]: ...
    @serverlessv2_scaling_configuration.setter
    def serverlessv2_scaling_configuration(
        self, value: Optional[pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_region.setter
    def source_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backtrack_window: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_valid_till: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_scalability_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_global_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_local_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[Union[_builtins.str, EngineType]]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_mode: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]
        ] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
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
        reader_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_source_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[ClusterRestoreToPointInTimeArgs]
        ] = ...,
        s3_import: Optional[pulumi.Input[ClusterS3ImportArgs]] = ...,
        scaling_configuration: Optional[
            pulumi.Input[ClusterScalingConfigurationArgs]
        ] = ...,
        serverlessv2_scaling_configuration: Optional[
            pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        upgrade_rollout_order: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backtrack_window.setter
    def backtrack_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_identifier.setter
    def ca_certificate_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateValidTill")
    def ca_certificate_valid_till(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_valid_till.setter
    def ca_certificate_valid_till(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier_prefix.setter
    def cluster_identifier_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_members.setter
    def cluster_members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_resource_id.setter
    def cluster_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterScalabilityType")
    def cluster_scalability_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_scalability_type.setter
    def cluster_scalability_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_insights_mode.setter
    def database_insights_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterInstanceClass")
    def db_cluster_instance_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_instance_class.setter
    def db_cluster_instance_class(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceParameterGroupName")
    def db_instance_parameter_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_parameter_group_name.setter
    def db_instance_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_system_id.setter
    def db_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteAutomatedBackups")
    def delete_automated_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_automated_backups.setter
    def delete_automated_backups(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_iam_role_name.setter
    def domain_iam_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableGlobalWriteForwarding")
    def enable_global_write_forwarding(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_global_write_forwarding.setter
    def enable_global_write_forwarding(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http_endpoint.setter
    def enable_http_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableLocalWriteForwarding")
    def enable_local_write_forwarding(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_local_write_forwarding.setter
    def enable_local_write_forwarding(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[Union[_builtins.str, EngineType]]]: ...
    @engine.setter
    def engine(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EngineType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_lifecycle_support.setter
    def engine_lifecycle_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineMode")
    def engine_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EngineMode]]]: ...
    @engine_mode.setter
    def engine_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]]
    ): ...
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
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @iam_database_authentication_enabled.setter
    def iam_database_authentication_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_user_password.setter
    def manage_master_user_password(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @master_password_wo_version.setter
    def master_password_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecretKmsKeyId")
    def master_user_secret_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_user_secret_kms_key_id.setter
    def master_user_secret_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]
    ]: ...
    @master_user_secrets.setter
    def master_user_secrets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reader_endpoint.setter
    def reader_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_source_identifier.setter
    def replication_source_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]: ...
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(
        self, value: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> Optional[pulumi.Input[ClusterS3ImportArgs]]: ...
    @s3_import.setter
    def s3_import(self, value: Optional[pulumi.Input[ClusterS3ImportArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[ClusterScalingConfigurationArgs]]: ...
    @scaling_configuration.setter
    def scaling_configuration(
        self, value: Optional[pulumi.Input[ClusterScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverlessv2ScalingConfiguration")
    def serverlessv2_scaling_configuration(
        self,
    ) -> Optional[pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]]: ...
    @serverlessv2_scaling_configuration.setter
    def serverlessv2_scaling_configuration(
        self, value: Optional[pulumi.Input[ClusterServerlessv2ScalingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_region.setter
    def source_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upgrade_rollout_order.setter
    def upgrade_rollout_order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:rds/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backtrack_window: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_scalability_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_global_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_local_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        engine: Optional[pulumi.Input[Union[_builtins.str, EngineType]]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_mode: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
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
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_source_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreToPointInTimeArgs, ClusterRestoreToPointInTimeArgsDict
                ]
            ]
        ] = ...,
        s3_import: Optional[
            pulumi.Input[Union[ClusterS3ImportArgs, ClusterS3ImportArgsDict]]
        ] = ...,
        scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    ClusterScalingConfigurationArgs, ClusterScalingConfigurationArgsDict
                ]
            ]
        ] = ...,
        serverlessv2_scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    ClusterServerlessv2ScalingConfigurationArgs,
                    ClusterServerlessv2ScalingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backtrack_window: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_valid_till: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_scalability_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_global_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_local_write_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[Union[_builtins.str, EngineType]]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_mode: Optional[pulumi.Input[Union[_builtins.str, EngineMode]]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_secrets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterMasterUserSecretArgs, ClusterMasterUserSecretArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
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
        reader_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_source_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreToPointInTimeArgs, ClusterRestoreToPointInTimeArgsDict
                ]
            ]
        ] = ...,
        s3_import: Optional[
            pulumi.Input[Union[ClusterS3ImportArgs, ClusterS3ImportArgsDict]]
        ] = ...,
        scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    ClusterScalingConfigurationArgs, ClusterScalingConfigurationArgsDict
                ]
            ]
        ] = ...,
        serverlessv2_scaling_configuration: Optional[
            pulumi.Input[
                Union[
                    ClusterServerlessv2ScalingConfigurationArgs,
                    ClusterServerlessv2ScalingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_region: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        upgrade_rollout_order: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateValidTill")
    def ca_certificate_valid_till(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterScalabilityType")
    def cluster_scalability_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterInstanceClass")
    def db_cluster_instance_class(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceParameterGroupName")
    def db_instance_parameter_group_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteAutomatedBackups")
    def delete_automated_backups(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableGlobalWriteForwarding")
    def enable_global_write_forwarding(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableLocalWriteForwarding")
    def enable_local_write_forwarding(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineMode")
    def engine_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecretKmsKeyId")
    def master_user_secret_kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterMasterUserSecret]]: ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="performanceInsightsEnabled")
    def performance_insights_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRestoreToPointInTime]]: ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> pulumi.Output[Optional[outputs.ClusterS3Import]]: ...
    @_builtins.property
    @pulumi.getter(name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterScalingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessv2ScalingConfiguration")
    def serverlessv2_scaling_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterServerlessv2ScalingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
