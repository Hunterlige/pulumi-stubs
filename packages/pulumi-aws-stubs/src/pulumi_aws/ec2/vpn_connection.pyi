import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpnConnectionArgs", "VpnConnection"]

@pulumi.input_type
class VpnConnectionArgs:
    def __init__(
        __self__,
        *,
        customer_gateway_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        enable_acceleration: Optional[pulumi.Input[_builtins.bool]] = ...,
        local_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        outside_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        static_routes_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_transit_gateway_attachment_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tunnel1_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel1_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_log_options: Optional[
            pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]
        ] = ...,
        tunnel1_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel2_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_log_options: Optional[
            pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]
        ] = ...,
        tunnel2_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_inside_ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_concentrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @customer_gateway_id.setter
    def customer_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleration")
    def enable_acceleration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_acceleration.setter
    def enable_acceleration(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="localIpv4NetworkCidr")
    def local_ipv4_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ipv4_network_cidr.setter
    def local_ipv4_network_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localIpv6NetworkCidr")
    def local_ipv6_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ipv6_network_cidr.setter
    def local_ipv6_network_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outsideIpAddressType")
    def outside_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outside_ip_address_type.setter
    def outside_ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presharedKeyStorage")
    def preshared_key_storage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preshared_key_storage.setter
    def preshared_key_storage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv4NetworkCidr")
    def remote_ipv4_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_ipv4_network_cidr.setter
    def remote_ipv4_network_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv6NetworkCidr")
    def remote_ipv6_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_ipv6_network_cidr.setter
    def remote_ipv6_network_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @static_routes_only.setter
    def static_routes_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportTransitGatewayAttachmentId")
    def transport_transit_gateway_attachment_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transport_transit_gateway_attachment_id.setter
    def transport_transit_gateway_attachment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutAction")
    def tunnel1_dpd_timeout_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_dpd_timeout_action.setter
    def tunnel1_dpd_timeout_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutSeconds")
    def tunnel1_dpd_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_dpd_timeout_seconds.setter
    def tunnel1_dpd_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1EnableTunnelLifecycleControl")
    def tunnel1_enable_tunnel_lifecycle_control(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tunnel1_enable_tunnel_lifecycle_control.setter
    def tunnel1_enable_tunnel_lifecycle_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1IkeVersions")
    def tunnel1_ike_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_ike_versions.setter
    def tunnel1_ike_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_inside_cidr.setter
    def tunnel1_inside_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideIpv6Cidr")
    def tunnel1_inside_ipv6_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_inside_ipv6_cidr.setter
    def tunnel1_inside_ipv6_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1LogOptions")
    def tunnel1_log_options(
        self,
    ) -> Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]]: ...
    @tunnel1_log_options.setter
    def tunnel1_log_options(
        self, value: Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1DhGroupNumbers")
    def tunnel1_phase1_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel1_phase1_dh_group_numbers.setter
    def tunnel1_phase1_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1EncryptionAlgorithms")
    def tunnel1_phase1_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase1_encryption_algorithms.setter
    def tunnel1_phase1_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1IntegrityAlgorithms")
    def tunnel1_phase1_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase1_integrity_algorithms.setter
    def tunnel1_phase1_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1LifetimeSeconds")
    def tunnel1_phase1_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_phase1_lifetime_seconds.setter
    def tunnel1_phase1_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2DhGroupNumbers")
    def tunnel1_phase2_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel1_phase2_dh_group_numbers.setter
    def tunnel1_phase2_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2EncryptionAlgorithms")
    def tunnel1_phase2_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase2_encryption_algorithms.setter
    def tunnel1_phase2_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2IntegrityAlgorithms")
    def tunnel1_phase2_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase2_integrity_algorithms.setter
    def tunnel1_phase2_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2LifetimeSeconds")
    def tunnel1_phase2_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_phase2_lifetime_seconds.setter
    def tunnel1_phase2_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_preshared_key.setter
    def tunnel1_preshared_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyFuzzPercentage")
    def tunnel1_rekey_fuzz_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_rekey_fuzz_percentage.setter
    def tunnel1_rekey_fuzz_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyMarginTimeSeconds")
    def tunnel1_rekey_margin_time_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_rekey_margin_time_seconds.setter
    def tunnel1_rekey_margin_time_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1ReplayWindowSize")
    def tunnel1_replay_window_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_replay_window_size.setter
    def tunnel1_replay_window_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1StartupAction")
    def tunnel1_startup_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_startup_action.setter
    def tunnel1_startup_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutAction")
    def tunnel2_dpd_timeout_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_dpd_timeout_action.setter
    def tunnel2_dpd_timeout_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutSeconds")
    def tunnel2_dpd_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_dpd_timeout_seconds.setter
    def tunnel2_dpd_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2EnableTunnelLifecycleControl")
    def tunnel2_enable_tunnel_lifecycle_control(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tunnel2_enable_tunnel_lifecycle_control.setter
    def tunnel2_enable_tunnel_lifecycle_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2IkeVersions")
    def tunnel2_ike_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_ike_versions.setter
    def tunnel2_ike_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_inside_cidr.setter
    def tunnel2_inside_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideIpv6Cidr")
    def tunnel2_inside_ipv6_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_inside_ipv6_cidr.setter
    def tunnel2_inside_ipv6_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2LogOptions")
    def tunnel2_log_options(
        self,
    ) -> Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]]: ...
    @tunnel2_log_options.setter
    def tunnel2_log_options(
        self, value: Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1DhGroupNumbers")
    def tunnel2_phase1_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel2_phase1_dh_group_numbers.setter
    def tunnel2_phase1_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1EncryptionAlgorithms")
    def tunnel2_phase1_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase1_encryption_algorithms.setter
    def tunnel2_phase1_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1IntegrityAlgorithms")
    def tunnel2_phase1_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase1_integrity_algorithms.setter
    def tunnel2_phase1_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1LifetimeSeconds")
    def tunnel2_phase1_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_phase1_lifetime_seconds.setter
    def tunnel2_phase1_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2DhGroupNumbers")
    def tunnel2_phase2_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel2_phase2_dh_group_numbers.setter
    def tunnel2_phase2_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2EncryptionAlgorithms")
    def tunnel2_phase2_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase2_encryption_algorithms.setter
    def tunnel2_phase2_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2IntegrityAlgorithms")
    def tunnel2_phase2_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase2_integrity_algorithms.setter
    def tunnel2_phase2_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2LifetimeSeconds")
    def tunnel2_phase2_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_phase2_lifetime_seconds.setter
    def tunnel2_phase2_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_preshared_key.setter
    def tunnel2_preshared_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyFuzzPercentage")
    def tunnel2_rekey_fuzz_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_rekey_fuzz_percentage.setter
    def tunnel2_rekey_fuzz_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyMarginTimeSeconds")
    def tunnel2_rekey_margin_time_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_rekey_margin_time_seconds.setter
    def tunnel2_rekey_margin_time_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2ReplayWindowSize")
    def tunnel2_replay_window_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_replay_window_size.setter
    def tunnel2_replay_window_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2StartupAction")
    def tunnel2_startup_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_startup_action.setter
    def tunnel2_startup_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnelBandwidth")
    def tunnel_bandwidth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel_bandwidth.setter
    def tunnel_bandwidth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnelInsideIpVersion")
    def tunnel_inside_ip_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel_inside_ip_version.setter
    def tunnel_inside_ip_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpnConcentratorId")
    def vpn_concentrator_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_concentrator_id.setter
    def vpn_concentrator_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpnConnectionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_attachment_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_gateway_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_acceleration: Optional[pulumi.Input[_builtins.bool]] = ...,
        local_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        outside_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionRouteArgs]]]
        ] = ...,
        static_routes_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_transit_gateway_attachment_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tunnel1_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_bgp_holdtime: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_cgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel1_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_log_options: Optional[
            pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]
        ] = ...,
        tunnel1_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_vgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_bgp_holdtime: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_cgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel2_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_log_options: Optional[
            pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]
        ] = ...,
        tunnel2_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_vgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_inside_ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vgw_telemetries: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionVgwTelemetryArgs]]]
        ] = ...,
        vpn_concentrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAttachmentArn")
    def core_network_attachment_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_attachment_arn.setter
    def core_network_attachment_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerGatewayConfiguration")
    def customer_gateway_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_gateway_configuration.setter
    def customer_gateway_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_gateway_id.setter
    def customer_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleration")
    def enable_acceleration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_acceleration.setter
    def enable_acceleration(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="localIpv4NetworkCidr")
    def local_ipv4_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ipv4_network_cidr.setter
    def local_ipv4_network_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localIpv6NetworkCidr")
    def local_ipv6_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ipv6_network_cidr.setter
    def local_ipv6_network_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outsideIpAddressType")
    def outside_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outside_ip_address_type.setter
    def outside_ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presharedKeyArn")
    def preshared_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preshared_key_arn.setter
    def preshared_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presharedKeyStorage")
    def preshared_key_storage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preshared_key_storage.setter
    def preshared_key_storage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv4NetworkCidr")
    def remote_ipv4_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_ipv4_network_cidr.setter
    def remote_ipv4_network_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv6NetworkCidr")
    def remote_ipv6_network_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_ipv6_network_cidr.setter
    def remote_ipv6_network_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def routes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpnConnectionRouteArgs]]]]: ...
    @routes.setter
    def routes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VpnConnectionRouteArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @static_routes_only.setter
    def static_routes_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportTransitGatewayAttachmentId")
    def transport_transit_gateway_attachment_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transport_transit_gateway_attachment_id.setter
    def transport_transit_gateway_attachment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Address")
    def tunnel1_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_address.setter
    def tunnel1_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1BgpAsn")
    def tunnel1_bgp_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_bgp_asn.setter
    def tunnel1_bgp_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1BgpHoldtime")
    def tunnel1_bgp_holdtime(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_bgp_holdtime.setter
    def tunnel1_bgp_holdtime(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1CgwInsideAddress")
    def tunnel1_cgw_inside_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_cgw_inside_address.setter
    def tunnel1_cgw_inside_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutAction")
    def tunnel1_dpd_timeout_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_dpd_timeout_action.setter
    def tunnel1_dpd_timeout_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutSeconds")
    def tunnel1_dpd_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_dpd_timeout_seconds.setter
    def tunnel1_dpd_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1EnableTunnelLifecycleControl")
    def tunnel1_enable_tunnel_lifecycle_control(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tunnel1_enable_tunnel_lifecycle_control.setter
    def tunnel1_enable_tunnel_lifecycle_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1IkeVersions")
    def tunnel1_ike_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_ike_versions.setter
    def tunnel1_ike_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_inside_cidr.setter
    def tunnel1_inside_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideIpv6Cidr")
    def tunnel1_inside_ipv6_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_inside_ipv6_cidr.setter
    def tunnel1_inside_ipv6_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1LogOptions")
    def tunnel1_log_options(
        self,
    ) -> Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]]: ...
    @tunnel1_log_options.setter
    def tunnel1_log_options(
        self, value: Optional[pulumi.Input[VpnConnectionTunnel1LogOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1DhGroupNumbers")
    def tunnel1_phase1_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel1_phase1_dh_group_numbers.setter
    def tunnel1_phase1_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1EncryptionAlgorithms")
    def tunnel1_phase1_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase1_encryption_algorithms.setter
    def tunnel1_phase1_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1IntegrityAlgorithms")
    def tunnel1_phase1_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase1_integrity_algorithms.setter
    def tunnel1_phase1_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1LifetimeSeconds")
    def tunnel1_phase1_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_phase1_lifetime_seconds.setter
    def tunnel1_phase1_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2DhGroupNumbers")
    def tunnel1_phase2_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel1_phase2_dh_group_numbers.setter
    def tunnel1_phase2_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2EncryptionAlgorithms")
    def tunnel1_phase2_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase2_encryption_algorithms.setter
    def tunnel1_phase2_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2IntegrityAlgorithms")
    def tunnel1_phase2_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel1_phase2_integrity_algorithms.setter
    def tunnel1_phase2_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2LifetimeSeconds")
    def tunnel1_phase2_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_phase2_lifetime_seconds.setter
    def tunnel1_phase2_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_preshared_key.setter
    def tunnel1_preshared_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyFuzzPercentage")
    def tunnel1_rekey_fuzz_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_rekey_fuzz_percentage.setter
    def tunnel1_rekey_fuzz_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyMarginTimeSeconds")
    def tunnel1_rekey_margin_time_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_rekey_margin_time_seconds.setter
    def tunnel1_rekey_margin_time_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1ReplayWindowSize")
    def tunnel1_replay_window_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel1_replay_window_size.setter
    def tunnel1_replay_window_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1StartupAction")
    def tunnel1_startup_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_startup_action.setter
    def tunnel1_startup_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel1VgwInsideAddress")
    def tunnel1_vgw_inside_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel1_vgw_inside_address.setter
    def tunnel1_vgw_inside_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Address")
    def tunnel2_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_address.setter
    def tunnel2_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2BgpAsn")
    def tunnel2_bgp_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_bgp_asn.setter
    def tunnel2_bgp_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2BgpHoldtime")
    def tunnel2_bgp_holdtime(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_bgp_holdtime.setter
    def tunnel2_bgp_holdtime(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2CgwInsideAddress")
    def tunnel2_cgw_inside_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_cgw_inside_address.setter
    def tunnel2_cgw_inside_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutAction")
    def tunnel2_dpd_timeout_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_dpd_timeout_action.setter
    def tunnel2_dpd_timeout_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutSeconds")
    def tunnel2_dpd_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_dpd_timeout_seconds.setter
    def tunnel2_dpd_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2EnableTunnelLifecycleControl")
    def tunnel2_enable_tunnel_lifecycle_control(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tunnel2_enable_tunnel_lifecycle_control.setter
    def tunnel2_enable_tunnel_lifecycle_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2IkeVersions")
    def tunnel2_ike_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_ike_versions.setter
    def tunnel2_ike_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_inside_cidr.setter
    def tunnel2_inside_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideIpv6Cidr")
    def tunnel2_inside_ipv6_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_inside_ipv6_cidr.setter
    def tunnel2_inside_ipv6_cidr(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2LogOptions")
    def tunnel2_log_options(
        self,
    ) -> Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]]: ...
    @tunnel2_log_options.setter
    def tunnel2_log_options(
        self, value: Optional[pulumi.Input[VpnConnectionTunnel2LogOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1DhGroupNumbers")
    def tunnel2_phase1_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel2_phase1_dh_group_numbers.setter
    def tunnel2_phase1_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1EncryptionAlgorithms")
    def tunnel2_phase1_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase1_encryption_algorithms.setter
    def tunnel2_phase1_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1IntegrityAlgorithms")
    def tunnel2_phase1_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase1_integrity_algorithms.setter
    def tunnel2_phase1_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1LifetimeSeconds")
    def tunnel2_phase1_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_phase1_lifetime_seconds.setter
    def tunnel2_phase1_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2DhGroupNumbers")
    def tunnel2_phase2_dh_group_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @tunnel2_phase2_dh_group_numbers.setter
    def tunnel2_phase2_dh_group_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2EncryptionAlgorithms")
    def tunnel2_phase2_encryption_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase2_encryption_algorithms.setter
    def tunnel2_phase2_encryption_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2IntegrityAlgorithms")
    def tunnel2_phase2_integrity_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tunnel2_phase2_integrity_algorithms.setter
    def tunnel2_phase2_integrity_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2LifetimeSeconds")
    def tunnel2_phase2_lifetime_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_phase2_lifetime_seconds.setter
    def tunnel2_phase2_lifetime_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_preshared_key.setter
    def tunnel2_preshared_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyFuzzPercentage")
    def tunnel2_rekey_fuzz_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_rekey_fuzz_percentage.setter
    def tunnel2_rekey_fuzz_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyMarginTimeSeconds")
    def tunnel2_rekey_margin_time_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_rekey_margin_time_seconds.setter
    def tunnel2_rekey_margin_time_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2ReplayWindowSize")
    def tunnel2_replay_window_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tunnel2_replay_window_size.setter
    def tunnel2_replay_window_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2StartupAction")
    def tunnel2_startup_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_startup_action.setter
    def tunnel2_startup_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnel2VgwInsideAddress")
    def tunnel2_vgw_inside_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel2_vgw_inside_address.setter
    def tunnel2_vgw_inside_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tunnelBandwidth")
    def tunnel_bandwidth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel_bandwidth.setter
    def tunnel_bandwidth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnelInsideIpVersion")
    def tunnel_inside_ip_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel_inside_ip_version.setter
    def tunnel_inside_ip_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vgwTelemetries")
    def vgw_telemetries(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VpnConnectionVgwTelemetryArgs]]]
    ]: ...
    @vgw_telemetries.setter
    def vgw_telemetries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionVgwTelemetryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpnConcentratorId")
    def vpn_concentrator_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_concentrator_id.setter
    def vpn_concentrator_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/vpnConnection:VpnConnection")
class VpnConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_acceleration: Optional[pulumi.Input[_builtins.bool]] = ...,
        local_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        outside_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        static_routes_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_transit_gateway_attachment_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tunnel1_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel1_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_log_options: Optional[
            pulumi.Input[
                Union[
                    VpnConnectionTunnel1LogOptionsArgs,
                    VpnConnectionTunnel1LogOptionsArgsDict,
                ]
            ]
        ] = ...,
        tunnel1_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel2_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_log_options: Optional[
            pulumi.Input[
                Union[
                    VpnConnectionTunnel2LogOptionsArgs,
                    VpnConnectionTunnel2LogOptionsArgsDict,
                ]
            ]
        ] = ...,
        tunnel2_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_inside_ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_concentrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpnConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_attachment_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_gateway_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_acceleration: Optional[pulumi.Input[_builtins.bool]] = ...,
        local_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        outside_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        preshared_key_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv4_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_ipv6_network_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VpnConnectionRouteArgs, VpnConnectionRouteArgsDict]
                    ]
                ]
            ]
        ] = ...,
        static_routes_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_transit_gateway_attachment_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        tunnel1_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_bgp_holdtime: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_cgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel1_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_log_options: Optional[
            pulumi.Input[
                Union[
                    VpnConnectionTunnel1LogOptionsArgs,
                    VpnConnectionTunnel1LogOptionsArgsDict,
                ]
            ]
        ] = ...,
        tunnel1_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel1_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel1_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel1_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel1_vgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_bgp_asn: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_bgp_holdtime: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_cgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_enable_tunnel_lifecycle_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        tunnel2_ike_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_inside_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_inside_ipv6_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_log_options: Optional[
            pulumi.Input[
                Union[
                    VpnConnectionTunnel2LogOptionsArgs,
                    VpnConnectionTunnel2LogOptionsArgsDict,
                ]
            ]
        ] = ...,
        tunnel2_phase1_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase1_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase1_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_phase2_dh_group_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        tunnel2_phase2_encryption_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_integrity_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tunnel2_phase2_lifetime_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_preshared_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_rekey_fuzz_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_rekey_margin_time_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_replay_window_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tunnel2_startup_action: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel2_vgw_inside_address: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_bandwidth: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_inside_ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vgw_telemetries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpnConnectionVgwTelemetryArgs,
                            VpnConnectionVgwTelemetryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        vpn_concentrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpnConnection: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAttachmentArn")
    def core_network_attachment_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerGatewayConfiguration")
    def customer_gateway_configuration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleration")
    def enable_acceleration(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="localIpv4NetworkCidr")
    def local_ipv4_network_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localIpv6NetworkCidr")
    def local_ipv6_network_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outsideIpAddressType")
    def outside_ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presharedKeyArn")
    def preshared_key_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presharedKeyStorage")
    def preshared_key_storage(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv4NetworkCidr")
    def remote_ipv4_network_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteIpv6NetworkCidr")
    def remote_ipv6_network_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Sequence[outputs.VpnConnectionRoute]]: ...
    @_builtins.property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transportTransitGatewayAttachmentId")
    def transport_transit_gateway_attachment_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Address")
    def tunnel1_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1BgpAsn")
    def tunnel1_bgp_asn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1BgpHoldtime")
    def tunnel1_bgp_holdtime(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1CgwInsideAddress")
    def tunnel1_cgw_inside_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutAction")
    def tunnel1_dpd_timeout_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1DpdTimeoutSeconds")
    def tunnel1_dpd_timeout_seconds(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1EnableTunnelLifecycleControl")
    def tunnel1_enable_tunnel_lifecycle_control(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1IkeVersions")
    def tunnel1_ike_versions(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1InsideIpv6Cidr")
    def tunnel1_inside_ipv6_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1LogOptions")
    def tunnel1_log_options(
        self,
    ) -> pulumi.Output[outputs.VpnConnectionTunnel1LogOptions]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1DhGroupNumbers")
    def tunnel1_phase1_dh_group_numbers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.int]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1EncryptionAlgorithms")
    def tunnel1_phase1_encryption_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1IntegrityAlgorithms")
    def tunnel1_phase1_integrity_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase1LifetimeSeconds")
    def tunnel1_phase1_lifetime_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2DhGroupNumbers")
    def tunnel1_phase2_dh_group_numbers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.int]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2EncryptionAlgorithms")
    def tunnel1_phase2_encryption_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2IntegrityAlgorithms")
    def tunnel1_phase2_integrity_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1Phase2LifetimeSeconds")
    def tunnel1_phase2_lifetime_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyFuzzPercentage")
    def tunnel1_rekey_fuzz_percentage(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1RekeyMarginTimeSeconds")
    def tunnel1_rekey_margin_time_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1ReplayWindowSize")
    def tunnel1_replay_window_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1StartupAction")
    def tunnel1_startup_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel1VgwInsideAddress")
    def tunnel1_vgw_inside_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Address")
    def tunnel2_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2BgpAsn")
    def tunnel2_bgp_asn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2BgpHoldtime")
    def tunnel2_bgp_holdtime(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2CgwInsideAddress")
    def tunnel2_cgw_inside_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutAction")
    def tunnel2_dpd_timeout_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2DpdTimeoutSeconds")
    def tunnel2_dpd_timeout_seconds(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2EnableTunnelLifecycleControl")
    def tunnel2_enable_tunnel_lifecycle_control(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2IkeVersions")
    def tunnel2_ike_versions(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2InsideIpv6Cidr")
    def tunnel2_inside_ipv6_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2LogOptions")
    def tunnel2_log_options(
        self,
    ) -> pulumi.Output[outputs.VpnConnectionTunnel2LogOptions]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1DhGroupNumbers")
    def tunnel2_phase1_dh_group_numbers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.int]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1EncryptionAlgorithms")
    def tunnel2_phase1_encryption_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1IntegrityAlgorithms")
    def tunnel2_phase1_integrity_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase1LifetimeSeconds")
    def tunnel2_phase1_lifetime_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2DhGroupNumbers")
    def tunnel2_phase2_dh_group_numbers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.int]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2EncryptionAlgorithms")
    def tunnel2_phase2_encryption_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2IntegrityAlgorithms")
    def tunnel2_phase2_integrity_algorithms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2Phase2LifetimeSeconds")
    def tunnel2_phase2_lifetime_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyFuzzPercentage")
    def tunnel2_rekey_fuzz_percentage(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2RekeyMarginTimeSeconds")
    def tunnel2_rekey_margin_time_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2ReplayWindowSize")
    def tunnel2_replay_window_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2StartupAction")
    def tunnel2_startup_action(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnel2VgwInsideAddress")
    def tunnel2_vgw_inside_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnelBandwidth")
    def tunnel_bandwidth(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnelInsideIpVersion")
    def tunnel_inside_ip_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vgwTelemetries")
    def vgw_telemetries(
        self,
    ) -> pulumi.Output[Sequence[outputs.VpnConnectionVgwTelemetry]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnConcentratorId")
    def vpn_concentrator_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
