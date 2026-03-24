import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectPeerArgs", "ConnectPeer"]

@pulumi.input_type
class ConnectPeerArgs:
    def __init__(
        __self__,
        *,
        inside_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        peer_address: pulumi.Input[_builtins.str],
        transit_gateway_attachment_id: pulumi.Input[_builtins.str],
        bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Input[_builtins.str]: ...
    @peer_address.setter
    def peer_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[_builtins.str]: ...
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_asn.setter
    def bgp_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAddress")
    def transit_gateway_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_address.setter
    def transit_gateway_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ConnectPeerState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_transit_gateway_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inside_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_address: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_asn.setter
    def bgp_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerAddress")
    def bgp_peer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_peer_address.setter
    def bgp_peer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpTransitGatewayAddresses")
    def bgp_transit_gateway_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @bgp_transit_gateway_addresses.setter
    def bgp_transit_gateway_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_address.setter
    def peer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAddress")
    def transit_gateway_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_address.setter
    def transit_gateway_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:ec2transitgateway/connectPeer:ConnectPeer")
class ConnectPeer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        inside_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_address: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectPeerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_transit_gateway_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inside_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_address: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConnectPeer: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerAddress")
    def bgp_peer_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpTransitGatewayAddresses")
    def bgp_transit_gateway_addresses(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAddress")
    def transit_gateway_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[_builtins.str]: ...
