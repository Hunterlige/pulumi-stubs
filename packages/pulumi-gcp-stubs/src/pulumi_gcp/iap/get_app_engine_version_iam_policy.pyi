import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAppEngineVersionIamPolicyResult",
    "AwaitableGetAppEngineVersionIamPolicyResult",
    "get_app_engine_version_iam_policy",
    "get_app_engine_version_iam_policy_output",
]

@pulumi.output_type
class GetAppEngineVersionIamPolicyResult:
    def __init__(
        __self__,
        app_id=...,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
        service=...,
        version_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str: ...
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
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str: ...

class AwaitableGetAppEngineVersionIamPolicyResult(GetAppEngineVersionIamPolicyResult):
    def __await__(self): ...

def get_app_engine_version_iam_policy(
    app_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    service: Optional[_builtins.str] = ...,
    version_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppEngineVersionIamPolicyResult: ...
def get_app_engine_version_iam_policy_output(
    app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service: Optional[pulumi.Input[_builtins.str]] = ...,
    version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppEngineVersionIamPolicyResult]: ...
