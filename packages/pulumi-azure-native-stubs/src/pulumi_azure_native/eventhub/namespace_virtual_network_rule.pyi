import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NamespaceVirtualNetworkRuleArgs", "NamespaceVirtualNetworkRule"]

@pulumi.input_type
class NamespaceVirtualNetworkRuleArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        virtual_network_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRuleName")
    def virtual_network_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_rule_name.setter
    def virtual_network_rule_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:eventhub:NamespaceVirtualNetworkRule")
class NamespaceVirtualNetworkRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NamespaceVirtualNetworkRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NamespaceVirtualNetworkRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
