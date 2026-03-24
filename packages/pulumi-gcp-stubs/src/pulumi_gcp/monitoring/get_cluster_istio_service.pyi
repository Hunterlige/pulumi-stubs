import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterIstioServiceResult",
    "AwaitableGetClusterIstioServiceResult",
    "get_cluster_istio_service",
    "get_cluster_istio_service_output",
]

@pulumi.output_type
class GetClusterIstioServiceResult:
    def __init__(
        __self__,
        cluster_name=...,
        display_name=...,
        id=...,
        location=...,
        name=...,
        project=...,
        service_id=...,
        service_name=...,
        service_namespace=...,
        telemetries=...,
        user_labels=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def telemetries(
        self,
    ) -> Sequence[outputs.GetClusterIstioServiceTelemetryResult]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetClusterIstioServiceResult(GetClusterIstioServiceResult):
    def __await__(self): ...

def get_cluster_istio_service(
    cluster_name: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    service_namespace: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterIstioServiceResult: ...
def get_cluster_istio_service_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterIstioServiceResult]: ...
