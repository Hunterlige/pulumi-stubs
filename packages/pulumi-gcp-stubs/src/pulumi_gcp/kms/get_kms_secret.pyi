import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKMSSecretResult",
    "AwaitableGetKMSSecretResult",
    "get_kms_secret",
    "get_kms_secret_output",
]

@pulumi.output_type
class GetKMSSecretResult:
    def __init__(
        __self__,
        additional_authenticated_data=...,
        ciphertext=...,
        crypto_key=...,
        id=...,
        plaintext=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(self) -> Optional[_builtins.str]: ...
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

class AwaitableGetKMSSecretResult(GetKMSSecretResult):
    def __await__(self): ...

def get_kms_secret(
    additional_authenticated_data: Optional[_builtins.str] = ...,
    ciphertext: Optional[_builtins.str] = ...,
    crypto_key: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKMSSecretResult: ...
def get_kms_secret_output(
    additional_authenticated_data: Optional[
        pulumi.Input[Optional[_builtins.str]]
    ] = ...,
    ciphertext: Optional[pulumi.Input[_builtins.str]] = ...,
    crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKMSSecretResult]: ...
