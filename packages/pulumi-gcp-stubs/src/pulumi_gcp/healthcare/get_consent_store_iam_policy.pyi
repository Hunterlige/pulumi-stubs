import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConsentStoreIamPolicyResult",
    "AwaitableGetConsentStoreIamPolicyResult",
    "get_consent_store_iam_policy",
    "get_consent_store_iam_policy_output",
]

@pulumi.output_type
class GetConsentStoreIamPolicyResult:
    def __init__(
        __self__, consent_store_id=..., dataset=..., etag=..., id=..., policy_data=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetConsentStoreIamPolicyResult(GetConsentStoreIamPolicyResult):
    def __await__(self): ...

def get_consent_store_iam_policy(
    consent_store_id: Optional[_builtins.str] = ...,
    dataset: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConsentStoreIamPolicyResult: ...
def get_consent_store_iam_policy_output(
    consent_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    dataset: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConsentStoreIamPolicyResult]: ...
