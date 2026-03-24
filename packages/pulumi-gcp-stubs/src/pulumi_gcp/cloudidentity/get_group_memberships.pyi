

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
    
    def __init__(__self__, group=..., id=..., memberships=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memberships(self) -> Sequence[outputs.GetGroupMembershipsMembershipResult]:
        
        ...
    


class AwaitableGetGroupMembershipsResult(GetGroupMembershipsResult):
    def __await__(self): # -> Generator[Never, Any, GetGroupMembershipsResult]:
        ...
    


def get_group_memberships(group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGroupMembershipsResult:
    
    ...

def get_group_memberships_output(group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGroupMembershipsResult]:
    
    ...

