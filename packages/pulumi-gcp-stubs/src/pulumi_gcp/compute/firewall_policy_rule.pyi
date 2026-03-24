

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
__all__ = ['FirewallPolicyRuleArgs', 'FirewallPolicyRule']
@pulumi.input_type
class FirewallPolicyRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], direction: pulumi.Input[_builtins.str], firewall_policy: pulumi.Input[_builtins.str], match: pulumi.Input[FirewallPolicyRuleMatchArgs], priority: pulumi.Input[_builtins.int], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., security_profile_group: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_secure_tags: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
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
    def direction(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @direction.setter
    def direction(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @firewall_policy.setter
    def firewall_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[FirewallPolicyRuleMatchArgs]:
        
        ...
    
    @match.setter
    def match(self, value: pulumi.Input[FirewallPolicyRuleMatchArgs]): # -> None:
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
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_profile_group.setter
    def security_profile_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]]:
        
        ...
    
    @target_secure_tags.setter
    def target_secure_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_inspect.setter
    def tls_inspect(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _FirewallPolicyRuleState:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., firewall_policy: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., match: Optional[pulumi.Input[FirewallPolicyRuleMatchArgs]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., security_profile_group: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_secure_tags: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[FirewallPolicyRuleMatchArgs]]:
        
        ...
    
    @match.setter
    def match(self, value: Optional[pulumi.Input[FirewallPolicyRuleMatchArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_profile_group.setter
    def security_profile_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]]:
        
        ...
    
    @target_secure_tags.setter
    def target_secure_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallPolicyRuleTargetSecureTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @tls_inspect.setter
    def tls_inspect(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/firewallPolicyRule:FirewallPolicyRule")
class FirewallPolicyRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., firewall_policy: Optional[pulumi.Input[_builtins.str]] = ..., match: Optional[pulumi.Input[Union[FirewallPolicyRuleMatchArgs, FirewallPolicyRuleMatchArgsDict]]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., security_profile_group: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_secure_tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyRuleTargetSecureTagArgs, FirewallPolicyRuleTargetSecureTagArgsDict]]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallPolicyRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., firewall_policy: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., match: Optional[pulumi.Input[Union[FirewallPolicyRuleMatchArgs, FirewallPolicyRuleMatchArgsDict]]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., security_profile_group: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_secure_tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallPolicyRuleTargetSecureTagArgs, FirewallPolicyRuleTargetSecureTagArgsDict]]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...) -> FirewallPolicyRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]:
        
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
    def direction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Output[outputs.FirewallPolicyRuleMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(self) -> pulumi.Output[Optional[Sequence[outputs.FirewallPolicyRuleTargetSecureTag]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


