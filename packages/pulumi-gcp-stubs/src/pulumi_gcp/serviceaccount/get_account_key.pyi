

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountKeyResult', 'AwaitableGetAccountKeyResult', 'get_account_key', 'get_account_key_output']
@pulumi.output_type
class GetAccountKeyResult:
    
    def __init__(__self__, id=..., key_algorithm=..., name=..., public_key=..., public_key_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetAccountKeyResult(GetAccountKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountKeyResult]:
        ...
    


def get_account_key(name: Optional[_builtins.str] = ..., public_key_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountKeyResult:
    
    ...

def get_account_key_output(name: Optional[pulumi.Input[_builtins.str]] = ..., public_key_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountKeyResult]:
    
    ...

