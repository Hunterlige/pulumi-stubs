

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClustersResult', 'AwaitableGetClustersResult', 'get_clusters', 'get_clusters_output']
@pulumi.output_type
class GetClustersResult:
    
    def __init__(__self__, cluster_arns=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterArns")
    def cluster_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetClustersResult(GetClustersResult):
    def __await__(self): # -> Generator[Never, Any, GetClustersResult]:
        ...
    


def get_clusters(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClustersResult:
    
    ...

def get_clusters_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClustersResult]:
    
    ...

