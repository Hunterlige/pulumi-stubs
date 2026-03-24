import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTaskIamPolicyResult",
    "AwaitableGetTaskIamPolicyResult",
    "get_task_iam_policy",
    "get_task_iam_policy_output",
]

@pulumi.output_type
class GetTaskIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        lake=...,
        location=...,
        policy_data=...,
        project=...,
        task_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lake(self) -> _builtins.str: ...
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
    @pulumi.getter(name="taskId")
    def task_id(self) -> _builtins.str: ...

class AwaitableGetTaskIamPolicyResult(GetTaskIamPolicyResult):
    def __await__(self): ...

def get_task_iam_policy(
    lake: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    task_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTaskIamPolicyResult: ...
def get_task_iam_policy_output(
    lake: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    task_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTaskIamPolicyResult]: ...
