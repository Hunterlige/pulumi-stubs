

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProfilingGroupResult', 'AwaitableGetProfilingGroupResult', 'get_profiling_group', 'get_profiling_group_output']
@pulumi.output_type
class GetProfilingGroupResult:
    
    def __init__(__self__, agent_orchestration_configs=..., arn=..., compute_platform=..., created_at=..., id=..., name=..., profiling_statuses=..., region=..., tags=..., updated_at=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentOrchestrationConfigs")
    def agent_orchestration_configs(self) -> Sequence[outputs.GetProfilingGroupAgentOrchestrationConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilingStatuses")
    def profiling_statuses(self) -> Sequence[outputs.GetProfilingGroupProfilingStatusResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProfilingGroupResult(GetProfilingGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetProfilingGroupResult]:
        ...
    


def get_profiling_group(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProfilingGroupResult:
    
    ...

def get_profiling_group_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProfilingGroupResult]:
    
    ...

