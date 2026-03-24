

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagementGroupResult', 'AwaitableGetManagementGroupResult', 'get_management_group', 'get_management_group_output']
@pulumi.output_type
class GetManagementGroupResult:
    
    def __init__(__self__, azure_api_version=..., children=..., details=..., display_name=..., id=..., name=..., system_data=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def children(self) -> Optional[Sequence[outputs.ManagementGroupChildInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.ManagementGroupDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagementGroupResult(GetManagementGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetManagementGroupResult]:
        ...
    


def get_management_group(expand: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., group_id: Optional[_builtins.str] = ..., recurse: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagementGroupResult:
    
    ...

def get_management_group_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., group_id: Optional[pulumi.Input[_builtins.str]] = ..., recurse: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagementGroupResult]:
    
    ...

