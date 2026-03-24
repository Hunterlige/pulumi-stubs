

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
__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']
@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *, subnet_id: pulumi.Input[_builtins.str], attachments: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_address_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips_count: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]]:
        
        ...
    
    @attachments.setter
    def attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_primary_ipv6.setter
    def enable_primary_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_prefix_count.setter
    def ipv4_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_prefixes.setter
    def ipv4_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressListEnabled")
    def ipv6_address_list_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv6_address_list_enabled.setter
    def ipv6_address_list_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressLists")
    def ipv6_address_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_address_lists.setter
    def ipv6_address_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_prefix_count.setter
    def ipv6_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_prefixes.setter
    def ipv6_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpListEnabled")
    def private_ip_list_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_ip_list_enabled.setter
    def private_ip_list_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpLists")
    def private_ip_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ip_lists.setter
    def private_ip_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ips.setter
    def private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpsCount")
    def private_ips_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @private_ips_count.setter
    def private_ips_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkInterfaceState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., attachments: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_address_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips_count: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]]:
        
        ...
    
    @attachments.setter
    def attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_primary_ipv6.setter
    def enable_primary_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv4_prefix_count.setter
    def ipv4_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_prefixes.setter
    def ipv4_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressListEnabled")
    def ipv6_address_list_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv6_address_list_enabled.setter
    def ipv6_address_list_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressLists")
    def ipv6_address_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_address_lists.setter
    def ipv6_address_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_prefix_count.setter
    def ipv6_prefix_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_prefixes.setter
    def ipv6_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_name.setter
    def private_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpListEnabled")
    def private_ip_list_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_ip_list_enabled.setter
    def private_ip_list_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpLists")
    def private_ip_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ip_lists.setter
    def private_ip_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @private_ips.setter
    def private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpsCount")
    def private_ips_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @private_ips_count.setter
    def private_ips_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    


@pulumi.type_token("aws:ec2/networkInterface:NetworkInterface")
class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attachments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInterfaceAttachmentArgs, NetworkInterfaceAttachmentArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_address_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips_count: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkInterfaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., attachments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInterfaceAttachmentArgs, NetworkInterfaceAttachmentArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., interface_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv4_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_address_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ipv6_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_prefix_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_list_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_ips_count: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> NetworkInterface:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> pulumi.Output[Sequence[outputs.NetworkInterfaceAttachment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Prefixes")
    def ipv4_prefixes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressListEnabled")
    def ipv6_address_list_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressLists")
    def ipv6_address_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Prefixes")
    def ipv6_prefixes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpListEnabled")
    def private_ip_list_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpLists")
    def private_ip_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpsCount")
    def private_ips_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


