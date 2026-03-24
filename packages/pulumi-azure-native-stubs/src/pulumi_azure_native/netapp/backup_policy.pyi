

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupPolicyArgs', 'BackupPolicy']
@pulumi.input_type
class BackupPolicyArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], backup_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., daily_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., monthly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., weekly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicyName")
    def backup_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_policy_name.setter
    def backup_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyBackupsToKeep")
    def daily_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @daily_backups_to_keep.setter
    def daily_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBackupsToKeep")
    def monthly_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @monthly_backups_to_keep.setter
    def monthly_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyBackupsToKeep")
    def weekly_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weekly_backups_to_keep.setter
    def weekly_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:netapp:BackupPolicy")
class BackupPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., daily_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., monthly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., weekly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BackupPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BackupPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicyId")
    def backup_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyBackupsToKeep")
    def daily_backups_to_keep(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBackupsToKeep")
    def monthly_backups_to_keep(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeBackups")
    def volume_backups(self) -> pulumi.Output[Sequence[outputs.VolumeBackupsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumesAssigned")
    def volumes_assigned(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyBackupsToKeep")
    def weekly_backups_to_keep(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


