import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityRuleArgs", "SecurityRule"]

@pulumi.input_type
class SecurityRuleArgs:
    def __init__(
        __self__,
        *,
        access: pulumi.Input[Union[_builtins.str, SecurityRuleAccess]],
        direction: pulumi.Input[Union[_builtins.str, SecurityRuleDirection]],
        network_security_group_name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[Union[_builtins.str, SecurityRuleProtocol]],
        resource_group_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        destination_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        security_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> pulumi.Input[Union[_builtins.str, SecurityRuleAccess]]: ...
    @access.setter
    def access(self, value: pulumi.Input[Union[_builtins.str, SecurityRuleAccess]]): ...
    @_builtins.property
    @pulumi.getter
    def direction(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SecurityRuleDirection]]: ...
    @direction.setter
    def direction(
        self, value: pulumi.Input[Union[_builtins.str, SecurityRuleDirection]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupName")
    def network_security_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_security_group_name.setter
    def network_security_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, SecurityRuleProtocol]]: ...
    @protocol.setter
    def protocol(
        self, value: pulumi.Input[Union[_builtins.str, SecurityRuleProtocol]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefixes")
    def destination_address_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_address_prefixes.setter
    def destination_address_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_port_ranges.setter
    def destination_port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityRuleName")
    def security_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_rule_name.setter
    def security_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefixes")
    def source_address_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_address_prefixes.setter
    def source_address_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_port_ranges.setter
    def source_port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:azurestackhci:SecurityRule")
class SecurityRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access: Optional[pulumi.Input[Union[_builtins.str, SecurityRuleAccess]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        destination_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        direction: Optional[
            pulumi.Input[Union[_builtins.str, SecurityRuleDirection]]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        network_security_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[
            pulumi.Input[Union[_builtins.str, SecurityRuleProtocol]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SecurityRule: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefixes")
    def destination_address_prefixes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefixes")
    def source_address_prefixes(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
