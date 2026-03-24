

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
__all__ = ['AccountKeyMetadataResponse', 'AnalyticalStorageConfigurationResponse', 'ApiPropertiesResponse', 'AuthenticationMethodLdapPropertiesResponse', 'AutoscaleSettingsResponse', 'BackupPolicyMigrationStateResponse', 'CapabilityResponse', 'CapacityResponse', 'CassandraErrorResponse', 'CassandraKeyspaceGetPropertiesResponseOptions', 'CassandraKeyspaceGetPropertiesResponseResource', 'CassandraPartitionKeyResponse', 'CassandraSchemaResponse', 'CassandraTableGetPropertiesResponseOptions', 'CassandraTableGetPropertiesResponseResource', 'CassandraViewGetPropertiesResponseOptions', 'CassandraViewGetPropertiesResponseResource', 'CertificateResponse', 'ClientEncryptionIncludedPathResponse', 'ClientEncryptionPolicyResponse', 'ClusterKeyResponse', 'ClusterResourceResponseProperties', 'ColumnResponse', 'CompositePathResponse', 'ComputedPropertyResponse', 'ConflictResolutionPolicyResponse', 'ConnectionStringResponse', 'ConsistencyPolicyResponse', 'ContainerPartitionKeyResponse', 'ContainerPartitionKeyResponseV1', 'ContainerPartitionKeyResponseV2', 'ContinuousModeBackupPolicyResponse', 'ContinuousModePropertiesResponse', 'CorsPolicyResponse', 'DataCenterResourceResponseProperties', 'DataTransferRegionalServiceResourceResponse', 'DataTransferServiceResourcePropertiesResponse', 'DatabaseAccountConnectionStringResponse', 'DatabaseAccountKeysMetadataResponse', 'DatabaseRestoreResourceResponse', 'ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'ExcludedPathResponse', 'FailoverPolicyResponse', ..., ..., 'FullTextIndexPathResponse', 'FullTextPathResponse', 'FullTextPolicyResponse', 'GarnetClusterResourceResponseEndPoints', 'GarnetClusterResourceResponseProperties', 'GraphAPIComputeRegionalServiceResourceResponse', 'GraphAPIComputeServiceResourcePropertiesResponse', 'GraphResourceGetPropertiesResponseOptions', 'GraphResourceGetPropertiesResponseResource', 'GremlinDatabaseGetPropertiesResponseOptions', 'GremlinDatabaseGetPropertiesResponseResource', 'GremlinDatabaseRestoreResourceResponse', 'GremlinGraphGetPropertiesResponseOptions', 'GremlinGraphGetPropertiesResponseResource', 'IncludedPathResponse', 'IndexesResponse', 'IndexingPolicyResponse', 'IndexingPolicyResponseV1', 'IndexingPolicyResponseV2', 'IpAddressOrRangeResponse', 'LocationResponse', 'ManagedCassandraManagedServiceIdentityResponse', 'ManagedServiceIdentityResponse', ..., ..., ..., 'MongoDBCollectionGetPropertiesResponseOptions', 'MongoDBCollectionGetPropertiesResponseResource', 'MongoDBDatabaseGetPropertiesResponseOptions', 'MongoDBDatabaseGetPropertiesResponseResource', 'MongoIndexKeysResponse', 'MongoIndexOptionsResponse', 'MongoIndexResponse', 'NodeGroupSpecResponse', 'PeriodicModeBackupPolicyResponse', 'PeriodicModePropertiesResponse', 'PermissionResponse', 'PermissionResponseV1', 'PrivateEndpointConnectionResponse', 'PrivateEndpointPropertyResponse', 'PrivateLinkServiceConnectionStatePropertyResponse', 'PrivilegeResponse', 'PrivilegeResponseResource', 'ResourceRestoreParametersResponse', 'RestoreParametersResponse', 'RoleResponse', 'SeedNodeResponse', 'SpatialSpecResponse', 'SqlContainerGetPropertiesResponseOptions', 'SqlContainerGetPropertiesResponseResource', 'SqlDatabaseGetPropertiesResponseOptions', 'SqlDatabaseGetPropertiesResponseResource', 'SqlDedicatedGatewayRegionalServiceResourceResponse', ..., 'SqlStoredProcedureGetPropertiesResponseResource', 'SqlTriggerGetPropertiesResponseResource', ..., 'SystemDataResponse', 'TableGetPropertiesResponseOptions', 'TableGetPropertiesResponseResource', 'UniqueKeyPolicyResponse', 'UniqueKeyResponse', 'VectorEmbeddingPolicyResponse', 'VectorEmbeddingResponse', 'VectorIndexResponse', 'VirtualNetworkRuleResponse']
@pulumi.output_type
class AccountKeyMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generation_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationTime")
    def generation_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AnalyticalStorageConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthenticationMethodLdapPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_timeout_in_ms: Optional[_builtins.int] = ..., search_base_distinguished_name: Optional[_builtins.str] = ..., search_filter_template: Optional[_builtins.str] = ..., server_certificates: Optional[Sequence[outputs.CertificateResponse]] = ..., server_hostname: Optional[_builtins.str] = ..., server_port: Optional[_builtins.int] = ..., service_user_distinguished_name: Optional[_builtins.str] = ..., service_user_password: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeoutInMs")
    def connection_timeout_in_ms(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchBaseDistinguishedName")
    def search_base_distinguished_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchFilterTemplate")
    def search_filter_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(self) -> Optional[Sequence[outputs.CertificateResponse]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserDistinguishedName")
    def service_user_distinguished_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserPassword")
    def service_user_password(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoscaleSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BackupPolicyMigrationStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_time: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., target_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapabilityResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapacityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, total_throughput_limit: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalThroughputLimit")
    def total_throughput_limit(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CassandraErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_error_info: Optional[_builtins.str] = ..., code: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalErrorInfo")
    def additional_error_info(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CassandraKeyspaceGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CassandraKeyspaceGetPropertiesResponseResource(dict):
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class CassandraPartitionKeyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CassandraSchemaResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_keys: Optional[Sequence[outputs.ClusterKeyResponse]] = ..., columns: Optional[Sequence[outputs.ColumnResponse]] = ..., partition_keys: Optional[Sequence[outputs.CassandraPartitionKeyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterKeys")
    def cluster_keys(self) -> Optional[Sequence[outputs.ClusterKeyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[outputs.ColumnResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[Sequence[outputs.CassandraPartitionKeyResponse]]:
        
        ...
    


@pulumi.output_type
class CassandraTableGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CassandraTableGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, analytical_storage_ttl: Optional[_builtins.int] = ..., default_ttl: Optional[_builtins.int] = ..., schema: Optional[outputs.CassandraSchemaResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[outputs.CassandraSchemaResponse]:
        
        ...
    


@pulumi.output_type
class CassandraViewGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CassandraViewGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, view_definition: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewDefinition")
    def view_definition(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CertificateResponse(dict):
    def __init__(__self__, *, pem: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pem(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClientEncryptionIncludedPathResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_encryption_key_id: _builtins.str, encryption_algorithm: _builtins.str, encryption_type: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientEncryptionKeyId")
    def client_encryption_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClientEncryptionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, included_paths: Sequence[outputs.ClientEncryptionIncludedPathResponse], policy_format_version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Sequence[outputs.ClientEncryptionIncludedPathResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFormatVersion")
    def policy_format_version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ClusterKeyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., order_by: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterResourceResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gossip_certificates: Sequence[outputs.CertificateResponse], private_link_resource_id: _builtins.str, seed_nodes: Sequence[outputs.SeedNodeResponse], authentication_method: Optional[_builtins.str] = ..., azure_connection_method: Optional[_builtins.str] = ..., cassandra_audit_logging_enabled: Optional[_builtins.bool] = ..., cassandra_version: Optional[_builtins.str] = ..., client_certificates: Optional[Sequence[outputs.CertificateResponse]] = ..., cluster_name_override: Optional[_builtins.str] = ..., deallocated: Optional[_builtins.bool] = ..., delegated_management_subnet_id: Optional[_builtins.str] = ..., external_gossip_certificates: Optional[Sequence[outputs.CertificateResponse]] = ..., external_seed_nodes: Optional[Sequence[outputs.SeedNodeResponse]] = ..., hours_between_backups: Optional[_builtins.int] = ..., prometheus_endpoint: Optional[outputs.SeedNodeResponse] = ..., provision_error: Optional[outputs.CassandraErrorResponse] = ..., provisioning_state: Optional[_builtins.str] = ..., repair_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gossipCertificates")
    def gossip_certificates(self) -> Sequence[outputs.CertificateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedNodes")
    def seed_nodes(self) -> Sequence[outputs.SeedNodeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureConnectionMethod")
    def azure_connection_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cassandraAuditLoggingEnabled")
    def cassandra_audit_logging_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cassandraVersion")
    def cassandra_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificates")
    def client_certificates(self) -> Optional[Sequence[outputs.CertificateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNameOverride")
    def cluster_name_override(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deallocated(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedManagementSubnetId")
    def delegated_management_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalGossipCertificates")
    def external_gossip_certificates(self) -> Optional[Sequence[outputs.CertificateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalSeedNodes")
    def external_seed_nodes(self) -> Optional[Sequence[outputs.SeedNodeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursBetweenBackups")
    def hours_between_backups(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prometheusEndpoint")
    def prometheus_endpoint(self) -> Optional[outputs.SeedNodeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionError")
    def provision_error(self) -> Optional[outputs.CassandraErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repairEnabled")
    def repair_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ColumnResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CompositePathResponse(dict):
    def __init__(__self__, *, order: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ComputedPropertyResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., query: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConflictResolutionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conflict_resolution_path: Optional[_builtins.str] = ..., conflict_resolution_procedure: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPath")
    def conflict_resolution_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionProcedure")
    def conflict_resolution_procedure(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionStringResponse(dict):
    
    def __init__(__self__, *, connection_string: _builtins.str, description: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConsistencyPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_consistency_level: _builtins.str, max_interval_in_seconds: Optional[_builtins.int] = ..., max_staleness_prefix: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConsistencyLevel")
    def default_consistency_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInSeconds")
    def max_interval_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStalenessPrefix")
    def max_staleness_prefix(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ContainerPartitionKeyResponse(dict):
    
    def __init__(__self__, *, kind: Optional[_builtins.str] = ..., paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ContainerPartitionKeyResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, system_key: _builtins.bool, kind: Optional[_builtins.str] = ..., paths: Optional[Sequence[_builtins.str]] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemKey")
    def system_key(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ContainerPartitionKeyResponseV2(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, system_key: _builtins.bool, kind: Optional[_builtins.str] = ..., paths: Optional[Sequence[_builtins.str]] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemKey")
    def system_key(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ContinuousModeBackupPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, continuous_mode_properties: Optional[outputs.ContinuousModePropertiesResponse] = ..., migration_state: Optional[outputs.BackupPolicyMigrationStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousModeProperties")
    def continuous_mode_properties(self) -> Optional[outputs.ContinuousModePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> Optional[outputs.BackupPolicyMigrationStateResponse]:
        
        ...
    


@pulumi.output_type
class ContinuousModePropertiesResponse(dict):
    
    def __init__(__self__, *, tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CorsPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_origins: _builtins.str, allowed_headers: Optional[_builtins.str] = ..., allowed_methods: Optional[_builtins.str] = ..., exposed_headers: Optional[_builtins.str] = ..., max_age_in_seconds: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class DataCenterResourceResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, seed_nodes: Sequence[outputs.SeedNodeResponse], authentication_method_ldap_properties: Optional[outputs.AuthenticationMethodLdapPropertiesResponse] = ..., availability_zone: Optional[_builtins.bool] = ..., backup_storage_customer_key_uri: Optional[_builtins.str] = ..., base64_encoded_cassandra_yaml_fragment: Optional[_builtins.str] = ..., data_center_location: Optional[_builtins.str] = ..., deallocated: Optional[_builtins.bool] = ..., delegated_subnet_id: Optional[_builtins.str] = ..., disk_capacity: Optional[_builtins.int] = ..., disk_sku: Optional[_builtins.str] = ..., managed_disk_customer_key_uri: Optional[_builtins.str] = ..., node_count: Optional[_builtins.int] = ..., private_endpoint_ip_address: Optional[_builtins.str] = ..., provision_error: Optional[outputs.CassandraErrorResponse] = ..., provisioning_state: Optional[_builtins.str] = ..., sku: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedNodes")
    def seed_nodes(self) -> Sequence[outputs.SeedNodeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethodLdapProperties")
    def authentication_method_ldap_properties(self) -> Optional[outputs.AuthenticationMethodLdapPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageCustomerKeyUri")
    def backup_storage_customer_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="base64EncodedCassandraYamlFragment")
    def base64_encoded_cassandra_yaml_fragment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCenterLocation")
    def data_center_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deallocated(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedSubnetId")
    def delegated_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacity")
    def disk_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSku")
    def disk_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDiskCustomerKeyUri")
    def managed_disk_customer_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointIpAddress")
    def private_endpoint_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionError")
    def provision_error(self) -> Optional[outputs.CassandraErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataTransferRegionalServiceResourceResponse(dict):
    
    def __init__(__self__, *, location: _builtins.str, name: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataTransferServiceResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time: _builtins.str, locations: Sequence[outputs.DataTransferRegionalServiceResourceResponse], service_type: _builtins.str, status: _builtins.str, instance_count: Optional[_builtins.int] = ..., instance_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.DataTransferRegionalServiceResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseAccountConnectionStringResponse(dict):
    
    def __init__(__self__, *, connection_string: _builtins.str, description: _builtins.str, key_kind: _builtins.str, type: _builtins.str) -> None:
        
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
    @pulumi.getter(name="keyKind")
    def key_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseAccountKeysMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primary_master_key: outputs.AccountKeyMetadataResponse, primary_readonly_master_key: outputs.AccountKeyMetadataResponse, secondary_master_key: outputs.AccountKeyMetadataResponse, secondary_readonly_master_key: outputs.AccountKeyMetadataResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryMasterKey")
    def primary_master_key(self) -> outputs.AccountKeyMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryReadonlyMasterKey")
    def primary_readonly_master_key(self) -> outputs.AccountKeyMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryMasterKey")
    def secondary_master_key(self) -> outputs.AccountKeyMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryReadonlyMasterKey")
    def secondary_readonly_master_key(self) -> outputs.AccountKeyMetadataResponse:
        
        ...
    


@pulumi.output_type
class DatabaseRestoreResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collection_names: Optional[Sequence[_builtins.str]] = ..., database_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionNames")
    def collection_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_info: Sequence[outputs.ErrorAdditionalInfoResponse], code: _builtins.str, details: Sequence[outputs.ErrorDetailResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExcludedPathResponse(dict):
    def __init__(__self__, *, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FailoverPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, failover_priority: Optional[_builtins.int] = ..., location_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverPriority")
    def failover_priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetspaceAccountPropertiesResponseGlobalDatabaseAccountProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arm_location: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="armLocation")
    def arm_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FleetspacePropertiesResponseThroughputPoolConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_throughput: Optional[_builtins.int] = ..., min_throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FullTextIndexPathResponse(dict):
    
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FullTextPathResponse(dict):
    
    def __init__(__self__, *, path: _builtins.str, language: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FullTextPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_language: Optional[_builtins.str] = ..., full_text_paths: Optional[Sequence[outputs.FullTextPathResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextPaths")
    def full_text_paths(self) -> Optional[Sequence[outputs.FullTextPathResponse]]:
        
        ...
    


@pulumi.output_type
class GarnetClusterResourceResponseEndPoints(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GarnetClusterResourceResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_points: Sequence[outputs.GarnetClusterResourceResponseEndPoints], provisioning_state: _builtins.str, allocation_state: Optional[_builtins.str] = ..., availability_zone: Optional[_builtins.bool] = ..., cluster_type: Optional[_builtins.str] = ..., extensions: Optional[Sequence[_builtins.str]] = ..., node_count: Optional[_builtins.int] = ..., node_sku: Optional[_builtins.str] = ..., provision_error: Optional[outputs.ErrorDetailResponse] = ..., replication_factor: Optional[_builtins.int] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endPoints")
    def end_points(self) -> Sequence[outputs.GarnetClusterResourceResponseEndPoints]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationState")
    def allocation_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSku")
    def node_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionError")
    def provision_error(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphAPIComputeRegionalServiceResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, graph_api_compute_endpoint: _builtins.str, location: _builtins.str, name: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphApiComputeEndpoint")
    def graph_api_compute_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GraphAPIComputeServiceResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time: _builtins.str, locations: Sequence[outputs.GraphAPIComputeRegionalServiceResourceResponse], service_type: _builtins.str, status: _builtins.str, graph_api_compute_endpoint: Optional[_builtins.str] = ..., instance_count: Optional[_builtins.int] = ..., instance_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.GraphAPIComputeRegionalServiceResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphApiComputeEndpoint")
    def graph_api_compute_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphResourceGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GraphResourceGetPropertiesResponseResource(dict):
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GremlinDatabaseGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GremlinDatabaseGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, create_mode: Optional[_builtins.str] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    


@pulumi.output_type
class GremlinDatabaseRestoreResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: Optional[_builtins.str] = ..., graph_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphNames")
    def graph_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GremlinGraphGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GremlinGraphGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, analytical_storage_ttl: Optional[_builtins.float] = ..., conflict_resolution_policy: Optional[outputs.ConflictResolutionPolicyResponse] = ..., create_mode: Optional[_builtins.str] = ..., default_ttl: Optional[_builtins.int] = ..., indexing_policy: Optional[outputs.IndexingPolicyResponseV1] = ..., partition_key: Optional[outputs.ContainerPartitionKeyResponseV1] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ..., unique_key_policy: Optional[outputs.UniqueKeyPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[outputs.ConflictResolutionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional[outputs.IndexingPolicyResponseV1]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[outputs.ContainerPartitionKeyResponseV1]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(self) -> Optional[outputs.UniqueKeyPolicyResponse]:
        
        ...
    


@pulumi.output_type
class IncludedPathResponse(dict):
    
    def __init__(__self__, *, indexes: Optional[Sequence[outputs.IndexesResponse]] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indexes(self) -> Optional[Sequence[outputs.IndexesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_type: Optional[_builtins.str] = ..., kind: Optional[_builtins.str] = ..., precision: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IndexingPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic: Optional[_builtins.bool] = ..., excluded_paths: Optional[Sequence[outputs.ExcludedPathResponse]] = ..., included_paths: Optional[Sequence[outputs.IncludedPathResponse]] = ..., indexing_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[outputs.ExcludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[outputs.IncludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexingPolicyResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic: Optional[_builtins.bool] = ..., composite_indexes: Optional[Sequence[Sequence[outputs.CompositePathResponse]]] = ..., excluded_paths: Optional[Sequence[outputs.ExcludedPathResponse]] = ..., full_text_indexes: Optional[Sequence[outputs.FullTextIndexPathResponse]] = ..., included_paths: Optional[Sequence[outputs.IncludedPathResponse]] = ..., indexing_mode: Optional[_builtins.str] = ..., spatial_indexes: Optional[Sequence[outputs.SpatialSpecResponse]] = ..., vector_indexes: Optional[Sequence[outputs.VectorIndexResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeIndexes")
    def composite_indexes(self) -> Optional[Sequence[Sequence[outputs.CompositePathResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[outputs.ExcludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextIndexes")
    def full_text_indexes(self) -> Optional[Sequence[outputs.FullTextIndexPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[outputs.IncludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spatialIndexes")
    def spatial_indexes(self) -> Optional[Sequence[outputs.SpatialSpecResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIndexes")
    def vector_indexes(self) -> Optional[Sequence[outputs.VectorIndexResponse]]:
        
        ...
    


@pulumi.output_type
class IndexingPolicyResponseV2(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic: Optional[_builtins.bool] = ..., composite_indexes: Optional[Sequence[Sequence[outputs.CompositePathResponse]]] = ..., excluded_paths: Optional[Sequence[outputs.ExcludedPathResponse]] = ..., full_text_indexes: Optional[Sequence[outputs.FullTextIndexPathResponse]] = ..., included_paths: Optional[Sequence[outputs.IncludedPathResponse]] = ..., indexing_mode: Optional[_builtins.str] = ..., spatial_indexes: Optional[Sequence[outputs.SpatialSpecResponse]] = ..., vector_indexes: Optional[Sequence[outputs.VectorIndexResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeIndexes")
    def composite_indexes(self) -> Optional[Sequence[Sequence[outputs.CompositePathResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[outputs.ExcludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextIndexes")
    def full_text_indexes(self) -> Optional[Sequence[outputs.FullTextIndexPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[outputs.IncludedPathResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spatialIndexes")
    def spatial_indexes(self) -> Optional[Sequence[outputs.SpatialSpecResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIndexes")
    def vector_indexes(self) -> Optional[Sequence[outputs.VectorIndexResponse]]:
        
        ...
    


@pulumi.output_type
class IpAddressOrRangeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address_or_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressOrRange")
    def ip_address_or_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LocationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, document_endpoint: _builtins.str, id: _builtins.str, provisioning_state: _builtins.str, failover_priority: Optional[_builtins.int] = ..., is_zone_redundant: Optional[_builtins.bool] = ..., location_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentEndpoint")
    def document_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverPriority")
    def failover_priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedCassandraManagedServiceIdentityResponse(dict):
    
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
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.ManagedServiceIdentityResponseUserAssignedIdentities]] = ...) -> None:
        
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
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.ManagedServiceIdentityResponseUserAssignedIdentities]]:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponseUserAssignedIdentities(dict):
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
class MaterializedViewsBuilderRegionalServiceResourceResponse(dict):
    
    def __init__(__self__, *, location: _builtins.str, name: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MaterializedViewsBuilderServiceResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time: _builtins.str, locations: Sequence[outputs.MaterializedViewsBuilderRegionalServiceResourceResponse], service_type: _builtins.str, status: _builtins.str, instance_count: Optional[_builtins.int] = ..., instance_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.MaterializedViewsBuilderRegionalServiceResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDBCollectionGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoDBCollectionGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, analytical_storage_ttl: Optional[_builtins.int] = ..., create_mode: Optional[_builtins.str] = ..., indexes: Optional[Sequence[outputs.MongoIndexResponse]] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ..., shard_key: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indexes(self) -> Optional[Sequence[outputs.MongoIndexResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardKey")
    def shard_key(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MongoDBDatabaseGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoDBDatabaseGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, create_mode: Optional[_builtins.str] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    


@pulumi.output_type
class MongoIndexKeysResponse(dict):
    
    def __init__(__self__, *, keys: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class MongoIndexOptionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_after_seconds: Optional[_builtins.int] = ..., unique: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireAfterSeconds")
    def expire_after_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unique(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MongoIndexResponse(dict):
    
    def __init__(__self__, *, key: Optional[outputs.MongoIndexKeysResponse] = ..., options: Optional[outputs.MongoIndexOptionsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[outputs.MongoIndexKeysResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.MongoIndexOptionsResponse]:
        
        ...
    


@pulumi.output_type
class NodeGroupSpecResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: Optional[_builtins.float] = ..., enable_ha: Optional[_builtins.bool] = ..., kind: Optional[_builtins.str] = ..., node_count: Optional[_builtins.int] = ..., sku: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PeriodicModeBackupPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, migration_state: Optional[outputs.BackupPolicyMigrationStateResponse] = ..., periodic_mode_properties: Optional[outputs.PeriodicModePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> Optional[outputs.BackupPolicyMigrationStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodicModeProperties")
    def periodic_mode_properties(self) -> Optional[outputs.PeriodicModePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PeriodicModePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_interval_in_minutes: Optional[_builtins.int] = ..., backup_retention_interval_in_hours: Optional[_builtins.int] = ..., backup_storage_redundancy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupIntervalInMinutes")
    def backup_interval_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionIntervalInHours")
    def backup_retention_interval_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageRedundancy")
    def backup_storage_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_actions: Optional[Sequence[_builtins.str]] = ..., id: Optional[_builtins.str] = ..., not_data_actions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PermissionResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_actions: Optional[Sequence[_builtins.str]] = ..., not_data_actions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, type: _builtins.str, group_id: Optional[_builtins.str] = ..., private_endpoint: Optional[outputs.PrivateEndpointPropertyResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse] = ..., provisioning_state: Optional[_builtins.str] = ...) -> None:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
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
class PrivateLinkServiceConnectionStatePropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
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
class PrivilegeResponse(dict):
    
    def __init__(__self__, *, actions: Optional[Sequence[_builtins.str]] = ..., resource: Optional[outputs.PrivilegeResponseResource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.PrivilegeResponseResource]:
        
        ...
    


@pulumi.output_type
class PrivilegeResponseResource(dict):
    
    def __init__(__self__, *, collection: Optional[_builtins.str] = ..., db: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceRestoreParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, restore_source: Optional[_builtins.str] = ..., restore_timestamp_in_utc: Optional[_builtins.str] = ..., restore_with_ttl_disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSource")
    def restore_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTimestampInUtc")
    def restore_timestamp_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreWithTtlDisabled")
    def restore_with_ttl_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestoreParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases_to_restore: Optional[Sequence[outputs.DatabaseRestoreResourceResponse]] = ..., gremlin_databases_to_restore: Optional[Sequence[outputs.GremlinDatabaseRestoreResourceResponse]] = ..., restore_mode: Optional[_builtins.str] = ..., restore_source: Optional[_builtins.str] = ..., restore_timestamp_in_utc: Optional[_builtins.str] = ..., restore_with_ttl_disabled: Optional[_builtins.bool] = ..., source_backup_location: Optional[_builtins.str] = ..., tables_to_restore: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToRestore")
    def databases_to_restore(self) -> Optional[Sequence[outputs.DatabaseRestoreResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gremlinDatabasesToRestore")
    def gremlin_databases_to_restore(self) -> Optional[Sequence[outputs.GremlinDatabaseRestoreResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreMode")
    def restore_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSource")
    def restore_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTimestampInUtc")
    def restore_timestamp_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreWithTtlDisabled")
    def restore_with_ttl_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBackupLocation")
    def source_backup_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToRestore")
    def tables_to_restore(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RoleResponse(dict):
    
    def __init__(__self__, *, db: Optional[_builtins.str] = ..., role: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SeedNodeResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpatialSpecResponse(dict):
    def __init__(__self__, *, path: Optional[_builtins.str] = ..., types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SqlContainerGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SqlContainerGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, analytical_storage_ttl: Optional[_builtins.float] = ..., client_encryption_policy: Optional[outputs.ClientEncryptionPolicyResponse] = ..., computed_properties: Optional[Sequence[outputs.ComputedPropertyResponse]] = ..., conflict_resolution_policy: Optional[outputs.ConflictResolutionPolicyResponse] = ..., create_mode: Optional[_builtins.str] = ..., default_ttl: Optional[_builtins.int] = ..., full_text_policy: Optional[outputs.FullTextPolicyResponse] = ..., indexing_policy: Optional[outputs.IndexingPolicyResponseV2] = ..., partition_key: Optional[outputs.ContainerPartitionKeyResponseV2] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ..., unique_key_policy: Optional[outputs.UniqueKeyPolicyResponse] = ..., vector_embedding_policy: Optional[outputs.VectorEmbeddingPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientEncryptionPolicy")
    def client_encryption_policy(self) -> Optional[outputs.ClientEncryptionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computedProperties")
    def computed_properties(self) -> Optional[Sequence[outputs.ComputedPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[outputs.ConflictResolutionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextPolicy")
    def full_text_policy(self) -> Optional[outputs.FullTextPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional[outputs.IndexingPolicyResponseV2]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[outputs.ContainerPartitionKeyResponseV2]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(self) -> Optional[outputs.UniqueKeyPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorEmbeddingPolicy")
    def vector_embedding_policy(self) -> Optional[outputs.VectorEmbeddingPolicyResponse]:
        
        ...
    


@pulumi.output_type
class SqlDatabaseGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SqlDatabaseGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, colls: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ..., users: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def colls(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlDedicatedGatewayRegionalServiceResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, name: _builtins.str, sql_dedicated_gateway_endpoint: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlDedicatedGatewayEndpoint")
    def sql_dedicated_gateway_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SqlDedicatedGatewayServiceResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time: _builtins.str, locations: Sequence[outputs.SqlDedicatedGatewayRegionalServiceResourceResponse], service_type: _builtins.str, status: _builtins.str, dedicated_gateway_type: Optional[_builtins.str] = ..., instance_count: Optional[_builtins.int] = ..., instance_size: Optional[_builtins.str] = ..., sql_dedicated_gateway_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.SqlDedicatedGatewayRegionalServiceResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedGatewayType")
    def dedicated_gateway_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlDedicatedGatewayEndpoint")
    def sql_dedicated_gateway_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlStoredProcedureGetPropertiesResponseResource(dict):
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, body: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlTriggerGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, body: Optional[_builtins.str] = ..., trigger_operation: Optional[_builtins.str] = ..., trigger_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerOperation")
    def trigger_operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlUserDefinedFunctionGetPropertiesResponseResource(dict):
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, body: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
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
class TableGetPropertiesResponseOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_settings: Optional[outputs.AutoscaleSettingsResponse] = ..., throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[outputs.AutoscaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TableGetPropertiesResponseResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, rid: _builtins.str, ts: _builtins.float, create_mode: Optional[_builtins.str] = ..., restore_parameters: Optional[outputs.ResourceRestoreParametersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[outputs.ResourceRestoreParametersResponse]:
        
        ...
    


@pulumi.output_type
class UniqueKeyPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, unique_keys: Optional[Sequence[outputs.UniqueKeyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeys")
    def unique_keys(self) -> Optional[Sequence[outputs.UniqueKeyResponse]]:
        
        ...
    


@pulumi.output_type
class UniqueKeyResponse(dict):
    
    def __init__(__self__, *, paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VectorEmbeddingPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vector_embeddings: Optional[Sequence[outputs.VectorEmbeddingResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorEmbeddings")
    def vector_embeddings(self) -> Optional[Sequence[outputs.VectorEmbeddingResponse]]:
        
        ...
    


@pulumi.output_type
class VectorEmbeddingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_type: _builtins.str, dimensions: _builtins.int, distance_function: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distanceFunction")
    def distance_function(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VectorIndexResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, type: _builtins.str, indexing_search_list_size: Optional[_builtins.float] = ..., quantization_byte_size: Optional[_builtins.float] = ..., vector_index_shard_key: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingSearchListSize")
    def indexing_search_list_size(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quantizationByteSize")
    def quantization_byte_size(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIndexShardKey")
    def vector_index_shard_key(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VirtualNetworkRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., ignore_missing_v_net_service_endpoint: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVNetServiceEndpoint")
    def ignore_missing_v_net_service_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    


