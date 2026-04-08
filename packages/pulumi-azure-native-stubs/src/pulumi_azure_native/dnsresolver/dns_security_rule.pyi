import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DnsSecurityRuleArgs", "DnsSecurityRule"]

@pulumi.input_type
class DnsSecurityRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[DnsSecurityRuleActionArgs],
        dns_resolver_domain_lists: pulumi.Input[
            Sequence[pulumi.Input[SubResourceArgs]]
        ],
        dns_resolver_policy_name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        resource_group_name: pulumi.Input[_builtins.str],
        dns_security_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_security_rule_state: Optional[
            pulumi.Input[Union[_builtins.str, DnsSecurityRuleState]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[DnsSecurityRuleActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[DnsSecurityRuleActionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="dnsResolverDomainLists")
    def dns_resolver_domain_lists(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]: ...
    @dns_resolver_domain_lists.setter
    def dns_resolver_domain_lists(
        self, value: pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsResolverPolicyName")
    def dns_resolver_policy_name(self) -> pulumi.Input[_builtins.str]: ...
    @dns_resolver_policy_name.setter
    def dns_resolver_policy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSecurityRuleName")
    def dns_security_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_security_rule_name.setter
    def dns_security_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSecurityRuleState")
    def dns_security_rule_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DnsSecurityRuleState]]]: ...
    @dns_security_rule_state.setter
    def dns_security_rule_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DnsSecurityRuleState]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:dnsresolver:DnsSecurityRule")
class DnsSecurityRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[
            pulumi.Input[
                Union[DnsSecurityRuleActionArgs, DnsSecurityRuleActionArgsDict]
            ]
        ] = ...,
        dns_resolver_domain_lists: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]
            ]
        ] = ...,
        dns_resolver_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_security_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_security_rule_state: Optional[
            pulumi.Input[Union[_builtins.str, DnsSecurityRuleState]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DnsSecurityRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DnsSecurityRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[outputs.DnsSecurityRuleActionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsResolverDomainLists")
    def dns_resolver_domain_lists(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSecurityRuleState")
    def dns_security_rule_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
