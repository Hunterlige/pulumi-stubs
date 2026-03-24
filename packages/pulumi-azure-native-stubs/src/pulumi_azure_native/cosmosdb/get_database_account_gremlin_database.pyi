

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseAccountGremlinDatabaseResult', 'AwaitableGetDatabaseAccountGremlinDatabaseResult', 'get_database_account_gremlin_database', 'get_database_account_gremlin_database_output']
@pulumi.output_type
class GetDatabaseAccountGremlinDatabaseResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., rid=..., tags=..., ts=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDatabaseAccountGremlinDatabaseResult(GetDatabaseAccountGremlinDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseAccountGremlinDatabaseResult]:
        ...
    


def get_database_account_gremlin_database(account_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseAccountGremlinDatabaseResult:
    
    ...

def get_database_account_gremlin_database_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseAccountGremlinDatabaseResult]:
    
    ...

