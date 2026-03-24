import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCryptoKeyVersionsResult",
    "AwaitableGetCryptoKeyVersionsResult",
    "get_crypto_key_versions",
    "get_crypto_key_versions_output",
]

@pulumi.output_type
class GetCryptoKeyVersionsResult:
    def __init__(
        __self__, crypto_key=..., filter=..., id=..., public_keys=..., versions=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Sequence[outputs.GetCryptoKeyVersionsPublicKeyResult]: ...
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[outputs.GetCryptoKeyVersionsVersionResult]: ...

class AwaitableGetCryptoKeyVersionsResult(GetCryptoKeyVersionsResult):
    def __await__(self): ...

def get_crypto_key_versions(
    crypto_key: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCryptoKeyVersionsResult: ...
def get_crypto_key_versions_output(
    crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCryptoKeyVersionsResult]: ...
