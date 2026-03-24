import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterIamPolicyResult",
    "AwaitableGetClusterIamPolicyResult",
    "get_cluster_iam_policy",
    "get_cluster_iam_policy_output",
]

@pulumi.output_type
class GetClusterIamPolicyResult:
    def __init__(
        __self__,
        cluster=...,
        etag=...,
        id=...,
        policy_data=...,
        project=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
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

class AwaitableGetClusterIamPolicyResult(GetClusterIamPolicyResult):
    def __await__(self): ...

def get_cluster_iam_policy(
    cluster: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterIamPolicyResult: ...
def get_cluster_iam_policy_output(
    cluster: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterIamPolicyResult]: ...
