

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NatGatewayArgs', 'NatGateway']
@pulumi.input_type
class NatGatewayArgs:
    def __init__(__self__, *, allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., availability_mode: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]] = ..., connectivity_type: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityMode")
    def availability_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_mode.setter
    def availability_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneAddresses")
    def availability_zone_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]]:
        
        ...
    
    @availability_zone_addresses.setter
    def availability_zone_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connectivity_type.setter
    def connectivity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_allocation_ids.setter
    def secondary_allocation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @secondary_private_ip_address_count.setter
    def secondary_private_ip_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_private_ip_addresses.setter
    def secondary_private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NatGatewayState:
    def __init__(__self__, *, allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., auto_provision_zones: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_ips: Optional[pulumi.Input[_builtins.str]] = ..., availability_mode: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]] = ..., connectivity_type: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayRegionalNatGatewayAddressArgs]]]] = ..., regional_nat_gateway_auto_mode: Optional[pulumi.Input[_builtins.str]] = ..., route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoProvisionZones")
    def auto_provision_zones(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_provision_zones.setter
    def auto_provision_zones(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingIps")
    def auto_scaling_ips(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_scaling_ips.setter
    def auto_scaling_ips(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityMode")
    def availability_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_mode.setter
    def availability_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneAddresses")
    def availability_zone_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]]:
        
        ...
    
    @availability_zone_addresses.setter
    def availability_zone_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayAvailabilityZoneAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connectivity_type.setter
    def connectivity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayAddresses")
    def regional_nat_gateway_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayRegionalNatGatewayAddressArgs]]]]:
        
        ...
    
    @regional_nat_gateway_addresses.setter
    def regional_nat_gateway_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NatGatewayRegionalNatGatewayAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayAutoMode")
    def regional_nat_gateway_auto_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @regional_nat_gateway_auto_mode.setter
    def regional_nat_gateway_auto_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_allocation_ids.setter
    def secondary_allocation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @secondary_private_ip_address_count.setter
    def secondary_private_ip_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_private_ip_addresses.setter
    def secondary_private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/natGateway:NatGateway")
class NatGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., availability_mode: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NatGatewayAvailabilityZoneAddressArgs, NatGatewayAvailabilityZoneAddressArgsDict]]]]] = ..., connectivity_type: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[NatGatewayArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., auto_provision_zones: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_ips: Optional[pulumi.Input[_builtins.str]] = ..., availability_mode: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NatGatewayAvailabilityZoneAddressArgs, NatGatewayAvailabilityZoneAddressArgsDict]]]]] = ..., connectivity_type: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regional_nat_gateway_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NatGatewayRegionalNatGatewayAddressArgs, NatGatewayRegionalNatGatewayAddressArgsDict]]]]] = ..., regional_nat_gateway_auto_mode: Optional[pulumi.Input[_builtins.str]] = ..., route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., secondary_allocation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secondary_private_ip_address_count: Optional[pulumi.Input[_builtins.int]] = ..., secondary_private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> NatGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoProvisionZones")
    def auto_provision_zones(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingIps")
    def auto_scaling_ips(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityMode")
    def availability_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneAddresses")
    def availability_zone_addresses(self) -> pulumi.Output[Optional[Sequence[outputs.NatGatewayAvailabilityZoneAddress]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayAddresses")
    def regional_nat_gateway_addresses(self) -> pulumi.Output[Sequence[outputs.NatGatewayRegionalNatGatewayAddress]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalNatGatewayAutoMode")
    def regional_nat_gateway_auto_mode(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryAllocationIds")
    def secondary_allocation_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


