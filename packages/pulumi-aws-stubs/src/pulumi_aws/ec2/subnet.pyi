

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SubnetArgs', 'Subnet']
@pulumi.input_type
class SubnetArgs:
    def __init__(__self__, *, vpc_id: pulumi.Input[_builtins.str], assign_ipv6_address_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., enable_dns64: Optional[pulumi.Input[_builtins.bool]] = ..., enable_lni_at_device_index: Optional[pulumi.Input[_builtins.int]] = ..., enable_resource_name_dns_a_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_native: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., map_customer_owned_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., map_public_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_hostname_type_on_launch: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @assign_ipv6_address_on_creation.setter
    def assign_ipv6_address_on_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dns64.setter
    def enable_dns64(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @enable_lni_at_device_index.setter
    def enable_lni_at_device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecordOnLaunch")
    def enable_resource_name_dns_a_record_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_a_record_on_launch.setter
    def enable_resource_name_dns_a_record_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecordOnLaunch")
    def enable_resource_name_dns_aaaa_record_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_aaaa_record_on_launch.setter
    def enable_resource_name_dns_aaaa_record_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv6_native.setter
    def ipv6_native(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @map_customer_owned_ip_on_launch.setter
    def map_customer_owned_ip_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsHostnameTypeOnLaunch")
    def private_dns_hostname_type_on_launch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_hostname_type_on_launch.setter
    def private_dns_hostname_type_on_launch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _SubnetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., assign_ipv6_address_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., enable_dns64: Optional[pulumi.Input[_builtins.bool]] = ..., enable_lni_at_device_index: Optional[pulumi.Input[_builtins.int]] = ..., enable_resource_name_dns_a_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_block_association_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_native: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., map_customer_owned_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., map_public_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_hostname_type_on_launch: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @assign_ipv6_address_on_creation.setter
    def assign_ipv6_address_on_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dns64.setter
    def enable_dns64(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @enable_lni_at_device_index.setter
    def enable_lni_at_device_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecordOnLaunch")
    def enable_resource_name_dns_a_record_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_a_record_on_launch.setter
    def enable_resource_name_dns_a_record_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecordOnLaunch")
    def enable_resource_name_dns_aaaa_record_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_resource_name_dns_aaaa_record_on_launch.setter
    def enable_resource_name_dns_aaaa_record_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockAssociationId")
    def ipv6_cidr_block_association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block_association_id.setter
    def ipv6_cidr_block_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv6_native.setter
    def ipv6_native(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @map_customer_owned_ip_on_launch.setter
    def map_customer_owned_ip_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsHostnameTypeOnLaunch")
    def private_dns_hostname_type_on_launch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_hostname_type_on_launch.setter
    def private_dns_hostname_type_on_launch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:ec2/subnet:Subnet")
class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assign_ipv6_address_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., enable_dns64: Optional[pulumi.Input[_builtins.bool]] = ..., enable_lni_at_device_index: Optional[pulumi.Input[_builtins.int]] = ..., enable_resource_name_dns_a_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_native: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., map_customer_owned_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., map_public_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_hostname_type_on_launch: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SubnetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., assign_ipv6_address_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., enable_dns64: Optional[pulumi.Input[_builtins.bool]] = ..., enable_lni_at_device_index: Optional[pulumi.Input[_builtins.int]] = ..., enable_resource_name_dns_a_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., enable_resource_name_dns_aaaa_record_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_block_association_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_native: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., map_customer_owned_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., map_public_ip_on_launch: Optional[pulumi.Input[_builtins.bool]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_hostname_type_on_launch: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Subnet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDns64")
    def enable_dns64(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLniAtDeviceIndex")
    def enable_lni_at_device_index(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsARecordOnLaunch")
    def enable_resource_name_dns_a_record_on_launch(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableResourceNameDnsAaaaRecordOnLaunch")
    def enable_resource_name_dns_aaaa_record_on_launch(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockAssociationId")
    def ipv6_cidr_block_association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Native")
    def ipv6_native(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsHostnameTypeOnLaunch")
    def private_dns_hostname_type_on_launch(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    


