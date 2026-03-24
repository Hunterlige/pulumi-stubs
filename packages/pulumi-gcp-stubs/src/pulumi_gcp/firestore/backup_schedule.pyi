import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackupScheduleArgs", "BackupSchedule"]

@pulumi.input_type
class BackupScheduleArgs:
    def __init__(
        __self__,
        *,
        retention: pulumi.Input[_builtins.str],
        daily_recurrence: Optional[
            pulumi.Input[BackupScheduleDailyRecurrenceArgs]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[
            pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Input[_builtins.str]: ...
    @retention.setter
    def retention(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleDailyRecurrenceArgs]]: ...
    @daily_recurrence.setter
    def daily_recurrence(
        self, value: Optional[pulumi.Input[BackupScheduleDailyRecurrenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]]: ...
    @weekly_recurrence.setter
    def weekly_recurrence(
        self, value: Optional[pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]]
    ): ...

@pulumi.input_type
class _BackupScheduleState:
    def __init__(
        __self__,
        *,
        daily_recurrence: Optional[
            pulumi.Input[BackupScheduleDailyRecurrenceArgs]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[
            pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleDailyRecurrenceArgs]]: ...
    @daily_recurrence.setter
    def daily_recurrence(
        self, value: Optional[pulumi.Input[BackupScheduleDailyRecurrenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]]: ...
    @weekly_recurrence.setter
    def weekly_recurrence(
        self, value: Optional[pulumi.Input[BackupScheduleWeeklyRecurrenceArgs]]
    ): ...

@pulumi.type_token("gcp:firestore/backupSchedule:BackupSchedule")
class BackupSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        daily_recurrence: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleDailyRecurrenceArgs,
                    BackupScheduleDailyRecurrenceArgsDict,
                ]
            ]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleWeeklyRecurrenceArgs,
                    BackupScheduleWeeklyRecurrenceArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BackupScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        daily_recurrence: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleDailyRecurrenceArgs,
                    BackupScheduleDailyRecurrenceArgsDict,
                ]
            ]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleWeeklyRecurrenceArgs,
                    BackupScheduleWeeklyRecurrenceArgsDict,
                ]
            ]
        ] = ...,
    ) -> BackupSchedule: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(
        self,
    ) -> pulumi.Output[Optional[outputs.BackupScheduleDailyRecurrence]]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(
        self,
    ) -> pulumi.Output[Optional[outputs.BackupScheduleWeeklyRecurrence]]: ...
