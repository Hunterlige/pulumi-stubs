

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGroupsResult', 'AwaitableGetGroupsResult', 'get_groups', 'get_groups_output']
@pulumi.output_type
class GetGroupsResult:
    
    def __init__(__self__, groups=..., id=..., identity_store_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[outputs.GetGroupsGroupResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetGroupsResult(GetGroupsResult):
    def __await__(self): # -> Generator[Never, Any, GetGroupsResult]:
        ...
    


def get_groups(identity_store_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGroupsResult:
    
    ...

def get_groups_output(identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGroupsResult]:
    
    ...

