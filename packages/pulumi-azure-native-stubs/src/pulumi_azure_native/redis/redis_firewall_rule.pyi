import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RedisFirewallRuleArgs", "RedisFirewallRule"]

@pulumi.input_type
class RedisFirewallRuleArgs:
    def __init__(
        __self__,
        *,
        cache_name: pulumi.Input[_builtins.str],
        end_ip: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        start_ip: pulumi.Input[_builtins.str],
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheName")
    def cache_name(self) -> pulumi.Input[_builtins.str]: ...
    @cache_name.setter
    def cache_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> pulumi.Input[_builtins.str]: ...
    @end_ip.setter
    def end_ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> pulumi.Input[_builtins.str]: ...
    @start_ip.setter
    def start_ip(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:redis:RedisFirewallRule")
class RedisFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RedisFirewallRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RedisFirewallRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
