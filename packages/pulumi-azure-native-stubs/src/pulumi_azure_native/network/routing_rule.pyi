import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoutingRuleArgs", "RoutingRule"]

@pulumi.input_type
class RoutingRuleArgs:
    def __init__(
        __self__,
        *,
        configuration_name: pulumi.Input[_builtins.str],
        destination: pulumi.Input[RoutingRuleRouteDestinationArgs],
        network_manager_name: pulumi.Input[_builtins.str],
        next_hop: pulumi.Input[RoutingRuleNextHopArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        rule_collection_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[RoutingRuleRouteDestinationArgs]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[RoutingRuleRouteDestinationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nextHop")
    def next_hop(self) -> pulumi.Input[RoutingRuleNextHopArgs]: ...
    @next_hop.setter
    def next_hop(self, value: pulumi.Input[RoutingRuleNextHopArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_collection_name.setter
    def rule_collection_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:network:RoutingRule")
class RoutingRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[
                Union[
                    RoutingRuleRouteDestinationArgs, RoutingRuleRouteDestinationArgsDict
                ]
            ]
        ] = ...,
        network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop: Optional[
            pulumi.Input[Union[RoutingRuleNextHopArgs, RoutingRuleNextHopArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RoutingRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RoutingRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Output[outputs.RoutingRuleRouteDestinationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHop")
    def next_hop(self) -> pulumi.Output[outputs.RoutingRuleNextHopResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
