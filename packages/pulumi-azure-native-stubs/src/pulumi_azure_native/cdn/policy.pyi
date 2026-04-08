import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyArgs", "Policy"]

@pulumi.input_type
class PolicyArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        custom_rules: Optional[pulumi.Input[CustomRuleListArgs]] = ...,
        extended_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_rules: Optional[pulumi.Input[ManagedRuleSetListArgs]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_settings: Optional[pulumi.Input[PolicySettingsArgs]] = ...,
        rate_limit_rules: Optional[pulumi.Input[RateLimitRuleListArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[CustomRuleListArgs]]: ...
    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[CustomRuleListArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @extended_properties.setter
    def extended_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> Optional[pulumi.Input[ManagedRuleSetListArgs]]: ...
    @managed_rules.setter
    def managed_rules(self, value: Optional[pulumi.Input[ManagedRuleSetListArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[pulumi.Input[PolicySettingsArgs]]: ...
    @policy_settings.setter
    def policy_settings(self, value: Optional[pulumi.Input[PolicySettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimitRules")
    def rate_limit_rules(self) -> Optional[pulumi.Input[RateLimitRuleListArgs]]: ...
    @rate_limit_rules.setter
    def rate_limit_rules(
        self, value: Optional[pulumi.Input[RateLimitRuleListArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:cdn:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_rules: Optional[
            pulumi.Input[Union[CustomRuleListArgs, CustomRuleListArgsDict]]
        ] = ...,
        extended_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_rules: Optional[
            pulumi.Input[Union[ManagedRuleSetListArgs, ManagedRuleSetListArgsDict]]
        ] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_settings: Optional[
            pulumi.Input[Union[PolicySettingsArgs, PolicySettingsArgsDict]]
        ] = ...,
        rate_limit_rules: Optional[
            pulumi.Input[Union[RateLimitRuleListArgs, RateLimitRuleListArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Policy: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(
        self,
    ) -> pulumi.Output[Optional[outputs.CustomRuleListResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointLinks")
    def endpoint_links(
        self,
    ) -> pulumi.Output[Sequence[outputs.CdnEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedRuleSetListResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.PolicySettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitRules")
    def rate_limit_rules(
        self,
    ) -> pulumi.Output[Optional[outputs.RateLimitRuleListResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
