

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetArnResult', 'AwaitableGetArnResult', 'get_arn', 'get_arn_output']
@pulumi.output_type
class GetArnResult:
    
    def __init__(__self__, account=..., arn=..., id=..., partition=..., region=..., resource=..., service=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> _builtins.str:
        
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
    @pulumi.getter
    def partition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


class AwaitableGetArnResult(GetArnResult):
    def __await__(self): # -> Generator[Never, Any, GetArnResult]:
        ...
    


def get_arn(arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetArnResult:
    
    ...

def get_arn_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetArnResult]:
    
    ...

