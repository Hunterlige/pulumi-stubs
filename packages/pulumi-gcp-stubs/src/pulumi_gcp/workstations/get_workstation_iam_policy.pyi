import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkstationIamPolicyResult",
    "AwaitableGetWorkstationIamPolicyResult",
    "get_workstation_iam_policy",
    "get_workstation_iam_policy_output",
]

@pulumi.output_type
class GetWorkstationIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
        workstation_cluster_id=...,
        workstation_config_id=...,
        workstation_id=...,
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
    @pulumi.getter(name="workstationClusterId")
    def workstation_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workstationConfigId")
    def workstation_config_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workstationId")
    def workstation_id(self) -> _builtins.str: ...

class AwaitableGetWorkstationIamPolicyResult(GetWorkstationIamPolicyResult):
    def __await__(self): ...

def get_workstation_iam_policy(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    workstation_cluster_id: Optional[_builtins.str] = ...,
    workstation_config_id: Optional[_builtins.str] = ...,
    workstation_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkstationIamPolicyResult: ...
def get_workstation_iam_policy_output(
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workstation_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    workstation_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
    workstation_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkstationIamPolicyResult]: ...
