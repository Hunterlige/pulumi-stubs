

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountJwtResult', 'AwaitableGetAccountJwtResult', 'get_account_jwt', 'get_account_jwt_output']
@pulumi.output_type
class GetAccountJwtResult:
    
    def __init__(__self__, delegates=..., expires_in=..., id=..., jwt=..., payload=..., target_service_account=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegates(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresIn")
    def expires_in(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def jwt(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccount")
    def target_service_account(self) -> _builtins.str:
        ...
    


class AwaitableGetAccountJwtResult(GetAccountJwtResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountJwtResult]:
        ...
    


def get_account_jwt(delegates: Optional[Sequence[_builtins.str]] = ..., expires_in: Optional[_builtins.int] = ..., payload: Optional[_builtins.str] = ..., target_service_account: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountJwtResult:
    
    ...

def get_account_jwt_output(delegates: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., expires_in: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., target_service_account: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountJwtResult]:
    
    ...

