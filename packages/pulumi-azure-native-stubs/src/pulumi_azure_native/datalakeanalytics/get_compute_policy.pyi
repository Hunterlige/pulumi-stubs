

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetComputePolicyResult', 'AwaitableGetComputePolicyResult', 'get_compute_policy', 'get_compute_policy_output']
@pulumi.output_type
class GetComputePolicyResult:
    
    def __init__(__self__, azure_api_version=..., id=..., max_degree_of_parallelism_per_job=..., min_priority_per_job=..., name=..., object_id=..., object_type=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> _builtins.int:
        
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
    @pulumi.getter(name="objectType")
    def object_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetComputePolicyResult(GetComputePolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetComputePolicyResult]:
        ...
    


def get_compute_policy(account_name: Optional[_builtins.str] = ..., compute_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetComputePolicyResult:
    
    ...

def get_compute_policy_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., compute_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetComputePolicyResult]:
    
    ...

