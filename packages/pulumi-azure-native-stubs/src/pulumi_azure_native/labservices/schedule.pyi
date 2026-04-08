import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
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
        lab_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        stop_at: pulumi.Input[_builtins.str],
        time_zone_id: pulumi.Input[_builtins.str],
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        recurrence_pattern: Optional[pulumi.Input[RecurrencePatternArgs]] = ...,
        schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_at: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[_builtins.str]: ...
    @lab_name.setter
    def lab_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stopAt")
    def stop_at(self) -> pulumi.Input[_builtins.str]: ...
    @stop_at.setter
    def stop_at(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone_id.setter
    def time_zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recurrencePattern")
    def recurrence_pattern(self) -> Optional[pulumi.Input[RecurrencePatternArgs]]: ...
    @recurrence_pattern.setter
    def recurrence_pattern(
        self, value: Optional[pulumi.Input[RecurrencePatternArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleName")
    def schedule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_name.setter
    def schedule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_at.setter
    def start_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:labservices:Schedule")
class Schedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        recurrence_pattern: Optional[
            pulumi.Input[Union[RecurrencePatternArgs, RecurrencePatternArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_at: Optional[pulumi.Input[_builtins.str]] = ...,
        stop_at: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurrencePattern")
    def recurrence_pattern(
        self,
    ) -> pulumi.Output[Optional[outputs.RecurrencePatternResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(
        self,
    ) -> pulumi.Output[outputs.ResourceOperationErrorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stopAt")
    def stop_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
