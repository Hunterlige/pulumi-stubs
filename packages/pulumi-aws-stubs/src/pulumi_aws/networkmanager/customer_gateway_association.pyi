

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomerGatewayAssociationArgs', 'CustomerGatewayAssociation']
@pulumi.input_type
class CustomerGatewayAssociationArgs:
    def __init__(__self__, *, customer_gateway_arn: pulumi.Input[_builtins.str], device_id: pulumi.Input[_builtins.str], global_network_id: pulumi.Input[_builtins.str], link_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGatewayArn")
    def customer_gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @customer_gateway_arn.setter
    def customer_gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_id.setter
    def device_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CustomerGatewayAssociationState:
    def __init__(__self__, *, customer_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., device_id: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGatewayArn")
    def customer_gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_gateway_arn.setter
    def customer_gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CustomerGatewayAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., customer_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., device_id: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomerGatewayAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., customer_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., device_id: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomerGatewayAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGatewayArn")
    def customer_gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


