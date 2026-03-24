import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCertificateTemplateIamPolicyResult",
    "AwaitableGetCertificateTemplateIamPolicyResult",
    "get_certificate_template_iam_policy",
    "get_certificate_template_iam_policy_output",
]

@pulumi.output_type
class GetCertificateTemplateIamPolicyResult:
    def __init__(
        __self__,
        certificate_template=...,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateTemplate")
    def certificate_template(self) -> _builtins.str: ...
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

class AwaitableGetCertificateTemplateIamPolicyResult(
    GetCertificateTemplateIamPolicyResult
):
    def __await__(self): ...

def get_certificate_template_iam_policy(
    certificate_template: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCertificateTemplateIamPolicyResult: ...
def get_certificate_template_iam_policy_output(
    certificate_template: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCertificateTemplateIamPolicyResult]: ...
