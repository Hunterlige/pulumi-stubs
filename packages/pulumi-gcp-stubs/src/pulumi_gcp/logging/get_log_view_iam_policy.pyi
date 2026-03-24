import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLogViewIamPolicyResult",
    "AwaitableGetLogViewIamPolicyResult",
    "get_log_view_iam_policy",
    "get_log_view_iam_policy_output",
]

@pulumi.output_type
class GetLogViewIamPolicyResult:
    def __init__(
        __self__,
        bucket=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        parent=...,
        policy_data=...,
    ) -> None: ...
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
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetLogViewIamPolicyResult(GetLogViewIamPolicyResult):
    def __await__(self): ...

def get_log_view_iam_policy(
    bucket: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLogViewIamPolicyResult: ...
def get_log_view_iam_policy_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLogViewIamPolicyResult]: ...
