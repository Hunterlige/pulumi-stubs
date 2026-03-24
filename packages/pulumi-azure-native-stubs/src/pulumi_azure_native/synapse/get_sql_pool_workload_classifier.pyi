

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlPoolWorkloadClassifierResult', 'AwaitableGetSqlPoolWorkloadClassifierResult', 'get_sql_pool_workload_classifier', 'get_sql_pool_workload_classifier_output']
@pulumi.output_type
class GetSqlPoolWorkloadClassifierResult:
    
    def __init__(__self__, azure_api_version=..., context=..., end_time=..., id=..., importance=..., label=..., member_name=..., name=..., start_time=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSqlPoolWorkloadClassifierResult(GetSqlPoolWorkloadClassifierResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlPoolWorkloadClassifierResult]:
        ...
    


def get_sql_pool_workload_classifier(resource_group_name: Optional[_builtins.str] = ..., sql_pool_name: Optional[_builtins.str] = ..., workload_classifier_name: Optional[_builtins.str] = ..., workload_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlPoolWorkloadClassifierResult:
    
    ...

def get_sql_pool_workload_classifier_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_classifier_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlPoolWorkloadClassifierResult]:
    
    ...

