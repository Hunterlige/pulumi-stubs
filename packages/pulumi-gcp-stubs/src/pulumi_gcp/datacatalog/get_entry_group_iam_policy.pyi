import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEntryGroupIamPolicyResult",
    "AwaitableGetEntryGroupIamPolicyResult",
    "get_entry_group_iam_policy",
    "get_entry_group_iam_policy_output",
]

@pulumi.output_type
class GetEntryGroupIamPolicyResult:
    def __init__(
        __self__,
        entry_group=...,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryGroup")
    def entry_group(self) -> _builtins.str: ...
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
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetEntryGroupIamPolicyResult(GetEntryGroupIamPolicyResult):
    def __await__(self): ...

def get_entry_group_iam_policy(
    entry_group: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEntryGroupIamPolicyResult: ...
def get_entry_group_iam_policy_output(
    entry_group: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEntryGroupIamPolicyResult]: ...
