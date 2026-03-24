

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSubnetResult', 'AwaitableGetSubnetResult', 'get_subnet', 'get_subnet_output']
@pulumi.output_type
class GetSubnetResult:
    
    def __init__(__self__, arn=..., assign_ipv6_address_on_creation=..., availability_zone=..., availability_zone_id=..., available_ip_address_count=..., cidr_block=..., customer_owned_ipv4_pool=..., default_for_az=..., enable_dns64=..., enable_lni_at_device_index=..., enable_resource_name_dns_a_record_on_launch=..., enable_resource_name_dns_aaaa_record_on_launch=..., filters=..., id=..., ipv6_cidr_block=..., ipv6_cidr_block_association_id=..., ipv6_native=..., map_customer_owned_ip_on_launch=..., map_public_ip_on_launch=..., outpost_arn=..., owner_id=..., private_dns_hostname_type_on_launch=..., region=..., state=..., tags=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableIpAddressCount")
    def available_ip_address_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultForAz")
    def default_for_az(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecordOnLaunch")
    def enable_resource_name_dns_a_record_on_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecordOnLaunch")
    def enable_resource_name_dns_aaaa_record_on_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSubnetFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockAssociationId")
    def ipv6_cidr_block_association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsHostnameTypeOnLaunch")
    def private_dns_hostname_type_on_launch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        ...
    


class AwaitableGetSubnetResult(GetSubnetResult):
    def __await__(self): # -> Generator[Never, Any, GetSubnetResult]:
        ...
    


def get_subnet(availability_zone: Optional[_builtins.str] = ..., availability_zone_id: Optional[_builtins.str] = ..., cidr_block: Optional[_builtins.str] = ..., default_for_az: Optional[_builtins.bool] = ..., filters: Optional[Sequence[Union[GetSubnetFilterArgs, GetSubnetFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., ipv6_cidr_block: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSubnetResult:
    
    ...

def get_subnet_output(availability_zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., availability_zone_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., default_for_az: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetSubnetFilterArgs, GetSubnetFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., ipv6_cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSubnetResult]:
    
    ...

