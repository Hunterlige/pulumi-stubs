import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceEndpointPolicyDefinitionResult",
    "AwaitableGetServiceEndpointPolicyDefinitionResult",
    "get_service_endpoint_policy_definition",
    "get_service_endpoint_policy_definition_output",
]

@pulumi.output_type
class GetServiceEndpointPolicyDefinitionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        etag=...,
        id=...,
        name=...,
        provisioning_state=...,
        service=...,
        service_resources=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceResources")
    def service_resources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

class AwaitableGetServiceEndpointPolicyDefinitionResult(
    GetServiceEndpointPolicyDefinitionResult
):
    def __await__(self): ...

def get_service_endpoint_policy_definition(
    resource_group_name: Optional[_builtins.str] = ...,
    service_endpoint_policy_definition_name: Optional[_builtins.str] = ...,
    service_endpoint_policy_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceEndpointPolicyDefinitionResult: ...
def get_service_endpoint_policy_definition_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_endpoint_policy_definition_name: Optional[
        pulumi.Input[_builtins.str]
    ] = ...,
    service_endpoint_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceEndpointPolicyDefinitionResult]: ...
