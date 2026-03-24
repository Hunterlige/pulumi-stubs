

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationManagedRuleArgs', 'OrganizationManagedRule']
@pulumi.input_type
class OrganizationManagedRuleArgs:
    def __init__(__self__, *, rule_identifier: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_parameters: Optional[pulumi.Input[_builtins.str]] = ..., maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ..., resource_types_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ..., tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleIdentifier")
    def rule_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_identifier.setter
    def rule_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id_scope.setter
    def resource_id_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types_scopes.setter
    def resource_types_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_key_scope.setter
    def tag_key_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_value_scope.setter
    def tag_value_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationManagedRuleState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_parameters: Optional[pulumi.Input[_builtins.str]] = ..., maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ..., resource_types_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., rule_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ..., tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_parameters.setter
    def input_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id_scope.setter
    def resource_id_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types_scopes.setter
    def resource_types_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleIdentifier")
    def rule_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_identifier.setter
    def rule_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_key_scope.setter
    def tag_key_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_value_scope.setter
    def tag_value_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OrganizationManagedRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_parameters: Optional[pulumi.Input[_builtins.str]] = ..., maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ..., resource_types_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., rule_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ..., tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationManagedRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_parameters: Optional[pulumi.Input[_builtins.str]] = ..., maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id_scope: Optional[pulumi.Input[_builtins.str]] = ..., resource_types_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., rule_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tag_key_scope: Optional[pulumi.Input[_builtins.str]] = ..., tag_value_scope: Optional[pulumi.Input[_builtins.str]] = ...) -> OrganizationManagedRule:
        
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
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdScope")
    def resource_id_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypesScopes")
    def resource_types_scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleIdentifier")
    def rule_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKeyScope")
    def tag_key_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValueScope")
    def tag_value_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


