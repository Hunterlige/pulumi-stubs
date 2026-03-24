import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LustreFileSystemArgs", "LustreFileSystem"]

@pulumi.input_type
class LustreFileSystemArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[_builtins.str],
        auto_import_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        data_read_cache_configuration: Optional[
            pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        drive_cache_type: Optional[pulumi.Input[_builtins.str]] = ...,
        efa_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_type_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[LustreFileSystemLogConfigurationArgs]
        ] = ...,
        metadata_configuration: Optional[
            pulumi.Input[LustreFileSystemMetadataConfigurationArgs]
        ] = ...,
        per_unit_storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_squash_configuration: Optional[
            pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_import_policy.setter
    def auto_import_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataReadCacheConfiguration")
    def data_read_cache_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]]: ...
    @data_read_cache_configuration.setter
    def data_read_cache_configuration(
        self,
        value: Optional[pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="driveCacheType")
    def drive_cache_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drive_cache_type.setter
    def drive_cache_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="efaEnabled")
    def efa_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @efa_enabled.setter
    def efa_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exportPath")
    def export_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_path.setter
    def export_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemTypeVersion")
    def file_system_type_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_type_version.setter
    def file_system_type_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @final_backup_tags.setter
    def final_backup_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importPath")
    def import_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @import_path.setter
    def import_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @imported_file_chunk_size.setter
    def imported_file_chunk_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemLogConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemMetadataConfigurationArgs]]: ...
    @metadata_configuration.setter
    def metadata_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemMetadataConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootSquashConfiguration")
    def root_squash_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]]: ...
    @root_squash_configuration.setter
    def root_squash_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_backup.setter
    def skip_final_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _LustreFileSystemState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_import_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        data_read_cache_configuration: Optional[
            pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        drive_cache_type: Optional[pulumi.Input[_builtins.str]] = ...,
        efa_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_type_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[LustreFileSystemLogConfigurationArgs]
        ] = ...,
        metadata_configuration: Optional[
            pulumi.Input[LustreFileSystemMetadataConfigurationArgs]
        ] = ...,
        mount_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        per_unit_storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_squash_configuration: Optional[
            pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_import_policy.setter
    def auto_import_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags_to_backups.setter
    def copy_tags_to_backups(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataReadCacheConfiguration")
    def data_read_cache_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]]: ...
    @data_read_cache_configuration.setter
    def data_read_cache_configuration(
        self,
        value: Optional[pulumi.Input[LustreFileSystemDataReadCacheConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="driveCacheType")
    def drive_cache_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drive_cache_type.setter
    def drive_cache_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="efaEnabled")
    def efa_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @efa_enabled.setter
    def efa_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exportPath")
    def export_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_path.setter
    def export_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemTypeVersion")
    def file_system_type_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_type_version.setter
    def file_system_type_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @final_backup_tags.setter
    def final_backup_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importPath")
    def import_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @import_path.setter
    def import_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @imported_file_chunk_size.setter
    def imported_file_chunk_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemLogConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemMetadataConfigurationArgs]]: ...
    @metadata_configuration.setter
    def metadata_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemMetadataConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_name.setter
    def mount_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_interface_ids.setter
    def network_interface_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootSquashConfiguration")
    def root_squash_configuration(
        self,
    ) -> Optional[pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]]: ...
    @root_squash_configuration.setter
    def root_squash_configuration(
        self, value: Optional[pulumi.Input[LustreFileSystemRootSquashConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_backup.setter
    def skip_final_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_capacity.setter
    def storage_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:fsx/lustreFileSystem:LustreFileSystem")
class LustreFileSystem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_import_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        data_read_cache_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemDataReadCacheConfigurationArgs,
                    LustreFileSystemDataReadCacheConfigurationArgsDict,
                ]
            ]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        drive_cache_type: Optional[pulumi.Input[_builtins.str]] = ...,
        efa_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_type_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemLogConfigurationArgs,
                    LustreFileSystemLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        metadata_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemMetadataConfigurationArgs,
                    LustreFileSystemMetadataConfigurationArgsDict,
                ]
            ]
        ] = ...,
        per_unit_storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_squash_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemRootSquashConfigurationArgs,
                    LustreFileSystemRootSquashConfigurationArgsDict,
                ]
            ]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LustreFileSystemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_import_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        data_read_cache_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemDataReadCacheConfigurationArgs,
                    LustreFileSystemDataReadCacheConfigurationArgsDict,
                ]
            ]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        drive_cache_type: Optional[pulumi.Input[_builtins.str]] = ...,
        efa_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_type_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemLogConfigurationArgs,
                    LustreFileSystemLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        metadata_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemMetadataConfigurationArgs,
                    LustreFileSystemMetadataConfigurationArgsDict,
                ]
            ]
        ] = ...,
        mount_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        per_unit_storage_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_squash_configuration: Optional[
            pulumi.Input[
                Union[
                    LustreFileSystemRootSquashConfigurationArgs,
                    LustreFileSystemRootSquashConfigurationArgsDict,
                ]
            ]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LustreFileSystem: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataReadCacheConfiguration")
    def data_read_cache_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.LustreFileSystemDataReadCacheConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="driveCacheType")
    def drive_cache_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="efaEnabled")
    def efa_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exportPath")
    def export_path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemTypeVersion")
    def file_system_type_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="importPath")
    def import_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> pulumi.Output[outputs.LustreFileSystemLogConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> pulumi.Output[outputs.LustreFileSystemMetadataConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootSquashConfiguration")
    def root_squash_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.LustreFileSystemRootSquashConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> pulumi.Output[_builtins.str]: ...
