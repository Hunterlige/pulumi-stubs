import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcPeeringConnectionAccepterInitArgs", "VpcPeeringConnectionAccepter"]

@pulumi.input_type
class VpcPeeringConnectionAccepterInitArgs:
    def __init__(
        __self__,
        *,
        vpc_peering_connection_id: pulumi.Input[_builtins.str],
        accepter: Optional[
            pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]
        ] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester: Optional[
            pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def accepter(
        self,
    ) -> Optional[pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]]: ...
    @accepter.setter
    def accepter(
        self, value: Optional[pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_accept.setter
    def auto_accept(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requester(
        self,
    ) -> Optional[pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]]: ...
    @requester.setter
    def requester(
        self, value: Optional[pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]]
    ): ...
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
class _VpcPeeringConnectionAccepterState:
    def __init__(
        __self__,
        *,
        accept_status: Optional[pulumi.Input[_builtins.str]] = ...,
        accepter: Optional[
            pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]
        ] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        peer_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_region: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester: Optional[
            pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptStatus")
    def accept_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_status.setter
    def accept_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def accepter(
        self,
    ) -> Optional[pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]]: ...
    @accepter.setter
    def accepter(
        self, value: Optional[pulumi.Input[VpcPeeringConnectionAccepterAccepterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_accept.setter
    def auto_accept(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="peerOwnerId")
    def peer_owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_owner_id.setter
    def peer_owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_region.setter
    def peer_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_vpc_id.setter
    def peer_vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requester(
        self,
    ) -> Optional[pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]]: ...
    @requester.setter
    def requester(
        self, value: Optional[pulumi.Input[VpcPeeringConnectionAccepterRequesterArgs]]
    ): ...
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class VpcPeeringConnectionAccepter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accepter: Optional[
            pulumi.Input[
                Union[
                    VpcPeeringConnectionAccepterAccepterArgs,
                    VpcPeeringConnectionAccepterAccepterArgsDict,
                ]
            ]
        ] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester: Optional[
            pulumi.Input[
                Union[
                    VpcPeeringConnectionAccepterRequesterArgs,
                    VpcPeeringConnectionAccepterRequesterArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcPeeringConnectionAccepterInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_status: Optional[pulumi.Input[_builtins.str]] = ...,
        accepter: Optional[
            pulumi.Input[
                Union[
                    VpcPeeringConnectionAccepterAccepterArgs,
                    VpcPeeringConnectionAccepterAccepterArgsDict,
                ]
            ]
        ] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        peer_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_region: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester: Optional[
            pulumi.Input[
                Union[
                    VpcPeeringConnectionAccepterRequesterArgs,
                    VpcPeeringConnectionAccepterRequesterArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcPeeringConnectionAccepter: ...
    @_builtins.property
    @pulumi.getter(name="acceptStatus")
    def accept_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def accepter(
        self,
    ) -> pulumi.Output[outputs.VpcPeeringConnectionAccepterAccepter]: ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="peerOwnerId")
    def peer_owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def requester(
        self,
    ) -> pulumi.Output[outputs.VpcPeeringConnectionAccepterRequester]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> pulumi.Output[_builtins.str]: ...
