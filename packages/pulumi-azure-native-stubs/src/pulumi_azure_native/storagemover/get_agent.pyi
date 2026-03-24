

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAgentResult', 'AwaitableGetAgentResult', 'get_agent', 'get_agent_output']
@pulumi.output_type
class GetAgentResult:
    
    def __init__(__self__, agent_status=..., agent_version=..., arc_resource_id=..., arc_vm_uuid=..., azure_api_version=..., description=..., error_details=..., id=..., last_status_update=..., local_ip_address=..., memory_in_mb=..., name=..., number_of_cores=..., provisioning_state=..., system_data=..., time_zone=..., type=..., upload_limit_schedule=..., uptime_in_seconds=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> outputs.AgentPropertiesErrorDetailsResponse:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusUpdate")
    def last_status_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localIPAddress")
    def local_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInMB")
    def memory_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfCores")
    def number_of_cores(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadLimitSchedule")
    def upload_limit_schedule(self) -> Optional[outputs.UploadLimitScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uptimeInSeconds")
    def uptime_in_seconds(self) -> _builtins.float:
        
        ...
    


class AwaitableGetAgentResult(GetAgentResult):
    def __await__(self): # -> Generator[Never, Any, GetAgentResult]:
        ...
    


def get_agent(agent_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., storage_mover_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAgentResult:
    
    ...

def get_agent_output(agent_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_mover_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAgentResult]:
    
    ...

