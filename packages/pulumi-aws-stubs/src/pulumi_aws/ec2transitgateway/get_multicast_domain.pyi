

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
__all__ = ['GetMulticastDomainResult', 'AwaitableGetMulticastDomainResult', 'get_multicast_domain', 'get_multicast_domain_output']
@pulumi.output_type
class GetMulticastDomainResult:
    
    def __init__(__self__, arn=..., associations=..., auto_accept_shared_associations=..., filters=..., id=..., igmpv2_support=..., members=..., owner_id=..., region=..., sources=..., state=..., static_sources_support=..., tags=..., transit_gateway_attachment_id=..., transit_gateway_id=..., transit_gateway_multicast_domain_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Sequence[outputs.GetMulticastDomainAssociationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoAcceptSharedAssociations")
    def auto_accept_shared_associations(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetMulticastDomainFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="igmpv2Support")
    def igmpv2_support(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[outputs.GetMulticastDomainMemberResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetMulticastDomainSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticSourcesSupport")
    def static_sources_support(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> _builtins.str:
        ...
    


class AwaitableGetMulticastDomainResult(GetMulticastDomainResult):
    def __await__(self): # -> Generator[Never, Any, GetMulticastDomainResult]:
        ...
    


def get_multicast_domain(filters: Optional[Sequence[Union[GetMulticastDomainFilterArgs, GetMulticastDomainFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., transit_gateway_multicast_domain_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMulticastDomainResult:
    
    ...

def get_multicast_domain_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetMulticastDomainFilterArgs, GetMulticastDomainFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., transit_gateway_multicast_domain_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMulticastDomainResult]:
    
    ...

