

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGlobalNetworksResult', 'AwaitableGetGlobalNetworksResult', 'get_global_networks', 'get_global_networks_output']
@pulumi.output_type
class GetGlobalNetworksResult:
    
    def __init__(__self__, id=..., ids=..., tags=...) -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetGlobalNetworksResult(GetGlobalNetworksResult):
    def __await__(self): # -> Generator[Never, Any, GetGlobalNetworksResult]:
        ...
    


def get_global_networks(tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGlobalNetworksResult:
    
    ...

def get_global_networks_output(tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGlobalNetworksResult]:
    
    ...

