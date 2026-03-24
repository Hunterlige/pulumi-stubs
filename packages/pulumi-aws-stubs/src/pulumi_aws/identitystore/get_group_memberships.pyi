

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGroupMembershipsResult', 'AwaitableGetGroupMembershipsResult', 'get_group_memberships', 'get_group_memberships_output']
@pulumi.output_type
class GetGroupMembershipsResult:
    
    def __init__(__self__, group_id=..., group_memberships=..., id=..., identity_store_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupMemberships")
    def group_memberships(self) -> Sequence[outputs.GetGroupMembershipsGroupMembershipResult]:
        
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
    


class AwaitableGetGroupMembershipsResult(GetGroupMembershipsResult):
    def __await__(self): # -> Generator[Never, Any, GetGroupMembershipsResult]:
        ...
    


def get_group_memberships(group_id: Optional[_builtins.str] = ..., identity_store_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGroupMembershipsResult:
    
    ...

def get_group_memberships_output(group_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGroupMembershipsResult]:
    
    ...

