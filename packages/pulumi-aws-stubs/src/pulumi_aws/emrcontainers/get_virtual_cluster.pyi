

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualClusterResult', 'AwaitableGetVirtualClusterResult', 'get_virtual_cluster', 'get_virtual_cluster_output']
@pulumi.output_type
class GetVirtualClusterResult:
    
    def __init__(__self__, arn=..., container_providers=..., created_at=..., id=..., name=..., region=..., state=..., tags=..., virtual_cluster_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerProviders")
    def container_providers(self) -> Sequence[outputs.GetVirtualClusterContainerProviderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
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
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualClusterId")
    def virtual_cluster_id(self) -> _builtins.str:
        ...
    


class AwaitableGetVirtualClusterResult(GetVirtualClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualClusterResult]:
        ...
    


def get_virtual_cluster(region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., virtual_cluster_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualClusterResult:
    
    ...

def get_virtual_cluster_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., virtual_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualClusterResult]:
    
    ...

