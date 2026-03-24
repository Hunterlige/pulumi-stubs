

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExperimentExecutionDetailsResult', 'AwaitableGetExperimentExecutionDetailsResult', 'get_experiment_execution_details', 'get_experiment_execution_details_output']
@pulumi.output_type
class GetExperimentExecutionDetailsResult:
    
    def __init__(__self__, failure_reason=..., id=..., last_action_at=..., name=..., run_information=..., started_at=..., status=..., stopped_at=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActionAt")
    def last_action_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runInformation")
    def run_information(self) -> outputs.ExperimentExecutionDetailsPropertiesResponseRunInformation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedAt")
    def started_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stoppedAt")
    def stopped_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetExperimentExecutionDetailsResult(GetExperimentExecutionDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetExperimentExecutionDetailsResult]:
        ...
    


def get_experiment_execution_details(execution_id: Optional[_builtins.str] = ..., experiment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExperimentExecutionDetailsResult:
    
    ...

def get_experiment_execution_details_output(execution_id: Optional[pulumi.Input[_builtins.str]] = ..., experiment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExperimentExecutionDetailsResult]:
    
    ...

