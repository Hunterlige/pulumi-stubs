import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalGatewayVirtualInterfaceResult",
    "AwaitableGetLocalGatewayVirtualInterfaceResult",
    "get_local_gateway_virtual_interface",
    "get_local_gateway_virtual_interface_output",
]

@pulumi.output_type
class GetLocalGatewayVirtualInterfaceResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        local_address=...,
        local_bgp_asn=...,
        local_gateway_id=...,
        local_gateway_virtual_interface_ids=...,
        peer_address=...,
        peer_bgp_asn=...,
        region=...,
        tags=...,
        vlan=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetLocalGatewayVirtualInterfaceFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAddress")
    def local_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localBgpAsn")
    def local_bgp_asn(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceIds")
    def local_gateway_virtual_interface_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerBgpAsn")
    def peer_bgp_asn(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> _builtins.int: ...

class AwaitableGetLocalGatewayVirtualInterfaceResult(
    GetLocalGatewayVirtualInterfaceResult
):
    def __await__(self): ...

def get_local_gateway_virtual_interface(
    filters: Optional[
        Sequence[
            Union[
                GetLocalGatewayVirtualInterfaceFilterArgs,
                GetLocalGatewayVirtualInterfaceFilterArgsDict,
            ]
        ]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalGatewayVirtualInterfaceResult: ...
def get_local_gateway_virtual_interface_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetLocalGatewayVirtualInterfaceFilterArgs,
                        GetLocalGatewayVirtualInterfaceFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalGatewayVirtualInterfaceResult]: ...
