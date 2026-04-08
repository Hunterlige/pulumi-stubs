import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FirewallRuleArgs", "FirewallRule"]

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(
        __self__,
        *,
        mongo_cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[FirewallRulePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mongoClusterName")
    def mongo_cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @mongo_cluster_name.setter
    def mongo_cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleName")
    def firewall_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_rule_name.setter
    def firewall_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[FirewallRulePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[FirewallRulePropertiesArgs]]): ...

@pulumi.type_token("azure-native:mongocluster:FirewallRule")
class FirewallRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mongo_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[FirewallRulePropertiesArgs, FirewallRulePropertiesArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FirewallRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FirewallRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.FirewallRulePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
