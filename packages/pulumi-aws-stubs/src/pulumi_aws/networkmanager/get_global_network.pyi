

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGlobalNetworkResult', 'AwaitableGetGlobalNetworkResult', 'get_global_network', 'get_global_network_output']
@pulumi.output_type
class GetGlobalNetworkResult:
    
    def __init__(__self__, arn=..., description=..., global_network_id=..., id=..., tags=...) -> None:
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
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetGlobalNetworkResult(GetGlobalNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetGlobalNetworkResult]:
        ...
    


def get_global_network(global_network_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGlobalNetworkResult:
    
    ...

def get_global_network_output(global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGlobalNetworkResult]:
    
    ...

