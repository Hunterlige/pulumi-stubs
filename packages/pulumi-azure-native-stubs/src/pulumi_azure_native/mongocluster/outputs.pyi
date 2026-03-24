

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AdministratorPropertiesResponse', 'BackupPropertiesResponse', 'ComputePropertiesResponse', 'ConnectionStringResponse', 'DatabaseRoleResponse', 'EntraIdentityProviderPropertiesResponse', 'EntraIdentityProviderResponse', 'FirewallRulePropertiesResponse', 'HighAvailabilityPropertiesResponse', 'MongoClusterPropertiesResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ReplicationPropertiesResponse', 'ShardingPropertiesResponse', 'StoragePropertiesResponse', 'SystemDataResponse', 'UserPropertiesResponse']
@pulumi.output_type
class AdministratorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, earliest_restore_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ComputePropertiesResponse(dict):
    
    def __init__(__self__, *, tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionStringResponse(dict):
    
    def __init__(__self__, *, connection_string: _builtins.str, description: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseRoleResponse(dict):
    
    def __init__(__self__, *, db: _builtins.str, role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EntraIdentityProviderPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EntraIdentityProviderResponse(dict):
    
    def __init__(__self__, *, properties: outputs.EntraIdentityProviderPropertiesResponse, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.EntraIdentityProviderPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallRulePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_ip_address: _builtins.str, provisioning_state: _builtins.str, start_ip_address: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HighAvailabilityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMode")
    def target_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoClusterPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_status: _builtins.str, connection_string: _builtins.str, infrastructure_version: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, replica: outputs.ReplicationPropertiesResponse, administrator: Optional[outputs.AdministratorPropertiesResponse] = ..., backup: Optional[outputs.BackupPropertiesResponse] = ..., compute: Optional[outputs.ComputePropertiesResponse] = ..., high_availability: Optional[outputs.HighAvailabilityPropertiesResponse] = ..., preview_features: Optional[Sequence[_builtins.str]] = ..., public_network_access: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., sharding: Optional[outputs.ShardingPropertiesResponse] = ..., storage: Optional[outputs.StoragePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureVersion")
    def infrastructure_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replica(self) -> outputs.ReplicationPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrator(self) -> Optional[outputs.AdministratorPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[outputs.BackupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compute(self) -> Optional[outputs.ComputePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional[outputs.HighAvailabilityPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewFeatures")
    def preview_features(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sharding(self) -> Optional[outputs.ShardingPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[outputs.StoragePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReplicationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replication_state: _builtins.str, role: _builtins.str, source_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ShardingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, shard_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class StoragePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, size_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, identity_provider: Optional[outputs.EntraIdentityProviderResponse] = ..., roles: Optional[Sequence[outputs.DatabaseRoleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[outputs.EntraIdentityProviderResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[outputs.DatabaseRoleResponse]]:
        
        ...
    


