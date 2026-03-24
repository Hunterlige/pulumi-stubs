

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
__all__ = ['DefaultRouteTableAssociationArgs', 'DefaultRouteTableAssociation']
@pulumi.input_type
class DefaultRouteTableAssociationArgs:
    def __init__(__self__, *, transit_gateway_id: pulumi.Input[_builtins.str], transit_gateway_route_table_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DefaultRouteTableAssociationState:
    def __init__(__self__, *, original_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originalDefaultRouteTableId")
    def original_default_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @original_default_route_table_id.setter
    def original_default_route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DefaultRouteTableAssociationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DefaultRouteTableAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DefaultRouteTableAssociationTimeoutsArgs, DefaultRouteTableAssociationTimeoutsArgsDict]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefaultRouteTableAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., original_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DefaultRouteTableAssociationTimeoutsArgs, DefaultRouteTableAssociationTimeoutsArgsDict]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...) -> DefaultRouteTableAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originalDefaultRouteTableId")
    def original_default_route_table_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DefaultRouteTableAssociationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


