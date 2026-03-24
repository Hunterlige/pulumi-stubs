

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRateBasedModResult', 'AwaitableGetRateBasedModResult', 'get_rate_based_mod', 'get_rate_based_mod_output']
@pulumi.output_type
class GetRateBasedModResult:
    
    def __init__(__self__, id=..., name=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetRateBasedModResult(GetRateBasedModResult):
    def __await__(self): # -> Generator[Never, Any, GetRateBasedModResult]:
        ...
    


def get_rate_based_mod(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRateBasedModResult:
    
    ...

def get_rate_based_mod_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRateBasedModResult]:
    
    ...

