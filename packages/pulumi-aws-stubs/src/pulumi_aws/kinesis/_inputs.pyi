

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalyticsApplicationCloudwatchLoggingOptionsArgs', ..., 'AnalyticsApplicationInputsArgs', 'AnalyticsApplicationInputsArgsDict', 'AnalyticsApplicationInputsKinesisFirehoseArgs', 'AnalyticsApplicationInputsKinesisFirehoseArgsDict', 'AnalyticsApplicationInputsKinesisStreamArgs', 'AnalyticsApplicationInputsKinesisStreamArgsDict', 'AnalyticsApplicationInputsParallelismArgs', 'AnalyticsApplicationInputsParallelismArgsDict', ..., ..., ..., ..., 'AnalyticsApplicationInputsSchemaArgs', 'AnalyticsApplicationInputsSchemaArgsDict', 'AnalyticsApplicationInputsSchemaRecordColumnArgs', ..., 'AnalyticsApplicationInputsSchemaRecordFormatArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'AnalyticsApplicationOutputArgs', 'AnalyticsApplicationOutputArgsDict', 'AnalyticsApplicationOutputKinesisFirehoseArgs', 'AnalyticsApplicationOutputKinesisFirehoseArgsDict', 'AnalyticsApplicationOutputKinesisStreamArgs', 'AnalyticsApplicationOutputKinesisStreamArgsDict', 'AnalyticsApplicationOutputLambdaArgs', 'AnalyticsApplicationOutputLambdaArgsDict', 'AnalyticsApplicationOutputSchemaArgs', 'AnalyticsApplicationOutputSchemaArgsDict', 'AnalyticsApplicationReferenceDataSourcesArgs', 'AnalyticsApplicationReferenceDataSourcesArgsDict', 'AnalyticsApplicationReferenceDataSourcesS3Args', 'AnalyticsApplicationReferenceDataSourcesS3ArgsDict', 'AnalyticsApplicationReferenceDataSourcesSchemaArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamExtendedS3ConfigurationArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamIcebergConfigurationArgs', 'FirehoseDeliveryStreamIcebergConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamMskSourceConfigurationArgs', ..., ..., ..., 'FirehoseDeliveryStreamOpensearchConfigurationArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamRedshiftConfigurationArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamServerSideEncryptionArgs', 'FirehoseDeliveryStreamServerSideEncryptionArgsDict', 'FirehoseDeliveryStreamSnowflakeConfigurationArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FirehoseDeliveryStreamSplunkConfigurationArgs', 'FirehoseDeliveryStreamSplunkConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'StreamStreamModeDetailsArgs', 'StreamStreamModeDetailsArgsDict']
class AnalyticsApplicationCloudwatchLoggingOptionsArgsDict(TypedDict):
    log_stream_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, log_stream_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamArn")
    def log_stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_stream_arn.setter
    def log_stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationInputsArgsDict(TypedDict):
    name_prefix: pulumi.Input[_builtins.str]
    schema: pulumi.Input[AnalyticsApplicationInputsSchemaArgsDict]
    id: NotRequired[pulumi.Input[_builtins.str]]
    kinesis_firehose: NotRequired[pulumi.Input[AnalyticsApplicationInputsKinesisFirehoseArgsDict]]
    kinesis_stream: NotRequired[pulumi.Input[AnalyticsApplicationInputsKinesisStreamArgsDict]]
    parallelism: NotRequired[pulumi.Input[AnalyticsApplicationInputsParallelismArgsDict]]
    processing_configuration: NotRequired[pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationArgsDict]]
    starting_position_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsStartingPositionConfigurationArgsDict]]]]
    stream_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnalyticsApplicationInputsArgs:
    def __init__(__self__, *, name_prefix: pulumi.Input[_builtins.str], schema: pulumi.Input[AnalyticsApplicationInputsSchemaArgs], id: Optional[pulumi.Input[_builtins.str]] = ..., kinesis_firehose: Optional[pulumi.Input[AnalyticsApplicationInputsKinesisFirehoseArgs]] = ..., kinesis_stream: Optional[pulumi.Input[AnalyticsApplicationInputsKinesisStreamArgs]] = ..., parallelism: Optional[pulumi.Input[AnalyticsApplicationInputsParallelismArgs]] = ..., processing_configuration: Optional[pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationArgs]] = ..., starting_position_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsStartingPositionConfigurationArgs]]]] = ..., stream_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[AnalyticsApplicationInputsSchemaArgs]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[AnalyticsApplicationInputsSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsKinesisFirehoseArgs]]:
        
        ...
    
    @kinesis_firehose.setter
    def kinesis_firehose(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsKinesisFirehoseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStream")
    def kinesis_stream(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsKinesisStreamArgs]]:
        
        ...
    
    @kinesis_stream.setter
    def kinesis_stream(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsKinesisStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsParallelismArgs]]:
        
        ...
    
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsParallelismArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPositionConfigurations")
    def starting_position_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsStartingPositionConfigurationArgs]]]]:
        
        ...
    
    @starting_position_configurations.setter
    def starting_position_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsStartingPositionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamNames")
    def stream_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @stream_names.setter
    def stream_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnalyticsApplicationInputsKinesisFirehoseArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationInputsKinesisFirehoseArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationInputsKinesisStreamArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationInputsKinesisStreamArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationInputsParallelismArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AnalyticsApplicationInputsParallelismArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AnalyticsApplicationInputsProcessingConfigurationArgsDict(TypedDict):
    lambda_: pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationLambdaArgsDict]


@pulumi.input_type
class AnalyticsApplicationInputsProcessingConfigurationArgs:
    def __init__(__self__, *, lambda_: pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationLambdaArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationLambdaArgs]:
        
        ...
    
    @lambda_.setter
    def lambda_(self, value: pulumi.Input[AnalyticsApplicationInputsProcessingConfigurationLambdaArgs]): # -> None:
        ...
    


class AnalyticsApplicationInputsProcessingConfigurationLambdaArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationInputsProcessingConfigurationLambdaArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaArgsDict(TypedDict):
    record_columns: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsSchemaRecordColumnArgsDict]]]
    record_format: pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatArgsDict]
    record_encoding: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaArgs:
    def __init__(__self__, *, record_columns: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsSchemaRecordColumnArgs]]], record_format: pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatArgs], record_encoding: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(self) -> pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsSchemaRecordColumnArgs]]]:
        
        ...
    
    @record_columns.setter
    def record_columns(self, value: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationInputsSchemaRecordColumnArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(self) -> pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatArgs]:
        
        ...
    
    @record_format.setter
    def record_format(self, value: pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_encoding.setter
    def record_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaRecordColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sql_type: pulumi.Input[_builtins.str]
    mapping: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaRecordColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], sql_type: pulumi.Input[_builtins.str], mapping: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_type.setter
    def sql_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping.setter
    def mapping(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaRecordFormatArgsDict(TypedDict):
    mapping_parameters: NotRequired[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgsDict]]
    record_format_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaRecordFormatArgs:
    def __init__(__self__, *, mapping_parameters: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs]] = ..., record_format_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs]]:
        
        ...
    
    @mapping_parameters.setter
    def mapping_parameters(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgsDict(TypedDict):
    csv: NotRequired[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgsDict]]
    json: NotRequired[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgsDict]]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs:
    def __init__(__self__, *, csv: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgs]] = ..., json: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgs]]:
        
        ...
    
    @csv.setter
    def csv(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs]]:
        
        ...
    
    @json.setter
    def json(self, value: Optional[pulumi.Input[AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs]]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgsDict(TypedDict):
    record_column_delimiter: pulumi.Input[_builtins.str]
    record_row_delimiter: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgs:
    def __init__(__self__, *, record_column_delimiter: pulumi.Input[_builtins.str], record_row_delimiter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_column_delimiter.setter
    def record_column_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_delimiter.setter
    def record_row_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgsDict(TypedDict):
    record_row_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs:
    def __init__(__self__, *, record_row_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_path.setter
    def record_row_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationInputsStartingPositionConfigurationArgsDict(TypedDict):
    starting_position: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationInputsStartingPositionConfigurationArgs:
    def __init__(__self__, *, starting_position: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationOutputArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    schema: pulumi.Input[AnalyticsApplicationOutputSchemaArgsDict]
    id: NotRequired[pulumi.Input[_builtins.str]]
    kinesis_firehose: NotRequired[pulumi.Input[AnalyticsApplicationOutputKinesisFirehoseArgsDict]]
    kinesis_stream: NotRequired[pulumi.Input[AnalyticsApplicationOutputKinesisStreamArgsDict]]
    lambda_: NotRequired[pulumi.Input[AnalyticsApplicationOutputLambdaArgsDict]]


@pulumi.input_type
class AnalyticsApplicationOutputArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], schema: pulumi.Input[AnalyticsApplicationOutputSchemaArgs], id: Optional[pulumi.Input[_builtins.str]] = ..., kinesis_firehose: Optional[pulumi.Input[AnalyticsApplicationOutputKinesisFirehoseArgs]] = ..., kinesis_stream: Optional[pulumi.Input[AnalyticsApplicationOutputKinesisStreamArgs]] = ..., lambda_: Optional[pulumi.Input[AnalyticsApplicationOutputLambdaArgs]] = ...) -> None:
        
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
    def schema(self) -> pulumi.Input[AnalyticsApplicationOutputSchemaArgs]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[AnalyticsApplicationOutputSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(self) -> Optional[pulumi.Input[AnalyticsApplicationOutputKinesisFirehoseArgs]]:
        
        ...
    
    @kinesis_firehose.setter
    def kinesis_firehose(self, value: Optional[pulumi.Input[AnalyticsApplicationOutputKinesisFirehoseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStream")
    def kinesis_stream(self) -> Optional[pulumi.Input[AnalyticsApplicationOutputKinesisStreamArgs]]:
        
        ...
    
    @kinesis_stream.setter
    def kinesis_stream(self, value: Optional[pulumi.Input[AnalyticsApplicationOutputKinesisStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[AnalyticsApplicationOutputLambdaArgs]]:
        
        ...
    
    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[AnalyticsApplicationOutputLambdaArgs]]): # -> None:
        ...
    


class AnalyticsApplicationOutputKinesisFirehoseArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationOutputKinesisFirehoseArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationOutputKinesisStreamArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationOutputKinesisStreamArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationOutputLambdaArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationOutputLambdaArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationOutputSchemaArgsDict(TypedDict):
    record_format_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationOutputSchemaArgs:
    def __init__(__self__, *, record_format_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesArgsDict(TypedDict):
    s3: pulumi.Input[AnalyticsApplicationReferenceDataSourcesS3ArgsDict]
    schema: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaArgsDict]
    table_name: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesArgs:
    def __init__(__self__, *, s3: pulumi.Input[AnalyticsApplicationReferenceDataSourcesS3Args], schema: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaArgs], table_name: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Input[AnalyticsApplicationReferenceDataSourcesS3Args]:
        
        ...
    
    @s3.setter
    def s3(self, value: pulumi.Input[AnalyticsApplicationReferenceDataSourcesS3Args]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaArgs]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesS3ArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    file_key: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesS3Args:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], file_key: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_key.setter
    def file_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaArgsDict(TypedDict):
    record_columns: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgsDict]]]
    record_format: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgsDict]
    record_encoding: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaArgs:
    def __init__(__self__, *, record_columns: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgs]]], record_format: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgs], record_encoding: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(self) -> pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgs]]]:
        
        ...
    
    @record_columns.setter
    def record_columns(self, value: pulumi.Input[Sequence[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(self) -> pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgs]:
        
        ...
    
    @record_format.setter
    def record_format(self, value: pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_encoding.setter
    def record_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sql_type: pulumi.Input[_builtins.str]
    mapping: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], sql_type: pulumi.Input[_builtins.str], mapping: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_type.setter
    def sql_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping.setter
    def mapping(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgsDict(TypedDict):
    mapping_parameters: NotRequired[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgsDict]]
    record_format_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgs:
    def __init__(__self__, *, mapping_parameters: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgs]] = ..., record_format_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(self) -> Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgs]]:
        
        ...
    
    @mapping_parameters.setter
    def mapping_parameters(self, value: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgsDict(TypedDict):
    csv: NotRequired[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgsDict]]
    json: NotRequired[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgsDict]]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgs:
    def __init__(__self__, *, csv: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgs]] = ..., json: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgs]]:
        
        ...
    
    @csv.setter
    def csv(self, value: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgs]]:
        
        ...
    
    @json.setter
    def json(self, value: Optional[pulumi.Input[AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgs]]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgsDict(TypedDict):
    record_column_delimiter: pulumi.Input[_builtins.str]
    record_row_delimiter: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgs:
    def __init__(__self__, *, record_column_delimiter: pulumi.Input[_builtins.str], record_row_delimiter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_column_delimiter.setter
    def record_column_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_delimiter.setter
    def record_row_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgsDict(TypedDict):
    record_row_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgs:
    def __init__(__self__, *, record_row_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_path.setter
    def record_row_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationArgsDict(TypedDict):
    index_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgsDict]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgsDict]]
    cluster_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    domain_arn: NotRequired[pulumi.Input[_builtins.str]]
    index_rotation_period: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    type_name: NotRequired[pulumi.Input[_builtins.str]]
    vpc_config: NotRequired[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationArgs:
    def __init__(__self__, *, index_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgs], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs]] = ..., cluster_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., domain_arn: Optional[pulumi.Input[_builtins.str]] = ..., index_rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_endpoint.setter
    def cluster_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_arn.setter
    def domain_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexRotationPeriod")
    def index_rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_rotation_period.setter
    def index_rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamElasticsearchConfigurationVpcConfigArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    custom_time_zone: NotRequired[pulumi.Input[_builtins.str]]
    data_format_conversion_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgsDict]]
    dynamic_partitioning_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgsDict]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    file_extension: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgsDict]]
    s3_backup_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgsDict]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., custom_time_zone: Optional[pulumi.Input[_builtins.str]] = ..., data_format_conversion_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs]] = ..., dynamic_partitioning_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgs]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., file_extension: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs]] = ..., s3_backup_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTimeZone")
    def custom_time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_time_zone.setter
    def custom_time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormatConversionConfiguration")
    def data_format_conversion_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs]]:
        
        ...
    
    @data_format_conversion_configuration.setter
    def data_format_conversion_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicPartitioningConfiguration")
    def dynamic_partitioning_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgs]]:
        
        ...
    
    @dynamic_partitioning_configuration.setter
    def dynamic_partitioning_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileExtension")
    def file_extension(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_extension.setter
    def file_extension(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupConfiguration")
    def s3_backup_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs]]:
        
        ...
    
    @s3_backup_configuration.setter
    def s3_backup_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgsDict(TypedDict):
    input_format_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgsDict]
    output_format_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgsDict]
    schema_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgsDict]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs:
    def __init__(__self__, *, input_format_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs], output_format_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs], schema_configuration: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs], enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormatConfiguration")
    def input_format_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs]:
        
        ...
    
    @input_format_configuration.setter
    def input_format_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormatConfiguration")
    def output_format_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs]:
        
        ...
    
    @output_format_configuration.setter
    def output_format_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaConfiguration")
    def schema_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs]:
        
        ...
    
    @schema_configuration.setter
    def schema_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgsDict(TypedDict):
    deserializer: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgsDict]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs:
    def __init__(__self__, *, deserializer: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deserializer(self) -> pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs]:
        
        ...
    
    @deserializer.setter
    def deserializer(self, value: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgsDict(TypedDict):
    hive_json_ser_de: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgsDict]]
    open_x_json_ser_de: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs:
    def __init__(__self__, *, hive_json_ser_de: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs]] = ..., open_x_json_ser_de: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveJsonSerDe")
    def hive_json_ser_de(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs]]:
        
        ...
    
    @hive_json_ser_de.setter
    def hive_json_ser_de(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openXJsonSerDe")
    def open_x_json_ser_de(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs]]:
        
        ...
    
    @open_x_json_ser_de.setter
    def open_x_json_ser_de(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgsDict(TypedDict):
    timestamp_formats: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs:
    def __init__(__self__, *, timestamp_formats: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampFormats")
    def timestamp_formats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @timestamp_formats.setter
    def timestamp_formats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgsDict(TypedDict):
    case_insensitive: NotRequired[pulumi.Input[_builtins.bool]]
    column_to_json_key_mappings: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    convert_dots_in_json_keys_to_underscores: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs:
    def __init__(__self__, *, case_insensitive: Optional[pulumi.Input[_builtins.bool]] = ..., column_to_json_key_mappings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., convert_dots_in_json_keys_to_underscores: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseInsensitive")
    def case_insensitive(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @case_insensitive.setter
    def case_insensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnToJsonKeyMappings")
    def column_to_json_key_mappings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @column_to_json_key_mappings.setter
    def column_to_json_key_mappings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="convertDotsInJsonKeysToUnderscores")
    def convert_dots_in_json_keys_to_underscores(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @convert_dots_in_json_keys_to_underscores.setter
    def convert_dots_in_json_keys_to_underscores(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgsDict(TypedDict):
    serializer: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgsDict]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs:
    def __init__(__self__, *, serializer: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serializer(self) -> pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs]:
        
        ...
    
    @serializer.setter
    def serializer(self, value: pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgsDict(TypedDict):
    orc_ser_de: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgsDict]]
    parquet_ser_de: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs:
    def __init__(__self__, *, orc_ser_de: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs]] = ..., parquet_ser_de: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orcSerDe")
    def orc_ser_de(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs]]:
        
        ...
    
    @orc_ser_de.setter
    def orc_ser_de(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parquetSerDe")
    def parquet_ser_de(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs]]:
        
        ...
    
    @parquet_ser_de.setter
    def parquet_ser_de(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgsDict(TypedDict):
    block_size_bytes: NotRequired[pulumi.Input[_builtins.int]]
    bloom_filter_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bloom_filter_false_positive_probability: NotRequired[pulumi.Input[_builtins.float]]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    dictionary_key_threshold: NotRequired[pulumi.Input[_builtins.float]]
    enable_padding: NotRequired[pulumi.Input[_builtins.bool]]
    format_version: NotRequired[pulumi.Input[_builtins.str]]
    padding_tolerance: NotRequired[pulumi.Input[_builtins.float]]
    row_index_stride: NotRequired[pulumi.Input[_builtins.int]]
    stripe_size_bytes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs:
    def __init__(__self__, *, block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., bloom_filter_columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bloom_filter_false_positive_probability: Optional[pulumi.Input[_builtins.float]] = ..., compression: Optional[pulumi.Input[_builtins.str]] = ..., dictionary_key_threshold: Optional[pulumi.Input[_builtins.float]] = ..., enable_padding: Optional[pulumi.Input[_builtins.bool]] = ..., format_version: Optional[pulumi.Input[_builtins.str]] = ..., padding_tolerance: Optional[pulumi.Input[_builtins.float]] = ..., row_index_stride: Optional[pulumi.Input[_builtins.int]] = ..., stripe_size_bytes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bloomFilterColumns")
    def bloom_filter_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @bloom_filter_columns.setter
    def bloom_filter_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bloomFilterFalsePositiveProbability")
    def bloom_filter_false_positive_probability(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @bloom_filter_false_positive_probability.setter
    def bloom_filter_false_positive_probability(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dictionaryKeyThreshold")
    def dictionary_key_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @dictionary_key_threshold.setter
    def dictionary_key_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePadding")
    def enable_padding(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_padding.setter
    def enable_padding(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="formatVersion")
    def format_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @format_version.setter
    def format_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="paddingTolerance")
    def padding_tolerance(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @padding_tolerance.setter
    def padding_tolerance(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowIndexStride")
    def row_index_stride(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @row_index_stride.setter
    def row_index_stride(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stripeSizeBytes")
    def stripe_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @stripe_size_bytes.setter
    def stripe_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgsDict(TypedDict):
    block_size_bytes: NotRequired[pulumi.Input[_builtins.int]]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    enable_dictionary_compression: NotRequired[pulumi.Input[_builtins.bool]]
    max_padding_bytes: NotRequired[pulumi.Input[_builtins.int]]
    page_size_bytes: NotRequired[pulumi.Input[_builtins.int]]
    writer_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs:
    def __init__(__self__, *, block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., compression: Optional[pulumi.Input[_builtins.str]] = ..., enable_dictionary_compression: Optional[pulumi.Input[_builtins.bool]] = ..., max_padding_bytes: Optional[pulumi.Input[_builtins.int]] = ..., page_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., writer_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDictionaryCompression")
    def enable_dictionary_compression(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dictionary_compression.setter
    def enable_dictionary_compression(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPaddingBytes")
    def max_padding_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_padding_bytes.setter
    def max_padding_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pageSizeBytes")
    def page_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @page_size_bytes.setter
    def page_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writerVersion")
    def writer_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @writer_version.setter
    def writer_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    version_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]]:
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationArgsDict(TypedDict):
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgsDict]
    url: pulumi.Input[_builtins.str]
    access_key: NotRequired[pulumi.Input[_builtins.str]]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgsDict]]
    request_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationArgs:
    def __init__(__self__, *, s3_configuration: pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgs], url: pulumi.Input[_builtins.str], access_key: Optional[pulumi.Input[_builtins.str]] = ..., buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgs]] = ..., request_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., secrets_manager_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestConfiguration")
    def request_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgs]]:
        
        ...
    
    @request_configuration.setter
    def request_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgs]]:
        
        ...
    
    @secrets_manager_configuration.setter
    def secrets_manager_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgsDict(TypedDict):
    common_attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgsDict]]]]
    content_encoding: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationArgs:
    def __init__(__self__, *, common_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgs]]]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonAttributes")
    def common_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgs]]]]:
        
        ...
    
    @common_attributes.setter
    def common_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
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
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamHttpEndpointConfigurationSecretsManagerConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationArgsDict(TypedDict):
    catalog_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgsDict]
    append_only: NotRequired[pulumi.Input[_builtins.bool]]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgsDict]]
    destination_table_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgsDict]]]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationArgs:
    def __init__(__self__, *, catalog_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgs], append_only: Optional[pulumi.Input[_builtins.bool]] = ..., buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgs]] = ..., destination_table_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgs]]]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogArn")
    def catalog_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_arn.setter
    def catalog_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appendOnly")
    def append_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @append_only.setter
    def append_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationTableConfigurations")
    def destination_table_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgs]]]]:
        
        ...
    
    @destination_table_configurations.setter
    def destination_table_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    s3_error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    unique_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationDestinationTableConfigurationArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], s3_error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., unique_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ErrorOutputPrefix")
    def s3_error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_error_output_prefix.setter
    def s3_error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueKeys")
    def unique_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @unique_keys.setter
    def unique_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamIcebergConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamKinesisSourceConfigurationArgsDict(TypedDict):
    kinesis_stream_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamKinesisSourceConfigurationArgs:
    def __init__(__self__, *, kinesis_stream_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kinesis_stream_arn.setter
    def kinesis_stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamMskSourceConfigurationArgsDict(TypedDict):
    authentication_configuration: pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgsDict]
    msk_cluster_arn: pulumi.Input[_builtins.str]
    topic_name: pulumi.Input[_builtins.str]
    read_from_timestamp: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamMskSourceConfigurationArgs:
    def __init__(__self__, *, authentication_configuration: pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgs], msk_cluster_arn: pulumi.Input[_builtins.str], topic_name: pulumi.Input[_builtins.str], read_from_timestamp: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgs]:
        
        ...
    
    @authentication_configuration.setter
    def authentication_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mskClusterArn")
    def msk_cluster_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @msk_cluster_arn.setter
    def msk_cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readFromTimestamp")
    def read_from_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @read_from_timestamp.setter
    def read_from_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgsDict(TypedDict):
    connectivity: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamMskSourceConfigurationAuthenticationConfigurationArgs:
    def __init__(__self__, *, connectivity: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connectivity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connectivity.setter
    def connectivity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationArgsDict(TypedDict):
    index_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgsDict]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgsDict]]
    cluster_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    document_id_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgsDict]]
    domain_arn: NotRequired[pulumi.Input[_builtins.str]]
    index_rotation_period: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    type_name: NotRequired[pulumi.Input[_builtins.str]]
    vpc_config: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationArgs:
    def __init__(__self__, *, index_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgs], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgs]] = ..., cluster_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., document_id_options: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgs]] = ..., domain_arn: Optional[pulumi.Input[_builtins.str]] = ..., index_rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_endpoint.setter
    def cluster_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentIdOptions")
    def document_id_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgs]]:
        
        ...
    
    @document_id_options.setter
    def document_id_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_arn.setter
    def domain_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexRotationPeriod")
    def index_rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_rotation_period.setter
    def index_rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgsDict(TypedDict):
    default_document_id_format: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationDocumentIdOptionsArgs:
    def __init__(__self__, *, default_document_id_format: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDocumentIdFormat")
    def default_document_id_format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_document_id_format.setter
    def default_document_id_format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchConfigurationVpcConfigArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationArgsDict(TypedDict):
    collection_endpoint: pulumi.Input[_builtins.str]
    index_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgsDict]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgsDict]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    vpc_config: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationArgs:
    def __init__(__self__, *, collection_endpoint: pulumi.Input[_builtins.str], index_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgs], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgs]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionEndpoint")
    def collection_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection_endpoint.setter
    def collection_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamOpensearchserverlessConfigurationVpcConfigArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationArgsDict(TypedDict):
    cluster_jdbcurl: pulumi.Input[_builtins.str]
    data_table_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgsDict]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgsDict]]
    copy_options: NotRequired[pulumi.Input[_builtins.str]]
    data_table_columns: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgsDict]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgsDict]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationArgs:
    def __init__(__self__, *, cluster_jdbcurl: pulumi.Input[_builtins.str], data_table_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgs], cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs]] = ..., copy_options: Optional[pulumi.Input[_builtins.str]] = ..., data_table_columns: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., secrets_manager_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgs]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterJdbcurl")
    def cluster_jdbcurl(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_jdbcurl.setter
    def cluster_jdbcurl(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTableName")
    def data_table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_table_name.setter
    def data_table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyOptions")
    def copy_options(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @copy_options.setter
    def copy_options(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTableColumns")
    def data_table_columns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_table_columns.setter
    def data_table_columns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupConfiguration")
    def s3_backup_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs]]:
        
        ...
    
    @s3_backup_configuration.setter
    def s3_backup_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgs]]:
        ...
    
    @secrets_manager_configuration.setter
    def secrets_manager_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]]:
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamRedshiftConfigurationSecretsManagerConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamServerSideEncryptionArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    key_arn: NotRequired[pulumi.Input[_builtins.str]]
    key_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamServerSideEncryptionArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_arn: Optional[pulumi.Input[_builtins.str]] = ..., key_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_arn.setter
    def key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_type.setter
    def key_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationArgsDict(TypedDict):
    account_url: pulumi.Input[_builtins.str]
    database: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgsDict]
    schema: pulumi.Input[_builtins.str]
    table: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgsDict]]
    content_column_name: NotRequired[pulumi.Input[_builtins.str]]
    data_loading_option: NotRequired[pulumi.Input[_builtins.str]]
    key_passphrase: NotRequired[pulumi.Input[_builtins.str]]
    metadata_column_name: NotRequired[pulumi.Input[_builtins.str]]
    private_key: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgsDict]]
    snowflake_role_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgsDict]]
    snowflake_vpc_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgsDict]]
    user: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationArgs:
    def __init__(__self__, *, account_url: pulumi.Input[_builtins.str], database: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgs], schema: pulumi.Input[_builtins.str], table: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgs]] = ..., content_column_name: Optional[pulumi.Input[_builtins.str]] = ..., data_loading_option: Optional[pulumi.Input[_builtins.str]] = ..., key_passphrase: Optional[pulumi.Input[_builtins.str]] = ..., metadata_column_name: Optional[pulumi.Input[_builtins.str]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., secrets_manager_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgs]] = ..., snowflake_role_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgs]] = ..., snowflake_vpc_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgs]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountUrl")
    def account_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_url.setter
    def account_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentColumnName")
    def content_column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_column_name.setter
    def content_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLoadingOption")
    def data_loading_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_loading_option.setter
    def data_loading_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPassphrase")
    def key_passphrase(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_passphrase.setter
    def key_passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataColumnName")
    def metadata_column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_column_name.setter
    def metadata_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgs]]:
        
        ...
    
    @secrets_manager_configuration.setter
    def secrets_manager_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snowflakeRoleConfiguration")
    def snowflake_role_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgs]]:
        
        ...
    
    @snowflake_role_configuration.setter
    def snowflake_role_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snowflakeVpcConfiguration")
    def snowflake_vpc_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgs]]:
        
        ...
    
    @snowflake_vpc_configuration.setter
    def snowflake_vpc_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationSecretsManagerConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    snowflake_role: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeRoleConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., snowflake_role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snowflakeRole")
    def snowflake_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snowflake_role.setter
    def snowflake_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgsDict(TypedDict):
    private_link_vpce_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamSnowflakeConfigurationSnowflakeVpcConfigurationArgs:
    def __init__(__self__, *, private_link_vpce_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkVpceId")
    def private_link_vpce_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_link_vpce_id.setter
    def private_link_vpce_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationArgsDict(TypedDict):
    hec_endpoint: pulumi.Input[_builtins.str]
    s3_configuration: pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgsDict]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgsDict]]
    hec_acknowledgment_timeout: NotRequired[pulumi.Input[_builtins.int]]
    hec_endpoint_type: NotRequired[pulumi.Input[_builtins.str]]
    hec_token: NotRequired[pulumi.Input[_builtins.str]]
    processing_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgsDict]]
    retry_duration: NotRequired[pulumi.Input[_builtins.int]]
    s3_backup_mode: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_configuration: NotRequired[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgsDict]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationArgs:
    def __init__(__self__, *, hec_endpoint: pulumi.Input[_builtins.str], s3_configuration: pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgs], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs]] = ..., hec_acknowledgment_timeout: Optional[pulumi.Input[_builtins.int]] = ..., hec_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., hec_token: Optional[pulumi.Input[_builtins.str]] = ..., processing_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs]] = ..., retry_duration: Optional[pulumi.Input[_builtins.int]] = ..., s3_backup_mode: Optional[pulumi.Input[_builtins.str]] = ..., secrets_manager_configuration: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hecEndpoint")
    def hec_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hec_endpoint.setter
    def hec_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(self) -> pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgs]:
        
        ...
    
    @s3_configuration.setter
    def s3_configuration(self, value: pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hecAcknowledgmentTimeout")
    def hec_acknowledgment_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hec_acknowledgment_timeout.setter
    def hec_acknowledgment_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hecEndpointType")
    def hec_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hec_endpoint_type.setter
    def hec_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hecToken")
    def hec_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hec_token.setter
    def hec_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs]]:
        
        ...
    
    @processing_configuration.setter
    def processing_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryDuration")
    def retry_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_duration.setter
    def retry_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BackupMode")
    def s3_backup_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_backup_mode.setter
    def s3_backup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagerConfiguration")
    def secrets_manager_configuration(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgs]]:
        ...
    
    @secrets_manager_configuration.setter
    def secrets_manager_configuration(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgs]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., processors: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs]]]]:
        
        ...
    
    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgsDict]]]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs]]]] = ...) -> None:
        
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs]]]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    buffering_interval: NotRequired[pulumi.Input[_builtins.int]]
    buffering_size: NotRequired[pulumi.Input[_builtins.int]]
    cloudwatch_logging_options: NotRequired[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict]]
    compression_format: NotRequired[pulumi.Input[_builtins.str]]
    error_output_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], buffering_interval: Optional[pulumi.Input[_builtins.int]] = ..., buffering_size: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_logging_options: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]] = ..., compression_format: Optional[pulumi.Input[_builtins.str]] = ..., error_output_prefix: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingInterval")
    def buffering_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_interval.setter
    def buffering_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bufferingSize")
    def buffering_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @buffering_size.setter
    def buffering_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(self) -> Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]:
        
        ...
    
    @cloudwatch_logging_options.setter
    def cloudwatch_logging_options(self, value: Optional[pulumi.Input[FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionFormat")
    def compression_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_format.setter
    def compression_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorOutputPrefix")
    def error_output_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_output_prefix.setter
    def error_output_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationS3ConfigurationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FirehoseDeliveryStreamSplunkConfigurationSecretsManagerConfigurationArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StreamStreamModeDetailsArgsDict(TypedDict):
    stream_mode: pulumi.Input[_builtins.str]


@pulumi.input_type
class StreamStreamModeDetailsArgs:
    def __init__(__self__, *, stream_mode: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamMode")
    def stream_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stream_mode.setter
    def stream_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


