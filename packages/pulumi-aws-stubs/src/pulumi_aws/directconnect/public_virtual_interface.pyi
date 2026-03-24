

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PublicVirtualInterfaceArgs', 'PublicVirtualInterface']
@pulumi.input_type
class PublicVirtualInterfaceArgs:
    def __init__(__self__, *, address_family: pulumi.Input[_builtins.str], bgp_asn: pulumi.Input[_builtins.int], connection_id: pulumi.Input[_builtins.str], route_filter_prefixes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vlan: pulumi.Input[_builtins.int], amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address_family.setter
    def address_family(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bgp_asn.setter
    def bgp_asn(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeFilterPrefixes")
    def route_filter_prefixes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @route_filter_prefixes.setter
    def route_filter_prefixes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan.setter
    def vlan(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _PublicVirtualInterfaceState:
    def __init__(__self__, *, address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., amazon_side_asn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_device: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_filter_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @amazon_side_asn.setter
    def amazon_side_asn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_device.setter
    def aws_device(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bgp_asn.setter
    def bgp_asn(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="routeFilterPrefixes")
    def route_filter_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @route_filter_prefixes.setter
    def route_filter_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PublicVirtualInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_filter_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PublicVirtualInterfaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., amazon_side_asn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_device: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_filter_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ...) -> PublicVirtualInterface:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeFilterPrefixes")
    def route_filter_prefixes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter
    def vlan(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


