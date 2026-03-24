import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScopeIamPolicyResult",
    "AwaitableGetScopeIamPolicyResult",
    "get_scope_iam_policy",
    "get_scope_iam_policy_output",
]

@pulumi.output_type
class GetScopeIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., policy_data=..., project=..., scope_id=...
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
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> _builtins.str: ...

class AwaitableGetScopeIamPolicyResult(GetScopeIamPolicyResult):
    def __await__(self): ...

def get_scope_iam_policy(
    project: Optional[_builtins.str] = ...,
    scope_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScopeIamPolicyResult: ...
def get_scope_iam_policy_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScopeIamPolicyResult]: ...
