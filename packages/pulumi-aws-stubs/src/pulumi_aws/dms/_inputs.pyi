import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EndpointElasticsearchSettingsArgs",
    "EndpointElasticsearchSettingsArgsDict",
    "EndpointKafkaSettingsArgs",
    "EndpointKafkaSettingsArgsDict",
    "EndpointKinesisSettingsArgs",
    "EndpointKinesisSettingsArgsDict",
    "EndpointMongodbSettingsArgs",
    "EndpointMongodbSettingsArgsDict",
    "EndpointMysqlSettingsArgs",
    "EndpointMysqlSettingsArgsDict",
    "EndpointOracleSettingsArgs",
    "EndpointOracleSettingsArgsDict",
    "EndpointPostgresSettingsArgs",
    "EndpointPostgresSettingsArgsDict",
    "EndpointRedisSettingsArgs",
    "EndpointRedisSettingsArgsDict",
    "EndpointRedshiftSettingsArgs",
    "EndpointRedshiftSettingsArgsDict",
    "ReplicationConfigComputeConfigArgs",
    "ReplicationConfigComputeConfigArgsDict",
    ...,
    ...,
]

class EndpointElasticsearchSettingsArgsDict(TypedDict):
    endpoint_uri: pulumi.Input[_builtins.str]
    service_access_role_arn: pulumi.Input[_builtins.str]
    error_retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    full_load_error_percentage: NotRequired[pulumi.Input[_builtins.int]]
    use_new_mapping_type: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EndpointElasticsearchSettingsArgs:
    def __init__(
        __self__,
        *,
        endpoint_uri: pulumi.Input[_builtins.str],
        service_access_role_arn: pulumi.Input[_builtins.str],
        error_retry_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        full_load_error_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        use_new_mapping_type: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_uri.setter
    def endpoint_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="errorRetryDuration")
    def error_retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @error_retry_duration.setter
    def error_retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @full_load_error_percentage.setter
    def full_load_error_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useNewMappingType")
    def use_new_mapping_type(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_new_mapping_type.setter
    def use_new_mapping_type(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EndpointKafkaSettingsArgsDict(TypedDict):
    broker: pulumi.Input[_builtins.str]
    include_control_details: NotRequired[pulumi.Input[_builtins.bool]]
    include_null_and_empty: NotRequired[pulumi.Input[_builtins.bool]]
    include_partition_value: NotRequired[pulumi.Input[_builtins.bool]]
    include_table_alter_operations: NotRequired[pulumi.Input[_builtins.bool]]
    include_transaction_details: NotRequired[pulumi.Input[_builtins.bool]]
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    message_max_bytes: NotRequired[pulumi.Input[_builtins.int]]
    no_hex_prefix: NotRequired[pulumi.Input[_builtins.bool]]
    partition_include_schema_table: NotRequired[pulumi.Input[_builtins.bool]]
    sasl_mechanism: NotRequired[pulumi.Input[_builtins.str]]
    sasl_password: NotRequired[pulumi.Input[_builtins.str]]
    sasl_username: NotRequired[pulumi.Input[_builtins.str]]
    security_protocol: NotRequired[pulumi.Input[_builtins.str]]
    ssl_ca_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    ssl_client_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    ssl_client_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    ssl_client_key_password: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointKafkaSettingsArgs:
    def __init__(
        __self__,
        *,
        broker: pulumi.Input[_builtins.str],
        include_control_details: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_null_and_empty: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_partition_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_table_alter_operations: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_transaction_details: Optional[pulumi.Input[_builtins.bool]] = ...,
        message_format: Optional[pulumi.Input[_builtins.str]] = ...,
        message_max_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        no_hex_prefix: Optional[pulumi.Input[_builtins.bool]] = ...,
        partition_include_schema_table: Optional[pulumi.Input[_builtins.bool]] = ...,
        sasl_mechanism: Optional[pulumi.Input[_builtins.str]] = ...,
        sasl_password: Optional[pulumi.Input[_builtins.str]] = ...,
        sasl_username: Optional[pulumi.Input[_builtins.str]] = ...,
        security_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_ca_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_client_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_client_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_client_key_password: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def broker(self) -> pulumi.Input[_builtins.str]: ...
    @broker.setter
    def broker(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_control_details.setter
    def include_control_details(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_null_and_empty.setter
    def include_null_and_empty(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_partition_value.setter
    def include_partition_value(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_transaction_details.setter
    def include_transaction_details(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messageMaxBytes")
    def message_max_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @message_max_bytes.setter
    def message_max_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="noHexPrefix")
    def no_hex_prefix(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_hex_prefix.setter
    def no_hex_prefix(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="saslMechanism")
    def sasl_mechanism(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_mechanism.setter
    def sasl_mechanism(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="saslPassword")
    def sasl_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_password.setter
    def sasl_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="saslUsername")
    def sasl_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_username.setter
    def sasl_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProtocol")
    def security_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_protocol.setter
    def security_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate_arn.setter
    def ssl_ca_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_client_certificate_arn.setter
    def ssl_client_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_client_key_arn.setter
    def ssl_client_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_client_key_password.setter
    def ssl_client_key_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointKinesisSettingsArgsDict(TypedDict):
    include_control_details: NotRequired[pulumi.Input[_builtins.bool]]
    include_null_and_empty: NotRequired[pulumi.Input[_builtins.bool]]
    include_partition_value: NotRequired[pulumi.Input[_builtins.bool]]
    include_table_alter_operations: NotRequired[pulumi.Input[_builtins.bool]]
    include_transaction_details: NotRequired[pulumi.Input[_builtins.bool]]
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    partition_include_schema_table: NotRequired[pulumi.Input[_builtins.bool]]
    service_access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    stream_arn: NotRequired[pulumi.Input[_builtins.str]]
    use_large_integer_value: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EndpointKinesisSettingsArgs:
    def __init__(
        __self__,
        *,
        include_control_details: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_null_and_empty: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_partition_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_table_alter_operations: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_transaction_details: Optional[pulumi.Input[_builtins.bool]] = ...,
        message_format: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_include_schema_table: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        use_large_integer_value: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeControlDetails")
    def include_control_details(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_control_details.setter
    def include_control_details(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeNullAndEmpty")
    def include_null_and_empty(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_null_and_empty.setter
    def include_null_and_empty(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includePartitionValue")
    def include_partition_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_partition_value.setter
    def include_partition_value(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeTransactionDetails")
    def include_transaction_details(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_transaction_details.setter
    def include_transaction_details(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_arn.setter
    def stream_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useLargeIntegerValue")
    def use_large_integer_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_large_integer_value.setter
    def use_large_integer_value(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class EndpointMongodbSettingsArgsDict(TypedDict):
    auth_mechanism: NotRequired[pulumi.Input[_builtins.str]]
    auth_source: NotRequired[pulumi.Input[_builtins.str]]
    auth_type: NotRequired[pulumi.Input[_builtins.str]]
    docs_to_investigate: NotRequired[pulumi.Input[_builtins.str]]
    extract_doc_id: NotRequired[pulumi.Input[_builtins.str]]
    nesting_level: NotRequired[pulumi.Input[_builtins.str]]
    use_update_lookup: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EndpointMongodbSettingsArgs:
    def __init__(
        __self__,
        *,
        auth_mechanism: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_source: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_type: Optional[pulumi.Input[_builtins.str]] = ...,
        docs_to_investigate: Optional[pulumi.Input[_builtins.str]] = ...,
        extract_doc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nesting_level: Optional[pulumi.Input[_builtins.str]] = ...,
        use_update_lookup: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMechanism")
    def auth_mechanism(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_mechanism.setter
    def auth_mechanism(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authSource")
    def auth_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_source.setter
    def auth_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="docsToInvestigate")
    def docs_to_investigate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docs_to_investigate.setter
    def docs_to_investigate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extractDocId")
    def extract_doc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extract_doc_id.setter
    def extract_doc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nestingLevel")
    def nesting_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nesting_level.setter
    def nesting_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useUpdateLookup")
    def use_update_lookup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_update_lookup.setter
    def use_update_lookup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EndpointMysqlSettingsArgsDict(TypedDict):
    after_connect_script: NotRequired[pulumi.Input[_builtins.str]]
    authentication_method: NotRequired[pulumi.Input[_builtins.str]]
    clean_source_metadata_on_mismatch: NotRequired[pulumi.Input[_builtins.bool]]
    events_poll_interval: NotRequired[pulumi.Input[_builtins.int]]
    execute_timeout: NotRequired[pulumi.Input[_builtins.int]]
    max_file_size: NotRequired[pulumi.Input[_builtins.int]]
    parallel_load_threads: NotRequired[pulumi.Input[_builtins.int]]
    server_timezone: NotRequired[pulumi.Input[_builtins.str]]
    service_access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    target_db_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointMysqlSettingsArgs:
    def __init__(
        __self__,
        *,
        after_connect_script: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_method: Optional[pulumi.Input[_builtins.str]] = ...,
        clean_source_metadata_on_mismatch: Optional[pulumi.Input[_builtins.bool]] = ...,
        events_poll_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        execute_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        parallel_load_threads: Optional[pulumi.Input[_builtins.int]] = ...,
        server_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_db_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @after_connect_script.setter
    def after_connect_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_method.setter
    def authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cleanSourceMetadataOnMismatch")
    def clean_source_metadata_on_mismatch(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @clean_source_metadata_on_mismatch.setter
    def clean_source_metadata_on_mismatch(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventsPollInterval")
    def events_poll_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @events_poll_interval.setter
    def events_poll_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execute_timeout.setter
    def execute_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_file_size.setter
    def max_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parallelLoadThreads")
    def parallel_load_threads(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallel_load_threads.setter
    def parallel_load_threads(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serverTimezone")
    def server_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_timezone.setter
    def server_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetDbType")
    def target_db_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_db_type.setter
    def target_db_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointOracleSettingsArgsDict(TypedDict):
    access_alternate_directly: NotRequired[pulumi.Input[_builtins.bool]]
    add_supplemental_logging: NotRequired[pulumi.Input[_builtins.bool]]
    additional_archived_log_dest_id: NotRequired[pulumi.Input[_builtins.int]]
    allow_selected_nested_tables: NotRequired[pulumi.Input[_builtins.bool]]
    archived_log_dest_id: NotRequired[pulumi.Input[_builtins.int]]
    archived_logs_only: NotRequired[pulumi.Input[_builtins.bool]]
    asm_password: NotRequired[pulumi.Input[_builtins.str]]
    asm_server: NotRequired[pulumi.Input[_builtins.str]]
    asm_user: NotRequired[pulumi.Input[_builtins.str]]
    authentication_method: NotRequired[pulumi.Input[_builtins.str]]
    char_length_semantics: NotRequired[pulumi.Input[_builtins.str]]
    convert_timestamp_with_zone_to_utc: NotRequired[pulumi.Input[_builtins.bool]]
    direct_path_no_log: NotRequired[pulumi.Input[_builtins.bool]]
    direct_path_parallel_load: NotRequired[pulumi.Input[_builtins.bool]]
    enable_homogenous_tablespace: NotRequired[pulumi.Input[_builtins.bool]]
    extra_archived_log_dest_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    fail_task_on_lob_truncation: NotRequired[pulumi.Input[_builtins.bool]]
    number_datatype_scale: NotRequired[pulumi.Input[_builtins.int]]
    open_transaction_window: NotRequired[pulumi.Input[_builtins.int]]
    oracle_path_prefix: NotRequired[pulumi.Input[_builtins.str]]
    parallel_asm_read_threads: NotRequired[pulumi.Input[_builtins.int]]
    read_ahead_blocks: NotRequired[pulumi.Input[_builtins.int]]
    read_table_space_name: NotRequired[pulumi.Input[_builtins.bool]]
    replace_path_prefix: NotRequired[pulumi.Input[_builtins.bool]]
    retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    secrets_manager_oracle_asm_access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_oracle_asm_secret_id: NotRequired[pulumi.Input[_builtins.str]]
    security_db_encryption: NotRequired[pulumi.Input[_builtins.str]]
    security_db_encryption_name: NotRequired[pulumi.Input[_builtins.str]]
    spatial_data_option_to_geo_json_function_name: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    standby_delay_time: NotRequired[pulumi.Input[_builtins.int]]
    trim_space_in_char: NotRequired[pulumi.Input[_builtins.bool]]
    use_alternate_folder_for_online: NotRequired[pulumi.Input[_builtins.bool]]
    use_bfile: NotRequired[pulumi.Input[_builtins.bool]]
    use_direct_path_full_load: NotRequired[pulumi.Input[_builtins.bool]]
    use_logminer_reader: NotRequired[pulumi.Input[_builtins.bool]]
    use_path_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointOracleSettingsArgs:
    def __init__(
        __self__,
        *,
        access_alternate_directly: Optional[pulumi.Input[_builtins.bool]] = ...,
        add_supplemental_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        additional_archived_log_dest_id: Optional[pulumi.Input[_builtins.int]] = ...,
        allow_selected_nested_tables: Optional[pulumi.Input[_builtins.bool]] = ...,
        archived_log_dest_id: Optional[pulumi.Input[_builtins.int]] = ...,
        archived_logs_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        asm_password: Optional[pulumi.Input[_builtins.str]] = ...,
        asm_server: Optional[pulumi.Input[_builtins.str]] = ...,
        asm_user: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_method: Optional[pulumi.Input[_builtins.str]] = ...,
        char_length_semantics: Optional[pulumi.Input[_builtins.str]] = ...,
        convert_timestamp_with_zone_to_utc: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        direct_path_no_log: Optional[pulumi.Input[_builtins.bool]] = ...,
        direct_path_parallel_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_homogenous_tablespace: Optional[pulumi.Input[_builtins.bool]] = ...,
        extra_archived_log_dest_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        fail_task_on_lob_truncation: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_datatype_scale: Optional[pulumi.Input[_builtins.int]] = ...,
        open_transaction_window: Optional[pulumi.Input[_builtins.int]] = ...,
        oracle_path_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        parallel_asm_read_threads: Optional[pulumi.Input[_builtins.int]] = ...,
        read_ahead_blocks: Optional[pulumi.Input[_builtins.int]] = ...,
        read_table_space_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        replace_path_prefix: Optional[pulumi.Input[_builtins.bool]] = ...,
        retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        secrets_manager_oracle_asm_access_role_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        secrets_manager_oracle_asm_secret_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        security_db_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        security_db_encryption_name: Optional[pulumi.Input[_builtins.str]] = ...,
        spatial_data_option_to_geo_json_function_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        standby_delay_time: Optional[pulumi.Input[_builtins.int]] = ...,
        trim_space_in_char: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_alternate_folder_for_online: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_bfile: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_direct_path_full_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_logminer_reader: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_path_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessAlternateDirectly")
    def access_alternate_directly(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @access_alternate_directly.setter
    def access_alternate_directly(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="addSupplementalLogging")
    def add_supplemental_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_supplemental_logging.setter
    def add_supplemental_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalArchivedLogDestId")
    def additional_archived_log_dest_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_archived_log_dest_id.setter
    def additional_archived_log_dest_id(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowSelectedNestedTables")
    def allow_selected_nested_tables(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_selected_nested_tables.setter
    def allow_selected_nested_tables(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="archivedLogDestId")
    def archived_log_dest_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @archived_log_dest_id.setter
    def archived_log_dest_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="archivedLogsOnly")
    def archived_logs_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @archived_logs_only.setter
    def archived_logs_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="asmPassword")
    def asm_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asm_password.setter
    def asm_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="asmServer")
    def asm_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asm_server.setter
    def asm_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="asmUser")
    def asm_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asm_user.setter
    def asm_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_method.setter
    def authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="charLengthSemantics")
    def char_length_semantics(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @char_length_semantics.setter
    def char_length_semantics(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="convertTimestampWithZoneToUtc")
    def convert_timestamp_with_zone_to_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @convert_timestamp_with_zone_to_utc.setter
    def convert_timestamp_with_zone_to_utc(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directPathNoLog")
    def direct_path_no_log(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @direct_path_no_log.setter
    def direct_path_no_log(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="directPathParallelLoad")
    def direct_path_parallel_load(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @direct_path_parallel_load.setter
    def direct_path_parallel_load(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHomogenousTablespace")
    def enable_homogenous_tablespace(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_homogenous_tablespace.setter
    def enable_homogenous_tablespace(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extraArchivedLogDestIds")
    def extra_archived_log_dest_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @extra_archived_log_dest_ids.setter
    def extra_archived_log_dest_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failTaskOnLobTruncation")
    def fail_task_on_lob_truncation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_task_on_lob_truncation.setter
    def fail_task_on_lob_truncation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberDatatypeScale")
    def number_datatype_scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_datatype_scale.setter
    def number_datatype_scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="openTransactionWindow")
    def open_transaction_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @open_transaction_window.setter
    def open_transaction_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="oraclePathPrefix")
    def oracle_path_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oracle_path_prefix.setter
    def oracle_path_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parallelAsmReadThreads")
    def parallel_asm_read_threads(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallel_asm_read_threads.setter
    def parallel_asm_read_threads(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readAheadBlocks")
    def read_ahead_blocks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @read_ahead_blocks.setter
    def read_ahead_blocks(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="readTableSpaceName")
    def read_table_space_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_table_space_name.setter
    def read_table_space_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="replacePathPrefix")
    def replace_path_prefix(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replace_path_prefix.setter
    def replace_path_prefix(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_interval.setter
    def retry_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerOracleAsmAccessRoleArn")
    def secrets_manager_oracle_asm_access_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_oracle_asm_access_role_arn.setter
    def secrets_manager_oracle_asm_access_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerOracleAsmSecretId")
    def secrets_manager_oracle_asm_secret_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_oracle_asm_secret_id.setter
    def secrets_manager_oracle_asm_secret_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityDbEncryption")
    def security_db_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_db_encryption.setter
    def security_db_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityDbEncryptionName")
    def security_db_encryption_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_db_encryption_name.setter
    def security_db_encryption_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spatialDataOptionToGeoJsonFunctionName")
    def spatial_data_option_to_geo_json_function_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spatial_data_option_to_geo_json_function_name.setter
    def spatial_data_option_to_geo_json_function_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standbyDelayTime")
    def standby_delay_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @standby_delay_time.setter
    def standby_delay_time(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="trimSpaceInChar")
    def trim_space_in_char(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @trim_space_in_char.setter
    def trim_space_in_char(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useAlternateFolderForOnline")
    def use_alternate_folder_for_online(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_alternate_folder_for_online.setter
    def use_alternate_folder_for_online(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useBfile")
    def use_bfile(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_bfile.setter
    def use_bfile(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useDirectPathFullLoad")
    def use_direct_path_full_load(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_direct_path_full_load.setter
    def use_direct_path_full_load(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useLogminerReader")
    def use_logminer_reader(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_logminer_reader.setter
    def use_logminer_reader(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="usePathPrefix")
    def use_path_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @use_path_prefix.setter
    def use_path_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointPostgresSettingsArgsDict(TypedDict):
    after_connect_script: NotRequired[pulumi.Input[_builtins.str]]
    authentication_method: NotRequired[pulumi.Input[_builtins.str]]
    babelfish_database_name: NotRequired[pulumi.Input[_builtins.str]]
    capture_ddls: NotRequired[pulumi.Input[_builtins.bool]]
    database_mode: NotRequired[pulumi.Input[_builtins.str]]
    ddl_artifacts_schema: NotRequired[pulumi.Input[_builtins.str]]
    execute_timeout: NotRequired[pulumi.Input[_builtins.int]]
    fail_tasks_on_lob_truncation: NotRequired[pulumi.Input[_builtins.bool]]
    heartbeat_enable: NotRequired[pulumi.Input[_builtins.bool]]
    heartbeat_frequency: NotRequired[pulumi.Input[_builtins.int]]
    heartbeat_schema: NotRequired[pulumi.Input[_builtins.str]]
    map_boolean_as_boolean: NotRequired[pulumi.Input[_builtins.bool]]
    map_jsonb_as_clob: NotRequired[pulumi.Input[_builtins.bool]]
    map_long_varchar_as: NotRequired[pulumi.Input[_builtins.str]]
    max_file_size: NotRequired[pulumi.Input[_builtins.int]]
    plugin_name: NotRequired[pulumi.Input[_builtins.str]]
    service_access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    slot_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointPostgresSettingsArgs:
    def __init__(
        __self__,
        *,
        after_connect_script: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_method: Optional[pulumi.Input[_builtins.str]] = ...,
        babelfish_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        capture_ddls: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        ddl_artifacts_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        execute_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        fail_tasks_on_lob_truncation: Optional[pulumi.Input[_builtins.bool]] = ...,
        heartbeat_enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        heartbeat_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        heartbeat_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        map_boolean_as_boolean: Optional[pulumi.Input[_builtins.bool]] = ...,
        map_jsonb_as_clob: Optional[pulumi.Input[_builtins.bool]] = ...,
        map_long_varchar_as: Optional[pulumi.Input[_builtins.str]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        plugin_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterConnectScript")
    def after_connect_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @after_connect_script.setter
    def after_connect_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_method.setter
    def authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="babelfishDatabaseName")
    def babelfish_database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @babelfish_database_name.setter
    def babelfish_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="captureDdls")
    def capture_ddls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @capture_ddls.setter
    def capture_ddls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseMode")
    def database_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_mode.setter
    def database_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ddlArtifactsSchema")
    def ddl_artifacts_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ddl_artifacts_schema.setter
    def ddl_artifacts_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executeTimeout")
    def execute_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execute_timeout.setter
    def execute_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="failTasksOnLobTruncation")
    def fail_tasks_on_lob_truncation(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_tasks_on_lob_truncation.setter
    def fail_tasks_on_lob_truncation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatEnable")
    def heartbeat_enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @heartbeat_enable.setter
    def heartbeat_enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatFrequency")
    def heartbeat_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @heartbeat_frequency.setter
    def heartbeat_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatSchema")
    def heartbeat_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @heartbeat_schema.setter
    def heartbeat_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mapBooleanAsBoolean")
    def map_boolean_as_boolean(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @map_boolean_as_boolean.setter
    def map_boolean_as_boolean(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mapJsonbAsClob")
    def map_jsonb_as_clob(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @map_jsonb_as_clob.setter
    def map_jsonb_as_clob(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mapLongVarcharAs")
    def map_long_varchar_as(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @map_long_varchar_as.setter
    def map_long_varchar_as(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_file_size.setter
    def max_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_name.setter
    def plugin_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotName")
    def slot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slot_name.setter
    def slot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointRedisSettingsArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    server_name: pulumi.Input[_builtins.str]
    auth_password: NotRequired[pulumi.Input[_builtins.str]]
    auth_user_name: NotRequired[pulumi.Input[_builtins.str]]
    ssl_ca_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    ssl_security_protocol: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointRedisSettingsArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
        server_name: pulumi.Input[_builtins.str],
        auth_password: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_ca_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_security_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authPassword")
    def auth_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_password.setter
    def auth_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authUserName")
    def auth_user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_user_name.setter
    def auth_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate_arn.setter
    def ssl_ca_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslSecurityProtocol")
    def ssl_security_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_security_protocol.setter
    def ssl_security_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointRedshiftSettingsArgsDict(TypedDict):
    bucket_folder: NotRequired[pulumi.Input[_builtins.str]]
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    server_side_encryption_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    service_access_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EndpointRedshiftSettingsArgs:
    def __init__(
        __self__,
        *,
        bucket_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_folder.setter
    def bucket_folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReplicationConfigComputeConfigArgsDict(TypedDict):
    replication_subnet_group_id: pulumi.Input[_builtins.str]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    dns_name_servers: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    max_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    min_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    multi_az: NotRequired[pulumi.Input[_builtins.bool]]
    preferred_maintenance_window: NotRequired[pulumi.Input[_builtins.str]]
    vpc_security_group_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class ReplicationConfigComputeConfigArgs:
    def __init__(
        __self__,
        *,
        replication_subnet_group_id: pulumi.Input[_builtins.str],
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name_servers: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
        min_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsNameServers")
    def dns_name_servers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name_servers.setter
    def dns_name_servers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacityUnits")
    def max_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_capacity_units.setter
    def max_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacityUnits")
    def min_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_capacity_units.setter
    def min_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ReplicationInstanceKerberosAuthenticationSettingsArgsDict(TypedDict):
    key_cache_secret_iam_arn: pulumi.Input[_builtins.str]
    key_cache_secret_id: pulumi.Input[_builtins.str]
    krb5_file_contents: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ReplicationInstanceKerberosAuthenticationSettingsArgs:
    def __init__(
        __self__,
        *,
        key_cache_secret_iam_arn: pulumi.Input[_builtins.str],
        key_cache_secret_id: pulumi.Input[_builtins.str],
        krb5_file_contents: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyCacheSecretIamArn")
    def key_cache_secret_iam_arn(self) -> pulumi.Input[_builtins.str]: ...
    @key_cache_secret_iam_arn.setter
    def key_cache_secret_iam_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyCacheSecretId")
    def key_cache_secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_cache_secret_id.setter
    def key_cache_secret_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="krb5FileContents")
    def krb5_file_contents(self) -> pulumi.Input[_builtins.str]: ...
    @krb5_file_contents.setter
    def krb5_file_contents(self, value: pulumi.Input[_builtins.str]): ...
