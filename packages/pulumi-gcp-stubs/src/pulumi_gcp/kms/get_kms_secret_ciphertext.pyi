import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKMSSecretCiphertextResult",
    "AwaitableGetKMSSecretCiphertextResult",
    "get_kms_secret_ciphertext",
    "get_kms_secret_ciphertext_output",
]

@pulumi.output_type
class GetKMSSecretCiphertextResult:
    def __init__(
        __self__, ciphertext=..., crypto_key=..., id=..., plaintext=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ciphertext(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> _builtins.str: ...

class AwaitableGetKMSSecretCiphertextResult(GetKMSSecretCiphertextResult):
    def __await__(self): ...

def get_kms_secret_ciphertext(
    crypto_key: Optional[_builtins.str] = ...,
    plaintext: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKMSSecretCiphertextResult: ...
def get_kms_secret_ciphertext_output(
    crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
    plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKMSSecretCiphertextResult]: ...
