import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNoteIamPolicyResult",
    "AwaitableGetNoteIamPolicyResult",
    "get_note_iam_policy",
    "get_note_iam_policy_output",
]

@pulumi.output_type
class GetNoteIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., note=..., policy_data=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def note(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetNoteIamPolicyResult(GetNoteIamPolicyResult):
    def __await__(self): ...

def get_note_iam_policy(
    note: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNoteIamPolicyResult: ...
def get_note_iam_policy_output(
    note: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNoteIamPolicyResult]: ...
