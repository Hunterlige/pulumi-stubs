

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureActiveDirectoryAppArgs', 'AzureActiveDirectoryAppArgsDict', 'AzureBlobArgs', 'AzureBlobArgsDict', 'BackupConfigurationArgs', 'BackupConfigurationArgsDict', 'BlobShareArgs', 'BlobShareArgsDict', 'ConnectToMongoDbTaskPropertiesArgs', 'ConnectToMongoDbTaskPropertiesArgsDict', 'ConnectToSourceMySqlTaskInputArgs', 'ConnectToSourceMySqlTaskInputArgsDict', 'ConnectToSourceMySqlTaskPropertiesArgs', 'ConnectToSourceMySqlTaskPropertiesArgsDict', 'ConnectToSourceOracleSyncTaskInputArgs', 'ConnectToSourceOracleSyncTaskInputArgsDict', 'ConnectToSourceOracleSyncTaskPropertiesArgs', 'ConnectToSourceOracleSyncTaskPropertiesArgsDict', 'ConnectToSourcePostgreSqlSyncTaskInputArgs', 'ConnectToSourcePostgreSqlSyncTaskInputArgsDict', 'ConnectToSourcePostgreSqlSyncTaskPropertiesArgs', ..., 'ConnectToSourceSqlServerSyncTaskPropertiesArgs', 'ConnectToSourceSqlServerSyncTaskPropertiesArgsDict', 'ConnectToSourceSqlServerTaskInputArgs', 'ConnectToSourceSqlServerTaskInputArgsDict', 'ConnectToSourceSqlServerTaskPropertiesArgs', 'ConnectToSourceSqlServerTaskPropertiesArgsDict', 'ConnectToTargetAzureDbForMySqlTaskInputArgs', 'ConnectToTargetAzureDbForMySqlTaskInputArgsDict', 'ConnectToTargetAzureDbForMySqlTaskPropertiesArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ConnectToTargetSqlDbTaskInputArgs', 'ConnectToTargetSqlDbTaskInputArgsDict', 'ConnectToTargetSqlDbTaskPropertiesArgs', 'ConnectToTargetSqlDbTaskPropertiesArgsDict', 'ConnectToTargetSqlMISyncTaskInputArgs', 'ConnectToTargetSqlMISyncTaskInputArgsDict', 'ConnectToTargetSqlMISyncTaskPropertiesArgs', 'ConnectToTargetSqlMISyncTaskPropertiesArgsDict', 'ConnectToTargetSqlMITaskInputArgs', 'ConnectToTargetSqlMITaskInputArgsDict', 'ConnectToTargetSqlMITaskPropertiesArgs', 'ConnectToTargetSqlMITaskPropertiesArgsDict', 'ConnectToTargetSqlSqlDbSyncTaskInputArgs', 'ConnectToTargetSqlSqlDbSyncTaskInputArgsDict', 'ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs', 'ConnectToTargetSqlSqlDbSyncTaskPropertiesArgsDict', 'DatabaseInfoArgs', 'DatabaseInfoArgsDict', 'DatabaseMigrationPropertiesSqlDbArgs', 'DatabaseMigrationPropertiesSqlDbArgsDict', 'DatabaseMigrationPropertiesSqlMiArgs', 'DatabaseMigrationPropertiesSqlMiArgsDict', 'DatabaseMigrationPropertiesSqlVmArgs', 'DatabaseMigrationPropertiesSqlVmArgsDict', 'FileShareArgs', 'FileShareArgsDict', 'GetTdeCertificatesSqlTaskInputArgs', 'GetTdeCertificatesSqlTaskInputArgsDict', 'GetTdeCertificatesSqlTaskPropertiesArgs', 'GetTdeCertificatesSqlTaskPropertiesArgsDict', 'GetUserTablesMySqlTaskInputArgs', 'GetUserTablesMySqlTaskInputArgsDict', 'GetUserTablesMySqlTaskPropertiesArgs', 'GetUserTablesMySqlTaskPropertiesArgsDict', 'GetUserTablesOracleTaskInputArgs', 'GetUserTablesOracleTaskInputArgsDict', 'GetUserTablesOracleTaskPropertiesArgs', 'GetUserTablesOracleTaskPropertiesArgsDict', 'GetUserTablesPostgreSqlTaskInputArgs', 'GetUserTablesPostgreSqlTaskInputArgsDict', 'GetUserTablesPostgreSqlTaskPropertiesArgs', 'GetUserTablesPostgreSqlTaskPropertiesArgsDict', 'GetUserTablesSqlSyncTaskInputArgs', 'GetUserTablesSqlSyncTaskInputArgsDict', 'GetUserTablesSqlSyncTaskPropertiesArgs', 'GetUserTablesSqlSyncTaskPropertiesArgsDict', 'GetUserTablesSqlTaskInputArgs', 'GetUserTablesSqlTaskInputArgsDict', 'GetUserTablesSqlTaskPropertiesArgs', 'GetUserTablesSqlTaskPropertiesArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MiSqlConnectionInfoArgs', 'MiSqlConnectionInfoArgsDict', 'MigrateMongoDbTaskPropertiesArgs', 'MigrateMongoDbTaskPropertiesArgsDict', ..., ..., 'MigrateMySqlAzureDbForMySqlOfflineTaskInputArgs', ..., ..., ..., 'MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgs', ..., 'MigrateMySqlAzureDbForMySqlSyncTaskInputArgs', 'MigrateMySqlAzureDbForMySqlSyncTaskInputArgsDict', 'MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs', ..., ..., ..., ..., ..., 'MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'MigrateSqlServerSqlDbDatabaseInputArgs', 'MigrateSqlServerSqlDbDatabaseInputArgsDict', 'MigrateSqlServerSqlDbSyncDatabaseInputArgs', 'MigrateSqlServerSqlDbSyncDatabaseInputArgsDict', 'MigrateSqlServerSqlDbSyncTaskInputArgs', 'MigrateSqlServerSqlDbSyncTaskInputArgsDict', 'MigrateSqlServerSqlDbSyncTaskPropertiesArgs', 'MigrateSqlServerSqlDbSyncTaskPropertiesArgsDict', 'MigrateSqlServerSqlDbTaskInputArgs', 'MigrateSqlServerSqlDbTaskInputArgsDict', 'MigrateSqlServerSqlDbTaskPropertiesArgs', 'MigrateSqlServerSqlDbTaskPropertiesArgsDict', 'MigrateSqlServerSqlMIDatabaseInputArgs', 'MigrateSqlServerSqlMIDatabaseInputArgsDict', 'MigrateSqlServerSqlMISyncTaskInputArgs', 'MigrateSqlServerSqlMISyncTaskInputArgsDict', 'MigrateSqlServerSqlMISyncTaskPropertiesArgs', 'MigrateSqlServerSqlMISyncTaskPropertiesArgsDict', 'MigrateSqlServerSqlMITaskInputArgs', 'MigrateSqlServerSqlMITaskInputArgsDict', 'MigrateSqlServerSqlMITaskPropertiesArgs', 'MigrateSqlServerSqlMITaskPropertiesArgsDict', 'MigrateSsisTaskInputArgs', 'MigrateSsisTaskInputArgsDict', 'MigrateSsisTaskPropertiesArgs', 'MigrateSsisTaskPropertiesArgsDict', 'MigrationValidationOptionsArgs', 'MigrationValidationOptionsArgsDict', 'MongoConnectionInformationArgs', 'MongoConnectionInformationArgsDict', 'MongoDbCollectionSettingsArgs', 'MongoDbCollectionSettingsArgsDict', 'MongoDbConnectionInfoArgs', 'MongoDbConnectionInfoArgsDict', 'MongoDbDatabaseSettingsArgs', 'MongoDbDatabaseSettingsArgsDict', 'MongoDbMigrationSettingsArgs', 'MongoDbMigrationSettingsArgsDict', 'MongoDbShardKeyFieldArgs', 'MongoDbShardKeyFieldArgsDict', 'MongoDbShardKeySettingArgs', 'MongoDbShardKeySettingArgsDict', 'MongoDbThrottlingSettingsArgs', 'MongoDbThrottlingSettingsArgsDict', 'MongoMigrationCollectionArgs', 'MongoMigrationCollectionArgsDict', 'MySqlConnectionInfoArgs', 'MySqlConnectionInfoArgsDict', 'OfflineConfigurationArgs', 'OfflineConfigurationArgsDict', 'OracleConnectionInfoArgs', 'OracleConnectionInfoArgsDict', 'PostgreSqlConnectionInfoArgs', 'PostgreSqlConnectionInfoArgsDict', 'ProjectFilePropertiesArgs', 'ProjectFilePropertiesArgsDict', 'SelectedCertificateInputArgs', 'SelectedCertificateInputArgsDict', 'ServiceSkuArgs', 'ServiceSkuArgsDict', 'SourceLocationArgs', 'SourceLocationArgsDict', 'SqlConnectionInformationArgs', 'SqlConnectionInformationArgsDict', 'SqlConnectionInfoArgs', 'SqlConnectionInfoArgsDict', 'SqlFileShareArgs', 'SqlFileShareArgsDict', 'SsisMigrationInfoArgs', 'SsisMigrationInfoArgsDict', 'TargetLocationArgs', 'TargetLocationArgsDict', ..., ..., ..., ..., ..., ..., 'ValidateMigrationInputSqlServerSqlMITaskInputArgs', ..., ..., ..., 'ValidateMongoDbTaskPropertiesArgs', 'ValidateMongoDbTaskPropertiesArgsDict', ..., ..., 'ValidateSyncMigrationInputSqlServerTaskInputArgs', ...]
class AzureActiveDirectoryAppArgsDict(TypedDict):
    
    app_key: NotRequired[pulumi.Input[_builtins.str]]
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    ignore_azure_permissions: NotRequired[pulumi.Input[_builtins.bool]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureActiveDirectoryAppArgs:
    def __init__(__self__, *, app_key: Optional[pulumi.Input[_builtins.str]] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., ignore_azure_permissions: Optional[pulumi.Input[_builtins.bool]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appKey")
    def app_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_key.setter
    def app_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreAzurePermissions")
    def ignore_azure_permissions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_azure_permissions.setter
    def ignore_azure_permissions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureBlobArgsDict(TypedDict):
    
    account_key: NotRequired[pulumi.Input[_builtins.str]]
    auth_type: NotRequired[pulumi.Input[AuthType]]
    blob_container_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[ManagedServiceIdentityArgsDict]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureBlobArgs:
    def __init__(__self__, *, account_key: Optional[pulumi.Input[_builtins.str]] = ..., auth_type: Optional[pulumi.Input[AuthType]] = ..., blob_container_name: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[AuthType]]:
        
        ...
    
    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[AuthType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_container_name.setter
    def blob_container_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BackupConfigurationArgsDict(TypedDict):
    
    source_location: NotRequired[pulumi.Input[SourceLocationArgsDict]]
    target_location: NotRequired[pulumi.Input[TargetLocationArgsDict]]


@pulumi.input_type
class BackupConfigurationArgs:
    def __init__(__self__, *, source_location: Optional[pulumi.Input[SourceLocationArgs]] = ..., target_location: Optional[pulumi.Input[TargetLocationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[SourceLocationArgs]]:
        
        ...
    
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[SourceLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> Optional[pulumi.Input[TargetLocationArgs]]:
        
        ...
    
    @target_location.setter
    def target_location(self, value: Optional[pulumi.Input[TargetLocationArgs]]): # -> None:
        ...
    


class BlobShareArgsDict(TypedDict):
    
    sas_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BlobShareArgs:
    def __init__(__self__, *, sas_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasUri")
    def sas_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_uri.setter
    def sas_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectToMongoDbTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MongoDbConnectionInfoArgsDict]]


@pulumi.input_type
class ConnectToMongoDbTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MongoDbConnectionInfoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MongoDbConnectionInfoArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MongoDbConnectionInfoArgs]]): # -> None:
        ...
    


class ConnectToSourceMySqlTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    check_permissions_group: NotRequired[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]
    is_offline_migration: NotRequired[pulumi.Input[_builtins.bool]]
    target_platform: NotRequired[pulumi.Input[Union[_builtins.str, MySqlTargetPlatformType]]]


@pulumi.input_type
class ConnectToSourceMySqlTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[MySqlConnectionInfoArgs], check_permissions_group: Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]] = ..., is_offline_migration: Optional[pulumi.Input[_builtins.bool]] = ..., target_platform: Optional[pulumi.Input[Union[_builtins.str, MySqlTargetPlatformType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkPermissionsGroup")
    def check_permissions_group(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]:
        
        ...
    
    @check_permissions_group.setter
    def check_permissions_group(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOfflineMigration")
    def is_offline_migration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_offline_migration.setter
    def is_offline_migration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> Optional[pulumi.Input[Union[_builtins.str, MySqlTargetPlatformType]]]:
        
        ...
    
    @target_platform.setter
    def target_platform(self, value: Optional[pulumi.Input[Union[_builtins.str, MySqlTargetPlatformType]]]): # -> None:
        ...
    


class ConnectToSourceMySqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToSourceMySqlTaskInputArgsDict]]


@pulumi.input_type
class ConnectToSourceMySqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToSourceMySqlTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToSourceMySqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToSourceMySqlTaskInputArgs]]): # -> None:
        ...
    


class ConnectToSourceOracleSyncTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[OracleConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToSourceOracleSyncTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[OracleConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[OracleConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[OracleConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToSourceOracleSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToSourceOracleSyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToSourceOracleSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToSourceOracleSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToSourceOracleSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToSourceOracleSyncTaskInputArgs]]): # -> None:
        ...
    


class ConnectToSourcePostgreSqlSyncTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToSourcePostgreSqlSyncTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToSourcePostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToSourcePostgreSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToSourcePostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToSourcePostgreSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToSourcePostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToSourcePostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class ConnectToSourceSqlServerSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToSourceSqlServerTaskInputArgsDict]]


@pulumi.input_type
class ConnectToSourceSqlServerSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]]): # -> None:
        ...
    


class ConnectToSourceSqlServerTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    check_permissions_group: NotRequired[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]
    collect_agent_jobs: NotRequired[pulumi.Input[_builtins.bool]]
    collect_databases: NotRequired[pulumi.Input[_builtins.bool]]
    collect_logins: NotRequired[pulumi.Input[_builtins.bool]]
    collect_tde_certificate_info: NotRequired[pulumi.Input[_builtins.bool]]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]
    validate_ssis_catalog_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectToSourceSqlServerTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[SqlConnectionInfoArgs], check_permissions_group: Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]] = ..., collect_agent_jobs: Optional[pulumi.Input[_builtins.bool]] = ..., collect_databases: Optional[pulumi.Input[_builtins.bool]] = ..., collect_logins: Optional[pulumi.Input[_builtins.bool]] = ..., collect_tde_certificate_info: Optional[pulumi.Input[_builtins.bool]] = ..., encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ..., validate_ssis_catalog_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkPermissionsGroup")
    def check_permissions_group(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]:
        
        ...
    
    @check_permissions_group.setter
    def check_permissions_group(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerLevelPermissionsGroup]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectAgentJobs")
    def collect_agent_jobs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_agent_jobs.setter
    def collect_agent_jobs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectDatabases")
    def collect_databases(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_databases.setter
    def collect_databases(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectLogins")
    def collect_logins(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_logins.setter
    def collect_logins(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectTdeCertificateInfo")
    def collect_tde_certificate_info(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_tde_certificate_info.setter
    def collect_tde_certificate_info(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsisCatalogOnly")
    def validate_ssis_catalog_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_ssis_catalog_only.setter
    def validate_ssis_catalog_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectToSourceSqlServerTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToSourceSqlServerTaskInputArgsDict]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectToSourceSqlServerTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToSourceSqlServerTaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectToTargetAzureDbForMySqlTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    is_offline_migration: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectToTargetAzureDbForMySqlTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[MySqlConnectionInfoArgs], target_connection_info: pulumi.Input[MySqlConnectionInfoArgs], is_offline_migration: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOfflineMigration")
    def is_offline_migration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_offline_migration.setter
    def is_offline_migration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectToTargetAzureDbForMySqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetAzureDbForMySqlTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetAzureDbForMySqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetAzureDbForMySqlTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetAzureDbForMySqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetAzureDbForMySqlTaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs], target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetAzureDbForPostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgsDict(TypedDict):
    
    target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgs:
    def __init__(__self__, *, target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetSqlDbTaskInputArgsDict(TypedDict):
    
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    query_object_counts: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectToTargetSqlDbTaskInputArgs:
    def __init__(__self__, *, target_connection_info: pulumi.Input[SqlConnectionInfoArgs], query_object_counts: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryObjectCounts")
    def query_object_counts(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @query_object_counts.setter
    def query_object_counts(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectToTargetSqlDbTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    created_on: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[ConnectToTargetSqlDbTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetSqlDbTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., created_on: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[ConnectToTargetSqlDbTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetSqlDbTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetSqlDbTaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetSqlMISyncTaskInputArgsDict(TypedDict):
    
    azure_app: pulumi.Input[AzureActiveDirectoryAppArgsDict]
    target_connection_info: pulumi.Input[MiSqlConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToTargetSqlMISyncTaskInputArgs:
    def __init__(__self__, *, azure_app: pulumi.Input[AzureActiveDirectoryAppArgs], target_connection_info: pulumi.Input[MiSqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> pulumi.Input[AzureActiveDirectoryAppArgs]:
        
        ...
    
    @azure_app.setter
    def azure_app(self, value: pulumi.Input[AzureActiveDirectoryAppArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MiSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MiSqlConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToTargetSqlMISyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetSqlMISyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetSqlMISyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetSqlMISyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetSqlMISyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetSqlMISyncTaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetSqlMITaskInputArgsDict(TypedDict):
    
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    collect_agent_jobs: NotRequired[pulumi.Input[_builtins.bool]]
    collect_logins: NotRequired[pulumi.Input[_builtins.bool]]
    validate_ssis_catalog_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectToTargetSqlMITaskInputArgs:
    def __init__(__self__, *, target_connection_info: pulumi.Input[SqlConnectionInfoArgs], collect_agent_jobs: Optional[pulumi.Input[_builtins.bool]] = ..., collect_logins: Optional[pulumi.Input[_builtins.bool]] = ..., validate_ssis_catalog_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectAgentJobs")
    def collect_agent_jobs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_agent_jobs.setter
    def collect_agent_jobs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectLogins")
    def collect_logins(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @collect_logins.setter
    def collect_logins(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsisCatalogOnly")
    def validate_ssis_catalog_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_ssis_catalog_only.setter
    def validate_ssis_catalog_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectToTargetSqlMITaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetSqlMITaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetSqlMITaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetSqlMITaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetSqlMITaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetSqlMITaskInputArgs]]): # -> None:
        ...
    


class ConnectToTargetSqlSqlDbSyncTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]


@pulumi.input_type
class ConnectToTargetSqlSqlDbSyncTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    


class ConnectToTargetSqlSqlDbSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ConnectToTargetSqlSqlDbSyncTaskInputArgsDict]]


@pulumi.input_type
class ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ConnectToTargetSqlSqlDbSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ConnectToTargetSqlSqlDbSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ConnectToTargetSqlSqlDbSyncTaskInputArgs]]): # -> None:
        ...
    


class DatabaseInfoArgsDict(TypedDict):
    
    source_database_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class DatabaseInfoArgs:
    def __init__(__self__, *, source_database_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_database_name.setter
    def source_database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DatabaseMigrationPropertiesSqlDbArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    migration_operation_id: NotRequired[pulumi.Input[_builtins.str]]
    migration_service: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_error: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    source_database_name: NotRequired[pulumi.Input[_builtins.str]]
    source_sql_connection: NotRequired[pulumi.Input[SqlConnectionInformationArgsDict]]
    table_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target_database_collation: NotRequired[pulumi.Input[_builtins.str]]
    target_sql_connection: NotRequired[pulumi.Input[SqlConnectionInformationArgsDict]]


@pulumi.input_type
class DatabaseMigrationPropertiesSqlDbArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], migration_operation_id: Optional[pulumi.Input[_builtins.str]] = ..., migration_service: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_error: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., source_database_name: Optional[pulumi.Input[_builtins.str]] = ..., source_sql_connection: Optional[pulumi.Input[SqlConnectionInformationArgs]] = ..., table_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_database_collation: Optional[pulumi.Input[_builtins.str]] = ..., target_sql_connection: Optional[pulumi.Input[SqlConnectionInformationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_operation_id.setter
    def migration_operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_service.setter
    def migration_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_error.setter
    def provisioning_error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_database_name.setter
    def source_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[pulumi.Input[SqlConnectionInformationArgs]]:
        
        ...
    
    @source_sql_connection.setter
    def source_sql_connection(self, value: Optional[pulumi.Input[SqlConnectionInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableList")
    def table_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_list.setter
    def table_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_collation.setter
    def target_database_collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSqlConnection")
    def target_sql_connection(self) -> Optional[pulumi.Input[SqlConnectionInformationArgs]]:
        
        ...
    
    @target_sql_connection.setter
    def target_sql_connection(self, value: Optional[pulumi.Input[SqlConnectionInformationArgs]]): # -> None:
        ...
    


class DatabaseMigrationPropertiesSqlMiArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    backup_configuration: NotRequired[pulumi.Input[BackupConfigurationArgsDict]]
    migration_operation_id: NotRequired[pulumi.Input[_builtins.str]]
    migration_service: NotRequired[pulumi.Input[_builtins.str]]
    offline_configuration: NotRequired[pulumi.Input[OfflineConfigurationArgsDict]]
    provisioning_error: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    source_database_name: NotRequired[pulumi.Input[_builtins.str]]
    source_sql_connection: NotRequired[pulumi.Input[SqlConnectionInformationArgsDict]]
    target_database_collation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseMigrationPropertiesSqlMiArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], backup_configuration: Optional[pulumi.Input[BackupConfigurationArgs]] = ..., migration_operation_id: Optional[pulumi.Input[_builtins.str]] = ..., migration_service: Optional[pulumi.Input[_builtins.str]] = ..., offline_configuration: Optional[pulumi.Input[OfflineConfigurationArgs]] = ..., provisioning_error: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., source_database_name: Optional[pulumi.Input[_builtins.str]] = ..., source_sql_connection: Optional[pulumi.Input[SqlConnectionInformationArgs]] = ..., target_database_collation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[pulumi.Input[BackupConfigurationArgs]]:
        
        ...
    
    @backup_configuration.setter
    def backup_configuration(self, value: Optional[pulumi.Input[BackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_operation_id.setter
    def migration_operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_service.setter
    def migration_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineConfiguration")
    def offline_configuration(self) -> Optional[pulumi.Input[OfflineConfigurationArgs]]:
        
        ...
    
    @offline_configuration.setter
    def offline_configuration(self, value: Optional[pulumi.Input[OfflineConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_error.setter
    def provisioning_error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_database_name.setter
    def source_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[pulumi.Input[SqlConnectionInformationArgs]]:
        
        ...
    
    @source_sql_connection.setter
    def source_sql_connection(self, value: Optional[pulumi.Input[SqlConnectionInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_collation.setter
    def target_database_collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseMigrationPropertiesSqlVmArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    backup_configuration: NotRequired[pulumi.Input[BackupConfigurationArgsDict]]
    migration_operation_id: NotRequired[pulumi.Input[_builtins.str]]
    migration_service: NotRequired[pulumi.Input[_builtins.str]]
    offline_configuration: NotRequired[pulumi.Input[OfflineConfigurationArgsDict]]
    provisioning_error: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    source_database_name: NotRequired[pulumi.Input[_builtins.str]]
    source_sql_connection: NotRequired[pulumi.Input[SqlConnectionInformationArgsDict]]
    target_database_collation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseMigrationPropertiesSqlVmArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], backup_configuration: Optional[pulumi.Input[BackupConfigurationArgs]] = ..., migration_operation_id: Optional[pulumi.Input[_builtins.str]] = ..., migration_service: Optional[pulumi.Input[_builtins.str]] = ..., offline_configuration: Optional[pulumi.Input[OfflineConfigurationArgs]] = ..., provisioning_error: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., source_database_name: Optional[pulumi.Input[_builtins.str]] = ..., source_sql_connection: Optional[pulumi.Input[SqlConnectionInformationArgs]] = ..., target_database_collation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[pulumi.Input[BackupConfigurationArgs]]:
        
        ...
    
    @backup_configuration.setter
    def backup_configuration(self, value: Optional[pulumi.Input[BackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_operation_id.setter
    def migration_operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_service.setter
    def migration_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineConfiguration")
    def offline_configuration(self) -> Optional[pulumi.Input[OfflineConfigurationArgs]]:
        
        ...
    
    @offline_configuration.setter
    def offline_configuration(self, value: Optional[pulumi.Input[OfflineConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_error.setter
    def provisioning_error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_database_name.setter
    def source_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[pulumi.Input[SqlConnectionInformationArgs]]:
        
        ...
    
    @source_sql_connection.setter
    def source_sql_connection(self, value: Optional[pulumi.Input[SqlConnectionInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_collation.setter
    def target_database_collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FileShareArgsDict(TypedDict):
    
    path: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FileShareArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    


class GetTdeCertificatesSqlTaskInputArgsDict(TypedDict):
    
    backup_file_share: pulumi.Input[FileShareArgsDict]
    connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    selected_certificates: pulumi.Input[Sequence[pulumi.Input[SelectedCertificateInputArgsDict]]]


@pulumi.input_type
class GetTdeCertificatesSqlTaskInputArgs:
    def __init__(__self__, *, backup_file_share: pulumi.Input[FileShareArgs], connection_info: pulumi.Input[SqlConnectionInfoArgs], selected_certificates: pulumi.Input[Sequence[pulumi.Input[SelectedCertificateInputArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> pulumi.Input[FileShareArgs]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: pulumi.Input[FileShareArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @connection_info.setter
    def connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedCertificates")
    def selected_certificates(self) -> pulumi.Input[Sequence[pulumi.Input[SelectedCertificateInputArgs]]]:
        
        ...
    
    @selected_certificates.setter
    def selected_certificates(self, value: pulumi.Input[Sequence[pulumi.Input[SelectedCertificateInputArgs]]]): # -> None:
        ...
    


class GetTdeCertificatesSqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetTdeCertificatesSqlTaskInputArgsDict]]


@pulumi.input_type
class GetTdeCertificatesSqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetTdeCertificatesSqlTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetTdeCertificatesSqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetTdeCertificatesSqlTaskInputArgs]]): # -> None:
        ...
    


class GetUserTablesMySqlTaskInputArgsDict(TypedDict):
    
    connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class GetUserTablesMySqlTaskInputArgs:
    def __init__(__self__, *, connection_info: pulumi.Input[MySqlConnectionInfoArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @connection_info.setter
    def connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class GetUserTablesMySqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetUserTablesMySqlTaskInputArgsDict]]


@pulumi.input_type
class GetUserTablesMySqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetUserTablesMySqlTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetUserTablesMySqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetUserTablesMySqlTaskInputArgs]]): # -> None:
        ...
    


class GetUserTablesOracleTaskInputArgsDict(TypedDict):
    
    connection_info: pulumi.Input[OracleConnectionInfoArgsDict]
    selected_schemas: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class GetUserTablesOracleTaskInputArgs:
    def __init__(__self__, *, connection_info: pulumi.Input[OracleConnectionInfoArgs], selected_schemas: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> pulumi.Input[OracleConnectionInfoArgs]:
        
        ...
    
    @connection_info.setter
    def connection_info(self, value: pulumi.Input[OracleConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSchemas")
    def selected_schemas(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_schemas.setter
    def selected_schemas(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class GetUserTablesOracleTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetUserTablesOracleTaskInputArgsDict]]


@pulumi.input_type
class GetUserTablesOracleTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetUserTablesOracleTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetUserTablesOracleTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetUserTablesOracleTaskInputArgs]]): # -> None:
        ...
    


class GetUserTablesPostgreSqlTaskInputArgsDict(TypedDict):
    
    connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class GetUserTablesPostgreSqlTaskInputArgs:
    def __init__(__self__, *, connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @connection_info.setter
    def connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class GetUserTablesPostgreSqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetUserTablesPostgreSqlTaskInputArgsDict]]


@pulumi.input_type
class GetUserTablesPostgreSqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetUserTablesPostgreSqlTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetUserTablesPostgreSqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetUserTablesPostgreSqlTaskInputArgs]]): # -> None:
        ...
    


class GetUserTablesSqlSyncTaskInputArgsDict(TypedDict):
    
    selected_source_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    selected_target_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]


@pulumi.input_type
class GetUserTablesSqlSyncTaskInputArgs:
    def __init__(__self__, *, selected_source_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], selected_target_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSourceDatabases")
    def selected_source_databases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_source_databases.setter
    def selected_source_databases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTargetDatabases")
    def selected_target_databases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_target_databases.setter
    def selected_target_databases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    


class GetUserTablesSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetUserTablesSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class GetUserTablesSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetUserTablesSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetUserTablesSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetUserTablesSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class GetUserTablesSqlTaskInputArgsDict(TypedDict):
    
    connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GetUserTablesSqlTaskInputArgs:
    def __init__(__self__, *, connection_info: pulumi.Input[SqlConnectionInfoArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @connection_info.setter
    def connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GetUserTablesSqlTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[GetUserTablesSqlTaskInputArgsDict]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GetUserTablesSqlTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[GetUserTablesSqlTaskInputArgs]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[GetUserTablesSqlTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[GetUserTablesSqlTaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


class MiSqlConnectionInfoArgsDict(TypedDict):
    
    managed_instance_resource_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MiSqlConnectionInfoArgs:
    def __init__(__self__, *, managed_instance_resource_id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceResourceId")
    def managed_instance_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_instance_resource_id.setter
    def managed_instance_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


class MigrateMongoDbTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MongoDbMigrationSettingsArgsDict]]


@pulumi.input_type
class MigrateMongoDbTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MongoDbMigrationSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MongoDbMigrationSettingsArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MongoDbMigrationSettingsArgs]]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    table_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., table_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_map.setter
    def table_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlOfflineTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]
    make_source_server_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    optional_agent_settings: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    started_on: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlOfflineTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgs]]], source_connection_info: pulumi.Input[MySqlConnectionInfoArgs], target_connection_info: pulumi.Input[MySqlConnectionInfoArgs], encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ..., make_source_server_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., optional_agent_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., started_on: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="makeSourceServerReadOnly")
    def make_source_server_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @make_source_server_read_only.setter
    def make_source_server_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalAgentSettings")
    def optional_agent_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @optional_agent_settings.setter
    def optional_agent_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @started_on.setter
    def started_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineTaskInputArgsDict]]
    is_cloneable: NotRequired[pulumi.Input[_builtins.bool]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineTaskInputArgs]] = ..., is_cloneable: Optional[pulumi.Input[_builtins.bool]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlOfflineTaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_cloneable.setter
    def is_cloneable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgsDict(TypedDict):
    
    migration_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    table_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]
    target_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgs:
    def __init__(__self__, *, migration_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., source_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., table_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ..., target_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @migration_setting.setter
    def migration_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_setting.setter
    def source_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_map.setter
    def table_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_setting.setter
    def target_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlSyncTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[MySqlConnectionInfoArgsDict]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlSyncTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgs]]], source_connection_info: pulumi.Input[MySqlConnectionInfoArgs], target_connection_info: pulumi.Input[MySqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MySqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MySqlConnectionInfoArgs]): # -> None:
        ...
    


class MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncTaskInputArgsDict]]


@pulumi.input_type
class MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateMySqlAzureDbForMySqlSyncTaskInputArgs]]): # -> None:
        ...
    


class MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgsDict(TypedDict):
    
    case_manipulation: NotRequired[pulumi.Input[_builtins.str]]
    migration_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schema_name: NotRequired[pulumi.Input[_builtins.str]]
    source_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    table_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]
    target_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgs:
    def __init__(__self__, *, case_manipulation: Optional[pulumi.Input[_builtins.str]] = ..., migration_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., source_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., table_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ..., target_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseManipulation")
    def case_manipulation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @case_manipulation.setter
    def case_manipulation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @migration_setting.setter
    def migration_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_setting.setter
    def source_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_map.setter
    def table_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_setting.setter
    def target_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MigrateOracleAzureDbPostgreSqlSyncTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[OracleConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]


@pulumi.input_type
class MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgs]]], source_connection_info: pulumi.Input[OracleConnectionInfoArgs], target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[OracleConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[OracleConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    


class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgsDict(TypedDict):
    
    migration_setting: NotRequired[Any]
    name: NotRequired[pulumi.Input[_builtins.str]]
    selected_tables: NotRequired[pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgsDict]]]]
    source_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]
    target_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgs:
    def __init__(__self__, *, migration_setting: Optional[Any] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., selected_tables: Optional[pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgs]]]] = ..., source_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ..., target_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[Any]:
        
        ...
    
    @migration_setting.setter
    def migration_setting(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTables")
    def selected_tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgs]]]]:
        
        ...
    
    @selected_tables.setter
    def selected_tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_setting.setter
    def source_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_setting.setter
    def target_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgsDict]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgs]]], source_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs], target_connection_info: pulumi.Input[PostgreSqlConnectionInfoArgs], encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[PostgreSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[PostgreSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    created_on: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgsDict]]
    is_cloneable: NotRequired[pulumi.Input[_builtins.bool]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., created_on: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgs]] = ..., is_cloneable: Optional[pulumi.Input[_builtins.bool]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_cloneable.setter
    def is_cloneable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbDatabaseInputArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    make_source_db_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schema_setting: NotRequired[Any]
    table_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateSqlServerSqlDbDatabaseInputArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., make_source_db_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., schema_setting: Optional[Any] = ..., table_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="makeSourceDbReadOnly")
    def make_source_db_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @make_source_db_read_only.setter
    def make_source_db_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaSetting")
    def schema_setting(self) -> Optional[Any]:
        
        ...
    
    @schema_setting.setter
    def schema_setting(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_map.setter
    def table_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbSyncDatabaseInputArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    migration_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schema_name: NotRequired[pulumi.Input[_builtins.str]]
    source_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    table_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_database_name: NotRequired[pulumi.Input[_builtins.str]]
    target_setting: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MigrateSqlServerSqlDbSyncDatabaseInputArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., migration_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., source_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., table_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_database_name: Optional[pulumi.Input[_builtins.str]] = ..., target_setting: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @migration_setting.setter
    def migration_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_setting.setter
    def source_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @table_map.setter
    def table_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database_name.setter
    def target_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_setting.setter
    def target_setting(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbSyncTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    validation_options: NotRequired[pulumi.Input[MigrationValidationOptionsArgsDict]]


@pulumi.input_type
class MigrateSqlServerSqlDbSyncTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs], validation_options: Optional[pulumi.Input[MigrationValidationOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[pulumi.Input[MigrationValidationOptionsArgs]]:
        
        ...
    
    @validation_options.setter
    def validation_options(self, value: Optional[pulumi.Input[MigrationValidationOptionsArgs]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateSqlServerSqlDbSyncTaskInputArgsDict]]


@pulumi.input_type
class MigrateSqlServerSqlDbSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateSqlServerSqlDbSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateSqlServerSqlDbSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateSqlServerSqlDbSyncTaskInputArgs]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]
    started_on: NotRequired[pulumi.Input[_builtins.str]]
    validation_options: NotRequired[pulumi.Input[MigrationValidationOptionsArgsDict]]


@pulumi.input_type
class MigrateSqlServerSqlDbTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs], encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ..., started_on: Optional[pulumi.Input[_builtins.str]] = ..., validation_options: Optional[pulumi.Input[MigrationValidationOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @started_on.setter
    def started_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[pulumi.Input[MigrationValidationOptionsArgs]]:
        
        ...
    
    @validation_options.setter
    def validation_options(self, value: Optional[pulumi.Input[MigrationValidationOptionsArgs]]): # -> None:
        ...
    


class MigrateSqlServerSqlDbTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    created_on: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[MigrateSqlServerSqlDbTaskInputArgsDict]]
    is_cloneable: NotRequired[pulumi.Input[_builtins.bool]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateSqlServerSqlDbTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., created_on: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[MigrateSqlServerSqlDbTaskInputArgs]] = ..., is_cloneable: Optional[pulumi.Input[_builtins.bool]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateSqlServerSqlDbTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateSqlServerSqlDbTaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_cloneable.setter
    def is_cloneable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSqlServerSqlMIDatabaseInputArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    restore_database_name: pulumi.Input[_builtins.str]
    backup_file_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    backup_file_share: NotRequired[pulumi.Input[FileShareArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateSqlServerSqlMIDatabaseInputArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], restore_database_name: pulumi.Input[_builtins.str], backup_file_paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_file_share: Optional[pulumi.Input[FileShareArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreDatabaseName")
    def restore_database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @restore_database_name.setter
    def restore_database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFilePaths")
    def backup_file_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backup_file_paths.setter
    def backup_file_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[pulumi.Input[FileShareArgs]]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: Optional[pulumi.Input[FileShareArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSqlServerSqlMISyncTaskInputArgsDict(TypedDict):
    
    azure_app: pulumi.Input[AzureActiveDirectoryAppArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    storage_resource_id: pulumi.Input[_builtins.str]
    target_connection_info: pulumi.Input[MiSqlConnectionInfoArgsDict]
    backup_file_share: NotRequired[pulumi.Input[FileShareArgsDict]]
    number_of_parallel_database_migrations: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class MigrateSqlServerSqlMISyncTaskInputArgs:
    def __init__(__self__, *, azure_app: pulumi.Input[AzureActiveDirectoryAppArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], storage_resource_id: pulumi.Input[_builtins.str], target_connection_info: pulumi.Input[MiSqlConnectionInfoArgs], backup_file_share: Optional[pulumi.Input[FileShareArgs]] = ..., number_of_parallel_database_migrations: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> pulumi.Input[AzureActiveDirectoryAppArgs]:
        
        ...
    
    @azure_app.setter
    def azure_app(self, value: pulumi.Input[AzureActiveDirectoryAppArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_resource_id.setter
    def storage_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MiSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MiSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[pulumi.Input[FileShareArgs]]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: Optional[pulumi.Input[FileShareArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfParallelDatabaseMigrations")
    def number_of_parallel_database_migrations(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @number_of_parallel_database_migrations.setter
    def number_of_parallel_database_migrations(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class MigrateSqlServerSqlMISyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    created_on: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[MigrateSqlServerSqlMISyncTaskInputArgsDict]]


@pulumi.input_type
class MigrateSqlServerSqlMISyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., created_on: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[MigrateSqlServerSqlMISyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateSqlServerSqlMISyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateSqlServerSqlMISyncTaskInputArgs]]): # -> None:
        ...
    


class MigrateSqlServerSqlMITaskInputArgsDict(TypedDict):
    
    backup_blob_share: pulumi.Input[BlobShareArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    aad_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    backup_file_share: NotRequired[pulumi.Input[FileShareArgsDict]]
    backup_mode: NotRequired[pulumi.Input[Union[_builtins.str, BackupMode]]]
    encrypted_key_for_secure_fields: NotRequired[pulumi.Input[_builtins.str]]
    selected_agent_jobs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    selected_logins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    started_on: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateSqlServerSqlMITaskInputArgs:
    def __init__(__self__, *, backup_blob_share: pulumi.Input[BlobShareArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs], aad_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_file_share: Optional[pulumi.Input[FileShareArgs]] = ..., backup_mode: Optional[pulumi.Input[Union[_builtins.str, BackupMode]]] = ..., encrypted_key_for_secure_fields: Optional[pulumi.Input[_builtins.str]] = ..., selected_agent_jobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., selected_logins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., started_on: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupBlobShare")
    def backup_blob_share(self) -> pulumi.Input[BlobShareArgs]:
        
        ...
    
    @backup_blob_share.setter
    def backup_blob_share(self, value: pulumi.Input[BlobShareArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadDomainName")
    def aad_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_domain_name.setter
    def aad_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[pulumi.Input[FileShareArgs]]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: Optional[pulumi.Input[FileShareArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMode")
    def backup_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupMode]]]:
        
        ...
    
    @backup_mode.setter
    def backup_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encrypted_key_for_secure_fields.setter
    def encrypted_key_for_secure_fields(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedAgentJobs")
    def selected_agent_jobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @selected_agent_jobs.setter
    def selected_agent_jobs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedLogins")
    def selected_logins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @selected_logins.setter
    def selected_logins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @started_on.setter
    def started_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSqlServerSqlMITaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    created_on: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[MigrateSqlServerSqlMITaskInputArgsDict]]
    is_cloneable: NotRequired[pulumi.Input[_builtins.bool]]
    parent_task_id: NotRequired[pulumi.Input[_builtins.str]]
    task_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrateSqlServerSqlMITaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., created_on: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[MigrateSqlServerSqlMITaskInputArgs]] = ..., is_cloneable: Optional[pulumi.Input[_builtins.bool]] = ..., parent_task_id: Optional[pulumi.Input[_builtins.str]] = ..., task_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateSqlServerSqlMITaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateSqlServerSqlMITaskInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_cloneable.setter
    def is_cloneable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentTaskId")
    def parent_task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_task_id.setter
    def parent_task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_id.setter
    def task_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrateSsisTaskInputArgsDict(TypedDict):
    
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    ssis_migration_info: pulumi.Input[SsisMigrationInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]


@pulumi.input_type
class MigrateSsisTaskInputArgs:
    def __init__(__self__, *, source_connection_info: pulumi.Input[SqlConnectionInfoArgs], ssis_migration_info: pulumi.Input[SsisMigrationInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssisMigrationInfo")
    def ssis_migration_info(self) -> pulumi.Input[SsisMigrationInfoArgs]:
        
        ...
    
    @ssis_migration_info.setter
    def ssis_migration_info(self, value: pulumi.Input[SsisMigrationInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    


class MigrateSsisTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateSsisTaskInputArgsDict]]


@pulumi.input_type
class MigrateSsisTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateSsisTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateSsisTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateSsisTaskInputArgs]]): # -> None:
        ...
    


class MigrationValidationOptionsArgsDict(TypedDict):
    
    enable_data_integrity_validation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_query_analysis_validation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_schema_validation: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MigrationValidationOptionsArgs:
    def __init__(__self__, *, enable_data_integrity_validation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_query_analysis_validation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_schema_validation: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataIntegrityValidation")
    def enable_data_integrity_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_data_integrity_validation.setter
    def enable_data_integrity_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQueryAnalysisValidation")
    def enable_query_analysis_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_query_analysis_validation.setter
    def enable_query_analysis_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSchemaValidation")
    def enable_schema_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_schema_validation.setter
    def enable_schema_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MongoConnectionInformationArgsDict(TypedDict):
    
    connection_string: NotRequired[pulumi.Input[_builtins.str]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    use_ssl: NotRequired[pulumi.Input[_builtins.bool]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MongoConnectionInformationArgs:
    def __init__(__self__, *, connection_string: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., use_ssl: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MongoDbCollectionSettingsArgsDict(TypedDict):
    
    can_delete: NotRequired[pulumi.Input[_builtins.bool]]
    shard_key: NotRequired[pulumi.Input[MongoDbShardKeySettingArgsDict]]
    target_rus: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MongoDbCollectionSettingsArgs:
    def __init__(__self__, *, can_delete: Optional[pulumi.Input[_builtins.bool]] = ..., shard_key: Optional[pulumi.Input[MongoDbShardKeySettingArgs]] = ..., target_rus: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canDelete")
    def can_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @can_delete.setter
    def can_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardKey")
    def shard_key(self) -> Optional[pulumi.Input[MongoDbShardKeySettingArgs]]:
        
        ...
    
    @shard_key.setter
    def shard_key(self, value: Optional[pulumi.Input[MongoDbShardKeySettingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRUs")
    def target_rus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_rus.setter
    def target_rus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MongoDbConnectionInfoArgsDict(TypedDict):
    
    connection_string: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    additional_settings: NotRequired[pulumi.Input[_builtins.str]]
    authentication: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    encrypt_connection: NotRequired[pulumi.Input[_builtins.bool]]
    enforce_ssl: NotRequired[pulumi.Input[_builtins.bool]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    server_brand_version: NotRequired[pulumi.Input[_builtins.str]]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    trust_server_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MongoDbConnectionInfoArgs:
    def __init__(__self__, *, connection_string: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], additional_settings: Optional[pulumi.Input[_builtins.str]] = ..., authentication: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_connection: Optional[pulumi.Input[_builtins.bool]] = ..., enforce_ssl: Optional[pulumi.Input[_builtins.bool]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., server_brand_version: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., server_version: Optional[pulumi.Input[_builtins.str]] = ..., trust_server_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_settings.setter
    def additional_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_connection.setter
    def encrypt_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceSSL")
    def enforce_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @enforce_ssl.setter
    def enforce_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_brand_version.setter
    def server_brand_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trust_server_certificate.setter
    def trust_server_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MongoDbDatabaseSettingsArgsDict(TypedDict):
    
    collections: pulumi.Input[Mapping[str, pulumi.Input[MongoDbCollectionSettingsArgsDict]]]
    target_rus: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MongoDbDatabaseSettingsArgs:
    def __init__(__self__, *, collections: pulumi.Input[Mapping[str, pulumi.Input[MongoDbCollectionSettingsArgs]]], target_rus: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collections(self) -> pulumi.Input[Mapping[str, pulumi.Input[MongoDbCollectionSettingsArgs]]]:
        
        ...
    
    @collections.setter
    def collections(self, value: pulumi.Input[Mapping[str, pulumi.Input[MongoDbCollectionSettingsArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRUs")
    def target_rus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_rus.setter
    def target_rus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MongoDbMigrationSettingsArgsDict(TypedDict):
    
    databases: pulumi.Input[Mapping[str, pulumi.Input[MongoDbDatabaseSettingsArgsDict]]]
    source: pulumi.Input[MongoDbConnectionInfoArgsDict]
    target: pulumi.Input[MongoDbConnectionInfoArgsDict]
    boost_rus: NotRequired[pulumi.Input[_builtins.int]]
    replication: NotRequired[pulumi.Input[Union[_builtins.str, MongoDbReplication]]]
    throttling: NotRequired[pulumi.Input[MongoDbThrottlingSettingsArgsDict]]


@pulumi.input_type
class MongoDbMigrationSettingsArgs:
    def __init__(__self__, *, databases: pulumi.Input[Mapping[str, pulumi.Input[MongoDbDatabaseSettingsArgs]]], source: pulumi.Input[MongoDbConnectionInfoArgs], target: pulumi.Input[MongoDbConnectionInfoArgs], boost_rus: Optional[pulumi.Input[_builtins.int]] = ..., replication: Optional[pulumi.Input[Union[_builtins.str, MongoDbReplication]]] = ..., throttling: Optional[pulumi.Input[MongoDbThrottlingSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> pulumi.Input[Mapping[str, pulumi.Input[MongoDbDatabaseSettingsArgs]]]:
        
        ...
    
    @databases.setter
    def databases(self, value: pulumi.Input[Mapping[str, pulumi.Input[MongoDbDatabaseSettingsArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[MongoDbConnectionInfoArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[MongoDbConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[MongoDbConnectionInfoArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[MongoDbConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostRUs")
    def boost_rus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @boost_rus.setter
    def boost_rus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replication(self) -> Optional[pulumi.Input[Union[_builtins.str, MongoDbReplication]]]:
        
        ...
    
    @replication.setter
    def replication(self, value: Optional[pulumi.Input[Union[_builtins.str, MongoDbReplication]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def throttling(self) -> Optional[pulumi.Input[MongoDbThrottlingSettingsArgs]]:
        
        ...
    
    @throttling.setter
    def throttling(self, value: Optional[pulumi.Input[MongoDbThrottlingSettingsArgs]]): # -> None:
        ...
    


class MongoDbShardKeyFieldArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    order: pulumi.Input[Union[_builtins.str, MongoDbShardKeyOrder]]


@pulumi.input_type
class MongoDbShardKeyFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], order: pulumi.Input[Union[_builtins.str, MongoDbShardKeyOrder]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[Union[_builtins.str, MongoDbShardKeyOrder]]:
        
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[Union[_builtins.str, MongoDbShardKeyOrder]]): # -> None:
        ...
    


class MongoDbShardKeySettingArgsDict(TypedDict):
    
    fields: pulumi.Input[Sequence[pulumi.Input[MongoDbShardKeyFieldArgsDict]]]
    is_unique: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MongoDbShardKeySettingArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[MongoDbShardKeyFieldArgs]]], is_unique: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[MongoDbShardKeyFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[MongoDbShardKeyFieldArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUnique")
    def is_unique(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_unique.setter
    def is_unique(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MongoDbThrottlingSettingsArgsDict(TypedDict):
    
    max_parallelism: NotRequired[pulumi.Input[_builtins.int]]
    min_free_cpu: NotRequired[pulumi.Input[_builtins.int]]
    min_free_memory_mb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MongoDbThrottlingSettingsArgs:
    def __init__(__self__, *, max_parallelism: Optional[pulumi.Input[_builtins.int]] = ..., min_free_cpu: Optional[pulumi.Input[_builtins.int]] = ..., min_free_memory_mb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelism")
    def max_parallelism(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_parallelism.setter
    def max_parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minFreeCpu")
    def min_free_cpu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_free_cpu.setter
    def min_free_cpu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minFreeMemoryMb")
    def min_free_memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_free_memory_mb.setter
    def min_free_memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MongoMigrationCollectionArgsDict(TypedDict):
    
    source_collection: NotRequired[pulumi.Input[_builtins.str]]
    source_database: NotRequired[pulumi.Input[_builtins.str]]
    target_collection: NotRequired[pulumi.Input[_builtins.str]]
    target_database: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MongoMigrationCollectionArgs:
    def __init__(__self__, *, source_collection: Optional[pulumi.Input[_builtins.str]] = ..., source_database: Optional[pulumi.Input[_builtins.str]] = ..., target_collection: Optional[pulumi.Input[_builtins.str]] = ..., target_database: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCollection")
    def source_collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_collection.setter
    def source_collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabase")
    def source_database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_database.setter
    def source_database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCollection")
    def target_collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_collection.setter
    def target_collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabase")
    def target_database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_database.setter
    def target_database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MySqlConnectionInfoArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    server_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    additional_settings: NotRequired[pulumi.Input[_builtins.str]]
    authentication: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    encrypt_connection: NotRequired[pulumi.Input[_builtins.bool]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MySqlConnectionInfoArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], server_name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], additional_settings: Optional[pulumi.Input[_builtins.str]] = ..., authentication: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_connection: Optional[pulumi.Input[_builtins.bool]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_settings.setter
    def additional_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_connection.setter
    def encrypt_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    


class OfflineConfigurationArgsDict(TypedDict):
    
    last_backup_name: NotRequired[pulumi.Input[_builtins.str]]
    offline: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class OfflineConfigurationArgs:
    def __init__(__self__, *, last_backup_name: Optional[pulumi.Input[_builtins.str]] = ..., offline: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupName")
    def last_backup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_backup_name.setter
    def last_backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def offline(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @offline.setter
    def offline(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class OracleConnectionInfoArgsDict(TypedDict):
    
    data_source: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    authentication: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OracleConnectionInfoArgs:
    def __init__(__self__, *, data_source: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], authentication: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., server_version: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PostgreSqlConnectionInfoArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    server_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    additional_settings: NotRequired[pulumi.Input[_builtins.str]]
    authentication: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypt_connection: NotRequired[pulumi.Input[_builtins.bool]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    server_brand_version: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    trust_server_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PostgreSqlConnectionInfoArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], server_name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], additional_settings: Optional[pulumi.Input[_builtins.str]] = ..., authentication: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_connection: Optional[pulumi.Input[_builtins.bool]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., server_brand_version: Optional[pulumi.Input[_builtins.str]] = ..., server_version: Optional[pulumi.Input[_builtins.str]] = ..., trust_server_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_settings.setter
    def additional_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_connection.setter
    def encrypt_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_brand_version.setter
    def server_brand_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trust_server_certificate.setter
    def trust_server_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectFilePropertiesArgsDict(TypedDict):
    
    extension: NotRequired[pulumi.Input[_builtins.str]]
    file_path: NotRequired[pulumi.Input[_builtins.str]]
    media_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectFilePropertiesArgs:
    def __init__(__self__, *, extension: Optional[pulumi.Input[_builtins.str]] = ..., file_path: Optional[pulumi.Input[_builtins.str]] = ..., media_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extension.setter
    def extension(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @media_type.setter
    def media_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SelectedCertificateInputArgsDict(TypedDict):
    
    certificate_name: pulumi.Input[_builtins.str]
    password: pulumi.Input[_builtins.str]


@pulumi.input_type
class SelectedCertificateInputArgs:
    def __init__(__self__, *, certificate_name: pulumi.Input[_builtins.str], password: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_name.setter
    def certificate_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServiceSkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceSkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SourceLocationArgsDict(TypedDict):
    
    azure_blob: NotRequired[pulumi.Input[AzureBlobArgsDict]]
    file_share: NotRequired[pulumi.Input[SqlFileShareArgsDict]]


@pulumi.input_type
class SourceLocationArgs:
    def __init__(__self__, *, azure_blob: Optional[pulumi.Input[AzureBlobArgs]] = ..., file_share: Optional[pulumi.Input[SqlFileShareArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlob")
    def azure_blob(self) -> Optional[pulumi.Input[AzureBlobArgs]]:
        
        ...
    
    @azure_blob.setter
    def azure_blob(self, value: Optional[pulumi.Input[AzureBlobArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> Optional[pulumi.Input[SqlFileShareArgs]]:
        
        ...
    
    @file_share.setter
    def file_share(self, value: Optional[pulumi.Input[SqlFileShareArgs]]): # -> None:
        ...
    


class SqlConnectionInformationArgsDict(TypedDict):
    
    authentication: NotRequired[pulumi.Input[_builtins.str]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    encrypt_connection: NotRequired[pulumi.Input[_builtins.bool]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    trust_server_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlConnectionInformationArgs:
    def __init__(__self__, *, authentication: Optional[pulumi.Input[_builtins.str]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_connection: Optional[pulumi.Input[_builtins.bool]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., trust_server_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_connection.setter
    def encrypt_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trust_server_certificate.setter
    def trust_server_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SqlConnectionInfoArgsDict(TypedDict):
    
    data_source: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    additional_settings: NotRequired[pulumi.Input[_builtins.str]]
    authentication: NotRequired[pulumi.Input[Union[_builtins.str, AuthenticationType]]]
    encrypt_connection: NotRequired[pulumi.Input[_builtins.bool]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    platform: NotRequired[pulumi.Input[Union[_builtins.str, SqlSourcePlatform]]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    server_brand_version: NotRequired[pulumi.Input[_builtins.str]]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    trust_server_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlConnectionInfoArgs:
    def __init__(__self__, *, data_source: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], additional_settings: Optional[pulumi.Input[_builtins.str]] = ..., authentication: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]] = ..., encrypt_connection: Optional[pulumi.Input[_builtins.bool]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[Union[_builtins.str, SqlSourcePlatform]]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., server_brand_version: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., server_version: Optional[pulumi.Input[_builtins.str]] = ..., trust_server_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_settings.setter
    def additional_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_connection.setter
    def encrypt_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlSourcePlatform]]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlSourcePlatform]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_brand_version.setter
    def server_brand_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trust_server_certificate.setter
    def trust_server_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SqlFileShareArgsDict(TypedDict):
    
    password: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlFileShareArgs:
    def __init__(__self__, *, password: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SsisMigrationInfoArgsDict(TypedDict):
    
    environment_overwrite_option: NotRequired[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]
    project_overwrite_option: NotRequired[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]
    ssis_store_type: NotRequired[pulumi.Input[Union[_builtins.str, SsisStoreType]]]


@pulumi.input_type
class SsisMigrationInfoArgs:
    def __init__(__self__, *, environment_overwrite_option: Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]] = ..., project_overwrite_option: Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]] = ..., ssis_store_type: Optional[pulumi.Input[Union[_builtins.str, SsisStoreType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentOverwriteOption")
    def environment_overwrite_option(self) -> Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]:
        
        ...
    
    @environment_overwrite_option.setter
    def environment_overwrite_option(self, value: Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectOverwriteOption")
    def project_overwrite_option(self) -> Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]:
        
        ...
    
    @project_overwrite_option.setter
    def project_overwrite_option(self, value: Optional[pulumi.Input[Union[_builtins.str, SsisMigrationOverwriteOption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssisStoreType")
    def ssis_store_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SsisStoreType]]]:
        
        ...
    
    @ssis_store_type.setter
    def ssis_store_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SsisStoreType]]]): # -> None:
        ...
    


class TargetLocationArgsDict(TypedDict):
    
    account_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetLocationArgs:
    def __init__(__self__, *, account_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ValidateSyncMigrationInputSqlServerTaskInputArgsDict]]


@pulumi.input_type
class ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ValidateSyncMigrationInputSqlServerTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ValidateSyncMigrationInputSqlServerTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ValidateSyncMigrationInputSqlServerTaskInputArgs]]): # -> None:
        ...
    


class ValidateMigrationInputSqlServerSqlMISyncTaskInputArgsDict(TypedDict):
    
    azure_app: pulumi.Input[AzureActiveDirectoryAppArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    storage_resource_id: pulumi.Input[_builtins.str]
    target_connection_info: pulumi.Input[MiSqlConnectionInfoArgsDict]
    backup_file_share: NotRequired[pulumi.Input[FileShareArgsDict]]


@pulumi.input_type
class ValidateMigrationInputSqlServerSqlMISyncTaskInputArgs:
    def __init__(__self__, *, azure_app: pulumi.Input[AzureActiveDirectoryAppArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], storage_resource_id: pulumi.Input[_builtins.str], target_connection_info: pulumi.Input[MiSqlConnectionInfoArgs], backup_file_share: Optional[pulumi.Input[FileShareArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> pulumi.Input[AzureActiveDirectoryAppArgs]:
        
        ...
    
    @azure_app.setter
    def azure_app(self, value: pulumi.Input[AzureActiveDirectoryAppArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_resource_id.setter
    def storage_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[MiSqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[MiSqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[pulumi.Input[FileShareArgs]]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: Optional[pulumi.Input[FileShareArgs]]): # -> None:
        ...
    


class ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ValidateMigrationInputSqlServerSqlMISyncTaskInputArgsDict]]


@pulumi.input_type
class ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMISyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMISyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMISyncTaskInputArgs]]): # -> None:
        ...
    


class ValidateMigrationInputSqlServerSqlMITaskInputArgsDict(TypedDict):
    
    backup_blob_share: pulumi.Input[BlobShareArgsDict]
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    backup_file_share: NotRequired[pulumi.Input[FileShareArgsDict]]
    backup_mode: NotRequired[pulumi.Input[Union[_builtins.str, BackupMode]]]
    selected_logins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ValidateMigrationInputSqlServerSqlMITaskInputArgs:
    def __init__(__self__, *, backup_blob_share: pulumi.Input[BlobShareArgs], selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs], backup_file_share: Optional[pulumi.Input[FileShareArgs]] = ..., backup_mode: Optional[pulumi.Input[Union[_builtins.str, BackupMode]]] = ..., selected_logins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupBlobShare")
    def backup_blob_share(self) -> pulumi.Input[BlobShareArgs]:
        
        ...
    
    @backup_blob_share.setter
    def backup_blob_share(self, value: pulumi.Input[BlobShareArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlMIDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[pulumi.Input[FileShareArgs]]:
        
        ...
    
    @backup_file_share.setter
    def backup_file_share(self, value: Optional[pulumi.Input[FileShareArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMode")
    def backup_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, BackupMode]]]:
        
        ...
    
    @backup_mode.setter
    def backup_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, BackupMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedLogins")
    def selected_logins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @selected_logins.setter
    def selected_logins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ValidateMigrationInputSqlServerSqlMITaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[ValidateMigrationInputSqlServerSqlMITaskInputArgsDict]]


@pulumi.input_type
class ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMITaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMITaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ValidateMigrationInputSqlServerSqlMITaskInputArgs]]): # -> None:
        ...
    


class ValidateMongoDbTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MongoDbMigrationSettingsArgsDict]]


@pulumi.input_type
class ValidateMongoDbTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MongoDbMigrationSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MongoDbMigrationSettingsArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MongoDbMigrationSettingsArgs]]): # -> None:
        ...
    


class ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict(TypedDict):
    
    task_type: pulumi.Input[_builtins.str]
    client_data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input: NotRequired[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgsDict]]


@pulumi.input_type
class ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], client_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input: Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_data.setter
    def client_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[MigrateOracleAzureDbPostgreSqlSyncTaskInputArgs]]): # -> None:
        ...
    


class ValidateSyncMigrationInputSqlServerTaskInputArgsDict(TypedDict):
    
    selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgsDict]]]
    source_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]
    target_connection_info: pulumi.Input[SqlConnectionInfoArgsDict]


@pulumi.input_type
class ValidateSyncMigrationInputSqlServerTaskInputArgs:
    def __init__(__self__, *, selected_databases: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]], source_connection_info: pulumi.Input[SqlConnectionInfoArgs], target_connection_info: pulumi.Input[SqlConnectionInfoArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]]:
        
        ...
    
    @selected_databases.setter
    def selected_databases(self, value: pulumi.Input[Sequence[pulumi.Input[MigrateSqlServerSqlDbSyncDatabaseInputArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Input[SqlConnectionInfoArgs]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: pulumi.Input[SqlConnectionInfoArgs]): # -> None:
        ...
    


