

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagementLockAtResourceGroupLevelResult', ..., 'get_management_lock_at_resource_group_level', 'get_management_lock_at_resource_group_level_output']
@pulumi.output_type
class GetManagementLockAtResourceGroupLevelResult:
    
    def __init__(__self__, azure_api_version=..., id=..., level=..., name=..., notes=..., owners=..., system_data=..., type=...) -> None:
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
    def level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[Sequence[outputs.ManagementLockOwnerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagementLockAtResourceGroupLevelResult(GetManagementLockAtResourceGroupLevelResult):
    def __await__(self): # -> Generator[Never, Any, GetManagementLockAtResourceGroupLevelResult]:
        ...
    


def get_management_lock_at_resource_group_level(lock_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagementLockAtResourceGroupLevelResult:
    
    ...

def get_management_lock_at_resource_group_level_output(lock_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagementLockAtResourceGroupLevelResult]:
    
    ...

