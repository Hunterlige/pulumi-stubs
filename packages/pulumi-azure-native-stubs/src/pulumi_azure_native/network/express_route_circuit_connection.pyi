

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
__all__ = ['ExpressRouteCircuitConnectionInitArgs', 'ExpressRouteCircuitConnection']
@pulumi.input_type
class ExpressRouteCircuitConnectionInitArgs:
    def __init__(__self__, *, circuit_name: pulumi.Input[_builtins.str], peering_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], address_prefix: Optional[pulumi.Input[_builtins.str]] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., express_route_circuit_peering: Optional[pulumi.Input[SubResourceArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_circuit_connection_config: Optional[pulumi.Input[Ipv6CircuitConnectionConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_express_route_circuit_peering: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @circuit_name.setter
    def circuit_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peering_name.setter
    def peering_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @express_route_circuit_peering.setter
    def express_route_circuit_peering(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CircuitConnectionConfig")
    def ipv6_circuit_connection_config(self) -> Optional[pulumi.Input[Ipv6CircuitConnectionConfigArgs]]:
        
        ...
    
    @ipv6_circuit_connection_config.setter
    def ipv6_circuit_connection_config(self, value: Optional[pulumi.Input[Ipv6CircuitConnectionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @peer_express_route_circuit_peering.setter
    def peer_express_route_circuit_peering(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:ExpressRouteCircuitConnection")
class ExpressRouteCircuitConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_prefix: Optional[pulumi.Input[_builtins.str]] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., circuit_name: Optional[pulumi.Input[_builtins.str]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., express_route_circuit_peering: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_circuit_connection_config: Optional[pulumi.Input[Union[Ipv6CircuitConnectionConfigArgs, Ipv6CircuitConnectionConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_express_route_circuit_peering: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., peering_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRouteCircuitConnectionInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRouteCircuitConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CircuitConnectionConfig")
    def ipv6_circuit_connection_config(self) -> pulumi.Output[Optional[outputs.Ipv6CircuitConnectionConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


