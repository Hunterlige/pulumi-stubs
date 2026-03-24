

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseAccountGremlinGraphResult', 'AwaitableGetDatabaseAccountGremlinGraphResult', 'get_database_account_gremlin_graph', 'get_database_account_gremlin_graph_output']
@pulumi.output_type
class GetDatabaseAccountGremlinGraphResult:
    
    def __init__(__self__, azure_api_version=..., conflict_resolution_policy=..., default_ttl=..., etag=..., id=..., indexing_policy=..., location=..., name=..., partition_key=..., rid=..., tags=..., ts=..., type=..., unique_key_policy=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[outputs.ConflictResolutionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
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
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional[outputs.IndexingPolicyResponse]:
        
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
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[outputs.ContainerPartitionKeyResponse]:
        
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
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(self) -> Optional[outputs.UniqueKeyPolicyResponse]:
        
        ...
    


class AwaitableGetDatabaseAccountGremlinGraphResult(GetDatabaseAccountGremlinGraphResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseAccountGremlinGraphResult]:
        ...
    


def get_database_account_gremlin_graph(account_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., graph_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseAccountGremlinGraphResult:
    
    ...

def get_database_account_gremlin_graph_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., graph_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseAccountGremlinGraphResult]:
    
    ...

