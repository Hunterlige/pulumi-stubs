import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StartStopManagedInstanceScheduleArgs", "StartStopManagedInstanceSchedule"]

@pulumi.input_type
class StartStopManagedInstanceScheduleArgs:
    def __init__(
        __self__,
        *,
        managed_instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        schedule_list: pulumi.Input[Sequence[pulumi.Input[ScheduleItemArgs]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        start_stop_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleList")
    def schedule_list(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ScheduleItemArgs]]]: ...
    @schedule_list.setter
    def schedule_list(
        self, value: pulumi.Input[Sequence[pulumi.Input[ScheduleItemArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startStopScheduleName")
    def start_stop_schedule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_stop_schedule_name.setter
    def start_stop_schedule_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:sql:StartStopManagedInstanceSchedule")
class StartStopManagedInstanceSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_list: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ScheduleItemArgs, ScheduleItemArgsDict]]]
            ]
        ] = ...,
        start_stop_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StartStopManagedInstanceScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StartStopManagedInstanceSchedule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextExecutionTime")
    def next_execution_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextRunAction")
    def next_run_action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleList")
    def schedule_list(
        self,
    ) -> pulumi.Output[Sequence[outputs.ScheduleItemResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
