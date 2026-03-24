

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListClusterZonesResult', 'AwaitableListClusterZonesResult', 'list_cluster_zones', 'list_cluster_zones_output']
@pulumi.output_type
class ListClusterZonesResult:
    
    def __init__(__self__, zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[outputs.ClusterZoneResponse]]:
        
        ...
    


class AwaitableListClusterZonesResult(ListClusterZonesResult):
    def __await__(self): # -> Generator[Never, Any, ListClusterZonesResult]:
        ...
    


def list_cluster_zones(cluster_name: Optional[_builtins.str] = ..., private_cloud_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListClusterZonesResult:
    
    ...

def list_cluster_zones_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListClusterZonesResult]:
    
    ...

