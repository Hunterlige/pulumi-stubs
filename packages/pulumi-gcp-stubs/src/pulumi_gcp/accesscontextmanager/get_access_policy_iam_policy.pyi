import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccessPolicyIamPolicyResult",
    "AwaitableGetAccessPolicyIamPolicyResult",
    "get_access_policy_iam_policy",
    "get_access_policy_iam_policy_output",
]

@pulumi.output_type
class GetAccessPolicyIamPolicyResult:
    def __init__(__self__, etag=..., id=..., name=..., policy_data=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetAccessPolicyIamPolicyResult(GetAccessPolicyIamPolicyResult):
    def __await__(self): ...

def get_access_policy_iam_policy(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetAccessPolicyIamPolicyResult: ...
def get_access_policy_iam_policy_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccessPolicyIamPolicyResult]: ...
