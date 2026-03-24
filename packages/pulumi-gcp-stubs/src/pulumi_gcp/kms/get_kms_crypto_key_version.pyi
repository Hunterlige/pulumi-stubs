import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKMSCryptoKeyVersionResult",
    "AwaitableGetKMSCryptoKeyVersionResult",
    "get_kms_crypto_key_version",
    "get_kms_crypto_key_version_output",
]

@pulumi.output_type
class GetKMSCryptoKeyVersionResult:
    def __init__(
        __self__,
        algorithm=...,
        crypto_key=...,
        id=...,
        name=...,
        protection_level=...,
        public_keys=...,
        state=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Sequence[outputs.GetKMSCryptoKeyVersionPublicKeyResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]: ...

class AwaitableGetKMSCryptoKeyVersionResult(GetKMSCryptoKeyVersionResult):
    def __await__(self): ...

def get_kms_crypto_key_version(
    crypto_key: Optional[_builtins.str] = ...,
    version: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKMSCryptoKeyVersionResult: ...
def get_kms_crypto_key_version_output(
    crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKMSCryptoKeyVersionResult]: ...
