import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DestinationEndpointArgs",
    "DestinationEndpointArgsDict",
    "DestinationStateTimelineArgs",
    "DestinationStateTimelineArgsDict",
    "DestinationStateTimelineStateArgs",
    "DestinationStateTimelineStateArgsDict",
    "GroupAutoAcceptArgs",
    "GroupAutoAcceptArgsDict",
    "HubRoutingVpcArgs",
    "HubRoutingVpcArgsDict",
    "InternalRangeAllocationOptionsArgs",
    "InternalRangeAllocationOptionsArgsDict",
    "InternalRangeMigrationArgs",
    "InternalRangeMigrationArgsDict",
    "MulticloudDataTransferConfigServiceArgs",
    "MulticloudDataTransferConfigServiceArgsDict",
    "MulticloudDataTransferConfigServiceStateArgs",
    "MulticloudDataTransferConfigServiceStateArgsDict",
    "PolicyBasedRouteFilterArgs",
    "PolicyBasedRouteFilterArgsDict",
    "PolicyBasedRouteInterconnectAttachmentArgs",
    "PolicyBasedRouteInterconnectAttachmentArgsDict",
    "PolicyBasedRouteVirtualMachineArgs",
    "PolicyBasedRouteVirtualMachineArgsDict",
    "PolicyBasedRouteWarningArgs",
    "PolicyBasedRouteWarningArgsDict",
    "ServiceConnectionPolicyPscConfigArgs",
    "ServiceConnectionPolicyPscConfigArgsDict",
    "ServiceConnectionPolicyPscConnectionArgs",
    "ServiceConnectionPolicyPscConnectionArgsDict",
    "ServiceConnectionPolicyPscConnectionErrorArgs",
    "ServiceConnectionPolicyPscConnectionErrorArgsDict",
    "ServiceConnectionPolicyPscConnectionErrorInfoArgs",
    ...,
    "SpokeGatewayArgs",
    "SpokeGatewayArgsDict",
    "SpokeGatewayIpRangeReservationArgs",
    "SpokeGatewayIpRangeReservationArgsDict",
    "SpokeLinkedInterconnectAttachmentsArgs",
    "SpokeLinkedInterconnectAttachmentsArgsDict",
    "SpokeLinkedProducerVpcNetworkArgs",
    "SpokeLinkedProducerVpcNetworkArgsDict",
    "SpokeLinkedRouterApplianceInstancesArgs",
    "SpokeLinkedRouterApplianceInstancesArgsDict",
    "SpokeLinkedRouterApplianceInstancesInstanceArgs",
    ...,
    "SpokeLinkedVpcNetworkArgs",
    "SpokeLinkedVpcNetworkArgsDict",
    "SpokeLinkedVpnTunnelsArgs",
    "SpokeLinkedVpnTunnelsArgsDict",
    "SpokeReasonArgs",
    "SpokeReasonArgsDict",
]

class DestinationEndpointArgsDict(TypedDict):
    asn: pulumi.Input[_builtins.str]
    csp: pulumi.Input[_builtins.str]
    state: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DestinationEndpointArgs:
    def __init__(
        __self__,
        *,
        asn: pulumi.Input[_builtins.str],
        csp: pulumi.Input[_builtins.str],
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> pulumi.Input[_builtins.str]: ...
    @asn.setter
    def asn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def csp(self) -> pulumi.Input[_builtins.str]: ...
    @csp.setter
    def csp(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DestinationStateTimelineArgsDict(TypedDict):
    states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DestinationStateTimelineStateArgsDict]]]
    ]

@pulumi.input_type
class DestinationStateTimelineArgs:
    def __init__(
        __self__,
        *,
        states: Optional[
            pulumi.Input[Sequence[pulumi.Input[DestinationStateTimelineStateArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DestinationStateTimelineStateArgs]]]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DestinationStateTimelineStateArgs]]]
        ],
    ): ...

class DestinationStateTimelineStateArgsDict(TypedDict):
    effective_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DestinationStateTimelineStateArgs:
    def __init__(
        __self__,
        *,
        effective_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupAutoAcceptArgsDict(TypedDict):
    auto_accept_projects: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class GroupAutoAcceptArgs:
    def __init__(
        __self__,
        *,
        auto_accept_projects: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptProjects")
    def auto_accept_projects(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @auto_accept_projects.setter
    def auto_accept_projects(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class HubRoutingVpcArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HubRoutingVpcArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InternalRangeAllocationOptionsArgsDict(TypedDict):
    allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    first_available_ranges_lookup_size: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InternalRangeAllocationOptionsArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        first_available_ranges_lookup_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firstAvailableRangesLookupSize")
    def first_available_ranges_lookup_size(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @first_available_ranges_lookup_size.setter
    def first_available_ranges_lookup_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InternalRangeMigrationArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class InternalRangeMigrationArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class MulticloudDataTransferConfigServiceArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    states: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[MulticloudDataTransferConfigServiceStateArgsDict]]
        ]
    ]

@pulumi.input_type
class MulticloudDataTransferConfigServiceArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        states: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MulticloudDataTransferConfigServiceStateArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MulticloudDataTransferConfigServiceStateArgs]]
        ]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MulticloudDataTransferConfigServiceStateArgs]]
            ]
        ],
    ): ...

class MulticloudDataTransferConfigServiceStateArgsDict(TypedDict):
    effective_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MulticloudDataTransferConfigServiceStateArgs:
    def __init__(
        __self__,
        *,
        effective_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyBasedRouteFilterArgsDict(TypedDict):
    protocol_version: pulumi.Input[_builtins.str]
    dest_range: NotRequired[pulumi.Input[_builtins.str]]
    ip_protocol: NotRequired[pulumi.Input[_builtins.str]]
    src_range: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyBasedRouteFilterArgs:
    def __init__(
        __self__,
        *,
        protocol_version: pulumi.Input[_builtins.str],
        dest_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        src_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> pulumi.Input[_builtins.str]: ...
    @protocol_version.setter
    def protocol_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dest_range.setter
    def dest_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="srcRange")
    def src_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @src_range.setter
    def src_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyBasedRouteInterconnectAttachmentArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyBasedRouteInterconnectAttachmentArgs:
    def __init__(__self__, *, region: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class PolicyBasedRouteVirtualMachineArgsDict(TypedDict):
    tags: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class PolicyBasedRouteVirtualMachineArgs:
    def __init__(
        __self__, *, tags: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PolicyBasedRouteWarningArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    warning_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyBasedRouteWarningArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        warning_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def data(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @data.setter
    def data(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warning_message.setter
    def warning_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceConnectionPolicyPscConfigArgsDict(TypedDict):
    subnetworks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_google_producers_resource_hierarchy_levels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    limit: NotRequired[pulumi.Input[_builtins.str]]
    producer_instance_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceConnectionPolicyPscConfigArgs:
    def __init__(
        __self__,
        *,
        subnetworks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        allowed_google_producers_resource_hierarchy_levels: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        limit: Optional[pulumi.Input[_builtins.str]] = ...,
        producer_instance_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnetworks.setter
    def subnetworks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedGoogleProducersResourceHierarchyLevels")
    def allowed_google_producers_resource_hierarchy_levels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_google_producers_resource_hierarchy_levels.setter
    def allowed_google_producers_resource_hierarchy_levels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @limit.setter
    def limit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="producerInstanceLocation")
    def producer_instance_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @producer_instance_location.setter
    def producer_instance_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServiceConnectionPolicyPscConnectionArgsDict(TypedDict):
    consumer_address: NotRequired[pulumi.Input[_builtins.str]]
    consumer_forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    consumer_target_project: NotRequired[pulumi.Input[_builtins.str]]
    error: NotRequired[pulumi.Input[ServiceConnectionPolicyPscConnectionErrorArgsDict]]
    error_info: NotRequired[
        pulumi.Input[ServiceConnectionPolicyPscConnectionErrorInfoArgsDict]
    ]
    error_type: NotRequired[pulumi.Input[_builtins.str]]
    gce_operation: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_id: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionArgs:
    def __init__(
        __self__,
        *,
        consumer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        consumer_forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        consumer_target_project: Optional[pulumi.Input[_builtins.str]] = ...,
        error: Optional[
            pulumi.Input[ServiceConnectionPolicyPscConnectionErrorArgs]
        ] = ...,
        error_info: Optional[
            pulumi.Input[ServiceConnectionPolicyPscConnectionErrorInfoArgs]
        ] = ...,
        error_type: Optional[pulumi.Input[_builtins.str]] = ...,
        gce_operation: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerAddress")
    def consumer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_address.setter
    def consumer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerForwardingRule")
    def consumer_forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_forwarding_rule.setter
    def consumer_forwarding_rule(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consumerTargetProject")
    def consumer_target_project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_target_project.setter
    def consumer_target_project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[pulumi.Input[ServiceConnectionPolicyPscConnectionErrorArgs]]: ...
    @error.setter
    def error(
        self,
        value: Optional[pulumi.Input[ServiceConnectionPolicyPscConnectionErrorArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorInfo")
    def error_info(
        self,
    ) -> Optional[pulumi.Input[ServiceConnectionPolicyPscConnectionErrorInfoArgs]]: ...
    @error_info.setter
    def error_info(
        self,
        value: Optional[
            pulumi.Input[ServiceConnectionPolicyPscConnectionErrorInfoArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_type.setter
    def error_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gceOperation")
    def gce_operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gce_operation.setter
    def gce_operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceConnectionPolicyPscConnectionErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceConnectionPolicyPscConnectionErrorInfoArgsDict(TypedDict):
    domain: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceConnectionPolicyPscConnectionErrorInfoArgs:
    def __init__(
        __self__,
        *,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SpokeGatewayArgsDict(TypedDict):
    capacity: pulumi.Input[_builtins.str]
    ip_range_reservations: pulumi.Input[
        Sequence[pulumi.Input[SpokeGatewayIpRangeReservationArgsDict]]
    ]
    routers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SpokeGatewayArgs:
    def __init__(
        __self__,
        *,
        capacity: pulumi.Input[_builtins.str],
        ip_range_reservations: pulumi.Input[
            Sequence[pulumi.Input[SpokeGatewayIpRangeReservationArgs]]
        ],
        routers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[_builtins.str]: ...
    @capacity.setter
    def capacity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipRangeReservations")
    def ip_range_reservations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SpokeGatewayIpRangeReservationArgs]]]: ...
    @ip_range_reservations.setter
    def ip_range_reservations(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[SpokeGatewayIpRangeReservationArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def routers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @routers.setter
    def routers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SpokeGatewayIpRangeReservationArgsDict(TypedDict):
    ip_range: pulumi.Input[_builtins.str]

@pulumi.input_type
class SpokeGatewayIpRangeReservationArgs:
    def __init__(__self__, *, ip_range: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Input[_builtins.str]: ...
    @ip_range.setter
    def ip_range(self, value: pulumi.Input[_builtins.str]): ...

class SpokeLinkedInterconnectAttachmentsArgsDict(TypedDict):
    site_to_site_data_transfer: pulumi.Input[_builtins.bool]
    uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    include_import_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SpokeLinkedInterconnectAttachmentsArgs:
    def __init__(
        __self__,
        *,
        site_to_site_data_transfer: pulumi.Input[_builtins.bool],
        uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        include_import_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[_builtins.bool]: ...
    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_import_ranges.setter
    def include_import_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SpokeLinkedProducerVpcNetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    peering: pulumi.Input[_builtins.str]
    exclude_export_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    include_export_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    producer_network: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SpokeLinkedProducerVpcNetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        peering: pulumi.Input[_builtins.str],
        exclude_export_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_export_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        producer_network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def peering(self) -> pulumi.Input[_builtins.str]: ...
    @peering.setter
    def peering(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeExportRanges")
    def exclude_export_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_export_ranges.setter
    def exclude_export_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeExportRanges")
    def include_export_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_export_ranges.setter
    def include_export_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="producerNetwork")
    def producer_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @producer_network.setter
    def producer_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SpokeLinkedRouterApplianceInstancesArgsDict(TypedDict):
    instances: pulumi.Input[
        Sequence[pulumi.Input[SpokeLinkedRouterApplianceInstancesInstanceArgsDict]]
    ]
    site_to_site_data_transfer: pulumi.Input[_builtins.bool]
    include_import_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SpokeLinkedRouterApplianceInstancesArgs:
    def __init__(
        __self__,
        *,
        instances: pulumi.Input[
            Sequence[pulumi.Input[SpokeLinkedRouterApplianceInstancesInstanceArgs]]
        ],
        site_to_site_data_transfer: pulumi.Input[_builtins.bool],
        include_import_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[SpokeLinkedRouterApplianceInstancesInstanceArgs]]
    ]: ...
    @instances.setter
    def instances(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[SpokeLinkedRouterApplianceInstancesInstanceArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[_builtins.bool]: ...
    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_import_ranges.setter
    def include_import_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SpokeLinkedRouterApplianceInstancesInstanceArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]
    virtual_machine: pulumi.Input[_builtins.str]

@pulumi.input_type
class SpokeLinkedRouterApplianceInstancesInstanceArgs:
    def __init__(
        __self__,
        *,
        ip_address: pulumi.Input[_builtins.str],
        virtual_machine: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_machine.setter
    def virtual_machine(self, value: pulumi.Input[_builtins.str]): ...

class SpokeLinkedVpcNetworkArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    exclude_export_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    include_export_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SpokeLinkedVpcNetworkArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        exclude_export_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_export_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeExportRanges")
    def exclude_export_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_export_ranges.setter
    def exclude_export_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeExportRanges")
    def include_export_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_export_ranges.setter
    def include_export_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SpokeLinkedVpnTunnelsArgsDict(TypedDict):
    site_to_site_data_transfer: pulumi.Input[_builtins.bool]
    uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    include_import_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SpokeLinkedVpnTunnelsArgs:
    def __init__(
        __self__,
        *,
        site_to_site_data_transfer: pulumi.Input[_builtins.bool],
        uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        include_import_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> pulumi.Input[_builtins.bool]: ...
    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_import_ranges.setter
    def include_import_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SpokeReasonArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    user_details: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SpokeReasonArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        user_details: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userDetails")
    def user_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_details.setter
    def user_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
