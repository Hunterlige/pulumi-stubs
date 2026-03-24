import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterResult",
    "AwaitableGetClusterResult",
    "get_cluster",
    "get_cluster_output",
]

@pulumi.output_type
class GetClusterResult:
    def __init__(
        __self__,
        autoscaling_settings=...,
        create_time=...,
        datastore_mount_configs=...,
        id=...,
        management=...,
        name=...,
        node_type_configs=...,
        parent=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(
        self,
    ) -> Sequence[outputs.GetClusterAutoscalingSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datastoreMountConfigs")
    def datastore_mount_configs(
        self,
    ) -> Sequence[outputs.GetClusterDatastoreMountConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Sequence[outputs.GetClusterNodeTypeConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
