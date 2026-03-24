import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppEngineServiceResult",
    "AwaitableGetAppEngineServiceResult",
    "get_app_engine_service",
    "get_app_engine_service_output",
]

@pulumi.output_type
class GetAppEngineServiceResult:
    def __init__(
        __self__,
        display_name=...,
        id=...,
        module_id=...,
        name=...,
        project=...,
        service_id=...,
        telemetries=...,
        user_labels=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="moduleId")
    def module_id(self) -> _builtins.str: ...
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
    @pulumi.getter
    def telemetries(self) -> Sequence[outputs.GetAppEngineServiceTelemetryResult]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetAppEngineServiceResult(GetAppEngineServiceResult):
    def __await__(self): ...

def get_app_engine_service(
    module_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppEngineServiceResult: ...
def get_app_engine_service_output(
    module_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppEngineServiceResult]: ...
