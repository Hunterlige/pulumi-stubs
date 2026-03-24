import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WindowsFileSystemArgs", "WindowsFileSystem"]

@pulumi.input_type
class WindowsFileSystemArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        throughput_capacity: pulumi.Input[_builtins.int],
        active_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        audit_log_configuration: Optional[
            pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]
        ] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]
        ] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_managed_active_directory: Optional[
            pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @throughput_capacity.setter
    def throughput_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aliases.setter
    def aliases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfiguration")
    def audit_log_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]]: ...
    @audit_log_configuration.setter
    def audit_log_configuration(
        self, value: Optional[pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]]
    ): ...
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
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]]: ...
    @disk_iops_configuration.setter
    def disk_iops_configuration(
        self, value: Optional[pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]]
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
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="selfManagedActiveDirectory")
    def self_managed_active_directory(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]]: ...
    @self_managed_active_directory.setter
    def self_managed_active_directory(
        self,
        value: Optional[pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]],
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
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _WindowsFileSystemState:
    def __init__(
        __self__,
        *,
        active_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_log_configuration: Optional[
            pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]
        ] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]
        ] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_file_server_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_administration_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_managed_active_directory: Optional[
            pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aliases.setter
    def aliases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfiguration")
    def audit_log_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]]: ...
    @audit_log_configuration.setter
    def audit_log_configuration(
        self, value: Optional[pulumi.Input[WindowsFileSystemAuditLogConfigurationArgs]]
    ): ...
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
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]]: ...
    @disk_iops_configuration.setter
    def disk_iops_configuration(
        self, value: Optional[pulumi.Input[WindowsFileSystemDiskIopsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="preferredFileServerIp")
    def preferred_file_server_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_file_server_ip.setter
    def preferred_file_server_ip(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_subnet_id.setter
    def preferred_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteAdministrationEndpoint")
    def remote_administration_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_administration_endpoint.setter
    def remote_administration_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="selfManagedActiveDirectory")
    def self_managed_active_directory(
        self,
    ) -> Optional[pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]]: ...
    @self_managed_active_directory.setter
    def self_managed_active_directory(
        self,
        value: Optional[pulumi.Input[WindowsFileSystemSelfManagedActiveDirectoryArgs]],
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
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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

@pulumi.type_token("aws:fsx/windowsFileSystem:WindowsFileSystem")
class WindowsFileSystem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        audit_log_configuration: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemAuditLogConfigurationArgs,
                    WindowsFileSystemAuditLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemDiskIopsConfigurationArgs,
                    WindowsFileSystemDiskIopsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_managed_active_directory: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemSelfManagedActiveDirectoryArgs,
                    WindowsFileSystemSelfManagedActiveDirectoryArgsDict,
                ]
            ]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WindowsFileSystemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_log_configuration: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemAuditLogConfigurationArgs,
                    WindowsFileSystemAuditLogConfigurationArgsDict,
                ]
            ]
        ] = ...,
        automatic_backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags_to_backups: Optional[pulumi.Input[_builtins.bool]] = ...,
        daily_automatic_backup_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_configuration: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemDiskIopsConfigurationArgs,
                    WindowsFileSystemDiskIopsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        final_backup_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_file_server_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_administration_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_managed_active_directory: Optional[
            pulumi.Input[
                Union[
                    WindowsFileSystemSelfManagedActiveDirectoryArgs,
                    WindowsFileSystemSelfManagedActiveDirectoryArgsDict,
                ]
            ]
        ] = ...,
        skip_final_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        throughput_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WindowsFileSystem: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfiguration")
    def audit_log_configuration(
        self,
    ) -> pulumi.Output[outputs.WindowsFileSystemAuditLogConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
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
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> pulumi.Output[outputs.WindowsFileSystemDiskIopsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalBackupTags")
    def final_backup_tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredFileServerIp")
    def preferred_file_server_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteAdministrationEndpoint")
    def remote_administration_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="selfManagedActiveDirectory")
    def self_managed_active_directory(
        self,
    ) -> pulumi.Output[
        Optional[outputs.WindowsFileSystemSelfManagedActiveDirectory]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> pulumi.Output[_builtins.str]: ...
