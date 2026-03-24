

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudVmClustersResult', 'AwaitableGetCloudVmClustersResult', 'get_cloud_vm_clusters', 'get_cloud_vm_clusters_output']
@pulumi.output_type
class GetCloudVmClustersResult:
    
    def __init__(__self__, cloud_vm_clusters=..., id=..., location=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudVmClusters")
    def cloud_vm_clusters(self) -> Sequence[outputs.GetCloudVmClustersCloudVmClusterResult]:
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
    


class AwaitableGetCloudVmClustersResult(GetCloudVmClustersResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudVmClustersResult]:
        ...
    


def get_cloud_vm_clusters(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudVmClustersResult:
    
    ...

def get_cloud_vm_clusters_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudVmClustersResult]:
    
    ...

