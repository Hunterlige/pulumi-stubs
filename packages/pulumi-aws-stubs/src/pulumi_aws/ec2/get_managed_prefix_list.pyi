

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
__all__ = ['GetManagedPrefixListResult', 'AwaitableGetManagedPrefixListResult', 'get_managed_prefix_list', 'get_managed_prefix_list_output']
@pulumi.output_type
class GetManagedPrefixListResult:
    
    def __init__(__self__, address_family=..., arn=..., entries=..., filters=..., id=..., max_entries=..., name=..., owner_id=..., region=..., tags=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entries(self) -> Sequence[outputs.GetManagedPrefixListEntryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetManagedPrefixListFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        ...
    


class AwaitableGetManagedPrefixListResult(GetManagedPrefixListResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedPrefixListResult]:
        ...
    


def get_managed_prefix_list(filters: Optional[Sequence[Union[GetManagedPrefixListFilterArgs, GetManagedPrefixListFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedPrefixListResult:
    
    ...

def get_managed_prefix_list_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetManagedPrefixListFilterArgs, GetManagedPrefixListFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedPrefixListResult]:
    
    ...

