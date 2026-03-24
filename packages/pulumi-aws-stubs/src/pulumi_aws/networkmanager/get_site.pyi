

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSiteResult', 'AwaitableGetSiteResult', 'get_site', 'get_site_output']
@pulumi.output_type
class GetSiteResult:
    
    def __init__(__self__, arn=..., description=..., global_network_id=..., id=..., locations=..., site_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
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
    @pulumi.getter
    def locations(self) -> Sequence[outputs.GetSiteLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetSiteResult(GetSiteResult):
    def __await__(self): # -> Generator[Never, Any, GetSiteResult]:
        ...
    


def get_site(global_network_id: Optional[_builtins.str] = ..., site_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSiteResult:
    
    ...

def get_site_output(global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSiteResult]:
    
    ...

