import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScheduleResult",
    "AwaitableGetScheduleResult",
    "get_schedule",
    "get_schedule_output",
]

@pulumi.output_type
class GetScheduleResult:
    def __init__(
        __self__,
        advanced_schedule=...,
        azure_api_version=...,
        creation_time=...,
        description=...,
        expiry_time=...,
        expiry_time_offset_minutes=...,
        frequency=...,
        id=...,
        interval=...,
        is_enabled=...,
        last_modified_time=...,
        name=...,
        next_run=...,
        next_run_offset_minutes=...,
        start_time=...,
        start_time_offset_minutes=...,
        system_data=...,
        time_zone=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional[outputs.AdvancedScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetScheduleResult(GetScheduleResult):
    def __await__(self): ...

def get_schedule(
    automation_account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    schedule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScheduleResult: ...
def get_schedule_output(
    automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScheduleResult]: ...
