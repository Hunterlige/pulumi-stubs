

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StackSetInstanceArgs', 'StackSetInstance']
@pulumi.input_type
class StackSetInstanceArgs:
    def __init__(__self__, *, stack_set_name: pulumi.Input[_builtins.str], account_id: Optional[pulumi.Input[_builtins.str]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]] = ..., operation_preferences: Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retain_stack: Optional[pulumi.Input[_builtins.bool]] = ..., stack_set_instance_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stack_set_name.setter
    def stack_set_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def deployment_targets(self) -> Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]]:
        
        ...
    
    @deployment_targets.setter
    def deployment_targets(self, value: Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]]): # -> None:
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
    @_utilities.deprecated(...)
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStack")
    def retain_stack(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_stack.setter
    def retain_stack(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetInstanceRegion")
    def stack_set_instance_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_instance_region.setter
    def stack_set_instance_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StackSetInstanceState:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]] = ..., operation_preferences: Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]] = ..., organizational_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retain_stack: Optional[pulumi.Input[_builtins.bool]] = ..., stack_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_instance_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[StackSetInstanceStackInstanceSummaryArgs]]]] = ..., stack_set_instance_region: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def deployment_targets(self) -> Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]]:
        
        ...
    
    @deployment_targets.setter
    def deployment_targets(self, value: Optional[pulumi.Input[StackSetInstanceDeploymentTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackSetInstanceOperationPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit_id.setter
    def organizational_unit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @_utilities.deprecated(...)
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStack")
    def retain_stack(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_stack.setter
    def retain_stack(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_id.setter
    def stack_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackInstanceSummaries")
    def stack_instance_summaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StackSetInstanceStackInstanceSummaryArgs]]]]:
        
        ...
    
    @stack_instance_summaries.setter
    def stack_instance_summaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StackSetInstanceStackInstanceSummaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetInstanceRegion")
    def stack_set_instance_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_instance_region.setter
    def stack_set_instance_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_name.setter
    def stack_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class StackSetInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[Union[StackSetInstanceDeploymentTargetsArgs, StackSetInstanceDeploymentTargetsArgsDict]]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackSetInstanceOperationPreferencesArgs, StackSetInstanceOperationPreferencesArgsDict]]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retain_stack: Optional[pulumi.Input[_builtins.bool]] = ..., stack_set_instance_region: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StackSetInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., deployment_targets: Optional[pulumi.Input[Union[StackSetInstanceDeploymentTargetsArgs, StackSetInstanceDeploymentTargetsArgsDict]]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackSetInstanceOperationPreferencesArgs, StackSetInstanceOperationPreferencesArgsDict]]] = ..., organizational_unit_id: Optional[pulumi.Input[_builtins.str]] = ..., parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retain_stack: Optional[pulumi.Input[_builtins.bool]] = ..., stack_id: Optional[pulumi.Input[_builtins.str]] = ..., stack_instance_summaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StackSetInstanceStackInstanceSummaryArgs, StackSetInstanceStackInstanceSummaryArgsDict]]]]] = ..., stack_set_instance_region: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_name: Optional[pulumi.Input[_builtins.str]] = ...) -> StackSetInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTargets")
    def deployment_targets(self) -> pulumi.Output[Optional[outputs.StackSetInstanceDeploymentTargets]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> pulumi.Output[Optional[outputs.StackSetInstanceOperationPreferences]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitId")
    def organizational_unit_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainStack")
    def retain_stack(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackInstanceSummaries")
    def stack_instance_summaries(self) -> pulumi.Output[Sequence[outputs.StackSetInstanceStackInstanceSummary]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetInstanceRegion")
    def stack_set_instance_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


