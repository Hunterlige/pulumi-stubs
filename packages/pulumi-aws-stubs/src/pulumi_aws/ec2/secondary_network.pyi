import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecondaryNetworkArgs", "SecondaryNetwork"]

@pulumi.input_type
class SecondaryNetworkArgs:
    def __init__(
        __self__,
        *,
        ipv4_cidr_block: pulumi.Input[_builtins.str],
        network_type: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> pulumi.Input[_builtins.str]: ...
    @ipv4_cidr_block.setter
    def ipv4_cidr_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Input[_builtins.str]: ...
    @network_type.setter
    def network_type(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]]): ...

@pulumi.input_type
class _SecondaryNetworkState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv4_cidr_block_associations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SecondaryNetworkIpv4CidrBlockAssociationArgs]]
            ]
        ] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_cidr_block.setter
    def ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlockAssociations")
    def ipv4_cidr_block_associations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[SecondaryNetworkIpv4CidrBlockAssociationArgs]]
        ]
    ]: ...
    @ipv4_cidr_block_associations.setter
    def ipv4_cidr_block_associations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SecondaryNetworkIpv4CidrBlockAssociationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_network_id.setter
    def secondary_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SecondaryNetworkTimeoutsArgs]]): ...

@pulumi.type_token("aws:ec2/secondaryNetwork:SecondaryNetwork")
class SecondaryNetwork(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[SecondaryNetworkTimeoutsArgs, SecondaryNetworkTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecondaryNetworkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv4_cidr_block_associations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SecondaryNetworkIpv4CidrBlockAssociationArgs,
                            SecondaryNetworkIpv4CidrBlockAssociationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[SecondaryNetworkTimeoutsArgs, SecondaryNetworkTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> SecondaryNetwork: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlockAssociations")
    def ipv4_cidr_block_associations(
        self,
    ) -> pulumi.Output[Sequence[outputs.SecondaryNetworkIpv4CidrBlockAssociation]]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkId")
    def secondary_network_id(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.SecondaryNetworkTimeouts]]: ...
