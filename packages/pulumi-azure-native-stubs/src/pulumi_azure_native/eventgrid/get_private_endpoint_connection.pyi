import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrivateEndpointConnectionResult",
    "AwaitableGetPrivateEndpointConnectionResult",
    "get_private_endpoint_connection",
    "get_private_endpoint_connection_output",
]

@pulumi.output_type
class GetPrivateEndpointConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        group_ids=...,
        id=...,
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
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.ConnectionStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPrivateEndpointConnectionResult(GetPrivateEndpointConnectionResult):
    def __await__(self): ...

def get_private_endpoint_connection(
    parent_name: Optional[_builtins.str] = ...,
    parent_type: Optional[_builtins.str] = ...,
    private_endpoint_connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrivateEndpointConnectionResult: ...
def get_private_endpoint_connection_output(
    parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
    private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrivateEndpointConnectionResult]: ...
