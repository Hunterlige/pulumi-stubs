

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectPeerResult', 'AwaitableGetConnectPeerResult', 'get_connect_peer', 'get_connect_peer_output']
@pulumi.output_type
class GetConnectPeerResult:
    
    def __init__(__self__, arn=..., bgp_asn=..., bgp_peer_address=..., bgp_transit_gateway_addresses=..., filters=..., id=..., inside_cidr_blocks=..., peer_address=..., region=..., tags=..., transit_gateway_address=..., transit_gateway_attachment_id=..., transit_gateway_connect_peer_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpPeerAddress")
    def bgp_peer_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpTransitGatewayAddresses")
    def bgp_transit_gateway_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetConnectPeerFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAddress")
    def transit_gateway_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayConnectPeerId")
    def transit_gateway_connect_peer_id(self) -> _builtins.str:
        ...
    


class AwaitableGetConnectPeerResult(GetConnectPeerResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectPeerResult]:
        ...
    


def get_connect_peer(filters: Optional[Sequence[Union[GetConnectPeerFilterArgs, GetConnectPeerFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., transit_gateway_connect_peer_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectPeerResult:
    
    ...

def get_connect_peer_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetConnectPeerFilterArgs, GetConnectPeerFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., transit_gateway_connect_peer_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectPeerResult]:
    
    ...

