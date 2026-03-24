

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthConfigResponse', 'BackupResponse', 'ClusterResponse', 'DataEncryptionResponse', 'DatabaseMigrationStateResponse', 'DbLevelValidationStatusResponse', 'DbServerMetadataResponse', 'HighAvailabilityResponse', 'IdentityPropertiesResponse', 'MaintenanceWindowResponse', 'MigrationStatusResponse', 'MigrationSubstateDetailsResponse', 'NetworkResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointPropertyResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ReplicaResponse', 'ResourceIdentityResponse', 'ServerGroupClusterAuthConfigResponse', 'ServerGroupClusterDataEncryptionResponse', 'ServerGroupClusterMaintenanceWindowResponse', 'ServerNameItemResponse', 'ServerPrivateEndpointConnectionPropertiesResponse', 'ServerPrivateEndpointConnectionResponse', ..., 'ServerSkuResponse', 'SimplePrivateEndpointConnectionResponse', 'SingleServerSkuResponse', 'SkuResponse', 'StorageProfileResponse', 'StorageResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', 'UserAssignedIdentityResponseV1', 'UserIdentityResponse', 'ValidationDetailsResponse', 'ValidationMessageResponse', 'ValidationSummaryItemResponse']
@pulumi.output_type
class AuthConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_directory_auth: Optional[_builtins.str] = ..., password_auth: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryAuth")
    def active_directory_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordAuth")
    def password_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, earliest_restore_date: _builtins.str, backup_retention_days: Optional[_builtins.int] = ..., geo_redundant_backup: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_size: Optional[_builtins.int] = ..., default_database_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatabaseName")
    def default_database_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataEncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, geo_backup_encryption_key_status: _builtins.str, primary_encryption_key_status: _builtins.str, geo_backup_key_uri: Optional[_builtins.str] = ..., geo_backup_user_assigned_identity_id: Optional[_builtins.str] = ..., primary_key_uri: Optional[_builtins.str] = ..., primary_user_assigned_identity_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoBackupEncryptionKeyStatus")
    def geo_backup_encryption_key_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryEncryptionKeyStatus")
    def primary_encryption_key_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoBackupKeyURI")
    def geo_backup_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoBackupUserAssignedIdentityId")
    def geo_backup_user_assigned_identity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKeyURI")
    def primary_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseMigrationStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_changes: Optional[_builtins.int] = ..., cdc_delete_counter: Optional[_builtins.int] = ..., cdc_insert_counter: Optional[_builtins.int] = ..., cdc_update_counter: Optional[_builtins.int] = ..., database_name: Optional[_builtins.str] = ..., ended_on: Optional[_builtins.str] = ..., full_load_completed_tables: Optional[_builtins.int] = ..., full_load_errored_tables: Optional[_builtins.int] = ..., full_load_loading_tables: Optional[_builtins.int] = ..., full_load_queued_tables: Optional[_builtins.int] = ..., incoming_changes: Optional[_builtins.int] = ..., latency: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ..., migration_operation: Optional[_builtins.str] = ..., migration_state: Optional[_builtins.str] = ..., started_on: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedChanges")
    def applied_changes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadCompletedTables")
    def full_load_completed_tables(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErroredTables")
    def full_load_errored_tables(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadLoadingTables")
    def full_load_loading_tables(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadQueuedTables")
    def full_load_queued_tables(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingChanges")
    def incoming_changes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperation")
    def migration_operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DbLevelValidationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: Optional[_builtins.str] = ..., ended_on: Optional[_builtins.str] = ..., started_on: Optional[_builtins.str] = ..., summary: Optional[Sequence[outputs.ValidationSummaryItemResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[Sequence[outputs.ValidationSummaryItemResponse]]:
        
        ...
    


@pulumi.output_type
class DbServerMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, sku: Optional[outputs.ServerSkuResponse] = ..., storage_mb: Optional[_builtins.int] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ServerSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMb")
    def storage_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HighAvailabilityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: _builtins.str, mode: Optional[_builtins.str] = ..., standby_availability_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponseV1]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponseV1]]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_window: Optional[_builtins.str] = ..., day_of_week: Optional[_builtins.int] = ..., start_hour: Optional[_builtins.int] = ..., start_minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MigrationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, current_sub_state_details: outputs.MigrationSubstateDetailsResponse, error: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentSubStateDetails")
    def current_sub_state_details(self) -> outputs.MigrationSubstateDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrationSubstateDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, current_sub_state: _builtins.str, db_details: Optional[Mapping[str, outputs.DatabaseMigrationStateResponse]] = ..., validation_details: Optional[outputs.ValidationDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentSubState")
    def current_sub_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbDetails")
    def db_details(self) -> Optional[Mapping[str, outputs.DatabaseMigrationStateResponse]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationDetails")
    def validation_details(self) -> Optional[outputs.ValidationDetailsResponse]:
        
        ...
    


@pulumi.output_type
class NetworkResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delegated_subnet_resource_id: Optional[_builtins.str] = ..., private_dns_zone_arm_resource_id: Optional[_builtins.str] = ..., public_network_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedSubnetResourceId")
    def delegated_subnet_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneArmResourceId")
    def private_dns_zone_arm_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
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
class PrivateEndpointPropertyResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
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
class ReplicaResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity: _builtins.int, replication_state: _builtins.str, role: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerGroupClusterAuthConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_directory_auth: Optional[_builtins.str] = ..., password_auth: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryAuth")
    def active_directory_auth(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordAuth")
    def password_auth(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ServerGroupClusterDataEncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primary_key_uri: Optional[_builtins.str] = ..., primary_user_assigned_identity_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKeyUri")
    def primary_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ServerGroupClusterMaintenanceWindowResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_window: Optional[_builtins.str] = ..., day_of_week: Optional[_builtins.int] = ..., start_hour: Optional[_builtins.int] = ..., start_minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServerNameItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fully_qualified_domain_name: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerPrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointPropertyResponse] = ..., private_link_service_connection_state: Optional[outputs.ServerPrivateLinkServiceConnectionStatePropertyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.ServerPrivateLinkServiceConnectionStatePropertyResponse]:
        
        ...
    


@pulumi.output_type
class ServerPrivateEndpointConnectionResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, properties: outputs.ServerPrivateEndpointConnectionPropertiesResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ServerPrivateEndpointConnectionPropertiesResponse:
        
        ...
    


@pulumi.output_type
class ServerPrivateLinkServiceConnectionStatePropertyResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerSkuResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SimplePrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointPropertyResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class SingleServerSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StorageProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_retention_days: Optional[_builtins.int] = ..., geo_redundant_backup: Optional[_builtins.str] = ..., storage_autogrow: Optional[_builtins.str] = ..., storage_mb: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAutogrow")
    def storage_autogrow(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class StorageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_grow: Optional[_builtins.str] = ..., iops: Optional[_builtins.int] = ..., storage_size_gb: Optional[_builtins.int] = ..., throughput: Optional[_builtins.int] = ..., tier: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoGrow")
    def auto_grow(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeGB")
    def storage_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
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
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tenant_id: _builtins.str, type: _builtins.str, principal_id: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ValidationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, db_level_validation_details: Optional[Sequence[outputs.DbLevelValidationStatusResponse]] = ..., server_level_validation_details: Optional[Sequence[outputs.ValidationSummaryItemResponse]] = ..., status: Optional[_builtins.str] = ..., validation_end_time_in_utc: Optional[_builtins.str] = ..., validation_start_time_in_utc: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbLevelValidationDetails")
    def db_level_validation_details(self) -> Optional[Sequence[outputs.DbLevelValidationStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverLevelValidationDetails")
    def server_level_validation_details(self) -> Optional[Sequence[outputs.ValidationSummaryItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationEndTimeInUtc")
    def validation_end_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationStartTimeInUtc")
    def validation_start_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ValidationMessageResponse(dict):
    
    def __init__(__self__, *, message: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ValidationSummaryItemResponse(dict):
    
    def __init__(__self__, *, messages: Optional[Sequence[outputs.ValidationMessageResponse]] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[Sequence[outputs.ValidationMessageResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


