

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
__all__ = ['BlockPublicAccessConfigurationArgs', 'BlockPublicAccessConfiguration']
@pulumi.input_type
class BlockPublicAccessConfigurationArgs:
    def __init__(__self__, *, block_public_security_group_rules: pulumi.Input[_builtins.bool], permitted_public_security_group_rule_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicSecurityGroupRules")
    def block_public_security_group_rules(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @block_public_security_group_rules.setter
    def block_public_security_group_rules(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permittedPublicSecurityGroupRuleRanges")
    def permitted_public_security_group_rule_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]]:
        
        ...
    
    @permitted_public_security_group_rule_ranges.setter
    def permitted_public_security_group_rule_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BlockPublicAccessConfigurationState:
    def __init__(__self__, *, block_public_security_group_rules: Optional[pulumi.Input[_builtins.bool]] = ..., permitted_public_security_group_rule_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicSecurityGroupRules")
    def block_public_security_group_rules(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_security_group_rules.setter
    def block_public_security_group_rules(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permittedPublicSecurityGroupRuleRanges")
    def permitted_public_security_group_rule_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]]:
        
        ...
    
    @permitted_public_security_group_rule_ranges.setter
    def permitted_public_security_group_rule_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BlockPublicAccessConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., block_public_security_group_rules: Optional[pulumi.Input[_builtins.bool]] = ..., permitted_public_security_group_rule_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs, BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlockPublicAccessConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., block_public_security_group_rules: Optional[pulumi.Input[_builtins.bool]] = ..., permitted_public_security_group_rule_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs, BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BlockPublicAccessConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicSecurityGroupRules")
    def block_public_security_group_rules(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permittedPublicSecurityGroupRuleRanges")
    def permitted_public_security_group_rule_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRange]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


