

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterVersionsResult', 'AwaitableGetClusterVersionsResult', 'get_cluster_versions', 'get_cluster_versions_output']
@pulumi.output_type
class GetClusterVersionsResult:
    
    def __init__(__self__, cluster_type=..., cluster_versions=..., cluster_versions_onlies=..., default_only=..., id=..., include_all=..., region=..., version_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersions")
    def cluster_versions(self) -> Sequence[outputs.GetClusterVersionsClusterVersionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersionsOnlies")
    def cluster_versions_onlies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOnly")
    def default_only(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeAll")
    def include_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetClusterVersionsResult(GetClusterVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterVersionsResult]:
        ...
    


def get_cluster_versions(cluster_type: Optional[_builtins.str] = ..., cluster_versions_onlies: Optional[Sequence[_builtins.str]] = ..., default_only: Optional[_builtins.bool] = ..., include_all: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., version_status: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterVersionsResult:
    
    ...

def get_cluster_versions_output(cluster_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., cluster_versions_onlies: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., default_only: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., include_all: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version_status: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterVersionsResult]:
    
    ...

