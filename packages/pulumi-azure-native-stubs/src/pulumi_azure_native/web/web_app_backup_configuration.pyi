

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAppBackupConfigurationArgs', 'WebAppBackupConfiguration']
@pulumi.input_type
class WebAppBackupConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], storage_account_url: pulumi.Input[_builtins.str], backup_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_schedule: Optional[pulumi.Input[BackupScheduleArgs]] = ..., databases: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseBackupSettingArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_account_url.setter
    def storage_account_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_name.setter
    def backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> Optional[pulumi.Input[BackupScheduleArgs]]:
        
        ...
    
    @backup_schedule.setter
    def backup_schedule(self, value: Optional[pulumi.Input[BackupScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseBackupSettingArgs]]]]:
        
        ...
    
    @databases.setter
    def databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseBackupSettingArgs]]]]): # -> None:
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
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:WebAppBackupConfiguration")
class WebAppBackupConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_schedule: Optional[pulumi.Input[Union[BackupScheduleArgs, BackupScheduleArgsDict]]] = ..., databases: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatabaseBackupSettingArgs, DatabaseBackupSettingArgsDict]]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_url: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppBackupConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppBackupConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSchedule")
    def backup_schedule(self) -> pulumi.Output[Optional[outputs.BackupScheduleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> pulumi.Output[Optional[Sequence[outputs.DatabaseBackupSettingResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


