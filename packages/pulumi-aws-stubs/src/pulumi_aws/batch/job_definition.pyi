

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
__all__ = ['JobDefinitionArgs', 'JobDefinition']
@pulumi.input_type
class JobDefinitionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], container_properties: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_new_revision: Optional[pulumi.Input[_builtins.bool]] = ..., ecs_properties: Optional[pulumi.Input[_builtins.str]] = ..., eks_properties: Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_properties: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retry_strategy: Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]] = ..., scheduling_priority: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout: Optional[pulumi.Input[JobDefinitionTimeoutArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_properties.setter
    def container_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnNewRevision")
    def deregister_on_new_revision(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deregister_on_new_revision.setter
    def deregister_on_new_revision(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsProperties")
    def ecs_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ecs_properties.setter
    def ecs_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksProperties")
    def eks_properties(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]]:
        
        ...
    
    @eks_properties.setter
    def eks_properties(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_properties.setter
    def node_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @platform_capabilities.setter
    def platform_capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]]:
        
        ...
    
    @retry_strategy.setter
    def retry_strategy(self, value: Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scheduling_priority.setter
    def scheduling_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def timeout(self) -> Optional[pulumi.Input[JobDefinitionTimeoutArgs]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[JobDefinitionTimeoutArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _JobDefinitionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., arn_prefix: Optional[pulumi.Input[_builtins.str]] = ..., container_properties: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_new_revision: Optional[pulumi.Input[_builtins.bool]] = ..., ecs_properties: Optional[pulumi.Input[_builtins.str]] = ..., eks_properties: Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_properties: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retry_strategy: Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]] = ..., revision: Optional[pulumi.Input[_builtins.int]] = ..., scheduling_priority: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout: Optional[pulumi.Input[JobDefinitionTimeoutArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arnPrefix")
    def arn_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn_prefix.setter
    def arn_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_properties.setter
    def container_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnNewRevision")
    def deregister_on_new_revision(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deregister_on_new_revision.setter
    def deregister_on_new_revision(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsProperties")
    def ecs_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ecs_properties.setter
    def ecs_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksProperties")
    def eks_properties(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]]:
        
        ...
    
    @eks_properties.setter
    def eks_properties(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_properties.setter
    def node_properties(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @platform_capabilities.setter
    def platform_capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]]:
        
        ...
    
    @retry_strategy.setter
    def retry_strategy(self, value: Optional[pulumi.Input[JobDefinitionRetryStrategyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scheduling_priority.setter
    def scheduling_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def timeout(self) -> Optional[pulumi.Input[JobDefinitionTimeoutArgs]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[JobDefinitionTimeoutArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:batch/jobDefinition:JobDefinition")
class JobDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., container_properties: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_new_revision: Optional[pulumi.Input[_builtins.bool]] = ..., ecs_properties: Optional[pulumi.Input[_builtins.str]] = ..., eks_properties: Optional[pulumi.Input[Union[JobDefinitionEksPropertiesArgs, JobDefinitionEksPropertiesArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_properties: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retry_strategy: Optional[pulumi.Input[Union[JobDefinitionRetryStrategyArgs, JobDefinitionRetryStrategyArgsDict]]] = ..., scheduling_priority: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout: Optional[pulumi.Input[Union[JobDefinitionTimeoutArgs, JobDefinitionTimeoutArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: JobDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., arn_prefix: Optional[pulumi.Input[_builtins.str]] = ..., container_properties: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_new_revision: Optional[pulumi.Input[_builtins.bool]] = ..., ecs_properties: Optional[pulumi.Input[_builtins.str]] = ..., eks_properties: Optional[pulumi.Input[Union[JobDefinitionEksPropertiesArgs, JobDefinitionEksPropertiesArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_properties: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., platform_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retry_strategy: Optional[pulumi.Input[Union[JobDefinitionRetryStrategyArgs, JobDefinitionRetryStrategyArgsDict]]] = ..., revision: Optional[pulumi.Input[_builtins.int]] = ..., scheduling_priority: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeout: Optional[pulumi.Input[Union[JobDefinitionTimeoutArgs, JobDefinitionTimeoutArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> JobDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arnPrefix")
    def arn_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerProperties")
    def container_properties(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnNewRevision")
    def deregister_on_new_revision(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsProperties")
    def ecs_properties(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksProperties")
    def eks_properties(self) -> pulumi.Output[Optional[outputs.JobDefinitionEksProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeProperties")
    def node_properties(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformCapabilities")
    def platform_capabilities(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> pulumi.Output[Optional[outputs.JobDefinitionRetryStrategy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    def timeout(self) -> pulumi.Output[Optional[outputs.JobDefinitionTimeout]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


