

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKMSSecretAsymmetricResult', 'AwaitableGetKMSSecretAsymmetricResult', 'get_kms_secret_asymmetric', 'get_kms_secret_asymmetric_output']
@pulumi.output_type
class GetKMSSecretAsymmetricResult:
    
    def __init__(__self__, ciphertext=..., crc32=..., crypto_key_version=..., id=..., plaintext=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ciphertext(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def crc32(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyVersion")
    def crypto_key_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> _builtins.str:
        
        ...
    


class AwaitableGetKMSSecretAsymmetricResult(GetKMSSecretAsymmetricResult):
    def __await__(self): # -> Generator[Never, Any, GetKMSSecretAsymmetricResult]:
        ...
    


def get_kms_secret_asymmetric(ciphertext: Optional[_builtins.str] = ..., crc32: Optional[_builtins.str] = ..., crypto_key_version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKMSSecretAsymmetricResult:
    
    ...

def get_kms_secret_asymmetric_output(ciphertext: Optional[pulumi.Input[_builtins.str]] = ..., crc32: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., crypto_key_version: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKMSSecretAsymmetricResult]:
    
    ...

