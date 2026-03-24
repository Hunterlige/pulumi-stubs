

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpcPeeringConnectionResult', 'AwaitableGetVpcPeeringConnectionResult', 'get_vpc_peering_connection', 'get_vpc_peering_connection_output']
@pulumi.output_type
class GetVpcPeeringConnectionResult:
    
    def __init__(__self__, accepter=..., cidr_block=..., cidr_block_sets=..., filters=..., id=..., ipv6_cidr_block_sets=..., owner_id=..., peer_cidr_block=..., peer_cidr_block_sets=..., peer_ipv6_cidr_block_sets=..., peer_owner_id=..., peer_region=..., peer_vpc_id=..., region=..., requester=..., requester_region=..., status=..., tags=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepter(self) -> Mapping[str, _builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlockSets")
    def cidr_block_sets(self) -> Sequence[outputs.GetVpcPeeringConnectionCidrBlockSetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcPeeringConnectionFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockSets")
    def ipv6_cidr_block_sets(self) -> Sequence[outputs.GetVpcPeeringConnectionIpv6CidrBlockSetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerCidrBlock")
    def peer_cidr_block(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerCidrBlockSets")
    def peer_cidr_block_sets(self) -> Sequence[outputs.GetVpcPeeringConnectionPeerCidrBlockSetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv6CidrBlockSets")
    def peer_ipv6_cidr_block_sets(self) -> Sequence[outputs.GetVpcPeeringConnectionPeerIpv6CidrBlockSetResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerOwnerId")
    def peer_owner_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerRegion")
    def peer_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requester(self) -> Mapping[str, _builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterRegion")
    def requester_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        ...
    


class AwaitableGetVpcPeeringConnectionResult(GetVpcPeeringConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcPeeringConnectionResult]:
        ...
    


def get_vpc_peering_connection(cidr_block: Optional[_builtins.str] = ..., filters: Optional[Sequence[Union[GetVpcPeeringConnectionFilterArgs, GetVpcPeeringConnectionFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., owner_id: Optional[_builtins.str] = ..., peer_cidr_block: Optional[_builtins.str] = ..., peer_owner_id: Optional[_builtins.str] = ..., peer_vpc_id: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcPeeringConnectionResult:
    
    ...

def get_vpc_peering_connection_output(cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpcPeeringConnectionFilterArgs, GetVpcPeeringConnectionFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., peer_cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., peer_owner_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., peer_vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., status: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcPeeringConnectionResult]:
    
    ...

