import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AnalyticsApplicationCloudwatchLoggingOptions",
    "AnalyticsApplicationInputs",
    "AnalyticsApplicationInputsKinesisFirehose",
    "AnalyticsApplicationInputsKinesisStream",
    "AnalyticsApplicationInputsParallelism",
    "AnalyticsApplicationInputsProcessingConfiguration",
    ...,
    "AnalyticsApplicationInputsSchema",
    "AnalyticsApplicationInputsSchemaRecordColumn",
    "AnalyticsApplicationInputsSchemaRecordFormat",
    ...,
    ...,
    ...,
    ...,
    "AnalyticsApplicationOutput",
    "AnalyticsApplicationOutputKinesisFirehose",
    "AnalyticsApplicationOutputKinesisStream",
    "AnalyticsApplicationOutputLambda",
    "AnalyticsApplicationOutputSchema",
    "AnalyticsApplicationReferenceDataSources",
    "AnalyticsApplicationReferenceDataSourcesS3",
    "AnalyticsApplicationReferenceDataSourcesSchema",
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamElasticsearchConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamExtendedS3Configuration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamHttpEndpointConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamIcebergConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamKinesisSourceConfiguration",
    "FirehoseDeliveryStreamMskSourceConfiguration",
    ...,
    "FirehoseDeliveryStreamOpensearchConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamRedshiftConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamServerSideEncryption",
    "FirehoseDeliveryStreamSnowflakeConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirehoseDeliveryStreamSplunkConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamStreamModeDetails",
    "GetStreamStreamModeDetailResult",
]

@pulumi.output_type
class AnalyticsApplicationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        log_stream_arn: _builtins.str,
        role_arn: _builtins.str,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logStreamArn")
    def log_stream_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationInputs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name_prefix: _builtins.str,
        schema: outputs.AnalyticsApplicationInputsSchema,
        id: Optional[_builtins.str] = ...,
        kinesis_firehose: Optional[
            outputs.AnalyticsApplicationInputsKinesisFirehose
        ] = ...,
        kinesis_stream: Optional[outputs.AnalyticsApplicationInputsKinesisStream] = ...,
        parallelism: Optional[outputs.AnalyticsApplicationInputsParallelism] = ...,
        processing_configuration: Optional[
            outputs.AnalyticsApplicationInputsProcessingConfiguration
        ] = ...,
        starting_position_configurations: Optional[
            Sequence[outputs.AnalyticsApplicationInputsStartingPositionConfiguration]
        ] = ...,
        stream_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.AnalyticsApplicationInputsSchema: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> Optional[outputs.AnalyticsApplicationInputsKinesisFirehose]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> Optional[outputs.AnalyticsApplicationInputsKinesisStream]: ...
    @_builtins.property
    @pulumi.getter
    def parallelism(
        self,
    ) -> Optional[outputs.AnalyticsApplicationInputsParallelism]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[outputs.AnalyticsApplicationInputsProcessingConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="startingPositionConfigurations")
    def starting_position_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.AnalyticsApplicationInputsStartingPositionConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="streamNames")
    def stream_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AnalyticsApplicationInputsKinesisFirehose(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationInputsKinesisStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationInputsParallelism(dict):
    def __init__(__self__, *, count: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AnalyticsApplicationInputsProcessingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_: outputs.AnalyticsApplicationInputsProcessingConfigurationLambda,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(
        self,
    ) -> outputs.AnalyticsApplicationInputsProcessingConfigurationLambda: ...

@pulumi.output_type
class AnalyticsApplicationInputsProcessingConfigurationLambda(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_columns: Sequence[outputs.AnalyticsApplicationInputsSchemaRecordColumn],
        record_format: outputs.AnalyticsApplicationInputsSchemaRecordFormat,
        record_encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(
        self,
    ) -> Sequence[outputs.AnalyticsApplicationInputsSchemaRecordColumn]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(self) -> outputs.AnalyticsApplicationInputsSchemaRecordFormat: ...
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchemaRecordColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        sql_type: _builtins.str,
        mapping: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchemaRecordFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mapping_parameters: Optional[
            outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParameters
        ] = ...,
        record_format_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParameters
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParameters(dict):
    def __init__(
        __self__,
        *,
        csv: Optional[
            outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv
        ] = ...,
        json: Optional[
            outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csv(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv
    ]: ...
    @_builtins.property
    @pulumi.getter
    def json(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson
    ]: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_column_delimiter: _builtins.str,
        record_row_delimiter: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_row_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationInputsStartingPositionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, starting_position: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        schema: outputs.AnalyticsApplicationOutputSchema,
        id: Optional[_builtins.str] = ...,
        kinesis_firehose: Optional[
            outputs.AnalyticsApplicationOutputKinesisFirehose
        ] = ...,
        kinesis_stream: Optional[outputs.AnalyticsApplicationOutputKinesisStream] = ...,
        lambda_: Optional[outputs.AnalyticsApplicationOutputLambda] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.AnalyticsApplicationOutputSchema: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> Optional[outputs.AnalyticsApplicationOutputKinesisFirehose]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> Optional[outputs.AnalyticsApplicationOutputKinesisStream]: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[outputs.AnalyticsApplicationOutputLambda]: ...

@pulumi.output_type
class AnalyticsApplicationOutputKinesisFirehose(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationOutputKinesisStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationOutputLambda(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationOutputSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_format_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3: outputs.AnalyticsApplicationReferenceDataSourcesS3,
        schema: outputs.AnalyticsApplicationReferenceDataSourcesSchema,
        table_name: _builtins.str,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> outputs.AnalyticsApplicationReferenceDataSourcesS3: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.AnalyticsApplicationReferenceDataSourcesSchema: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        file_key: _builtins.str,
        role_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_columns: Sequence[
            outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordColumn
        ],
        record_format: outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormat,
        record_encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(
        self,
    ) -> Sequence[
        outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordColumn
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(
        self,
    ) -> outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormat: ...
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        sql_type: _builtins.str,
        mapping: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mapping_parameters: Optional[
            outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters
        ] = ...,
        record_format_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(dict):
    def __init__(
        __self__,
        *,
        csv: Optional[
            outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv
        ] = ...,
        json: Optional[
            outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csv(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv
    ]: ...
    @_builtins.property
    @pulumi.getter
    def json(
        self,
    ) -> Optional[
        outputs.AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson
    ]: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_column_delimiter: _builtins.str,
        record_row_delimiter: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_row_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        index_name: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamElasticsearchConfigurationS3Configuration,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions
        ] = ...,
        cluster_endpoint: Optional[_builtins.str] = ...,
        domain_arn: Optional[_builtins.str] = ...,
        index_rotation_period: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        type_name: Optional[_builtins.str] = ...,
        vpc_config: Optional[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamElasticsearchConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexRotationPeriod")
    def index_rotation_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamElasticsearchConfigurationVpcConfig
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_arn: _builtins.str,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        custom_time_zone: Optional[_builtins.str] = ...,
        data_format_conversion_configuration: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration
        ] = ...,
        dynamic_partitioning_configuration: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration
        ] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        file_extension: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration
        ] = ...,
        s3_backup_configuration: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration
        ] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customTimeZone")
    def custom_time_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormatConversionConfiguration")
    def data_format_conversion_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicPartitioningConfiguration")
    def dynamic_partitioning_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileExtension")
    def file_extension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_format_configuration: outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration,
        output_format_configuration: outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration,
        schema_configuration: outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormatConfiguration")
    def input_format_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="outputFormatConfiguration")
    def output_format_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="schemaConfiguration")
    def schema_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(
    dict
):
    def __init__(
        __self__,
        *,
        deserializer: outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deserializer(
        self,
    ) -> outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hive_json_ser_de: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe
        ] = ...,
        open_x_json_ser_de: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiveJsonSerDe")
    def hive_json_ser_de(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe
    ]: ...
    @_builtins.property
    @pulumi.getter(name="openXJsonSerDe")
    def open_x_json_ser_de(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, timestamp_formats: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timestampFormats")
    def timestamp_formats(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        case_insensitive: Optional[_builtins.bool] = ...,
        column_to_json_key_mappings: Optional[Mapping[str, _builtins.str]] = ...,
        convert_dots_in_json_keys_to_underscores: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caseInsensitive")
    def case_insensitive(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="columnToJsonKeyMappings")
    def column_to_json_key_mappings(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="convertDotsInJsonKeysToUnderscores")
    def convert_dots_in_json_keys_to_underscores(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(
    dict
):
    def __init__(
        __self__,
        *,
        serializer: outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def serializer(
        self,
    ) -> outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        orc_ser_de: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe
        ] = ...,
        parquet_ser_de: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="orcSerDe")
    def orc_ser_de(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parquetSerDe")
    def parquet_ser_de(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        block_size_bytes: Optional[_builtins.int] = ...,
        bloom_filter_columns: Optional[Sequence[_builtins.str]] = ...,
        bloom_filter_false_positive_probability: Optional[_builtins.float] = ...,
        compression: Optional[_builtins.str] = ...,
        dictionary_key_threshold: Optional[_builtins.float] = ...,
        enable_padding: Optional[_builtins.bool] = ...,
        format_version: Optional[_builtins.str] = ...,
        padding_tolerance: Optional[_builtins.float] = ...,
        row_index_stride: Optional[_builtins.int] = ...,
        stripe_size_bytes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bloomFilterColumns")
    def bloom_filter_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bloomFilterFalsePositiveProbability")
    def bloom_filter_false_positive_probability(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dictionaryKeyThreshold")
    def dictionary_key_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="enablePadding")
    def enable_padding(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="formatVersion")
    def format_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="paddingTolerance")
    def padding_tolerance(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="rowIndexStride")
    def row_index_stride(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stripeSizeBytes")
    def stripe_size_bytes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        block_size_bytes: Optional[_builtins.int] = ...,
        compression: Optional[_builtins.str] = ...,
        enable_dictionary_compression: Optional[_builtins.bool] = ...,
        max_padding_bytes: Optional[_builtins.int] = ...,
        page_size_bytes: Optional[_builtins.int] = ...,
        writer_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDictionaryCompression")
    def enable_dictionary_compression(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxPaddingBytes")
    def max_padding_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pageSizeBytes")
    def page_size_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="writerVersion")
    def writer_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        role_arn: _builtins.str,
        table_name: _builtins.str,
        catalog_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        version_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        retry_duration: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_configuration: outputs.FirehoseDeliveryStreamHttpEndpointConfigurationS3Configuration,
        url: _builtins.str,
        access_key: Optional[_builtins.str] = ...,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions
        ] = ...,
        name: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration
        ] = ...,
        request_configuration: Optional[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        role_arn: Optional[_builtins.str] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        secrets_manager_configuration: Optional[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamHttpEndpointConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requestConfiguration")
    def request_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfiguration
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        common_attributes: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttribute
            ]
        ] = ...,
        content_encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonAttributes")
    def common_attributes(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttribute
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttribute(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        role_arn: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_arn: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamIcebergConfigurationS3Configuration,
        append_only: Optional[_builtins.bool] = ...,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptions
        ] = ...,
        destination_table_configurations: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfiguration
            ]
        ] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogArn")
    def catalog_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamIcebergConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter(name="appendOnly")
    def append_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="destinationTableConfigurations")
    def destination_table_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfiguration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        table_name: _builtins.str,
        s3_error_output_prefix: Optional[_builtins.str] = ...,
        unique_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3ErrorOutputPrefix")
    def s3_error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKeys")
    def unique_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessor(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamKinesisSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kinesis_stream_arn: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamMskSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_configuration: outputs.FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfiguration,
        msk_cluster_arn: _builtins.str,
        topic_name: _builtins.str,
        read_from_timestamp: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> (
        outputs.FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfiguration
    ): ...
    @_builtins.property
    @pulumi.getter(name="mskClusterArn")
    def msk_cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readFromTimestamp")
    def read_from_timestamp(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, connectivity: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connectivity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        index_name: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamOpensearchConfigurationS3Configuration,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptions
        ] = ...,
        cluster_endpoint: Optional[_builtins.str] = ...,
        document_id_options: Optional[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptions
        ] = ...,
        domain_arn: Optional[_builtins.str] = ...,
        index_rotation_period: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        type_name: Optional[_builtins.str] = ...,
        vpc_config: Optional[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamOpensearchConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentIdOptions")
    def document_id_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexRotationPeriod")
    def index_rotation_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[outputs.FirehoseDeliveryStreamOpensearchConfigurationVpcConfig]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, default_document_id_format: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultDocumentIdFormat")
    def default_document_id_format(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchConfigurationVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_arn: _builtins.str,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collection_endpoint: _builtins.str,
        index_name: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationS3Configuration,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptions
        ] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        vpc_config: Optional[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionEndpoint")
    def collection_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> (
        outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationS3Configuration
    ): ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfig
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfiguration(
    dict
):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_arn: _builtins.str,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_jdbcurl: _builtins.str,
        data_table_name: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamRedshiftConfigurationS3Configuration,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions
        ] = ...,
        copy_options: Optional[_builtins.str] = ...,
        data_table_columns: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_configuration: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration
        ] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        secrets_manager_configuration: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfiguration
        ] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterJdbcurl")
    def cluster_jdbcurl(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTableName")
    def data_table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamRedshiftConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="copyOptions")
    def copy_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataTableColumns")
    def data_table_columns(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        role_arn: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamServerSideEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        key_arn: Optional[_builtins.str] = ...,
        key_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_url: _builtins.str,
        database: _builtins.str,
        role_arn: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamSnowflakeConfigurationS3Configuration,
        schema: _builtins.str,
        table: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptions
        ] = ...,
        content_column_name: Optional[_builtins.str] = ...,
        data_loading_option: Optional[_builtins.str] = ...,
        key_passphrase: Optional[_builtins.str] = ...,
        metadata_column_name: Optional[_builtins.str] = ...,
        private_key: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        secrets_manager_configuration: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfiguration
        ] = ...,
        snowflake_role_configuration: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfiguration
        ] = ...,
        snowflake_vpc_configuration: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfiguration
        ] = ...,
        user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountUrl")
    def account_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamSnowflakeConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="contentColumnName")
    def content_column_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataLoadingOption")
    def data_loading_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPassphrase")
    def key_passphrase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataColumnName")
    def metadata_column_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snowflakeRoleConfiguration")
    def snowflake_role_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snowflakeVpcConfiguration")
    def snowflake_vpc_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessor(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        role_arn: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        snowflake_role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="snowflakeRole")
    def snowflake_role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, private_link_vpce_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkVpceId")
    def private_link_vpce_id(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hec_endpoint: _builtins.str,
        s3_configuration: outputs.FirehoseDeliveryStreamSplunkConfigurationS3Configuration,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions
        ] = ...,
        hec_acknowledgment_timeout: Optional[_builtins.int] = ...,
        hec_endpoint_type: Optional[_builtins.str] = ...,
        hec_token: Optional[_builtins.str] = ...,
        processing_configuration: Optional[
            outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration
        ] = ...,
        retry_duration: Optional[_builtins.int] = ...,
        s3_backup_mode: Optional[_builtins.str] = ...,
        secrets_manager_configuration: Optional[
            outputs.FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hecEndpoint")
    def hec_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.FirehoseDeliveryStreamSplunkConfigurationS3Configuration: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hecAcknowledgmentTimeout")
    def hec_acknowledgment_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="hecEndpointType")
    def hec_endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hecToken")
    def hec_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfiguration
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        processors: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[
            Sequence[
                outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter
        ]
    ]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        role_arn: _builtins.str,
        buffering_interval: Optional[_builtins.int] = ...,
        buffering_size: Optional[_builtins.int] = ...,
        cloudwatch_logging_options: Optional[
            outputs.FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptions
        ] = ...,
        compression_format: Optional[_builtins.str] = ...,
        error_output_prefix: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> Optional[
        outputs.FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        log_group_name: Optional[_builtins.str] = ...,
        log_stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        role_arn: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamStreamModeDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, stream_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamMode")
    def stream_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetStreamStreamModeDetailResult(dict):
    def __init__(__self__, *, stream_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamMode")
    def stream_mode(self) -> _builtins.str: ...
