

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLinksResult', 'AwaitableGetLinksResult', 'get_links', 'get_links_output']
@pulumi.output_type
class GetLinksResult:
    
    def __init__(__self__, global_network_id=..., id=..., ids=..., provider_name=..., site_id=..., tags=..., type=...) -> None:
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
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetLinksResult(GetLinksResult):
    def __await__(self): # -> Generator[Never, Any, GetLinksResult]:
        ...
    


def get_links(global_network_id: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., site_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLinksResult:
    
    ...

def get_links_output(global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., provider_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., site_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLinksResult]:
    
    ...

