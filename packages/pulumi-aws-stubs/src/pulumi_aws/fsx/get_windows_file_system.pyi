

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWindowsFileSystemResult', 'AwaitableGetWindowsFileSystemResult', 'get_windows_file_system', 'get_windows_file_system_output']
@pulumi.output_type
class GetWindowsFileSystemResult:
    
    def __init__(__self__, active_directory_id=..., aliases=..., arn=..., audit_log_configurations=..., automatic_backup_retention_days=..., backup_id=..., copy_tags_to_backups=..., daily_automatic_backup_start_time=..., deployment_type=..., disk_iops_configurations=..., dns_name=..., id=..., kms_key_id=..., network_interface_ids=..., owner_id=..., preferred_file_server_ip=..., preferred_subnet_id=..., region=..., security_group_ids=..., skip_final_backup=..., storage_capacity=..., storage_type=..., subnet_ids=..., tags=..., throughput_capacity=..., vpc_id=..., weekly_maintenance_start_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLogConfigurations")
    def audit_log_configurations(self) -> Sequence[outputs.GetWindowsFileSystemAuditLogConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskIopsConfigurations")
    def disk_iops_configurations(self) -> Sequence[outputs.GetWindowsFileSystemDiskIopsConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredFileServerIp")
    def preferred_file_server_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredSubnetId")
    def preferred_subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipFinalBackup")
    def skip_final_backup(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWindowsFileSystemResult(GetWindowsFileSystemResult):
    def __await__(self): # -> Generator[Never, Any, GetWindowsFileSystemResult]:
        ...
    


def get_windows_file_system(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWindowsFileSystemResult:
    
    ...

def get_windows_file_system_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWindowsFileSystemResult]:
    
    ...

