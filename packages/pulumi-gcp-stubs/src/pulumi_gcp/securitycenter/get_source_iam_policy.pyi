import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSourceIamPolicyResult",
    "AwaitableGetSourceIamPolicyResult",
    "get_source_iam_policy",
    "get_source_iam_policy_output",
]

@pulumi.output_type
class GetSourceIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., organization=..., policy_data=..., source=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...

class AwaitableGetSourceIamPolicyResult(GetSourceIamPolicyResult):
    def __await__(self): ...

def get_source_iam_policy(
    organization: Optional[_builtins.str] = ...,
    source: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSourceIamPolicyResult: ...
def get_source_iam_policy_output(
    organization: Optional[pulumi.Input[_builtins.str]] = ...,
    source: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSourceIamPolicyResult]: ...
