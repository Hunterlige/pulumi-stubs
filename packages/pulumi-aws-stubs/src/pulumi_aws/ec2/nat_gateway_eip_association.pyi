import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NatGatewayEipAssociationArgs", "NatGatewayEipAssociation"]

@pulumi.input_type
class NatGatewayEipAssociationArgs:
    def __init__(
        __self__,
        *,
        allocation_id: pulumi.Input[_builtins.str],
        nat_gateway_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_id.setter
    def allocation_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _NatGatewayEipAssociationState:
    def __init__(
        __self__,
        *,
        allocation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[NatGatewayEipAssociationTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class NatGatewayEipAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    NatGatewayEipAssociationTimeoutsArgs,
                    NatGatewayEipAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NatGatewayEipAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    NatGatewayEipAssociationTimeoutsArgs,
                    NatGatewayEipAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> NatGatewayEipAssociation: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.NatGatewayEipAssociationTimeouts]]: ...
