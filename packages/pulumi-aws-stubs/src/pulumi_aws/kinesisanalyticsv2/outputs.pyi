import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationApplicationConfiguration",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ApplicationCloudwatchLoggingOptions",
]

@pulumi.output_type
class ApplicationApplicationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_code_configuration: outputs.ApplicationApplicationConfigurationApplicationCodeConfiguration,
        application_encryption_configuration: Optional[
            outputs.ApplicationApplicationConfigurationApplicationEncryptionConfiguration
        ] = ...,
        application_snapshot_configuration: Optional[
            outputs.ApplicationApplicationConfigurationApplicationSnapshotConfiguration
        ] = ...,
        environment_properties: Optional[
            outputs.ApplicationApplicationConfigurationEnvironmentProperties
        ] = ...,
        flink_application_configuration: Optional[
            outputs.ApplicationApplicationConfigurationFlinkApplicationConfiguration
        ] = ...,
        run_configuration: Optional[
            outputs.ApplicationApplicationConfigurationRunConfiguration
        ] = ...,
        sql_application_configuration: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfiguration
        ] = ...,
        vpc_configuration: Optional[
            outputs.ApplicationApplicationConfigurationVpcConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationCodeConfiguration")
    def application_code_configuration(
        self,
    ) -> outputs.ApplicationApplicationConfigurationApplicationCodeConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="applicationEncryptionConfiguration")
    def application_encryption_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationApplicationEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="applicationSnapshotConfiguration")
    def application_snapshot_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationApplicationSnapshotConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="environmentProperties")
    def environment_properties(
        self,
    ) -> Optional[outputs.ApplicationApplicationConfigurationEnvironmentProperties]: ...
    @_builtins.property
    @pulumi.getter(name="flinkApplicationConfiguration")
    def flink_application_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationFlinkApplicationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="runConfiguration")
    def run_configuration(
        self,
    ) -> Optional[outputs.ApplicationApplicationConfigurationRunConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="sqlApplicationConfiguration")
    def sql_application_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[outputs.ApplicationApplicationConfigurationVpcConfiguration]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationApplicationCodeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_content_type: _builtins.str,
        code_content: Optional[
            outputs.ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeContentType")
    def code_content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="codeContent")
    def code_content(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_content_location: Optional[
            outputs.ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation
        ] = ...,
        text_content: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ContentLocation")
    def s3_content_location(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation
    ]: ...
    @_builtins.property
    @pulumi.getter(name="textContent")
    def text_content(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        file_key: _builtins.str,
        object_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationApplicationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key_type: _builtins.str, key_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationApplicationSnapshotConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, snapshots_enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snapshotsEnabled")
    def snapshots_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ApplicationApplicationConfigurationEnvironmentProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        property_groups: Sequence[
            outputs.ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyGroups")
    def property_groups(
        self,
    ) -> Sequence[
        outputs.ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        property_group_id: _builtins.str,
        property_map: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyGroupId")
    def property_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="propertyMap")
    def property_map(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationFlinkApplicationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        checkpoint_configuration: Optional[
            outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration
        ] = ...,
        monitoring_configuration: Optional[
            outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration
        ] = ...,
        parallelism_configuration: Optional[
            outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkpointConfiguration")
    def checkpoint_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        checkpoint_interval: Optional[_builtins.int] = ...,
        checkpointing_enabled: Optional[_builtins.bool] = ...,
        min_pause_between_checkpoints: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="checkpointInterval")
    def checkpoint_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="checkpointingEnabled")
    def checkpointing_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="minPauseBetweenCheckpoints")
    def min_pause_between_checkpoints(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        log_level: Optional[_builtins.str] = ...,
        metrics_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricsLevel")
    def metrics_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_type: _builtins.str,
        auto_scaling_enabled: Optional[_builtins.bool] = ...,
        parallelism: Optional[_builtins.int] = ...,
        parallelism_per_kpu: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingEnabled")
    def auto_scaling_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parallelismPerKpu")
    def parallelism_per_kpu(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationRunConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_restore_configuration: Optional[
            outputs.ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration
        ] = ...,
        flink_run_configuration: Optional[
            outputs.ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationRestoreConfiguration")
    def application_restore_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="flinkRunConfiguration")
    def flink_run_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_restore_type: Optional[_builtins.str] = ...,
        snapshot_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationRestoreType")
    def application_restore_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allow_non_restored_state: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNonRestoredState")
    def allow_non_restored_state(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInput
        ] = ...,
        outputs: Optional[
            Sequence[
                outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutput
            ]
        ] = ...,
        reference_data_source: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def input(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInput
    ]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutput
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="referenceDataSource")
    def reference_data_source(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_schema: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema,
        name_prefix: _builtins.str,
        in_app_stream_names: Optional[Sequence[_builtins.str]] = ...,
        input_id: Optional[_builtins.str] = ...,
        input_parallelism: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism
        ] = ...,
        input_processing_configuration: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration
        ] = ...,
        input_starting_position_configurations: Optional[
            Sequence[
                outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration
            ]
        ] = ...,
        kinesis_firehose_input: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput
        ] = ...,
        kinesis_streams_input: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inAppStreamNames")
    def in_app_stream_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputId")
    def input_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputParallelism")
    def input_parallelism(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputProcessingConfiguration")
    def input_processing_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputStartingPositionConfigurations")
    def input_starting_position_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamsInput")
    def kinesis_streams_input(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism(
    dict
):
    def __init__(__self__, *, count: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_lambda_processor: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputLambdaProcessor")
    def input_lambda_processor(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_columns: Sequence[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn
        ],
        record_format: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat,
        record_encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(
        self,
    ) -> Sequence[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat: ...
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn(
    dict
):
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
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mapping_parameters: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters,
        record_format_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        csv_mapping_parameters: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters
        ] = ...,
        json_mapping_parameters: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvMappingParameters")
    def csv_mapping_parameters(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters
    ]: ...
    @_builtins.property
    @pulumi.getter(name="jsonMappingParameters")
    def json_mapping_parameters(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters(
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
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_row_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, input_starting_position: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputStartingPosition")
    def input_starting_position(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_schema: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema,
        name: _builtins.str,
        kinesis_firehose_output: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput
        ] = ...,
        kinesis_streams_output: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput
        ] = ...,
        lambda_output: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput
        ] = ...,
        output_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationSchema")
    def destination_schema(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseOutput")
    def kinesis_firehose_output(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamsOutput")
    def kinesis_streams_output(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaOutput")
    def lambda_output(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputId")
    def output_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_format_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        reference_schema: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema,
        s3_reference_data_source: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource,
        table_name: _builtins.str,
        reference_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceSchema")
    def reference_schema(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema: ...
    @_builtins.property
    @pulumi.getter(name="s3ReferenceDataSource")
    def s3_reference_data_source(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_columns: Sequence[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn
        ],
        record_format: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat,
        record_encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(
        self,
    ) -> Sequence[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat: ...
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn(
    dict
):
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
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mapping_parameters: outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters,
        record_format_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters: ...
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        csv_mapping_parameters: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters
        ] = ...,
        json_mapping_parameters: Optional[
            outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvMappingParameters")
    def csv_mapping_parameters(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters
    ]: ...
    @_builtins.property
    @pulumi.getter(name="jsonMappingParameters")
    def json_mapping_parameters(
        self,
    ) -> Optional[
        outputs.ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters
    ]: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters(
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
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_row_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, bucket_arn: _builtins.str, file_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationApplicationConfigurationVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_configuration_id: Optional[_builtins.str] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfigurationId")
    def vpc_configuration_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationCloudwatchLoggingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        log_stream_arn: _builtins.str,
        cloudwatch_logging_option_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logStreamArn")
    def log_stream_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptionId")
    def cloudwatch_logging_option_id(self) -> Optional[_builtins.str]: ...
