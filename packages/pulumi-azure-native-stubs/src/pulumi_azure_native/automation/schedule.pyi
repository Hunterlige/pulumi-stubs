import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScheduleArgs", "Schedule"]

@pulumi.input_type
class ScheduleArgs:
    def __init__(
        __self__,
        *,
        automation_account_name: pulumi.Input[_builtins.str],
        frequency: pulumi.Input[Union[_builtins.str, ScheduleFrequency]],
        name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
        advanced_schedule: Optional[pulumi.Input[AdvancedScheduleArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        interval: Optional[Any] = ...,
        schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[Union[_builtins.str, ScheduleFrequency]]: ...
    @frequency.setter
    def frequency(
        self, value: pulumi.Input[Union[_builtins.str, ScheduleFrequency]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional[pulumi.Input[AdvancedScheduleArgs]]: ...
    @advanced_schedule.setter
    def advanced_schedule(
        self, value: Optional[pulumi.Input[AdvancedScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[Any]: ...
    @interval.setter
    def interval(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleName")
    def schedule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_name.setter
    def schedule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:automation:Schedule")
class Schedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_schedule: Optional[
            pulumi.Input[Union[AdvancedScheduleArgs, AdvancedScheduleArgsDict]]
        ] = ...,
        automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        frequency: Optional[
            pulumi.Input[Union[_builtins.str, ScheduleFrequency]]
        ] = ...,
        interval: Optional[Any] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Schedule: ...
    @_builtins.property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(
        self,
    ) -> pulumi.Output[Optional[outputs.AdvancedScheduleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
