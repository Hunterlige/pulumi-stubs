import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIamPolicyResult",
    "AwaitableGetIamPolicyResult",
    "get_iam_policy",
    "get_iam_policy_output",
]

@pulumi.output_type
class GetIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., policy_data=..., service_account_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> _builtins.str: ...

class AwaitableGetIamPolicyResult(GetIamPolicyResult):
    def __await__(self): ...

def get_iam_policy(
    service_account_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIamPolicyResult: ...
def get_iam_policy_output(
    service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIamPolicyResult]: ...
