

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
__all__ = ['GetCoipPoolsResult', 'AwaitableGetCoipPoolsResult', 'get_coip_pools', 'get_coip_pools_output']
@pulumi.output_type
class GetCoipPoolsResult:
    
    def __init__(__self__, filters=..., id=..., pool_ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetCoipPoolsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolIds")
    def pool_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetCoipPoolsResult(GetCoipPoolsResult):
    def __await__(self): # -> Generator[Never, Any, GetCoipPoolsResult]:
        ...
    


def get_coip_pools(filters: Optional[Sequence[Union[GetCoipPoolsFilterArgs, GetCoipPoolsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCoipPoolsResult:
    
    ...

def get_coip_pools_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetCoipPoolsFilterArgs, GetCoipPoolsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCoipPoolsResult]:
    
    ...

