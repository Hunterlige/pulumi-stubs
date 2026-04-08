import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualRouterPeeringResult",
    "AwaitableGetVirtualRouterPeeringResult",
    "get_virtual_router_peering",
    "get_virtual_router_peering_output",
]

@pulumi.output_type
class GetVirtualRouterPeeringResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        peer_asn=...,
        peer_ip=...,
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
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualRouterPeeringResult(GetVirtualRouterPeeringResult):
    def __await__(self): ...

def get_virtual_router_peering(
    peering_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_router_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualRouterPeeringResult: ...
def get_virtual_router_peering_output(
    peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_router_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualRouterPeeringResult]: ...
