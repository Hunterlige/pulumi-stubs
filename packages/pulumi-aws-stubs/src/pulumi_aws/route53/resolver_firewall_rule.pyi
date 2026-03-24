import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResolverFirewallRuleArgs", "ResolverFirewallRule"]

@pulumi.input_type
class ResolverFirewallRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        firewall_rule_group_id: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        block_override_dns_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        block_response: Optional[pulumi.Input[_builtins.str]] = ...,
        confidence_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_threat_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_redirection_action: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        q_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @firewall_rule_group_id.setter
    def firewall_rule_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDnsType")
    def block_override_dns_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_override_dns_type.setter
    def block_override_dns_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDomain")
    def block_override_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_override_domain.setter
    def block_override_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideTtl")
    def block_override_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_override_ttl.setter
    def block_override_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="blockResponse")
    def block_response(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_response.setter
    def block_response(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsThreatProtection")
    def dns_threat_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_threat_protection.setter
    def dns_threat_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_domain_list_id.setter
    def firewall_domain_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainRedirectionAction")
    def firewall_domain_redirection_action(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_domain_redirection_action.setter
    def firewall_domain_redirection_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qType")
    def q_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @q_type.setter
    def q_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ResolverFirewallRuleState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_dns_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        block_response: Optional[pulumi.Input[_builtins.str]] = ...,
        confidence_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_threat_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_redirection_action: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_rule_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_threat_protection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        q_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDnsType")
    def block_override_dns_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_override_dns_type.setter
    def block_override_dns_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDomain")
    def block_override_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_override_domain.setter
    def block_override_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideTtl")
    def block_override_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_override_ttl.setter
    def block_override_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="blockResponse")
    def block_response(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @block_response.setter
    def block_response(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsThreatProtection")
    def dns_threat_protection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_threat_protection.setter
    def dns_threat_protection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_domain_list_id.setter
    def firewall_domain_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainRedirectionAction")
    def firewall_domain_redirection_action(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_domain_redirection_action.setter
    def firewall_domain_redirection_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_rule_group_id.setter
    def firewall_rule_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallThreatProtectionId")
    def firewall_threat_protection_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_threat_protection_id.setter
    def firewall_threat_protection_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="qType")
    def q_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @q_type.setter
    def q_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ResolverFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_dns_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        block_response: Optional[pulumi.Input[_builtins.str]] = ...,
        confidence_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_threat_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_redirection_action: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_rule_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        q_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ResolverFirewallRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_dns_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        block_override_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        block_response: Optional[pulumi.Input[_builtins.str]] = ...,
        confidence_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_threat_protection: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_domain_redirection_action: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_rule_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_threat_protection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        q_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ResolverFirewallRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDnsType")
    def block_override_dns_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDomain")
    def block_override_domain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideTtl")
    def block_override_ttl(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="blockResponse")
    def block_response(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsThreatProtection")
    def dns_threat_protection(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainRedirectionAction")
    def firewall_domain_redirection_action(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firewallThreatProtectionId")
    def firewall_threat_protection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="qType")
    def q_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
