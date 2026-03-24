

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MaintenanceWindowTaskArgs', 'MaintenanceWindowTask']
@pulumi.input_type
class MaintenanceWindowTaskArgs:
    def __init__(__self__, *, task_arn: pulumi.Input[_builtins.str], task_type: pulumi.Input[_builtins.str], window_id: pulumi.Input[_builtins.str], cutoff_behavior: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.str]] = ..., max_errors: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]] = ..., task_invocation_parameters: Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskArn")
    def task_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_arn.setter
    def task_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @window_id.setter
    def window_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cutoffBehavior")
    def cutoff_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cutoff_behavior.setter
    def cutoff_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_errors.setter
    def max_errors(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskInvocationParameters")
    def task_invocation_parameters(self) -> Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]]:
        
        ...
    
    @task_invocation_parameters.setter
    def task_invocation_parameters(self, value: Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _MaintenanceWindowTaskState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cutoff_behavior: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.str]] = ..., max_errors: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]] = ..., task_arn: Optional[pulumi.Input[_builtins.str]] = ..., task_invocation_parameters: Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]] = ..., task_type: Optional[pulumi.Input[_builtins.str]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ..., window_task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cutoffBehavior")
    def cutoff_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cutoff_behavior.setter
    def cutoff_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_errors.setter
    def max_errors(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowTaskTargetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskArn")
    def task_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_arn.setter
    def task_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskInvocationParameters")
    def task_invocation_parameters(self) -> Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]]:
        
        ...
    
    @task_invocation_parameters.setter
    def task_invocation_parameters(self, value: Optional[pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @window_id.setter
    def window_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowTaskId")
    def window_task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @window_task_id.setter
    def window_task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MaintenanceWindowTask(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cutoff_behavior: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.str]] = ..., max_errors: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MaintenanceWindowTaskTargetArgs, MaintenanceWindowTaskTargetArgsDict]]]]] = ..., task_arn: Optional[pulumi.Input[_builtins.str]] = ..., task_invocation_parameters: Optional[pulumi.Input[Union[MaintenanceWindowTaskTaskInvocationParametersArgs, MaintenanceWindowTaskTaskInvocationParametersArgsDict]]] = ..., task_type: Optional[pulumi.Input[_builtins.str]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MaintenanceWindowTaskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cutoff_behavior: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.str]] = ..., max_errors: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MaintenanceWindowTaskTargetArgs, MaintenanceWindowTaskTargetArgsDict]]]]] = ..., task_arn: Optional[pulumi.Input[_builtins.str]] = ..., task_invocation_parameters: Optional[pulumi.Input[Union[MaintenanceWindowTaskTaskInvocationParametersArgs, MaintenanceWindowTaskTaskInvocationParametersArgsDict]]] = ..., task_type: Optional[pulumi.Input[_builtins.str]] = ..., window_id: Optional[pulumi.Input[_builtins.str]] = ..., window_task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> MaintenanceWindowTask:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cutoffBehavior")
    def cutoff_behavior(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Optional[Sequence[outputs.MaintenanceWindowTaskTarget]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskArn")
    def task_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskInvocationParameters")
    def task_invocation_parameters(self) -> pulumi.Output[Optional[outputs.MaintenanceWindowTaskTaskInvocationParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowId")
    def window_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowTaskId")
    def window_task_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


