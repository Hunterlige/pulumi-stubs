

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], custom_rules: Optional[pulumi.Input[CustomRuleListArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_rules: Optional[pulumi.Input[ManagedRuleSetListArgs]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_settings: Optional[pulumi.Input[PolicySettingsArgs]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[CustomRuleListArgs]]:
        
        ...
    
    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[CustomRuleListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> Optional[pulumi.Input[ManagedRuleSetListArgs]]:
        
        ...
    
    @managed_rules.setter
    def managed_rules(self, value: Optional[pulumi.Input[ManagedRuleSetListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[pulumi.Input[PolicySettingsArgs]]:
        
        ...
    
    @policy_settings.setter
    def policy_settings(self, value: Optional[pulumi.Input[PolicySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:frontdoor:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_rules: Optional[pulumi.Input[Union[CustomRuleListArgs, CustomRuleListArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_rules: Optional[pulumi.Input[Union[ManagedRuleSetListArgs, ManagedRuleSetListArgsDict]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_settings: Optional[pulumi.Input[Union[PolicySettingsArgs, PolicySettingsArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[outputs.CustomRuleListResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendEndpointLinks")
    def frontend_endpoint_links(self) -> pulumi.Output[Sequence[outputs.FrontendEndpointLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Output[Optional[outputs.ManagedRuleSetListResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> pulumi.Output[Optional[outputs.PolicySettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRuleLinks")
    def routing_rule_links(self) -> pulumi.Output[Sequence[outputs.RoutingRuleLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyLinks")
    def security_policy_links(self) -> pulumi.Output[Sequence[outputs.SecurityPolicyLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


