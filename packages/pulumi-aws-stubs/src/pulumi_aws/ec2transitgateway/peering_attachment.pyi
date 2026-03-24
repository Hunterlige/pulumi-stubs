import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PeeringAttachmentArgs", "PeeringAttachment"]

@pulumi.input_type
class PeeringAttachmentArgs:
    def __init__(
        __self__,
        *,
        peer_region: pulumi.Input[_builtins.str],
        peer_transit_gateway_id: pulumi.Input[_builtins.str],
        transit_gateway_id: pulumi.Input[_builtins.str],
        options: Optional[pulumi.Input[PeeringAttachmentOptionsArgs]] = ...,
        peer_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Input[_builtins.str]: ...
    @peer_region.setter
    def peer_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @peer_transit_gateway_id.setter
    def peer_transit_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[PeeringAttachmentOptionsArgs]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[PeeringAttachmentOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_account_id.setter
    def peer_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.input_type
class _PeeringAttachmentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[PeeringAttachmentOptionsArgs]] = ...,
        peer_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_region: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[PeeringAttachmentOptionsArgs]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[PeeringAttachmentOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_account_id.setter
    def peer_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_region.setter
    def peer_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_transit_gateway_id.setter
    def peer_transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PeeringAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        options: Optional[
            pulumi.Input[
                Union[PeeringAttachmentOptionsArgs, PeeringAttachmentOptionsArgsDict]
            ]
        ] = ...,
        peer_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_region: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PeeringAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[
            pulumi.Input[
                Union[PeeringAttachmentOptionsArgs, PeeringAttachmentOptionsArgsDict]
            ]
        ] = ...,
        peer_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_region: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PeeringAttachment: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional[outputs.PeeringAttachmentOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerTransitGatewayId")
    def peer_transit_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
