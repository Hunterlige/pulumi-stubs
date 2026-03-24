

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AdministratorPropertiesArgs', 'AdministratorPropertiesArgsDict', 'ComputePropertiesArgs', 'ComputePropertiesArgsDict', 'DatabaseRoleArgs', 'DatabaseRoleArgsDict', 'EntraIdentityProviderPropertiesArgs', 'EntraIdentityProviderPropertiesArgsDict', 'EntraIdentityProviderArgs', 'EntraIdentityProviderArgsDict', 'FirewallRulePropertiesArgs', 'FirewallRulePropertiesArgsDict', 'HighAvailabilityPropertiesArgs', 'HighAvailabilityPropertiesArgsDict', 'MongoClusterPropertiesArgs', 'MongoClusterPropertiesArgsDict', 'MongoClusterReplicaParametersArgs', 'MongoClusterReplicaParametersArgsDict', 'MongoClusterRestoreParametersArgs', 'MongoClusterRestoreParametersArgsDict', 'PrivateEndpointConnectionPropertiesArgs', 'PrivateEndpointConnectionPropertiesArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'ShardingPropertiesArgs', 'ShardingPropertiesArgsDict', 'StoragePropertiesArgs', 'StoragePropertiesArgsDict', 'UserPropertiesArgs', 'UserPropertiesArgsDict']
class AdministratorPropertiesArgsDict(TypedDict):
    
    password: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AdministratorPropertiesArgs:
    def __init__(__self__, *, password: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ComputePropertiesArgsDict(TypedDict):
    
    tier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ComputePropertiesArgs:
    def __init__(__self__, *, tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseRoleArgsDict(TypedDict):
    
    db: pulumi.Input[_builtins.str]
    role: pulumi.Input[Union[_builtins.str, UserRole]]


@pulumi.input_type
class DatabaseRoleArgs:
    def __init__(__self__, *, db: pulumi.Input[_builtins.str], role: pulumi.Input[Union[_builtins.str, UserRole]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db.setter
    def db(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[Union[_builtins.str, UserRole]]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[Union[_builtins.str, UserRole]]): # -> None:
        ...
    


class EntraIdentityProviderPropertiesArgsDict(TypedDict):
    
    principal_type: pulumi.Input[Union[_builtins.str, EntraPrincipalType]]


@pulumi.input_type
class EntraIdentityProviderPropertiesArgs:
    def __init__(__self__, *, principal_type: pulumi.Input[Union[_builtins.str, EntraPrincipalType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[Union[_builtins.str, EntraPrincipalType]]:
        
        ...
    
    @principal_type.setter
    def principal_type(self, value: pulumi.Input[Union[_builtins.str, EntraPrincipalType]]): # -> None:
        ...
    


class EntraIdentityProviderArgsDict(TypedDict):
    
    properties: pulumi.Input[EntraIdentityProviderPropertiesArgsDict]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class EntraIdentityProviderArgs:
    def __init__(__self__, *, properties: pulumi.Input[EntraIdentityProviderPropertiesArgs], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[EntraIdentityProviderPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[EntraIdentityProviderPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirewallRulePropertiesArgsDict(TypedDict):
    
    end_ip_address: pulumi.Input[_builtins.str]
    start_ip_address: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirewallRulePropertiesArgs:
    def __init__(__self__, *, end_ip_address: pulumi.Input[_builtins.str], start_ip_address: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class HighAvailabilityPropertiesArgsDict(TypedDict):
    
    target_mode: NotRequired[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]


@pulumi.input_type
class HighAvailabilityPropertiesArgs:
    def __init__(__self__, *, target_mode: Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMode")
    def target_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]:
        
        ...
    
    @target_mode.setter
    def target_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]): # -> None:
        ...
    


class MongoClusterPropertiesArgsDict(TypedDict):
    
    administrator: NotRequired[pulumi.Input[AdministratorPropertiesArgsDict]]
    compute: NotRequired[pulumi.Input[ComputePropertiesArgsDict]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    high_availability: NotRequired[pulumi.Input[HighAvailabilityPropertiesArgsDict]]
    preview_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreviewFeature]]]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    replica_parameters: NotRequired[pulumi.Input[MongoClusterReplicaParametersArgsDict]]
    restore_parameters: NotRequired[pulumi.Input[MongoClusterRestoreParametersArgsDict]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    sharding: NotRequired[pulumi.Input[ShardingPropertiesArgsDict]]
    storage: NotRequired[pulumi.Input[StoragePropertiesArgsDict]]


@pulumi.input_type
class MongoClusterPropertiesArgs:
    def __init__(__self__, *, administrator: Optional[pulumi.Input[AdministratorPropertiesArgs]] = ..., compute: Optional[pulumi.Input[ComputePropertiesArgs]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., high_availability: Optional[pulumi.Input[HighAvailabilityPropertiesArgs]] = ..., preview_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreviewFeature]]]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., replica_parameters: Optional[pulumi.Input[MongoClusterReplicaParametersArgs]] = ..., restore_parameters: Optional[pulumi.Input[MongoClusterRestoreParametersArgs]] = ..., server_version: Optional[pulumi.Input[_builtins.str]] = ..., sharding: Optional[pulumi.Input[ShardingPropertiesArgs]] = ..., storage: Optional[pulumi.Input[StoragePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrator(self) -> Optional[pulumi.Input[AdministratorPropertiesArgs]]:
        
        ...
    
    @administrator.setter
    def administrator(self, value: Optional[pulumi.Input[AdministratorPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compute(self) -> Optional[pulumi.Input[ComputePropertiesArgs]]:
        
        ...
    
    @compute.setter
    def compute(self, value: Optional[pulumi.Input[ComputePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional[pulumi.Input[HighAvailabilityPropertiesArgs]]:
        
        ...
    
    @high_availability.setter
    def high_availability(self, value: Optional[pulumi.Input[HighAvailabilityPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewFeatures")
    def preview_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreviewFeature]]]]]:
        
        ...
    
    @preview_features.setter
    def preview_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreviewFeature]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaParameters")
    def replica_parameters(self) -> Optional[pulumi.Input[MongoClusterReplicaParametersArgs]]:
        
        ...
    
    @replica_parameters.setter
    def replica_parameters(self, value: Optional[pulumi.Input[MongoClusterReplicaParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[MongoClusterRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[MongoClusterRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sharding(self) -> Optional[pulumi.Input[ShardingPropertiesArgs]]:
        
        ...
    
    @sharding.setter
    def sharding(self, value: Optional[pulumi.Input[ShardingPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[StoragePropertiesArgs]]:
        
        ...
    
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[StoragePropertiesArgs]]): # -> None:
        ...
    


class MongoClusterReplicaParametersArgsDict(TypedDict):
    
    source_location: pulumi.Input[_builtins.str]
    source_resource_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class MongoClusterReplicaParametersArgs:
    def __init__(__self__, *, source_location: pulumi.Input[_builtins.str], source_resource_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_location.setter
    def source_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_resource_id.setter
    def source_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MongoClusterRestoreParametersArgsDict(TypedDict):
    
    point_in_time_utc: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MongoClusterRestoreParametersArgs:
    def __init__(__self__, *, point_in_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @point_in_time_utc.setter
    def point_in_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    
    private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]


@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(__self__, *, private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input[PrivateLinkServiceConnectionStateArgs]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input[PrivateLinkServiceConnectionStateArgs]): # -> None:
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
    


class ShardingPropertiesArgsDict(TypedDict):
    
    shard_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ShardingPropertiesArgs:
    def __init__(__self__, *, shard_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class StoragePropertiesArgsDict(TypedDict):
    
    size_gb: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StoragePropertiesArgs:
    def __init__(__self__, *, size_gb: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class UserPropertiesArgsDict(TypedDict):
    
    identity_provider: NotRequired[pulumi.Input[EntraIdentityProviderArgsDict]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseRoleArgsDict]]]]


@pulumi.input_type
class UserPropertiesArgs:
    def __init__(__self__, *, identity_provider: Optional[pulumi.Input[EntraIdentityProviderArgs]] = ..., roles: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRoleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[pulumi.Input[EntraIdentityProviderArgs]]:
        
        ...
    
    @identity_provider.setter
    def identity_provider(self, value: Optional[pulumi.Input[EntraIdentityProviderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRoleArgs]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRoleArgs]]]]): # -> None:
        ...
    


