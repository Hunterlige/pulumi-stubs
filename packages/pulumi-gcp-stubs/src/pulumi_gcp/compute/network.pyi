import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkArgs", "Network"]

@pulumi.input_type
class NetworkArgs:
    def __init__(
        __self__,
        *,
        auto_create_subnetworks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_best_path_selection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_default_routes_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_ula_internal_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        internal_ipv6_range: Optional[pulumi.Input[_builtins.str]] = ...,
        mtu: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_enforcement_order: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[NetworkParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoCreateSubnetworks")
    def auto_create_subnetworks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_create_subnetworks.setter
    def auto_create_subnetworks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpAlwaysCompareMed")
    def bgp_always_compare_med(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bgp_always_compare_med.setter
    def bgp_always_compare_med(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpBestPathSelectionMode")
    def bgp_best_path_selection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_best_path_selection_mode.setter
    def bgp_best_path_selection_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpInterRegionCost")
    def bgp_inter_region_cost(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_inter_region_cost.setter
    def bgp_inter_region_cost(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteBgpAlwaysCompareMed")
    def delete_bgp_always_compare_med(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_bgp_always_compare_med.setter
    def delete_bgp_always_compare_med(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteDefaultRoutesOnCreate")
    def delete_default_routes_on_create(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_default_routes_on_create.setter
    def delete_default_routes_on_create(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableUlaInternalIpv6")
    def enable_ula_internal_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ula_internal_ipv6.setter
    def enable_ula_internal_ipv6(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="internalIpv6Range")
    def internal_ipv6_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_ipv6_range.setter
    def internal_ipv6_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicyEnforcementOrder")
    def network_firewall_policy_enforcement_order(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_firewall_policy_enforcement_order.setter
    def network_firewall_policy_enforcement_order(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[NetworkParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[NetworkParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkState:
    def __init__(
        __self__,
        *,
        auto_create_subnetworks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_best_path_selection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_default_routes_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_ula_internal_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        gateway_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ipv6_range: Optional[pulumi.Input[_builtins.str]] = ...,
        mtu: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_enforcement_order: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        numeric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[NetworkParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoCreateSubnetworks")
    def auto_create_subnetworks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_create_subnetworks.setter
    def auto_create_subnetworks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpAlwaysCompareMed")
    def bgp_always_compare_med(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bgp_always_compare_med.setter
    def bgp_always_compare_med(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpBestPathSelectionMode")
    def bgp_best_path_selection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_best_path_selection_mode.setter
    def bgp_best_path_selection_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bgpInterRegionCost")
    def bgp_inter_region_cost(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_inter_region_cost.setter
    def bgp_inter_region_cost(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteBgpAlwaysCompareMed")
    def delete_bgp_always_compare_med(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_bgp_always_compare_med.setter
    def delete_bgp_always_compare_med(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteDefaultRoutesOnCreate")
    def delete_default_routes_on_create(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_default_routes_on_create.setter
    def delete_default_routes_on_create(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableUlaInternalIpv6")
    def enable_ula_internal_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ula_internal_ipv6.setter
    def enable_ula_internal_ipv6(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIpv4")
    def gateway_ipv4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_ipv4.setter
    def gateway_ipv4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIpv6Range")
    def internal_ipv6_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internal_ipv6_range.setter
    def internal_ipv6_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicyEnforcementOrder")
    def network_firewall_policy_enforcement_order(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_firewall_policy_enforcement_order.setter
    def network_firewall_policy_enforcement_order(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numericId")
    @_utilities.deprecated(...)
    def numeric_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @numeric_id.setter
    def numeric_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[NetworkParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[NetworkParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/network:Network")
class Network(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_create_subnetworks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_best_path_selection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_default_routes_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_ula_internal_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        internal_ipv6_range: Optional[pulumi.Input[_builtins.str]] = ...,
        mtu: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_enforcement_order: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[NetworkParamsArgs, NetworkParamsArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[NetworkArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_create_subnetworks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        bgp_best_path_selection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_bgp_always_compare_med: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_default_routes_on_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_ula_internal_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        gateway_ipv4: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ipv6_range: Optional[pulumi.Input[_builtins.str]] = ...,
        mtu: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_enforcement_order: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        numeric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[NetworkParamsArgs, NetworkParamsArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Network: ...
    @_builtins.property
    @pulumi.getter(name="autoCreateSubnetworks")
    def auto_create_subnetworks(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="bgpAlwaysCompareMed")
    def bgp_always_compare_med(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="bgpBestPathSelectionMode")
    def bgp_best_path_selection_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpInterRegionCost")
    def bgp_inter_region_cost(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteBgpAlwaysCompareMed")
    def delete_bgp_always_compare_med(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteDefaultRoutesOnCreate")
    def delete_default_routes_on_create(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableUlaInternalIpv6")
    def enable_ula_internal_ipv6(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIpv4")
    def gateway_ipv4(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="internalIpv6Range")
    def internal_ipv6_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicyEnforcementOrder")
    def network_firewall_policy_enforcement_order(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="numericId")
    @_utilities.deprecated(...)
    def numeric_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.NetworkParams]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
