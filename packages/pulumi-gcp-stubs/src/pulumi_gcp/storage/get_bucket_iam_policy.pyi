import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBucketIamPolicyResult",
    "AwaitableGetBucketIamPolicyResult",
    "get_bucket_iam_policy",
    "get_bucket_iam_policy_output",
]

@pulumi.output_type
class GetBucketIamPolicyResult:
    def __init__(__self__, bucket=..., etag=..., id=..., policy_data=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetBucketIamPolicyResult(GetBucketIamPolicyResult):
    def __await__(self): ...

def get_bucket_iam_policy(
    bucket: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetBucketIamPolicyResult: ...
def get_bucket_iam_policy_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBucketIamPolicyResult]: ...
