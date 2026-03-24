import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebRegionBackendServiceIamPolicyResult",
    "AwaitableGetWebRegionBackendServiceIamPolicyResult",
    "get_web_region_backend_service_iam_policy",
    "get_web_region_backend_service_iam_policy_output",
]

@pulumi.output_type
class GetWebRegionBackendServiceIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
        region=...,
        web_region_backend_service=...,
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
    @pulumi.getter(name="webRegionBackendService")
    def web_region_backend_service(self) -> _builtins.str: ...

class AwaitableGetWebRegionBackendServiceIamPolicyResult(
    GetWebRegionBackendServiceIamPolicyResult
):
    def __await__(self): ...

def get_web_region_backend_service_iam_policy(
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    web_region_backend_service: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebRegionBackendServiceIamPolicyResult: ...
def get_web_region_backend_service_iam_policy_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    web_region_backend_service: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebRegionBackendServiceIamPolicyResult]: ...
