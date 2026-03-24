

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GatewayRouteConfigArgs', 'GatewayRouteConfig']
@pulumi.input_type
class GatewayRouteConfigArgs:
    def __init__(__self__, *, gateway_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[GatewayRouteConfigPropertiesArgs]] = ..., route_config_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[GatewayRouteConfigPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[GatewayRouteConfigPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeConfigName")
    def route_config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_config_name.setter
    def route_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:appplatform:GatewayRouteConfig")
class GatewayRouteConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[GatewayRouteConfigPropertiesArgs, GatewayRouteConfigPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_config_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GatewayRouteConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> GatewayRouteConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.GatewayRouteConfigPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


