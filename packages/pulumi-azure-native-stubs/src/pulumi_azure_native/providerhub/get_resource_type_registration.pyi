import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResourceTypeRegistrationResult",
    "AwaitableGetResourceTypeRegistrationResult",
    "get_resource_type_registration",
    "get_resource_type_registration_output",
]

@pulumi.output_type
class GetResourceTypeRegistrationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        kind=...,
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
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ResourceTypeRegistrationPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetResourceTypeRegistrationResult(GetResourceTypeRegistrationResult):
    def __await__(self): ...

def get_resource_type_registration(
    provider_namespace: Optional[_builtins.str] = ...,
    resource_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResourceTypeRegistrationResult: ...
def get_resource_type_registration_output(
    provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResourceTypeRegistrationResult]: ...
