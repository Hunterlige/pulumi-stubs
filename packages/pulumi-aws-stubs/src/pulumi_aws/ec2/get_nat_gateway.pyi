import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNatGatewayResult",
    "AwaitableGetNatGatewayResult",
    "get_nat_gateway",
    "get_nat_gateway_output",
]

@pulumi.output_type
class GetNatGatewayResult:
    def __init__(
        __self__,
        allocation_id=...,
        association_id=...,
        auto_provision_zones=...,
        auto_scaling_ips=...,
        availability_mode=...,
        availability_zone_addresses=...,
        connectivity_type=...,
        filters=...,
        id=...,
        network_interface_id=...,
        private_ip=...,
        public_ip=...,
        region=...,
        regional_nat_gateway_addresses=...,
        route_table_id=...,
        secondary_allocation_ids=...,
        secondary_private_ip_address_count=...,
        secondary_private_ip_addresses=...,
        state=...,
        subnet_id=...,
        tags=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisionZones")
    def auto_provision_zones(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingIps")
    def auto_scaling_ips(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityMode")
    def availability_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneAddresses")
    def availability_zone_addresses(
        self,
    ) -> Sequence[outputs.GetNatGatewayAvailabilityZoneAddressResult]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetNatGatewayFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayAddresses")
    def regional_nat_gateway_addresses(
        self,
    ) -> Sequence[outputs.GetNatGatewayRegionalNatGatewayAddressResult]: ...
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetNatGatewayResult(GetNatGatewayResult):
    def __await__(self): ...

def get_nat_gateway(
    filters: Optional[
        Sequence[Union[GetNatGatewayFilterArgs, GetNatGatewayFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    state: Optional[_builtins.str] = ...,
    subnet_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    vpc_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNatGatewayResult: ...
def get_nat_gateway_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetNatGatewayFilterArgs, GetNatGatewayFilterArgsDict]]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    state: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    subnet_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNatGatewayResult]: ...
