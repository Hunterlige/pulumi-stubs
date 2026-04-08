import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectAttachmentOptionsArgs",
    "ConnectAttachmentOptionsArgsDict",
    "ConnectPeerBgpOptionsArgs",
    "ConnectPeerBgpOptionsArgsDict",
    "ConnectPeerConfigurationArgs",
    "ConnectPeerConfigurationArgsDict",
    "ConnectPeerConfigurationBgpConfigurationArgs",
    "ConnectPeerConfigurationBgpConfigurationArgsDict",
    "CoreNetworkEdgeArgs",
    "CoreNetworkEdgeArgsDict",
    "CoreNetworkSegmentArgs",
    "CoreNetworkSegmentArgsDict",
    "DeviceAwsLocationArgs",
    "DeviceAwsLocationArgsDict",
    "DeviceLocationArgs",
    "DeviceLocationArgsDict",
    "DxGatewayAttachmentTimeoutsArgs",
    "DxGatewayAttachmentTimeoutsArgsDict",
    "LinkBandwidthArgs",
    "LinkBandwidthArgsDict",
    "SiteLocationArgs",
    "SiteLocationArgsDict",
    "VpcAttachmentOptionsArgs",
    "VpcAttachmentOptionsArgsDict",
    "GetCoreNetworkPolicyDocumentAttachmentPolicyArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCoreNetworkPolicyDocumentRoutingPolicyArgs",
    "GetCoreNetworkPolicyDocumentRoutingPolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCoreNetworkPolicyDocumentSegmentArgs",
    "GetCoreNetworkPolicyDocumentSegmentArgsDict",
    "GetCoreNetworkPolicyDocumentSegmentActionArgs",
    "GetCoreNetworkPolicyDocumentSegmentActionArgsDict",
    ...,
    ...,
    "GetCoreNetworkPolicyDocumentSegmentActionViaArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
]

class ConnectAttachmentOptionsArgsDict(TypedDict):
    protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectAttachmentOptionsArgs:
    def __init__(
        __self__, *, protocol: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectPeerBgpOptionsArgsDict(TypedDict):
    peer_asn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectPeerBgpOptionsArgs:
    def __init__(
        __self__, *, peer_asn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectPeerConfigurationArgsDict(TypedDict):
    bgp_configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectPeerConfigurationBgpConfigurationArgsDict]]
        ]
    ]
    core_network_address: NotRequired[pulumi.Input[_builtins.str]]
    inside_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    peer_address: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectPeerConfigurationArgs:
    def __init__(
        __self__,
        *,
        bgp_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectPeerConfigurationBgpConfigurationArgs]]
            ]
        ] = ...,
        core_network_address: Optional[pulumi.Input[_builtins.str]] = ...,
        inside_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bgpConfigurations")
    def bgp_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectPeerConfigurationBgpConfigurationArgs]]
        ]
    ]: ...
    @bgp_configurations.setter
    def bgp_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectPeerConfigurationBgpConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_address.setter
    def peer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectPeerConfigurationBgpConfigurationArgsDict(TypedDict):
    core_network_address: NotRequired[pulumi.Input[_builtins.str]]
    core_network_asn: NotRequired[pulumi.Input[_builtins.int]]
    peer_address: NotRequired[pulumi.Input[_builtins.str]]
    peer_asn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectPeerConfigurationBgpConfigurationArgs:
    def __init__(
        __self__,
        *,
        core_network_address: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        peer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_asn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkAsn")
    def core_network_asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @core_network_asn.setter
    def core_network_asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_address.setter
    def peer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CoreNetworkEdgeArgsDict(TypedDict):
    asn: NotRequired[pulumi.Input[_builtins.int]]
    edge_location: NotRequired[pulumi.Input[_builtins.str]]
    inside_cidr_blocks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CoreNetworkEdgeArgs:
    def __init__(
        __self__,
        *,
        asn: Optional[pulumi.Input[_builtins.int]] = ...,
        edge_location: Optional[pulumi.Input[_builtins.str]] = ...,
        inside_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @asn.setter
    def asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CoreNetworkSegmentArgsDict(TypedDict):
    edge_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    shared_segments: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CoreNetworkSegmentArgs:
    def __init__(
        __self__,
        *,
        edge_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_segments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @edge_locations.setter
    def edge_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedSegments")
    def shared_segments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_segments.setter
    def shared_segments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeviceAwsLocationArgsDict(TypedDict):
    subnet_arn: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeviceAwsLocationArgs:
    def __init__(
        __self__,
        *,
        subnet_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeviceLocationArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    latitude: NotRequired[pulumi.Input[_builtins.str]]
    longitude: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeviceLocationArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        latitude: Optional[pulumi.Input[_builtins.str]] = ...,
        longitude: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DxGatewayAttachmentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DxGatewayAttachmentTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinkBandwidthArgsDict(TypedDict):
    download_speed: NotRequired[pulumi.Input[_builtins.int]]
    upload_speed: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LinkBandwidthArgs:
    def __init__(
        __self__,
        *,
        download_speed: Optional[pulumi.Input[_builtins.int]] = ...,
        upload_speed: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="downloadSpeed")
    def download_speed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @download_speed.setter
    def download_speed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @upload_speed.setter
    def upload_speed(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SiteLocationArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    latitude: NotRequired[pulumi.Input[_builtins.str]]
    longitude: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SiteLocationArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        latitude: Optional[pulumi.Input[_builtins.str]] = ...,
        longitude: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcAttachmentOptionsArgsDict(TypedDict):
    appliance_mode_support: NotRequired[pulumi.Input[_builtins.bool]]
    dns_support: NotRequired[pulumi.Input[_builtins.bool]]
    ipv6_support: NotRequired[pulumi.Input[_builtins.bool]]
    security_group_referencing_support: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VpcAttachmentOptionsArgs:
    def __init__(
        __self__,
        *,
        appliance_mode_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv6_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_group_referencing_support: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @appliance_mode_support.setter
    def appliance_mode_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dns_support.setter
    def dns_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ipv6_support.setter
    def ipv6_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @security_group_referencing_support.setter
    def security_group_referencing_support(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class GetCoreNetworkPolicyDocumentAttachmentPolicyArgsDict(TypedDict):
    action: GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgsDict
    conditions: Sequence[GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgsDict]
    rule_number: _builtins.int
    condition_logic: NotRequired[_builtins.str]
    description: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyArgs:
    def __init__(
        __self__,
        *,
        action: GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgs,
        conditions: Sequence[GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgs],
        rule_number: _builtins.int,
        condition_logic: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgs: ...
    @action.setter
    def action(self, value: GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgs): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Sequence[GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgs]: ...
    @conditions.setter
    def conditions(
        self, value: Sequence[GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @rule_number.setter
    def rule_number(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter(name="conditionLogic")
    def condition_logic(self) -> Optional[_builtins.str]: ...
    @condition_logic.setter
    def condition_logic(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgsDict(TypedDict):
    add_to_network_function_group: NotRequired[_builtins.str]
    association_method: NotRequired[_builtins.str]
    require_acceptance: NotRequired[_builtins.bool]
    segment: NotRequired[_builtins.str]
    tag_value_of_key: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyActionArgs:
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
    @add_to_network_function_group.setter
    def add_to_network_function_group(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="associationMethod")
    def association_method(self) -> Optional[_builtins.str]: ...
    @association_method.setter
    def association_method(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requireAcceptance")
    def require_acceptance(self) -> Optional[_builtins.bool]: ...
    @require_acceptance.setter
    def require_acceptance(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> Optional[_builtins.str]: ...
    @segment.setter
    def segment(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagValueOfKey")
    def tag_value_of_key(self) -> Optional[_builtins.str]: ...
    @tag_value_of_key.setter
    def tag_value_of_key(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgsDict(TypedDict):
    type: _builtins.str
    key: NotRequired[_builtins.str]
    operator: NotRequired[_builtins.str]
    value: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentPolicyConditionArgs:
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
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @key.setter
    def key(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @operator.setter
    def operator(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...
    @value.setter
    def value(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgsDict(TypedDict):
    action: GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgsDict
    conditions: Sequence[
        GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgsDict
    ]
    rule_number: _builtins.int
    description: NotRequired[_builtins.str]
    edge_locations: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        action: GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgs,
        conditions: Sequence[
            GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgs
        ],
        rule_number: _builtins.int,
        description: Optional[_builtins.str] = ...,
        edge_locations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgs: ...
    @action.setter
    def action(
        self, value: GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgs
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Sequence[
        GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgs
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Sequence[
            GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @rule_number.setter
    def rule_number(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @edge_locations.setter
    def edge_locations(self, value: Optional[Sequence[_builtins.str]]): ...

class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgsDict(TypedDict):
    associate_routing_policies: Sequence[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleActionArgs:
    def __init__(
        __self__, *, associate_routing_policies: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associateRoutingPolicies")
    def associate_routing_policies(self) -> Sequence[_builtins.str]: ...
    @associate_routing_policies.setter
    def associate_routing_policies(self, value: Sequence[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgsDict(
    TypedDict
):
    type: _builtins.str
    value: _builtins.str

@pulumi.input_type
class GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleConditionArgs:
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @value.setter
    def value(self, value: _builtins.str): ...

class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgsDict(TypedDict):
    asn_ranges: Sequence[_builtins.str]
    edge_locations: Sequence[
        GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgsDict
    ]
    dns_support: NotRequired[_builtins.bool]
    inside_cidr_blocks: NotRequired[Sequence[_builtins.str]]
    security_group_referencing_support: NotRequired[_builtins.bool]
    vpn_ecmp_support: NotRequired[_builtins.bool]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        asn_ranges: Sequence[_builtins.str],
        edge_locations: Sequence[
            GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgs
        ],
        dns_support: Optional[_builtins.bool] = ...,
        inside_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
        security_group_referencing_support: Optional[_builtins.bool] = ...,
        vpn_ecmp_support: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asnRanges")
    def asn_ranges(self) -> Sequence[_builtins.str]: ...
    @asn_ranges.setter
    def asn_ranges(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(
        self,
    ) -> Sequence[
        GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgs
    ]: ...
    @edge_locations.setter
    def edge_locations(
        self,
        value: Sequence[
            GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[_builtins.bool]: ...
    @dns_support.setter
    def dns_support(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> Optional[_builtins.bool]: ...
    @security_group_referencing_support.setter
    def security_group_referencing_support(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> Optional[_builtins.bool]: ...
    @vpn_ecmp_support.setter
    def vpn_ecmp_support(self, value: Optional[_builtins.bool]): ...

class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgsDict(
    TypedDict
):
    location: _builtins.str
    asn: NotRequired[_builtins.str]
    inside_cidr_blocks: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentCoreNetworkConfigurationEdgeLocationArgs:
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
    @location.setter
    def location(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.str]: ...
    @asn.setter
    def asn(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[Sequence[_builtins.str]]): ...

class GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgsDict(TypedDict):
    name: _builtins.str
    require_attachment_acceptance: _builtins.bool
    description: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgs:
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
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="requireAttachmentAcceptance")
    def require_attachment_acceptance(self) -> _builtins.bool: ...
    @require_attachment_acceptance.setter
    def require_attachment_acceptance(self, value: _builtins.bool): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentRoutingPolicyArgsDict(TypedDict):
    routing_policy_direction: _builtins.str
    routing_policy_name: _builtins.str
    routing_policy_number: _builtins.int
    routing_policy_rules: Sequence[
        GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgsDict
    ]
    routing_policy_description: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentRoutingPolicyArgs:
    def __init__(
        __self__,
        *,
        routing_policy_direction: _builtins.str,
        routing_policy_name: _builtins.str,
        routing_policy_number: _builtins.int,
        routing_policy_rules: Sequence[
            GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgs
        ],
        routing_policy_description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyDirection")
    def routing_policy_direction(self) -> _builtins.str: ...
    @routing_policy_direction.setter
    def routing_policy_direction(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyName")
    def routing_policy_name(self) -> _builtins.str: ...
    @routing_policy_name.setter
    def routing_policy_name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNumber")
    def routing_policy_number(self) -> _builtins.int: ...
    @routing_policy_number.setter
    def routing_policy_number(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyRules")
    def routing_policy_rules(
        self,
    ) -> Sequence[GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgs]: ...
    @routing_policy_rules.setter
    def routing_policy_rules(
        self,
        value: Sequence[GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyDescription")
    def routing_policy_description(self) -> Optional[_builtins.str]: ...
    @routing_policy_description.setter
    def routing_policy_description(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgsDict(TypedDict):
    rule_definition: (
        GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgsDict
    )
    rule_number: _builtins.int

@pulumi.input_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        rule_definition: GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgs,
        rule_number: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(
        self,
    ) -> (
        GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgs
    ): ...
    @rule_definition.setter
    def rule_definition(
        self,
        value: GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgs,
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> _builtins.int: ...
    @rule_number.setter
    def rule_number(self, value: _builtins.int): ...

class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgsDict(
    TypedDict
):
    action: GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgsDict
    condition_logic: NotRequired[_builtins.str]
    match_conditions: NotRequired[
        Sequence[
            GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgsDict
        ]
    ]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionArgs:
    def __init__(
        __self__,
        *,
        action: GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgs,
        condition_logic: Optional[_builtins.str] = ...,
        match_conditions: Optional[
            Sequence[
                GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgs: ...
    @action.setter
    def action(
        self,
        value: GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgs,
    ): ...
    @_builtins.property
    @pulumi.getter(name="conditionLogic")
    def condition_logic(self) -> Optional[_builtins.str]: ...
    @condition_logic.setter
    def condition_logic(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(
        self,
    ) -> Optional[
        Sequence[
            GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgs
        ]
    ]: ...
    @match_conditions.setter
    def match_conditions(
        self,
        value: Optional[
            Sequence[
                GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgs
            ]
        ],
    ): ...

class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgsDict(
    TypedDict
):
    type: _builtins.str
    value: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionActionArgs:
    def __init__(
        __self__, *, type: _builtins.str, value: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...
    @value.setter
    def value(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgsDict(
    TypedDict
):
    type: _builtins.str
    value: _builtins.str

@pulumi.input_type
class GetCoreNetworkPolicyDocumentRoutingPolicyRoutingPolicyRuleRuleDefinitionMatchConditionArgs:
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @value.setter
    def value(self, value: _builtins.str): ...

class GetCoreNetworkPolicyDocumentSegmentArgsDict(TypedDict):
    name: _builtins.str
    allow_filters: NotRequired[Sequence[_builtins.str]]
    deny_filters: NotRequired[Sequence[_builtins.str]]
    description: NotRequired[_builtins.str]
    edge_locations: NotRequired[Sequence[_builtins.str]]
    isolate_attachments: NotRequired[_builtins.bool]
    require_attachment_acceptance: NotRequired[_builtins.bool]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentArgs:
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
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="allowFilters")
    def allow_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @allow_filters.setter
    def allow_filters(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="denyFilters")
    def deny_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @deny_filters.setter
    def deny_filters(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @edge_locations.setter
    def edge_locations(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isolateAttachments")
    def isolate_attachments(self) -> Optional[_builtins.bool]: ...
    @isolate_attachments.setter
    def isolate_attachments(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="requireAttachmentAcceptance")
    def require_attachment_acceptance(self) -> Optional[_builtins.bool]: ...
    @require_attachment_acceptance.setter
    def require_attachment_acceptance(self, value: Optional[_builtins.bool]): ...

class GetCoreNetworkPolicyDocumentSegmentActionArgsDict(TypedDict):
    action: _builtins.str
    segment: _builtins.str
    description: NotRequired[_builtins.str]
    destination_cidr_blocks: NotRequired[Sequence[_builtins.str]]
    destinations: NotRequired[Sequence[_builtins.str]]
    edge_location_association: NotRequired[
        GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgsDict
    ]
    mode: NotRequired[_builtins.str]
    routing_policy_names: NotRequired[Sequence[_builtins.str]]
    share_with_excepts: NotRequired[Sequence[_builtins.str]]
    share_withs: NotRequired[Sequence[_builtins.str]]
    via: NotRequired[GetCoreNetworkPolicyDocumentSegmentActionViaArgsDict]
    when_sent_to: NotRequired[
        GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgsDict
    ]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentActionArgs:
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        segment: _builtins.str,
        description: Optional[_builtins.str] = ...,
        destination_cidr_blocks: Optional[Sequence[_builtins.str]] = ...,
        destinations: Optional[Sequence[_builtins.str]] = ...,
        edge_location_association: Optional[
            GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgs
        ] = ...,
        mode: Optional[_builtins.str] = ...,
        routing_policy_names: Optional[Sequence[_builtins.str]] = ...,
        share_with_excepts: Optional[Sequence[_builtins.str]] = ...,
        share_withs: Optional[Sequence[_builtins.str]] = ...,
        via: Optional[GetCoreNetworkPolicyDocumentSegmentActionViaArgs] = ...,
        when_sent_to: Optional[
            GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgs
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @action.setter
    def action(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> _builtins.str: ...
    @segment.setter
    def segment(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlocks")
    def destination_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]: ...
    @destination_cidr_blocks.setter
    def destination_cidr_blocks(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]: ...
    @destinations.setter
    def destinations(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocationAssociation")
    def edge_location_association(
        self,
    ) -> Optional[
        GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgs
    ]: ...
    @edge_location_association.setter
    def edge_location_association(
        self,
        value: Optional[
            GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @mode.setter
    def mode(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNames")
    def routing_policy_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @routing_policy_names.setter
    def routing_policy_names(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareWithExcepts")
    def share_with_excepts(self) -> Optional[Sequence[_builtins.str]]: ...
    @share_with_excepts.setter
    def share_with_excepts(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareWiths")
    def share_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @share_withs.setter
    def share_withs(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def via(self) -> Optional[GetCoreNetworkPolicyDocumentSegmentActionViaArgs]: ...
    @via.setter
    def via(
        self, value: Optional[GetCoreNetworkPolicyDocumentSegmentActionViaArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="whenSentTo")
    def when_sent_to(
        self,
    ) -> Optional[GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgs]: ...
    @when_sent_to.setter
    def when_sent_to(
        self, value: Optional[GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgs]
    ): ...

class GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgsDict(
    TypedDict
):
    edge_location: _builtins.str
    peer_edge_location: _builtins.str
    routing_policy_names: Sequence[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentActionEdgeLocationAssociationArgs:
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
    @edge_location.setter
    def edge_location(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="peerEdgeLocation")
    def peer_edge_location(self) -> _builtins.str: ...
    @peer_edge_location.setter
    def peer_edge_location(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicyNames")
    def routing_policy_names(self) -> Sequence[_builtins.str]: ...
    @routing_policy_names.setter
    def routing_policy_names(self, value: Sequence[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentSegmentActionViaArgsDict(TypedDict):
    network_function_groups: NotRequired[Sequence[_builtins.str]]
    with_edge_overrides: NotRequired[
        Sequence[GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgsDict]
    ]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentActionViaArgs:
    def __init__(
        __self__,
        *,
        network_function_groups: Optional[Sequence[_builtins.str]] = ...,
        with_edge_overrides: Optional[
            Sequence[GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkFunctionGroups")
    def network_function_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @network_function_groups.setter
    def network_function_groups(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="withEdgeOverrides")
    def with_edge_overrides(
        self,
    ) -> Optional[
        Sequence[GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgs]
    ]: ...
    @with_edge_overrides.setter
    def with_edge_overrides(
        self,
        value: Optional[
            Sequence[GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgs]
        ],
    ): ...

class GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgsDict(TypedDict):
    edge_sets: NotRequired[Sequence[Sequence[_builtins.str]]]
    use_edge: NotRequired[_builtins.str]
    use_edge_location: NotRequired[_builtins.str]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentActionViaWithEdgeOverrideArgs:
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
    @edge_sets.setter
    def edge_sets(self, value: Optional[Sequence[Sequence[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="useEdge")
    @_utilities.deprecated(...)
    def use_edge(self) -> Optional[_builtins.str]: ...
    @use_edge.setter
    def use_edge(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useEdgeLocation")
    def use_edge_location(self) -> Optional[_builtins.str]: ...
    @use_edge_location.setter
    def use_edge_location(self, value: Optional[_builtins.str]): ...

class GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgsDict(TypedDict):
    segments: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetCoreNetworkPolicyDocumentSegmentActionWhenSentToArgs:
    def __init__(
        __self__, *, segments: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[Sequence[_builtins.str]]: ...
    @segments.setter
    def segments(self, value: Optional[Sequence[_builtins.str]]): ...
