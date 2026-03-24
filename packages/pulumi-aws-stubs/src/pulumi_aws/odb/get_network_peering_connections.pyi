

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkPeeringConnectionsResult', 'AwaitableGetNetworkPeeringConnectionsResult', 'get_network_peering_connections', 'get_network_peering_connections_output']
@pulumi.output_type
class GetNetworkPeeringConnectionsResult:
    
    def __init__(__self__, id=..., odb_peering_connections=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbPeeringConnections")
    def odb_peering_connections(self) -> Sequence[outputs.GetNetworkPeeringConnectionsOdbPeeringConnectionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetNetworkPeeringConnectionsResult(GetNetworkPeeringConnectionsResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkPeeringConnectionsResult]:
        ...
    


def get_network_peering_connections(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkPeeringConnectionsResult:
    
    ...

def get_network_peering_connections_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkPeeringConnectionsResult]:
    
    ...

