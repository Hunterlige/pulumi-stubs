

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobDefinitionArgs', 'JobDefinition']
@pulumi.input_type
class JobDefinitionArgs:
    def __init__(__self__, *, copy_mode: pulumi.Input[Union[_builtins.str, CopyMode]], project_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], source_name: pulumi.Input[_builtins.str], storage_mover_name: pulumi.Input[_builtins.str], target_name: pulumi.Input[_builtins.str], agent_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., job_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., source_subpath: Optional[pulumi.Input[_builtins.str]] = ..., target_subpath: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyMode")
    def copy_mode(self) -> pulumi.Input[Union[_builtins.str, CopyMode]]:
        
        ...
    
    @copy_mode.setter
    def copy_mode(self, value: pulumi.Input[Union[_builtins.str, CopyMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMoverName")
    def storage_mover_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_mover_name.setter
    def storage_mover_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_name.setter
    def target_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDefinitionName")
    def job_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_definition_name.setter
    def job_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubpath")
    def source_subpath(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_subpath.setter
    def source_subpath(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSubpath")
    def target_subpath(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_subpath.setter
    def target_subpath(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storagemover:JobDefinition")
class JobDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_name: Optional[pulumi.Input[_builtins.str]] = ..., copy_mode: Optional[pulumi.Input[Union[_builtins.str, CopyMode]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., job_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_name: Optional[pulumi.Input[_builtins.str]] = ..., source_subpath: Optional[pulumi.Input[_builtins.str]] = ..., storage_mover_name: Optional[pulumi.Input[_builtins.str]] = ..., target_name: Optional[pulumi.Input[_builtins.str]] = ..., target_subpath: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JobDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> JobDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentResourceId")
    def agent_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyMode")
    def copy_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestJobRunName")
    def latest_job_run_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestJobRunResourceId")
    def latest_job_run_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestJobRunStatus")
    def latest_job_run_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubpath")
    def source_subpath(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSubpath")
    def target_subpath(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


