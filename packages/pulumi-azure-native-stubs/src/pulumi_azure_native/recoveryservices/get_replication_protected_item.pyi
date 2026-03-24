

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationProtectedItemResult', 'AwaitableGetReplicationProtectedItemResult', 'get_replication_protected_item', 'get_replication_protected_item_output']
@pulumi.output_type
class GetReplicationProtectedItemResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ReplicationProtectedItemPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReplicationProtectedItemResult(GetReplicationProtectedItemResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationProtectedItemResult]:
        ...
    


def get_replication_protected_item(fabric_name: Optional[_builtins.str] = ..., protection_container_name: Optional[_builtins.str] = ..., replicated_protected_item_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationProtectedItemResult:
    
    ...

def get_replication_protected_item_output(fabric_name: Optional[pulumi.Input[_builtins.str]] = ..., protection_container_name: Optional[pulumi.Input[_builtins.str]] = ..., replicated_protected_item_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationProtectedItemResult]:
    
    ...

