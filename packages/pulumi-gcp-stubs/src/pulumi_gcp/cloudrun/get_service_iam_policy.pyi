import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceIamPolicyResult",
    "AwaitableGetServiceIamPolicyResult",
    "get_service_iam_policy",
    "get_service_iam_policy_output",
]

@pulumi.output_type
class GetServiceIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
        service=...,
    ) -> None: ...
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
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

class AwaitableGetServiceIamPolicyResult(GetServiceIamPolicyResult):
    def __await__(self): ...

def get_service_iam_policy(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    service: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceIamPolicyResult: ...
def get_service_iam_policy_output(
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceIamPolicyResult]: ...
