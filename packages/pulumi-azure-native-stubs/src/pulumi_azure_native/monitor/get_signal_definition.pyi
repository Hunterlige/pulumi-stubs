import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSignalDefinitionResult",
    "AwaitableGetSignalDefinitionResult",
    "get_signal_definition",
    "get_signal_definition_output",
]

@pulumi.output_type
class GetSignalDefinitionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSignalDefinitionResult(GetSignalDefinitionResult):
    def __await__(self): ...

def get_signal_definition(
    azure_monitor_workspace_name: Optional[_builtins.str] = ...,
    health_model_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    signal_definition_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSignalDefinitionResult: ...
def get_signal_definition_output(
    azure_monitor_workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    health_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    signal_definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSignalDefinitionResult]: ...
