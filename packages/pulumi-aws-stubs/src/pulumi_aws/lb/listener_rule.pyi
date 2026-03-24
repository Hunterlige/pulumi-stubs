

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
__all__ = ['ListenerRuleArgs', 'ListenerRule']
@pulumi.input_type
class ListenerRuleArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]], conditions: pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]], listener_arn: pulumi.Input[_builtins.str], priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @listener_arn.setter
    def listener_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ListenerRuleState:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionArgs]]]]): # -> None:
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
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @listener_arn.setter
    def listener_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleTransformArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:lb/listenerRule:ListenerRule")
class ListenerRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleActionArgs, ListenerRuleActionArgsDict]]]]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleConditionArgs, ListenerRuleConditionArgsDict]]]]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleTransformArgs, ListenerRuleTransformArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ListenerRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleActionArgs, ListenerRuleActionArgsDict]]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleConditionArgs, ListenerRuleConditionArgsDict]]]]] = ..., listener_arn: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListenerRuleTransformArgs, ListenerRuleTransformArgsDict]]]]] = ...) -> ListenerRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.ListenerRuleAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.ListenerRuleCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> pulumi.Output[Optional[Sequence[outputs.ListenerRuleTransform]]]:
        
        ...
    


