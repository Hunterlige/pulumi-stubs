

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScalingPlanPooledScheduleArgs', 'ScalingPlanPooledSchedule']
@pulumi.input_type
class ScalingPlanPooledScheduleArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], scaling_plan_name: pulumi.Input[_builtins.str], days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]] = ..., off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., off_peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_down_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_force_logoff_users: Optional[pulumi.Input[_builtins.bool]] = ..., ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_down_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_notification_message: Optional[pulumi.Input[_builtins.str]] = ..., ramp_down_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]] = ..., ramp_down_wait_time_minutes: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_up_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_start_time: Optional[pulumi.Input[TimeArgs]] = ..., scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanName")
    def scaling_plan_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scaling_plan_name.setter
    def scaling_plan_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]]:
        
        ...
    
    @days_of_week.setter
    def days_of_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @off_peak_load_balancing_algorithm.setter
    def off_peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @off_peak_start_time.setter
    def off_peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @peak_load_balancing_algorithm.setter
    def peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @peak_start_time.setter
    def peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_capacity_threshold_pct.setter
    def ramp_down_capacity_threshold_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ramp_down_force_logoff_users.setter
    def ramp_down_force_logoff_users(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @ramp_down_load_balancing_algorithm.setter
    def ramp_down_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_minimum_hosts_pct.setter
    def ramp_down_minimum_hosts_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ramp_down_notification_message.setter
    def ramp_down_notification_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_down_start_time.setter
    def ramp_down_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]]:
        
        ...
    
    @ramp_down_stop_hosts_when.setter
    def ramp_down_stop_hosts_when(self, value: Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_wait_time_minutes.setter
    def ramp_down_wait_time_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_capacity_threshold_pct.setter
    def ramp_up_capacity_threshold_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @ramp_up_load_balancing_algorithm.setter
    def ramp_up_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_minimum_hosts_pct.setter
    def ramp_up_minimum_hosts_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_up_start_time.setter
    def ramp_up_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanScheduleName")
    def scaling_plan_schedule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scaling_plan_schedule_name.setter
    def scaling_plan_schedule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ScalingPlanPooledSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]] = ..., off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., off_peak_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., peak_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., ramp_down_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_force_logoff_users: Optional[pulumi.Input[_builtins.bool]] = ..., ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_down_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_notification_message: Optional[pulumi.Input[_builtins.str]] = ..., ramp_down_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]] = ..., ramp_down_wait_time_minutes: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_up_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScalingPlanPooledScheduleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ScalingPlanPooledSchedule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


