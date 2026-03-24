

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
__all__ = ['WebApplicationFirewallPolicyArgs', 'WebApplicationFirewallPolicy']
@pulumi.input_type
class WebApplicationFirewallPolicyArgs:
    def __init__(__self__, *, managed_rules: pulumi.Input[ManagedRulesDefinitionArgs], resource_group_name: pulumi.Input[_builtins.str], custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[WebApplicationFirewallCustomRuleArgs]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_settings: Optional[pulumi.Input[PolicySettingsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Input[ManagedRulesDefinitionArgs]:
        
        ...
    
    @managed_rules.setter
    def managed_rules(self, value: pulumi.Input[ManagedRulesDefinitionArgs]): # -> None:
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
    def custom_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebApplicationFirewallCustomRuleArgs]]]]:
        
        ...
    
    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebApplicationFirewallCustomRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:WebApplicationFirewallPolicy")
class WebApplicationFirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebApplicationFirewallCustomRuleArgs, WebApplicationFirewallCustomRuleArgsDict]]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_rules: Optional[pulumi.Input[Union[ManagedRulesDefinitionArgs, ManagedRulesDefinitionArgsDict]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_settings: Optional[pulumi.Input[Union[PolicySettingsArgs, PolicySettingsArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebApplicationFirewallPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebApplicationFirewallPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayForContainers")
    def application_gateway_for_containers(self) -> pulumi.Output[Sequence[outputs.ApplicationGatewayForContainersReferenceDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGateways")
    def application_gateways(self) -> pulumi.Output[Sequence[outputs.ApplicationGatewayResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[Sequence[outputs.WebApplicationFirewallCustomRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Output[outputs.ManagedRulesDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathBasedRules")
    def path_based_rules(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


