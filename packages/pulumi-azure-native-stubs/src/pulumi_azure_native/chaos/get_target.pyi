import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTargetResult",
    "AwaitableGetTargetResult",
    "get_target",
    "get_target_output",
]

@pulumi.output_type
class GetTargetResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
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
    def location(self) -> Optional[_builtins.str]: ...
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

class AwaitableGetTargetResult(GetTargetResult):
    def __await__(self): ...

def get_target(
    parent_provider_namespace: Optional[_builtins.str] = ...,
    parent_resource_name: Optional[_builtins.str] = ...,
    parent_resource_type: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    target_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTargetResult: ...
def get_target_output(
    parent_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    target_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTargetResult]: ...
