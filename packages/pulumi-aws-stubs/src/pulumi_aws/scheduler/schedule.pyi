

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScheduleArgs', 'Schedule']
@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *, flexible_time_window: pulumi.Input[ScheduleFlexibleTimeWindowArgs], schedule_expression: pulumi.Input[_builtins.str], target: pulumi.Input[ScheduleTargetArgs], action_after_completion: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> pulumi.Input[ScheduleFlexibleTimeWindowArgs]:
        
        ...
    
    @flexible_time_window.setter
    def flexible_time_window(self, value: pulumi.Input[ScheduleFlexibleTimeWindowArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[ScheduleTargetArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[ScheduleTargetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionAfterCompletion")
    def action_after_completion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_after_completion.setter
    def action_after_completion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_expression_timezone.setter
    def schedule_expression_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ScheduleState:
    def __init__(__self__, *, action_after_completion: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., flexible_time_window: Optional[pulumi.Input[ScheduleFlexibleTimeWindowArgs]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[ScheduleTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionAfterCompletion")
    def action_after_completion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_after_completion.setter
    def action_after_completion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> Optional[pulumi.Input[ScheduleFlexibleTimeWindowArgs]]:
        
        ...
    
    @flexible_time_window.setter
    def flexible_time_window(self, value: Optional[pulumi.Input[ScheduleFlexibleTimeWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_expression_timezone.setter
    def schedule_expression_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[ScheduleTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[ScheduleTargetArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:scheduler/schedule:Schedule")
class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action_after_completion: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., flexible_time_window: Optional[pulumi.Input[Union[ScheduleFlexibleTimeWindowArgs, ScheduleFlexibleTimeWindowArgsDict]]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[ScheduleTargetArgs, ScheduleTargetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScheduleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action_after_completion: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., flexible_time_window: Optional[pulumi.Input[Union[ScheduleFlexibleTimeWindowArgs, ScheduleFlexibleTimeWindowArgsDict]]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression: Optional[pulumi.Input[_builtins.str]] = ..., schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[ScheduleTargetArgs, ScheduleTargetArgsDict]]] = ...) -> Schedule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionAfterCompletion")
    def action_after_completion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flexibleTimeWindow")
    def flexible_time_window(self) -> pulumi.Output[outputs.ScheduleFlexibleTimeWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[outputs.ScheduleTarget]:
        
        ...
    


