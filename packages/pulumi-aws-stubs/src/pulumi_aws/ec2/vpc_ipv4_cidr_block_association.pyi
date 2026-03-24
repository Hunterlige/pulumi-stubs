

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcIpv4CidrBlockAssociationArgs', 'VpcIpv4CidrBlockAssociation']
@pulumi.input_type
class VpcIpv4CidrBlockAssociationArgs:
    def __init__(__self__, *, vpc_id: pulumi.Input[_builtins.str], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcIpv4CidrBlockAssociationState:
    def __init__(__self__, *, cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcIpv4CidrBlockAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcIpv4CidrBlockAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcIpv4CidrBlockAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


