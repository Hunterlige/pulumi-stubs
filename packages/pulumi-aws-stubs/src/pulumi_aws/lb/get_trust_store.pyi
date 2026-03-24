

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTrustStoreResult', 'AwaitableGetTrustStoreResult', 'get_trust_store', 'get_trust_store_output']
@pulumi.output_type
class GetTrustStoreResult:
    
    def __init__(__self__, arn=..., id=..., name=..., region=...) -> None:
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
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetTrustStoreResult(GetTrustStoreResult):
    def __await__(self): # -> Generator[Never, Any, GetTrustStoreResult]:
        ...
    


def get_trust_store(arn: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTrustStoreResult:
    
    ...

def get_trust_store_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTrustStoreResult]:
    
    ...

