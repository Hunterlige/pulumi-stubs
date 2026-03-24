

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGeoBackupPolicyResult', 'AwaitableGetGeoBackupPolicyResult', 'get_geo_backup_policy', 'get_geo_backup_policy_output']
@pulumi.output_type
class GetGeoBackupPolicyResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., location=..., name=..., state=..., storage_type=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGeoBackupPolicyResult(GetGeoBackupPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetGeoBackupPolicyResult]:
        ...
    


def get_geo_backup_policy(database_name: Optional[_builtins.str] = ..., geo_backup_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGeoBackupPolicyResult:
    
    ...

def get_geo_backup_policy_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., geo_backup_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGeoBackupPolicyResult]:
    
    ...

