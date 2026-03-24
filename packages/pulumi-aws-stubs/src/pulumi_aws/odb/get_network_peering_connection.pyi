

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkPeeringConnectionResult', 'AwaitableGetNetworkPeeringConnectionResult', 'get_network_peering_connection', 'get_network_peering_connection_output']
@pulumi.output_type
class GetNetworkPeeringConnectionResult:
    
    def __init__(__self__, arn=..., created_at=..., display_name=..., id=..., odb_network_arn=..., odb_peering_connection_type=..., peer_network_arn=..., percent_progress=..., region=..., status=..., status_reason=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbPeeringConnectionType")
    def odb_peering_connection_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerNetworkArn")
    def peer_network_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetNetworkPeeringConnectionResult(GetNetworkPeeringConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkPeeringConnectionResult]:
        ...
    


def get_network_peering_connection(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkPeeringConnectionResult:
    
    ...

def get_network_peering_connection_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkPeeringConnectionResult]:
    
    ...

