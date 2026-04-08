import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppPrivateEndpointConnectionSlotResult",
    ...,
    "get_web_app_private_endpoint_connection_slot",
    ...,
]

@pulumi.output_type
class GetWebAppPrivateEndpointConnectionSlotResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        ip_addresses=...,
        kind=...,
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
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.ArmIdWrapperResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkConnectionStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAppPrivateEndpointConnectionSlotResult(
    GetWebAppPrivateEndpointConnectionSlotResult
):
    def __await__(self): ...

def get_web_app_private_endpoint_connection_slot(
    name: Optional[_builtins.str] = ...,
    private_endpoint_connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    slot: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppPrivateEndpointConnectionSlotResult: ...
def get_web_app_private_endpoint_connection_slot_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    slot: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppPrivateEndpointConnectionSlotResult]: ...
