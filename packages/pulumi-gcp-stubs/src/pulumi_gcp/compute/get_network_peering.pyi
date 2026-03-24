

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkPeeringResult', 'AwaitableGetNetworkPeeringResult', 'get_network_peering', 'get_network_peering_output']
@pulumi.output_type
class GetNetworkPeeringResult:
    
    def __init__(__self__, export_custom_routes=..., export_subnet_routes_with_public_ip=..., id=..., import_custom_routes=..., import_subnet_routes_with_public_ip=..., name=..., network=..., peer_network=..., stack_type=..., state=..., state_details=..., update_strategy=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> _builtins.str:
        ...
    


class AwaitableGetNetworkPeeringResult(GetNetworkPeeringResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkPeeringResult]:
        ...
    


def get_network_peering(name: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkPeeringResult:
    
    ...

def get_network_peering_output(name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkPeeringResult]:
    
    ...

