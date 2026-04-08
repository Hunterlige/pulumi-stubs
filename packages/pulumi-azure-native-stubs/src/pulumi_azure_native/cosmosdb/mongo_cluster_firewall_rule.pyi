import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MongoClusterFirewallRuleArgs", "MongoClusterFirewallRule"]

@pulumi.input_type
class MongoClusterFirewallRuleArgs:
    def __init__(
        __self__,
        *,
        end_ip_address: pulumi.Input[_builtins.str],
        mongo_cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        start_ip_address: pulumi.Input[_builtins.str],
        firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleName")
    def firewall_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_rule_name.setter
    def firewall_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cosmosdb:MongoClusterFirewallRule")
class MongoClusterFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        end_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mongo_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MongoClusterFirewallRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MongoClusterFirewallRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
