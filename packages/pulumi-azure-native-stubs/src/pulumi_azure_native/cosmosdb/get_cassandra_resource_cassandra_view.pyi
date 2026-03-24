

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCassandraResourceCassandraViewResult', 'AwaitableGetCassandraResourceCassandraViewResult', 'get_cassandra_resource_cassandra_view', 'get_cassandra_resource_cassandra_view_output']
@pulumi.output_type
class GetCassandraResourceCassandraViewResult:
    
    def __init__(__self__, azure_api_version=..., id=..., identity=..., location=..., name=..., options=..., resource=..., tags=..., type=...) -> None:
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
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
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
    def options(self) -> Optional[outputs.CassandraViewGetPropertiesResponseOptions]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.CassandraViewGetPropertiesResponseResource]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCassandraResourceCassandraViewResult(GetCassandraResourceCassandraViewResult):
    def __await__(self): # -> Generator[Never, Any, GetCassandraResourceCassandraViewResult]:
        ...
    


def get_cassandra_resource_cassandra_view(account_name: Optional[_builtins.str] = ..., keyspace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., view_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCassandraResourceCassandraViewResult:
    
    ...

def get_cassandra_resource_cassandra_view_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., keyspace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., view_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCassandraResourceCassandraViewResult]:
    
    ...

