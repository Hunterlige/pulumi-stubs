

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUsersResult', 'AwaitableGetUsersResult', 'get_users', 'get_users_output']
@pulumi.output_type
class GetUsersResult:
    
    def __init__(__self__, arns=..., id=..., name_regex=..., names=..., path_prefix=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetUsersResult(GetUsersResult):
    def __await__(self): # -> Generator[Never, Any, GetUsersResult]:
        ...
    


def get_users(name_regex: Optional[_builtins.str] = ..., path_prefix: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUsersResult:
    
    ...

def get_users_output(name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., path_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUsersResult]:
    
    ...

