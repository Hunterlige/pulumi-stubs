

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
__all__ = ['AutomationRuleArgs', 'AutomationRule']
@pulumi.input_type
class AutomationRuleArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]], criteria: pulumi.Input[AutomationRuleCriteriaArgs], description: pulumi.Input[_builtins.str], rule_name: pulumi.Input[_builtins.str], rule_order: pulumi.Input[_builtins.int], is_terminal: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Input[AutomationRuleCriteriaArgs]:
        
        ...
    
    @criteria.setter
    def criteria(self, value: pulumi.Input[AutomationRuleCriteriaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_order.setter
    def rule_order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTerminal")
    def is_terminal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_terminal.setter
    def is_terminal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleStatus")
    def rule_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_status.setter
    def rule_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AutomationRuleState:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., criteria: Optional[pulumi.Input[AutomationRuleCriteriaArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_terminal: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_order: Optional[pulumi.Input[_builtins.int]] = ..., rule_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationRuleActionArgs]]]]): # -> None:
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
    def criteria(self) -> Optional[pulumi.Input[AutomationRuleCriteriaArgs]]:
        
        ...
    
    @criteria.setter
    def criteria(self, value: Optional[pulumi.Input[AutomationRuleCriteriaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTerminal")
    def is_terminal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_terminal.setter
    def is_terminal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_order.setter
    def rule_order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleStatus")
    def rule_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_status.setter
    def rule_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:securityhub/automationRule:AutomationRule")
class AutomationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AutomationRuleActionArgs, AutomationRuleActionArgsDict]]]]] = ..., criteria: Optional[pulumi.Input[Union[AutomationRuleCriteriaArgs, AutomationRuleCriteriaArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_terminal: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_order: Optional[pulumi.Input[_builtins.int]] = ..., rule_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AutomationRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AutomationRuleActionArgs, AutomationRuleActionArgsDict]]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., criteria: Optional[pulumi.Input[Union[AutomationRuleCriteriaArgs, AutomationRuleCriteriaArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_terminal: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_order: Optional[pulumi.Input[_builtins.int]] = ..., rule_status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> AutomationRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.AutomationRuleAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Output[outputs.AutomationRuleCriteria]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTerminal")
    def is_terminal(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleStatus")
    def rule_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    


