

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
__all__ = ['GetManagedPrefixListsResult', 'AwaitableGetManagedPrefixListsResult', 'get_managed_prefix_lists', 'get_managed_prefix_lists_output']
@pulumi.output_type
class GetManagedPrefixListsResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetManagedPrefixListsFilterResult]]:
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
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetManagedPrefixListsResult(GetManagedPrefixListsResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedPrefixListsResult]:
        ...
    


def get_managed_prefix_lists(filters: Optional[Sequence[Union[GetManagedPrefixListsFilterArgs, GetManagedPrefixListsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedPrefixListsResult:
    
    ...

def get_managed_prefix_lists_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetManagedPrefixListsFilterArgs, GetManagedPrefixListsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedPrefixListsResult]:
    
    ...

