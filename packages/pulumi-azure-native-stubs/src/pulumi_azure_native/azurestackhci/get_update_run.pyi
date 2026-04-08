import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetUpdateRunResult",
    "AwaitableGetUpdateRunResult",
    "get_update_run",
    "get_update_run_output",
]

@pulumi.output_type
class GetUpdateRunResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        duration=...,
        end_time_utc=...,
        error_message=...,
        expected_execution_time=...,
        id=...,
        last_updated_time=...,
        last_updated_time_utc=...,
        location=...,
        name=...,
        provisioning_state=...,
        start_time_utc=...,
        state=...,
        status=...,
        steps=...,
        system_data=...,
        time_started=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedExecutionTime")
    def expected_execution_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[Sequence[outputs.StepResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetUpdateRunResult(GetUpdateRunResult):
    def __await__(self): ...

def get_update_run(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    update_name: Optional[_builtins.str] = ...,
    update_run_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUpdateRunResult: ...
def get_update_run_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    update_name: Optional[pulumi.Input[_builtins.str]] = ...,
    update_run_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUpdateRunResult]: ...
