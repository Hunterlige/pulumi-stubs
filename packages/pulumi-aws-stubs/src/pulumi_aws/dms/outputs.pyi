

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointElasticsearchSettings', 'EndpointKafkaSettings', 'EndpointKinesisSettings', 'EndpointMongodbSettings', 'EndpointMysqlSettings', 'EndpointOracleSettings', 'EndpointPostgresSettings', 'EndpointRedisSettings', 'EndpointRedshiftSettings', 'ReplicationConfigComputeConfig', 'ReplicationInstanceKerberosAuthenticationSettings', 'GetEndpointElasticsearchSettingResult', 'GetEndpointKafkaSettingResult', 'GetEndpointKinesisSettingResult', 'GetEndpointMongodbSettingResult', 'GetEndpointMysqlSettingResult', 'GetEndpointPostgresSettingResult', 'GetEndpointRedisSettingResult', 'GetEndpointRedshiftSettingResult', 'GetEndpointS3SettingResult']
@pulumi.output_type
class EndpointElasticsearchSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint_uri: _builtins.str, service_access_role_arn: _builtins.str, error_retry_duration: Optional[_builtins.int] = ..., full_load_error_percentage: Optional[_builtins.int] = ..., use_new_mapping_type: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorRetryDuration")
    def error_retry_duration(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useNewMappingType")
    def use_new_mapping_type(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EndpointKafkaSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, broker: _builtins.str, include_control_details: Optional[_builtins.bool] = ..., include_null_and_empty: Optional[_builtins.bool] = ..., include_partition_value: Optional[_builtins.bool] = ..., include_table_alter_operations: Optional[_builtins.bool] = ..., include_transaction_details: Optional[_builtins.bool] = ..., message_format: Optional[_builtins.str] = ..., message_max_bytes: Optional[_builtins.int] = ..., no_hex_prefix: Optional[_builtins.bool] = ..., partition_include_schema_table: Optional[_builtins.bool] = ..., sasl_mechanism: Optional[_builtins.str] = ..., sasl_password: Optional[_builtins.str] = ..., sasl_username: Optional[_builtins.str] = ..., security_protocol: Optional[_builtins.str] = ..., ssl_ca_certificate_arn: Optional[_builtins.str] = ..., ssl_client_certificate_arn: Optional[_builtins.str] = ..., ssl_client_key_arn: Optional[_builtins.str] = ..., ssl_client_key_password: Optional[_builtins.str] = ..., topic: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def broker(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageMaxBytes")
    def message_max_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noHexPrefix")
    def no_hex_prefix(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslMechanism")
    def sasl_mechanism(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslPassword")
    def sasl_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslUsername")
    def sasl_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProtocol")
    def security_protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointKinesisSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_control_details: Optional[_builtins.bool] = ..., include_null_and_empty: Optional[_builtins.bool] = ..., include_partition_value: Optional[_builtins.bool] = ..., include_table_alter_operations: Optional[_builtins.bool] = ..., include_transaction_details: Optional[_builtins.bool] = ..., message_format: Optional[_builtins.str] = ..., partition_include_schema_table: Optional[_builtins.bool] = ..., service_access_role_arn: Optional[_builtins.str] = ..., stream_arn: Optional[_builtins.str] = ..., use_large_integer_value: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLargeIntegerValue")
    def use_large_integer_value(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EndpointMongodbSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_mechanism: Optional[_builtins.str] = ..., auth_source: Optional[_builtins.str] = ..., auth_type: Optional[_builtins.str] = ..., docs_to_investigate: Optional[_builtins.str] = ..., extract_doc_id: Optional[_builtins.str] = ..., nesting_level: Optional[_builtins.str] = ..., use_update_lookup: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authMechanism")
    def auth_mechanism(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authSource")
    def auth_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="docsToInvestigate")
    def docs_to_investigate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extractDocId")
    def extract_doc_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestingLevel")
    def nesting_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useUpdateLookup")
    def use_update_lookup(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EndpointMysqlSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, after_connect_script: Optional[_builtins.str] = ..., authentication_method: Optional[_builtins.str] = ..., clean_source_metadata_on_mismatch: Optional[_builtins.bool] = ..., events_poll_interval: Optional[_builtins.int] = ..., execute_timeout: Optional[_builtins.int] = ..., max_file_size: Optional[_builtins.int] = ..., parallel_load_threads: Optional[_builtins.int] = ..., server_timezone: Optional[_builtins.str] = ..., service_access_role_arn: Optional[_builtins.str] = ..., target_db_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanSourceMetadataOnMismatch")
    def clean_source_metadata_on_mismatch(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsPollInterval")
    def events_poll_interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelLoadThreads")
    def parallel_load_threads(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTimezone")
    def server_timezone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDbType")
    def target_db_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointOracleSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_alternate_directly: Optional[_builtins.bool] = ..., add_supplemental_logging: Optional[_builtins.bool] = ..., additional_archived_log_dest_id: Optional[_builtins.int] = ..., allow_selected_nested_tables: Optional[_builtins.bool] = ..., archived_log_dest_id: Optional[_builtins.int] = ..., archived_logs_only: Optional[_builtins.bool] = ..., asm_password: Optional[_builtins.str] = ..., asm_server: Optional[_builtins.str] = ..., asm_user: Optional[_builtins.str] = ..., authentication_method: Optional[_builtins.str] = ..., char_length_semantics: Optional[_builtins.str] = ..., convert_timestamp_with_zone_to_utc: Optional[_builtins.bool] = ..., direct_path_no_log: Optional[_builtins.bool] = ..., direct_path_parallel_load: Optional[_builtins.bool] = ..., enable_homogenous_tablespace: Optional[_builtins.bool] = ..., extra_archived_log_dest_ids: Optional[Sequence[_builtins.int]] = ..., fail_task_on_lob_truncation: Optional[_builtins.bool] = ..., number_datatype_scale: Optional[_builtins.int] = ..., open_transaction_window: Optional[_builtins.int] = ..., oracle_path_prefix: Optional[_builtins.str] = ..., parallel_asm_read_threads: Optional[_builtins.int] = ..., read_ahead_blocks: Optional[_builtins.int] = ..., read_table_space_name: Optional[_builtins.bool] = ..., replace_path_prefix: Optional[_builtins.bool] = ..., retry_interval: Optional[_builtins.int] = ..., secrets_manager_oracle_asm_access_role_arn: Optional[_builtins.str] = ..., secrets_manager_oracle_asm_secret_id: Optional[_builtins.str] = ..., security_db_encryption: Optional[_builtins.str] = ..., security_db_encryption_name: Optional[_builtins.str] = ..., spatial_data_option_to_geo_json_function_name: Optional[_builtins.str] = ..., standby_delay_time: Optional[_builtins.int] = ..., trim_space_in_char: Optional[_builtins.bool] = ..., use_alternate_folder_for_online: Optional[_builtins.bool] = ..., use_bfile: Optional[_builtins.bool] = ..., use_direct_path_full_load: Optional[_builtins.bool] = ..., use_logminer_reader: Optional[_builtins.bool] = ..., use_path_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessAlternateDirectly")
    def access_alternate_directly(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addSupplementalLogging")
    def add_supplemental_logging(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalArchivedLogDestId")
    def additional_archived_log_dest_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSelectedNestedTables")
    def allow_selected_nested_tables(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archivedLogDestId")
    def archived_log_dest_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archivedLogsOnly")
    def archived_logs_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asmPassword")
    def asm_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asmServer")
    def asm_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asmUser")
    def asm_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charLengthSemantics")
    def char_length_semantics(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="convertTimestampWithZoneToUtc")
    def convert_timestamp_with_zone_to_utc(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directPathNoLog")
    def direct_path_no_log(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directPathParallelLoad")
    def direct_path_parallel_load(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHomogenousTablespace")
    def enable_homogenous_tablespace(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraArchivedLogDestIds")
    def extra_archived_log_dest_ids(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failTaskOnLobTruncation")
    def fail_task_on_lob_truncation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberDatatypeScale")
    def number_datatype_scale(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openTransactionWindow")
    def open_transaction_window(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oraclePathPrefix")
    def oracle_path_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelAsmReadThreads")
    def parallel_asm_read_threads(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAheadBlocks")
    def read_ahead_blocks(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readTableSpaceName")
    def read_table_space_name(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacePathPrefix")
    def replace_path_prefix(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerOracleAsmAccessRoleArn")
    def secrets_manager_oracle_asm_access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerOracleAsmSecretId")
    def secrets_manager_oracle_asm_secret_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityDbEncryption")
    def security_db_encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityDbEncryptionName")
    def security_db_encryption_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spatialDataOptionToGeoJsonFunctionName")
    def spatial_data_option_to_geo_json_function_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyDelayTime")
    def standby_delay_time(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trimSpaceInChar")
    def trim_space_in_char(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAlternateFolderForOnline")
    def use_alternate_folder_for_online(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useBfile")
    def use_bfile(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDirectPathFullLoad")
    def use_direct_path_full_load(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLogminerReader")
    def use_logminer_reader(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePathPrefix")
    def use_path_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointPostgresSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, after_connect_script: Optional[_builtins.str] = ..., authentication_method: Optional[_builtins.str] = ..., babelfish_database_name: Optional[_builtins.str] = ..., capture_ddls: Optional[_builtins.bool] = ..., database_mode: Optional[_builtins.str] = ..., ddl_artifacts_schema: Optional[_builtins.str] = ..., execute_timeout: Optional[_builtins.int] = ..., fail_tasks_on_lob_truncation: Optional[_builtins.bool] = ..., heartbeat_enable: Optional[_builtins.bool] = ..., heartbeat_frequency: Optional[_builtins.int] = ..., heartbeat_schema: Optional[_builtins.str] = ..., map_boolean_as_boolean: Optional[_builtins.bool] = ..., map_jsonb_as_clob: Optional[_builtins.bool] = ..., map_long_varchar_as: Optional[_builtins.str] = ..., max_file_size: Optional[_builtins.int] = ..., plugin_name: Optional[_builtins.str] = ..., service_access_role_arn: Optional[_builtins.str] = ..., slot_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="babelfishDatabaseName")
    def babelfish_database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureDdls")
    def capture_ddls(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseMode")
    def database_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddlArtifactsSchema")
    def ddl_artifacts_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failTasksOnLobTruncation")
    def fail_tasks_on_lob_truncation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatEnable")
    def heartbeat_enable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatFrequency")
    def heartbeat_frequency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatSchema")
    def heartbeat_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBooleanAsBoolean")
    def map_boolean_as_boolean(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapJsonbAsClob")
    def map_jsonb_as_clob(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapLongVarcharAs")
    def map_long_varchar_as(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotName")
    def slot_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointRedisSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, port: _builtins.int, server_name: _builtins.str, auth_password: Optional[_builtins.str] = ..., auth_user_name: Optional[_builtins.str] = ..., ssl_ca_certificate_arn: Optional[_builtins.str] = ..., ssl_security_protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
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
    @pulumi.getter(name="authPassword")
    def auth_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authUserName")
    def auth_user_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSecurityProtocol")
    def ssl_security_protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointRedshiftSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_folder: Optional[_builtins.str] = ..., bucket_name: Optional[_builtins.str] = ..., encryption_mode: Optional[_builtins.str] = ..., server_side_encryption_kms_key_id: Optional[_builtins.str] = ..., service_access_role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReplicationConfigComputeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replication_subnet_group_id: _builtins.str, availability_zone: Optional[_builtins.str] = ..., dns_name_servers: Optional[_builtins.str] = ..., kms_key_id: Optional[_builtins.str] = ..., max_capacity_units: Optional[_builtins.int] = ..., min_capacity_units: Optional[_builtins.int] = ..., multi_az: Optional[_builtins.bool] = ..., preferred_maintenance_window: Optional[_builtins.str] = ..., vpc_security_group_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNameServers")
    def dns_name_servers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacityUnits")
    def max_capacity_units(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCapacityUnits")
    def min_capacity_units(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ReplicationInstanceKerberosAuthenticationSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_cache_secret_iam_arn: _builtins.str, key_cache_secret_id: _builtins.str, krb5_file_contents: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyCacheSecretIamArn")
    def key_cache_secret_iam_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyCacheSecretId")
    def key_cache_secret_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="krb5FileContents")
    def krb5_file_contents(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEndpointElasticsearchSettingResult(dict):
    def __init__(__self__, *, endpoint_uri: _builtins.str, error_retry_duration: _builtins.int, full_load_error_percentage: _builtins.int, service_access_role_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorRetryDuration")
    def error_retry_duration(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointKafkaSettingResult(dict):
    def __init__(__self__, *, broker: _builtins.str, include_control_details: _builtins.bool, include_null_and_empty: _builtins.bool, include_partition_value: _builtins.bool, include_table_alter_operations: _builtins.bool, include_transaction_details: _builtins.bool, message_format: _builtins.str, message_max_bytes: _builtins.int, no_hex_prefix: _builtins.bool, partition_include_schema_table: _builtins.bool, sasl_mechanism: _builtins.str, sasl_password: _builtins.str, sasl_username: _builtins.str, security_protocol: _builtins.str, ssl_ca_certificate_arn: _builtins.str, ssl_client_certificate_arn: _builtins.str, ssl_client_key_arn: _builtins.str, ssl_client_key_password: _builtins.str, topic: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def broker(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageMaxBytes")
    def message_max_bytes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noHexPrefix")
    def no_hex_prefix(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslMechanism")
    def sasl_mechanism(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslPassword")
    def sasl_password(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslUsername")
    def sasl_username(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProtocol")
    def security_protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointKinesisSettingResult(dict):
    def __init__(__self__, *, include_control_details: _builtins.bool, include_null_and_empty: _builtins.bool, include_partition_value: _builtins.bool, include_table_alter_operations: _builtins.bool, include_transaction_details: _builtins.bool, message_format: _builtins.str, partition_include_schema_table: _builtins.bool, service_access_role_arn: _builtins.str, stream_arn: _builtins.str, use_large_integer_value: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLargeIntegerValue")
    def use_large_integer_value(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetEndpointMongodbSettingResult(dict):
    def __init__(__self__, *, auth_mechanism: _builtins.str, auth_source: _builtins.str, auth_type: _builtins.str, docs_to_investigate: _builtins.str, extract_doc_id: _builtins.str, nesting_level: _builtins.str, use_update_lookup: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authMechanism")
    def auth_mechanism(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authSource")
    def auth_source(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="docsToInvestigate")
    def docs_to_investigate(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extractDocId")
    def extract_doc_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nestingLevel")
    def nesting_level(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useUpdateLookup")
    def use_update_lookup(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetEndpointMysqlSettingResult(dict):
    def __init__(__self__, *, after_connect_script: _builtins.str, authentication_method: _builtins.str, clean_source_metadata_on_mismatch: _builtins.bool, events_poll_interval: _builtins.int, execute_timeout: _builtins.int, max_file_size: _builtins.int, parallel_load_threads: _builtins.int, server_timezone: _builtins.str, service_access_role_arn: _builtins.str, target_db_type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanSourceMetadataOnMismatch")
    def clean_source_metadata_on_mismatch(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsPollInterval")
    def events_poll_interval(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelLoadThreads")
    def parallel_load_threads(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTimezone")
    def server_timezone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDbType")
    def target_db_type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointPostgresSettingResult(dict):
    def __init__(__self__, *, after_connect_script: _builtins.str, authentication_method: _builtins.str, babelfish_database_name: _builtins.str, capture_ddls: _builtins.bool, database_mode: _builtins.str, ddl_artifacts_schema: _builtins.str, execute_timeout: _builtins.int, fail_tasks_on_lob_truncation: _builtins.bool, heartbeat_enable: _builtins.bool, heartbeat_frequency: _builtins.int, heartbeat_schema: _builtins.str, map_boolean_as_boolean: _builtins.bool, map_jsonb_as_clob: _builtins.bool, map_long_varchar_as: _builtins.str, max_file_size: _builtins.int, plugin_name: _builtins.str, service_access_role_arn: _builtins.str, slot_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="babelfishDatabaseName")
    def babelfish_database_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureDdls")
    def capture_ddls(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseMode")
    def database_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddlArtifactsSchema")
    def ddl_artifacts_schema(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failTasksOnLobTruncation")
    def fail_tasks_on_lob_truncation(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatEnable")
    def heartbeat_enable(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatFrequency")
    def heartbeat_frequency(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatSchema")
    def heartbeat_schema(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBooleanAsBoolean")
    def map_boolean_as_boolean(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapJsonbAsClob")
    def map_jsonb_as_clob(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapLongVarcharAs")
    def map_long_varchar_as(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotName")
    def slot_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointRedisSettingResult(dict):
    def __init__(__self__, *, auth_password: _builtins.str, auth_type: _builtins.str, auth_user_name: _builtins.str, port: _builtins.int, server_name: _builtins.str, ssl_ca_certificate_arn: _builtins.str, ssl_security_protocol: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authPassword")
    def auth_password(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authUserName")
    def auth_user_name(self) -> _builtins.str:
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
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSecurityProtocol")
    def ssl_security_protocol(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointRedshiftSettingResult(dict):
    def __init__(__self__, *, bucket_folder: _builtins.str, bucket_name: _builtins.str, encryption_mode: _builtins.str, server_side_encryption_kms_key_id: _builtins.str, service_access_role_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointS3SettingResult(dict):
    def __init__(__self__, *, add_column_name: _builtins.bool, bucket_folder: _builtins.str, bucket_name: _builtins.str, canned_acl_for_objects: _builtins.str, cdc_inserts_and_updates: _builtins.bool, cdc_inserts_only: _builtins.bool, cdc_max_batch_interval: _builtins.int, cdc_min_file_size: _builtins.int, cdc_path: _builtins.str, compression_type: _builtins.str, csv_delimiter: _builtins.str, csv_no_sup_value: _builtins.str, csv_null_value: _builtins.str, csv_row_delimiter: _builtins.str, data_format: _builtins.str, data_page_size: _builtins.int, date_partition_delimiter: _builtins.str, date_partition_enabled: _builtins.bool, date_partition_sequence: _builtins.str, dict_page_size_limit: _builtins.int, enable_statistics: _builtins.bool, encoding_type: _builtins.str, encryption_mode: _builtins.str, external_table_definition: _builtins.str, glue_catalog_generation: _builtins.bool, ignore_header_rows: _builtins.int, ignore_headers_row: _builtins.int, include_op_for_full_load: _builtins.bool, max_file_size: _builtins.int, parquet_timestamp_in_millisecond: _builtins.bool, parquet_version: _builtins.str, preserve_transactions: _builtins.bool, rfc4180: _builtins.bool, row_group_length: _builtins.int, server_side_encryption_kms_key_id: _builtins.str, service_access_role_arn: _builtins.str, timestamp_column_name: _builtins.str, use_csv_no_sup_value: _builtins.bool, use_task_start_time_for_full_load_timestamp: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addColumnName")
    def add_column_name(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcMinFileSize")
    def cdc_min_file_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdcPath")
    def cdc_path(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvNoSupValue")
    def csv_no_sup_value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvNullValue")
    def csv_null_value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvRowDelimiter")
    def csv_row_delimiter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPageSize")
    def data_page_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datePartitionEnabled")
    def date_partition_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datePartitionSequence")
    def date_partition_sequence(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStatistics")
    def enable_statistics(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalTableDefinition")
    def external_table_definition(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueCatalogGeneration")
    def glue_catalog_generation(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreHeaderRows")
    def ignore_header_rows(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreHeadersRow")
    def ignore_headers_row(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeOpForFullLoad")
    def include_op_for_full_load(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parquetVersion")
    def parquet_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveTransactions")
    def preserve_transactions(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rfc4180(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowGroupLength")
    def row_group_length(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampColumnName")
    def timestamp_column_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(self) -> _builtins.bool:
        ...
    


