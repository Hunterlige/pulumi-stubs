

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScheduleArgs', 'Schedule']
@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *, autoscaling_group_name: pulumi.Input[_builtins.str], scheduled_action_name: pulumi.Input[_builtins.str], desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., recurrence: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scheduled_action_name.setter
    def scheduled_action_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ScheduleState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., recurrence: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_action_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduled_action_name.setter
    def scheduled_action_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscaling/schedule:Schedule")
class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., recurrence: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_action_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScheduleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., recurrence: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_action_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Schedule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


