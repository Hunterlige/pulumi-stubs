import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ForwardingRuleArgs", "ForwardingRule"]

@pulumi.input_type
class ForwardingRuleArgs:
    def __init__(
        __self__,
        *,
        all_ports: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_psc_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        backend_service: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        is_mirroring_collector: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        no_automate_dns_zone: Optional[pulumi.Input[_builtins.bool]] = ...,
        port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recreate_closed_psc: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_registrations: Optional[
            pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]
        ] = ...,
        service_label: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allPorts")
    def all_ports(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_ports.setter
    def all_ports(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowGlobalAccess")
    def allow_global_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_global_access.setter
    def allow_global_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowPscGlobalAccess")
    def allow_psc_global_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_psc_global_access.setter
    def allow_psc_global_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backend_service.setter
    def backend_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_collection.setter
    def ip_collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isMirroringCollector")
    def is_mirroring_collector(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_mirroring_collector.setter
    def is_mirroring_collector(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_tier.setter
    def network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noAutomateDnsZone")
    def no_automate_dns_zone(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_automate_dns_zone.setter
    def no_automate_dns_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recreateClosedPsc")
    def recreate_closed_psc(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @recreate_closed_psc.setter
    def recreate_closed_psc(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryRegistrations")
    def service_directory_registrations(
        self,
    ) -> Optional[pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]]: ...
    @service_directory_registrations.setter
    def service_directory_registrations(
        self,
        value: Optional[pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceLabel")
    def service_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_label.setter
    def service_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_ip_ranges.setter
    def source_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ForwardingRuleState:
    def __init__(
        __self__,
        *,
        all_ports: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_psc_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        backend_service: Optional[pulumi.Input[_builtins.str]] = ...,
        base_forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        forwarding_rule_id: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        is_mirroring_collector: Optional[pulumi.Input[_builtins.bool]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        no_automate_dns_zone: Optional[pulumi.Input[_builtins.bool]] = ...,
        port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        recreate_closed_psc: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_registrations: Optional[
            pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]
        ] = ...,
        service_label: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allPorts")
    def all_ports(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_ports.setter
    def all_ports(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowGlobalAccess")
    def allow_global_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_global_access.setter
    def allow_global_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowPscGlobalAccess")
    def allow_psc_global_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_psc_global_access.setter
    def allow_psc_global_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backend_service.setter
    def backend_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baseForwardingRule")
    def base_forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_forwarding_rule.setter
    def base_forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @forwarding_rule_id.setter
    def forwarding_rule_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_collection.setter
    def ip_collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isMirroringCollector")
    def is_mirroring_collector(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_mirroring_collector.setter
    def is_mirroring_collector(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_tier.setter
    def network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noAutomateDnsZone")
    def no_automate_dns_zone(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_automate_dns_zone.setter
    def no_automate_dns_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_status.setter
    def psc_connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="recreateClosedPsc")
    def recreate_closed_psc(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @recreate_closed_psc.setter
    def recreate_closed_psc(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryRegistrations")
    def service_directory_registrations(
        self,
    ) -> Optional[pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]]: ...
    @service_directory_registrations.setter
    def service_directory_registrations(
        self,
        value: Optional[pulumi.Input[ForwardingRuleServiceDirectoryRegistrationsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceLabel")
    def service_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_label.setter
    def service_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_ip_ranges.setter
    def source_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/forwardingRule:ForwardingRule")
class ForwardingRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_ports: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_psc_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        backend_service: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        is_mirroring_collector: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        no_automate_dns_zone: Optional[pulumi.Input[_builtins.bool]] = ...,
        port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recreate_closed_psc: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_registrations: Optional[
            pulumi.Input[
                Union[
                    ForwardingRuleServiceDirectoryRegistrationsArgs,
                    ForwardingRuleServiceDirectoryRegistrationsArgsDict,
                ]
            ]
        ] = ...,
        service_label: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ForwardingRuleArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_ports: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_psc_global_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        backend_service: Optional[pulumi.Input[_builtins.str]] = ...,
        base_forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        forwarding_rule_id: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_version: Optional[pulumi.Input[_builtins.str]] = ...,
        is_mirroring_collector: Optional[pulumi.Input[_builtins.bool]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        no_automate_dns_zone: Optional[pulumi.Input[_builtins.bool]] = ...,
        port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        recreate_closed_psc: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_registrations: Optional[
            pulumi.Input[
                Union[
                    ForwardingRuleServiceDirectoryRegistrationsArgs,
                    ForwardingRuleServiceDirectoryRegistrationsArgsDict,
                ]
            ]
        ] = ...,
        service_label: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ForwardingRule: ...
    @_builtins.property
    @pulumi.getter(name="allPorts")
    def all_ports(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowGlobalAccess")
    def allow_global_access(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowPscGlobalAccess")
    def allow_psc_global_access(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="baseForwardingRule")
    def base_forwarding_rule(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isMirroringCollector")
    def is_mirroring_collector(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noAutomateDnsZone")
    def no_automate_dns_zone(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="recreateClosedPsc")
    def recreate_closed_psc(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryRegistrations")
    def service_directory_registrations(
        self,
    ) -> pulumi.Output[outputs.ForwardingRuleServiceDirectoryRegistrations]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLabel")
    def service_label(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[_builtins.str]]: ...
