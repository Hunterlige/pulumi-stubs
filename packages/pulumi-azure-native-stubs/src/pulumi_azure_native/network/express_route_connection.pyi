

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
__all__ = ['ExpressRouteConnectionInitArgs', 'ExpressRouteConnection']
@pulumi.input_type
class ExpressRouteConnectionInitArgs:
    def __init__(__self__, *, express_route_circuit_peering: pulumi.Input[ExpressRouteCircuitPeeringIdArgs], express_route_gateway_name: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., enable_private_link_fast_path: Optional[pulumi.Input[_builtins.bool]] = ..., express_route_gateway_bypass: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., routing_configuration: Optional[pulumi.Input[RoutingConfigurationArgs]] = ..., routing_weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Input[ExpressRouteCircuitPeeringIdArgs]:
        
        ...
    
    @express_route_circuit_peering.setter
    def express_route_circuit_peering(self, value: pulumi.Input[ExpressRouteCircuitPeeringIdArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteGatewayName")
    def express_route_gateway_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @express_route_gateway_name.setter
    def express_route_gateway_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_security.setter
    def enable_internet_security(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_private_link_fast_path.setter
    def enable_private_link_fast_path(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @express_route_gateway_bypass.setter
    def express_route_gateway_bypass(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[pulumi.Input[RoutingConfigurationArgs]]:
        
        ...
    
    @routing_configuration.setter
    def routing_configuration(self, value: Optional[pulumi.Input[RoutingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @routing_weight.setter
    def routing_weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:ExpressRouteConnection")
class ExpressRouteConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., enable_private_link_fast_path: Optional[pulumi.Input[_builtins.bool]] = ..., express_route_circuit_peering: Optional[pulumi.Input[Union[ExpressRouteCircuitPeeringIdArgs, ExpressRouteCircuitPeeringIdArgsDict]]] = ..., express_route_gateway_bypass: Optional[pulumi.Input[_builtins.bool]] = ..., express_route_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_configuration: Optional[pulumi.Input[Union[RoutingConfigurationArgs, RoutingConfigurationArgsDict]]] = ..., routing_weight: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRouteConnectionInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRouteConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateLinkFastPath")
    def enable_private_link_fast_path(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Output[outputs.ExpressRouteCircuitPeeringIdResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> pulumi.Output[Optional[outputs.RoutingConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


