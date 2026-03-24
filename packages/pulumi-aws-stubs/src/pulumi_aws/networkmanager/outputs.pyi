import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectAttachmentOptions",
    "ConnectPeerBgpOptions",
    "ConnectPeerConfiguration",
    "ConnectPeerConfigurationBgpConfiguration",
    "CoreNetworkEdge",
    "CoreNetworkSegment",
    "DeviceAwsLocation",
    "DeviceLocation",
    "DxGatewayAttachmentTimeouts",
    "LinkBandwidth",
    "SiteLocation",
    "VpcAttachmentOptions",
    "GetCoreNetworkPolicyDocumentAttachmentPolicyResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCoreNetworkPolicyDocumentRoutingPolicyResult",
    ...,
    ...,
    ...,
    ...,
    "GetCoreNetworkPolicyDocumentSegmentResult",
    "GetCoreNetworkPolicyDocumentSegmentActionResult",
    ...,
    "GetCoreNetworkPolicyDocumentSegmentActionViaResult",
    ...,
    ...,
    "GetDeviceAwsLocationResult",
    "GetDeviceLocationResult",
    "GetLinkBandwidthResult",
    "GetSiteLocationResult",
]

@pulumi.output_type
class ConnectAttachmentOptions(dict):
    def __init__(__self__, *, protocol: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectPeerBgpOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, peer_asn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectPeerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bgp_configurations: Optional[
            Sequence[outputs.ConnectPeerConfigurationBgpConfiguration]
        ] = ...,
        core_network_address: Optional[_builtins.str] = ...,
        inside_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
        peer_address: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bgpConfigurations")
    def bgp_configurations(
        self,
    ) -> Optional[Sequence[outputs.ConnectPeerConfigurationBgpConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectPeerConfigurationBgpConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        core_network_address: Optional[_builtins.str] = ...,
        core_network_asn: Optional[_builtins.int] = ...,
        peer_address: Optional[_builtins.str] = ...,
        peer_asn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAsn")
    def core_network_asn(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CoreNetworkEdge(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asn: Optional[_builtins.int] = ...,
        edge_location: Optional[_builtins.str] = ...,
        inside_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CoreNetworkSegment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        edge_locations: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        shared_segments: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedSegments")
    def shared_segments(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeviceAwsLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_arn: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeviceLocation(dict):
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        latitude: Optional[_builtins.str] = ...,
        longitude: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DxGatewayAttachmentTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinkBandwidth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        download_speed: Optional[_builtins.int] = ...,
        upload_speed: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="downloadSpeed")
    def download_speed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SiteLocation(dict):
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        latitude: Optional[_builtins.str] = ...,
        longitude: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VpcAttachmentOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        appliance_mode_support: Optional[_builtins.bool] = ...,
        dns_support: Optional[_builtins.bool] = ...,
        ipv6_support: Optional[_builtins.bool] = ...,
        security_group_referencing_support: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyResult(dict):
    def __init__(
        __self__,
        *,
        action: outputs.GetCoreNetworkPolicyDocumentAttachmentPolicyActionResult,
        conditions: Sequence[
            outputs.GetCoreNetworkPolicyDocumentAttachmentPolicyConditionResult
        ],
        rule_number: _builtins.int,
        condition_logic: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> outputs.GetCoreNetworkPolicyDocumentAttachmentPolicyActionResult: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Sequence[
        outputs.GetCoreNetworkPolicyDocumentAttachmentPolicyConditionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="conditionLogic")
    def condition_logic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyActionResult(dict):
    def __init__(
        __self__,
        *,
        add_to_network_function_group: Optional[_builtins.str] = ...,
        association_method: Optional[_builtins.str] = ...,
        require_acceptance: Optional[_builtins.bool] = ...,
        segment: Optional[_builtins.str] = ...,
        tag_value_of_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addToNetworkFunctionGroup")
    def add_to_network_function_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationMethod")
    def association_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireAcceptance")
    def require_acceptance(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValueOfKey")
    def tag_value_of_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyConditionResult(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        key: Optional[_builtins.str] = ...,
        operator: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleResult(dict):
    def __init__(
        __self__,
        *,
        action: outputs.GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionResult,
        conditions: Sequence[
            outputs.GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionResult
        ],
        rule_number: _builtins.int,
        description: Optional[_builtins.str] = ...,
        edge_locations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> (
        outputs.GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionResult
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Sequence[
        outputs.GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionResult(dict):
    def __init__(
        __self__, *, associate_routing_policies: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associateRoutingPolicies")
    def associate_routing_policies(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionResult(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        asn_ranges: Sequence[_builtins.str],
        edge_locations: Sequence[
            outputs.GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationResult
        ],
        dns_support: Optional[_builtins.bool] = ...,
        inside_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
        security_group_referencing_support: Optional[_builtins.bool] = ...,
        vpn_ecmp_support: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asnRanges")
    def asn_ranges(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(
        self,
    ) -> Sequence[
        outputs.GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationResult(dict):
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        asn: Optional[_builtins.str] = ...,
        inside_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentNetworkFunctionGroupResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        require_attachment_acceptance: _builtins.bool,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requireAttachmentAcceptance")
    def require_attachment_acceptance(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentRoutingPolicyResult(dict):
    def __init__(
        __self__,
        *,
        routing_policy_direction: _builtins.str,
        routing_policy_name: _builtins.str,
        routing_policy_number: _builtins.int,
        routing_policy_rules: Sequence[
            outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleResult
        ],
        routing_policy_description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyDirection")
    def routing_policy_direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyName")
    def routing_policy_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNumber")
    def routing_policy_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyRules")
    def routing_policy_rules(
        self,
    ) -> Sequence[
        outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyDescription")
    def routing_policy_description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleResult(dict):
    def __init__(
        __self__,
        *,
        rule_definition: outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionResult,
        rule_number: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(
        self,
    ) -> outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionResult: ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionResult(
    dict
):
    def __init__(
        __self__,
        *,
        action: outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionResult,
        condition_logic: Optional[_builtins.str] = ...,
        match_conditions: Optional[
            Sequence[
                outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionResult
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionResult: ...
    @_builtins.property
    @pulumi.getter(name="conditionLogic")
    def condition_logic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(
        self,
    ) -> Optional[
        Sequence[
            outputs.GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionResult
        ]
    ]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionResult(
    dict
):
    def __init__(
        __self__, *, type: _builtins.str, value: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionResult(
    dict
):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        allow_filters: Optional[Sequence[_builtins.str]] = ...,
        deny_filters: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
        edge_locations: Optional[Sequence[_builtins.str]] = ...,
        isolate_attachments: Optional[_builtins.bool] = ...,
        require_attachment_acceptance: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowFilters")
    def allow_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="denyFilters")
    def deny_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isolateAttachments")
    def isolate_attachments(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requireAttachmentAcceptance")
    def require_attachment_acceptance(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentActionResult(dict):
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        segment: _builtins.str,
        description: Optional[_builtins.str] = ...,
        destination_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
        destinations: Optional[Sequence[_builtins.str]] = ...,
        edge_location_association: Optional[
            outputs.GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationResult
        ] = ...,
        mode: Optional[_builtins.str] = ...,
        routing_policy_names: Optional[Sequence[_builtins.str]] = ...,
        share_with_excepts: Optional[Sequence[_builtins.str]] = ...,
        share_withs: Optional[Sequence[_builtins.str]] = ...,
        via: Optional[outputs.GetCoreNetworkPolicyDocumentSegmentActionViaResult] = ...,
        when_sent_to: Optional[
            outputs.GetCoreNetworkPolicyDocumentSegmentActionWhenSentToResult
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlocks")
    def destination_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocationAssociation")
    def edge_location_association(
        self,
    ) -> Optional[
        outputs.GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNames")
    def routing_policy_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shareWithExcepts")
    def share_with_excepts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shareWiths")
    def share_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def via(
        self,
    ) -> Optional[outputs.GetCoreNetworkPolicyDocumentSegmentActionViaResult]: ...
    @_builtins.property
    @pulumi.getter(name="whenSentTo")
    def when_sent_to(
        self,
    ) -> Optional[
        outputs.GetCoreNetworkPolicyDocumentSegmentActionWhenSentToResult
    ]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationResult(dict):
    def __init__(
        __self__,
        *,
        edge_location: _builtins.str,
        peer_edge_location: _builtins.str,
        routing_policy_names: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerEdgeLocation")
    def peer_edge_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNames")
    def routing_policy_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentActionViaResult(dict):
    def __init__(
        __self__,
        *,
        network_function_groups: Optional[Sequence[_builtins.str]] = ...,
        with_edge_overrides: Optional[
            Sequence[
                outputs.GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideResult
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionGroups")
    def network_function_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="withEdgeOverrides")
    def with_edge_overrides(
        self,
    ) -> Optional[
        Sequence[
            outputs.GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideResult
        ]
    ]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideResult(dict):
    def __init__(
        __self__,
        *,
        edge_sets: Optional[Sequence[Sequence[_builtins.str]]] = ...,
        use_edge: Optional[_builtins.str] = ...,
        use_edge_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeSets")
    def edge_sets(self) -> Optional[Sequence[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="useEdge")
    @_utilities.deprecated(...)
    def use_edge(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useEdgeLocation")
    def use_edge_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCoreNetworkPolicyDocumentSegmentActionWhenSentToResult(dict):
    def __init__(
        __self__, *, segments: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetDeviceAwsLocationResult(dict):
    def __init__(
        __self__, *, subnet_arn: _builtins.str, zone: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetDeviceLocationResult(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        latitude: _builtins.str,
        longitude: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> _builtins.str: ...

@pulumi.output_type
class GetLinkBandwidthResult(dict):
    def __init__(
        __self__, *, download_speed: _builtins.int, upload_speed: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="downloadSpeed")
    def download_speed(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> _builtins.int: ...

@pulumi.output_type
class GetSiteLocationResult(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        latitude: _builtins.str,
        longitude: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> _builtins.str: ...
