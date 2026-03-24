

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProtectionResult', 'AwaitableGetProtectionResult', 'get_protection', 'get_protection_output']
@pulumi.output_type
class GetProtectionResult:
    
    def __init__(__self__, id=..., name=..., protection_arn=..., protection_id=..., resource_arn=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionArn")
    def protection_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionId")
    def protection_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        ...
    


class AwaitableGetProtectionResult(GetProtectionResult):
    def __await__(self): # -> Generator[Never, Any, GetProtectionResult]:
        ...
    


def get_protection(protection_id: Optional[_builtins.str] = ..., resource_arn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProtectionResult:
    
    ...

def get_protection_output(protection_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProtectionResult]:
    
    ...

