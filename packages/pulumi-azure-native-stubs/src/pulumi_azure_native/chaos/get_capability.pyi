import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCapabilityResult",
    "AwaitableGetCapabilityResult",
    "get_capability",
    "get_capability_output",
]

@pulumi.output_type
class GetCapabilityResult:
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
    def properties(self) -> outputs.CapabilityPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCapabilityResult(GetCapabilityResult):
    def __await__(self): ...

def get_capability(
    capability_name: Optional[_builtins.str] = ...,
    parent_provider_namespace: Optional[_builtins.str] = ...,
    parent_resource_name: Optional[_builtins.str] = ...,
    parent_resource_type: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    target_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCapabilityResult: ...
def get_capability_output(
    capability_name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    target_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCapabilityResult]: ...
