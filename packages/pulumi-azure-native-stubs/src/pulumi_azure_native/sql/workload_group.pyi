

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadGroupArgs', 'WorkloadGroup']
@pulumi.input_type
class WorkloadGroupArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], max_resource_percent: pulumi.Input[_builtins.int], min_resource_percent: pulumi.Input[_builtins.int], min_resource_percent_per_request: pulumi.Input[_builtins.float], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], importance: Optional[pulumi.Input[_builtins.str]] = ..., max_resource_percent_per_request: Optional[pulumi.Input[_builtins.float]] = ..., query_execution_timeout: Optional[pulumi.Input[_builtins.int]] = ..., workload_group_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_resource_percent.setter
    def max_resource_percent(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min_resource_percent.setter
    def min_resource_percent(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @min_resource_percent_per_request.setter
    def min_resource_percent_per_request(self, value: pulumi.Input[_builtins.float]): # -> None:
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
    def importance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @importance.setter
    def importance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_resource_percent_per_request.setter
    def max_resource_percent_per_request(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryExecutionTimeout")
    def query_execution_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @query_execution_timeout.setter
    def query_execution_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadGroupName")
    def workload_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_group_name.setter
    def workload_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:WorkloadGroup")
class WorkloadGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., importance: Optional[pulumi.Input[_builtins.str]] = ..., max_resource_percent: Optional[pulumi.Input[_builtins.int]] = ..., max_resource_percent_per_request: Optional[pulumi.Input[_builtins.float]] = ..., min_resource_percent: Optional[pulumi.Input[_builtins.int]] = ..., min_resource_percent_per_request: Optional[pulumi.Input[_builtins.float]] = ..., query_execution_timeout: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkloadGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryExecutionTimeout")
    def query_execution_timeout(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


