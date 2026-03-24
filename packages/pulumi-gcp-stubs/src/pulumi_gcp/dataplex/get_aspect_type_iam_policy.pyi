import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAspectTypeIamPolicyResult",
    "AwaitableGetAspectTypeIamPolicyResult",
    "get_aspect_type_iam_policy",
    "get_aspect_type_iam_policy_output",
]

@pulumi.output_type
class GetAspectTypeIamPolicyResult:
    def __init__(
        __self__,
        aspect_type_id=...,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aspectTypeId")
    def aspect_type_id(self) -> _builtins.str: ...
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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetAspectTypeIamPolicyResult(GetAspectTypeIamPolicyResult):
    def __await__(self): ...

def get_aspect_type_iam_policy(
    aspect_type_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAspectTypeIamPolicyResult: ...
def get_aspect_type_iam_policy_output(
    aspect_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAspectTypeIamPolicyResult]: ...
