

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallPolicyRuleGroupArgs', 'FirewallPolicyRuleGroup']
@pulumi.input_type
class FirewallPolicyRuleGroupArgs:
    def __init__(__self__, *, firewall_policy_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., rule_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyFilterRuleArgs, FirewallPolicyNatRuleArgs]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyName")
    def firewall_policy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @firewall_policy_name.setter
    def firewall_policy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroupName")
    def rule_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_group_name.setter
    def rule_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyFilterRuleArgs, FirewallPolicyNatRuleArgs]]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyFilterRuleArgs, FirewallPolicyNatRuleArgs]]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:FirewallPolicyRuleGroup")
class FirewallPolicyRuleGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union[FirewallPolicyFilterRuleArgs, FirewallPolicyFilterRuleArgsDict], Union[FirewallPolicyNatRuleArgs, FirewallPolicyNatRuleArgsDict]]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallPolicyRuleGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FirewallPolicyRuleGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


