

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupPolicyArgs', 'BackupPolicy']
@pulumi.input_type
class BackupPolicyArgs:
    def __init__(__self__, *, backup_policy: pulumi.Input[BackupPolicyBackupPolicyArgs], file_system_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> pulumi.Input[BackupPolicyBackupPolicyArgs]:
        
        ...
    
    @backup_policy.setter
    def backup_policy(self, value: pulumi.Input[BackupPolicyBackupPolicyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BackupPolicyState:
    def __init__(__self__, *, backup_policy: Optional[pulumi.Input[BackupPolicyBackupPolicyArgs]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> Optional[pulumi.Input[BackupPolicyBackupPolicyArgs]]:
        
        ...
    
    @backup_policy.setter
    def backup_policy(self, value: Optional[pulumi.Input[BackupPolicyBackupPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:efs/backupPolicy:BackupPolicy")
class BackupPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_policy: Optional[pulumi.Input[Union[BackupPolicyBackupPolicyArgs, BackupPolicyBackupPolicyArgsDict]]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BackupPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_policy: Optional[pulumi.Input[Union[BackupPolicyBackupPolicyArgs, BackupPolicyBackupPolicyArgsDict]]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BackupPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> pulumi.Output[outputs.BackupPolicyBackupPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


