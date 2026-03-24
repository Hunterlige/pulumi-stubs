import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["S3EndpointArgs", "S3Endpoint"]

@pulumi.input_type
class S3EndpointArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        endpoint_id: pulumi.Input[_builtins.str],
        endpoint_type: pulumi.Input[_builtins.str],
        service_access_role_arn: pulumi.Input[_builtins.str],
        add_column_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        add_trailing_padding_character: Optional[pulumi.Input[_builtins.bool]] = ...,
        bucket_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        canned_acl_for_objects: Optional[pulumi.Input[_builtins.str]] = ...,
        cdc_inserts_and_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_inserts_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_max_batch_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_min_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_path: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_no_sup_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_null_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_row_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[pulumi.Input[_builtins.str]] = ...,
        data_page_size: Optional[pulumi.Input[_builtins.int]] = ...,
        date_partition_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_partition_sequence: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        detach_target_on_lob_lookup_failure_parquet: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        dict_page_size_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_statistics: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_table_definition: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_catalog_generation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        include_op_for_full_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        parquet_timestamp_in_millisecond: Optional[pulumi.Input[_builtins.bool]] = ...,
        parquet_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_transactions: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rfc4180: Optional[pulumi.Input[_builtins.bool]] = ...,
        row_group_length: Optional[pulumi.Input[_builtins.int]] = ...,
        server_side_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timestamp_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_csv_no_sup_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_task_start_time_for_full_load_timestamp: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_access_role_arn.setter
    def service_access_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addColumnName")
    def add_column_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_column_name.setter
    def add_column_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="addTrailingPaddingCharacter")
    def add_trailing_padding_character(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_trailing_padding_character.setter
    def add_trailing_padding_character(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_folder.setter
    def bucket_folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl_for_objects.setter
    def canned_acl_for_objects(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cdc_inserts_and_updates.setter
    def cdc_inserts_and_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cdc_inserts_only.setter
    def cdc_inserts_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cdc_max_batch_interval.setter
    def cdc_max_batch_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcMinFileSize")
    def cdc_min_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cdc_min_file_size.setter
    def cdc_min_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcPath")
    def cdc_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cdc_path.setter
    def cdc_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_type.setter
    def compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_delimiter.setter
    def csv_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvNoSupValue")
    def csv_no_sup_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_no_sup_value.setter
    def csv_no_sup_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvNullValue")
    def csv_null_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_null_value.setter
    def csv_null_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvRowDelimiter")
    def csv_row_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_row_delimiter.setter
    def csv_row_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPageSize")
    def data_page_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_page_size.setter
    def data_page_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_delimiter.setter
    def date_partition_delimiter(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionEnabled")
    def date_partition_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @date_partition_enabled.setter
    def date_partition_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionSequence")
    def date_partition_sequence(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_sequence.setter
    def date_partition_sequence(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionTimezone")
    def date_partition_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_timezone.setter
    def date_partition_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detachTargetOnLobLookupFailureParquet")
    def detach_target_on_lob_lookup_failure_parquet(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @detach_target_on_lob_lookup_failure_parquet.setter
    def detach_target_on_lob_lookup_failure_parquet(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dict_page_size_limit.setter
    def dict_page_size_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableStatistics")
    def enable_statistics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_statistics.setter
    def enable_statistics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding_type.setter
    def encoding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalTableDefinition")
    def external_table_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_table_definition.setter
    def external_table_definition(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="glueCatalogGeneration")
    def glue_catalog_generation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @glue_catalog_generation.setter
    def glue_catalog_generation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreHeaderRows")
    def ignore_header_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ignore_header_rows.setter
    def ignore_header_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="includeOpForFullLoad")
    def include_op_for_full_load(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_op_for_full_load.setter
    def include_op_for_full_load(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_file_size.setter
    def max_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @parquet_timestamp_in_millisecond.setter
    def parquet_timestamp_in_millisecond(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parquetVersion")
    def parquet_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parquet_version.setter
    def parquet_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveTransactions")
    def preserve_transactions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve_transactions.setter
    def preserve_transactions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rfc4180(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @rfc4180.setter
    def rfc4180(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rowGroupLength")
    def row_group_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @row_group_length.setter
    def row_group_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampColumnName")
    def timestamp_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_column_name.setter
    def timestamp_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_csv_no_sup_value.setter
    def use_csv_no_sup_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_task_start_time_for_full_load_timestamp.setter
    def use_task_start_time_for_full_load_timestamp(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _S3EndpointState:
    def __init__(
        __self__,
        *,
        add_column_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        add_trailing_padding_character: Optional[pulumi.Input[_builtins.bool]] = ...,
        bucket_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        canned_acl_for_objects: Optional[pulumi.Input[_builtins.str]] = ...,
        cdc_inserts_and_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_inserts_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_max_batch_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_min_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_path: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_no_sup_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_null_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_row_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[pulumi.Input[_builtins.str]] = ...,
        data_page_size: Optional[pulumi.Input[_builtins.int]] = ...,
        date_partition_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_partition_sequence: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        detach_target_on_lob_lookup_failure_parquet: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        dict_page_size_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_statistics: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_table_definition: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_catalog_generation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        include_op_for_full_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        parquet_timestamp_in_millisecond: Optional[pulumi.Input[_builtins.bool]] = ...,
        parquet_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_transactions: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rfc4180: Optional[pulumi.Input[_builtins.bool]] = ...,
        row_group_length: Optional[pulumi.Input[_builtins.int]] = ...,
        server_side_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timestamp_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_csv_no_sup_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_task_start_time_for_full_load_timestamp: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addColumnName")
    def add_column_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_column_name.setter
    def add_column_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="addTrailingPaddingCharacter")
    def add_trailing_padding_character(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_trailing_padding_character.setter
    def add_trailing_padding_character(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl_for_objects.setter
    def canned_acl_for_objects(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cdc_inserts_and_updates.setter
    def cdc_inserts_and_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cdc_inserts_only.setter
    def cdc_inserts_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cdc_max_batch_interval.setter
    def cdc_max_batch_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcMinFileSize")
    def cdc_min_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cdc_min_file_size.setter
    def cdc_min_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cdcPath")
    def cdc_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cdc_path.setter
    def cdc_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_type.setter
    def compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_delimiter.setter
    def csv_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvNoSupValue")
    def csv_no_sup_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_no_sup_value.setter
    def csv_no_sup_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvNullValue")
    def csv_null_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_null_value.setter
    def csv_null_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvRowDelimiter")
    def csv_row_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csv_row_delimiter.setter
    def csv_row_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPageSize")
    def data_page_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_page_size.setter
    def data_page_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_delimiter.setter
    def date_partition_delimiter(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionEnabled")
    def date_partition_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @date_partition_enabled.setter
    def date_partition_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionSequence")
    def date_partition_sequence(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_sequence.setter
    def date_partition_sequence(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datePartitionTimezone")
    def date_partition_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_partition_timezone.setter
    def date_partition_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detachTargetOnLobLookupFailureParquet")
    def detach_target_on_lob_lookup_failure_parquet(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @detach_target_on_lob_lookup_failure_parquet.setter
    def detach_target_on_lob_lookup_failure_parquet(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dict_page_size_limit.setter
    def dict_page_size_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableStatistics")
    def enable_statistics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_statistics.setter
    def enable_statistics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding_type.setter
    def encoding_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_mode.setter
    def encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_arn.setter
    def endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineDisplayName")
    def engine_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_display_name.setter
    def engine_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalTableDefinition")
    def external_table_definition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_table_definition.setter
    def external_table_definition(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="glueCatalogGeneration")
    def glue_catalog_generation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @glue_catalog_generation.setter
    def glue_catalog_generation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreHeaderRows")
    def ignore_header_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ignore_header_rows.setter
    def ignore_header_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="includeOpForFullLoad")
    def include_op_for_full_load(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_op_for_full_load.setter
    def include_op_for_full_load(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_file_size.setter
    def max_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @parquet_timestamp_in_millisecond.setter
    def parquet_timestamp_in_millisecond(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parquetVersion")
    def parquet_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parquet_version.setter
    def parquet_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveTransactions")
    def preserve_transactions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve_transactions.setter
    def preserve_transactions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rfc4180(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @rfc4180.setter
    def rfc4180(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rowGroupLength")
    def row_group_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @row_group_length.setter
    def row_group_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampColumnName")
    def timestamp_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_column_name.setter
    def timestamp_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_csv_no_sup_value.setter
    def use_csv_no_sup_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_task_start_time_for_full_load_timestamp.setter
    def use_task_start_time_for_full_load_timestamp(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token("aws:dms/s3Endpoint:S3Endpoint")
class S3Endpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        add_column_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        add_trailing_padding_character: Optional[pulumi.Input[_builtins.bool]] = ...,
        bucket_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        canned_acl_for_objects: Optional[pulumi.Input[_builtins.str]] = ...,
        cdc_inserts_and_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_inserts_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_max_batch_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_min_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_path: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_no_sup_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_null_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_row_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[pulumi.Input[_builtins.str]] = ...,
        data_page_size: Optional[pulumi.Input[_builtins.int]] = ...,
        date_partition_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_partition_sequence: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        detach_target_on_lob_lookup_failure_parquet: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        dict_page_size_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_statistics: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_table_definition: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_catalog_generation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        include_op_for_full_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        parquet_timestamp_in_millisecond: Optional[pulumi.Input[_builtins.bool]] = ...,
        parquet_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_transactions: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rfc4180: Optional[pulumi.Input[_builtins.bool]] = ...,
        row_group_length: Optional[pulumi.Input[_builtins.int]] = ...,
        server_side_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timestamp_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_csv_no_sup_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_task_start_time_for_full_load_timestamp: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: S3EndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        add_column_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        add_trailing_padding_character: Optional[pulumi.Input[_builtins.bool]] = ...,
        bucket_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        canned_acl_for_objects: Optional[pulumi.Input[_builtins.str]] = ...,
        cdc_inserts_and_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_inserts_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        cdc_max_batch_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_min_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        cdc_path: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression_type: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_no_sup_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_null_value: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_row_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        data_format: Optional[pulumi.Input[_builtins.str]] = ...,
        data_page_size: Optional[pulumi.Input[_builtins.int]] = ...,
        date_partition_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_partition_sequence: Optional[pulumi.Input[_builtins.str]] = ...,
        date_partition_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        detach_target_on_lob_lookup_failure_parquet: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        dict_page_size_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_statistics: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        external_table_definition: Optional[pulumi.Input[_builtins.str]] = ...,
        glue_catalog_generation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_header_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        include_op_for_full_load: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        max_file_size: Optional[pulumi.Input[_builtins.int]] = ...,
        parquet_timestamp_in_millisecond: Optional[pulumi.Input[_builtins.bool]] = ...,
        parquet_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preserve_transactions: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rfc4180: Optional[pulumi.Input[_builtins.bool]] = ...,
        row_group_length: Optional[pulumi.Input[_builtins.int]] = ...,
        server_side_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timestamp_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_csv_no_sup_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_task_start_time_for_full_load_timestamp: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> S3Endpoint: ...
    @_builtins.property
    @pulumi.getter(name="addColumnName")
    def add_column_name(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="addTrailingPaddingCharacter")
    def add_trailing_padding_character(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="cdcMinFileSize")
    def cdc_min_file_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="cdcPath")
    def cdc_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="csvNoSupValue")
    def csv_no_sup_value(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="csvNullValue")
    def csv_null_value(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="csvRowDelimiter")
    def csv_row_delimiter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataPageSize")
    def data_page_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="datePartitionEnabled")
    def date_partition_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="datePartitionSequence")
    def date_partition_sequence(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="datePartitionTimezone")
    def date_partition_timezone(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="detachTargetOnLobLookupFailureParquet")
    def detach_target_on_lob_lookup_failure_parquet(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="enableStatistics")
    def enable_statistics(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionMode")
    def encryption_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineDisplayName")
    def engine_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalTableDefinition")
    def external_table_definition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="glueCatalogGeneration")
    def glue_catalog_generation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreHeaderRows")
    def ignore_header_rows(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="includeOpForFullLoad")
    def include_op_for_full_load(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxFileSize")
    def max_file_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="parquetVersion")
    def parquet_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="preserveTransactions")
    def preserve_transactions(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rfc4180(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="rowGroupLength")
    def row_group_length(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timestampColumnName")
    def timestamp_column_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
