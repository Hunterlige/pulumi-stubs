

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
    
    def __init__(__self__, create_time=..., description=..., export_custom_routes=..., export_custom_routes_with_public_ip=..., id=..., import_custom_routes=..., import_custom_routes_with_public_ip=..., name=..., peer_network=..., peer_network_type=..., project=..., state=..., state_details=..., uid=..., update_time=..., vmware_engine_network=..., vmware_engine_network_canonical=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutesWithPublicIp")
    def export_custom_routes_with_public_ip(self) -> _builtins.bool:
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
    @pulumi.getter(name="importCustomRoutesWithPublicIp")
    def import_custom_routes_with_public_ip(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetworkType")
    def peer_network_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
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
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> _builtins.str:
        ...
    


class AwaitableGetNetworkPeeringResult(GetNetworkPeeringResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkPeeringResult]:
        ...
    


def get_network_peering(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkPeeringResult:
    
    ...

def get_network_peering_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkPeeringResult]:
    
    ...

