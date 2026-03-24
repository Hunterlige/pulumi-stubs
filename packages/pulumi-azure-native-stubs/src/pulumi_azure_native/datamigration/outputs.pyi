

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
__all__ = ['AzureActiveDirectoryAppResponse', 'AzureBlobResponse', 'BackupConfigurationResponse', 'BackupFileInfoResponse', 'BackupSetInfoResponse', 'BlobShareResponse', 'ConnectToMongoDbTaskPropertiesResponse', 'ConnectToSourceMySqlTaskInputResponse', 'ConnectToSourceMySqlTaskPropertiesResponse', 'ConnectToSourceNonSqlTaskOutputResponse', 'ConnectToSourceOracleSyncTaskInputResponse', 'ConnectToSourceOracleSyncTaskOutputResponse', 'ConnectToSourceOracleSyncTaskPropertiesResponse', 'ConnectToSourcePostgreSqlSyncTaskInputResponse', 'ConnectToSourcePostgreSqlSyncTaskOutputResponse', ..., 'ConnectToSourceSqlServerSyncTaskPropertiesResponse', 'ConnectToSourceSqlServerTaskInputResponse', ..., ..., ..., ..., 'ConnectToSourceSqlServerTaskPropertiesResponse', 'ConnectToTargetAzureDbForMySqlTaskInputResponse', 'ConnectToTargetAzureDbForMySqlTaskOutputResponse', ..., ..., ..., ..., ..., ..., ..., ..., 'ConnectToTargetSqlDbTaskInputResponse', 'ConnectToTargetSqlDbTaskOutputResponse', 'ConnectToTargetSqlDbTaskPropertiesResponse', 'ConnectToTargetSqlMISyncTaskInputResponse', 'ConnectToTargetSqlMISyncTaskOutputResponse', 'ConnectToTargetSqlMISyncTaskPropertiesResponse', 'ConnectToTargetSqlMITaskInputResponse', 'ConnectToTargetSqlMITaskOutputResponse', 'ConnectToTargetSqlMITaskPropertiesResponse', 'ConnectToTargetSqlSqlDbSyncTaskInputResponse', 'ConnectToTargetSqlSqlDbSyncTaskPropertiesResponse', 'CopyProgressDetailsResponse', 'DataIntegrityValidationResultResponse', 'DataItemMigrationSummaryResultResponse', 'DatabaseBackupInfoResponse', 'DatabaseFileInfoResponse', 'DatabaseInfoResponse', 'DatabaseMigrationPropertiesSqlDbResponse', 'DatabaseMigrationPropertiesSqlMiResponse', 'DatabaseMigrationPropertiesSqlVmResponse', 'DatabaseSummaryResultResponse', 'DatabaseTableResponse', 'ErrorInfoResponse', 'ExecutionStatisticsResponse', 'FileShareResponse', 'GetTdeCertificatesSqlTaskInputResponse', 'GetTdeCertificatesSqlTaskOutputResponse', 'GetTdeCertificatesSqlTaskPropertiesResponse', 'GetUserTablesMySqlTaskInputResponse', 'GetUserTablesMySqlTaskOutputResponse', 'GetUserTablesMySqlTaskPropertiesResponse', 'GetUserTablesOracleTaskInputResponse', 'GetUserTablesOracleTaskOutputResponse', 'GetUserTablesOracleTaskPropertiesResponse', 'GetUserTablesPostgreSqlTaskInputResponse', 'GetUserTablesPostgreSqlTaskOutputResponse', 'GetUserTablesPostgreSqlTaskPropertiesResponse', 'GetUserTablesSqlSyncTaskInputResponse', 'GetUserTablesSqlSyncTaskOutputResponse', 'GetUserTablesSqlSyncTaskPropertiesResponse', 'GetUserTablesSqlTaskInputResponse', 'GetUserTablesSqlTaskOutputResponse', 'GetUserTablesSqlTaskPropertiesResponse', 'ManagedServiceIdentityResponse', 'MiSqlConnectionInfoResponse', 'MigrateMISyncCompleteCommandInputResponse', 'MigrateMISyncCompleteCommandOutputResponse', 'MigrateMISyncCompleteCommandPropertiesResponse', 'MigrateMongoDbTaskPropertiesResponse', ..., ..., ..., ..., ..., ..., ..., ..., 'MigrateMySqlAzureDbForMySqlSyncTaskInputResponse', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'MigrateSqlServerSqlDbDatabaseInputResponse', 'MigrateSqlServerSqlDbSyncDatabaseInputResponse', 'MigrateSqlServerSqlDbSyncTaskInputResponse', ..., ..., 'MigrateSqlServerSqlDbSyncTaskOutputErrorResponse', ..., ..., 'MigrateSqlServerSqlDbSyncTaskPropertiesResponse', 'MigrateSqlServerSqlDbTaskInputResponse', ..., ..., 'MigrateSqlServerSqlDbTaskOutputErrorResponse', ..., 'MigrateSqlServerSqlDbTaskOutputTableLevelResponse', ..., 'MigrateSqlServerSqlDbTaskPropertiesResponse', 'MigrateSqlServerSqlMIDatabaseInputResponse', 'MigrateSqlServerSqlMISyncTaskInputResponse', ..., 'MigrateSqlServerSqlMISyncTaskOutputErrorResponse', ..., 'MigrateSqlServerSqlMISyncTaskPropertiesResponse', 'MigrateSqlServerSqlMITaskInputResponse', ..., ..., 'MigrateSqlServerSqlMITaskOutputErrorResponse', 'MigrateSqlServerSqlMITaskOutputLoginLevelResponse', ..., 'MigrateSqlServerSqlMITaskPropertiesResponse', 'MigrateSsisTaskInputResponse', 'MigrateSsisTaskOutputMigrationLevelResponse', 'MigrateSsisTaskOutputProjectLevelResponse', 'MigrateSsisTaskPropertiesResponse', 'MigrateSyncCompleteCommandInputResponse', 'MigrateSyncCompleteCommandOutputResponse', 'MigrateSyncCompleteCommandPropertiesResponse', 'MigrationEligibilityInfoResponse', 'MigrationReportResultResponse', 'MigrationStatusDetailsResponse', 'MigrationValidationDatabaseSummaryResultResponse', 'MigrationValidationOptionsResponse', 'MigrationValidationResultResponse', 'MongoConnectionInformationResponse', 'MongoDbClusterInfoResponse', 'MongoDbCollectionInfoResponse', 'MongoDbCollectionProgressResponse', 'MongoDbCollectionSettingsResponse', 'MongoDbConnectionInfoResponse', 'MongoDbDatabaseInfoResponse', 'MongoDbDatabaseProgressResponse', 'MongoDbDatabaseSettingsResponse', 'MongoDbErrorResponse', 'MongoDbMigrationProgressResponse', 'MongoDbMigrationSettingsResponse', 'MongoDbShardKeyFieldResponse', 'MongoDbShardKeyInfoResponse', 'MongoDbShardKeySettingResponse', 'MongoDbThrottlingSettingsResponse', 'MongoMigrationCollectionResponse', 'MongoMigrationProgressDetailsResponse', 'MySqlConnectionInfoResponse', 'NodeMonitoringDataResponse', 'ODataErrorResponse', 'OfflineConfigurationResponse', 'OracleConnectionInfoResponse', 'OrphanedUserInfoResponse', 'PostgreSqlConnectionInfoResponse', 'ProjectFilePropertiesResponse', 'QueryAnalysisValidationResultResponse', 'QueryExecutionResultResponse', 'ReportableExceptionResponse', 'SchemaComparisonValidationResultResponse', 'SchemaComparisonValidationResultTypeResponse', 'SelectedCertificateInputResponse', 'ServerPropertiesResponse', 'ServiceSkuResponse', 'SourceLocationResponse', 'SqlBackupFileInfoResponse', 'SqlBackupSetInfoResponse', 'SqlConnectionInfoResponse', 'SqlConnectionInformationResponse', 'SqlDbMigrationStatusDetailsResponse', 'SqlDbOfflineConfigurationResponse', 'SqlFileShareResponse', 'SsisMigrationInfoResponse', 'StartMigrationScenarioServerRoleResultResponse', 'SyncMigrationDatabaseErrorEventResponse', 'SystemDataResponse', 'TargetLocationResponse', 'UserAssignedIdentityResponse', ..., ..., ..., ..., ..., ..., ..., 'ValidateMongoDbTaskPropertiesResponse', ..., ..., ..., ..., 'ValidationErrorResponse', 'WaitStatisticsResponse']
@pulumi.output_type
class AzureActiveDirectoryAppResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_key: Optional[_builtins.str] = ..., application_id: Optional[_builtins.str] = ..., ignore_azure_permissions: Optional[_builtins.bool] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appKey")
    def app_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreAzurePermissions")
    def ignore_azure_permissions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureBlobResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_key: Optional[_builtins.str] = ..., auth_type: Optional[_builtins.str] = ..., blob_container_name: Optional[_builtins.str] = ..., identity: Optional[outputs.ManagedServiceIdentityResponse] = ..., storage_account_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_location: Optional[outputs.SourceLocationResponse] = ..., target_location: Optional[outputs.TargetLocationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[outputs.SourceLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> Optional[outputs.TargetLocationResponse]:
        
        ...
    


@pulumi.output_type
class BackupFileInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, family_sequence_number: Optional[_builtins.int] = ..., file_location: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familySequenceNumber")
    def family_sequence_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileLocation")
    def file_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupSetInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_finished_date: Optional[_builtins.str] = ..., backup_set_id: Optional[_builtins.str] = ..., backup_start_date: Optional[_builtins.str] = ..., backup_type: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., first_lsn: Optional[_builtins.str] = ..., is_backup_restored: Optional[_builtins.bool] = ..., last_lsn: Optional[_builtins.str] = ..., last_modified_time: Optional[_builtins.str] = ..., list_of_backup_files: Optional[Sequence[outputs.BackupFileInfoResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFinishedDate")
    def backup_finished_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetId")
    def backup_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStartDate")
    def backup_start_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstLsn")
    def first_lsn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBackupRestored")
    def is_backup_restored(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastLsn")
    def last_lsn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listOfBackupFiles")
    def list_of_backup_files(self) -> Optional[Sequence[outputs.BackupFileInfoResponse]]:
        
        ...
    


@pulumi.output_type
class BlobShareResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sas_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasUri")
    def sas_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectToMongoDbTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.MongoDbClusterInfoResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MongoDbConnectionInfoResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.MongoDbClusterInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MongoDbConnectionInfoResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceMySqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.MySqlConnectionInfoResponse, check_permissions_group: Optional[_builtins.str] = ..., is_offline_migration: Optional[_builtins.bool] = ..., target_platform: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkPermissionsGroup")
    def check_permissions_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOfflineMigration")
    def is_offline_migration(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceMySqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToSourceNonSqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToSourceMySqlTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToSourceNonSqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToSourceMySqlTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceNonSqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], id: _builtins.str, server_properties: outputs.ServerPropertiesResponse, source_server_brand_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverProperties")
    def server_properties(self) -> outputs.ServerPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceOracleSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.OracleConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.OracleConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToSourceOracleSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], source_server_brand_version: _builtins.str, source_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceOracleSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToSourceOracleSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToSourceOracleSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToSourceOracleSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToSourceOracleSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourcePostgreSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.PostgreSqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToSourcePostgreSqlSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], id: _builtins.str, source_server_brand_version: _builtins.str, source_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourcePostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToSourcePostgreSqlSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToSourcePostgreSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToSourcePostgreSqlSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToSourcePostgreSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToSourceSqlServerTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToSourceSqlServerTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.SqlConnectionInfoResponse, check_permissions_group: Optional[_builtins.str] = ..., collect_agent_jobs: Optional[_builtins.bool] = ..., collect_databases: Optional[_builtins.bool] = ..., collect_logins: Optional[_builtins.bool] = ..., collect_tde_certificate_info: Optional[_builtins.bool] = ..., encrypted_key_for_secure_fields: Optional[_builtins.str] = ..., validate_ssis_catalog_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkPermissionsGroup")
    def check_permissions_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectAgentJobs")
    def collect_agent_jobs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectDatabases")
    def collect_databases(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectLogins")
    def collect_logins(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectTdeCertificateInfo")
    def collect_tde_certificate_info(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsisCatalogOnly")
    def validate_ssis_catalog_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskOutputAgentJobLevelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, is_enabled: _builtins.bool, job_category: _builtins.str, job_owner: _builtins.str, last_executed_on: _builtins.str, migration_eligibility: outputs.MigrationEligibilityInfoResponse, name: _builtins.str, result_type: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobCategory")
    def job_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobOwner")
    def job_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutedOn")
    def last_executed_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationEligibility")
    def migration_eligibility(self) -> outputs.MigrationEligibilityInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskOutputDatabaseLevelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compatibility_level: _builtins.str, database_files: Sequence[outputs.DatabaseFileInfoResponse], database_state: _builtins.str, id: _builtins.str, name: _builtins.str, result_type: _builtins.str, size_mb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFiles")
    def database_files(self) -> Sequence[outputs.DatabaseFileInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseState")
    def database_state(self) -> _builtins.str:
        
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
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeMB")
    def size_mb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskOutputLoginLevelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_database: _builtins.str, id: _builtins.str, is_enabled: _builtins.bool, login_type: _builtins.str, migration_eligibility: outputs.MigrationEligibilityInfoResponse, name: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatabase")
    def default_database(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginType")
    def login_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationEligibility")
    def migration_eligibility(self) -> outputs.MigrationEligibilityInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskOutputTaskLevelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_jobs: Mapping[str, _builtins.str], database_tde_certificate_mapping: Mapping[str, _builtins.str], databases: Mapping[str, _builtins.str], id: _builtins.str, logins: Mapping[str, _builtins.str], result_type: _builtins.str, source_server_brand_version: _builtins.str, source_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentJobs")
    def agent_jobs(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseTdeCertificateMapping")
    def database_tde_certificate_mapping(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logins(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToSourceSqlServerTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToSourceSqlServerTaskInputResponse] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToSourceSqlServerTaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForMySqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.MySqlConnectionInfoResponse, target_connection_info: outputs.MySqlConnectionInfoResponse, is_offline_migration: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOfflineMigration")
    def is_offline_migration(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForMySqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], id: _builtins.str, server_version: _builtins.str, target_server_brand_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForMySqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetAzureDbForMySqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetAzureDbForMySqlTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetAzureDbForMySqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetAzureDbForMySqlTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForPostgreSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.PostgreSqlConnectionInfoResponse, target_connection_info: outputs.PostgreSqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForPostgreSqlSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], id: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetAzureDbForPostgreSqlSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetAzureDbForPostgreSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetAzureDbForPostgreSqlSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetAzureDbForPostgreSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_connection_info: outputs.PostgreSqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[_builtins.str], target_server_brand_version: _builtins.str, target_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse], database_schema_map: Optional[Sequence[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponseDatabaseSchemaMap]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseSchemaMap")
    def database_schema_map(self) -> Optional[Sequence[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponseDatabaseSchemaMap]]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponseDatabaseSchemaMap(dict):
    def __init__(__self__, *, database: Optional[_builtins.str] = ..., schemas: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlDbTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_connection_info: outputs.SqlConnectionInfoResponse, query_object_counts: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryObjectCounts")
    def query_object_counts(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlDbTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Mapping[str, _builtins.str], id: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlDbTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetSqlDbTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., created_on: Optional[_builtins.str] = ..., input: Optional[outputs.ConnectToTargetSqlDbTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetSqlDbTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetSqlDbTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMISyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_app: outputs.AzureActiveDirectoryAppResponse, target_connection_info: outputs.MiSqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> outputs.AzureActiveDirectoryAppResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MiSqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMISyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_server_brand_version: _builtins.str, target_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMISyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetSqlMISyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetSqlMISyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetSqlMISyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetSqlMISyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMITaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_connection_info: outputs.SqlConnectionInfoResponse, collect_agent_jobs: Optional[_builtins.bool] = ..., collect_logins: Optional[_builtins.bool] = ..., validate_ssis_catalog_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectAgentJobs")
    def collect_agent_jobs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectLogins")
    def collect_logins(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsisCatalogOnly")
    def validate_ssis_catalog_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMITaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_jobs: Sequence[_builtins.str], id: _builtins.str, logins: Sequence[_builtins.str], target_server_brand_version: _builtins.str, target_server_version: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentJobs")
    def agent_jobs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logins(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlMITaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetSqlMITaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetSqlMITaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetSqlMITaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetSqlMITaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlSqlDbSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ConnectToTargetSqlSqlDbSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ConnectToTargetSqlDbTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ConnectToTargetSqlSqlDbSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ConnectToTargetSqlDbTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ConnectToTargetSqlSqlDbSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class CopyProgressDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, copy_duration: _builtins.int, copy_start: _builtins.str, copy_throughput: _builtins.float, data_read: _builtins.float, data_written: _builtins.float, parallel_copy_type: _builtins.str, rows_copied: _builtins.float, rows_read: _builtins.float, status: _builtins.str, table_name: _builtins.str, used_parallel_copies: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyDuration")
    def copy_duration(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStart")
    def copy_start(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyThroughput")
    def copy_throughput(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRead")
    def data_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataWritten")
    def data_written(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelCopyType")
    def parallel_copy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsCopied")
    def rows_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsRead")
    def rows_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedParallelCopies")
    def used_parallel_copies(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class DataIntegrityValidationResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failed_objects: Optional[Mapping[str, _builtins.str]] = ..., validation_errors: Optional[outputs.ValidationErrorResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failedObjects")
    def failed_objects(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[outputs.ValidationErrorResponse]:
        
        ...
    


@pulumi.output_type
class DataItemMigrationSummaryResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, error_prefix: _builtins.str, items_completed_count: _builtins.float, items_count: _builtins.float, name: _builtins.str, result_prefix: _builtins.str, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCompletedCount")
    def items_completed_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCount")
    def items_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseBackupInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_files: Sequence[_builtins.str], backup_finish_date: _builtins.str, backup_type: _builtins.str, database_name: _builtins.str, family_count: _builtins.int, is_compressed: _builtins.bool, is_damaged: _builtins.bool, position: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFiles")
    def backup_files(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFinishDate")
    def backup_finish_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familyCount")
    def family_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCompressed")
    def is_compressed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDamaged")
    def is_damaged(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class DatabaseFileInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: Optional[_builtins.str] = ..., file_type: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., logical_name: Optional[_builtins.str] = ..., physical_full_name: Optional[_builtins.str] = ..., restore_full_name: Optional[_builtins.str] = ..., size_mb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalName")
    def logical_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalFullName")
    def physical_full_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreFullName")
    def restore_full_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeMB")
    def size_mb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class DatabaseInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_database_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseMigrationPropertiesSqlDbResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, kind: _builtins.str, migration_failure_error: outputs.ErrorInfoResponse, migration_status: _builtins.str, migration_status_details: outputs.SqlDbMigrationStatusDetailsResponse, offline_configuration: outputs.SqlDbOfflineConfigurationResponse, provisioning_state: _builtins.str, source_server_name: _builtins.str, started_on: _builtins.str, migration_operation_id: Optional[_builtins.str] = ..., migration_service: Optional[_builtins.str] = ..., provisioning_error: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., source_database_name: Optional[_builtins.str] = ..., source_sql_connection: Optional[outputs.SqlConnectionInformationResponse] = ..., table_list: Optional[Sequence[_builtins.str]] = ..., target_database_collation: Optional[_builtins.str] = ..., target_sql_connection: Optional[outputs.SqlConnectionInformationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationFailureError")
    def migration_failure_error(self) -> outputs.ErrorInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatusDetails")
    def migration_status_details(self) -> outputs.SqlDbMigrationStatusDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineConfiguration")
    def offline_configuration(self) -> outputs.SqlDbOfflineConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[outputs.SqlConnectionInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableList")
    def table_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSqlConnection")
    def target_sql_connection(self) -> Optional[outputs.SqlConnectionInformationResponse]:
        
        ...
    


@pulumi.output_type
class DatabaseMigrationPropertiesSqlMiResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, kind: _builtins.str, migration_failure_error: outputs.ErrorInfoResponse, migration_status: _builtins.str, migration_status_details: outputs.MigrationStatusDetailsResponse, provisioning_state: _builtins.str, source_server_name: _builtins.str, started_on: _builtins.str, backup_configuration: Optional[outputs.BackupConfigurationResponse] = ..., migration_operation_id: Optional[_builtins.str] = ..., migration_service: Optional[_builtins.str] = ..., offline_configuration: Optional[outputs.OfflineConfigurationResponse] = ..., provisioning_error: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., source_database_name: Optional[_builtins.str] = ..., source_sql_connection: Optional[outputs.SqlConnectionInformationResponse] = ..., target_database_collation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationFailureError")
    def migration_failure_error(self) -> outputs.ErrorInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatusDetails")
    def migration_status_details(self) -> outputs.MigrationStatusDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[outputs.BackupConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineConfiguration")
    def offline_configuration(self) -> Optional[outputs.OfflineConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[outputs.SqlConnectionInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseMigrationPropertiesSqlVmResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, kind: _builtins.str, migration_failure_error: outputs.ErrorInfoResponse, migration_status: _builtins.str, migration_status_details: outputs.MigrationStatusDetailsResponse, provisioning_state: _builtins.str, source_server_name: _builtins.str, started_on: _builtins.str, backup_configuration: Optional[outputs.BackupConfigurationResponse] = ..., migration_operation_id: Optional[_builtins.str] = ..., migration_service: Optional[_builtins.str] = ..., offline_configuration: Optional[outputs.OfflineConfigurationResponse] = ..., provisioning_error: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., source_database_name: Optional[_builtins.str] = ..., source_sql_connection: Optional[outputs.SqlConnectionInformationResponse] = ..., target_database_collation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationFailureError")
    def migration_failure_error(self) -> outputs.ErrorInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatusDetails")
    def migration_status_details(self) -> outputs.MigrationStatusDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[outputs.BackupConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineConfiguration")
    def offline_configuration(self) -> Optional[outputs.OfflineConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSqlConnection")
    def source_sql_connection(self) -> Optional[outputs.SqlConnectionInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseCollation")
    def target_database_collation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseSummaryResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, error_prefix: _builtins.str, items_completed_count: _builtins.float, items_count: _builtins.float, name: _builtins.str, result_prefix: _builtins.str, size_mb: _builtins.float, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCompletedCount")
    def items_completed_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCount")
    def items_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeMB")
    def size_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseTableResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, has_rows: _builtins.bool, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasRows")
    def has_rows(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorInfoResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExecutionStatisticsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_time_ms: Optional[_builtins.float] = ..., elapsed_time_ms: Optional[_builtins.float] = ..., execution_count: Optional[_builtins.float] = ..., has_errors: Optional[_builtins.bool] = ..., sql_errors: Optional[Sequence[_builtins.str]] = ..., wait_stats: Optional[Mapping[str, outputs.WaitStatisticsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuTimeMs")
    def cpu_time_ms(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elapsedTimeMs")
    def elapsed_time_ms(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionCount")
    def execution_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasErrors")
    def has_errors(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlErrors")
    def sql_errors(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitStats")
    def wait_stats(self) -> Optional[Mapping[str, outputs.WaitStatisticsResponse]]:
        
        ...
    


@pulumi.output_type
class FileShareResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, password: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTdeCertificatesSqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_file_share: outputs.FileShareResponse, connection_info: outputs.SqlConnectionInfoResponse, selected_certificates: Sequence[outputs.SelectedCertificateInputResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> outputs.FileShareResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedCertificates")
    def selected_certificates(self) -> Sequence[outputs.SelectedCertificateInputResponse]:
        
        ...
    


@pulumi.output_type
class GetTdeCertificatesSqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, base64_encoded_certificates: Mapping[str, Sequence[_builtins.str]], validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="base64EncodedCertificates")
    def base64_encoded_certificates(self) -> Mapping[str, Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetTdeCertificatesSqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetTdeCertificatesSqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetTdeCertificatesSqlTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetTdeCertificatesSqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetTdeCertificatesSqlTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesMySqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_info: outputs.MySqlConnectionInfoResponse, selected_databases: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetUserTablesMySqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases_to_tables: Mapping[str, Sequence[outputs.DatabaseTableResponse]], id: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToTables")
    def databases_to_tables(self) -> Mapping[str, Sequence[outputs.DatabaseTableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesMySqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetUserTablesMySqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetUserTablesMySqlTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetUserTablesMySqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetUserTablesMySqlTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesOracleTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_info: outputs.OracleConnectionInfoResponse, selected_schemas: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> outputs.OracleConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSchemas")
    def selected_schemas(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetUserTablesOracleTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_name: _builtins.str, tables: Sequence[outputs.DatabaseTableResponse], validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Sequence[outputs.DatabaseTableResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesOracleTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetUserTablesOracleTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetUserTablesOracleTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetUserTablesOracleTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetUserTablesOracleTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesPostgreSqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_info: outputs.PostgreSqlConnectionInfoResponse, selected_databases: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetUserTablesPostgreSqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, tables: Sequence[outputs.DatabaseTableResponse], validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Sequence[outputs.DatabaseTableResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesPostgreSqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetUserTablesPostgreSqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetUserTablesPostgreSqlTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetUserTablesPostgreSqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetUserTablesPostgreSqlTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_source_databases: Sequence[_builtins.str], selected_target_databases: Sequence[_builtins.str], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSourceDatabases")
    def selected_source_databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTargetDatabases")
    def selected_target_databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases_to_source_tables: Mapping[str, Sequence[outputs.DatabaseTableResponse]], databases_to_target_tables: Mapping[str, Sequence[outputs.DatabaseTableResponse]], table_validation_errors: Mapping[str, Sequence[_builtins.str]], validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToSourceTables")
    def databases_to_source_tables(self) -> Mapping[str, Sequence[outputs.DatabaseTableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToTargetTables")
    def databases_to_target_tables(self) -> Mapping[str, Sequence[outputs.DatabaseTableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableValidationErrors")
    def table_validation_errors(self) -> Mapping[str, Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetUserTablesSqlSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetUserTablesSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetUserTablesSqlSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetUserTablesSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_info: outputs.SqlConnectionInfoResponse, selected_databases: Sequence[_builtins.str], encrypted_key_for_secure_fields: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfo")
    def connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases_to_tables: Mapping[str, Sequence[outputs.DatabaseTableResponse]], id: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesToTables")
    def databases_to_tables(self) -> Mapping[str, Sequence[outputs.DatabaseTableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class GetUserTablesSqlTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.GetUserTablesSqlTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.GetUserTablesSqlTaskInputResponse] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.GetUserTablesSqlTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.GetUserTablesSqlTaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
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
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class MiSqlConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, managed_instance_resource_id: _builtins.str, type: _builtins.str, password: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceResourceId")
    def managed_instance_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateMISyncCompleteCommandInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_database_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMISyncCompleteCommandOutputResponse(dict):
    
    def __init__(__self__, *, errors: Optional[Sequence[outputs.ReportableExceptionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ReportableExceptionResponse]]:
        
        ...
    


@pulumi.output_type
class MigrateMISyncCompleteCommandPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, command_type: _builtins.str, errors: Sequence[outputs.ODataErrorResponse], output: outputs.MigrateMISyncCompleteCommandOutputResponse, state: _builtins.str, input: Optional[outputs.MigrateMISyncCompleteCommandInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandType")
    def command_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> outputs.MigrateMISyncCompleteCommandOutputResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateMISyncCompleteCommandInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateMongoDbTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MongoDbMigrationSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MongoDbMigrationSettingsResponse]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., table_map: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateMySqlAzureDbForMySqlOfflineDatabaseInputResponse], source_connection_info: outputs.MySqlConnectionInfoResponse, target_connection_info: outputs.MySqlConnectionInfoResponse, encrypted_key_for_secure_fields: Optional[_builtins.str] = ..., make_source_server_read_only: Optional[_builtins.bool] = ..., optional_agent_settings: Optional[Mapping[str, _builtins.str]] = ..., started_on: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateMySqlAzureDbForMySqlOfflineDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="makeSourceServerReadOnly")
    def make_source_server_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalAgentSettings")
    def optional_agent_settings(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, ended_on: _builtins.str, error_count: _builtins.float, error_prefix: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, last_storage_update: _builtins.str, message: _builtins.str, number_of_objects: _builtins.float, number_of_objects_completed: _builtins.float, object_summary: Mapping[str, outputs.DataItemMigrationSummaryResultResponse], result_prefix: _builtins.str, result_type: _builtins.str, stage: _builtins.str, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCount")
    def error_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStorageUpdate")
    def last_storage_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfObjects")
    def number_of_objects(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfObjectsCompleted")
    def number_of_objects_completed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSummary")
    def object_summary(self) -> Mapping[str, outputs.DataItemMigrationSummaryResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_summary: Mapping[str, outputs.DatabaseSummaryResultResponse], duration_in_seconds: _builtins.float, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, last_storage_update: _builtins.str, message: _builtins.str, result_type: _builtins.str, source_server_brand_version: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, status: _builtins.str, status_message: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str, databases: Optional[Mapping[str, _builtins.str]] = ..., migration_report_result: Optional[outputs.MigrationReportResultResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseSummary")
    def database_summary(self) -> Mapping[str, outputs.DatabaseSummaryResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStorageUpdate")
    def last_storage_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationReportResult")
    def migration_report_result(self) -> Optional[outputs.MigrationReportResultResponse]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, error_prefix: _builtins.str, id: _builtins.str, items_completed_count: _builtins.float, items_count: _builtins.float, last_storage_update: _builtins.str, object_name: _builtins.str, result_prefix: _builtins.str, result_type: _builtins.str, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCompletedCount")
    def items_completed_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCount")
    def items_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStorageUpdate")
    def last_storage_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateMySqlAzureDbForMySqlOfflineTaskInputResponse] = ..., is_cloneable: Optional[_builtins.bool] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateMySqlAzureDbForMySqlOfflineTaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, migration_setting: Optional[Mapping[str, _builtins.str]] = ..., name: Optional[_builtins.str] = ..., source_setting: Optional[Mapping[str, _builtins.str]] = ..., table_map: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ..., target_setting: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateMySqlAzureDbForMySqlSyncDatabaseInputResponse], source_connection_info: outputs.MySqlConnectionInfoResponse, target_connection_info: outputs.MySqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateMySqlAzureDbForMySqlSyncDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MySqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, result_type: _builtins.str, error_message: Optional[_builtins.str] = ..., events: Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]]:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_changes: _builtins.float, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, database_name: _builtins.str, ended_on: _builtins.str, full_load_completed_tables: _builtins.float, full_load_errored_tables: _builtins.float, full_load_loading_tables: _builtins.float, full_load_queued_tables: _builtins.float, id: _builtins.str, incoming_changes: _builtins.float, initialization_completed: _builtins.bool, latency: _builtins.float, migration_state: _builtins.str, result_type: _builtins.str, started_on: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedChanges")
    def applied_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadCompletedTables")
    def full_load_completed_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErroredTables")
    def full_load_errored_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadLoadingTables")
    def full_load_loading_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadQueuedTables")
    def full_load_queued_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingChanges")
    def incoming_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationCompleted")
    def initialization_completed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, id: _builtins.str, result_type: _builtins.str, source_server: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, target_server: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServer")
    def source_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServer")
    def target_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cdc_delete_counter: _builtins.str, cdc_insert_counter: _builtins.str, cdc_update_counter: _builtins.str, data_errors_counter: _builtins.float, database_name: _builtins.str, full_load_ended_on: _builtins.str, full_load_est_finish_time: _builtins.str, full_load_started_on: _builtins.str, full_load_total_rows: _builtins.float, id: _builtins.str, last_modified_time: _builtins.str, result_type: _builtins.str, state: _builtins.str, table_name: _builtins.str, total_changes_applied: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataErrorsCounter")
    def data_errors_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEndedOn")
    def full_load_ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEstFinishTime")
    def full_load_est_finish_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadStartedOn")
    def full_load_started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadTotalRows")
    def full_load_total_rows(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalChangesApplied")
    def total_changes_applied(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MigrateMySqlAzureDbForMySqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateMySqlAzureDbForMySqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateMySqlAzureDbForMySqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateOracleAzureDbPostgreSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateOracleAzureDbPostgreSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, case_manipulation: Optional[_builtins.str] = ..., migration_setting: Optional[Mapping[str, _builtins.str]] = ..., name: Optional[_builtins.str] = ..., schema_name: Optional[_builtins.str] = ..., source_setting: Optional[Mapping[str, _builtins.str]] = ..., table_map: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ..., target_setting: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseManipulation")
    def case_manipulation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateOracleAzureDbPostgreSqlSyncDatabaseInputResponse], source_connection_info: outputs.OracleConnectionInfoResponse, target_connection_info: outputs.PostgreSqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateOracleAzureDbPostgreSqlSyncDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.OracleConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, result_type: _builtins.str, error_message: Optional[_builtins.str] = ..., events: Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]]:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_changes: _builtins.float, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, database_name: _builtins.str, ended_on: _builtins.str, full_load_completed_tables: _builtins.float, full_load_errored_tables: _builtins.float, full_load_loading_tables: _builtins.float, full_load_queued_tables: _builtins.float, id: _builtins.str, incoming_changes: _builtins.float, initialization_completed: _builtins.bool, latency: _builtins.float, migration_state: _builtins.str, result_type: _builtins.str, started_on: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedChanges")
    def applied_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadCompletedTables")
    def full_load_completed_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErroredTables")
    def full_load_errored_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadLoadingTables")
    def full_load_loading_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadQueuedTables")
    def full_load_queued_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingChanges")
    def incoming_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationCompleted")
    def initialization_completed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, id: _builtins.str, result_type: _builtins.str, source_server: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, target_server: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServer")
    def source_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServer")
    def target_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, data_errors_counter: _builtins.float, database_name: _builtins.str, full_load_ended_on: _builtins.str, full_load_est_finish_time: _builtins.str, full_load_started_on: _builtins.str, full_load_total_rows: _builtins.float, id: _builtins.str, last_modified_time: _builtins.str, result_type: _builtins.str, state: _builtins.str, table_name: _builtins.str, total_changes_applied: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataErrorsCounter")
    def data_errors_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEndedOn")
    def full_load_ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEstFinishTime")
    def full_load_est_finish_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadStartedOn")
    def full_load_started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadTotalRows")
    def full_load_total_rows(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalChangesApplied")
    def total_changes_applied(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, migration_setting: Optional[Any] = ..., name: Optional[_builtins.str] = ..., selected_tables: Optional[Sequence[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputResponse]] = ..., source_setting: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ..., target_setting: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTables")
    def selected_tables(self) -> Optional[Sequence[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInputResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputResponse], source_connection_info: outputs.PostgreSqlConnectionInfoResponse, started_on: _builtins.str, target_connection_info: outputs.PostgreSqlConnectionInfoResponse, encrypted_key_for_secure_fields: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.PostgreSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, result_type: _builtins.str, error_message: Optional[_builtins.str] = ..., events: Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_changes: _builtins.float, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, database_name: _builtins.str, ended_on: _builtins.str, full_load_completed_tables: _builtins.float, full_load_errored_tables: _builtins.float, full_load_loading_tables: _builtins.float, full_load_queued_tables: _builtins.float, id: _builtins.str, incoming_changes: _builtins.float, initialization_completed: _builtins.bool, latency: _builtins.float, migration_state: _builtins.str, result_type: _builtins.str, started_on: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedChanges")
    def applied_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadCompletedTables")
    def full_load_completed_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErroredTables")
    def full_load_errored_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadLoadingTables")
    def full_load_loading_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadQueuedTables")
    def full_load_queued_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingChanges")
    def incoming_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationCompleted")
    def initialization_completed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str, events: Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, id: _builtins.str, result_type: _builtins.str, source_server: _builtins.str, source_server_type: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, state: _builtins.str, target_server: _builtins.str, target_server_type: _builtins.str, target_server_version: _builtins.str, database_count: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServer")
    def source_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerType")
    def source_server_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServer")
    def target_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerType")
    def target_server_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseCount")
    def database_count(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, data_errors_counter: _builtins.float, database_name: _builtins.str, full_load_ended_on: _builtins.str, full_load_est_finish_time: _builtins.str, full_load_started_on: _builtins.str, full_load_total_rows: _builtins.float, id: _builtins.str, last_modified_time: _builtins.str, result_type: _builtins.str, state: _builtins.str, table_name: _builtins.str, total_changes_applied: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataErrorsCounter")
    def data_errors_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEndedOn")
    def full_load_ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEstFinishTime")
    def full_load_est_finish_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadStartedOn")
    def full_load_started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadTotalRows")
    def full_load_total_rows(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalChangesApplied")
    def total_changes_applied(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., created_on: Optional[_builtins.str] = ..., input: Optional[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputResponse] = ..., is_cloneable: Optional[_builtins.bool] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., make_source_db_read_only: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., schema_setting: Optional[Any] = ..., table_map: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="makeSourceDbReadOnly")
    def make_source_db_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaSetting")
    def schema_setting(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., migration_setting: Optional[Mapping[str, _builtins.str]] = ..., name: Optional[_builtins.str] = ..., schema_name: Optional[_builtins.str] = ..., source_setting: Optional[Mapping[str, _builtins.str]] = ..., table_map: Optional[Mapping[str, _builtins.str]] = ..., target_database_name: Optional[_builtins.str] = ..., target_setting: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSetting")
    def migration_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSetting")
    def source_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMap")
    def table_map(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSetting")
    def target_setting(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateSqlServerSqlDbSyncDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse, validation_options: Optional[outputs.MigrationValidationOptionsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlDbSyncDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[outputs.MigrationValidationOptionsResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskOutputDatabaseErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, result_type: _builtins.str, error_message: Optional[_builtins.str] = ..., events: Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.SyncMigrationDatabaseErrorEventResponse]]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_changes: _builtins.float, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, database_name: _builtins.str, ended_on: _builtins.str, full_load_completed_tables: _builtins.float, full_load_errored_tables: _builtins.float, full_load_loading_tables: _builtins.float, full_load_queued_tables: _builtins.float, id: _builtins.str, incoming_changes: _builtins.float, initialization_completed: _builtins.bool, latency: _builtins.float, migration_state: _builtins.str, result_type: _builtins.str, started_on: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedChanges")
    def applied_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadCompletedTables")
    def full_load_completed_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErroredTables")
    def full_load_errored_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadLoadingTables")
    def full_load_loading_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadQueuedTables")
    def full_load_queued_tables(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingChanges")
    def incoming_changes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationCompleted")
    def initialization_completed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_count: _builtins.int, ended_on: _builtins.str, id: _builtins.str, result_type: _builtins.str, source_server: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, target_server: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseCount")
    def database_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServer")
    def source_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServer")
    def target_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cdc_delete_counter: _builtins.float, cdc_insert_counter: _builtins.float, cdc_update_counter: _builtins.float, data_errors_counter: _builtins.float, database_name: _builtins.str, full_load_ended_on: _builtins.str, full_load_est_finish_time: _builtins.str, full_load_started_on: _builtins.str, full_load_total_rows: _builtins.float, id: _builtins.str, last_modified_time: _builtins.str, result_type: _builtins.str, state: _builtins.str, table_name: _builtins.str, total_changes_applied: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcDeleteCounter")
    def cdc_delete_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertCounter")
    def cdc_insert_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcUpdateCounter")
    def cdc_update_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataErrorsCounter")
    def data_errors_counter(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEndedOn")
    def full_load_ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadEstFinishTime")
    def full_load_est_finish_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadStartedOn")
    def full_load_started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadTotalRows")
    def full_load_total_rows(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalChangesApplied")
    def total_changes_applied(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateSqlServerSqlDbSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSqlServerSqlDbSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateSqlServerSqlDbDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse, encrypted_key_for_secure_fields: Optional[_builtins.str] = ..., started_on: Optional[_builtins.str] = ..., validation_options: Optional[outputs.MigrationValidationOptionsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlDbDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOptions")
    def validation_options(self) -> Optional[outputs.MigrationValidationOptionsResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, ended_on: _builtins.str, error_count: _builtins.float, error_prefix: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, message: _builtins.str, number_of_objects: _builtins.float, number_of_objects_completed: _builtins.float, object_summary: Mapping[str, outputs.DataItemMigrationSummaryResultResponse], result_prefix: _builtins.str, result_type: _builtins.str, stage: _builtins.str, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCount")
    def error_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfObjects")
    def number_of_objects(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfObjectsCompleted")
    def number_of_objects_completed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSummary")
    def object_summary(self) -> Mapping[str, outputs.DataItemMigrationSummaryResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputDatabaseLevelValidationResultResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_integrity_validation_result: outputs.DataIntegrityValidationResultResponse, ended_on: _builtins.str, id: _builtins.str, migration_id: _builtins.str, query_analysis_validation_result: outputs.QueryAnalysisValidationResultResponse, result_type: _builtins.str, schema_validation_result: outputs.SchemaComparisonValidationResultResponse, source_database_name: _builtins.str, started_on: _builtins.str, status: _builtins.str, target_database_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataIntegrityValidationResult")
    def data_integrity_validation_result(self) -> outputs.DataIntegrityValidationResultResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryAnalysisValidationResult")
    def query_analysis_validation_result(self) -> outputs.QueryAnalysisValidationResultResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaValidationResult")
    def schema_validation_result(self) -> outputs.SchemaComparisonValidationResultResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_summary: Mapping[str, outputs.DatabaseSummaryResultResponse], databases: Mapping[str, _builtins.str], duration_in_seconds: _builtins.float, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, message: _builtins.str, result_type: _builtins.str, source_server_brand_version: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, status: _builtins.str, status_message: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str, migration_report_result: Optional[outputs.MigrationReportResultResponse] = ..., migration_validation_result: Optional[outputs.MigrationValidationResultResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseSummary")
    def database_summary(self) -> Mapping[str, outputs.DatabaseSummaryResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationReportResult")
    def migration_report_result(self) -> Optional[outputs.MigrationReportResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationValidationResult")
    def migration_validation_result(self) -> Optional[outputs.MigrationValidationResultResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputTableLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, error_prefix: _builtins.str, id: _builtins.str, items_completed_count: _builtins.float, items_count: _builtins.float, object_name: _builtins.str, result_prefix: _builtins.str, result_type: _builtins.str, started_on: _builtins.str, state: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCompletedCount")
    def items_completed_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsCount")
    def items_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultPrefix")
    def result_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskOutputValidationResultResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, migration_id: _builtins.str, result_type: _builtins.str, status: _builtins.str, summary_results: Optional[Mapping[str, outputs.MigrationValidationDatabaseSummaryResultResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryResults")
    def summary_results(self) -> Optional[Mapping[str, outputs.MigrationValidationDatabaseSummaryResultResponse]]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlDbTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., created_on: Optional[_builtins.str] = ..., input: Optional[outputs.MigrateSqlServerSqlDbTaskInputResponse] = ..., is_cloneable: Optional[_builtins.bool] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSqlServerSqlDbTaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMIDatabaseInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, restore_database_name: _builtins.str, backup_file_paths: Optional[Sequence[_builtins.str]] = ..., backup_file_share: Optional[outputs.FileShareResponse] = ..., id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreDatabaseName")
    def restore_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFilePaths")
    def backup_file_paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[outputs.FileShareResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMISyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_app: outputs.AzureActiveDirectoryAppResponse, selected_databases: Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, storage_resource_id: _builtins.str, target_connection_info: outputs.MiSqlConnectionInfoResponse, backup_file_share: Optional[outputs.FileShareResponse] = ..., number_of_parallel_database_migrations: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> outputs.AzureActiveDirectoryAppResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MiSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[outputs.FileShareResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfParallelDatabaseMigrations")
    def number_of_parallel_database_migrations(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMISyncTaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_backup_sets: Sequence[outputs.BackupSetInfoResponse], container_name: _builtins.str, ended_on: _builtins.str, error_prefix: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], full_backup_set_info: outputs.BackupSetInfoResponse, id: _builtins.str, is_full_backup_restored: _builtins.bool, last_restored_backup_set_info: outputs.BackupSetInfoResponse, migration_state: _builtins.str, result_type: _builtins.str, source_database_name: _builtins.str, started_on: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeBackupSets")
    def active_backup_sets(self) -> Sequence[outputs.BackupSetInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPrefix")
    def error_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupSetInfo")
    def full_backup_set_info(self) -> outputs.BackupSetInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFullBackupRestored")
    def is_full_backup_restored(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRestoredBackupSetInfo")
    def last_restored_backup_set_info(self) -> outputs.BackupSetInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMISyncTaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMISyncTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_count: _builtins.int, database_error_count: _builtins.int, ended_on: _builtins.str, id: _builtins.str, result_type: _builtins.str, source_server_brand_version: _builtins.str, source_server_name: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, state: _builtins.str, target_server_brand_version: _builtins.str, target_server_name: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseCount")
    def database_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseErrorCount")
    def database_error_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerName")
    def source_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerName")
    def target_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMISyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., created_on: Optional[_builtins.str] = ..., input: Optional[outputs.MigrateSqlServerSqlMISyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSqlServerSqlMISyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_blob_share: outputs.BlobShareResponse, selected_databases: Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse, aad_domain_name: Optional[_builtins.str] = ..., backup_file_share: Optional[outputs.FileShareResponse] = ..., backup_mode: Optional[_builtins.str] = ..., encrypted_key_for_secure_fields: Optional[_builtins.str] = ..., selected_agent_jobs: Optional[Sequence[_builtins.str]] = ..., selected_logins: Optional[Sequence[_builtins.str]] = ..., started_on: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupBlobShare")
    def backup_blob_share(self) -> outputs.BlobShareResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadDomainName")
    def aad_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[outputs.FileShareResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMode")
    def backup_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedKeyForSecureFields")
    def encrypted_key_for_secure_fields(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedAgentJobs")
    def selected_agent_jobs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedLogins")
    def selected_logins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskOutputAgentJobLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, is_enabled: _builtins.bool, message: _builtins.str, name: _builtins.str, result_type: _builtins.str, started_on: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskOutputDatabaseLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, message: _builtins.str, result_type: _builtins.str, size_mb: _builtins.float, stage: _builtins.str, started_on: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeMB")
    def size_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskOutputErrorResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ReportableExceptionResponse, id: _builtins.str, result_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ReportableExceptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskOutputLoginLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, login_name: _builtins.str, message: _builtins.str, result_type: _builtins.str, stage: _builtins.str, started_on: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginName")
    def login_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_jobs: Mapping[str, _builtins.str], databases: Mapping[str, _builtins.str], ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, logins: Mapping[str, _builtins.str], message: _builtins.str, orphaned_users_info: Sequence[outputs.OrphanedUserInfoResponse], result_type: _builtins.str, server_role_results: Mapping[str, outputs.StartMigrationScenarioServerRoleResultResponse], source_server_brand_version: _builtins.str, source_server_version: _builtins.str, started_on: _builtins.str, state: _builtins.str, status: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentJobs")
    def agent_jobs(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logins(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orphanedUsersInfo")
    def orphaned_users_info(self) -> Sequence[outputs.OrphanedUserInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRoleResults")
    def server_role_results(self) -> Mapping[str, outputs.StartMigrationScenarioServerRoleResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSqlServerSqlMITaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., created_on: Optional[_builtins.str] = ..., input: Optional[outputs.MigrateSqlServerSqlMITaskInputResponse] = ..., is_cloneable: Optional[_builtins.bool] = ..., parent_task_id: Optional[_builtins.str] = ..., task_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSqlServerSqlMITaskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCloneable")
    def is_cloneable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentTaskId")
    def parent_task_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskId")
    def task_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSsisTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_connection_info: outputs.SqlConnectionInfoResponse, ssis_migration_info: outputs.SsisMigrationInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssisMigrationInfo")
    def ssis_migration_info(self) -> outputs.SsisMigrationInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class MigrateSsisTaskOutputMigrationLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, message: _builtins.str, result_type: _builtins.str, source_server_brand_version: _builtins.str, source_server_version: _builtins.str, stage: _builtins.str, started_on: _builtins.str, status: _builtins.str, target_server_brand_version: _builtins.str, target_server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerBrandVersion")
    def source_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerVersion")
    def source_server_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerBrandVersion")
    def target_server_brand_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServerVersion")
    def target_server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSsisTaskOutputProjectLevelResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], folder_name: _builtins.str, id: _builtins.str, message: _builtins.str, project_name: _builtins.str, result_type: _builtins.str, stage: _builtins.str, started_on: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderName")
    def folder_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSsisTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[Any], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateSsisTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSsisTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrateSyncCompleteCommandInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, commit_time_stamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitTimeStamp")
    def commit_time_stamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrateSyncCompleteCommandOutputResponse(dict):
    
    def __init__(__self__, *, errors: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrateSyncCompleteCommandPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, command_type: _builtins.str, errors: Sequence[outputs.ODataErrorResponse], output: outputs.MigrateSyncCompleteCommandOutputResponse, state: _builtins.str, command_id: Optional[_builtins.str] = ..., input: Optional[outputs.MigrateSyncCompleteCommandInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandType")
    def command_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> outputs.MigrateSyncCompleteCommandOutputResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandId")
    def command_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateSyncCompleteCommandInputResponse]:
        
        ...
    


@pulumi.output_type
class MigrationEligibilityInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_eligible_for_migration: _builtins.bool, validation_messages: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEligibleForMigration")
    def is_eligible_for_migration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationMessages")
    def validation_messages(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationReportResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., report_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportUrl")
    def report_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationStatusDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_backup_sets: Sequence[outputs.SqlBackupSetInfoResponse], blob_container_name: _builtins.str, complete_restore_error_message: _builtins.str, current_restoring_filename: _builtins.str, file_upload_blocking_errors: Sequence[_builtins.str], full_backup_set_info: outputs.SqlBackupSetInfoResponse, invalid_files: Sequence[_builtins.str], is_full_backup_restored: _builtins.bool, last_restored_backup_set_info: outputs.SqlBackupSetInfoResponse, last_restored_filename: _builtins.str, migration_state: _builtins.str, pending_log_backups_count: _builtins.int, restore_blocking_reason: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeBackupSets")
    def active_backup_sets(self) -> Sequence[outputs.SqlBackupSetInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completeRestoreErrorMessage")
    def complete_restore_error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentRestoringFilename")
    def current_restoring_filename(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUploadBlockingErrors")
    def file_upload_blocking_errors(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupSetInfo")
    def full_backup_set_info(self) -> outputs.SqlBackupSetInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFiles")
    def invalid_files(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFullBackupRestored")
    def is_full_backup_restored(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRestoredBackupSetInfo")
    def last_restored_backup_set_info(self) -> outputs.SqlBackupSetInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRestoredFilename")
    def last_restored_filename(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingLogBackupsCount")
    def pending_log_backups_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBlockingReason")
    def restore_blocking_reason(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrationValidationDatabaseSummaryResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ended_on: _builtins.str, id: _builtins.str, migration_id: _builtins.str, source_database_name: _builtins.str, started_on: _builtins.str, status: _builtins.str, target_database_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseName")
    def source_database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseName")
    def target_database_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MigrationValidationOptionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_data_integrity_validation: Optional[_builtins.bool] = ..., enable_query_analysis_validation: Optional[_builtins.bool] = ..., enable_schema_validation: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataIntegrityValidation")
    def enable_data_integrity_validation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQueryAnalysisValidation")
    def enable_query_analysis_validation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSchemaValidation")
    def enable_schema_validation(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MigrationValidationResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, migration_id: _builtins.str, status: _builtins.str, summary_results: Optional[Mapping[str, outputs.MigrationValidationDatabaseSummaryResultResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryResults")
    def summary_results(self) -> Optional[Mapping[str, outputs.MigrationValidationDatabaseSummaryResultResponse]]:
        
        ...
    


@pulumi.output_type
class MongoConnectionInformationResponse(dict):
    
    def __init__(__self__, *, host: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoDbClusterInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Sequence[outputs.MongoDbDatabaseInfoResponse], supports_sharding: _builtins.bool, type: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[outputs.MongoDbDatabaseInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsSharding")
    def supports_sharding(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MongoDbCollectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, average_document_size: _builtins.float, data_size: _builtins.float, database_name: _builtins.str, document_count: _builtins.float, is_capped: _builtins.bool, is_system_collection: _builtins.bool, is_view: _builtins.bool, name: _builtins.str, qualified_name: _builtins.str, supports_sharding: _builtins.bool, shard_key: Optional[outputs.MongoDbShardKeyInfoResponse] = ..., view_of: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageDocumentSize")
    def average_document_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentCount")
    def document_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCapped")
    def is_capped(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSystemCollection")
    def is_system_collection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isView")
    def is_view(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsSharding")
    def supports_sharding(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardKey")
    def shard_key(self) -> Optional[outputs.MongoDbShardKeyInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOf")
    def view_of(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbCollectionProgressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bytes_copied: _builtins.float, documents_copied: _builtins.float, elapsed_time: _builtins.str, errors: Mapping[str, outputs.MongoDbErrorResponse], events_pending: _builtins.float, events_replayed: _builtins.float, result_type: _builtins.str, state: _builtins.str, total_bytes: _builtins.float, total_documents: _builtins.float, last_event_time: Optional[_builtins.str] = ..., last_replay_time: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., qualified_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesCopied")
    def bytes_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentsCopied")
    def documents_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elapsedTime")
    def elapsed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Mapping[str, outputs.MongoDbErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsPending")
    def events_pending(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsReplayed")
    def events_replayed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBytes")
    def total_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDocuments")
    def total_documents(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEventTime")
    def last_event_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplayTime")
    def last_replay_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbCollectionSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, can_delete: Optional[_builtins.bool] = ..., shard_key: Optional[outputs.MongoDbShardKeySettingResponse] = ..., target_rus: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canDelete")
    def can_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardKey")
    def shard_key(self) -> Optional[outputs.MongoDbShardKeySettingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRUs")
    def target_rus(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoDbConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_string: _builtins.str, type: _builtins.str, additional_settings: Optional[_builtins.str] = ..., authentication: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ..., encrypt_connection: Optional[_builtins.bool] = ..., enforce_ssl: Optional[_builtins.bool] = ..., password: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., server_brand_version: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., trust_server_certificate: Optional[_builtins.bool] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceSSL")
    def enforce_ssl(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbDatabaseInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, average_document_size: _builtins.float, collections: Sequence[outputs.MongoDbCollectionInfoResponse], data_size: _builtins.float, document_count: _builtins.float, name: _builtins.str, qualified_name: _builtins.str, supports_sharding: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageDocumentSize")
    def average_document_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collections(self) -> Sequence[outputs.MongoDbCollectionInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentCount")
    def document_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsSharding")
    def supports_sharding(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class MongoDbDatabaseProgressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bytes_copied: _builtins.float, documents_copied: _builtins.float, elapsed_time: _builtins.str, errors: Mapping[str, outputs.MongoDbErrorResponse], events_pending: _builtins.float, events_replayed: _builtins.float, result_type: _builtins.str, state: _builtins.str, total_bytes: _builtins.float, total_documents: _builtins.float, collections: Optional[Mapping[str, outputs.MongoDbCollectionProgressResponse]] = ..., last_event_time: Optional[_builtins.str] = ..., last_replay_time: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., qualified_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesCopied")
    def bytes_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentsCopied")
    def documents_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elapsedTime")
    def elapsed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Mapping[str, outputs.MongoDbErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsPending")
    def events_pending(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsReplayed")
    def events_replayed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBytes")
    def total_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDocuments")
    def total_documents(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collections(self) -> Optional[Mapping[str, outputs.MongoDbCollectionProgressResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEventTime")
    def last_event_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplayTime")
    def last_replay_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbDatabaseSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collections: Mapping[str, outputs.MongoDbCollectionSettingsResponse], target_rus: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collections(self) -> Mapping[str, outputs.MongoDbCollectionSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRUs")
    def target_rus(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoDbErrorResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., count: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbMigrationProgressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bytes_copied: _builtins.float, documents_copied: _builtins.float, elapsed_time: _builtins.str, errors: Mapping[str, outputs.MongoDbErrorResponse], events_pending: _builtins.float, events_replayed: _builtins.float, result_type: _builtins.str, state: _builtins.str, total_bytes: _builtins.float, total_documents: _builtins.float, databases: Optional[Mapping[str, outputs.MongoDbDatabaseProgressResponse]] = ..., last_event_time: Optional[_builtins.str] = ..., last_replay_time: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., qualified_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesCopied")
    def bytes_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentsCopied")
    def documents_copied(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elapsedTime")
    def elapsed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Mapping[str, outputs.MongoDbErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsPending")
    def events_pending(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsReplayed")
    def events_replayed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultType")
    def result_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBytes")
    def total_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDocuments")
    def total_documents(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Optional[Mapping[str, outputs.MongoDbDatabaseProgressResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEventTime")
    def last_event_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplayTime")
    def last_replay_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoDbMigrationSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, databases: Mapping[str, outputs.MongoDbDatabaseSettingsResponse], source: outputs.MongoDbConnectionInfoResponse, target: outputs.MongoDbConnectionInfoResponse, boost_rus: Optional[_builtins.int] = ..., replication: Optional[_builtins.str] = ..., throttling: Optional[outputs.MongoDbThrottlingSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Mapping[str, outputs.MongoDbDatabaseSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.MongoDbConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> outputs.MongoDbConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostRUs")
    def boost_rus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throttling(self) -> Optional[outputs.MongoDbThrottlingSettingsResponse]:
        
        ...
    


@pulumi.output_type
class MongoDbShardKeyFieldResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, order: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MongoDbShardKeyInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fields: Sequence[outputs.MongoDbShardKeyFieldResponse], is_unique: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.MongoDbShardKeyFieldResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUnique")
    def is_unique(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class MongoDbShardKeySettingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fields: Sequence[outputs.MongoDbShardKeyFieldResponse], is_unique: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.MongoDbShardKeyFieldResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUnique")
    def is_unique(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MongoDbThrottlingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_parallelism: Optional[_builtins.int] = ..., min_free_cpu: Optional[_builtins.int] = ..., min_free_memory_mb: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelism")
    def max_parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minFreeCpu")
    def min_free_cpu(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minFreeMemoryMb")
    def min_free_memory_mb(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MongoMigrationCollectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, migration_progress_details: outputs.MongoMigrationProgressDetailsResponse, source_collection: Optional[_builtins.str] = ..., source_database: Optional[_builtins.str] = ..., target_collection: Optional[_builtins.str] = ..., target_database: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationProgressDetails")
    def migration_progress_details(self) -> outputs.MongoMigrationProgressDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCollection")
    def source_collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabase")
    def source_database(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCollection")
    def target_collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabase")
    def target_database(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MongoMigrationProgressDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration_in_seconds: _builtins.int, migration_error: _builtins.str, migration_status: _builtins.str, processed_document_count: _builtins.float, source_document_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInSeconds")
    def duration_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationError")
    def migration_error(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processedDocumentCount")
    def processed_document_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDocumentCount")
    def source_document_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MySqlConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, server_name: _builtins.str, type: _builtins.str, additional_settings: Optional[_builtins.str] = ..., authentication: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ..., encrypt_connection: Optional[_builtins.bool] = ..., password: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeMonitoringDataResponse(dict):
    def __init__(__self__, *, additional_properties: Mapping[str, Any], available_memory_in_mb: _builtins.int, concurrent_jobs_limit: _builtins.int, concurrent_jobs_running: _builtins.int, cpu_utilization: _builtins.int, max_concurrent_jobs: _builtins.int, node_name: _builtins.str, received_bytes: _builtins.float, sent_bytes: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Mapping[str, Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryInMB")
    def available_memory_in_mb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrentJobsLimit")
    def concurrent_jobs_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrentJobsRunning")
    def concurrent_jobs_running(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentJobs")
    def max_concurrent_jobs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="receivedBytes")
    def received_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sentBytes")
    def sent_bytes(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ODataErrorResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., details: Optional[Sequence[outputs.ODataErrorResponse]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.ODataErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OfflineConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_backup_name: Optional[_builtins.str] = ..., offline: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupName")
    def last_backup_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offline(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OracleConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source: _builtins.str, type: _builtins.str, authentication: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., server_name: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrphanedUserInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PostgreSqlConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, server_name: _builtins.str, type: _builtins.str, additional_settings: Optional[_builtins.str] = ..., authentication: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., encrypt_connection: Optional[_builtins.bool] = ..., password: Optional[_builtins.str] = ..., server_brand_version: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., trust_server_certificate: Optional[_builtins.bool] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectFilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_modified: _builtins.str, size: _builtins.float, extension: Optional[_builtins.str] = ..., file_path: Optional[_builtins.str] = ..., media_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QueryAnalysisValidationResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, query_results: Optional[outputs.QueryExecutionResultResponse] = ..., validation_errors: Optional[outputs.ValidationErrorResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryResults")
    def query_results(self) -> Optional[outputs.QueryExecutionResultResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[outputs.ValidationErrorResponse]:
        
        ...
    


@pulumi.output_type
class QueryExecutionResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, query_text: Optional[_builtins.str] = ..., source_result: Optional[outputs.ExecutionStatisticsResponse] = ..., statements_in_batch: Optional[_builtins.float] = ..., target_result: Optional[outputs.ExecutionStatisticsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryText")
    def query_text(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResult")
    def source_result(self) -> Optional[outputs.ExecutionStatisticsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementsInBatch")
    def statements_in_batch(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResult")
    def target_result(self) -> Optional[outputs.ExecutionStatisticsResponse]:
        
        ...
    


@pulumi.output_type
class ReportableExceptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actionable_message: Optional[_builtins.str] = ..., file_path: Optional[_builtins.str] = ..., h_result: Optional[_builtins.int] = ..., line_number: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., stack_trace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionableMessage")
    def actionable_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hResult")
    def h_result(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineNumber")
    def line_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackTrace")
    def stack_trace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SchemaComparisonValidationResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schema_differences: Optional[outputs.SchemaComparisonValidationResultTypeResponse] = ..., source_database_object_count: Optional[Mapping[str, _builtins.float]] = ..., target_database_object_count: Optional[Mapping[str, _builtins.float]] = ..., validation_errors: Optional[outputs.ValidationErrorResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDifferences")
    def schema_differences(self) -> Optional[outputs.SchemaComparisonValidationResultTypeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseObjectCount")
    def source_database_object_count(self) -> Optional[Mapping[str, _builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDatabaseObjectCount")
    def target_database_object_count(self) -> Optional[Mapping[str, _builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[outputs.ValidationErrorResponse]:
        
        ...
    


@pulumi.output_type
class SchemaComparisonValidationResultTypeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, object_name: Optional[_builtins.str] = ..., object_type: Optional[_builtins.str] = ..., update_action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateAction")
    def update_action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SelectedCertificateInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_name: _builtins.str, password: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_database_count: _builtins.int, server_edition: _builtins.str, server_name: _builtins.str, server_operating_system_version: _builtins.str, server_platform: _builtins.str, server_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverDatabaseCount")
    def server_database_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverEdition")
    def server_edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverOperatingSystemVersion")
    def server_operating_system_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverPlatform")
    def server_platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceSkuResponse(dict):
    
    def __init__(__self__, *, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
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
    def name(self) -> Optional[_builtins.str]:
        
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
class SourceLocationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_storage_type: _builtins.str, azure_blob: Optional[outputs.AzureBlobResponse] = ..., file_share: Optional[outputs.SqlFileShareResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileStorageType")
    def file_storage_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlob")
    def azure_blob(self) -> Optional[outputs.AzureBlobResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> Optional[outputs.SqlFileShareResponse]:
        
        ...
    


@pulumi.output_type
class SqlBackupFileInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, copy_duration: _builtins.int, copy_throughput: _builtins.float, data_read: _builtins.float, data_written: _builtins.float, family_sequence_number: _builtins.int, file_name: _builtins.str, status: _builtins.str, total_size: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyDuration")
    def copy_duration(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyThroughput")
    def copy_throughput(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRead")
    def data_read(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataWritten")
    def data_written(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familySequenceNumber")
    def family_sequence_number(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSize")
    def total_size(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class SqlBackupSetInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_finish_date: _builtins.str, backup_set_id: _builtins.str, backup_start_date: _builtins.str, backup_type: _builtins.str, family_count: _builtins.int, first_lsn: _builtins.str, has_backup_checksums: _builtins.bool, ignore_reasons: Sequence[_builtins.str], is_backup_restored: _builtins.bool, last_lsn: _builtins.str, list_of_backup_files: Sequence[outputs.SqlBackupFileInfoResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFinishDate")
    def backup_finish_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetId")
    def backup_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStartDate")
    def backup_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="familyCount")
    def family_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstLSN")
    def first_lsn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasBackupChecksums")
    def has_backup_checksums(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreReasons")
    def ignore_reasons(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBackupRestored")
    def is_backup_restored(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastLSN")
    def last_lsn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listOfBackupFiles")
    def list_of_backup_files(self) -> Sequence[outputs.SqlBackupFileInfoResponse]:
        
        ...
    


@pulumi.output_type
class SqlConnectionInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source: _builtins.str, type: _builtins.str, additional_settings: Optional[_builtins.str] = ..., authentication: Optional[_builtins.str] = ..., encrypt_connection: Optional[_builtins.bool] = ..., password: Optional[_builtins.str] = ..., platform: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., resource_id: Optional[_builtins.str] = ..., server_brand_version: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., trust_server_certificate: Optional[_builtins.bool] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSettings")
    def additional_settings(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBrandVersion")
    def server_brand_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlConnectionInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ..., encrypt_connection: Optional[_builtins.bool] = ..., password: Optional[_builtins.str] = ..., trust_server_certificate: Optional[_builtins.bool] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptConnection")
    def encrypt_connection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustServerCertificate")
    def trust_server_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlDbMigrationStatusDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, list_of_copy_progress_details: Sequence[outputs.CopyProgressDetailsResponse], migration_state: _builtins.str, sql_data_copy_errors: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listOfCopyProgressDetails")
    def list_of_copy_progress_details(self) -> Sequence[outputs.CopyProgressDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlDataCopyErrors")
    def sql_data_copy_errors(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlDbOfflineConfigurationResponse(dict):
    
    def __init__(__self__, *, offline: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offline(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class SqlFileShareResponse(dict):
    
    def __init__(__self__, *, path: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SsisMigrationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, environment_overwrite_option: Optional[_builtins.str] = ..., project_overwrite_option: Optional[_builtins.str] = ..., ssis_store_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentOverwriteOption")
    def environment_overwrite_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectOverwriteOption")
    def project_overwrite_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssisStoreType")
    def ssis_store_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StartMigrationScenarioServerRoleResultResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exceptions_and_warnings: Sequence[outputs.ReportableExceptionResponse], name: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionsAndWarnings")
    def exceptions_and_warnings(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SyncMigrationDatabaseErrorEventResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_text: _builtins.str, event_type_string: _builtins.str, timestamp_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventText")
    def event_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTypeString")
    def event_type_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampString")
    def timestamp_string(self) -> _builtins.str:
        
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
class TargetLocationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_key: Optional[_builtins.str] = ..., storage_account_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
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
class ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ValidateSyncMigrationInputSqlServerTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ValidateSyncMigrationInputSqlServerTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ValidateSyncMigrationInputSqlServerTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ValidateSyncMigrationInputSqlServerTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMISyncTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_app: outputs.AzureActiveDirectoryAppResponse, selected_databases: Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, storage_resource_id: _builtins.str, target_connection_info: outputs.MiSqlConnectionInfoResponse, backup_file_share: Optional[outputs.FileShareResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApp")
    def azure_app(self) -> outputs.AzureActiveDirectoryAppResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.MiSqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[outputs.FileShareResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMISyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
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
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ValidateMigrationInputSqlServerSqlMISyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ValidateMigrationInputSqlServerSqlMISyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ValidateMigrationInputSqlServerSqlMISyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ValidateMigrationInputSqlServerSqlMISyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMITaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_blob_share: outputs.BlobShareResponse, selected_databases: Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse, backup_file_share: Optional[outputs.FileShareResponse] = ..., backup_mode: Optional[_builtins.str] = ..., selected_logins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupBlobShare")
    def backup_blob_share(self) -> outputs.BlobShareResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlMIDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFileShare")
    def backup_file_share(self) -> Optional[outputs.FileShareResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMode")
    def backup_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedLogins")
    def selected_logins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMITaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_folder_errors: Sequence[outputs.ReportableExceptionResponse], backup_share_credentials_errors: Sequence[outputs.ReportableExceptionResponse], backup_storage_account_errors: Sequence[outputs.ReportableExceptionResponse], existing_backup_errors: Sequence[outputs.ReportableExceptionResponse], id: _builtins.str, name: _builtins.str, restore_database_name_errors: Sequence[outputs.ReportableExceptionResponse], database_backup_info: Optional[outputs.DatabaseBackupInfoResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupFolderErrors")
    def backup_folder_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupShareCredentialsErrors")
    def backup_share_credentials_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageAccountErrors")
    def backup_storage_account_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingBackupErrors")
    def existing_backup_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
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
    @pulumi.getter(name="restoreDatabaseNameErrors")
    def restore_database_name_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseBackupInfo")
    def database_backup_info(self) -> Optional[outputs.DatabaseBackupInfoResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMigrationInputSqlServerSqlMITaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ValidateMigrationInputSqlServerSqlMITaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.ValidateMigrationInputSqlServerSqlMITaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ValidateMigrationInputSqlServerSqlMITaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.ValidateMigrationInputSqlServerSqlMITaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ValidateMongoDbTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.MongoDbMigrationProgressResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MongoDbMigrationSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.MongoDbMigrationProgressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MongoDbMigrationSettingsResponse]:
        
        ...
    


@pulumi.output_type
class ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Sequence[Any], errors: Sequence[outputs.ODataErrorResponse], output: Sequence[outputs.ValidateOracleAzureDbPostgreSqlSyncTaskOutputResponse], state: _builtins.str, task_type: _builtins.str, client_data: Optional[Mapping[str, _builtins.str]] = ..., input: Optional[outputs.MigrateOracleAzureDbPostgreSqlSyncTaskInputResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.ODataErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Sequence[outputs.ValidateOracleAzureDbPostgreSqlSyncTaskOutputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientData")
    def client_data(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.MigrateOracleAzureDbPostgreSqlSyncTaskInputResponse]:
        
        ...
    


@pulumi.output_type
class ValidateOracleAzureDbPostgreSqlSyncTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ValidateSyncMigrationInputSqlServerTaskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, selected_databases: Sequence[outputs.MigrateSqlServerSqlDbSyncDatabaseInputResponse], source_connection_info: outputs.SqlConnectionInfoResponse, target_connection_info: outputs.SqlConnectionInfoResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedDatabases")
    def selected_databases(self) -> Sequence[outputs.MigrateSqlServerSqlDbSyncDatabaseInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> outputs.SqlConnectionInfoResponse:
        
        ...
    


@pulumi.output_type
class ValidateSyncMigrationInputSqlServerTaskOutputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, validation_errors: Sequence[outputs.ReportableExceptionResponse]) -> None:
        
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
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[outputs.ReportableExceptionResponse]:
        
        ...
    


@pulumi.output_type
class ValidationErrorResponse(dict):
    
    def __init__(__self__, *, severity: Optional[_builtins.str] = ..., text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WaitStatisticsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, wait_count: Optional[_builtins.float] = ..., wait_time_ms: Optional[_builtins.float] = ..., wait_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitCount")
    def wait_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitTimeMs")
    def wait_time_ms(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitType")
    def wait_type(self) -> Optional[_builtins.str]:
        
        ...
    


