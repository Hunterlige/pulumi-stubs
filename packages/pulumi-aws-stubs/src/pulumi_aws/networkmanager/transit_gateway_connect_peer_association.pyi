import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "TransitGatewayConnectPeerAssociationArgs",
    "TransitGatewayConnectPeerAssociation",
]

@pulumi.input_type
class TransitGatewayConnectPeerAssociationArgs:
    def __init__(
        __self__,
        *,
        device_id: pulumi.Input[_builtins.str],
        global_network_id: pulumi.Input[_builtins.str],
        transit_gateway_connect_peer_arn: pulumi.Input[_builtins.str],
        link_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[_builtins.str]: ...
    @device_id.setter
    def device_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayConnectPeerArn")
    def transit_gateway_connect_peer_arn(self) -> pulumi.Input[_builtins.str]: ...
    @transit_gateway_connect_peer_arn.setter
    def transit_gateway_connect_peer_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TransitGatewayConnectPeerAssociationState:
    def __init__(
        __self__,
        *,
        device_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_connect_peer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayConnectPeerArn")
    def transit_gateway_connect_peer_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_connect_peer_arn.setter
    def transit_gateway_connect_peer_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class TransitGatewayConnectPeerAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_connect_peer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TransitGatewayConnectPeerAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_connect_peer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TransitGatewayConnectPeerAssociation: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayConnectPeerArn")
    def transit_gateway_connect_peer_arn(self) -> pulumi.Output[_builtins.str]: ...
