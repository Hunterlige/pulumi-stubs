import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceArgs", "Instance"]

@pulumi.input_type
class InstanceArgs:
    def __init__(
        __self__,
        *,
        instance_class: pulumi.Input[Union[_builtins.str, InstanceType]],
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_target: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        blue_green_update: Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_owned_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_log_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_auth_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_dns_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_ou: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_model: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        max_allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        nchar_character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        option_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        replicate_source_db: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[InstanceRestoreToPointInTimeArgs]
        ] = ...,
        s3_import: Optional[pulumi.Input[InstanceS3ImportArgs]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_storage_config: Optional[pulumi.Input[_builtins.bool]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Input[Union[_builtins.str, InstanceType]]: ...
    @instance_class.setter
    def instance_class(
        self, value: pulumi.Input[Union[_builtins.str, InstanceType]]
    ): ...
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
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="backupTarget")
    def backup_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_target.setter
    def backup_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_window.setter
    def backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blueGreenUpdate")
    def blue_green_update(
        self,
    ) -> Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]]: ...
    @blue_green_update.setter
    def blue_green_update(
        self, value: Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="characterSetName")
    def character_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @character_set_name.setter
    def character_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="customerOwnedIpEnabled")
    def customer_owned_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @customer_owned_ip_enabled.setter
    def customer_owned_ip_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_insights_mode.setter
    def database_insights_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedLogVolume")
    def dedicated_log_volume(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_log_volume.setter
    def dedicated_log_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="domainAuthSecretArn")
    def domain_auth_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_auth_secret_arn.setter
    def domain_auth_secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainDnsIps")
    def domain_dns_ips(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domain_dns_ips.setter
    def domain_dns_ips(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_fqdn.setter
    def domain_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_iam_role_name.setter
    def domain_iam_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainOu")
    def domain_ou(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_ou.setter
    def domain_ou(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_lifecycle_support.setter
    def engine_lifecycle_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @iam_database_authentication_enabled.setter
    def iam_database_authentication_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_user_password.setter
    def manage_master_user_password(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
    @pulumi.getter(name="maxAllocatedStorage")
    def max_allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_allocated_storage.setter
    def max_allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ncharCharacterSetName")
    def nchar_character_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nchar_character_set_name.setter
    def nchar_character_set_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @option_group_name.setter
    def option_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="replicaMode")
    def replica_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_mode.setter
    def replica_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicateSourceDb")
    def replicate_source_db(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replicate_source_db.setter
    def replicate_source_db(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> Optional[pulumi.Input[InstanceRestoreToPointInTimeArgs]]: ...
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(
        self, value: Optional[pulumi.Input[InstanceRestoreToPointInTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> Optional[pulumi.Input[InstanceS3ImportArgs]]: ...
    @s3_import.setter
    def s3_import(self, value: Optional[pulumi.Input[InstanceS3ImportArgs]]): ...
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
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageThroughput")
    def storage_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_throughput.setter
    def storage_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]: ...
    @storage_type.setter
    def storage_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]
    ): ...
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
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeStorageConfig")
    def upgrade_storage_config(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @upgrade_storage_config.setter
    def upgrade_storage_config(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _InstanceState:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_target: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        blue_green_update: Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_owned_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_log_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_auth_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_dns_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_ou: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_restorable_time: Optional[pulumi.Input[_builtins.str]] = ...,
        license_model: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceListenerEndpointArgs]]]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceMasterUserSecretArgs]]]
        ] = ...,
        max_allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        nchar_character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        option_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        replicate_source_db: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[InstanceRestoreToPointInTimeArgs]
        ] = ...,
        s3_import: Optional[pulumi.Input[InstanceS3ImportArgs]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_rollout_order: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_storage_config: Optional[pulumi.Input[_builtins.bool]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_period.setter
    def backup_retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="backupTarget")
    def backup_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_target.setter
    def backup_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_window.setter
    def backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blueGreenUpdate")
    def blue_green_update(
        self,
    ) -> Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]]: ...
    @blue_green_update.setter
    def blue_green_update(
        self, value: Optional[pulumi.Input[InstanceBlueGreenUpdateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="characterSetName")
    def character_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @character_set_name.setter
    def character_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="customerOwnedIpEnabled")
    def customer_owned_ip_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @customer_owned_ip_enabled.setter
    def customer_owned_ip_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_insights_mode.setter
    def database_insights_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedLogVolume")
    def dedicated_log_volume(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_log_volume.setter
    def dedicated_log_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="domainAuthSecretArn")
    def domain_auth_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_auth_secret_arn.setter
    def domain_auth_secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainDnsIps")
    def domain_dns_ips(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domain_dns_ips.setter
    def domain_dns_ips(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_fqdn.setter
    def domain_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_iam_role_name.setter
    def domain_iam_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainOu")
    def domain_ou(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_ou.setter
    def domain_ou(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_lifecycle_support.setter
    def engine_lifecycle_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="latestRestorableTime")
    def latest_restorable_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_restorable_time.setter
    def latest_restorable_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="listenerEndpoints")
    def listener_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceListenerEndpointArgs]]]
    ]: ...
    @listener_endpoints.setter
    def listener_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceListenerEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_user_password.setter
    def manage_master_user_password(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
        pulumi.Input[Sequence[pulumi.Input[InstanceMasterUserSecretArgs]]]
    ]: ...
    @master_user_secrets.setter
    def master_user_secrets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceMasterUserSecretArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAllocatedStorage")
    def max_allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_allocated_storage.setter
    def max_allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ncharCharacterSetName")
    def nchar_character_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nchar_character_set_name.setter
    def nchar_character_set_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @option_group_name.setter
    def option_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="replicaMode")
    def replica_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_mode.setter
    def replica_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replicas.setter
    def replicas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicateSourceDb")
    def replicate_source_db(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replicate_source_db.setter
    def replicate_source_db(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> Optional[pulumi.Input[InstanceRestoreToPointInTimeArgs]]: ...
    @restore_to_point_in_time.setter
    def restore_to_point_in_time(
        self, value: Optional[pulumi.Input[InstanceRestoreToPointInTimeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> Optional[pulumi.Input[InstanceS3ImportArgs]]: ...
    @s3_import.setter
    def s3_import(self, value: Optional[pulumi.Input[InstanceS3ImportArgs]]): ...
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
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageThroughput")
    def storage_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_throughput.setter
    def storage_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]: ...
    @storage_type.setter
    def storage_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]
    ): ...
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
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upgrade_rollout_order.setter
    def upgrade_rollout_order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeStorageConfig")
    def upgrade_storage_config(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @upgrade_storage_config.setter
    def upgrade_storage_config(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:rds/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_target: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        blue_green_update: Optional[
            pulumi.Input[
                Union[InstanceBlueGreenUpdateArgs, InstanceBlueGreenUpdateArgsDict]
            ]
        ] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_owned_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_log_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_auth_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_dns_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_ou: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_model: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        max_allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        nchar_character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        option_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        replicate_source_db: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[
                Union[
                    InstanceRestoreToPointInTimeArgs,
                    InstanceRestoreToPointInTimeArgsDict,
                ]
            ]
        ] = ...,
        s3_import: Optional[
            pulumi.Input[Union[InstanceS3ImportArgs, InstanceS3ImportArgsDict]]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_storage_config: Optional[pulumi.Input[_builtins.bool]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_target: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        blue_green_update: Optional[
            pulumi.Input[
                Union[InstanceBlueGreenUpdateArgs, InstanceBlueGreenUpdateArgsDict]
            ]
        ] = ...,
        ca_cert_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_owned_ip_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_insights_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_log_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_automated_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_auth_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_dns_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_iam_role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_ou: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_cloudwatch_logs_exports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_lifecycle_support: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_database_authentication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        identifier_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_class: Optional[
            pulumi.Input[Union[_builtins.str, InstanceType]]
        ] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_restorable_time: Optional[pulumi.Input[_builtins.str]] = ...,
        license_model: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceListenerEndpointArgs,
                            InstanceListenerEndpointArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_user_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_user_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_user_secrets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceMasterUserSecretArgs,
                            InstanceMasterUserSecretArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        max_allocated_storage: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        monitoring_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        nchar_character_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        option_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        performance_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_insights_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        performance_insights_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        replicate_source_db: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_to_point_in_time: Optional[
            pulumi.Input[
                Union[
                    InstanceRestoreToPointInTimeArgs,
                    InstanceRestoreToPointInTimeArgsDict,
                ]
            ]
        ] = ...,
        s3_import: Optional[
            pulumi.Input[Union[InstanceS3ImportArgs, InstanceS3ImportArgsDict]]
        ] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_rollout_order: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_storage_config: Optional[pulumi.Input[_builtins.bool]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Output[_builtins.str]: ...
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
    def apply_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="backupTarget")
    def backup_target(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenUpdate")
    def blue_green_update(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceBlueGreenUpdate]]: ...
    @_builtins.property
    @pulumi.getter(name="caCertIdentifier")
    def ca_cert_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="characterSetName")
    def character_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="customIamInstanceProfile")
    def custom_iam_instance_profile(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpEnabled")
    def customer_owned_ip_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedLogVolume")
    def dedicated_log_volume(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    @pulumi.getter(name="domainAuthSecretArn")
    def domain_auth_secret_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainDnsIps")
    def domain_dns_ips(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainOu")
    def domain_ou(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    @pulumi.getter
    def iops(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestRestorableTime")
    def latest_restorable_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="listenerEndpoints")
    def listener_endpoints(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceListenerEndpoint]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecretKmsKeyId")
    def master_user_secret_kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceMasterUserSecret]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAllocatedStorage")
    def max_allocated_storage(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ncharCharacterSetName")
    def nchar_character_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
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
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaMode")
    def replica_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicateSourceDb")
    def replicate_source_db(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceRestoreToPointInTime]]: ...
    @_builtins.property
    @pulumi.getter(name="s3Import")
    def s3_import(self) -> pulumi.Output[Optional[outputs.InstanceS3Import]]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="storageThroughput")
    def storage_throughput(self) -> pulumi.Output[_builtins.int]: ...
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
    @pulumi.getter
    def timezone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeStorageConfig")
    def upgrade_storage_config(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
