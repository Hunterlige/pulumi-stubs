import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApiConfigIamPolicyResult",
    "AwaitableGetApiConfigIamPolicyResult",
    "get_api_config_iam_policy",
    "get_api_config_iam_policy_output",
]

@pulumi.output_type
class GetApiConfigIamPolicyResult:
    def __init__(
        __self__,
        api=...,
        api_config=...,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> _builtins.str: ...
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

class AwaitableGetApiConfigIamPolicyResult(GetApiConfigIamPolicyResult):
    def __await__(self): ...

def get_api_config_iam_policy(
    api: Optional[_builtins.str] = ...,
    api_config: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApiConfigIamPolicyResult: ...
def get_api_config_iam_policy_output(
    api: Optional[pulumi.Input[_builtins.str]] = ...,
    api_config: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApiConfigIamPolicyResult]: ...
