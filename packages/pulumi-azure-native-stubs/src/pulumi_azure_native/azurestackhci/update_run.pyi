

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
__all__ = ['UpdateRunArgs', 'UpdateRun']
@pulumi.input_type
class UpdateRunArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], update_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.str]] = ..., end_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ..., expected_execution_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., start_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, UpdateRunPropertiesState]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[StepArgs]]]] = ..., time_started: Optional[pulumi.Input[_builtins.str]] = ..., update_run_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateName")
    def update_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @update_name.setter
    def update_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_utc.setter
    def end_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedExecutionTime")
    def expected_execution_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expected_execution_time.setter
    def expected_execution_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_time_utc.setter
    def last_updated_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_utc.setter
    def start_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, UpdateRunPropertiesState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, UpdateRunPropertiesState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StepArgs]]]]:
        
        ...
    
    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StepArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_started.setter
    def time_started(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateRunName")
    def update_run_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_run_name.setter
    def update_run_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:UpdateRun")
class UpdateRun(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.str]] = ..., end_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., error_message: Optional[pulumi.Input[_builtins.str]] = ..., expected_execution_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, UpdateRunPropertiesState]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StepArgs, StepArgsDict]]]]] = ..., time_started: Optional[pulumi.Input[_builtins.str]] = ..., update_name: Optional[pulumi.Input[_builtins.str]] = ..., update_run_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UpdateRunArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> UpdateRun:
        
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
    def duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedExecutionTime")
    def expected_execution_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Optional[Sequence[outputs.StepResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


