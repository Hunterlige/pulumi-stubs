import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebCloudRunServiceIamPolicyResult",
    "AwaitableGetWebCloudRunServiceIamPolicyResult",
    "get_web_cloud_run_service_iam_policy",
    "get_web_cloud_run_service_iam_policy_output",
]

@pulumi.output_type
class GetWebCloudRunServiceIamPolicyResult:
    def __init__(
        __self__,
        cloud_run_service_name=...,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRunServiceName")
    def cloud_run_service_name(self) -> _builtins.str: ...
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

class AwaitableGetWebCloudRunServiceIamPolicyResult(
    GetWebCloudRunServiceIamPolicyResult
):
    def __await__(self): ...

def get_web_cloud_run_service_iam_policy(
    cloud_run_service_name: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebCloudRunServiceIamPolicyResult: ...
def get_web_cloud_run_service_iam_policy_output(
    cloud_run_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebCloudRunServiceIamPolicyResult]: ...
