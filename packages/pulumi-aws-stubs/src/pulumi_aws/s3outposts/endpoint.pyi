

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointArgs', 'Endpoint']
@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *, outpost_id: pulumi.Input[_builtins.str], security_group_id: pulumi.Input[_builtins.str], subnet_id: pulumi.Input[_builtins.str], access_type: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @outpost_id.setter
    def outpost_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointState:
    def __init__(__self__, *, access_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceArgs]]]] = ..., outpost_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_id.setter
    def outpost_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3outposts/endpoint:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_type: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., outpost_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., customer_owned_ipv4_pool: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointNetworkInterfaceArgs, EndpointNetworkInterfaceArgsDict]]]]] = ..., outpost_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Endpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence[outputs.EndpointNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


