

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
__all__ = ['GetAmiIdsResult', 'AwaitableGetAmiIdsResult', 'get_ami_ids', 'get_ami_ids_output']
@pulumi.output_type
class GetAmiIdsResult:
    
    def __init__(__self__, executable_users=..., filters=..., id=..., ids=..., include_deprecated=..., name_regex=..., owners=..., region=..., sort_ascending=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executableUsers")
    def executable_users(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAmiIdsFilterResult]]:
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
    @pulumi.getter(name="includeDeprecated")
    def include_deprecated(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortAscending")
    def sort_ascending(self) -> Optional[_builtins.bool]:
        ...
    


class AwaitableGetAmiIdsResult(GetAmiIdsResult):
    def __await__(self): # -> Generator[Never, Any, GetAmiIdsResult]:
        ...
    


def get_ami_ids(executable_users: Optional[Sequence[_builtins.str]] = ..., filters: Optional[Sequence[Union[GetAmiIdsFilterArgs, GetAmiIdsFilterArgsDict]]] = ..., include_deprecated: Optional[_builtins.bool] = ..., name_regex: Optional[_builtins.str] = ..., owners: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., sort_ascending: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAmiIdsResult:
    
    ...

def get_ami_ids_output(executable_users: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetAmiIdsFilterArgs, GetAmiIdsFilterArgsDict]]]]] = ..., include_deprecated: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owners: Optional[pulumi.Input[Sequence[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., sort_ascending: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAmiIdsResult]:
    
    ...

