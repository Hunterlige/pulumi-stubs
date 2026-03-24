

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobQueueArgs', 'JobQueue']
@pulumi.input_type
class JobQueueArgs:
    def __init__(__self__, *, priority: pulumi.Input[_builtins.int], state: pulumi.Input[_builtins.str], compute_environment_orders: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]] = ..., job_state_time_limit_actions: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[JobQueueTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeEnvironmentOrders")
    def compute_environment_orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]]:
        
        ...
    
    @compute_environment_orders.setter
    def compute_environment_orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStateTimeLimitActions")
    def job_state_time_limit_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]]:
        
        ...
    
    @job_state_time_limit_actions.setter
    def job_state_time_limit_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduling_policy_arn.setter
    def scheduling_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[JobQueueTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[JobQueueTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _JobQueueState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_environment_orders: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]] = ..., job_state_time_limit_actions: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[JobQueueTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeEnvironmentOrders")
    def compute_environment_orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]]:
        
        ...
    
    @compute_environment_orders.setter
    def compute_environment_orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueComputeEnvironmentOrderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStateTimeLimitActions")
    def job_state_time_limit_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]]:
        
        ...
    
    @job_state_time_limit_actions.setter
    def job_state_time_limit_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobQueueJobStateTimeLimitActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduling_policy_arn.setter
    def scheduling_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[JobQueueTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[JobQueueTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:batch/jobQueue:JobQueue")
class JobQueue(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compute_environment_orders: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JobQueueComputeEnvironmentOrderArgs, JobQueueComputeEnvironmentOrderArgsDict]]]]] = ..., job_state_time_limit_actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JobQueueJobStateTimeLimitActionArgs, JobQueueJobStateTimeLimitActionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[JobQueueTimeoutsArgs, JobQueueTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JobQueueArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_environment_orders: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JobQueueComputeEnvironmentOrderArgs, JobQueueComputeEnvironmentOrderArgsDict]]]]] = ..., job_state_time_limit_actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[JobQueueJobStateTimeLimitActionArgs, JobQueueJobStateTimeLimitActionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[JobQueueTimeoutsArgs, JobQueueTimeoutsArgsDict]]] = ...) -> JobQueue:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeEnvironmentOrders")
    def compute_environment_orders(self) -> pulumi.Output[Optional[Sequence[outputs.JobQueueComputeEnvironmentOrder]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStateTimeLimitActions")
    def job_state_time_limit_actions(self) -> pulumi.Output[Optional[Sequence[outputs.JobQueueJobStateTimeLimitAction]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPolicyArn")
    def scheduling_policy_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.JobQueueTimeouts]]:
        ...
    


