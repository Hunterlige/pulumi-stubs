

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCipherTextResult', 'AwaitableGetCipherTextResult', 'get_cipher_text', 'get_cipher_text_output']
@pulumi.output_type
class GetCipherTextResult:
    
    def __init__(__self__, ciphertext_blob=..., context=..., id=..., key_id=..., plaintext=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ciphertextBlob")
    def ciphertext_blob(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetCipherTextResult(GetCipherTextResult):
    def __await__(self): # -> Generator[Never, Any, GetCipherTextResult]:
        ...
    


def get_cipher_text(context: Optional[Mapping[str, _builtins.str]] = ..., key_id: Optional[_builtins.str] = ..., plaintext: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCipherTextResult:
    
    ...

def get_cipher_text_output(context: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., key_id: Optional[pulumi.Input[_builtins.str]] = ..., plaintext: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCipherTextResult]:
    
    ...

