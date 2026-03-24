

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlServerResult', 'AwaitableGetSqlServerResult', 'get_sql_server', 'get_sql_server_output']
@pulumi.output_type
class GetSqlServerResult:
    
    def __init__(__self__, azure_api_version=..., cores=..., edition=..., id=..., name=..., property_bag=..., registration_id=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cores(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationID")
    def registration_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetSqlServerResult(GetSqlServerResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlServerResult]:
        ...
    


def get_sql_server(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sql_server_name: Optional[_builtins.str] = ..., sql_server_registration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlServerResult:
    
    ...

def get_sql_server_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_registration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlServerResult]:
    
    ...

