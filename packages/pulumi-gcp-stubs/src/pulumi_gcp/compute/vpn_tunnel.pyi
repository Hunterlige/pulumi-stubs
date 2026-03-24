import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VPNTunnelArgs", "VPNTunnel"]

@pulumi.input_type
class VPNTunnelArgs:
    def __init__(
        __self__,
        *,
        cipher_suite: Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ike_version: Optional[pulumi.Input[_builtins.int]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        local_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[VPNTunnelParamsArgs]] = ...,
        peer_external_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_external_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
        peer_gcp_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        router: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuite")
    def cipher_suite(self) -> Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]]: ...
    @cipher_suite.setter
    def cipher_suite(self, value: Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ike_version.setter
    def ike_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localTrafficSelectors")
    def local_traffic_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @local_traffic_selectors.setter
    def local_traffic_selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[VPNTunnelParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[VPNTunnelParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGateway")
    def peer_external_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_external_gateway.setter
    def peer_external_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGatewayInterface")
    def peer_external_gateway_interface(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @peer_external_gateway_interface.setter
    def peer_external_gateway_interface(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerGcpGateway")
    def peer_gcp_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_gcp_gateway.setter
    def peer_gcp_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_ip.setter
    def peer_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteTrafficSelectors")
    def remote_traffic_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @remote_traffic_selectors.setter
    def remote_traffic_selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def router(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @router.setter
    def router(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWo")
    def shared_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret_wo.setter
    def shared_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWoVersion")
    def shared_secret_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret_wo_version.setter
    def shared_secret_wo_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVpnGateway")
    def target_vpn_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vpn_gateway.setter
    def target_vpn_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_gateway.setter
    def vpn_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayInterface")
    def vpn_gateway_interface(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vpn_gateway_interface.setter
    def vpn_gateway_interface(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _VPNTunnelState:
    def __init__(
        __self__,
        *,
        cipher_suite: Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        detailed_status: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ike_version: Optional[pulumi.Input[_builtins.int]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        local_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[VPNTunnelParamsArgs]] = ...,
        peer_external_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_external_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
        peer_gcp_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        router: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_hash: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuite")
    def cipher_suite(self) -> Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]]: ...
    @cipher_suite.setter
    def cipher_suite(self, value: Optional[pulumi.Input[VPNTunnelCipherSuiteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detailed_status.setter
    def detailed_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ike_version.setter
    def ike_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localTrafficSelectors")
    def local_traffic_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @local_traffic_selectors.setter
    def local_traffic_selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[VPNTunnelParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[VPNTunnelParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGateway")
    def peer_external_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_external_gateway.setter
    def peer_external_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGatewayInterface")
    def peer_external_gateway_interface(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @peer_external_gateway_interface.setter
    def peer_external_gateway_interface(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerGcpGateway")
    def peer_gcp_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_gcp_gateway.setter
    def peer_gcp_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_ip.setter
    def peer_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteTrafficSelectors")
    def remote_traffic_selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @remote_traffic_selectors.setter
    def remote_traffic_selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def router(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @router.setter
    def router(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretHash")
    def shared_secret_hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret_hash.setter
    def shared_secret_hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWo")
    def shared_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret_wo.setter
    def shared_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWoVersion")
    def shared_secret_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_secret_wo_version.setter
    def shared_secret_wo_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVpnGateway")
    def target_vpn_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vpn_gateway.setter
    def target_vpn_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tunnel_id.setter
    def tunnel_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_gateway.setter
    def vpn_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayInterface")
    def vpn_gateway_interface(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vpn_gateway_interface.setter
    def vpn_gateway_interface(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("gcp:compute/vPNTunnel:VPNTunnel")
class VPNTunnel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cipher_suite: Optional[
            pulumi.Input[Union[VPNTunnelCipherSuiteArgs, VPNTunnelCipherSuiteArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ike_version: Optional[pulumi.Input[_builtins.int]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        local_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[VPNTunnelParamsArgs, VPNTunnelParamsArgsDict]]
        ] = ...,
        peer_external_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_external_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
        peer_gcp_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        router: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[VPNTunnelArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cipher_suite: Optional[
            pulumi.Input[Union[VPNTunnelCipherSuiteArgs, VPNTunnelCipherSuiteArgsDict]]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        detailed_status: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ike_version: Optional[pulumi.Input[_builtins.int]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        local_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[VPNTunnelParamsArgs, VPNTunnelParamsArgsDict]]
        ] = ...,
        peer_external_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_external_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
        peer_gcp_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_traffic_selectors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        router: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_hash: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_secret_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        tunnel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_gateway_interface: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> VPNTunnel: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuite")
    def cipher_suite(self) -> pulumi.Output[Optional[outputs.VPNTunnelCipherSuite]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="localTrafficSelectors")
    def local_traffic_selectors(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.VPNTunnelParams]]: ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGateway")
    def peer_external_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="peerExternalGatewayInterface")
    def peer_external_gateway_interface(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="peerGcpGateway")
    def peer_gcp_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteTrafficSelectors")
    def remote_traffic_selectors(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def router(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretHash")
    def shared_secret_hash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWo")
    def shared_secret_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharedSecretWoVersion")
    def shared_secret_wo_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetVpnGateway")
    def target_vpn_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnGatewayInterface")
    def vpn_gateway_interface(self) -> pulumi.Output[Optional[_builtins.int]]: ...
