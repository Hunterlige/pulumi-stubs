import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStartStopManagedInstanceScheduleResult",
    "AwaitableGetStartStopManagedInstanceScheduleResult",
    "get_start_stop_managed_instance_schedule",
    "get_start_stop_managed_instance_schedule_output",
]

@pulumi.output_type
class GetStartStopManagedInstanceScheduleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        id=...,
        name=...,
        next_execution_time=...,
        next_run_action=...,
        schedule_list=...,
        system_data=...,
        time_zone_id=...,
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
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextExecutionTime")
    def next_execution_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextRunAction")
    def next_run_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleList")
    def schedule_list(self) -> Sequence[outputs.ScheduleItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStartStopManagedInstanceScheduleResult(
    GetStartStopManagedInstanceScheduleResult
):
    def __await__(self): ...

def get_start_stop_managed_instance_schedule(
    managed_instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    start_stop_schedule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStartStopManagedInstanceScheduleResult: ...
def get_start_stop_managed_instance_schedule_output(
    managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    start_stop_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStartStopManagedInstanceScheduleResult]: ...
