

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobArgs', 'Job']
@pulumi.input_type
class JobArgs:
    def __init__(__self__, *, job_agent_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., job_name: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[JobScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobAgentName")
    def job_agent_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_agent_name.setter
    def job_agent_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[JobScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[JobScheduleArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., job_agent_name: Optional[pulumi.Input[_builtins.str]] = ..., job_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[JobScheduleArgs, JobScheduleArgsDict]]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Job:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[outputs.JobScheduleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


