

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TransitGatewayRegistrationArgs', 'TransitGatewayRegistration']
@pulumi.input_type
class TransitGatewayRegistrationArgs:
    def __init__(__self__, *, global_network_id: pulumi.Input[_builtins.str], transit_gateway_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _TransitGatewayRegistrationState:
    def __init__(__self__, *, global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TransitGatewayRegistration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TransitGatewayRegistrationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> TransitGatewayRegistration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


