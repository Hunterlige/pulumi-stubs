

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserGroupResult', 'AwaitableGetUserGroupResult', 'get_user_group', 'get_user_group_output']
@pulumi.output_type
class GetUserGroupResult:
    
    def __init__(__self__, description=..., id=..., name=..., precedence=..., region=..., role_arn=..., user_pool_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter
    def precedence(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        ...
    


class AwaitableGetUserGroupResult(GetUserGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetUserGroupResult]:
        ...
    


def get_user_group(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., user_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserGroupResult:
    
    ...

def get_user_group_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserGroupResult]:
    
    ...

