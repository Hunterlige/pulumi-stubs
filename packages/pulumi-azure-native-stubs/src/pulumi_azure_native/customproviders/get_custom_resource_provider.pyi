import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomResourceProviderResult",
    "AwaitableGetCustomResourceProviderResult",
    "get_custom_resource_provider",
    "get_custom_resource_provider_output",
]

@pulumi.output_type
class GetCustomResourceProviderResult:
    def __init__(
        __self__,
        actions=...,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        resource_types=...,
        tags=...,
        type=...,
        validations=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[Sequence[outputs.CustomRPActionRouteDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[Sequence[outputs.CustomRPResourceTypeRouteDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Optional[Sequence[outputs.CustomRPValidationsResponse]]: ...

class AwaitableGetCustomResourceProviderResult(GetCustomResourceProviderResult):
    def __await__(self): ...

def get_custom_resource_provider(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_provider_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCustomResourceProviderResult: ...
def get_custom_resource_provider_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomResourceProviderResult]: ...
