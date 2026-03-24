

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cluster_members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ..., master_password: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., master_username: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_point_in_time: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]] = ..., serverless_v2_scaling_configuration: Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]] = ..., skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier_prefix.setter
    def cluster_identifier_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cluster_members.setter
    def cluster_members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manage_master_user_password.setter
    def manage_master_user_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @master_password_wo_version.setter
    def master_password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(self) -> Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]:
        
        ...
    
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(self, value: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverlessV2ScalingConfiguration")
    def serverless_v2_scaling_configuration(self) -> Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]]:
        
        ...
    
    @serverless_v2_scaling_configuration.setter
    def serverless_v2_scaling_configuration(self, value: Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cluster_members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ..., master_password: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., master_user_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]] = ..., master_username: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., reader_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_point_in_time: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]] = ..., serverless_v2_scaling_configuration: Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]] = ..., skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier_prefix.setter
    def cluster_identifier_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cluster_members.setter
    def cluster_members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_resource_id.setter
    def cluster_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manage_master_user_password.setter
    def manage_master_user_password(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @master_password_wo_version.setter
    def master_password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]]:
        ...
    
    @master_user_secrets.setter
    def master_user_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMasterUserSecretArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reader_endpoint.setter
    def reader_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(self) -> Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]:
        
        ...
    
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(self, value: Optional[pulumi.Input[ClusterRestoreToPointInTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverlessV2ScalingConfiguration")
    def serverless_v2_scaling_configuration(self) -> Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]]:
        
        ...
    
    @serverless_v2_scaling_configuration.setter
    def serverless_v2_scaling_configuration(self, value: Optional[pulumi.Input[ClusterServerlessV2ScalingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:docdb/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cluster_members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ..., master_password: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., master_username: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_point_in_time: Optional[pulumi.Input[Union[ClusterRestoreToPointInTimeArgs, ClusterRestoreToPointInTimeArgsDict]]] = ..., serverless_v2_scaling_configuration: Optional[pulumi.Input[Union[ClusterServerlessV2ScalingConfigurationArgs, ClusterServerlessV2ScalingConfigurationArgsDict]]] = ..., skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ClusterArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cluster_members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., db_cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cloudwatch_logs_exports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ..., master_password: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ..., master_user_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterMasterUserSecretArgs, ClusterMasterUserSecretArgsDict]]]]] = ..., master_username: Optional[pulumi.Input[_builtins.str]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., reader_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_point_in_time: Optional[pulumi.Input[Union[ClusterRestoreToPointInTimeArgs, ClusterRestoreToPointInTimeArgsDict]]] = ..., serverless_v2_scaling_configuration: Optional[pulumi.Input[Union[ClusterServerlessV2ScalingConfigurationArgs, ClusterServerlessV2ScalingConfigurationArgsDict]]] = ..., skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(self) -> pulumi.Output[Sequence[outputs.ClusterMasterUserSecret]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(self) -> pulumi.Output[Optional[outputs.ClusterRestoreToPointInTime]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverlessV2ScalingConfiguration")
    def serverless_v2_scaling_configuration(self) -> pulumi.Output[Optional[outputs.ClusterServerlessV2ScalingConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


