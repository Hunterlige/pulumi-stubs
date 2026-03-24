

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureDataExplorerConnectionPropertiesArgs', 'AzureDataExplorerConnectionPropertiesArgsDict', ..., ..., 'ConnectionPropertiesArgs', 'ConnectionPropertiesArgsDict', 'DigitalTwinsIdentityArgs', 'DigitalTwinsIdentityArgsDict', 'EventGridArgs', 'EventGridArgsDict', 'EventHubArgs', 'EventHubArgsDict', 'ManagedIdentityReferenceArgs', 'ManagedIdentityReferenceArgsDict', 'PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict', 'ServiceBusArgs', 'ServiceBusArgsDict']
class AzureDataExplorerConnectionPropertiesArgsDict(TypedDict):
    
    adx_database_name: pulumi.Input[_builtins.str]
    adx_endpoint_uri: pulumi.Input[_builtins.str]
    adx_resource_id: pulumi.Input[_builtins.str]
    connection_type: pulumi.Input[_builtins.str]
    event_hub_endpoint_uri: pulumi.Input[_builtins.str]
    event_hub_entity_path: pulumi.Input[_builtins.str]
    event_hub_namespace_resource_id: pulumi.Input[_builtins.str]
    adx_relationship_lifecycle_events_table_name: NotRequired[pulumi.Input[_builtins.str]]
    adx_table_name: NotRequired[pulumi.Input[_builtins.str]]
    adx_twin_lifecycle_events_table_name: NotRequired[pulumi.Input[_builtins.str]]
    event_hub_consumer_group: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[ManagedIdentityReferenceArgsDict]]
    record_property_and_item_removals: NotRequired[pulumi.Input[Union[_builtins.str, RecordPropertyAndItemRemovals]]]


@pulumi.input_type
class AzureDataExplorerConnectionPropertiesArgs:
    def __init__(__self__, *, adx_database_name: pulumi.Input[_builtins.str], adx_endpoint_uri: pulumi.Input[_builtins.str], adx_resource_id: pulumi.Input[_builtins.str], connection_type: pulumi.Input[_builtins.str], event_hub_endpoint_uri: pulumi.Input[_builtins.str], event_hub_entity_path: pulumi.Input[_builtins.str], event_hub_namespace_resource_id: pulumi.Input[_builtins.str], adx_relationship_lifecycle_events_table_name: Optional[pulumi.Input[_builtins.str]] = ..., adx_table_name: Optional[pulumi.Input[_builtins.str]] = ..., adx_twin_lifecycle_events_table_name: Optional[pulumi.Input[_builtins.str]] = ..., event_hub_consumer_group: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedIdentityReferenceArgs]] = ..., record_property_and_item_removals: Optional[pulumi.Input[Union[_builtins.str, RecordPropertyAndItemRemovals]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxDatabaseName")
    def adx_database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @adx_database_name.setter
    def adx_database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxEndpointUri")
    def adx_endpoint_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @adx_endpoint_uri.setter
    def adx_endpoint_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxResourceId")
    def adx_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @adx_resource_id.setter
    def adx_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubEndpointUri")
    def event_hub_endpoint_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_hub_endpoint_uri.setter
    def event_hub_endpoint_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubEntityPath")
    def event_hub_entity_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_hub_entity_path.setter
    def event_hub_entity_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubNamespaceResourceId")
    def event_hub_namespace_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_hub_namespace_resource_id.setter
    def event_hub_namespace_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxRelationshipLifecycleEventsTableName")
    def adx_relationship_lifecycle_events_table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adx_relationship_lifecycle_events_table_name.setter
    def adx_relationship_lifecycle_events_table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxTableName")
    def adx_table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adx_table_name.setter
    def adx_table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxTwinLifecycleEventsTableName")
    def adx_twin_lifecycle_events_table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adx_twin_lifecycle_events_table_name.setter
    def adx_twin_lifecycle_events_table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubConsumerGroup")
    def event_hub_consumer_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_hub_consumer_group.setter
    def event_hub_consumer_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedIdentityReferenceArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedIdentityReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordPropertyAndItemRemovals")
    def record_property_and_item_removals(self) -> Optional[pulumi.Input[Union[_builtins.str, RecordPropertyAndItemRemovals]]]:
        
        ...
    
    @record_property_and_item_removals.setter
    def record_property_and_item_removals(self, value: Optional[pulumi.Input[Union[_builtins.str, RecordPropertyAndItemRemovals]]]): # -> None:
        ...
    


class ConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    description: pulumi.Input[_builtins.str]
    status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]
    actions_required: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionPropertiesPrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]], actions_required: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionPropertiesArgsDict(TypedDict):
    
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    private_link_service_connection_state: NotRequired[pulumi.Input[ConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict]]


@pulumi.input_type
class ConnectionPropertiesArgs:
    def __init__(__self__, *, group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_link_service_connection_state: Optional[pulumi.Input[ConnectionPropertiesPrivateLinkServiceConnectionStateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input[ConnectionPropertiesPrivateLinkServiceConnectionStateArgs]]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input[ConnectionPropertiesPrivateLinkServiceConnectionStateArgs]]): # -> None:
        ...
    


class DigitalTwinsIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, DigitalTwinsIdentityType]]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DigitalTwinsIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, DigitalTwinsIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, DigitalTwinsIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, DigitalTwinsIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EventGridArgsDict(TypedDict):
    
    access_key1: pulumi.Input[_builtins.str]
    endpoint_type: pulumi.Input[_builtins.str]
    topic_endpoint: pulumi.Input[_builtins.str]
    access_key2: NotRequired[pulumi.Input[_builtins.str]]
    authentication_type: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    dead_letter_secret: NotRequired[pulumi.Input[_builtins.str]]
    dead_letter_uri: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[ManagedIdentityReferenceArgsDict]]


@pulumi.input_type
class EventGridArgs:
    def __init__(__self__, *, access_key1: pulumi.Input[_builtins.str], endpoint_type: pulumi.Input[_builtins.str], topic_endpoint: pulumi.Input[_builtins.str], access_key2: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., dead_letter_secret: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_uri: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedIdentityReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey1")
    def access_key1(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_key1.setter
    def access_key1(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicEndpoint")
    def topic_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_endpoint.setter
    def topic_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey2")
    def access_key2(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_key2.setter
    def access_key2(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_secret.setter
    def dead_letter_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_uri.setter
    def dead_letter_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedIdentityReferenceArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedIdentityReferenceArgs]]): # -> None:
        ...
    


class EventHubArgsDict(TypedDict):
    
    endpoint_type: pulumi.Input[_builtins.str]
    authentication_type: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    connection_string_primary_key: NotRequired[pulumi.Input[_builtins.str]]
    connection_string_secondary_key: NotRequired[pulumi.Input[_builtins.str]]
    dead_letter_secret: NotRequired[pulumi.Input[_builtins.str]]
    dead_letter_uri: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]
    entity_path: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[ManagedIdentityReferenceArgsDict]]


@pulumi.input_type
class EventHubArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], authentication_type: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., connection_string_primary_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_string_secondary_key: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_secret: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_uri: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ..., entity_path: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedIdentityReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStringPrimaryKey")
    def connection_string_primary_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string_primary_key.setter
    def connection_string_primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStringSecondaryKey")
    def connection_string_secondary_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string_secondary_key.setter
    def connection_string_secondary_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_secret.setter
    def dead_letter_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_uri.setter
    def dead_letter_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entity_path.setter
    def entity_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedIdentityReferenceArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedIdentityReferenceArgs]]): # -> None:
        ...
    


class ManagedIdentityReferenceArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedIdentityReferenceArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ..., user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateEndpointConnectionArgsDict(TypedDict):
    
    properties: pulumi.Input[ConnectionPropertiesArgsDict]


@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *, properties: pulumi.Input[ConnectionPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ConnectionPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[ConnectionPropertiesArgs]): # -> None:
        ...
    


class ServiceBusArgsDict(TypedDict):
    
    endpoint_type: pulumi.Input[_builtins.str]
    authentication_type: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    dead_letter_secret: NotRequired[pulumi.Input[_builtins.str]]
    dead_letter_uri: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]
    entity_path: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[ManagedIdentityReferenceArgsDict]]
    primary_connection_string: NotRequired[pulumi.Input[_builtins.str]]
    secondary_connection_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceBusArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], authentication_type: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., dead_letter_secret: Optional[pulumi.Input[_builtins.str]] = ..., dead_letter_uri: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ..., entity_path: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedIdentityReferenceArgs]] = ..., primary_connection_string: Optional[pulumi.Input[_builtins.str]] = ..., secondary_connection_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterSecret")
    def dead_letter_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_secret.setter
    def dead_letter_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterUri")
    def dead_letter_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_uri.setter
    def dead_letter_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entity_path.setter
    def entity_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedIdentityReferenceArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedIdentityReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_connection_string.setter
    def primary_connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_connection_string.setter
    def secondary_connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


