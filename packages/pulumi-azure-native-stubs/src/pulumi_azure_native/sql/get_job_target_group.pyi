import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetJobTargetGroupResult",
    "AwaitableGetJobTargetGroupResult",
    "get_job_target_group",
    "get_job_target_group_output",
]

@pulumi.output_type
class GetJobTargetGroupResult:
    def __init__(
        __self__, azure_api_version=..., id=..., members=..., name=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[outputs.JobTargetResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetJobTargetGroupResult(GetJobTargetGroupResult):
    def __await__(self): ...

def get_job_target_group(
    job_agent_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    target_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobTargetGroupResult: ...
def get_job_target_group_output(
    job_agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    target_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobTargetGroupResult]: ...
