import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureDataExplorerConnectionPropertiesResponse",
    "ConnectionPropertiesResponse",
    ...,
    "DigitalTwinsIdentityResponse",
    "EventGridResponse",
    "EventHubResponse",
    "ManagedIdentityReferenceResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "ServiceBusResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class AzureDataExplorerConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        adx_database_name: _builtins.str,
        adx_endpoint_uri: _builtins.str,
        adx_resource_id: _builtins.str,
        connection_type: _builtins.str,
        event_hub_endpoint_uri: _builtins.str,
        event_hub_entity_path: _builtins.str,
        event_hub_namespace_resource_id: _builtins.str,
        provisioning_state: _builtins.str,
        adx_relationship_lifecycle_events_table_name: Optional[_builtins.str] = ...,
        adx_table_name: Optional[_builtins.str] = ...,
        adx_twin_lifecycle_events_table_name: Optional[_builtins.str] = ...,
        event_hub_consumer_group: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityReferenceResponse] = ...,
        record_property_and_item_removals: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adxDatabaseName")
    def adx_database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="adxEndpointUri")
    def adx_endpoint_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="adxResourceId")
    def adx_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventHubEndpointUri")
    def event_hub_endpoint_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventHubEntityPath")
    def event_hub_entity_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventHubNamespaceResourceId")
    def event_hub_namespace_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="adxRelationshipLifecycleEventsTableName")
    def adx_relationship_lifecycle_events_table_name(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="adxTableName")
    def adx_table_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="adxTwinLifecycleEventsTableName")
    def adx_twin_lifecycle_events_table_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubConsumerGroup")
    def event_hub_consumer_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="recordPropertyAndItemRemovals")
    def record_property_and_item_removals(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        group_ids: Optional[Sequence[_builtins.str]] = ...,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
        private_link_service_connection_state: Optional[
            outputs.ConnectionPropertiesResponsePrivateLinkServiceConnectionState
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[
        outputs.ConnectionPropertiesResponsePrivateLinkServiceConnectionState
    ]: ...

@pulumi.output_type
class ConnectionPropertiesResponsePrivateLinkServiceConnectionState(dict):
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
class DigitalTwinsIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
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
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class EventGridResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_key1: _builtins.str,
        created_time: _builtins.str,
        endpoint_type: _builtins.str,
        provisioning_state: _builtins.str,
        topic_endpoint: _builtins.str,
        access_key2: Optional[_builtins.str] = ...,
        authentication_type: Optional[_builtins.str] = ...,
        dead_letter_secret: Optional[_builtins.str] = ...,
        dead_letter_uri: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKey1")
    def access_key1(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="topicEndpoint")
    def topic_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessKey2")
    def access_key2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityReferenceResponse]: ...

@pulumi.output_type
class EventHubResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_time: _builtins.str,
        endpoint_type: _builtins.str,
        provisioning_state: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        connection_string_primary_key: Optional[_builtins.str] = ...,
        connection_string_secondary_key: Optional[_builtins.str] = ...,
        dead_letter_secret: Optional[_builtins.str] = ...,
        dead_letter_uri: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        entity_path: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionStringPrimaryKey")
    def connection_string_primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionStringSecondaryKey")
    def connection_string_secondary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityReferenceResponse]: ...

@pulumi.output_type
class ManagedIdentityReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        user_assigned_identity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        properties: outputs.ConnectionPropertiesResponse,
        system_data: outputs.SystemDataResponse,
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
    def properties(self) -> outputs.ConnectionPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
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
class ServiceBusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_time: _builtins.str,
        endpoint_type: _builtins.str,
        provisioning_state: _builtins.str,
        authentication_type: Optional[_builtins.str] = ...,
        dead_letter_secret: Optional[_builtins.str] = ...,
        dead_letter_uri: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        entity_path: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedIdentityReferenceResponse] = ...,
        primary_connection_string: Optional[_builtins.str] = ...,
        secondary_connection_string: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[_builtins.str]: ...

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

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
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
