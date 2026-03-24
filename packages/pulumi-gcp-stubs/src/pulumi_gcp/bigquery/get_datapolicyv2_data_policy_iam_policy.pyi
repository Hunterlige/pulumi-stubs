import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatapolicyv2DataPolicyIamPolicyResult",
    "AwaitableGetDatapolicyv2DataPolicyIamPolicyResult",
    "get_datapolicyv2_data_policy_iam_policy",
    "get_datapolicyv2_data_policy_iam_policy_output",
]

@pulumi.output_type
class GetDatapolicyv2DataPolicyIamPolicyResult:
    def __init__(
        __self__,
        data_policy_id=...,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyId")
    def data_policy_id(self) -> _builtins.str: ...
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

class AwaitableGetDatapolicyv2DataPolicyIamPolicyResult(
    GetDatapolicyv2DataPolicyIamPolicyResult
):
    def __await__(self): ...

def get_datapolicyv2_data_policy_iam_policy(
    data_policy_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatapolicyv2DataPolicyIamPolicyResult: ...
def get_datapolicyv2_data_policy_iam_policy_output(
    data_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatapolicyv2DataPolicyIamPolicyResult]: ...
