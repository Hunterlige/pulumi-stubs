import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ArmIdentityResponse",
    "ArmUserIdentityResponse",
    "CertificatePropertiesResponse",
    "CloudToDevicePropertiesResponse",
    "EnrichmentPropertiesResponse",
    "EventHubPropertiesResponse",
    "FallbackRoutePropertiesResponse",
    "FeedbackPropertiesResponse",
    "IotHubLocationDescriptionResponse",
    "IotHubPropertiesResponse",
    "IotHubSkuInfoResponse",
    "IpFilterRuleResponse",
    "ManagedIdentityResponse",
    "MessagingEndpointPropertiesResponse",
    "NetworkRuleSetIpRuleResponse",
    "NetworkRuleSetPropertiesResponse",
    "PrivateEndpointConnectionPropertiesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "RoutePropertiesResponse",
    "RoutingCosmosDBSqlApiPropertiesResponse",
    "RoutingEndpointsResponse",
    "RoutingEventHubPropertiesResponse",
    "RoutingPropertiesResponse",
    "RoutingServiceBusQueueEndpointPropertiesResponse",
    "RoutingServiceBusTopicEndpointPropertiesResponse",
    "RoutingStorageContainerPropertiesResponse",
    "SharedAccessSignatureAuthorizationRuleResponse",
    "StorageEndpointPropertiesResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class ArmIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.ArmUserIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.ArmUserIdentityResponse]]: ...

@pulumi.output_type
class ArmUserIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class CertificatePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created: _builtins.str,
        expiry: _builtins.str,
        subject: _builtins.str,
        thumbprint: _builtins.str,
        updated: _builtins.str,
        certificate: Optional[_builtins.str] = ...,
        is_verified: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isVerified")
    def is_verified(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CloudToDevicePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ttl_as_iso8601: Optional[_builtins.str] = ...,
        feedback: Optional[outputs.FeedbackPropertiesResponse] = ...,
        max_delivery_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtlAsIso8601")
    def default_ttl_as_iso8601(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def feedback(self) -> Optional[outputs.FeedbackPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EnrichmentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_names: Sequence[_builtins.str],
        key: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class EventHubPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: _builtins.str,
        partition_ids: Sequence[_builtins.str],
        path: _builtins.str,
        partition_count: Optional[_builtins.int] = ...,
        retention_time_in_days: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partitionIds")
    def partition_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retentionTimeInDays")
    def retention_time_in_days(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class FallbackRoutePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_names: Sequence[_builtins.str],
        is_enabled: _builtins.bool,
        source: _builtins.str,
        condition: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeedbackPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lock_duration_as_iso8601: Optional[_builtins.str] = ...,
        max_delivery_count: Optional[_builtins.int] = ...,
        ttl_as_iso8601: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lockDurationAsIso8601")
    def lock_duration_as_iso8601(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ttlAsIso8601")
    def ttl_as_iso8601(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IotHubLocationDescriptionResponse(dict):
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IotHubPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: _builtins.str,
        locations: Sequence[outputs.IotHubLocationDescriptionResponse],
        provisioning_state: _builtins.str,
        state: _builtins.str,
        allowed_fqdn_list: Optional[Sequence[_builtins.str]] = ...,
        authorization_policies: Optional[
            Sequence[outputs.SharedAccessSignatureAuthorizationRuleResponse]
        ] = ...,
        cloud_to_device: Optional[outputs.CloudToDevicePropertiesResponse] = ...,
        comments: Optional[_builtins.str] = ...,
        disable_device_sas: Optional[_builtins.bool] = ...,
        disable_local_auth: Optional[_builtins.bool] = ...,
        disable_module_sas: Optional[_builtins.bool] = ...,
        enable_data_residency: Optional[_builtins.bool] = ...,
        enable_file_upload_notifications: Optional[_builtins.bool] = ...,
        event_hub_endpoints: Optional[
            Mapping[str, outputs.EventHubPropertiesResponse]
        ] = ...,
        features: Optional[_builtins.str] = ...,
        ip_filter_rules: Optional[Sequence[outputs.IpFilterRuleResponse]] = ...,
        messaging_endpoints: Optional[
            Mapping[str, outputs.MessagingEndpointPropertiesResponse]
        ] = ...,
        min_tls_version: Optional[_builtins.str] = ...,
        network_rule_sets: Optional[outputs.NetworkRuleSetPropertiesResponse] = ...,
        private_endpoint_connections: Optional[
            Sequence[outputs.PrivateEndpointConnectionResponse]
        ] = ...,
        public_network_access: Optional[_builtins.str] = ...,
        restrict_outbound_network_access: Optional[_builtins.bool] = ...,
        routing: Optional[outputs.RoutingPropertiesResponse] = ...,
        storage_endpoints: Optional[
            Mapping[str, outputs.StorageEndpointPropertiesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.IotHubLocationDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedFqdnList")
    def allowed_fqdn_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(
        self,
    ) -> Optional[Sequence[outputs.SharedAccessSignatureAuthorizationRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudToDevice")
    def cloud_to_device(self) -> Optional[outputs.CloudToDevicePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def comments(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableDeviceSAS")
    def disable_device_sas(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableModuleSAS")
    def disable_module_sas(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableDataResidency")
    def enable_data_residency(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableFileUploadNotifications")
    def enable_file_upload_notifications(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubEndpoints")
    def event_hub_endpoints(
        self,
    ) -> Optional[Mapping[str, outputs.EventHubPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipFilterRules")
    def ip_filter_rules(self) -> Optional[Sequence[outputs.IpFilterRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="messagingEndpoints")
    def messaging_endpoints(
        self,
    ) -> Optional[Mapping[str, outputs.MessagingEndpointPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="minTlsVersion")
    def min_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkRuleSets")
    def network_rule_sets(
        self,
    ) -> Optional[outputs.NetworkRuleSetPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restrictOutboundNetworkAccess")
    def restrict_outbound_network_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def routing(self) -> Optional[outputs.RoutingPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageEndpoints")
    def storage_endpoints(
        self,
    ) -> Optional[Mapping[str, outputs.StorageEndpointPropertiesResponse]]: ...

@pulumi.output_type
class IotHubSkuInfoResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        tier: _builtins.str,
        capacity: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class IpFilterRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        filter_name: _builtins.str,
        ip_mask: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, user_assigned_identity: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MessagingEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lock_duration_as_iso8601: Optional[_builtins.str] = ...,
        max_delivery_count: Optional[_builtins.int] = ...,
        ttl_as_iso8601: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lockDurationAsIso8601")
    def lock_duration_as_iso8601(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ttlAsIso8601")
    def ttl_as_iso8601(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkRuleSetIpRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_name: _builtins.str,
        ip_mask: _builtins.str,
        action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkRuleSetPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apply_to_built_in_event_hub_endpoint: _builtins.bool,
        ip_rules: Sequence[outputs.NetworkRuleSetIpRuleResponse],
        default_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyToBuiltInEventHubEndpoint")
    def apply_to_built_in_event_hub_endpoint(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Sequence[outputs.NetworkRuleSetIpRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        properties: outputs.PrivateEndpointConnectionPropertiesResponse,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        status: _builtins.str,
        actions_required: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_names: Sequence[_builtins.str],
        is_enabled: _builtins.bool,
        name: _builtins.str,
        source: _builtins.str,
        condition: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointNames")
    def endpoint_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingCosmosDBSqlApiPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_name: _builtins.str,
        database_name: _builtins.str,
        endpoint_uri: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        partition_key_name: Optional[_builtins.str] = ...,
        partition_key_template: Optional[_builtins.str] = ...,
        primary_key: Optional[_builtins.str] = ...,
        resource_group: Optional[_builtins.str] = ...,
        secondary_key: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyName")
    def partition_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyTemplate")
    def partition_key_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingEndpointsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cosmos_db_sql_containers: Optional[
            Sequence[outputs.RoutingCosmosDBSqlApiPropertiesResponse]
        ] = ...,
        event_hubs: Optional[Sequence[outputs.RoutingEventHubPropertiesResponse]] = ...,
        service_bus_queues: Optional[
            Sequence[outputs.RoutingServiceBusQueueEndpointPropertiesResponse]
        ] = ...,
        service_bus_topics: Optional[
            Sequence[outputs.RoutingServiceBusTopicEndpointPropertiesResponse]
        ] = ...,
        storage_containers: Optional[
            Sequence[outputs.RoutingStorageContainerPropertiesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDBSqlContainers")
    def cosmos_db_sql_containers(
        self,
    ) -> Optional[Sequence[outputs.RoutingCosmosDBSqlApiPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubs")
    def event_hubs(
        self,
    ) -> Optional[Sequence[outputs.RoutingEventHubPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusQueues")
    def service_bus_queues(
        self,
    ) -> Optional[
        Sequence[outputs.RoutingServiceBusQueueEndpointPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusTopics")
    def service_bus_topics(
        self,
    ) -> Optional[
        Sequence[outputs.RoutingServiceBusTopicEndpointPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="storageContainers")
    def storage_containers(
        self,
    ) -> Optional[Sequence[outputs.RoutingStorageContainerPropertiesResponse]]: ...

@pulumi.output_type
class RoutingEventHubPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        connection_string: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        entity_path: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        resource_group: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoints: Optional[outputs.RoutingEndpointsResponse] = ...,
        enrichments: Optional[Sequence[outputs.EnrichmentPropertiesResponse]] = ...,
        fallback_route: Optional[outputs.FallbackRoutePropertiesResponse] = ...,
        routes: Optional[Sequence[outputs.RoutePropertiesResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[outputs.RoutingEndpointsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def enrichments(
        self,
    ) -> Optional[Sequence[outputs.EnrichmentPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="fallbackRoute")
    def fallback_route(self) -> Optional[outputs.FallbackRoutePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[Sequence[outputs.RoutePropertiesResponse]]: ...

@pulumi.output_type
class RoutingServiceBusQueueEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        connection_string: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        entity_path: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        resource_group: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingServiceBusTopicEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        connection_string: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        entity_path: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        resource_group: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingStorageContainerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_name: _builtins.str,
        name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        batch_frequency_in_seconds: Optional[_builtins.int] = ...,
        connection_string: Optional[_builtins.str] = ...,
        encoding: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        file_name_format: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        max_chunk_size_in_bytes: Optional[_builtins.int] = ...,
        resource_group: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="batchFrequencyInSeconds")
    def batch_frequency_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileNameFormat")
    def file_name_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="maxChunkSizeInBytes")
    def max_chunk_size_in_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SharedAccessSignatureAuthorizationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: _builtins.str,
        rights: _builtins.str,
        primary_key: Optional[_builtins.str] = ...,
        secondary_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rights(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_string: _builtins.str,
        container_name: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityResponse] = ...,
        sas_ttl_as_iso8601: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sasTtlAsIso8601")
    def sas_ttl_as_iso8601(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...
