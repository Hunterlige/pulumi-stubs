

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetJobQueueResult', 'AwaitableGetJobQueueResult', 'get_job_queue', 'get_job_queue_output']
@pulumi.output_type
class GetJobQueueResult:
    
    def __init__(__self__, arn=..., compute_environment_orders=..., id=..., job_state_time_limit_actions=..., name=..., priority=..., region=..., scheduling_policy_arn=..., state=..., status=..., status_reason=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeEnvironmentOrders")
    def compute_environment_orders(self) -> Sequence[outputs.GetJobQueueComputeEnvironmentOrderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStateTimeLimitActions")
    def job_state_time_limit_actions(self) -> Sequence[outputs.GetJobQueueJobStateTimeLimitActionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetJobQueueResult(GetJobQueueResult):
    def __await__(self): # -> Generator[Never, Any, GetJobQueueResult]:
        ...
    


def get_job_queue(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetJobQueueResult:
    
    ...

def get_job_queue_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetJobQueueResult]:
    
    ...

