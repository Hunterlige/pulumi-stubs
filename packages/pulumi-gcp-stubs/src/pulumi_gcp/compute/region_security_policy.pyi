

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
__all__ = ['RegionSecurityPolicyArgs', 'RegionSecurityPolicy']
@pulumi.input_type
class RegionSecurityPolicyArgs:
    def __init__(__self__, *, advanced_options_config: Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]] = ..., ddos_protection_config: Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(self) -> Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]]:
        
        ...
    
    @advanced_options_config.setter
    def advanced_options_config(self, value: Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddosProtectionConfig")
    def ddos_protection_config(self) -> Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]]:
        
        ...
    
    @ddos_protection_config.setter
    def ddos_protection_config(self, value: Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]]): # -> None:
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]]:
        
        ...
    
    @user_defined_fields.setter
    def user_defined_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionSecurityPolicyState:
    def __init__(__self__, *, advanced_options_config: Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]] = ..., ddos_protection_config: Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(self) -> Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]]:
        
        ...
    
    @advanced_options_config.setter
    def advanced_options_config(self, value: Optional[pulumi.Input[RegionSecurityPolicyAdvancedOptionsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddosProtectionConfig")
    def ddos_protection_config(self) -> Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]]:
        
        ...
    
    @ddos_protection_config.setter
    def ddos_protection_config(self, value: Optional[pulumi.Input[RegionSecurityPolicyDdosProtectionConfigArgs]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithPolicyId")
    def self_link_with_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link_with_policy_id.setter
    def self_link_with_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]]:
        
        ...
    
    @user_defined_fields.setter
    def user_defined_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionSecurityPolicyUserDefinedFieldArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionSecurityPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., advanced_options_config: Optional[pulumi.Input[Union[RegionSecurityPolicyAdvancedOptionsConfigArgs, RegionSecurityPolicyAdvancedOptionsConfigArgsDict]]] = ..., ddos_protection_config: Optional[pulumi.Input[Union[RegionSecurityPolicyDdosProtectionConfigArgs, RegionSecurityPolicyDdosProtectionConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionSecurityPolicyRuleArgs, RegionSecurityPolicyRuleArgsDict]]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionSecurityPolicyUserDefinedFieldArgs, RegionSecurityPolicyUserDefinedFieldArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[RegionSecurityPolicyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., advanced_options_config: Optional[pulumi.Input[Union[RegionSecurityPolicyAdvancedOptionsConfigArgs, RegionSecurityPolicyAdvancedOptionsConfigArgsDict]]] = ..., ddos_protection_config: Optional[pulumi.Input[Union[RegionSecurityPolicyDdosProtectionConfigArgs, RegionSecurityPolicyDdosProtectionConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionSecurityPolicyRuleArgs, RegionSecurityPolicyRuleArgsDict]]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_defined_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionSecurityPolicyUserDefinedFieldArgs, RegionSecurityPolicyUserDefinedFieldArgsDict]]]]] = ...) -> RegionSecurityPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(self) -> pulumi.Output[Optional[outputs.RegionSecurityPolicyAdvancedOptionsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddosProtectionConfig")
    def ddos_protection_config(self) -> pulumi.Output[Optional[outputs.RegionSecurityPolicyDdosProtectionConfig]]:
        
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
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[outputs.RegionSecurityPolicyRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithPolicyId")
    def self_link_with_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> pulumi.Output[Optional[Sequence[outputs.RegionSecurityPolicyUserDefinedField]]]:
        
        ...
    


