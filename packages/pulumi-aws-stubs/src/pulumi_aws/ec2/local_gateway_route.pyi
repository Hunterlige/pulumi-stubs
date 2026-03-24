import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocalGatewayRouteArgs", "LocalGatewayRoute"]

@pulumi.input_type
class LocalGatewayRouteArgs:
    def __init__(
        __self__,
        *,
        destination_cidr_block: pulumi.Input[_builtins.str],
        local_gateway_route_table_id: pulumi.Input[_builtins.str],
        local_gateway_virtual_interface_group_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Input[_builtins.str]: ...
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Input[_builtins.str]: ...
    @local_gateway_route_table_id.setter
    def local_gateway_route_table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceGroupId")
    def local_gateway_virtual_interface_group_id(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @local_gateway_virtual_interface_group_id.setter
    def local_gateway_virtual_interface_group_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LocalGatewayRouteState:
    def __init__(
        __self__,
        *,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_virtual_interface_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_gateway_route_table_id.setter
    def local_gateway_route_table_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceGroupId")
    def local_gateway_virtual_interface_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_gateway_virtual_interface_group_id.setter
    def local_gateway_virtual_interface_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/localGatewayRoute:LocalGatewayRoute")
class LocalGatewayRoute(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_virtual_interface_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocalGatewayRouteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_virtual_interface_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LocalGatewayRoute: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceGroupId")
    def local_gateway_virtual_interface_group_id(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
