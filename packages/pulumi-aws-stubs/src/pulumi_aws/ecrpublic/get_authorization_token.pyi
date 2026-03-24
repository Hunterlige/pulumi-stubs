

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAuthorizationTokenResult', 'AwaitableGetAuthorizationTokenResult', 'get_authorization_token', 'get_authorization_token_output']
@pulumi.output_type
class GetAuthorizationTokenResult:
    
    def __init__(__self__, authorization_token=..., expires_at=..., id=..., password=..., region=..., user_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationToken")
    def authorization_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAuthorizationTokenResult(GetAuthorizationTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetAuthorizationTokenResult]:
        ...
    


def get_authorization_token(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAuthorizationTokenResult:
    
    ...

def get_authorization_token_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAuthorizationTokenResult]:
    
    ...

