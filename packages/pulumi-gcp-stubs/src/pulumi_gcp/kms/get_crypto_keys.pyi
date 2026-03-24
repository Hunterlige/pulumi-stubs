

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCryptoKeysResult', 'AwaitableGetCryptoKeysResult', 'get_crypto_keys', 'get_crypto_keys_output']
@pulumi.output_type
class GetCryptoKeysResult:
    
    def __init__(__self__, filter=..., id=..., key_ring=..., keys=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[outputs.GetCryptoKeysKeyResult]:
        
        ...
    


class AwaitableGetCryptoKeysResult(GetCryptoKeysResult):
    def __await__(self): # -> Generator[Never, Any, GetCryptoKeysResult]:
        ...
    


def get_crypto_keys(filter: Optional[_builtins.str] = ..., key_ring: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCryptoKeysResult:
    
    ...

def get_crypto_keys_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., key_ring: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCryptoKeysResult]:
    
    ...

