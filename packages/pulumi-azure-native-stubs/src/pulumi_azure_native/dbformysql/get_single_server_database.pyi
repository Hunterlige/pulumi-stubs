

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSingleServerDatabaseResult', 'AwaitableGetSingleServerDatabaseResult', 'get_single_server_database', 'get_single_server_database_output']
@pulumi.output_type
class GetSingleServerDatabaseResult:
    
    def __init__(__self__, azure_api_version=..., charset=..., collation=..., id=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def charset(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSingleServerDatabaseResult(GetSingleServerDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetSingleServerDatabaseResult]:
        ...
    


def get_single_server_database(database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSingleServerDatabaseResult:
    
    ...

def get_single_server_database_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSingleServerDatabaseResult]:
    
    ...

