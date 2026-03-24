

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDbNodesResult', 'AwaitableGetDbNodesResult', 'get_db_nodes', 'get_db_nodes_output']
@pulumi.output_type
class GetDbNodesResult:
    
    def __init__(__self__, cloud_vm_cluster=..., db_nodes=..., id=..., location=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudVmCluster")
    def cloud_vm_cluster(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodes")
    def db_nodes(self) -> Sequence[outputs.GetDbNodesDbNodeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetDbNodesResult(GetDbNodesResult):
    def __await__(self): # -> Generator[Never, Any, GetDbNodesResult]:
        ...
    


def get_db_nodes(cloud_vm_cluster: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDbNodesResult:
    
    ...

def get_db_nodes_output(cloud_vm_cluster: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDbNodesResult]:
    
    ...

