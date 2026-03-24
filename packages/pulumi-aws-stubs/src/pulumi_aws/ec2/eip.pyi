

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EipArgs', 'Eip']
@pulumi.input_type
class EipArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., associate_with_private_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., network_border_group: Optional[pulumi.Input[_builtins.str]] = ..., network_interface: Optional[pulumi.Input[_builtins.str]] = ..., public_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateWithPrivateIp")
    def associate_with_private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @associate_with_private_ip.setter
    def associate_with_private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_border_group.setter
    def network_border_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface.setter
    def network_interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ipv4_pool.setter
    def public_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _EipState:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_with_private_ip: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., carrier_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., network_border_group: Optional[pulumi.Input[_builtins.str]] = ..., network_interface: Optional[pulumi.Input[_builtins.str]] = ..., private_dns: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., ptr_record: Optional[pulumi.Input[_builtins.str]] = ..., public_dns: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateWithPrivateIp")
    def associate_with_private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @associate_with_private_ip.setter
    def associate_with_private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierIp")
    def carrier_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @carrier_ip.setter
    def carrier_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIp")
    def customer_owned_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ip.setter
    def customer_owned_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_border_group.setter
    def network_border_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface.setter
    def network_interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns.setter
    def private_dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecord")
    def ptr_record(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ptr_record.setter
    def ptr_record(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_dns.setter
    def public_dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ipv4_pool.setter
    def public_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:ec2/eip:Eip")
class Eip(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address: Optional[pulumi.Input[_builtins.str]] = ..., associate_with_private_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., network_border_group: Optional[pulumi.Input[_builtins.str]] = ..., network_interface: Optional[pulumi.Input[_builtins.str]] = ..., public_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[EipArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., address: Optional[pulumi.Input[_builtins.str]] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_with_private_ip: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., carrier_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ip: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., network_border_group: Optional[pulumi.Input[_builtins.str]] = ..., network_interface: Optional[pulumi.Input[_builtins.str]] = ..., private_dns: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., ptr_record: Optional[pulumi.Input[_builtins.str]] = ..., public_dns: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Eip:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateWithPrivateIp")
    def associate_with_private_ip(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierIp")
    def carrier_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIp")
    def customer_owned_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecord")
    def ptr_record(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> pulumi.Output[_builtins.str]:
        
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
    


