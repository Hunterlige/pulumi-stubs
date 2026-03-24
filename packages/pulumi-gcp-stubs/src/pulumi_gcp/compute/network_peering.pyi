

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkPeeringArgs', 'NetworkPeering']
@pulumi.input_type
class NetworkPeeringArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str], peer_network: pulumi.Input[_builtins.str], export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., export_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., import_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_network.setter
    def peer_network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @export_custom_routes.setter
    def export_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @export_subnet_routes_with_public_ip.setter
    def export_subnet_routes_with_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_custom_routes.setter
    def import_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_subnet_routes_with_public_ip.setter
    def import_subnet_routes_with_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkPeeringState:
    def __init__(__self__, *, export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., export_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., import_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., peer_network: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @export_custom_routes.setter
    def export_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @export_subnet_routes_with_public_ip.setter
    def export_subnet_routes_with_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_custom_routes.setter
    def import_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_subnet_routes_with_public_ip.setter
    def import_subnet_routes_with_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_network.setter
    def peer_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_details.setter
    def state_details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_strategy.setter
    def update_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/networkPeering:NetworkPeering")
class NetworkPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., export_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., import_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., peer_network: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkPeeringArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., export_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ..., import_subnet_routes_with_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., peer_network: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., update_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> NetworkPeering:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


