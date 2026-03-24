import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RouteArgs", "Route"]

@pulumi.input_type
class RouteArgs:
    def __init__(
        __self__,
        *,
        route_table_id: pulumi.Input[_builtins.str],
        carrier_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Input[_builtins.str]: ...
    @route_table_id.setter
    def route_table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @carrier_gateway_id.setter
    def carrier_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_ipv6_cidr_block.setter
    def destination_ipv6_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress_only_gateway_id.setter
    def egress_only_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_gateway_id.setter
    def local_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _RouteState:
    def __init__(
        __self__,
        *,
        carrier_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        origin: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @carrier_gateway_id.setter
    def carrier_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_ipv6_cidr_block.setter
    def destination_ipv6_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_prefix_list_id.setter
    def destination_prefix_list_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress_only_gateway_id.setter
    def egress_only_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceOwnerId")
    def instance_owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_owner_id.setter
    def instance_owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_gateway_id.setter
    def local_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nat_gateway_id.setter
    def nat_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:ec2/route:Route")
class Route(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        carrier_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RouteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        carrier_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_only_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        origin: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Route: ...
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceOwnerId")
    def instance_owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
