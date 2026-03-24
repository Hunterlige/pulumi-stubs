

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
__all__ = ['TriggerArgs', 'Trigger']
@pulumi.input_type
class TriggerArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]], type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_batching_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., predicate: Optional[pulumi.Input[TriggerPredicateArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., start_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBatchingConditions")
    def event_batching_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]]:
        
        ...
    
    @event_batching_conditions.setter
    def event_batching_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]]): # -> None:
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
    def predicate(self) -> Optional[pulumi.Input[TriggerPredicateArgs]]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: Optional[pulumi.Input[TriggerPredicateArgs]]): # -> None:
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
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startOnCreation")
    def start_on_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_on_creation.setter
    def start_on_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TriggerState:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_batching_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., predicate: Optional[pulumi.Input[TriggerPredicateArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., start_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBatchingConditions")
    def event_batching_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]]:
        
        ...
    
    @event_batching_conditions.setter
    def event_batching_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerEventBatchingConditionArgs]]]]): # -> None:
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
    def predicate(self) -> Optional[pulumi.Input[TriggerPredicateArgs]]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: Optional[pulumi.Input[TriggerPredicateArgs]]): # -> None:
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
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startOnCreation")
    def start_on_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_on_creation.setter
    def start_on_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/trigger:Trigger")
class Trigger(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerActionArgs, TriggerActionArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_batching_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerEventBatchingConditionArgs, TriggerEventBatchingConditionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., predicate: Optional[pulumi.Input[Union[TriggerPredicateArgs, TriggerPredicateArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., start_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TriggerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerActionArgs, TriggerActionArgsDict]]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_batching_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TriggerEventBatchingConditionArgs, TriggerEventBatchingConditionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., predicate: Optional[pulumi.Input[Union[TriggerPredicateArgs, TriggerPredicateArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., start_on_creation: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Trigger:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.TriggerAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBatchingConditions")
    def event_batching_conditions(self) -> pulumi.Output[Optional[Sequence[outputs.TriggerEventBatchingCondition]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Output[Optional[outputs.TriggerPredicate]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startOnCreation")
    def start_on_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


