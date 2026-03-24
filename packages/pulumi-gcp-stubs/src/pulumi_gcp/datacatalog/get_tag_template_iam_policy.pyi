import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagTemplateIamPolicyResult",
    "AwaitableGetTagTemplateIamPolicyResult",
    "get_tag_template_iam_policy",
    "get_tag_template_iam_policy_output",
]

@pulumi.output_type
class GetTagTemplateIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
        region=...,
        tag_template=...,
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
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagTemplate")
    def tag_template(self) -> _builtins.str: ...

class AwaitableGetTagTemplateIamPolicyResult(GetTagTemplateIamPolicyResult):
    def __await__(self): ...

def get_tag_template_iam_policy(
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tag_template: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagTemplateIamPolicyResult: ...
def get_tag_template_iam_policy_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tag_template: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagTemplateIamPolicyResult]: ...
