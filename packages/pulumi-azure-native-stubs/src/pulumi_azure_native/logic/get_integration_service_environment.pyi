import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIntegrationServiceEnvironmentResult",
    "AwaitableGetIntegrationServiceEnvironmentResult",
    "get_integration_service_environment",
    "get_integration_service_environment_output",
]

@pulumi.output_type
class GetIntegrationServiceEnvironmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        properties=...,
        sku=...,
        tags=...,
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
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.IntegrationServiceEnvironmentPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.IntegrationServiceEnvironmentSkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIntegrationServiceEnvironmentResult(
    GetIntegrationServiceEnvironmentResult
):
    def __await__(self): ...

def get_integration_service_environment(
    integration_service_environment_name: Optional[_builtins.str] = ...,
    resource_group: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIntegrationServiceEnvironmentResult: ...
def get_integration_service_environment_output(
    integration_service_environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIntegrationServiceEnvironmentResult]: ...
