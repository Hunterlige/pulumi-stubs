import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetRouteResult", "AwaitableGetRouteResult", "get_route", "get_route_output"]

@pulumi.output_type
class GetRouteResult:
    def __init__(
        __self__,
        carrier_gateway_id=...,
        core_network_arn=...,
        destination_cidr_block=...,
        destination_ipv6_cidr_block=...,
        destination_prefix_list_id=...,
        egress_only_gateway_id=...,
        gateway_id=...,
        id=...,
        instance_id=...,
        local_gateway_id=...,
        nat_gateway_id=...,
        network_interface_id=...,
        region=...,
        route_table_id=...,
        transit_gateway_id=...,
        vpc_peering_connection_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="carrierGatewayId")
    def carrier_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="egressOnlyGatewayId")
    def egress_only_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="natGatewayId")
    def nat_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> _builtins.str: ...

class AwaitableGetRouteResult(GetRouteResult):
    def __await__(self): ...

def get_route(
    carrier_gateway_id: Optional[_builtins.str] = ...,
    core_network_arn: Optional[_builtins.str] = ...,
    destination_cidr_block: Optional[_builtins.str] = ...,
    destination_ipv6_cidr_block: Optional[_builtins.str] = ...,
    destination_prefix_list_id: Optional[_builtins.str] = ...,
    egress_only_gateway_id: Optional[_builtins.str] = ...,
    gateway_id: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    local_gateway_id: Optional[_builtins.str] = ...,
    nat_gateway_id: Optional[_builtins.str] = ...,
    network_interface_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    route_table_id: Optional[_builtins.str] = ...,
    transit_gateway_id: Optional[_builtins.str] = ...,
    vpc_peering_connection_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRouteResult: ...
def get_route_output(
    carrier_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    core_network_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    destination_cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    destination_ipv6_cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    destination_prefix_list_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    egress_only_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    local_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    nat_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    network_interface_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    transit_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    vpc_peering_connection_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRouteResult]: ...
