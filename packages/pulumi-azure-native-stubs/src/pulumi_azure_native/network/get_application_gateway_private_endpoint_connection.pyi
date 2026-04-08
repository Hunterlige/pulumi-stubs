import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetApplicationGatewayPrivateEndpointConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        link_identifier=...,
        name=...,
        private_endpoint=...,
        private_link_service_connection_state=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetApplicationGatewayPrivateEndpointConnectionResult(
    GetApplicationGatewayPrivateEndpointConnectionResult
):
    def __await__(self): ...

def get_application_gateway_private_endpoint_connection(
    application_gateway_name: Optional[_builtins.str] = ...,
    connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationGatewayPrivateEndpointConnectionResult: ...
def get_application_gateway_private_endpoint_connection_output(
    application_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationGatewayPrivateEndpointConnectionResult]: ...
