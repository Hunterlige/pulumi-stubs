import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebIamPolicyResult",
    "AwaitableGetWebIamPolicyResult",
    "get_web_iam_policy",
    "get_web_iam_policy_output",
]

@pulumi.output_type
class GetWebIamPolicyResult:
    def __init__(__self__, etag=..., id=..., policy_data=..., project=...) -> None: ...
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

class AwaitableGetWebIamPolicyResult(GetWebIamPolicyResult):
    def __await__(self): ...

def get_web_iam_policy(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetWebIamPolicyResult: ...
def get_web_iam_policy_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebIamPolicyResult]: ...
