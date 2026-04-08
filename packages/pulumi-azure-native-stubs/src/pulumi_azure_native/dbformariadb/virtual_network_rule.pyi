import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualNetworkRuleArgs", "VirtualNetworkRule"]

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        virtual_network_subnet_id: pulumi.Input[_builtins.str],
        ignore_missing_vnet_service_endpoint: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        virtual_network_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRuleName")
    def virtual_network_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_rule_name.setter
    def virtual_network_rule_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:dbformariadb:VirtualNetworkRule")
class VirtualNetworkRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ignore_missing_vnet_service_endpoint: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualNetworkRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualNetworkRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> pulumi.Output[_builtins.str]: ...
