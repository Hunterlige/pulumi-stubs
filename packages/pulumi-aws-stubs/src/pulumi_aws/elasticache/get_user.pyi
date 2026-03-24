

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserResult', 'AwaitableGetUserResult', 'get_user', 'get_user_output']
@pulumi.output_type
class GetUserResult:
    
    def __init__(__self__, access_string=..., authentication_modes=..., engine=..., id=..., no_password_required=..., passwords=..., region=..., user_id=..., user_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessString")
    def access_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationModes")
    def authentication_modes(self) -> Optional[Sequence[outputs.GetUserAuthenticationModeResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noPasswordRequired")
    def no_password_required(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetUserResult(GetUserResult):
    def __await__(self): # -> Generator[Never, Any, GetUserResult]:
        ...
    


def get_user(access_string: Optional[_builtins.str] = ..., authentication_modes: Optional[Sequence[Union[GetUserAuthenticationModeArgs, GetUserAuthenticationModeArgsDict]]] = ..., engine: Optional[_builtins.str] = ..., no_password_required: Optional[_builtins.bool] = ..., passwords: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., user_id: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserResult:
    
    ...

def get_user_output(access_string: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., authentication_modes: Optional[pulumi.Input[Optional[Sequence[Union[GetUserAuthenticationModeArgs, GetUserAuthenticationModeArgsDict]]]]] = ..., engine: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., no_password_required: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., passwords: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserResult]:
    
    ...

