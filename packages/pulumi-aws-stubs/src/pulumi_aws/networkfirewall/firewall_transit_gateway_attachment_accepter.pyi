import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FirewallTransitGatewayAttachmentAccepterArgs",
    "FirewallTransitGatewayAttachmentAccepter",
]

@pulumi.input_type
class FirewallTransitGatewayAttachmentAccepterArgs:
    def __init__(
        __self__,
        *,
        transit_gateway_attachment_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[_builtins.str]: ...
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[
        pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
    ]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
        ],
    ): ...

@pulumi.input_type
class _FirewallTransitGatewayAttachmentAccepterState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
        ] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[
        pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
    ]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[FirewallTransitGatewayAttachmentAccepterTimeoutsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class FirewallTransitGatewayAttachmentAccepter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    FirewallTransitGatewayAttachmentAccepterTimeoutsArgs,
                    FirewallTransitGatewayAttachmentAccepterTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FirewallTransitGatewayAttachmentAccepterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    FirewallTransitGatewayAttachmentAccepterTimeoutsArgs,
                    FirewallTransitGatewayAttachmentAccepterTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FirewallTransitGatewayAttachmentAccepter: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FirewallTransitGatewayAttachmentAccepterTimeouts]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[_builtins.str]: ...
