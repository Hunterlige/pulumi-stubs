

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalyticalStorageConfigurationArgs', 'AnalyticalStorageConfigurationArgsDict', 'ApiPropertiesArgs', 'ApiPropertiesArgsDict', 'AuthenticationMethodLdapPropertiesArgs', 'AuthenticationMethodLdapPropertiesArgsDict', 'AutoscaleSettingsArgs', 'AutoscaleSettingsArgsDict', 'BackupPolicyMigrationStateArgs', 'BackupPolicyMigrationStateArgsDict', 'CapabilityArgs', 'CapabilityArgsDict', 'CapacityArgs', 'CapacityArgsDict', 'CassandraErrorArgs', 'CassandraErrorArgsDict', 'CassandraKeyspaceResourceArgs', 'CassandraKeyspaceResourceArgsDict', 'CassandraPartitionKeyArgs', 'CassandraPartitionKeyArgsDict', 'CassandraSchemaArgs', 'CassandraSchemaArgsDict', 'CassandraTableResourceArgs', 'CassandraTableResourceArgsDict', 'CassandraViewResourceArgs', 'CassandraViewResourceArgsDict', 'CertificateArgs', 'CertificateArgsDict', 'ClientEncryptionIncludedPathArgs', 'ClientEncryptionIncludedPathArgsDict', 'ClientEncryptionPolicyArgs', 'ClientEncryptionPolicyArgsDict', 'ClusterKeyArgs', 'ClusterKeyArgsDict', 'ClusterResourcePropertiesArgs', 'ClusterResourcePropertiesArgsDict', 'ColumnArgs', 'ColumnArgsDict', 'CompositePathArgs', 'CompositePathArgsDict', 'ComputedPropertyArgs', 'ComputedPropertyArgsDict', 'ConflictResolutionPolicyArgs', 'ConflictResolutionPolicyArgsDict', 'ConsistencyPolicyArgs', 'ConsistencyPolicyArgsDict', 'ContainerPartitionKeyArgs', 'ContainerPartitionKeyArgsDict', 'ContinuousModeBackupPolicyArgs', 'ContinuousModeBackupPolicyArgsDict', 'ContinuousModePropertiesArgs', 'ContinuousModePropertiesArgsDict', 'CorsPolicyArgs', 'CorsPolicyArgsDict', 'CreateUpdateOptionsArgs', 'CreateUpdateOptionsArgsDict', 'DataCenterResourcePropertiesArgs', 'DataCenterResourcePropertiesArgsDict', ..., ..., 'DatabaseRestoreResourceArgs', 'DatabaseRestoreResourceArgsDict', 'ExcludedPathArgs', 'ExcludedPathArgsDict', ..., ..., ..., ..., 'FullTextIndexPathArgs', 'FullTextIndexPathArgsDict', 'FullTextPathArgs', 'FullTextPathArgsDict', 'FullTextPolicyArgs', 'FullTextPolicyArgsDict', 'GarnetClusterResourcePropertiesArgs', 'GarnetClusterResourcePropertiesArgsDict', ..., ..., 'GraphResourceArgs', 'GraphResourceArgsDict', 'GremlinDatabaseResourceArgs', 'GremlinDatabaseResourceArgsDict', 'GremlinDatabaseRestoreResourceArgs', 'GremlinDatabaseRestoreResourceArgsDict', 'GremlinGraphResourceArgs', 'GremlinGraphResourceArgsDict', 'IncludedPathArgs', 'IncludedPathArgsDict', 'IndexesArgs', 'IndexesArgsDict', 'IndexingPolicyArgs', 'IndexingPolicyArgsDict', 'IpAddressOrRangeArgs', 'IpAddressOrRangeArgsDict', 'LocationArgs', 'LocationArgsDict', 'ManagedCassandraManagedServiceIdentityArgs', 'ManagedCassandraManagedServiceIdentityArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', ..., ..., 'MongoClusterRestoreParametersArgs', 'MongoClusterRestoreParametersArgsDict', 'MongoDBCollectionResourceArgs', 'MongoDBCollectionResourceArgsDict', 'MongoDBDatabaseResourceArgs', 'MongoDBDatabaseResourceArgsDict', 'MongoIndexKeysArgs', 'MongoIndexKeysArgsDict', 'MongoIndexOptionsArgs', 'MongoIndexOptionsArgsDict', 'MongoIndexArgs', 'MongoIndexArgsDict', 'NodeGroupSpecArgs', 'NodeGroupSpecArgsDict', 'PeriodicModeBackupPolicyArgs', 'PeriodicModeBackupPolicyArgsDict', 'PeriodicModePropertiesArgs', 'PeriodicModePropertiesArgsDict', 'PermissionArgs', 'PermissionArgsDict', 'PrivateEndpointPropertyArgs', 'PrivateEndpointPropertyArgsDict', 'PrivateLinkServiceConnectionStatePropertyArgs', 'PrivateLinkServiceConnectionStatePropertyArgsDict', 'PrivilegeResourceArgs', 'PrivilegeResourceArgsDict', 'PrivilegeArgs', 'PrivilegeArgsDict', 'ResourceRestoreParametersArgs', 'ResourceRestoreParametersArgsDict', 'RestoreParametersArgs', 'RestoreParametersArgsDict', 'RoleArgs', 'RoleArgsDict', 'SeedNodeArgs', 'SeedNodeArgsDict', 'SpatialSpecArgs', 'SpatialSpecArgsDict', 'SqlContainerResourceArgs', 'SqlContainerResourceArgsDict', 'SqlDatabaseResourceArgs', 'SqlDatabaseResourceArgsDict', ..., ..., 'SqlStoredProcedureResourceArgs', 'SqlStoredProcedureResourceArgsDict', 'SqlTriggerResourceArgs', 'SqlTriggerResourceArgsDict', 'SqlUserDefinedFunctionResourceArgs', 'SqlUserDefinedFunctionResourceArgsDict', 'TableResourceArgs', 'TableResourceArgsDict', 'UniqueKeyPolicyArgs', 'UniqueKeyPolicyArgsDict', 'UniqueKeyArgs', 'UniqueKeyArgsDict', 'VectorEmbeddingPolicyArgs', 'VectorEmbeddingPolicyArgsDict', 'VectorEmbeddingArgs', 'VectorEmbeddingArgsDict', 'VectorIndexArgs', 'VectorIndexArgsDict', 'VirtualNetworkRuleArgs', 'VirtualNetworkRuleArgsDict']
class AnalyticalStorageConfigurationArgsDict(TypedDict):
    
    schema_type: NotRequired[pulumi.Input[Union[_builtins.str, AnalyticalStorageSchemaType]]]


@pulumi.input_type
class AnalyticalStorageConfigurationArgs:
    def __init__(__self__, *, schema_type: Optional[pulumi.Input[Union[_builtins.str, AnalyticalStorageSchemaType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AnalyticalStorageSchemaType]]]:
        
        ...
    
    @schema_type.setter
    def schema_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AnalyticalStorageSchemaType]]]): # -> None:
        ...
    


class ApiPropertiesArgsDict(TypedDict):
    server_version: NotRequired[pulumi.Input[Union[_builtins.str, ServerVersion]]]


@pulumi.input_type
class ApiPropertiesArgs:
    def __init__(__self__, *, server_version: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]): # -> None:
        ...
    


class AuthenticationMethodLdapPropertiesArgsDict(TypedDict):
    
    connection_timeout_in_ms: NotRequired[pulumi.Input[_builtins.int]]
    search_base_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]
    search_filter_template: NotRequired[pulumi.Input[_builtins.str]]
    server_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertificateArgsDict]]]]
    server_hostname: NotRequired[pulumi.Input[_builtins.str]]
    server_port: NotRequired[pulumi.Input[_builtins.int]]
    service_user_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]
    service_user_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthenticationMethodLdapPropertiesArgs:
    def __init__(__self__, *, connection_timeout_in_ms: Optional[pulumi.Input[_builtins.int]] = ..., search_base_distinguished_name: Optional[pulumi.Input[_builtins.str]] = ..., search_filter_template: Optional[pulumi.Input[_builtins.str]] = ..., server_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]] = ..., server_hostname: Optional[pulumi.Input[_builtins.str]] = ..., server_port: Optional[pulumi.Input[_builtins.int]] = ..., service_user_distinguished_name: Optional[pulumi.Input[_builtins.str]] = ..., service_user_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeoutInMs")
    def connection_timeout_in_ms(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_timeout_in_ms.setter
    def connection_timeout_in_ms(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchBaseDistinguishedName")
    def search_base_distinguished_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @search_base_distinguished_name.setter
    def search_base_distinguished_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchFilterTemplate")
    def search_filter_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @search_filter_template.setter
    def search_filter_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]:
        ...
    
    @server_certificates.setter
    def server_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverHostname")
    def server_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_hostname.setter
    def server_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @server_port.setter
    def server_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserDistinguishedName")
    def service_user_distinguished_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_user_distinguished_name.setter
    def service_user_distinguished_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUserPassword")
    def service_user_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_user_password.setter
    def service_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AutoscaleSettingsArgsDict(TypedDict):
    max_throughput: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AutoscaleSettingsArgs:
    def __init__(__self__, *, max_throughput: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_throughput.setter
    def max_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BackupPolicyMigrationStateArgsDict(TypedDict):
    
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, BackupPolicyMigrationStatus]]]
    target_type: NotRequired[pulumi.Input[Union[_builtins.str, BackupPolicyType]]]


@pulumi.input_type
class BackupPolicyMigrationStateArgs:
    def __init__(__self__, *, start_time: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, BackupPolicyMigrationStatus]]] = ..., target_type: Optional[pulumi.Input[Union[_builtins.str, BackupPolicyType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupPolicyMigrationStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupPolicyMigrationStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupPolicyType]]]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupPolicyType]]]): # -> None:
        ...
    


class CapabilityArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CapabilityArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CapacityArgsDict(TypedDict):
    
    total_throughput_limit: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CapacityArgs:
    def __init__(__self__, *, total_throughput_limit: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalThroughputLimit")
    def total_throughput_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @total_throughput_limit.setter
    def total_throughput_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CassandraErrorArgsDict(TypedDict):
    additional_error_info: NotRequired[pulumi.Input[_builtins.str]]
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CassandraErrorArgs:
    def __init__(__self__, *, additional_error_info: Optional[pulumi.Input[_builtins.str]] = ..., code: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalErrorInfo")
    def additional_error_info(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_error_info.setter
    def additional_error_info(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CassandraKeyspaceResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class CassandraKeyspaceResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CassandraPartitionKeyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CassandraPartitionKeyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CassandraSchemaArgsDict(TypedDict):
    
    cluster_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterKeyArgsDict]]]]
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[ColumnArgsDict]]]]
    partition_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[CassandraPartitionKeyArgsDict]]]]


@pulumi.input_type
class CassandraSchemaArgs:
    def __init__(__self__, *, cluster_keys: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterKeyArgs]]]] = ..., columns: Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]] = ..., partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[CassandraPartitionKeyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterKeys")
    def cluster_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterKeyArgs]]]]:
        
        ...
    
    @cluster_keys.setter
    def cluster_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]]:
        
        ...
    
    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CassandraPartitionKeyArgs]]]]:
        
        ...
    
    @partition_keys.setter
    def partition_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CassandraPartitionKeyArgs]]]]): # -> None:
        ...
    


class CassandraTableResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    analytical_storage_ttl: NotRequired[pulumi.Input[_builtins.int]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    schema: NotRequired[pulumi.Input[CassandraSchemaArgsDict]]


@pulumi.input_type
class CassandraTableResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], analytical_storage_ttl: Optional[pulumi.Input[_builtins.int]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., schema: Optional[pulumi.Input[CassandraSchemaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[CassandraSchemaArgs]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[CassandraSchemaArgs]]): # -> None:
        ...
    


class CassandraViewResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    view_definition: pulumi.Input[_builtins.str]


@pulumi.input_type
class CassandraViewResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], view_definition: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewDefinition")
    def view_definition(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @view_definition.setter
    def view_definition(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CertificateArgsDict(TypedDict):
    pem: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *, pem: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pem(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pem.setter
    def pem(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClientEncryptionIncludedPathArgsDict(TypedDict):
    
    client_encryption_key_id: pulumi.Input[_builtins.str]
    encryption_algorithm: pulumi.Input[_builtins.str]
    encryption_type: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClientEncryptionIncludedPathArgs:
    def __init__(__self__, *, client_encryption_key_id: pulumi.Input[_builtins.str], encryption_algorithm: pulumi.Input[_builtins.str], encryption_type: pulumi.Input[_builtins.str], path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientEncryptionKeyId")
    def client_encryption_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_encryption_key_id.setter
    def client_encryption_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClientEncryptionPolicyArgsDict(TypedDict):
    
    included_paths: pulumi.Input[Sequence[pulumi.Input[ClientEncryptionIncludedPathArgsDict]]]
    policy_format_version: pulumi.Input[_builtins.int]


@pulumi.input_type
class ClientEncryptionPolicyArgs:
    def __init__(__self__, *, included_paths: pulumi.Input[Sequence[pulumi.Input[ClientEncryptionIncludedPathArgs]]], policy_format_version: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> pulumi.Input[Sequence[pulumi.Input[ClientEncryptionIncludedPathArgs]]]:
        
        ...
    
    @included_paths.setter
    def included_paths(self, value: pulumi.Input[Sequence[pulumi.Input[ClientEncryptionIncludedPathArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFormatVersion")
    def policy_format_version(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @policy_format_version.setter
    def policy_format_version(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ClusterKeyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    order_by: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterKeyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., order_by: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @order_by.setter
    def order_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterResourcePropertiesArgsDict(TypedDict):
    
    authentication_method: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]
    azure_connection_method: NotRequired[pulumi.Input[Union[_builtins.str, AzureConnectionType]]]
    cassandra_audit_logging_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    cassandra_version: NotRequired[pulumi.Input[_builtins.str]]
    client_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertificateArgsDict]]]]
    cluster_name_override: NotRequired[pulumi.Input[_builtins.str]]
    deallocated: NotRequired[pulumi.Input[_builtins.bool]]
    delegated_management_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    external_gossip_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertificateArgsDict]]]]
    external_seed_nodes: NotRequired[pulumi.Input[Sequence[pulumi.Input[SeedNodeArgsDict]]]]
    hours_between_backups: NotRequired[pulumi.Input[_builtins.int]]
    initial_cassandra_admin_password: NotRequired[pulumi.Input[_builtins.str]]
    prometheus_endpoint: NotRequired[pulumi.Input[SeedNodeArgsDict]]
    provision_error: NotRequired[pulumi.Input[CassandraErrorArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]
    repair_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    restore_from_backup_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterResourcePropertiesArgs:
    def __init__(__self__, *, authentication_method: Optional[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]] = ..., azure_connection_method: Optional[pulumi.Input[Union[_builtins.str, AzureConnectionType]]] = ..., cassandra_audit_logging_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cassandra_version: Optional[pulumi.Input[_builtins.str]] = ..., client_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]] = ..., cluster_name_override: Optional[pulumi.Input[_builtins.str]] = ..., deallocated: Optional[pulumi.Input[_builtins.bool]] = ..., delegated_management_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., external_gossip_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]] = ..., external_seed_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[SeedNodeArgs]]]] = ..., hours_between_backups: Optional[pulumi.Input[_builtins.int]] = ..., initial_cassandra_admin_password: Optional[pulumi.Input[_builtins.str]] = ..., prometheus_endpoint: Optional[pulumi.Input[SeedNodeArgs]] = ..., provision_error: Optional[pulumi.Input[CassandraErrorArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]] = ..., repair_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., restore_from_backup_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]:
        
        ...
    
    @authentication_method.setter
    def authentication_method(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureConnectionMethod")
    def azure_connection_method(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureConnectionType]]]:
        
        ...
    
    @azure_connection_method.setter
    def azure_connection_method(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureConnectionType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cassandraAuditLoggingEnabled")
    def cassandra_audit_logging_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cassandra_audit_logging_enabled.setter
    def cassandra_audit_logging_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cassandraVersion")
    def cassandra_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cassandra_version.setter
    def cassandra_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificates")
    def client_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]:
        
        ...
    
    @client_certificates.setter
    def client_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNameOverride")
    def cluster_name_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name_override.setter
    def cluster_name_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deallocated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deallocated.setter
    def deallocated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedManagementSubnetId")
    def delegated_management_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_management_subnet_id.setter
    def delegated_management_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalGossipCertificates")
    def external_gossip_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]:
        
        ...
    
    @external_gossip_certificates.setter
    def external_gossip_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalSeedNodes")
    def external_seed_nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SeedNodeArgs]]]]:
        
        ...
    
    @external_seed_nodes.setter
    def external_seed_nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SeedNodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursBetweenBackups")
    def hours_between_backups(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hours_between_backups.setter
    def hours_between_backups(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialCassandraAdminPassword")
    def initial_cassandra_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initial_cassandra_admin_password.setter
    def initial_cassandra_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prometheusEndpoint")
    def prometheus_endpoint(self) -> Optional[pulumi.Input[SeedNodeArgs]]:
        
        ...
    
    @prometheus_endpoint.setter
    def prometheus_endpoint(self, value: Optional[pulumi.Input[SeedNodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionError")
    def provision_error(self) -> Optional[pulumi.Input[CassandraErrorArgs]]:
        
        ...
    
    @provision_error.setter
    def provision_error(self, value: Optional[pulumi.Input[CassandraErrorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repairEnabled")
    def repair_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @repair_enabled.setter
    def repair_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreFromBackupId")
    def restore_from_backup_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_from_backup_id.setter
    def restore_from_backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ColumnArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ColumnArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CompositePathArgsDict(TypedDict):
    order: NotRequired[pulumi.Input[Union[_builtins.str, CompositePathSortOrder]]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CompositePathArgs:
    def __init__(__self__, *, order: Optional[pulumi.Input[Union[_builtins.str, CompositePathSortOrder]]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[Union[_builtins.str, CompositePathSortOrder]]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[Union[_builtins.str, CompositePathSortOrder]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ComputedPropertyArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ComputedPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConflictResolutionPolicyArgsDict(TypedDict):
    
    conflict_resolution_path: NotRequired[pulumi.Input[_builtins.str]]
    conflict_resolution_procedure: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, ConflictResolutionMode]]]


@pulumi.input_type
class ConflictResolutionPolicyArgs:
    def __init__(__self__, *, conflict_resolution_path: Optional[pulumi.Input[_builtins.str]] = ..., conflict_resolution_procedure: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, ConflictResolutionMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPath")
    def conflict_resolution_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @conflict_resolution_path.setter
    def conflict_resolution_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionProcedure")
    def conflict_resolution_procedure(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @conflict_resolution_procedure.setter
    def conflict_resolution_procedure(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ConflictResolutionMode]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ConflictResolutionMode]]]): # -> None:
        ...
    


class ConsistencyPolicyArgsDict(TypedDict):
    
    default_consistency_level: pulumi.Input[DefaultConsistencyLevel]
    max_interval_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    max_staleness_prefix: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class ConsistencyPolicyArgs:
    def __init__(__self__, *, default_consistency_level: pulumi.Input[DefaultConsistencyLevel], max_interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., max_staleness_prefix: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConsistencyLevel")
    def default_consistency_level(self) -> pulumi.Input[DefaultConsistencyLevel]:
        
        ...
    
    @default_consistency_level.setter
    def default_consistency_level(self, value: pulumi.Input[DefaultConsistencyLevel]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInSeconds")
    def max_interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_interval_in_seconds.setter
    def max_interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStalenessPrefix")
    def max_staleness_prefix(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_staleness_prefix.setter
    def max_staleness_prefix(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class ContainerPartitionKeyArgsDict(TypedDict):
    
    kind: NotRequired[pulumi.Input[Union[_builtins.str, PartitionKind]]]
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    version: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ContainerPartitionKeyArgs:
    def __init__(__self__, *, kind: Optional[pulumi.Input[Union[_builtins.str, PartitionKind]]] = ..., paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, PartitionKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, PartitionKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ContinuousModeBackupPolicyArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    continuous_mode_properties: NotRequired[pulumi.Input[ContinuousModePropertiesArgsDict]]
    migration_state: NotRequired[pulumi.Input[BackupPolicyMigrationStateArgsDict]]


@pulumi.input_type
class ContinuousModeBackupPolicyArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], continuous_mode_properties: Optional[pulumi.Input[ContinuousModePropertiesArgs]] = ..., migration_state: Optional[pulumi.Input[BackupPolicyMigrationStateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousModeProperties")
    def continuous_mode_properties(self) -> Optional[pulumi.Input[ContinuousModePropertiesArgs]]:
        
        ...
    
    @continuous_mode_properties.setter
    def continuous_mode_properties(self, value: Optional[pulumi.Input[ContinuousModePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> Optional[pulumi.Input[BackupPolicyMigrationStateArgs]]:
        
        ...
    
    @migration_state.setter
    def migration_state(self, value: Optional[pulumi.Input[BackupPolicyMigrationStateArgs]]): # -> None:
        ...
    


class ContinuousModePropertiesArgsDict(TypedDict):
    
    tier: NotRequired[pulumi.Input[Union[_builtins.str, ContinuousTier]]]


@pulumi.input_type
class ContinuousModePropertiesArgs:
    def __init__(__self__, *, tier: Optional[pulumi.Input[Union[_builtins.str, ContinuousTier]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, ContinuousTier]]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, ContinuousTier]]]): # -> None:
        ...
    


class CorsPolicyArgsDict(TypedDict):
    
    allowed_origins: pulumi.Input[_builtins.str]
    allowed_headers: NotRequired[pulumi.Input[_builtins.str]]
    allowed_methods: NotRequired[pulumi.Input[_builtins.str]]
    exposed_headers: NotRequired[pulumi.Input[_builtins.str]]
    max_age_in_seconds: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class CorsPolicyArgs:
    def __init__(__self__, *, allowed_origins: pulumi.Input[_builtins.str], allowed_headers: Optional[pulumi.Input[_builtins.str]] = ..., allowed_methods: Optional[pulumi.Input[_builtins.str]] = ..., exposed_headers: Optional[pulumi.Input[_builtins.str]] = ..., max_age_in_seconds: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exposed_headers.setter
    def exposed_headers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class CreateUpdateOptionsArgsDict(TypedDict):
    
    autoscale_settings: NotRequired[pulumi.Input[AutoscaleSettingsArgsDict]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CreateUpdateOptionsArgs:
    def __init__(__self__, *, autoscale_settings: Optional[pulumi.Input[AutoscaleSettingsArgs]] = ..., throughput: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[pulumi.Input[AutoscaleSettingsArgs]]:
        
        ...
    
    @autoscale_settings.setter
    def autoscale_settings(self, value: Optional[pulumi.Input[AutoscaleSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DataCenterResourcePropertiesArgsDict(TypedDict):
    
    authentication_method_ldap_properties: NotRequired[pulumi.Input[AuthenticationMethodLdapPropertiesArgsDict]]
    availability_zone: NotRequired[pulumi.Input[_builtins.bool]]
    backup_storage_customer_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    base64_encoded_cassandra_yaml_fragment: NotRequired[pulumi.Input[_builtins.str]]
    data_center_location: NotRequired[pulumi.Input[_builtins.str]]
    deallocated: NotRequired[pulumi.Input[_builtins.bool]]
    delegated_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_capacity: NotRequired[pulumi.Input[_builtins.int]]
    disk_sku: NotRequired[pulumi.Input[_builtins.str]]
    managed_disk_customer_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    private_endpoint_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    provision_error: NotRequired[pulumi.Input[CassandraErrorArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]
    sku: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataCenterResourcePropertiesArgs:
    def __init__(__self__, *, authentication_method_ldap_properties: Optional[pulumi.Input[AuthenticationMethodLdapPropertiesArgs]] = ..., availability_zone: Optional[pulumi.Input[_builtins.bool]] = ..., backup_storage_customer_key_uri: Optional[pulumi.Input[_builtins.str]] = ..., base64_encoded_cassandra_yaml_fragment: Optional[pulumi.Input[_builtins.str]] = ..., data_center_location: Optional[pulumi.Input[_builtins.str]] = ..., deallocated: Optional[pulumi.Input[_builtins.bool]] = ..., delegated_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_capacity: Optional[pulumi.Input[_builtins.int]] = ..., disk_sku: Optional[pulumi.Input[_builtins.str]] = ..., managed_disk_customer_key_uri: Optional[pulumi.Input[_builtins.str]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., private_endpoint_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., provision_error: Optional[pulumi.Input[CassandraErrorArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]] = ..., sku: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethodLdapProperties")
    def authentication_method_ldap_properties(self) -> Optional[pulumi.Input[AuthenticationMethodLdapPropertiesArgs]]:
        
        ...
    
    @authentication_method_ldap_properties.setter
    def authentication_method_ldap_properties(self, value: Optional[pulumi.Input[AuthenticationMethodLdapPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageCustomerKeyUri")
    def backup_storage_customer_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_storage_customer_key_uri.setter
    def backup_storage_customer_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="base64EncodedCassandraYamlFragment")
    def base64_encoded_cassandra_yaml_fragment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base64_encoded_cassandra_yaml_fragment.setter
    def base64_encoded_cassandra_yaml_fragment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCenterLocation")
    def data_center_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_center_location.setter
    def data_center_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deallocated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deallocated.setter
    def deallocated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedSubnetId")
    def delegated_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_subnet_id.setter
    def delegated_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacity")
    def disk_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_capacity.setter
    def disk_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSku")
    def disk_sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_sku.setter
    def disk_sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDiskCustomerKeyUri")
    def managed_disk_customer_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_disk_customer_key_uri.setter
    def managed_disk_customer_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointIpAddress")
    def private_endpoint_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_endpoint_ip_address.setter
    def private_endpoint_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionError")
    def provision_error(self) -> Optional[pulumi.Input[CassandraErrorArgs]]:
        
        ...
    
    @provision_error.setter
    def provision_error(self, value: Optional[pulumi.Input[CassandraErrorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataTransferServiceResourceCreateUpdatePropertiesArgsDict(TypedDict):
    
    service_type: pulumi.Input[_builtins.str]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_size: NotRequired[pulumi.Input[Union[_builtins.str, ServiceSize]]]


@pulumi.input_type
class DataTransferServiceResourceCreateUpdatePropertiesArgs:
    def __init__(__self__, *, service_type: pulumi.Input[_builtins.str], instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_size: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]:
        
        ...
    
    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]): # -> None:
        ...
    


class DatabaseRestoreResourceArgsDict(TypedDict):
    
    collection_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    database_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseRestoreResourceArgs:
    def __init__(__self__, *, collection_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionNames")
    def collection_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @collection_names.setter
    def collection_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExcludedPathArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExcludedPathArgs:
    def __init__(__self__, *, path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgsDict(TypedDict):
    
    arm_location: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgs:
    def __init__(__self__, *, arm_location: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="armLocation")
    def arm_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arm_location.setter
    def arm_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FleetspacePropertiesThroughputPoolConfigurationArgsDict(TypedDict):
    
    max_throughput: NotRequired[pulumi.Input[_builtins.int]]
    min_throughput: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FleetspacePropertiesThroughputPoolConfigurationArgs:
    def __init__(__self__, *, max_throughput: Optional[pulumi.Input[_builtins.int]] = ..., min_throughput: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_throughput.setter
    def max_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_throughput.setter
    def min_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FullTextIndexPathArgsDict(TypedDict):
    
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class FullTextIndexPathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FullTextPathArgsDict(TypedDict):
    
    path: pulumi.Input[_builtins.str]
    language: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FullTextPathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], language: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FullTextPolicyArgsDict(TypedDict):
    
    default_language: NotRequired[pulumi.Input[_builtins.str]]
    full_text_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[FullTextPathArgsDict]]]]


@pulumi.input_type
class FullTextPolicyArgs:
    def __init__(__self__, *, default_language: Optional[pulumi.Input[_builtins.str]] = ..., full_text_paths: Optional[pulumi.Input[Sequence[pulumi.Input[FullTextPathArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_language.setter
    def default_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextPaths")
    def full_text_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FullTextPathArgs]]]]:
        
        ...
    
    @full_text_paths.setter
    def full_text_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FullTextPathArgs]]]]): # -> None:
        ...
    


class GarnetClusterResourcePropertiesArgsDict(TypedDict):
    
    allocation_state: NotRequired[pulumi.Input[Union[_builtins.str, AllocationState]]]
    availability_zone: NotRequired[pulumi.Input[_builtins.bool]]
    cluster_type: NotRequired[pulumi.Input[Union[_builtins.str, ClusterType]]]
    extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    node_sku: NotRequired[pulumi.Input[_builtins.str]]
    replication_factor: NotRequired[pulumi.Input[_builtins.int]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GarnetClusterResourcePropertiesArgs:
    def __init__(__self__, *, allocation_state: Optional[pulumi.Input[Union[_builtins.str, AllocationState]]] = ..., availability_zone: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_type: Optional[pulumi.Input[Union[_builtins.str, ClusterType]]] = ..., extensions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., node_sku: Optional[pulumi.Input[_builtins.str]] = ..., replication_factor: Optional[pulumi.Input[_builtins.int]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationState")
    def allocation_state(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationState]]]:
        
        ...
    
    @allocation_state.setter
    def allocation_state(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ClusterType]]]:
        
        ...
    
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSku")
    def node_sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_sku.setter
    def node_sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GraphAPIComputeServiceResourceCreateUpdatePropertiesArgsDict(TypedDict):
    
    service_type: pulumi.Input[_builtins.str]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_size: NotRequired[pulumi.Input[Union[_builtins.str, ServiceSize]]]


@pulumi.input_type
class GraphAPIComputeServiceResourceCreateUpdatePropertiesArgs:
    def __init__(__self__, *, service_type: pulumi.Input[_builtins.str], instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_size: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]:
        
        ...
    
    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]): # -> None:
        ...
    


class GraphResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class GraphResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GremlinDatabaseResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]


@pulumi.input_type
class GremlinDatabaseResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    


class GremlinDatabaseRestoreResourceArgsDict(TypedDict):
    
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    graph_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class GremlinDatabaseRestoreResourceArgs:
    def __init__(__self__, *, database_name: Optional[pulumi.Input[_builtins.str]] = ..., graph_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphNames")
    def graph_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @graph_names.setter
    def graph_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class GremlinGraphResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    analytical_storage_ttl: NotRequired[pulumi.Input[_builtins.float]]
    conflict_resolution_policy: NotRequired[pulumi.Input[ConflictResolutionPolicyArgsDict]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    indexing_policy: NotRequired[pulumi.Input[IndexingPolicyArgsDict]]
    partition_key: NotRequired[pulumi.Input[ContainerPartitionKeyArgsDict]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]
    unique_key_policy: NotRequired[pulumi.Input[UniqueKeyPolicyArgsDict]]


@pulumi.input_type
class GremlinGraphResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], analytical_storage_ttl: Optional[pulumi.Input[_builtins.float]] = ..., conflict_resolution_policy: Optional[pulumi.Input[ConflictResolutionPolicyArgs]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., indexing_policy: Optional[pulumi.Input[IndexingPolicyArgs]] = ..., partition_key: Optional[pulumi.Input[ContainerPartitionKeyArgs]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ..., unique_key_policy: Optional[pulumi.Input[UniqueKeyPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[pulumi.Input[ConflictResolutionPolicyArgs]]:
        
        ...
    
    @conflict_resolution_policy.setter
    def conflict_resolution_policy(self, value: Optional[pulumi.Input[ConflictResolutionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional[pulumi.Input[IndexingPolicyArgs]]:
        
        ...
    
    @indexing_policy.setter
    def indexing_policy(self, value: Optional[pulumi.Input[IndexingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[pulumi.Input[ContainerPartitionKeyArgs]]:
        
        ...
    
    @partition_key.setter
    def partition_key(self, value: Optional[pulumi.Input[ContainerPartitionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(self) -> Optional[pulumi.Input[UniqueKeyPolicyArgs]]:
        
        ...
    
    @unique_key_policy.setter
    def unique_key_policy(self, value: Optional[pulumi.Input[UniqueKeyPolicyArgs]]): # -> None:
        ...
    


class IncludedPathArgsDict(TypedDict):
    
    indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[IndexesArgsDict]]]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IncludedPathArgs:
    def __init__(__self__, *, indexes: Optional[pulumi.Input[Sequence[pulumi.Input[IndexesArgs]]]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexesArgs]]]]:
        
        ...
    
    @indexes.setter
    def indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IndexesArgsDict(TypedDict):
    
    data_type: NotRequired[pulumi.Input[Union[_builtins.str, DataType]]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, IndexKind]]]
    precision: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class IndexesArgs:
    def __init__(__self__, *, data_type: Optional[pulumi.Input[Union[_builtins.str, DataType]]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, IndexKind]]] = ..., precision: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DataType]]]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DataType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, IndexKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, IndexKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class IndexingPolicyArgsDict(TypedDict):
    
    automatic: NotRequired[pulumi.Input[_builtins.bool]]
    composite_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[CompositePathArgsDict]]]]]]
    excluded_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExcludedPathArgsDict]]]]
    full_text_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[FullTextIndexPathArgsDict]]]]
    included_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[IncludedPathArgsDict]]]]
    indexing_mode: NotRequired[pulumi.Input[Union[_builtins.str, IndexingMode]]]
    spatial_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpatialSpecArgsDict]]]]
    vector_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[VectorIndexArgsDict]]]]


@pulumi.input_type
class IndexingPolicyArgs:
    def __init__(__self__, *, automatic: Optional[pulumi.Input[_builtins.bool]] = ..., composite_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[CompositePathArgs]]]]]] = ..., excluded_paths: Optional[pulumi.Input[Sequence[pulumi.Input[ExcludedPathArgs]]]] = ..., full_text_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[FullTextIndexPathArgs]]]] = ..., included_paths: Optional[pulumi.Input[Sequence[pulumi.Input[IncludedPathArgs]]]] = ..., indexing_mode: Optional[pulumi.Input[Union[_builtins.str, IndexingMode]]] = ..., spatial_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[SpatialSpecArgs]]]] = ..., vector_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[VectorIndexArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def automatic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeIndexes")
    def composite_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[CompositePathArgs]]]]]]:
        
        ...
    
    @composite_indexes.setter
    def composite_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[CompositePathArgs]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExcludedPathArgs]]]]:
        
        ...
    
    @excluded_paths.setter
    def excluded_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExcludedPathArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextIndexes")
    def full_text_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FullTextIndexPathArgs]]]]:
        
        ...
    
    @full_text_indexes.setter
    def full_text_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FullTextIndexPathArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IncludedPathArgs]]]]:
        
        ...
    
    @included_paths.setter
    def included_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IncludedPathArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, IndexingMode]]]:
        
        ...
    
    @indexing_mode.setter
    def indexing_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, IndexingMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spatialIndexes")
    def spatial_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpatialSpecArgs]]]]:
        
        ...
    
    @spatial_indexes.setter
    def spatial_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpatialSpecArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIndexes")
    def vector_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorIndexArgs]]]]:
        
        ...
    
    @vector_indexes.setter
    def vector_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorIndexArgs]]]]): # -> None:
        ...
    


class IpAddressOrRangeArgsDict(TypedDict):
    
    ip_address_or_range: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpAddressOrRangeArgs:
    def __init__(__self__, *, ip_address_or_range: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressOrRange")
    def ip_address_or_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_or_range.setter
    def ip_address_or_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationArgsDict(TypedDict):
    
    failover_priority: NotRequired[pulumi.Input[_builtins.int]]
    is_zone_redundant: NotRequired[pulumi.Input[_builtins.bool]]
    location_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationArgs:
    def __init__(__self__, *, failover_priority: Optional[pulumi.Input[_builtins.int]] = ..., is_zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ..., location_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverPriority")
    def failover_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failover_priority.setter
    def failover_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_zone_redundant.setter
    def is_zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_name.setter
    def location_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedCassandraManagedServiceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedCassandraResourceIdentityType]]]


@pulumi.input_type
class ManagedCassandraManagedServiceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraResourceIdentityType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraResourceIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedCassandraResourceIdentityType]]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgsDict(TypedDict):
    
    service_type: pulumi.Input[_builtins.str]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_size: NotRequired[pulumi.Input[Union[_builtins.str, ServiceSize]]]


@pulumi.input_type
class MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgs:
    def __init__(__self__, *, service_type: pulumi.Input[_builtins.str], instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_size: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]:
        
        ...
    
    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]): # -> None:
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
    


class MongoDBCollectionResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    analytical_storage_ttl: NotRequired[pulumi.Input[_builtins.int]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[MongoIndexArgsDict]]]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]
    shard_key: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MongoDBCollectionResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], analytical_storage_ttl: Optional[pulumi.Input[_builtins.int]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., indexes: Optional[pulumi.Input[Sequence[pulumi.Input[MongoIndexArgs]]]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ..., shard_key: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MongoIndexArgs]]]]:
        
        ...
    
    @indexes.setter
    def indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MongoIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardKey")
    def shard_key(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @shard_key.setter
    def shard_key(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MongoDBDatabaseResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]


@pulumi.input_type
class MongoDBDatabaseResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    


class MongoIndexKeysArgsDict(TypedDict):
    
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MongoIndexKeysArgs:
    def __init__(__self__, *, keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MongoIndexOptionsArgsDict(TypedDict):
    
    expire_after_seconds: NotRequired[pulumi.Input[_builtins.int]]
    unique: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MongoIndexOptionsArgs:
    def __init__(__self__, *, expire_after_seconds: Optional[pulumi.Input[_builtins.int]] = ..., unique: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireAfterSeconds")
    def expire_after_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expire_after_seconds.setter
    def expire_after_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unique(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @unique.setter
    def unique(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MongoIndexArgsDict(TypedDict):
    
    key: NotRequired[pulumi.Input[MongoIndexKeysArgsDict]]
    options: NotRequired[pulumi.Input[MongoIndexOptionsArgsDict]]


@pulumi.input_type
class MongoIndexArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[MongoIndexKeysArgs]] = ..., options: Optional[pulumi.Input[MongoIndexOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[MongoIndexKeysArgs]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[MongoIndexKeysArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[MongoIndexOptionsArgs]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[MongoIndexOptionsArgs]]): # -> None:
        ...
    


class NodeGroupSpecArgsDict(TypedDict):
    
    disk_size_gb: NotRequired[pulumi.Input[_builtins.float]]
    enable_ha: NotRequired[pulumi.Input[_builtins.bool]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, NodeKind]]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    sku: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NodeGroupSpecArgs:
    def __init__(__self__, *, disk_size_gb: Optional[pulumi.Input[_builtins.float]] = ..., enable_ha: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, NodeKind]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., sku: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ha.setter
    def enable_ha(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, NodeKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, NodeKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PeriodicModeBackupPolicyArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    migration_state: NotRequired[pulumi.Input[BackupPolicyMigrationStateArgsDict]]
    periodic_mode_properties: NotRequired[pulumi.Input[PeriodicModePropertiesArgsDict]]


@pulumi.input_type
class PeriodicModeBackupPolicyArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], migration_state: Optional[pulumi.Input[BackupPolicyMigrationStateArgs]] = ..., periodic_mode_properties: Optional[pulumi.Input[PeriodicModePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> Optional[pulumi.Input[BackupPolicyMigrationStateArgs]]:
        
        ...
    
    @migration_state.setter
    def migration_state(self, value: Optional[pulumi.Input[BackupPolicyMigrationStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodicModeProperties")
    def periodic_mode_properties(self) -> Optional[pulumi.Input[PeriodicModePropertiesArgs]]:
        
        ...
    
    @periodic_mode_properties.setter
    def periodic_mode_properties(self, value: Optional[pulumi.Input[PeriodicModePropertiesArgs]]): # -> None:
        ...
    


class PeriodicModePropertiesArgsDict(TypedDict):
    
    backup_interval_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    backup_retention_interval_in_hours: NotRequired[pulumi.Input[_builtins.int]]
    backup_storage_redundancy: NotRequired[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]]


@pulumi.input_type
class PeriodicModePropertiesArgs:
    def __init__(__self__, *, backup_interval_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., backup_retention_interval_in_hours: Optional[pulumi.Input[_builtins.int]] = ..., backup_storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupIntervalInMinutes")
    def backup_interval_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_interval_in_minutes.setter
    def backup_interval_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionIntervalInHours")
    def backup_retention_interval_in_hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_retention_interval_in_hours.setter
    def backup_retention_interval_in_hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageRedundancy")
    def backup_storage_redundancy(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]]:
        
        ...
    
    @backup_storage_redundancy.setter
    def backup_storage_redundancy(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupStorageRedundancy]]]): # -> None:
        ...
    


class PermissionArgsDict(TypedDict):
    
    data_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    not_data_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PermissionArgs:
    def __init__(__self__, *, data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., not_data_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_actions.setter
    def data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @not_data_actions.setter
    def not_data_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrivateEndpointPropertyArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivilegeResourceArgsDict(TypedDict):
    
    collection: NotRequired[pulumi.Input[_builtins.str]]
    db: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivilegeResourceArgs:
    def __init__(__self__, *, collection: Optional[pulumi.Input[_builtins.str]] = ..., db: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db.setter
    def db(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivilegeArgsDict(TypedDict):
    
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource: NotRequired[pulumi.Input[PrivilegeResourceArgsDict]]


@pulumi.input_type
class PrivilegeArgs:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource: Optional[pulumi.Input[PrivilegeResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[PrivilegeResourceArgs]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[PrivilegeResourceArgs]]): # -> None:
        ...
    


class ResourceRestoreParametersArgsDict(TypedDict):
    
    restore_source: NotRequired[pulumi.Input[_builtins.str]]
    restore_timestamp_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    restore_with_ttl_disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ResourceRestoreParametersArgs:
    def __init__(__self__, *, restore_source: Optional[pulumi.Input[_builtins.str]] = ..., restore_timestamp_in_utc: Optional[pulumi.Input[_builtins.str]] = ..., restore_with_ttl_disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSource")
    def restore_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source.setter
    def restore_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTimestampInUtc")
    def restore_timestamp_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_timestamp_in_utc.setter
    def restore_timestamp_in_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreWithTtlDisabled")
    def restore_with_ttl_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restore_with_ttl_disabled.setter
    def restore_with_ttl_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RestoreParametersArgsDict(TypedDict):
    
    databases_to_restore: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseRestoreResourceArgsDict]]]]
    gremlin_databases_to_restore: NotRequired[pulumi.Input[Sequence[pulumi.Input[GremlinDatabaseRestoreResourceArgsDict]]]]
    restore_mode: NotRequired[pulumi.Input[Union[_builtins.str, RestoreMode]]]
    restore_source: NotRequired[pulumi.Input[_builtins.str]]
    restore_timestamp_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    restore_with_ttl_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    source_backup_location: NotRequired[pulumi.Input[_builtins.str]]
    tables_to_restore: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RestoreParametersArgs:
    def __init__(__self__, *, databases_to_restore: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRestoreResourceArgs]]]] = ..., gremlin_databases_to_restore: Optional[pulumi.Input[Sequence[pulumi.Input[GremlinDatabaseRestoreResourceArgs]]]] = ..., restore_mode: Optional[pulumi.Input[Union[_builtins.str, RestoreMode]]] = ..., restore_source: Optional[pulumi.Input[_builtins.str]] = ..., restore_timestamp_in_utc: Optional[pulumi.Input[_builtins.str]] = ..., restore_with_ttl_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., source_backup_location: Optional[pulumi.Input[_builtins.str]] = ..., tables_to_restore: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToRestore")
    def databases_to_restore(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRestoreResourceArgs]]]]:
        
        ...
    
    @databases_to_restore.setter
    def databases_to_restore(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseRestoreResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gremlinDatabasesToRestore")
    def gremlin_databases_to_restore(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GremlinDatabaseRestoreResourceArgs]]]]:
        
        ...
    
    @gremlin_databases_to_restore.setter
    def gremlin_databases_to_restore(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GremlinDatabaseRestoreResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreMode")
    def restore_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, RestoreMode]]]:
        
        ...
    
    @restore_mode.setter
    def restore_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, RestoreMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSource")
    def restore_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source.setter
    def restore_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTimestampInUtc")
    def restore_timestamp_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_timestamp_in_utc.setter
    def restore_timestamp_in_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreWithTtlDisabled")
    def restore_with_ttl_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restore_with_ttl_disabled.setter
    def restore_with_ttl_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBackupLocation")
    def source_backup_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_backup_location.setter
    def source_backup_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToRestore")
    def tables_to_restore(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tables_to_restore.setter
    def tables_to_restore(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RoleArgsDict(TypedDict):
    
    db: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *, db: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db.setter
    def db(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SeedNodeArgsDict(TypedDict):
    ip_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SeedNodeArgs:
    def __init__(__self__, *, ip_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpatialSpecArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SpatialType]]]]]


@pulumi.input_type
class SpatialSpecArgs:
    def __init__(__self__, *, path: Optional[pulumi.Input[_builtins.str]] = ..., types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SpatialType]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SpatialType]]]]]:
        
        ...
    
    @types.setter
    def types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SpatialType]]]]]): # -> None:
        ...
    


class SqlContainerResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    analytical_storage_ttl: NotRequired[pulumi.Input[_builtins.float]]
    client_encryption_policy: NotRequired[pulumi.Input[ClientEncryptionPolicyArgsDict]]
    computed_properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[ComputedPropertyArgsDict]]]]
    conflict_resolution_policy: NotRequired[pulumi.Input[ConflictResolutionPolicyArgsDict]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    full_text_policy: NotRequired[pulumi.Input[FullTextPolicyArgsDict]]
    indexing_policy: NotRequired[pulumi.Input[IndexingPolicyArgsDict]]
    partition_key: NotRequired[pulumi.Input[ContainerPartitionKeyArgsDict]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]
    unique_key_policy: NotRequired[pulumi.Input[UniqueKeyPolicyArgsDict]]
    vector_embedding_policy: NotRequired[pulumi.Input[VectorEmbeddingPolicyArgsDict]]


@pulumi.input_type
class SqlContainerResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], analytical_storage_ttl: Optional[pulumi.Input[_builtins.float]] = ..., client_encryption_policy: Optional[pulumi.Input[ClientEncryptionPolicyArgs]] = ..., computed_properties: Optional[pulumi.Input[Sequence[pulumi.Input[ComputedPropertyArgs]]]] = ..., conflict_resolution_policy: Optional[pulumi.Input[ConflictResolutionPolicyArgs]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., full_text_policy: Optional[pulumi.Input[FullTextPolicyArgs]] = ..., indexing_policy: Optional[pulumi.Input[IndexingPolicyArgs]] = ..., partition_key: Optional[pulumi.Input[ContainerPartitionKeyArgs]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ..., unique_key_policy: Optional[pulumi.Input[UniqueKeyPolicyArgs]] = ..., vector_embedding_policy: Optional[pulumi.Input[VectorEmbeddingPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientEncryptionPolicy")
    def client_encryption_policy(self) -> Optional[pulumi.Input[ClientEncryptionPolicyArgs]]:
        
        ...
    
    @client_encryption_policy.setter
    def client_encryption_policy(self, value: Optional[pulumi.Input[ClientEncryptionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computedProperties")
    def computed_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ComputedPropertyArgs]]]]:
        
        ...
    
    @computed_properties.setter
    def computed_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ComputedPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[pulumi.Input[ConflictResolutionPolicyArgs]]:
        
        ...
    
    @conflict_resolution_policy.setter
    def conflict_resolution_policy(self, value: Optional[pulumi.Input[ConflictResolutionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullTextPolicy")
    def full_text_policy(self) -> Optional[pulumi.Input[FullTextPolicyArgs]]:
        
        ...
    
    @full_text_policy.setter
    def full_text_policy(self, value: Optional[pulumi.Input[FullTextPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(self) -> Optional[pulumi.Input[IndexingPolicyArgs]]:
        
        ...
    
    @indexing_policy.setter
    def indexing_policy(self, value: Optional[pulumi.Input[IndexingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[pulumi.Input[ContainerPartitionKeyArgs]]:
        
        ...
    
    @partition_key.setter
    def partition_key(self, value: Optional[pulumi.Input[ContainerPartitionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(self) -> Optional[pulumi.Input[UniqueKeyPolicyArgs]]:
        
        ...
    
    @unique_key_policy.setter
    def unique_key_policy(self, value: Optional[pulumi.Input[UniqueKeyPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorEmbeddingPolicy")
    def vector_embedding_policy(self) -> Optional[pulumi.Input[VectorEmbeddingPolicyArgs]]:
        
        ...
    
    @vector_embedding_policy.setter
    def vector_embedding_policy(self, value: Optional[pulumi.Input[VectorEmbeddingPolicyArgs]]): # -> None:
        ...
    


class SqlDatabaseResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]


@pulumi.input_type
class SqlDatabaseResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    


class SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgsDict(TypedDict):
    
    service_type: pulumi.Input[_builtins.str]
    dedicated_gateway_type: NotRequired[pulumi.Input[Union[_builtins.str, DedicatedGatewayType]]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_size: NotRequired[pulumi.Input[Union[_builtins.str, ServiceSize]]]


@pulumi.input_type
class SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgs:
    def __init__(__self__, *, service_type: pulumi.Input[_builtins.str], dedicated_gateway_type: Optional[pulumi.Input[Union[_builtins.str, DedicatedGatewayType]]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_size: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedGatewayType")
    def dedicated_gateway_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DedicatedGatewayType]]]:
        
        ...
    
    @dedicated_gateway_type.setter
    def dedicated_gateway_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DedicatedGatewayType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]:
        
        ...
    
    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceSize]]]): # -> None:
        ...
    


class SqlStoredProcedureResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    body: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlStoredProcedureResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], body: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SqlTriggerResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    body: NotRequired[pulumi.Input[_builtins.str]]
    trigger_operation: NotRequired[pulumi.Input[Union[_builtins.str, TriggerOperation]]]
    trigger_type: NotRequired[pulumi.Input[Union[_builtins.str, TriggerType]]]


@pulumi.input_type
class SqlTriggerResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], body: Optional[pulumi.Input[_builtins.str]] = ..., trigger_operation: Optional[pulumi.Input[Union[_builtins.str, TriggerOperation]]] = ..., trigger_type: Optional[pulumi.Input[Union[_builtins.str, TriggerType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerOperation")
    def trigger_operation(self) -> Optional[pulumi.Input[Union[_builtins.str, TriggerOperation]]]:
        
        ...
    
    @trigger_operation.setter
    def trigger_operation(self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> Optional[pulumi.Input[Union[_builtins.str, TriggerType]]]:
        
        ...
    
    @trigger_type.setter
    def trigger_type(self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerType]]]): # -> None:
        ...
    


class SqlUserDefinedFunctionResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    body: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlUserDefinedFunctionResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], body: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableResourceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    restore_parameters: NotRequired[pulumi.Input[ResourceRestoreParametersArgsDict]]


@pulumi.input_type
class TableResourceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ..., restore_parameters: Optional[pulumi.Input[ResourceRestoreParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[ResourceRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[ResourceRestoreParametersArgs]]): # -> None:
        ...
    


class UniqueKeyPolicyArgsDict(TypedDict):
    
    unique_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[UniqueKeyArgsDict]]]]


@pulumi.input_type
class UniqueKeyPolicyArgs:
    def __init__(__self__, *, unique_keys: Optional[pulumi.Input[Sequence[pulumi.Input[UniqueKeyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeys")
    def unique_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UniqueKeyArgs]]]]:
        
        ...
    
    @unique_keys.setter
    def unique_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UniqueKeyArgs]]]]): # -> None:
        ...
    


class UniqueKeyArgsDict(TypedDict):
    
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UniqueKeyArgs:
    def __init__(__self__, *, paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VectorEmbeddingPolicyArgsDict(TypedDict):
    
    vector_embeddings: NotRequired[pulumi.Input[Sequence[pulumi.Input[VectorEmbeddingArgsDict]]]]


@pulumi.input_type
class VectorEmbeddingPolicyArgs:
    def __init__(__self__, *, vector_embeddings: Optional[pulumi.Input[Sequence[pulumi.Input[VectorEmbeddingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorEmbeddings")
    def vector_embeddings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VectorEmbeddingArgs]]]]:
        
        ...
    
    @vector_embeddings.setter
    def vector_embeddings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VectorEmbeddingArgs]]]]): # -> None:
        ...
    


class VectorEmbeddingArgsDict(TypedDict):
    
    data_type: pulumi.Input[Union[_builtins.str, VectorDataType]]
    dimensions: pulumi.Input[_builtins.int]
    distance_function: pulumi.Input[Union[_builtins.str, DistanceFunction]]
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class VectorEmbeddingArgs:
    def __init__(__self__, *, data_type: pulumi.Input[Union[_builtins.str, VectorDataType]], dimensions: pulumi.Input[_builtins.int], distance_function: pulumi.Input[Union[_builtins.str, DistanceFunction]], path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[Union[_builtins.str, VectorDataType]]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: pulumi.Input[Union[_builtins.str, VectorDataType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @dimensions.setter
    def dimensions(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distanceFunction")
    def distance_function(self) -> pulumi.Input[Union[_builtins.str, DistanceFunction]]:
        
        ...
    
    @distance_function.setter
    def distance_function(self, value: pulumi.Input[Union[_builtins.str, DistanceFunction]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VectorIndexArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, VectorIndexType]]
    indexing_search_list_size: NotRequired[pulumi.Input[_builtins.float]]
    quantization_byte_size: NotRequired[pulumi.Input[_builtins.float]]
    vector_index_shard_key: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VectorIndexArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], type: pulumi.Input[Union[_builtins.str, VectorIndexType]], indexing_search_list_size: Optional[pulumi.Input[_builtins.float]] = ..., quantization_byte_size: Optional[pulumi.Input[_builtins.float]] = ..., vector_index_shard_key: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, VectorIndexType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, VectorIndexType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexingSearchListSize")
    def indexing_search_list_size(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @indexing_search_list_size.setter
    def indexing_search_list_size(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quantizationByteSize")
    def quantization_byte_size(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @quantization_byte_size.setter
    def quantization_byte_size(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorIndexShardKey")
    def vector_index_shard_key(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vector_index_shard_key.setter
    def vector_index_shard_key(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VirtualNetworkRuleArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    ignore_missing_v_net_service_endpoint: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., ignore_missing_v_net_service_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVNetServiceEndpoint")
    def ignore_missing_v_net_service_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_missing_v_net_service_endpoint.setter
    def ignore_missing_v_net_service_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


