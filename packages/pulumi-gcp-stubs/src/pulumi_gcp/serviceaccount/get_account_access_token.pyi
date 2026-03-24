

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountAccessTokenResult', 'AwaitableGetAccountAccessTokenResult', 'get_account_access_token', 'get_account_access_token_output']
@pulumi.output_type
class GetAccountAccessTokenResult:
    
    def __init__(__self__, access_token=..., delegates=..., id=..., lifetime=..., scopes=..., target_service_account=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegates(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccount")
    def target_service_account(self) -> _builtins.str:
        ...
    


class AwaitableGetAccountAccessTokenResult(GetAccountAccessTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountAccessTokenResult]:
        ...
    


def get_account_access_token(delegates: Optional[Sequence[_builtins.str]] = ..., lifetime: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., target_service_account: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountAccessTokenResult:
    
    ...

def get_account_access_token_output(delegates: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., lifetime: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., scopes: Optional[pulumi.Input[Sequence[_builtins.str]]] = ..., target_service_account: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountAccessTokenResult]:
    
    ...

