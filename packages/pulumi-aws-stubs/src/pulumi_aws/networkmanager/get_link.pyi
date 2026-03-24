

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLinkResult', 'AwaitableGetLinkResult', 'get_link', 'get_link_output']
@pulumi.output_type
class GetLinkResult:
    
    def __init__(__self__, arn=..., bandwidths=..., description=..., global_network_id=..., id=..., link_id=..., provider_name=..., site_id=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bandwidths(self) -> Sequence[outputs.GetLinkBandwidthResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkId")
    def link_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLinkResult(GetLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetLinkResult]:
        ...
    


def get_link(global_network_id: Optional[_builtins.str] = ..., link_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLinkResult:
    
    ...

def get_link_output(global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., link_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLinkResult]:
    
    ...

