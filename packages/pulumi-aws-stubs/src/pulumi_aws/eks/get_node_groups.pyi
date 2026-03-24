

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNodeGroupsResult', 'AwaitableGetNodeGroupsResult', 'get_node_groups', 'get_node_groups_output']
@pulumi.output_type
class GetNodeGroupsResult:
    
    def __init__(__self__, cluster_name=..., id=..., names=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetNodeGroupsResult(GetNodeGroupsResult):
    def __await__(self): # -> Generator[Never, Any, GetNodeGroupsResult]:
        ...
    


def get_node_groups(cluster_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNodeGroupsResult:
    
    ...

def get_node_groups_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNodeGroupsResult]:
    
    ...

