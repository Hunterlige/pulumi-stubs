

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSessionHostResult', 'AwaitableGetSessionHostResult', 'get_session_host', 'get_session_host_output']
@pulumi.output_type
class GetSessionHostResult:
    
    def __init__(__self__, active_sessions=..., agent_version=..., allow_new_session=..., assigned_user=..., azure_api_version=..., disconnected_sessions=..., friendly_name=..., id=..., last_heart_beat=..., last_session_host_update_time=..., last_update_time=..., name=..., object_id=..., os_version=..., pending_sessions=..., resource_id=..., session_host_configuration=..., session_host_health_check_results=..., sessions=..., status=..., status_timestamp=..., sx_s_stack_version=..., system_data=..., type=..., update_error_message=..., update_state=..., virtual_machine_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeSessions")
    def active_sessions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNewSession")
    def allow_new_session(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedUser")
    def assigned_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectedSessions")
    def disconnected_sessions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartBeat")
    def last_heart_beat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSessionHostUpdateTime")
    def last_session_host_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingSessions")
    def pending_sessions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionHostConfiguration")
    def session_host_configuration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionHostHealthCheckResults")
    def session_host_health_check_results(self) -> Sequence[outputs.SessionHostHealthCheckReportResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sessions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusTimestamp")
    def status_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sxSStackVersion")
    def sx_s_stack_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateErrorMessage")
    def update_error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateState")
    def update_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSessionHostResult(GetSessionHostResult):
    def __await__(self): # -> Generator[Never, Any, GetSessionHostResult]:
        ...
    


def get_session_host(host_pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., session_host_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSessionHostResult:
    
    ...

def get_session_host_output(host_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., session_host_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSessionHostResult]:
    
    ...

