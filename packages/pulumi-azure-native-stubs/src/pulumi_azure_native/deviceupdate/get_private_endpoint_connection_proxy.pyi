import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateEndpointConnectionProxyResult",
    "AwaitableGetPrivateEndpointConnectionProxyResult",
    "get_private_endpoint_connection_proxy",
    "get_private_endpoint_connection_proxy_output",
]

@pulumi.output_type
class GetPrivateEndpointConnectionProxyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        name=...,
        provisioning_state=...,
        remote_private_endpoint=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remotePrivateEndpoint")
    def remote_private_endpoint(
        self,
    ) -> Optional[outputs.RemotePrivateEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPrivateEndpointConnectionProxyResult(
    GetPrivateEndpointConnectionProxyResult
):
    def __await__(self): ...

def get_private_endpoint_connection_proxy(
    account_name: Optional[_builtins.str] = ...,
    private_endpoint_connection_proxy_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateEndpointConnectionProxyResult: ...
def get_private_endpoint_connection_proxy_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_endpoint_connection_proxy_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateEndpointConnectionProxyResult]: ...
