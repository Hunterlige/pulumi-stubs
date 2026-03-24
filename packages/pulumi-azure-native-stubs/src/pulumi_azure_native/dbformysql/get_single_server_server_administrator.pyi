

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSingleServerServerAdministratorResult', 'AwaitableGetSingleServerServerAdministratorResult', 'get_single_server_server_administrator', 'get_single_server_server_administrator_output']
@pulumi.output_type
class GetSingleServerServerAdministratorResult:
    
    def __init__(__self__, administrator_type=..., azure_api_version=..., id=..., login=..., name=..., sid=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> _builtins.str:
        
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
    def login(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSingleServerServerAdministratorResult(GetSingleServerServerAdministratorResult):
    def __await__(self): # -> Generator[Never, Any, GetSingleServerServerAdministratorResult]:
        ...
    


def get_single_server_server_administrator(resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSingleServerServerAdministratorResult:
    
    ...

def get_single_server_server_administrator_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSingleServerServerAdministratorResult]:
    
    ...

