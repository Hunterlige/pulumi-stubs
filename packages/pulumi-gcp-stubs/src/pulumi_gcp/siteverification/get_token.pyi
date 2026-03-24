

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTokenResult', 'AwaitableGetTokenResult', 'get_token', 'get_token_output']
@pulumi.output_type
class GetTokenResult:
    
    def __init__(__self__, id=..., identifier=..., token=..., type=..., verification_method=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationMethod")
    def verification_method(self) -> _builtins.str:
        ...
    


class AwaitableGetTokenResult(GetTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetTokenResult]:
        ...
    


def get_token(identifier: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., verification_method: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTokenResult:
    
    ...

def get_token_output(identifier: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., verification_method: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTokenResult]:
    
    ...

