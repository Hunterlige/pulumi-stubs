import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebTypeAppEngineIamPolicyResult",
    "AwaitableGetWebTypeAppEngineIamPolicyResult",
    "get_web_type_app_engine_iam_policy",
    "get_web_type_app_engine_iam_policy_output",
]

@pulumi.output_type
class GetWebTypeAppEngineIamPolicyResult:
    def __init__(
        __self__, app_id=..., etag=..., id=..., policy_data=..., project=...
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

class AwaitableGetWebTypeAppEngineIamPolicyResult(GetWebTypeAppEngineIamPolicyResult):
    def __await__(self): ...

def get_web_type_app_engine_iam_policy(
    app_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebTypeAppEngineIamPolicyResult: ...
def get_web_type_app_engine_iam_policy_output(
    app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebTypeAppEngineIamPolicyResult]: ...
