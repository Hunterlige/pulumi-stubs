import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GlobalScheduleArgs", "GlobalSchedule"]

@pulumi.input_type
class GlobalScheduleArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        daily_recurrence: Optional[pulumi.Input[DayDetailsArgs]] = ...,
        hourly_recurrence: Optional[pulumi.Input[HourDetailsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_settings: Optional[pulumi.Input[NotificationSettingsArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        task_type: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[pulumi.Input[WeekDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[pulumi.Input[DayDetailsArgs]]: ...
    @daily_recurrence.setter
    def daily_recurrence(self, value: Optional[pulumi.Input[DayDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[pulumi.Input[HourDetailsArgs]]: ...
    @hourly_recurrence.setter
    def hourly_recurrence(self, value: Optional[pulumi.Input[HourDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingsArgs]]: ...
    @notification_settings.setter
    def notification_settings(
        self, value: Optional[pulumi.Input[NotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_type.setter
    def task_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[pulumi.Input[WeekDetailsArgs]]: ...
    @weekly_recurrence.setter
    def weekly_recurrence(self, value: Optional[pulumi.Input[WeekDetailsArgs]]): ...

@pulumi.type_token("azure-native:devtestlab:GlobalSchedule")
class GlobalSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        daily_recurrence: Optional[
            pulumi.Input[Union[DayDetailsArgs, DayDetailsArgsDict]]
        ] = ...,
        hourly_recurrence: Optional[
            pulumi.Input[Union[HourDetailsArgs, HourDetailsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_settings: Optional[
            pulumi.Input[Union[NotificationSettingsArgs, NotificationSettingsArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        task_type: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[
            pulumi.Input[Union[WeekDetailsArgs, WeekDetailsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GlobalScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GlobalSchedule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(
        self,
    ) -> pulumi.Output[Optional[outputs.DayDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(
        self,
    ) -> pulumi.Output[Optional[outputs.HourDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.NotificationSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(
        self,
    ) -> pulumi.Output[Optional[outputs.WeekDetailsResponse]]: ...
