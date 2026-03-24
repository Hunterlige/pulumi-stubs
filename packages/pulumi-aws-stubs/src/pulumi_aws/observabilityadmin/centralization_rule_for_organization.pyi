

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CentralizationRuleForOrganizationArgs', 'CentralizationRuleForOrganization']
@pulumi.input_type
class CentralizationRuleForOrganizationArgs:
    def __init__(__self__, *, rule: pulumi.Input[CentralizationRuleForOrganizationRuleArgs], rule_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[CentralizationRuleForOrganizationRuleArgs]:
        
        ...
    
    @rule.setter
    def rule(self, value: pulumi.Input[CentralizationRuleForOrganizationRuleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CentralizationRuleForOrganizationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleArgs]] = ..., rule_arn: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]] = ...) -> None:
        
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
    def rule(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_arn.setter
    def rule_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CentralizationRuleForOrganization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[CentralizationRuleForOrganizationRuleArgs, CentralizationRuleForOrganizationRuleArgsDict]]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CentralizationRuleForOrganizationTimeoutsArgs, CentralizationRuleForOrganizationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CentralizationRuleForOrganizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[CentralizationRuleForOrganizationRuleArgs, CentralizationRuleForOrganizationRuleArgsDict]]] = ..., rule_arn: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CentralizationRuleForOrganizationTimeoutsArgs, CentralizationRuleForOrganizationTimeoutsArgsDict]]] = ...) -> CentralizationRuleForOrganization:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[outputs.CentralizationRuleForOrganizationRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.CentralizationRuleForOrganizationTimeouts]]:
        ...
    


