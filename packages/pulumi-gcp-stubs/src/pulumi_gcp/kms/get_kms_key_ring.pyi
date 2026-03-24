

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKMSKeyRingResult', 'AwaitableGetKMSKeyRingResult', 'get_kms_key_ring', 'get_kms_key_ring_output']
@pulumi.output_type
class GetKMSKeyRingResult:
    
    def __init__(__self__, id=..., location=..., name=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetKMSKeyRingResult(GetKMSKeyRingResult):
    def __await__(self): # -> Generator[Never, Any, GetKMSKeyRingResult]:
        ...
    


def get_kms_key_ring(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKMSKeyRingResult:
    
    ...

def get_kms_key_ring_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKMSKeyRingResult]:
    
    ...

