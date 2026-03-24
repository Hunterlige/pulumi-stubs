

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkloadGroupResult', 'AwaitableGetWorkloadGroupResult', 'get_workload_group', 'get_workload_group_output']
@pulumi.output_type
class GetWorkloadGroupResult:
    
    def __init__(__self__, azure_api_version=..., id=..., importance=..., max_resource_percent=..., max_resource_percent_per_request=..., min_resource_percent=..., min_resource_percent_per_request=..., name=..., query_execution_timeout=..., type=...) -> None:
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
    @pulumi.getter
    def importance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercent")
    def max_resource_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResourcePercentPerRequest")
    def max_resource_percent_per_request(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercent")
    def min_resource_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minResourcePercentPerRequest")
    def min_resource_percent_per_request(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryExecutionTimeout")
    def query_execution_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkloadGroupResult(GetWorkloadGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkloadGroupResult]:
        ...
    


def get_workload_group(database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., workload_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkloadGroupResult:
    
    ...

def get_workload_group_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkloadGroupResult]:
    
    ...

