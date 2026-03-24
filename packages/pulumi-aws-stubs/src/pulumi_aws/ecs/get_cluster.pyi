import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
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
        arn=...,
        cluster_name=...,
        id=...,
        pending_tasks_count=...,
        region=...,
        registered_container_instances_count=...,
        running_tasks_count=...,
        service_connect_defaults=...,
        settings=...,
        status=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pendingTasksCount")
    def pending_tasks_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registeredContainerInstancesCount")
    def registered_container_instances_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="runningTasksCount")
    def running_tasks_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(
        self,
    ) -> Sequence[outputs.GetClusterServiceConnectDefaultResult]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Sequence[outputs.GetClusterSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): ...

def get_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterResult: ...
def get_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterResult]: ...
