

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionResult', 'AwaitableGetRegionResult', 'get_region', 'get_region_output']
@pulumi.output_type
class GetRegionResult:
    
    def __init__(__self__, description=..., endpoint=..., id=..., name=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""name is deprecated. Use region instead.""")
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetRegionResult(GetRegionResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionResult]:
        ...
    


def get_region(endpoint: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionResult:
    
    ...

def get_region_output(endpoint: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionResult]:
    
    ...

