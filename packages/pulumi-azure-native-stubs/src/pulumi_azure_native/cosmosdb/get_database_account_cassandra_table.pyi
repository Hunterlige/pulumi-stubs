

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseAccountCassandraTableResult', 'AwaitableGetDatabaseAccountCassandraTableResult', 'get_database_account_cassandra_table', 'get_database_account_cassandra_table_output']
@pulumi.output_type
class GetDatabaseAccountCassandraTableResult:
    
    def __init__(__self__, azure_api_version=..., default_ttl=..., id=..., location=..., name=..., schema=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
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
    def schema(self) -> Optional[outputs.CassandraSchemaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDatabaseAccountCassandraTableResult(GetDatabaseAccountCassandraTableResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseAccountCassandraTableResult]:
        ...
    


def get_database_account_cassandra_table(account_name: Optional[_builtins.str] = ..., keyspace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., table_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseAccountCassandraTableResult:
    
    ...

def get_database_account_cassandra_table_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., keyspace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseAccountCassandraTableResult]:
    
    ...

