

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserResult', 'AwaitableGetUserResult', 'get_user', 'get_user_output']
@pulumi.output_type
class GetUserResult:
    
    def __init__(__self__, arn=..., id=..., path=..., permissions_boundary=..., tags=..., user_id=..., user_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
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
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetUserResult(GetUserResult):
    def __await__(self): # -> Generator[Never, Any, GetUserResult]:
        ...
    


def get_user(tags: Optional[Mapping[str, _builtins.str]] = ..., user_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserResult:
    
    ...

def get_user_output(tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserResult]:
    
    ...

