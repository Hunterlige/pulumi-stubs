import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppConnectionResult",
    "AwaitableGetAppConnectionResult",
    "get_app_connection",
    "get_app_connection_output",
]

@pulumi.output_type
class GetAppConnectionResult:
    def __init__(
        __self__,
        application_endpoints=...,
        connectors=...,
        display_name=...,
        effective_labels=...,
        gateways=...,
        id=...,
        labels=...,
        name=...,
        project=...,
        pulumi_labels=...,
        region=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationEndpoints")
    def application_endpoints(
        self,
    ) -> Sequence[outputs.GetAppConnectionApplicationEndpointResult]: ...
    @_builtins.property
    @pulumi.getter
    def connectors(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def gateways(self) -> Sequence[outputs.GetAppConnectionGatewayResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAppConnectionResult(GetAppConnectionResult):
    def __await__(self): ...

def get_app_connection(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppConnectionResult: ...
def get_app_connection_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppConnectionResult]: ...
