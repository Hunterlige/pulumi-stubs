

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
__all__ = ['FirewallPolicyWithRulesArgs', 'FirewallPolicyWithRules']
@pulumi.input_type
class FirewallPolicyWithRulesArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], rules: pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]], short_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FirewallPolicyWithRulesState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., predefined_rules: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesPredefinedRuleArgs]]]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedRules")
    def predefined_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesPredefinedRuleArgs]]]]:
        
        ...
    
    @predefined_rules.setter
    def predefined_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesPredefinedRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyWithRulesRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link_with_id.setter
    def self_link_with_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FirewallPolicyWithRules(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyWithRulesRuleArgs, FirewallPolicyWithRulesRuleArgsDict]]]]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallPolicyWithRulesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., predefined_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyWithRulesPredefinedRuleArgs, FirewallPolicyWithRulesPredefinedRuleArgsDict]]]]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyWithRulesRuleArgs, FirewallPolicyWithRulesRuleArgsDict]]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ...) -> FirewallPolicyWithRules:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedRules")
    def predefined_rules(self) -> pulumi.Output[Sequence[outputs.FirewallPolicyWithRulesPredefinedRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[outputs.FirewallPolicyWithRulesRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


