

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionsResult', 'AwaitableGetRegionsResult', 'get_regions', 'get_regions_output']
@pulumi.output_type
class GetRegionsResult:
    
    def __init__(__self__, all_regions=..., filters=..., id=..., names=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allRegions")
    def all_regions(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetRegionsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetRegionsResult(GetRegionsResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionsResult]:
        ...
    


def get_regions(all_regions: Optional[_builtins.bool] = ..., filters: Optional[Sequence[Union[GetRegionsFilterArgs, GetRegionsFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionsResult:
    
    ...

def get_regions_output(all_regions: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetRegionsFilterArgs, GetRegionsFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionsResult]:
    
    ...

