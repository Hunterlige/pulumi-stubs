import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ManagedServiceIdentityResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "RedisAccessKeysResponse",
    "RedisCommonPropertiesRedisConfigurationResponse",
    "RedisInstanceDetailsResponse",
    "RedisLinkedServerResponse",
    "ScheduleEntryResponse",
    "SkuResponse",
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
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
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

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
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RedisAccessKeysResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, primary_key: _builtins.str, secondary_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> _builtins.str: ...

@pulumi.output_type
class RedisCommonPropertiesRedisConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maxclients: _builtins.str,
        preferred_data_archive_auth_method: _builtins.str,
        zonal_configuration: _builtins.str,
        aad_enabled: Optional[_builtins.str] = ...,
        aof_backup_enabled: Optional[_builtins.str] = ...,
        aof_storage_connection_string0: Optional[_builtins.str] = ...,
        aof_storage_connection_string1: Optional[_builtins.str] = ...,
        authnotrequired: Optional[_builtins.str] = ...,
        maxfragmentationmemory_reserved: Optional[_builtins.str] = ...,
        maxmemory_delta: Optional[_builtins.str] = ...,
        maxmemory_policy: Optional[_builtins.str] = ...,
        maxmemory_reserved: Optional[_builtins.str] = ...,
        notify_keyspace_events: Optional[_builtins.str] = ...,
        preferred_data_persistence_auth_method: Optional[_builtins.str] = ...,
        rdb_backup_enabled: Optional[_builtins.str] = ...,
        rdb_backup_frequency: Optional[_builtins.str] = ...,
        rdb_backup_max_snapshot_count: Optional[_builtins.str] = ...,
        rdb_storage_connection_string: Optional[_builtins.str] = ...,
        storage_subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxclients(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredDataArchiveAuthMethod")
    def preferred_data_archive_auth_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zonalConfiguration")
    def zonal_configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="aadEnabled")
    def aad_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aofBackupEnabled")
    def aof_backup_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aofStorageConnectionString0")
    def aof_storage_connection_string0(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aofStorageConnectionString1")
    def aof_storage_connection_string1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def authnotrequired(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxfragmentationmemoryReserved")
    def maxfragmentationmemory_reserved(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxmemoryDelta")
    def maxmemory_delta(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxmemoryPolicy")
    def maxmemory_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxmemoryReserved")
    def maxmemory_reserved(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notifyKeyspaceEvents")
    def notify_keyspace_events(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredDataPersistenceAuthMethod")
    def preferred_data_persistence_auth_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbBackupEnabled")
    def rdb_backup_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbBackupFrequency")
    def rdb_backup_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbBackupMaxSnapshotCount")
    def rdb_backup_max_snapshot_count(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbStorageConnectionString")
    def rdb_storage_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageSubscriptionId")
    def storage_subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RedisInstanceDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_master: _builtins.bool,
        is_primary: _builtins.bool,
        non_ssl_port: _builtins.int,
        shard_id: _builtins.int,
        ssl_port: _builtins.int,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isMaster")
    def is_master(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="nonSslPort")
    def non_ssl_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shardId")
    def shard_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sslPort")
    def ssl_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class RedisLinkedServerResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduleEntryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        start_hour_utc: _builtins.int,
        maintenance_window: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startHourUtc")
    def start_hour_utc(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__, *, capacity: _builtins.int, family: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

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
