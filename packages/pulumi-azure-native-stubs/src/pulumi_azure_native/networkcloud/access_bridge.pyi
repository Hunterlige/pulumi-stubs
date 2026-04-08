import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessBridgeArgs", "AccessBridge"]

@pulumi.input_type
class AccessBridgeArgs:
    def __init__(
        __self__,
        *,
        extended_location: pulumi.Input[ExtendedLocationArgs],
        network_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        access_bridge_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv4_connected_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_connected_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        security_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessBridgeSecurityRuleArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]: ...
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[_builtins.str]: ...
    @network_id.setter
    def network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessBridgeName")
    def access_bridge_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_bridge_name.setter
    def access_bridge_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4ConnectedPrefix")
    def ipv4_connected_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_connected_prefix.setter
    def ipv4_connected_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6ConnectedPrefix")
    def ipv6_connected_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_connected_prefix.setter
    def ipv6_connected_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AccessBridgeSecurityRuleArgs]]]
    ]: ...
    @security_rules.setter
    def security_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessBridgeSecurityRuleArgs]]]
        ],
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

@pulumi.type_token("azure-native:networkcloud:AccessBridge")
class AccessBridge(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_bridge_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        ipv4_connected_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_connected_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AccessBridgeSecurityRuleArgs,
                            AccessBridgeSecurityRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessBridgeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AccessBridge: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> pulumi.Output[Sequence[outputs.AccessBridgeEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4ConnectedPrefix")
    def ipv4_connected_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6ConnectedPrefix")
    def ipv6_connected_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityRules")
    def security_rules(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.AccessBridgeSecurityRuleResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
