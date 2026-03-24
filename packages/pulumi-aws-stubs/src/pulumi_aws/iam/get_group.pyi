

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGroupResult', 'AwaitableGetGroupResult', 'get_group', 'get_group_output']
@pulumi.output_type
class GetGroupResult:
    
    def __init__(__self__, arn=..., group_id=..., group_name=..., id=..., path=..., users=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Sequence[outputs.GetGroupUserResult]:
        
        ...
    


class AwaitableGetGroupResult(GetGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetGroupResult]:
        ...
    


def get_group(group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGroupResult:
    
    ...

def get_group_output(group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGroupResult]:
    
    ...

