

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
__all__ = ['RuleGroupArgs', 'RuleGroup']
@pulumi.input_type
class RuleGroupArgs:
    def __init__(__self__, *, capacity: pulumi.Input[_builtins.int], scope: pulumi.Input[_builtins.str], visibility_config: pulumi.Input[RuleGroupVisibilityConfigArgs], custom_response_bodies: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]] = ..., rules_json: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Input[RuleGroupVisibilityConfigArgs]:
        
        ...
    
    @visibility_config.setter
    def visibility_config(self, value: pulumi.Input[RuleGroupVisibilityConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]]:
        
        ...
    
    @custom_response_bodies.setter
    def custom_response_bodies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesJson")
    def rules_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rules_json.setter
    def rules_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _RuleGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity: Optional[pulumi.Input[_builtins.int]] = ..., custom_response_bodies: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., lock_token: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]] = ..., rules_json: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., visibility_config: Optional[pulumi.Input[RuleGroupVisibilityConfigArgs]] = ...) -> None:
        
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
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]]:
        
        ...
    
    @custom_response_bodies.setter
    def custom_response_bodies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupCustomResponseBodyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lockToken")
    def lock_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @lock_token.setter
    def lock_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesJson")
    def rules_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rules_json.setter
    def rules_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> Optional[pulumi.Input[RuleGroupVisibilityConfigArgs]]:
        
        ...
    
    @visibility_config.setter
    def visibility_config(self, value: Optional[pulumi.Input[RuleGroupVisibilityConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:wafv2/ruleGroup:RuleGroup")
class RuleGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity: Optional[pulumi.Input[_builtins.int]] = ..., custom_response_bodies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RuleGroupCustomResponseBodyArgs, RuleGroupCustomResponseBodyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RuleGroupRuleArgs, RuleGroupRuleArgsDict]]]]] = ..., rules_json: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., visibility_config: Optional[pulumi.Input[Union[RuleGroupVisibilityConfigArgs, RuleGroupVisibilityConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RuleGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity: Optional[pulumi.Input[_builtins.int]] = ..., custom_response_bodies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RuleGroupCustomResponseBodyArgs, RuleGroupCustomResponseBodyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., lock_token: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RuleGroupRuleArgs, RuleGroupRuleArgsDict]]]]] = ..., rules_json: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., visibility_config: Optional[pulumi.Input[Union[RuleGroupVisibilityConfigArgs, RuleGroupVisibilityConfigArgsDict]]] = ...) -> RuleGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> pulumi.Output[Optional[Sequence[outputs.RuleGroupCustomResponseBody]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lockToken")
    def lock_token(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.RuleGroupRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesJson")
    def rules_json(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Output[outputs.RuleGroupVisibilityConfig]:
        
        ...
    


