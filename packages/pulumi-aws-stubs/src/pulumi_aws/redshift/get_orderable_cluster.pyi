import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrderableClusterResult",
    "AwaitableGetOrderableClusterResult",
    "get_orderable_cluster",
    "get_orderable_cluster_output",
]

@pulumi.output_type
class GetOrderableClusterResult:
    def __init__(
        __self__,
        availability_zones=...,
        cluster_type=...,
        cluster_version=...,
        id=...,
        node_type=...,
        preferred_node_types=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredNodeTypes")
    def preferred_node_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetOrderableClusterResult(GetOrderableClusterResult):
    def __await__(self): ...

def get_orderable_cluster(
    cluster_type: Optional[_builtins.str] = ...,
    cluster_version: Optional[_builtins.str] = ...,
    node_type: Optional[_builtins.str] = ...,
    preferred_node_types: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrderableClusterResult: ...
def get_orderable_cluster_output(
    cluster_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    cluster_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    node_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    preferred_node_types: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrderableClusterResult]: ...
