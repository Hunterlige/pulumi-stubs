

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadClassifierArgs', 'WorkloadClassifier']
@pulumi.input_type
class WorkloadClassifierArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], member_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], workload_group_name: pulumi.Input[_builtins.str], context: Optional[pulumi.Input[_builtins.str]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., importance: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_classifier_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @member_name.setter
    def member_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="workloadGroupName")
    def workload_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_group_name.setter
    def workload_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @importance.setter
    def importance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadClassifierName")
    def workload_classifier_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_classifier_name.setter
    def workload_classifier_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:WorkloadClassifier")
class WorkloadClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., importance: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., member_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_classifier_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadClassifierArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkloadClassifier:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


