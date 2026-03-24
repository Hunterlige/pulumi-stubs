

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
__all__ = ['GetPrefixListResult', 'AwaitableGetPrefixListResult', 'get_prefix_list', 'get_prefix_list_output']
@pulumi.output_type
class GetPrefixListResult:
    
    def __init__(__self__, cidr_blocks=..., filters=..., id=..., name=..., prefix_list_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetPrefixListFilterResult]]:
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
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetPrefixListResult(GetPrefixListResult):
    def __await__(self): # -> Generator[Never, Any, GetPrefixListResult]:
        ...
    


def get_prefix_list(filters: Optional[Sequence[Union[GetPrefixListFilterArgs, GetPrefixListFilterArgsDict]]] = ..., name: Optional[_builtins.str] = ..., prefix_list_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrefixListResult:
    
    ...

def get_prefix_list_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetPrefixListFilterArgs, GetPrefixListFilterArgsDict]]]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., prefix_list_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrefixListResult]:
    
    ...

