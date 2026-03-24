

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserSshKeyResult', 'AwaitableGetUserSshKeyResult', 'get_user_ssh_key', 'get_user_ssh_key_output']
@pulumi.output_type
class GetUserSshKeyResult:
    
    def __init__(__self__, encoding=..., fingerprint=..., id=..., public_key=..., ssh_public_key_id=..., status=..., username=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKeyId")
    def ssh_public_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        ...
    


class AwaitableGetUserSshKeyResult(GetUserSshKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetUserSshKeyResult]:
        ...
    


def get_user_ssh_key(encoding: Optional[_builtins.str] = ..., ssh_public_key_id: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserSshKeyResult:
    
    ...

def get_user_ssh_key_output(encoding: Optional[pulumi.Input[_builtins.str]] = ..., ssh_public_key_id: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserSshKeyResult]:
    
    ...

