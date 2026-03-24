

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
__all__ = ['StackInstancesArgs', 'StackInstances']
@pulumi.input_type
class StackInstancesArgs:
    def __init__(__self__, *, stack_set_name: pulumi.Input[_builtins.str], accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]] = ..., operation_preferences: Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retain_stacks: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stack_set_name.setter
    def stack_set_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @call_as.setter
    def call_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTargets")
    def deployment_targets(self) -> Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]]:
        
        ...
    
    @deployment_targets.setter
    def deployment_targets(self, value: Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameter_overrides.setter
    def parameter_overrides(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStacks")
    def retain_stacks(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_stacks.setter
    def retain_stacks(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _StackInstancesState:
    def __init__(__self__, *, accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]] = ..., operation_preferences: Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retain_stacks: Optional[pulumi.Input[_builtins.bool]] = ..., stack_instance_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[StackInstancesStackInstanceSummaryArgs]]]] = ..., stack_set_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @call_as.setter
    def call_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTargets")
    def deployment_targets(self) -> Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]]:
        
        ...
    
    @deployment_targets.setter
    def deployment_targets(self, value: Optional[pulumi.Input[StackInstancesDeploymentTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackInstancesOperationPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameter_overrides.setter
    def parameter_overrides(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStacks")
    def retain_stacks(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_stacks.setter
    def retain_stacks(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackInstanceSummaries")
    def stack_instance_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackInstancesStackInstanceSummaryArgs]]]]:
        
        ...
    
    @stack_instance_summaries.setter
    def stack_instance_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackInstancesStackInstanceSummaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_id.setter
    def stack_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudformation/stackInstances:StackInstances")
class StackInstances(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[Union[StackInstancesDeploymentTargetsArgs, StackInstancesDeploymentTargetsArgsDict]]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackInstancesOperationPreferencesArgs, StackInstancesOperationPreferencesArgsDict]]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retain_stacks: Optional[pulumi.Input[_builtins.bool]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StackInstancesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[Union[StackInstancesDeploymentTargetsArgs, StackInstancesDeploymentTargetsArgsDict]]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackInstancesOperationPreferencesArgs, StackInstancesOperationPreferencesArgsDict]]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retain_stacks: Optional[pulumi.Input[_builtins.bool]] = ..., stack_instance_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackInstancesStackInstanceSummaryArgs, StackInstancesStackInstanceSummaryArgsDict]]]]] = ..., stack_set_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...) -> StackInstances:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTargets")
    def deployment_targets(self) -> pulumi.Output[Optional[outputs.StackInstancesDeploymentTargets]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> pulumi.Output[Optional[outputs.StackInstancesOperationPreferences]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStacks")
    def retain_stacks(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackInstanceSummaries")
    def stack_instance_summaries(self) -> pulumi.Output[Sequence[outputs.StackInstancesStackInstanceSummary]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


