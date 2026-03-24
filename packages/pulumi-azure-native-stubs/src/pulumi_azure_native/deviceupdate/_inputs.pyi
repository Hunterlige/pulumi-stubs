

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DiagnosticStoragePropertiesArgs', 'DiagnosticStoragePropertiesArgsDict', 'EncryptionArgs', 'EncryptionArgsDict', 'GroupConnectivityInformationArgs', 'GroupConnectivityInformationArgsDict', 'IotHubSettingsArgs', 'IotHubSettingsArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'PrivateLinkServiceConnectionArgs', 'PrivateLinkServiceConnectionArgsDict', 'PrivateLinkServiceProxyArgs', 'PrivateLinkServiceProxyArgsDict', 'RemotePrivateEndpointArgs', 'RemotePrivateEndpointArgsDict']
class DiagnosticStoragePropertiesArgsDict(TypedDict):
    
    authentication_type: pulumi.Input[Union[_builtins.str, AuthenticationType]]
    resource_id: pulumi.Input[_builtins.str]
    connection_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiagnosticStoragePropertiesArgs:
    def __init__(__self__, *, authentication_type: pulumi.Input[Union[_builtins.str, AuthenticationType]], resource_id: pulumi.Input[_builtins.str], connection_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[Union[_builtins.str, AuthenticationType]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[Union[_builtins.str, AuthenticationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionArgsDict(TypedDict):
    
    key_vault_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *, key_vault_key_uri: Optional[pulumi.Input[_builtins.str]] = ..., user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_key_uri.setter
    def key_vault_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GroupConnectivityInformationArgsDict(TypedDict):
    
    customer_visible_fqdns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    private_link_service_arm_region: NotRequired[pulumi.Input[_builtins.str]]
    redirect_map_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GroupConnectivityInformationArgs:
    def __init__(__self__, *, customer_visible_fqdns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., private_link_service_arm_region: Optional[pulumi.Input[_builtins.str]] = ..., redirect_map_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerVisibleFqdns")
    def customer_visible_fqdns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @customer_visible_fqdns.setter
    def customer_visible_fqdns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceArmRegion")
    def private_link_service_arm_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_service_arm_region.setter
    def private_link_service_arm_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectMapId")
    def redirect_map_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_map_id.setter
    def redirect_map_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IotHubSettingsArgsDict(TypedDict):
    
    resource_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class IotHubSettingsArgs:
    def __init__(__self__, *, resource_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrivateEndpointConnectionArgsDict(TypedDict):
    
    private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *, private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgs], group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input[PrivateLinkServiceConnectionStateArgs]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input[PrivateLinkServiceConnectionStateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionArgsDict(TypedDict):
    
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    request_message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateLinkServiceConnectionArgs:
    def __init__(__self__, *, group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., request_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceProxyArgsDict(TypedDict):
    
    group_connectivity_information: NotRequired[pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgsDict]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    remote_private_link_service_connection_state: NotRequired[pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]]


@pulumi.input_type
class PrivateLinkServiceProxyArgs:
    def __init__(__self__, *, group_connectivity_information: Optional[pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., remote_private_link_service_connection_state: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConnectivityInformation")
    def group_connectivity_information(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]]:
        
        ...
    
    @group_connectivity_information.setter
    def group_connectivity_information(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupConnectivityInformationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePrivateLinkServiceConnectionState")
    def remote_private_link_service_connection_state(self) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]:
        
        ...
    
    @remote_private_link_service_connection_state.setter
    def remote_private_link_service_connection_state(self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]): # -> None:
        ...
    


class RemotePrivateEndpointArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    immutable_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    immutable_subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    manual_private_link_service_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgsDict]]]]
    private_link_service_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgsDict]]]]
    private_link_service_proxies: NotRequired[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgsDict]]]]
    vnet_traffic_tag: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RemotePrivateEndpointArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., immutable_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., immutable_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]] = ..., private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]] = ..., private_link_service_proxies: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]] = ..., vnet_traffic_tag: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableResourceId")
    def immutable_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @immutable_resource_id.setter
    def immutable_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableSubscriptionId")
    def immutable_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @immutable_subscription_id.setter
    def immutable_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]:
        
        ...
    
    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]:
        
        ...
    
    @private_link_service_connections.setter
    def private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceProxies")
    def private_link_service_proxies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]]:
        
        ...
    
    @private_link_service_proxies.setter
    def private_link_service_proxies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceProxyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetTrafficTag")
    def vnet_traffic_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vnet_traffic_tag.setter
    def vnet_traffic_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


