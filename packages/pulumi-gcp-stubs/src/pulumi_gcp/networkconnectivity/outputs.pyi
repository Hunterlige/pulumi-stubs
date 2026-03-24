import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DestinationEndpoint",
    "DestinationStateTimeline",
    "DestinationStateTimelineState",
    "GroupAutoAccept",
    "HubRoutingVpc",
    "InternalRangeAllocationOptions",
    "InternalRangeMigration",
    "MulticloudDataTransferConfigService",
    "MulticloudDataTransferConfigServiceState",
    "PolicyBasedRouteFilter",
    "PolicyBasedRouteInterconnectAttachment",
    "PolicyBasedRouteVirtualMachine",
    "PolicyBasedRouteWarning",
    "ServiceConnectionPolicyPscConfig",
    "ServiceConnectionPolicyPscConnection",
    "ServiceConnectionPolicyPscConnectionError",
    "ServiceConnectionPolicyPscConnectionErrorInfo",
    "SpokeGateway",
    "SpokeGatewayIpRangeReservation",
    "SpokeLinkedInterconnectAttachments",
    "SpokeLinkedProducerVpcNetwork",
    "SpokeLinkedRouterApplianceInstances",
    "SpokeLinkedRouterApplianceInstancesInstance",
    "SpokeLinkedVpcNetwork",
    "SpokeLinkedVpnTunnels",
    "SpokeReason",
]

@pulumi.output_type
class DestinationEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asn: _builtins.str,
        csp: _builtins.str,
        state: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def csp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DestinationStateTimeline(dict):
    def __init__(
        __self__,
        *,
        states: Optional[Sequence[outputs.DestinationStateTimelineState]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def states(self) -> Optional[Sequence[outputs.DestinationStateTimelineState]]: ...

@pulumi.output_type
class DestinationStateTimelineState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effective_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GroupAutoAccept(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, auto_accept_projects: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptProjects")
    def auto_accept_projects(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class HubRoutingVpc(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InternalRangeAllocationOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[_builtins.str] = ...,
        first_available_ranges_lookup_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstAvailableRangesLookupSize")
    def first_available_ranges_lookup_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InternalRangeMigration(dict):
    def __init__(__self__, *, source: _builtins.str, target: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class MulticloudDataTransferConfigService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: _builtins.str,
        states: Optional[
            Sequence[outputs.MulticloudDataTransferConfigServiceState]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> Optional[Sequence[outputs.MulticloudDataTransferConfigServiceState]]: ...

@pulumi.output_type
class MulticloudDataTransferConfigServiceState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effective_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyBasedRouteFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        protocol_version: _builtins.str,
        dest_range: Optional[_builtins.str] = ...,
        ip_protocol: Optional[_builtins.str] = ...,
        src_range: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="srcRange")
    def src_range(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyBasedRouteInterconnectAttachment(dict):
    def __init__(__self__, *, region: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyBasedRouteVirtualMachine(dict):
    def __init__(__self__, *, tags: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class PolicyBasedRouteWarning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        data: Optional[Mapping[str, _builtins.str]] = ...,
        warning_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceConnectionPolicyPscConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnetworks: Sequence[_builtins.str],
        allowed_google_producers_resource_hierarchy_levels: Optional[
            Sequence[_builtins.str]
        ] = ...,
        limit: Optional[_builtins.str] = ...,
        producer_instance_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedGoogleProducersResourceHierarchyLevels")
    def allowed_google_producers_resource_hierarchy_levels(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def limit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="producerInstanceLocation")
    def producer_instance_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceConnectionPolicyPscConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_address: Optional[_builtins.str] = ...,
        consumer_forwarding_rule: Optional[_builtins.str] = ...,
        consumer_target_project: Optional[_builtins.str] = ...,
        error: Optional[outputs.ServiceConnectionPolicyPscConnectionError] = ...,
        error_info: Optional[
            outputs.ServiceConnectionPolicyPscConnectionErrorInfo
        ] = ...,
        error_type: Optional[_builtins.str] = ...,
        gce_operation: Optional[_builtins.str] = ...,
        psc_connection_id: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerAddress")
    def consumer_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerForwardingRule")
    def consumer_forwarding_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerTargetProject")
    def consumer_target_project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ServiceConnectionPolicyPscConnectionError]: ...
    @_builtins.property
    @pulumi.getter(name="errorInfo")
    def error_info(
        self,
    ) -> Optional[outputs.ServiceConnectionPolicyPscConnectionErrorInfo]: ...
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gceOperation")
    def gce_operation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceConnectionPolicyPscConnectionError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[Sequence[Mapping[str, _builtins.str]]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceConnectionPolicyPscConnectionErrorInfo(dict):
    def __init__(
        __self__,
        *,
        domain: Optional[_builtins.str] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpokeGateway(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity: _builtins.str,
        ip_range_reservations: Sequence[outputs.SpokeGatewayIpRangeReservation],
        routers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipRangeReservations")
    def ip_range_reservations(
        self,
    ) -> Sequence[outputs.SpokeGatewayIpRangeReservation]: ...
    @_builtins.property
    @pulumi.getter
    def routers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpokeGatewayIpRangeReservation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ip_range: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> _builtins.str: ...

@pulumi.output_type
class SpokeLinkedInterconnectAttachments(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        site_to_site_data_transfer: _builtins.bool,
        uris: Sequence[_builtins.str],
        include_import_ranges: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpokeLinkedProducerVpcNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        peering: _builtins.str,
        exclude_export_ranges: Optional[Sequence[_builtins.str]] = ...,
        include_export_ranges: Optional[Sequence[_builtins.str]] = ...,
        producer_network: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def peering(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeExportRanges")
    def exclude_export_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includeExportRanges")
    def include_export_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="producerNetwork")
    def producer_network(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpokeLinkedRouterApplianceInstances(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.SpokeLinkedRouterApplianceInstancesInstance],
        site_to_site_data_transfer: _builtins.bool,
        include_import_ranges: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Sequence[outputs.SpokeLinkedRouterApplianceInstancesInstance]: ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpokeLinkedRouterApplianceInstancesInstance(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ip_address: _builtins.str, virtual_machine: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> _builtins.str: ...

@pulumi.output_type
class SpokeLinkedVpcNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        exclude_export_ranges: Optional[Sequence[_builtins.str]] = ...,
        include_export_ranges: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeExportRanges")
    def exclude_export_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includeExportRanges")
    def include_export_ranges(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpokeLinkedVpnTunnels(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        site_to_site_data_transfer: _builtins.bool,
        uris: Sequence[_builtins.str],
        include_import_ranges: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeImportRanges")
    def include_import_ranges(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpokeReason(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        user_details: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userDetails")
    def user_details(self) -> Optional[_builtins.str]: ...
