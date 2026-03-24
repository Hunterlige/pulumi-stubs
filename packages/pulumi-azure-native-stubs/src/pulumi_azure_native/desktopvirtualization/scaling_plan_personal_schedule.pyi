

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
__all__ = ['ScalingPlanPersonalScheduleArgs', 'ScalingPlanPersonalSchedule']
@pulumi.input_type
class ScalingPlanPersonalScheduleArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], scaling_plan_name: pulumi.Input[_builtins.str], days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]] = ..., off_peak_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., off_peak_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., off_peak_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., off_peak_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., off_peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., off_peak_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., peak_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., peak_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., peak_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., peak_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., peak_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., ramp_down_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_down_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_down_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_down_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., ramp_up_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_up_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_up_auto_start_hosts: Optional[pulumi.Input[Union[_builtins.str, StartupBehavior]]] = ..., ramp_up_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_up_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="offPeakActionOnDisconnect")
    def off_peak_action_on_disconnect(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @off_peak_action_on_disconnect.setter
    def off_peak_action_on_disconnect(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakActionOnLogoff")
    def off_peak_action_on_logoff(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @off_peak_action_on_logoff.setter
    def off_peak_action_on_logoff(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnDisconnect")
    def off_peak_minutes_to_wait_on_disconnect(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @off_peak_minutes_to_wait_on_disconnect.setter
    def off_peak_minutes_to_wait_on_disconnect(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnLogoff")
    def off_peak_minutes_to_wait_on_logoff(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @off_peak_minutes_to_wait_on_logoff.setter
    def off_peak_minutes_to_wait_on_logoff(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @off_peak_start_time.setter
    def off_peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartVMOnConnect")
    def off_peak_start_vm_on_connect(self) -> Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]:
        
        ...
    
    @off_peak_start_vm_on_connect.setter
    def off_peak_start_vm_on_connect(self, value: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnDisconnect")
    def peak_action_on_disconnect(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @peak_action_on_disconnect.setter
    def peak_action_on_disconnect(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnLogoff")
    def peak_action_on_logoff(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @peak_action_on_logoff.setter
    def peak_action_on_logoff(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnDisconnect")
    def peak_minutes_to_wait_on_disconnect(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @peak_minutes_to_wait_on_disconnect.setter
    def peak_minutes_to_wait_on_disconnect(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnLogoff")
    def peak_minutes_to_wait_on_logoff(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @peak_minutes_to_wait_on_logoff.setter
    def peak_minutes_to_wait_on_logoff(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @peak_start_time.setter
    def peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartVMOnConnect")
    def peak_start_vm_on_connect(self) -> Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]:
        
        ...
    
    @peak_start_vm_on_connect.setter
    def peak_start_vm_on_connect(self, value: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnDisconnect")
    def ramp_down_action_on_disconnect(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @ramp_down_action_on_disconnect.setter
    def ramp_down_action_on_disconnect(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnLogoff")
    def ramp_down_action_on_logoff(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @ramp_down_action_on_logoff.setter
    def ramp_down_action_on_logoff(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnDisconnect")
    def ramp_down_minutes_to_wait_on_disconnect(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_minutes_to_wait_on_disconnect.setter
    def ramp_down_minutes_to_wait_on_disconnect(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnLogoff")
    def ramp_down_minutes_to_wait_on_logoff(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_minutes_to_wait_on_logoff.setter
    def ramp_down_minutes_to_wait_on_logoff(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_down_start_time.setter
    def ramp_down_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartVMOnConnect")
    def ramp_down_start_vm_on_connect(self) -> Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]:
        
        ...
    
    @ramp_down_start_vm_on_connect.setter
    def ramp_down_start_vm_on_connect(self, value: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnDisconnect")
    def ramp_up_action_on_disconnect(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @ramp_up_action_on_disconnect.setter
    def ramp_up_action_on_disconnect(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnLogoff")
    def ramp_up_action_on_logoff(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]:
        
        ...
    
    @ramp_up_action_on_logoff.setter
    def ramp_up_action_on_logoff(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpAutoStartHosts")
    def ramp_up_auto_start_hosts(self) -> Optional[pulumi.Input[Union[_builtins.str, StartupBehavior]]]:
        
        ...
    
    @ramp_up_auto_start_hosts.setter
    def ramp_up_auto_start_hosts(self, value: Optional[pulumi.Input[Union[_builtins.str, StartupBehavior]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnDisconnect")
    def ramp_up_minutes_to_wait_on_disconnect(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_minutes_to_wait_on_disconnect.setter
    def ramp_up_minutes_to_wait_on_disconnect(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnLogoff")
    def ramp_up_minutes_to_wait_on_logoff(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_minutes_to_wait_on_logoff.setter
    def ramp_up_minutes_to_wait_on_logoff(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_up_start_time.setter
    def ramp_up_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartVMOnConnect")
    def ramp_up_start_vm_on_connect(self) -> Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]:
        
        ...
    
    @ramp_up_start_vm_on_connect.setter
    def ramp_up_start_vm_on_connect(self, value: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanScheduleName")
    def scaling_plan_schedule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scaling_plan_schedule_name.setter
    def scaling_plan_schedule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ScalingPlanPersonalSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]] = ..., off_peak_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., off_peak_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., off_peak_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., off_peak_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., off_peak_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., off_peak_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., peak_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., peak_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., peak_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., peak_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., peak_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., peak_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., ramp_down_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_down_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_down_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., ramp_down_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., ramp_up_action_on_disconnect: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_up_action_on_logoff: Optional[pulumi.Input[Union[_builtins.str, SessionHandlingOperation]]] = ..., ramp_up_auto_start_hosts: Optional[pulumi.Input[Union[_builtins.str, StartupBehavior]]] = ..., ramp_up_minutes_to_wait_on_disconnect: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_minutes_to_wait_on_logoff: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_start_time: Optional[pulumi.Input[Union[TimeArgs, TimeArgsDict]]] = ..., ramp_up_start_vm_on_connect: Optional[pulumi.Input[Union[_builtins.str, SetStartVMOnConnect]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_schedule_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScalingPlanPersonalScheduleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ScalingPlanPersonalSchedule:
        
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
    @pulumi.getter(name="offPeakActionOnDisconnect")
    def off_peak_action_on_disconnect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakActionOnLogoff")
    def off_peak_action_on_logoff(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnDisconnect")
    def off_peak_minutes_to_wait_on_disconnect(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakMinutesToWaitOnLogoff")
    def off_peak_minutes_to_wait_on_logoff(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartVMOnConnect")
    def off_peak_start_vm_on_connect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnDisconnect")
    def peak_action_on_disconnect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakActionOnLogoff")
    def peak_action_on_logoff(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnDisconnect")
    def peak_minutes_to_wait_on_disconnect(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakMinutesToWaitOnLogoff")
    def peak_minutes_to_wait_on_logoff(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartVMOnConnect")
    def peak_start_vm_on_connect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnDisconnect")
    def ramp_down_action_on_disconnect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownActionOnLogoff")
    def ramp_down_action_on_logoff(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnDisconnect")
    def ramp_down_minutes_to_wait_on_disconnect(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinutesToWaitOnLogoff")
    def ramp_down_minutes_to_wait_on_logoff(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartVMOnConnect")
    def ramp_down_start_vm_on_connect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnDisconnect")
    def ramp_up_action_on_disconnect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpActionOnLogoff")
    def ramp_up_action_on_logoff(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpAutoStartHosts")
    def ramp_up_auto_start_hosts(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnDisconnect")
    def ramp_up_minutes_to_wait_on_disconnect(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinutesToWaitOnLogoff")
    def ramp_up_minutes_to_wait_on_logoff(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> pulumi.Output[Optional[outputs.TimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartVMOnConnect")
    def ramp_up_start_vm_on_connect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


