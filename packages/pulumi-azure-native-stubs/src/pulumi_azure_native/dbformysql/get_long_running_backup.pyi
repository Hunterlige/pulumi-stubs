

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLongRunningBackupResult', 'AwaitableGetLongRunningBackupResult', 'get_long_running_backup', 'get_long_running_backup_output']
@pulumi.output_type
class GetLongRunningBackupResult:
    
    def __init__(__self__, azure_api_version=..., backup_name_v2=..., backup_type=..., completed_time=..., id=..., name=..., provisioning_state=..., source=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupNameV2")
    def backup_name_v2(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="completedTime")
    def completed_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLongRunningBackupResult(GetLongRunningBackupResult):
    def __await__(self): # -> Generator[Never, Any, GetLongRunningBackupResult]:
        ...
    


def get_long_running_backup(backup_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLongRunningBackupResult:
    
    ...

def get_long_running_backup_output(backup_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLongRunningBackupResult]:
    
    ...

