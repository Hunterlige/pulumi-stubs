

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserGroupsResult', 'AwaitableGetUserGroupsResult', 'get_user_groups', 'get_user_groups_output']
@pulumi.output_type
class GetUserGroupsResult:
    
    def __init__(__self__, groups=..., id=..., region=..., user_pool_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[outputs.GetUserGroupsGroupResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        ...
    


class AwaitableGetUserGroupsResult(GetUserGroupsResult):
    def __await__(self): # -> Generator[Never, Any, GetUserGroupsResult]:
        ...
    


def get_user_groups(region: Optional[_builtins.str] = ..., user_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserGroupsResult:
    
    ...

def get_user_groups_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserGroupsResult]:
    
    ...

