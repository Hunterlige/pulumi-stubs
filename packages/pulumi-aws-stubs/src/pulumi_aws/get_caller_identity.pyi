

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCallerIdentityResult', 'AwaitableGetCallerIdentityResult', 'get_caller_identity', 'get_caller_identity_output']
@pulumi.output_type
class GetCallerIdentityResult:
    
    def __init__(__self__, account_id=..., arn=..., id=..., user_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCallerIdentityResult(GetCallerIdentityResult):
    def __await__(self): # -> Generator[Never, Any, GetCallerIdentityResult]:
        ...
    


def get_caller_identity(id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCallerIdentityResult:
    
    ...

def get_caller_identity_output(id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCallerIdentityResult]:
    
    ...

