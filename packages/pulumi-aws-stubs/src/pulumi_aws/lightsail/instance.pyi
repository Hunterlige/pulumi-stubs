

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
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, availability_zone: pulumi.Input[_builtins.str], blueprint_id: pulumi.Input[_builtins.str], bundle_id: pulumi.Input[_builtins.str], add_on: Optional[pulumi.Input[InstanceAddOnArgs]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., key_pair_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @blueprint_id.setter
    def blueprint_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addOn")
    def add_on(self) -> Optional[pulumi.Input[InstanceAddOnArgs]]:
        
        ...
    
    @add_on.setter
    def add_on(self, value: Optional[pulumi.Input[InstanceAddOnArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_pair_name.setter
    def key_pair_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, add_on: Optional[pulumi.Input[InstanceAddOnArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., blueprint_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., is_static_ip: Optional[pulumi.Input[_builtins.bool]] = ..., key_pair_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ram_size: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addOn")
    def add_on(self) -> Optional[pulumi.Input[InstanceAddOnArgs]]:
        
        ...
    
    @add_on.setter
    def add_on(self, value: Optional[pulumi.Input[InstanceAddOnArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blueprint_id.setter
    def blueprint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStaticIp")
    def is_static_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_static_ip.setter
    def is_static_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_pair_name.setter
    def key_pair_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @ram_size.setter
    def ram_size(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lightsail/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., add_on: Optional[pulumi.Input[Union[InstanceAddOnArgs, InstanceAddOnArgsDict]]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., blueprint_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., key_pair_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., add_on: Optional[pulumi.Input[Union[InstanceAddOnArgs, InstanceAddOnArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., blueprint_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., is_static_ip: Optional[pulumi.Input[_builtins.bool]] = ..., key_pair_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ram_size: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addOn")
    def add_on(self) -> pulumi.Output[Optional[outputs.InstanceAddOn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStaticIp")
    def is_static_ip(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> pulumi.Output[_builtins.float]:
        
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
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


