

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
__all__ = ['OrganizationSecurityPolicyRuleArgs', 'OrganizationSecurityPolicyRule']
@pulumi.input_type
class OrganizationSecurityPolicyRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], match: pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs], policy_id: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs]:
        
        ...
    
    @match.setter
    def match(self, value: pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
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
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationSecurityPolicyRuleState:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match: Optional[pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs]]:
        
        ...
    
    @match.setter
    def match(self, value: Optional[pulumi.Input[OrganizationSecurityPolicyRuleMatchArgs]]): # -> None:
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
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OrganizationSecurityPolicyRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match: Optional[pulumi.Input[Union[OrganizationSecurityPolicyRuleMatchArgs, OrganizationSecurityPolicyRuleMatchArgsDict]]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationSecurityPolicyRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., match: Optional[pulumi.Input[Union[OrganizationSecurityPolicyRuleMatchArgs, OrganizationSecurityPolicyRuleMatchArgsDict]]] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> OrganizationSecurityPolicyRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Output[outputs.OrganizationSecurityPolicyRuleMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


