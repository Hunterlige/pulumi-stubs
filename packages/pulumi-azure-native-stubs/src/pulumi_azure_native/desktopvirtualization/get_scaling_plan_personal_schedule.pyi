

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScalingPlanPersonalScheduleResult', 'AwaitableGetScalingPlanPersonalScheduleResult', 'get_scaling_plan_personal_schedule', 'get_scaling_plan_personal_schedule_output']
@pulumi.output_type
class GetScalingPlanPersonalScheduleResult:
    
    def __init__(__self__, azure_api_version=..., days_of_week=..., id=..., name=..., off_peak_action_on_disconnect=..., off_peak_action_on_logoff=..., off_peak_minutes_to_wait_on_disconnect=..., off_peak_minutes_to_wait_on_logoff=..., off_peak_start_time=..., off_peak_start_vm_on_connect=..., peak_action_on_disconnect=..., peak_action_on_logoff=..., peak_minutes_to_wait_on_disconnect=..., peak_minutes_to_wait_on_logoff=..., peak_start_time=..., peak_start_vm_on_connect=..., ramp_down_action_on_disconnect=..., ramp_down_action_on_logoff=..., ramp_down_minutes_to_wait_on_disconnect=..., ramp_down_minutes_to_wait_on_logoff=..., ramp_down_start_time=..., ramp_down_start_vm_on_connect=..., ramp_up_action_on_disconnect=..., ramp_up_action_on_logoff=..., ramp_up_auto_start_hosts=..., ramp_up_minutes_to_wait_on_disconnect=..., ramp_up_minutes_to_wait_on_logoff=..., ramp_up_start_time=..., ramp_up_start_vm_on_connect=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakActionOnDisconnect")
    def off_peak_action_on_disconnect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakActionOnLogoff")
    def off_peak_action_on_logoff(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnDisconnect")
    def off_peak_minutes_to_wait_on_disconnect(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnLogoff")
    def off_peak_minutes_to_wait_on_logoff(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[outputs.TimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartVMOnConnect")
    def off_peak_start_vm_on_connect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnDisconnect")
    def peak_action_on_disconnect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnLogoff")
    def peak_action_on_logoff(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnDisconnect")
    def peak_minutes_to_wait_on_disconnect(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnLogoff")
    def peak_minutes_to_wait_on_logoff(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[outputs.TimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartVMOnConnect")
    def peak_start_vm_on_connect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnDisconnect")
    def ramp_down_action_on_disconnect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnLogoff")
    def ramp_down_action_on_logoff(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnDisconnect")
    def ramp_down_minutes_to_wait_on_disconnect(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnLogoff")
    def ramp_down_minutes_to_wait_on_logoff(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[outputs.TimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartVMOnConnect")
    def ramp_down_start_vm_on_connect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnDisconnect")
    def ramp_up_action_on_disconnect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnLogoff")
    def ramp_up_action_on_logoff(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpAutoStartHosts")
    def ramp_up_auto_start_hosts(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnDisconnect")
    def ramp_up_minutes_to_wait_on_disconnect(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnLogoff")
    def ramp_up_minutes_to_wait_on_logoff(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[outputs.TimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartVMOnConnect")
    def ramp_up_start_vm_on_connect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetScalingPlanPersonalScheduleResult(GetScalingPlanPersonalScheduleResult):
    def __await__(self): # -> Generator[Never, Any, GetScalingPlanPersonalScheduleResult]:
        ...
    


def get_scaling_plan_personal_schedule(resource_group_name: Optional[_builtins.str] = ..., scaling_plan_name: Optional[_builtins.str] = ..., scaling_plan_schedule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScalingPlanPersonalScheduleResult:
    
    ...

def get_scaling_plan_personal_schedule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScalingPlanPersonalScheduleResult]:
    
    ...

