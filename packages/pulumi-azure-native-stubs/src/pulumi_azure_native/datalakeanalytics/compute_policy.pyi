

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ComputePolicyArgs', 'ComputePolicy']
@pulumi.input_type
class ComputePolicyArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], object_id: pulumi.Input[_builtins.str], object_type: pulumi.Input[Union[_builtins.str, AADObjectType]], resource_group_name: pulumi.Input[_builtins.str], compute_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., max_degree_of_parallelism_per_job: Optional[pulumi.Input[_builtins.int]] = ..., min_priority_per_job: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[Union[_builtins.str, AADObjectType]]:
        
        ...
    
    @object_type.setter
    def object_type(self, value: pulumi.Input[Union[_builtins.str, AADObjectType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePolicyName")
    def compute_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_policy_name.setter
    def compute_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_degree_of_parallelism_per_job.setter
    def max_degree_of_parallelism_per_job(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_priority_per_job.setter
    def min_priority_per_job(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datalakeanalytics:ComputePolicy")
class ComputePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., compute_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., max_degree_of_parallelism_per_job: Optional[pulumi.Input[_builtins.int]] = ..., min_priority_per_job: Optional[pulumi.Input[_builtins.int]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ..., object_type: Optional[pulumi.Input[Union[_builtins.str, AADObjectType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ComputePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ComputePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


