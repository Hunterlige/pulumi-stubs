

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcIpamPoolCidrArgs', 'VpcIpamPoolCidr']
@pulumi.input_type
class VpcIpamPoolCidrArgs:
    def __init__(__self__, *, ipam_pool_id: pulumi.Input[_builtins.str], cidr: Optional[pulumi.Input[_builtins.str]] = ..., cidr_authorization_context: Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]] = ..., netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrAuthorizationContext")
    def cidr_authorization_context(self) -> Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]]:
        
        ...
    
    @cidr_authorization_context.setter
    def cidr_authorization_context(self, value: Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcIpamPoolCidrState:
    def __init__(__self__, *, cidr: Optional[pulumi.Input[_builtins.str]] = ..., cidr_authorization_context: Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]] = ..., ipam_pool_cidr_id: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrAuthorizationContext")
    def cidr_authorization_context(self) -> Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]]:
        
        ...
    
    @cidr_authorization_context.setter
    def cidr_authorization_context(self, value: Optional[pulumi.Input[VpcIpamPoolCidrCidrAuthorizationContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolCidrId")
    def ipam_pool_cidr_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipam_pool_cidr_id.setter
    def ipam_pool_cidr_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipam_pool_id.setter
    def ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @netmask_length.setter
    def netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/vpcIpamPoolCidr:VpcIpamPoolCidr")
class VpcIpamPoolCidr(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cidr: Optional[pulumi.Input[_builtins.str]] = ..., cidr_authorization_context: Optional[pulumi.Input[Union[VpcIpamPoolCidrCidrAuthorizationContextArgs, VpcIpamPoolCidrCidrAuthorizationContextArgsDict]]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcIpamPoolCidrArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cidr: Optional[pulumi.Input[_builtins.str]] = ..., cidr_authorization_context: Optional[pulumi.Input[Union[VpcIpamPoolCidrCidrAuthorizationContextArgs, VpcIpamPoolCidrCidrAuthorizationContextArgsDict]]] = ..., ipam_pool_cidr_id: Optional[pulumi.Input[_builtins.str]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., netmask_length: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcIpamPoolCidr:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrAuthorizationContext")
    def cidr_authorization_context(self) -> pulumi.Output[Optional[outputs.VpcIpamPoolCidrCidrAuthorizationContext]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolCidrId")
    def ipam_pool_cidr_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


