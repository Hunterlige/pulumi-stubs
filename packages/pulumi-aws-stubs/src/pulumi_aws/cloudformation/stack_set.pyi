

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
__all__ = ['StackSetArgs', 'StackSet']
@pulumi.input_type
class StackSetArgs:
    def __init__(__self__, *, administration_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deployment: Optional[pulumi.Input[StackSetAutoDeploymentArgs]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_execution: Optional[pulumi.Input[StackSetManagedExecutionArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., operation_preferences: Optional[pulumi.Input[StackSetOperationPreferencesArgs]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., permission_model: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_body: Optional[pulumi.Input[_builtins.str]] = ..., template_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administration_role_arn.setter
    def administration_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeployment")
    def auto_deployment(self) -> Optional[pulumi.Input[StackSetAutoDeploymentArgs]]:
        
        ...
    
    @auto_deployment.setter
    def auto_deployment(self, value: Optional[pulumi.Input[StackSetAutoDeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @call_as.setter
    def call_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_name.setter
    def execution_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedExecution")
    def managed_execution(self) -> Optional[pulumi.Input[StackSetManagedExecutionArgs]]:
        
        ...
    
    @managed_execution.setter
    def managed_execution(self, value: Optional[pulumi.Input[StackSetManagedExecutionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackSetOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackSetOperationPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionModel")
    def permission_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @permission_model.setter
    def permission_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_url.setter
    def template_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StackSetState:
    def __init__(__self__, *, administration_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deployment: Optional[pulumi.Input[StackSetAutoDeploymentArgs]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_execution: Optional[pulumi.Input[StackSetManagedExecutionArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., operation_preferences: Optional[pulumi.Input[StackSetOperationPreferencesArgs]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., permission_model: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_body: Optional[pulumi.Input[_builtins.str]] = ..., template_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administration_role_arn.setter
    def administration_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeployment")
    def auto_deployment(self) -> Optional[pulumi.Input[StackSetAutoDeploymentArgs]]:
        
        ...
    
    @auto_deployment.setter
    def auto_deployment(self, value: Optional[pulumi.Input[StackSetAutoDeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @call_as.setter
    def call_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_name.setter
    def execution_role_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedExecution")
    def managed_execution(self) -> Optional[pulumi.Input[StackSetManagedExecutionArgs]]:
        
        ...
    
    @managed_execution.setter
    def managed_execution(self, value: Optional[pulumi.Input[StackSetManagedExecutionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> Optional[pulumi.Input[StackSetOperationPreferencesArgs]]:
        
        ...
    
    @operation_preferences.setter
    def operation_preferences(self, value: Optional[pulumi.Input[StackSetOperationPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionModel")
    def permission_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @permission_model.setter
    def permission_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_set_id.setter
    def stack_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_url.setter
    def template_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudformation/stackSet:StackSet")
class StackSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., administration_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deployment: Optional[pulumi.Input[Union[StackSetAutoDeploymentArgs, StackSetAutoDeploymentArgsDict]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_execution: Optional[pulumi.Input[Union[StackSetManagedExecutionArgs, StackSetManagedExecutionArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackSetOperationPreferencesArgs, StackSetOperationPreferencesArgsDict]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., permission_model: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_body: Optional[pulumi.Input[_builtins.str]] = ..., template_url: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[StackSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., administration_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_deployment: Optional[pulumi.Input[Union[StackSetAutoDeploymentArgs, StackSetAutoDeploymentArgsDict]]] = ..., call_as: Optional[pulumi.Input[_builtins.str]] = ..., capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., execution_role_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_execution: Optional[pulumi.Input[Union[StackSetManagedExecutionArgs, StackSetManagedExecutionArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., operation_preferences: Optional[pulumi.Input[Union[StackSetOperationPreferencesArgs, StackSetOperationPreferencesArgsDict]]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., permission_model: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stack_set_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_body: Optional[pulumi.Input[_builtins.str]] = ..., template_url: Optional[pulumi.Input[_builtins.str]] = ...) -> StackSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrationRoleArn")
    def administration_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeployment")
    def auto_deployment(self) -> pulumi.Output[Optional[outputs.StackSetAutoDeployment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAs")
    def call_as(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleName")
    def execution_role_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedExecution")
    def managed_execution(self) -> pulumi.Output[Optional[outputs.StackSetManagedExecution]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationPreferences")
    def operation_preferences(self) -> pulumi.Output[Optional[outputs.StackSetOperationPreferences]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionModel")
    def permission_model(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackSetId")
    def stack_set_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="templateBody")
    def template_body(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


