import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScalingPlanPooledScheduleResult",
    "AwaitableGetScalingPlanPooledScheduleResult",
    "get_scaling_plan_pooled_schedule",
    "get_scaling_plan_pooled_schedule_output",
]

@pulumi.output_type
class GetScalingPlanPooledScheduleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        days_of_week=...,
        id=...,
        name=...,
        off_peak_load_balancing_algorithm=...,
        off_peak_start_time=...,
        peak_load_balancing_algorithm=...,
        peak_start_time=...,
        ramp_down_capacity_threshold_pct=...,
        ramp_down_force_logoff_users=...,
        ramp_down_load_balancing_algorithm=...,
        ramp_down_minimum_hosts_pct=...,
        ramp_down_notification_message=...,
        ramp_down_start_time=...,
        ramp_down_stop_hosts_when=...,
        ramp_down_wait_time_minutes=...,
        ramp_up_capacity_threshold_pct=...,
        ramp_up_load_balancing_algorithm=...,
        ramp_up_minimum_hosts_pct=...,
        ramp_up_start_time=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetScalingPlanPooledScheduleResult(GetScalingPlanPooledScheduleResult):
    def __await__(self): ...

def get_scaling_plan_pooled_schedule(
    resource_group_name: Optional[_builtins.str] = ...,
    scaling_plan_name: Optional[_builtins.str] = ...,
    scaling_plan_schedule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScalingPlanPooledScheduleResult: ...
def get_scaling_plan_pooled_schedule_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scaling_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScalingPlanPooledScheduleResult]: ...
