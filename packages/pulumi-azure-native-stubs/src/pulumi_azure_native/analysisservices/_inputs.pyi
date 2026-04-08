import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GatewayDetailsArgs",
    "GatewayDetailsArgsDict",
    "IPv4FirewallRuleArgs",
    "IPv4FirewallRuleArgsDict",
    "IPv4FirewallSettingsArgs",
    "IPv4FirewallSettingsArgsDict",
    "ResourceSkuArgs",
    "ResourceSkuArgsDict",
    "ServerAdministratorsArgs",
    "ServerAdministratorsArgsDict",
]

class GatewayDetailsArgsDict(TypedDict):
    gateway_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayDetailsArgs:
    def __init__(
        __self__, *, gateway_resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayResourceId")
    def gateway_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_resource_id.setter
    def gateway_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IPv4FirewallRuleArgsDict(TypedDict):
    firewall_rule_name: NotRequired[pulumi.Input[_builtins.str]]
    range_end: NotRequired[pulumi.Input[_builtins.str]]
    range_start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IPv4FirewallRuleArgs:
    def __init__(
        __self__,
        *,
        firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        range_end: Optional[pulumi.Input[_builtins.str]] = ...,
        range_start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleName")
    def firewall_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_rule_name.setter
    def firewall_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeEnd")
    def range_end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_end.setter
    def range_end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeStart")
    def range_start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_start.setter
    def range_start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IPv4FirewallSettingsArgsDict(TypedDict):
    enable_power_bi_service: NotRequired[pulumi.Input[_builtins.bool]]
    firewall_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IPv4FirewallRuleArgsDict]]]
    ]

@pulumi.input_type
class IPv4FirewallSettingsArgs:
    def __init__(
        __self__,
        *,
        enable_power_bi_service: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[IPv4FirewallRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePowerBIService")
    def enable_power_bi_service(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_power_bi_service.setter
    def enable_power_bi_service(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPv4FirewallRuleArgs]]]]: ...
    @firewall_rules.setter
    def firewall_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[IPv4FirewallRuleArgs]]]],
    ): ...

class ResourceSkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SkuTier]]]

@pulumi.input_type
class ResourceSkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        tier: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]): ...

class ServerAdministratorsArgsDict(TypedDict):
    members: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServerAdministratorsArgs:
    def __init__(
        __self__,
        *,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
