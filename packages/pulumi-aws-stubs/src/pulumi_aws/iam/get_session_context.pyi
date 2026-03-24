

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSessionContextResult', 'AwaitableGetSessionContextResult', 'get_session_context', 'get_session_context_output']
@pulumi.output_type
class GetSessionContextResult:
    
    def __init__(__self__, arn=..., id=..., issuer_arn=..., issuer_id=..., issuer_name=..., session_name=...) -> None:
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
    @pulumi.getter(name="issuerArn")
    def issuer_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerId")
    def issuer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerName")
    def issuer_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionName")
    def session_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSessionContextResult(GetSessionContextResult):
    def __await__(self): # -> Generator[Never, Any, GetSessionContextResult]:
        ...
    


def get_session_context(arn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSessionContextResult:
    
    ...

def get_session_context_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSessionContextResult]:
    
    ...

