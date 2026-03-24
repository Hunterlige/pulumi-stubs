

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppServicePlanRouteForVnetArgs', 'AppServicePlanRouteForVnet']
@pulumi.input_type
class AppServicePlanRouteForVnetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], vnet_name: pulumi.Input[_builtins.str], end_address: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., route_name: Optional[pulumi.Input[_builtins.str]] = ..., route_type: Optional[pulumi.Input[Union[_builtins.str, RouteType]]] = ..., start_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vnet_name.setter
    def vnet_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_address.setter
    def end_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[pulumi.Input[Union[_builtins.str, RouteType]]]:
        
        ...
    
    @route_type.setter
    def route_type(self, value: Optional[pulumi.Input[Union[_builtins.str, RouteType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_address.setter
    def start_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:AppServicePlanRouteForVnet")
class AppServicePlanRouteForVnet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., end_address: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_name: Optional[pulumi.Input[_builtins.str]] = ..., route_type: Optional[pulumi.Input[Union[_builtins.str, RouteType]]] = ..., start_address: Optional[pulumi.Input[_builtins.str]] = ..., vnet_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppServicePlanRouteForVnetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AppServicePlanRouteForVnet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


