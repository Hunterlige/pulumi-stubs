

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCryptoKeyLatestVersionResult', 'AwaitableGetCryptoKeyLatestVersionResult', 'get_crypto_key_latest_version', 'get_crypto_key_latest_version_output']
@pulumi.output_type
class GetCryptoKeyLatestVersionResult:
    
    def __init__(__self__, algorithm=..., crypto_key=..., filter=..., id=..., name=..., protection_level=..., public_keys=..., state=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> _builtins.str:
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Sequence[outputs.GetCryptoKeyLatestVersionPublicKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        ...
    


class AwaitableGetCryptoKeyLatestVersionResult(GetCryptoKeyLatestVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetCryptoKeyLatestVersionResult]:
        ...
    


def get_crypto_key_latest_version(crypto_key: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCryptoKeyLatestVersionResult:
    
    ...

def get_crypto_key_latest_version_output(crypto_key: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCryptoKeyLatestVersionResult]:
    
    ...

