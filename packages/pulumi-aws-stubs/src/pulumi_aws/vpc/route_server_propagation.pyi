

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
__all__ = ['RouteServerPropagationArgs', 'RouteServerPropagation']
@pulumi.input_type
class RouteServerPropagationArgs:
    def __init__(__self__, *, route_server_id: pulumi.Input[_builtins.str], route_table_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @route_server_id.setter
    def route_server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @route_table_id.setter
    def route_table_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RouteServerPropagationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_server_id.setter
    def route_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_table_id.setter
    def route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RouteServerPropagationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RouteServerPropagation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[RouteServerPropagationTimeoutsArgs, RouteServerPropagationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouteServerPropagationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., route_table_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[RouteServerPropagationTimeoutsArgs, RouteServerPropagationTimeoutsArgsDict]]] = ...) -> RouteServerPropagation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.RouteServerPropagationTimeouts]]:
        ...
    


