import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCryptoKeyIamPolicyResult",
    "AwaitableGetCryptoKeyIamPolicyResult",
    "get_crypto_key_iam_policy",
    "get_crypto_key_iam_policy_output",
]

@pulumi.output_type
class GetCryptoKeyIamPolicyResult:
    def __init__(
        __self__, crypto_key_id=..., etag=..., id=..., policy_data=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyId")
    def crypto_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetCryptoKeyIamPolicyResult(GetCryptoKeyIamPolicyResult):
    def __await__(self): ...

def get_crypto_key_iam_policy(
    crypto_key_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCryptoKeyIamPolicyResult: ...
def get_crypto_key_iam_policy_output(
    crypto_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCryptoKeyIamPolicyResult]: ...
