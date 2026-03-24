import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipeEnrichmentParametersArgs",
    "PipeEnrichmentParametersArgsDict",
    "PipeEnrichmentParametersHttpParametersArgs",
    "PipeEnrichmentParametersHttpParametersArgsDict",
    "PipeLogConfigurationArgs",
    "PipeLogConfigurationArgsDict",
    ...,
    ...,
    "PipeLogConfigurationFirehoseLogDestinationArgs",
    "PipeLogConfigurationFirehoseLogDestinationArgsDict",
    "PipeLogConfigurationS3LogDestinationArgs",
    "PipeLogConfigurationS3LogDestinationArgsDict",
    "PipeSourceParametersArgs",
    "PipeSourceParametersArgsDict",
    "PipeSourceParametersActivemqBrokerParametersArgs",
    ...,
    ...,
    ...,
    "PipeSourceParametersDynamodbStreamParametersArgs",
    ...,
    ...,
    ...,
    "PipeSourceParametersFilterCriteriaArgs",
    "PipeSourceParametersFilterCriteriaArgsDict",
    "PipeSourceParametersFilterCriteriaFilterArgs",
    "PipeSourceParametersFilterCriteriaFilterArgsDict",
    "PipeSourceParametersKinesisStreamParametersArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PipeSourceParametersRabbitmqBrokerParametersArgs",
    ...,
    ...,
    ...,
    "PipeSourceParametersSelfManagedKafkaParametersArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "PipeSourceParametersSqsQueueParametersArgs",
    "PipeSourceParametersSqsQueueParametersArgsDict",
    "PipeTargetParametersArgs",
    "PipeTargetParametersArgsDict",
    "PipeTargetParametersBatchJobParametersArgs",
    "PipeTargetParametersBatchJobParametersArgsDict",
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
    "PipeTargetParametersCloudwatchLogsParametersArgs",
    ...,
    "PipeTargetParametersEcsTaskParametersArgs",
    "PipeTargetParametersEcsTaskParametersArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PipeTargetParametersEcsTaskParametersOverridesArgs",
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
    "PipeTargetParametersHttpParametersArgs",
    "PipeTargetParametersHttpParametersArgsDict",
    "PipeTargetParametersKinesisStreamParametersArgs",
    ...,
    "PipeTargetParametersLambdaFunctionParametersArgs",
    ...,
    "PipeTargetParametersRedshiftDataParametersArgs",
    "PipeTargetParametersRedshiftDataParametersArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PipeTargetParametersSqsQueueParametersArgs",
    "PipeTargetParametersSqsQueueParametersArgsDict",
    ...,
    ...,
]

class PipeEnrichmentParametersArgsDict(TypedDict):
    http_parameters: NotRequired[
        pulumi.Input[PipeEnrichmentParametersHttpParametersArgsDict]
    ]
    input_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeEnrichmentParametersArgs:
    def __init__(
        __self__,
        *,
        http_parameters: Optional[
            pulumi.Input[PipeEnrichmentParametersHttpParametersArgs]
        ] = ...,
        input_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpParameters")
    def http_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeEnrichmentParametersHttpParametersArgs]]: ...
    @http_parameters.setter
    def http_parameters(
        self, value: Optional[pulumi.Input[PipeEnrichmentParametersHttpParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_template.setter
    def input_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeEnrichmentParametersHttpParametersArgsDict(TypedDict):
    header_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    path_parameter_values: NotRequired[pulumi.Input[_builtins.str]]
    query_string_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PipeEnrichmentParametersHttpParametersArgs:
    def __init__(
        __self__,
        *,
        header_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        path_parameter_values: Optional[pulumi.Input[_builtins.str]] = ...,
        query_string_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @header_parameters.setter
    def header_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_parameter_values.setter
    def path_parameter_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @query_string_parameters.setter
    def query_string_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class PipeLogConfigurationArgsDict(TypedDict):
    level: pulumi.Input[_builtins.str]
    cloudwatch_logs_log_destination: NotRequired[
        pulumi.Input[PipeLogConfigurationCloudwatchLogsLogDestinationArgsDict]
    ]
    firehose_log_destination: NotRequired[
        pulumi.Input[PipeLogConfigurationFirehoseLogDestinationArgsDict]
    ]
    include_execution_datas: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    s3_log_destination: NotRequired[
        pulumi.Input[PipeLogConfigurationS3LogDestinationArgsDict]
    ]
    ...

@pulumi.input_type
class PipeLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        level: pulumi.Input[_builtins.str],
        cloudwatch_logs_log_destination: Optional[
            pulumi.Input[PipeLogConfigurationCloudwatchLogsLogDestinationArgs]
        ] = ...,
        firehose_log_destination: Optional[
            pulumi.Input[PipeLogConfigurationFirehoseLogDestinationArgs]
        ] = ...,
        include_execution_datas: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        s3_log_destination: Optional[
            pulumi.Input[PipeLogConfigurationS3LogDestinationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Input[_builtins.str]: ...
    @level.setter
    def level(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsLogDestination")
    def cloudwatch_logs_log_destination(
        self,
    ) -> Optional[
        pulumi.Input[PipeLogConfigurationCloudwatchLogsLogDestinationArgs]
    ]: ...
    @cloudwatch_logs_log_destination.setter
    def cloudwatch_logs_log_destination(
        self,
        value: Optional[
            pulumi.Input[PipeLogConfigurationCloudwatchLogsLogDestinationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firehoseLogDestination")
    def firehose_log_destination(
        self,
    ) -> Optional[pulumi.Input[PipeLogConfigurationFirehoseLogDestinationArgs]]: ...
    @firehose_log_destination.setter
    def firehose_log_destination(
        self,
        value: Optional[pulumi.Input[PipeLogConfigurationFirehoseLogDestinationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeExecutionDatas")
    def include_execution_datas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_execution_datas.setter
    def include_execution_datas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3LogDestination")
    def s3_log_destination(
        self,
    ) -> Optional[pulumi.Input[PipeLogConfigurationS3LogDestinationArgs]]: ...
    @s3_log_destination.setter
    def s3_log_destination(
        self, value: Optional[pulumi.Input[PipeLogConfigurationS3LogDestinationArgs]]
    ): ...

class PipeLogConfigurationCloudwatchLogsLogDestinationArgsDict(TypedDict):
    log_group_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeLogConfigurationCloudwatchLogsLogDestinationArgs:
    def __init__(__self__, *, log_group_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[_builtins.str]): ...

class PipeLogConfigurationFirehoseLogDestinationArgsDict(TypedDict):
    delivery_stream_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeLogConfigurationFirehoseLogDestinationArgs:
    def __init__(
        __self__, *, delivery_stream_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStreamArn")
    def delivery_stream_arn(self) -> pulumi.Input[_builtins.str]: ...
    @delivery_stream_arn.setter
    def delivery_stream_arn(self, value: pulumi.Input[_builtins.str]): ...

class PipeLogConfigurationS3LogDestinationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    bucket_owner: pulumi.Input[_builtins.str]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeLogConfigurationS3LogDestinationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        bucket_owner: pulumi.Input[_builtins.str],
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_owner.setter
    def bucket_owner(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersArgsDict(TypedDict):
    activemq_broker_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersActivemqBrokerParametersArgsDict]
    ]
    dynamodb_stream_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersDynamodbStreamParametersArgsDict]
    ]
    filter_criteria: NotRequired[
        pulumi.Input[PipeSourceParametersFilterCriteriaArgsDict]
    ]
    kinesis_stream_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersKinesisStreamParametersArgsDict]
    ]
    managed_streaming_kafka_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersManagedStreamingKafkaParametersArgsDict]
    ]
    rabbitmq_broker_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersRabbitmqBrokerParametersArgsDict]
    ]
    self_managed_kafka_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersArgsDict]
    ]
    sqs_queue_parameters: NotRequired[
        pulumi.Input[PipeSourceParametersSqsQueueParametersArgsDict]
    ]
    ...

@pulumi.input_type
class PipeSourceParametersArgs:
    def __init__(
        __self__,
        *,
        activemq_broker_parameters: Optional[
            pulumi.Input[PipeSourceParametersActivemqBrokerParametersArgs]
        ] = ...,
        dynamodb_stream_parameters: Optional[
            pulumi.Input[PipeSourceParametersDynamodbStreamParametersArgs]
        ] = ...,
        filter_criteria: Optional[
            pulumi.Input[PipeSourceParametersFilterCriteriaArgs]
        ] = ...,
        kinesis_stream_parameters: Optional[
            pulumi.Input[PipeSourceParametersKinesisStreamParametersArgs]
        ] = ...,
        managed_streaming_kafka_parameters: Optional[
            pulumi.Input[PipeSourceParametersManagedStreamingKafkaParametersArgs]
        ] = ...,
        rabbitmq_broker_parameters: Optional[
            pulumi.Input[PipeSourceParametersRabbitmqBrokerParametersArgs]
        ] = ...,
        self_managed_kafka_parameters: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersArgs]
        ] = ...,
        sqs_queue_parameters: Optional[
            pulumi.Input[PipeSourceParametersSqsQueueParametersArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activemqBrokerParameters")
    def activemq_broker_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersActivemqBrokerParametersArgs]]: ...
    @activemq_broker_parameters.setter
    def activemq_broker_parameters(
        self,
        value: Optional[pulumi.Input[PipeSourceParametersActivemqBrokerParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dynamodbStreamParameters")
    def dynamodb_stream_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersDynamodbStreamParametersArgs]]: ...
    @dynamodb_stream_parameters.setter
    def dynamodb_stream_parameters(
        self,
        value: Optional[pulumi.Input[PipeSourceParametersDynamodbStreamParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersFilterCriteriaArgs]]: ...
    @filter_criteria.setter
    def filter_criteria(
        self, value: Optional[pulumi.Input[PipeSourceParametersFilterCriteriaArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamParameters")
    def kinesis_stream_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersKinesisStreamParametersArgs]]: ...
    @kinesis_stream_parameters.setter
    def kinesis_stream_parameters(
        self,
        value: Optional[pulumi.Input[PipeSourceParametersKinesisStreamParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedStreamingKafkaParameters")
    def managed_streaming_kafka_parameters(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersManagedStreamingKafkaParametersArgs]
    ]: ...
    @managed_streaming_kafka_parameters.setter
    def managed_streaming_kafka_parameters(
        self,
        value: Optional[
            pulumi.Input[PipeSourceParametersManagedStreamingKafkaParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rabbitmqBrokerParameters")
    def rabbitmq_broker_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersRabbitmqBrokerParametersArgs]]: ...
    @rabbitmq_broker_parameters.setter
    def rabbitmq_broker_parameters(
        self,
        value: Optional[pulumi.Input[PipeSourceParametersRabbitmqBrokerParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfManagedKafkaParameters")
    def self_managed_kafka_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersArgs]]: ...
    @self_managed_kafka_parameters.setter
    def self_managed_kafka_parameters(
        self,
        value: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqsQueueParameters")
    def sqs_queue_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeSourceParametersSqsQueueParametersArgs]]: ...
    @sqs_queue_parameters.setter
    def sqs_queue_parameters(
        self, value: Optional[pulumi.Input[PipeSourceParametersSqsQueueParametersArgs]]
    ): ...

class PipeSourceParametersActivemqBrokerParametersArgsDict(TypedDict):
    credentials: pulumi.Input[
        PipeSourceParametersActivemqBrokerParametersCredentialsArgsDict
    ]
    queue_name: pulumi.Input[_builtins.str]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeSourceParametersActivemqBrokerParametersArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[
            PipeSourceParametersActivemqBrokerParametersCredentialsArgs
        ],
        queue_name: pulumi.Input[_builtins.str],
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[PipeSourceParametersActivemqBrokerParametersCredentialsArgs]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            PipeSourceParametersActivemqBrokerParametersCredentialsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> pulumi.Input[_builtins.str]: ...
    @queue_name.setter
    def queue_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class PipeSourceParametersActivemqBrokerParametersCredentialsArgsDict(TypedDict):
    basic_auth: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeSourceParametersActivemqBrokerParametersCredentialsArgs:
    def __init__(__self__, *, basic_auth: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> pulumi.Input[_builtins.str]: ...
    @basic_auth.setter
    def basic_auth(self, value: pulumi.Input[_builtins.str]): ...

class PipeSourceParametersDynamodbStreamParametersArgsDict(TypedDict):
    starting_position: pulumi.Input[_builtins.str]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    dead_letter_config: NotRequired[
        pulumi.Input[
            PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgsDict
        ]
    ]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_record_age_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_attempts: NotRequired[pulumi.Input[_builtins.int]]
    on_partial_batch_item_failure: NotRequired[pulumi.Input[_builtins.str]]
    parallelization_factor: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeSourceParametersDynamodbStreamParametersArgs:
    def __init__(
        __self__,
        *,
        starting_position: pulumi.Input[_builtins.str],
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        dead_letter_config: Optional[
            pulumi.Input[
                PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgs
            ]
        ] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        on_partial_batch_item_failure: Optional[pulumi.Input[_builtins.str]] = ...,
        parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> pulumi.Input[_builtins.str]: ...
    @starting_position.setter
    def starting_position(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgs]
    ]: ...
    @dead_letter_config.setter
    def dead_letter_config(
        self,
        value: Optional[
            pulumi.Input[
                PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_record_age_in_seconds.setter
    def maximum_record_age_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="onPartialBatchItemFailure")
    def on_partial_batch_item_failure(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_partial_batch_item_failure.setter
    def on_partial_batch_item_failure(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallelization_factor.setter
    def parallelization_factor(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersDynamodbStreamParametersDeadLetterConfigArgs:
    def __init__(
        __self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersFilterCriteriaArgsDict(TypedDict):
    filters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipeSourceParametersFilterCriteriaFilterArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PipeSourceParametersFilterCriteriaArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipeSourceParametersFilterCriteriaFilterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipeSourceParametersFilterCriteriaFilterArgs]]
        ]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipeSourceParametersFilterCriteriaFilterArgs]]
            ]
        ],
    ): ...

class PipeSourceParametersFilterCriteriaFilterArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeSourceParametersFilterCriteriaFilterArgs:
    def __init__(__self__, *, pattern: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...

class PipeSourceParametersKinesisStreamParametersArgsDict(TypedDict):
    starting_position: pulumi.Input[_builtins.str]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    dead_letter_config: NotRequired[
        pulumi.Input[
            PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgsDict
        ]
    ]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_record_age_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_attempts: NotRequired[pulumi.Input[_builtins.int]]
    on_partial_batch_item_failure: NotRequired[pulumi.Input[_builtins.str]]
    parallelization_factor: NotRequired[pulumi.Input[_builtins.int]]
    starting_position_timestamp: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersKinesisStreamParametersArgs:
    def __init__(
        __self__,
        *,
        starting_position: pulumi.Input[_builtins.str],
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        dead_letter_config: Optional[
            pulumi.Input[
                PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgs
            ]
        ] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        on_partial_batch_item_failure: Optional[pulumi.Input[_builtins.str]] = ...,
        parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ...,
        starting_position_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> pulumi.Input[_builtins.str]: ...
    @starting_position.setter
    def starting_position(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgs]
    ]: ...
    @dead_letter_config.setter
    def dead_letter_config(
        self,
        value: Optional[
            pulumi.Input[
                PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_record_age_in_seconds.setter
    def maximum_record_age_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="onPartialBatchItemFailure")
    def on_partial_batch_item_failure(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_partial_batch_item_failure.setter
    def on_partial_batch_item_failure(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallelization_factor.setter
    def parallelization_factor(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @starting_position_timestamp.setter
    def starting_position_timestamp(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersKinesisStreamParametersDeadLetterConfigArgs:
    def __init__(
        __self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersManagedStreamingKafkaParametersArgsDict(TypedDict):
    topic_name: pulumi.Input[_builtins.str]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    consumer_group_id: NotRequired[pulumi.Input[_builtins.str]]
    credentials: NotRequired[
        pulumi.Input[
            PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgsDict
        ]
    ]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    starting_position: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersManagedStreamingKafkaParametersArgs:
    def __init__(
        __self__,
        *,
        topic_name: pulumi.Input[_builtins.str],
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        consumer_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[
            pulumi.Input[
                PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgs
            ]
        ] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        starting_position: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]: ...
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group_id.setter
    def consumer_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgs]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: Optional[
            pulumi.Input[
                PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgsDict(TypedDict):
    client_certificate_tls_auth: NotRequired[pulumi.Input[_builtins.str]]
    sasl_scram512_auth: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersManagedStreamingKafkaParametersCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_certificate_tls_auth: Optional[pulumi.Input[_builtins.str]] = ...,
        sasl_scram512_auth: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateTlsAuth")
    def client_certificate_tls_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate_tls_auth.setter
    def client_certificate_tls_auth(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="saslScram512Auth")
    def sasl_scram512_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_scram512_auth.setter
    def sasl_scram512_auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersRabbitmqBrokerParametersArgsDict(TypedDict):
    credentials: pulumi.Input[
        PipeSourceParametersRabbitmqBrokerParametersCredentialsArgsDict
    ]
    queue_name: pulumi.Input[_builtins.str]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    virtual_host: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersRabbitmqBrokerParametersArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[
            PipeSourceParametersRabbitmqBrokerParametersCredentialsArgs
        ],
        queue_name: pulumi.Input[_builtins.str],
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        virtual_host: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[PipeSourceParametersRabbitmqBrokerParametersCredentialsArgs]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            PipeSourceParametersRabbitmqBrokerParametersCredentialsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> pulumi.Input[_builtins.str]: ...
    @queue_name.setter
    def queue_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualHost")
    def virtual_host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_host.setter
    def virtual_host(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersRabbitmqBrokerParametersCredentialsArgsDict(TypedDict):
    basic_auth: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeSourceParametersRabbitmqBrokerParametersCredentialsArgs:
    def __init__(__self__, *, basic_auth: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> pulumi.Input[_builtins.str]: ...
    @basic_auth.setter
    def basic_auth(self, value: pulumi.Input[_builtins.str]): ...

class PipeSourceParametersSelfManagedKafkaParametersArgsDict(TypedDict):
    topic_name: pulumi.Input[_builtins.str]
    additional_bootstrap_servers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    consumer_group_id: NotRequired[pulumi.Input[_builtins.str]]
    credentials: NotRequired[
        pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersCredentialsArgsDict]
    ]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    server_root_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    starting_position: NotRequired[pulumi.Input[_builtins.str]]
    vpc: NotRequired[
        pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersVpcArgsDict]
    ]
    ...

@pulumi.input_type
class PipeSourceParametersSelfManagedKafkaParametersArgs:
    def __init__(
        __self__,
        *,
        topic_name: pulumi.Input[_builtins.str],
        additional_bootstrap_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        consumer_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersCredentialsArgs]
        ] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        server_root_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        starting_position: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersVpcArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]: ...
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalBootstrapServers")
    def additional_bootstrap_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_bootstrap_servers.setter
    def additional_bootstrap_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group_id.setter
    def consumer_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersCredentialsArgs]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverRootCaCertificate")
    def server_root_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_root_ca_certificate.setter
    def server_root_ca_certificate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def vpc(
        self,
    ) -> Optional[
        pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersVpcArgs]
    ]: ...
    @vpc.setter
    def vpc(
        self,
        value: Optional[
            pulumi.Input[PipeSourceParametersSelfManagedKafkaParametersVpcArgs]
        ],
    ): ...

class PipeSourceParametersSelfManagedKafkaParametersCredentialsArgsDict(TypedDict):
    basic_auth: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate_tls_auth: NotRequired[pulumi.Input[_builtins.str]]
    sasl_scram256_auth: NotRequired[pulumi.Input[_builtins.str]]
    sasl_scram512_auth: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeSourceParametersSelfManagedKafkaParametersCredentialsArgs:
    def __init__(
        __self__,
        *,
        basic_auth: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate_tls_auth: Optional[pulumi.Input[_builtins.str]] = ...,
        sasl_scram256_auth: Optional[pulumi.Input[_builtins.str]] = ...,
        sasl_scram512_auth: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateTlsAuth")
    def client_certificate_tls_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate_tls_auth.setter
    def client_certificate_tls_auth(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="saslScram256Auth")
    def sasl_scram256_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_scram256_auth.setter
    def sasl_scram256_auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="saslScram512Auth")
    def sasl_scram512_auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sasl_scram512_auth.setter
    def sasl_scram512_auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeSourceParametersSelfManagedKafkaParametersVpcArgsDict(TypedDict):
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipeSourceParametersSelfManagedKafkaParametersVpcArgs:
    def __init__(
        __self__,
        *,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnets.setter
    def subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipeSourceParametersSqsQueueParametersArgsDict(TypedDict):
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    maximum_batching_window_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeSourceParametersSqsQueueParametersArgs:
    def __init__(
        __self__,
        *,
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class PipeTargetParametersArgsDict(TypedDict):
    batch_job_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersBatchJobParametersArgsDict]
    ]
    cloudwatch_logs_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersCloudwatchLogsParametersArgsDict]
    ]
    ecs_task_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersEcsTaskParametersArgsDict]
    ]
    eventbridge_event_bus_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersEventbridgeEventBusParametersArgsDict]
    ]
    http_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersHttpParametersArgsDict]
    ]
    input_template: NotRequired[pulumi.Input[_builtins.str]]
    kinesis_stream_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersKinesisStreamParametersArgsDict]
    ]
    lambda_function_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersLambdaFunctionParametersArgsDict]
    ]
    redshift_data_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersRedshiftDataParametersArgsDict]
    ]
    sagemaker_pipeline_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersSagemakerPipelineParametersArgsDict]
    ]
    sqs_queue_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersSqsQueueParametersArgsDict]
    ]
    step_function_state_machine_parameters: NotRequired[
        pulumi.Input[PipeTargetParametersStepFunctionStateMachineParametersArgsDict]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersArgs:
    def __init__(
        __self__,
        *,
        batch_job_parameters: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersArgs]
        ] = ...,
        cloudwatch_logs_parameters: Optional[
            pulumi.Input[PipeTargetParametersCloudwatchLogsParametersArgs]
        ] = ...,
        ecs_task_parameters: Optional[
            pulumi.Input[PipeTargetParametersEcsTaskParametersArgs]
        ] = ...,
        eventbridge_event_bus_parameters: Optional[
            pulumi.Input[PipeTargetParametersEventbridgeEventBusParametersArgs]
        ] = ...,
        http_parameters: Optional[
            pulumi.Input[PipeTargetParametersHttpParametersArgs]
        ] = ...,
        input_template: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesis_stream_parameters: Optional[
            pulumi.Input[PipeTargetParametersKinesisStreamParametersArgs]
        ] = ...,
        lambda_function_parameters: Optional[
            pulumi.Input[PipeTargetParametersLambdaFunctionParametersArgs]
        ] = ...,
        redshift_data_parameters: Optional[
            pulumi.Input[PipeTargetParametersRedshiftDataParametersArgs]
        ] = ...,
        sagemaker_pipeline_parameters: Optional[
            pulumi.Input[PipeTargetParametersSagemakerPipelineParametersArgs]
        ] = ...,
        sqs_queue_parameters: Optional[
            pulumi.Input[PipeTargetParametersSqsQueueParametersArgs]
        ] = ...,
        step_function_state_machine_parameters: Optional[
            pulumi.Input[PipeTargetParametersStepFunctionStateMachineParametersArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchJobParameters")
    def batch_job_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersBatchJobParametersArgs]]: ...
    @batch_job_parameters.setter
    def batch_job_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersBatchJobParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsParameters")
    def cloudwatch_logs_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersCloudwatchLogsParametersArgs]]: ...
    @cloudwatch_logs_parameters.setter
    def cloudwatch_logs_parameters(
        self,
        value: Optional[pulumi.Input[PipeTargetParametersCloudwatchLogsParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecsTaskParameters")
    def ecs_task_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersEcsTaskParametersArgs]]: ...
    @ecs_task_parameters.setter
    def ecs_task_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersEcsTaskParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventbridgeEventBusParameters")
    def eventbridge_event_bus_parameters(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersEventbridgeEventBusParametersArgs]
    ]: ...
    @eventbridge_event_bus_parameters.setter
    def eventbridge_event_bus_parameters(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersEventbridgeEventBusParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpParameters")
    def http_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersHttpParametersArgs]]: ...
    @http_parameters.setter
    def http_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersHttpParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_template.setter
    def input_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamParameters")
    def kinesis_stream_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersKinesisStreamParametersArgs]]: ...
    @kinesis_stream_parameters.setter
    def kinesis_stream_parameters(
        self,
        value: Optional[pulumi.Input[PipeTargetParametersKinesisStreamParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionParameters")
    def lambda_function_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersLambdaFunctionParametersArgs]]: ...
    @lambda_function_parameters.setter
    def lambda_function_parameters(
        self,
        value: Optional[pulumi.Input[PipeTargetParametersLambdaFunctionParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftDataParameters")
    def redshift_data_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersRedshiftDataParametersArgs]]: ...
    @redshift_data_parameters.setter
    def redshift_data_parameters(
        self,
        value: Optional[pulumi.Input[PipeTargetParametersRedshiftDataParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineParameters")
    def sagemaker_pipeline_parameters(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersSagemakerPipelineParametersArgs]
    ]: ...
    @sagemaker_pipeline_parameters.setter
    def sagemaker_pipeline_parameters(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersSagemakerPipelineParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqsQueueParameters")
    def sqs_queue_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersSqsQueueParametersArgs]]: ...
    @sqs_queue_parameters.setter
    def sqs_queue_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersSqsQueueParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stepFunctionStateMachineParameters")
    def step_function_state_machine_parameters(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersStepFunctionStateMachineParametersArgs]
    ]: ...
    @step_function_state_machine_parameters.setter
    def step_function_state_machine_parameters(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersStepFunctionStateMachineParametersArgs]
        ],
    ): ...

class PipeTargetParametersBatchJobParametersArgsDict(TypedDict):
    job_definition: pulumi.Input[_builtins.str]
    job_name: pulumi.Input[_builtins.str]
    array_properties: NotRequired[
        pulumi.Input[PipeTargetParametersBatchJobParametersArrayPropertiesArgsDict]
    ]
    container_overrides: NotRequired[
        pulumi.Input[PipeTargetParametersBatchJobParametersContainerOverridesArgsDict]
    ]
    depends_ons: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipeTargetParametersBatchJobParametersDependsOnArgsDict]
            ]
        ]
    ]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    retry_strategy: NotRequired[
        pulumi.Input[PipeTargetParametersBatchJobParametersRetryStrategyArgsDict]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersArgs:
    def __init__(
        __self__,
        *,
        job_definition: pulumi.Input[_builtins.str],
        job_name: pulumi.Input[_builtins.str],
        array_properties: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersArrayPropertiesArgs]
        ] = ...,
        container_overrides: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersContainerOverridesArgs]
        ] = ...,
        depends_ons: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipeTargetParametersBatchJobParametersDependsOnArgs]
                ]
            ]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_strategy: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersRetryStrategyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> pulumi.Input[_builtins.str]: ...
    @job_definition.setter
    def job_definition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arrayProperties")
    def array_properties(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersBatchJobParametersArrayPropertiesArgs]
    ]: ...
    @array_properties.setter
    def array_properties(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersArrayPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersBatchJobParametersContainerOverridesArgs]
    ]: ...
    @container_overrides.setter
    def container_overrides(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersContainerOverridesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipeTargetParametersBatchJobParametersDependsOnArgs]]
        ]
    ]: ...
    @depends_ons.setter
    def depends_ons(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipeTargetParametersBatchJobParametersDependsOnArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersBatchJobParametersRetryStrategyArgs]
    ]: ...
    @retry_strategy.setter
    def retry_strategy(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersBatchJobParametersRetryStrategyArgs]
        ],
    ): ...

class PipeTargetParametersBatchJobParametersArrayPropertiesArgsDict(TypedDict):
    size: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersArrayPropertiesArgs:
    def __init__(
        __self__, *, size: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipeTargetParametersBatchJobParametersContainerOverridesArgsDict(TypedDict):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    environments: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgsDict
                ]
            ]
        ]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_requirements: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersContainerOverridesArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        environments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgs
                    ]
                ]
            ]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_requirements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgs
                ]
            ]
        ]
    ]: ...
    @environments.setter
    def environments(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgs
                ]
            ]
        ]
    ]: ...
    @resource_requirements.setter
    def resource_requirements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgs
                    ]
                ]
            ]
        ],
    ): ...

class PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersContainerOverridesEnvironmentArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirementArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersBatchJobParametersDependsOnArgsDict(TypedDict):
    job_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersDependsOnArgs:
    def __init__(
        __self__,
        *,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersBatchJobParametersRetryStrategyArgsDict(TypedDict):
    attempts: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeTargetParametersBatchJobParametersRetryStrategyArgs:
    def __init__(
        __self__, *, attempts: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @attempts.setter
    def attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipeTargetParametersCloudwatchLogsParametersArgsDict(TypedDict):
    log_stream_name: NotRequired[pulumi.Input[_builtins.str]]
    timestamp: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersCloudwatchLogsParametersArgs:
    def __init__(
        __self__,
        *,
        log_stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_stream_name.setter
    def log_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp.setter
    def timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEcsTaskParametersArgsDict(TypedDict):
    task_definition_arn: pulumi.Input[_builtins.str]
    capacity_provider_strategies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgsDict
                ]
            ]
        ]
    ]
    enable_ecs_managed_tags: NotRequired[pulumi.Input[_builtins.bool]]
    enable_execute_command: NotRequired[pulumi.Input[_builtins.bool]]
    group: NotRequired[pulumi.Input[_builtins.str]]
    launch_type: NotRequired[pulumi.Input[_builtins.str]]
    network_configuration: NotRequired[
        pulumi.Input[PipeTargetParametersEcsTaskParametersNetworkConfigurationArgsDict]
    ]
    overrides: NotRequired[
        pulumi.Input[PipeTargetParametersEcsTaskParametersOverridesArgsDict]
    ]
    placement_constraints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersPlacementConstraintArgsDict
                ]
            ]
        ]
    ]
    placement_strategies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersPlacementStrategyArgsDict
                ]
            ]
        ]
    ]
    platform_version: NotRequired[pulumi.Input[_builtins.str]]
    propagate_tags: NotRequired[pulumi.Input[_builtins.str]]
    reference_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    task_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersArgs:
    def __init__(
        __self__,
        *,
        task_definition_arn: pulumi.Input[_builtins.str],
        capacity_provider_strategies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgs
                    ]
                ]
            ]
        ] = ...,
        enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_type: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[PipeTargetParametersEcsTaskParametersNetworkConfigurationArgs]
        ] = ...,
        overrides: Optional[
            pulumi.Input[PipeTargetParametersEcsTaskParametersOverridesArgs]
        ] = ...,
        placement_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersPlacementConstraintArgs
                    ]
                ]
            ]
        ] = ...,
        placement_strategies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersPlacementStrategyArgs
                    ]
                ]
            ]
        ] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        propagate_tags: Optional[pulumi.Input[_builtins.str]] = ...,
        reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        task_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Input[_builtins.str]: ...
    @task_definition_arn.setter
    def task_definition_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgs
                ]
            ]
        ]
    ]: ...
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersEcsTaskParametersNetworkConfigurationArgs]
    ]: ...
    @network_configuration.setter
    def network_configuration(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersEcsTaskParametersNetworkConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> Optional[pulumi.Input[PipeTargetParametersEcsTaskParametersOverridesArgs]]: ...
    @overrides.setter
    def overrides(
        self,
        value: Optional[
            pulumi.Input[PipeTargetParametersEcsTaskParametersOverridesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersPlacementConstraintArgs
                ]
            ]
        ]
    ]: ...
    @placement_constraints.setter
    def placement_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersPlacementConstraintArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipeTargetParametersEcsTaskParametersPlacementStrategyArgs]
            ]
        ]
    ]: ...
    @placement_strategies.setter
    def placement_strategies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersPlacementStrategyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    base: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: pulumi.Input[_builtins.str],
        base: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipeTargetParametersEcsTaskParametersNetworkConfigurationArgsDict(TypedDict):
    aws_vpc_configuration: NotRequired[
        pulumi.Input[
            PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        aws_vpc_configuration: Optional[
            pulumi.Input[
                PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsVpcConfiguration")
    def aws_vpc_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgs
        ]
    ]: ...
    @aws_vpc_configuration.setter
    def aws_vpc_configuration(
        self,
        value: Optional[
            pulumi.Input[
                PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgs
            ]
        ],
    ): ...

class PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgsDict(
    TypedDict
):
    assign_public_ip: NotRequired[pulumi.Input[_builtins.str]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfigurationArgs:
    def __init__(
        __self__,
        *,
        assign_public_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnets.setter
    def subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipeTargetParametersEcsTaskParametersOverridesArgsDict(TypedDict):
    container_overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgsDict
                ]
            ]
        ]
    ]
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    ephemeral_storage: NotRequired[
        pulumi.Input[
            PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgsDict
        ]
    ]
    execution_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    inference_accelerator_overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgsDict
                ]
            ]
        ]
    ]
    memory: NotRequired[pulumi.Input[_builtins.str]]
    task_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesArgs:
    def __init__(
        __self__,
        *,
        container_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgs
                    ]
                ]
            ]
        ] = ...,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        ephemeral_storage: Optional[
            pulumi.Input[
                PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgs
            ]
        ] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        inference_accelerator_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgs
                    ]
                ]
            ]
        ] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
        task_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgs
                ]
            ]
        ]
    ]: ...
    @container_overrides.setter
    def container_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(
        self,
    ) -> Optional[
        pulumi.Input[PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgs]
    ]: ...
    @ephemeral_storage.setter
    def ephemeral_storage(
        self,
        value: Optional[
            pulumi.Input[
                PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inferenceAcceleratorOverrides")
    def inference_accelerator_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgs
                ]
            ]
        ]
    ]: ...
    @inference_accelerator_overrides.setter
    def inference_accelerator_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgsDict(
    TypedDict
):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cpu: NotRequired[pulumi.Input[_builtins.int]]
    environment_files: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgsDict
                ]
            ]
        ]
    ]
    environments: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgsDict
                ]
            ]
        ]
    ]
    memory: NotRequired[pulumi.Input[_builtins.int]]
    memory_reservation: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resource_requirements: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        cpu: Optional[pulumi.Input[_builtins.int]] = ...,
        environment_files: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgs
                    ]
                ]
            ]
        ] = ...,
        environments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgs
                    ]
                ]
            ]
        ] = ...,
        memory: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_reservation: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_requirements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentFiles")
    def environment_files(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgs
                ]
            ]
        ]
    ]: ...
    @environment_files.setter
    def environment_files(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgs
                ]
            ]
        ]
    ]: ...
    @environments.setter
    def environments(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_reservation.setter
    def memory_reservation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgs
                ]
            ]
        ]
    ]: ...
    @resource_requirements.setter
    def resource_requirements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgs
                    ]
                ]
            ]
        ],
    ): ...

class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFileArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirementArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgsDict(TypedDict):
    size_in_gib: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesEphemeralStorageArgs:
    def __init__(__self__, *, size_in_gib: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> pulumi.Input[_builtins.int]: ...
    @size_in_gib.setter
    def size_in_gib(self, value: pulumi.Input[_builtins.int]): ...

class PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgsDict(
    TypedDict
):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    device_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverrideArgs:
    def __init__(
        __self__,
        *,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        device_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_type.setter
    def device_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEcsTaskParametersPlacementConstraintArgsDict(TypedDict):
    expression: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersPlacementConstraintArgs:
    def __init__(
        __self__,
        *,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEcsTaskParametersPlacementStrategyArgsDict(TypedDict):
    field: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEcsTaskParametersPlacementStrategyArgs:
    def __init__(
        __self__,
        *,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersEventbridgeEventBusParametersArgsDict(TypedDict):
    detail_type: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersEventbridgeEventBusParametersArgs:
    def __init__(
        __self__,
        *,
        detail_type: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detail_type.setter
    def detail_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time.setter
    def time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersHttpParametersArgsDict(TypedDict):
    header_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    path_parameter_values: NotRequired[pulumi.Input[_builtins.str]]
    query_string_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersHttpParametersArgs:
    def __init__(
        __self__,
        *,
        header_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        path_parameter_values: Optional[pulumi.Input[_builtins.str]] = ...,
        query_string_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @header_parameters.setter
    def header_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_parameter_values.setter
    def path_parameter_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @query_string_parameters.setter
    def query_string_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class PipeTargetParametersKinesisStreamParametersArgsDict(TypedDict):
    partition_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersKinesisStreamParametersArgs:
    def __init__(__self__, *, partition_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> pulumi.Input[_builtins.str]: ...
    @partition_key.setter
    def partition_key(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersLambdaFunctionParametersArgsDict(TypedDict):
    invocation_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersLambdaFunctionParametersArgs:
    def __init__(__self__, *, invocation_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> pulumi.Input[_builtins.str]: ...
    @invocation_type.setter
    def invocation_type(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersRedshiftDataParametersArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    sqls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    db_user: NotRequired[pulumi.Input[_builtins.str]]
    secret_manager_arn: NotRequired[pulumi.Input[_builtins.str]]
    statement_name: NotRequired[pulumi.Input[_builtins.str]]
    with_event: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PipeTargetParametersRedshiftDataParametersArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        sqls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        db_user: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_name: Optional[pulumi.Input[_builtins.str]] = ...,
        with_event: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sqls(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @sqls.setter
    def sqls(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_user.setter
    def db_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerArn")
    def secret_manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_arn.setter
    def secret_manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_name.setter
    def statement_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @with_event.setter
    def with_event(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PipeTargetParametersSagemakerPipelineParametersArgsDict(TypedDict):
    pipeline_parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PipeTargetParametersSagemakerPipelineParametersArgs:
    def __init__(
        __self__,
        *,
        pipeline_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineParameters")
    def pipeline_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgs
                ]
            ]
        ]
    ]: ...
    @pipeline_parameters.setter
    def pipeline_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgs
                    ]
                ]
            ]
        ],
    ): ...

class PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersSagemakerPipelineParametersPipelineParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class PipeTargetParametersSqsQueueParametersArgsDict(TypedDict):
    message_deduplication_id: NotRequired[pulumi.Input[_builtins.str]]
    message_group_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipeTargetParametersSqsQueueParametersArgs:
    def __init__(
        __self__,
        *,
        message_deduplication_id: Optional[pulumi.Input[_builtins.str]] = ...,
        message_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageDeduplicationId")
    def message_deduplication_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_deduplication_id.setter
    def message_deduplication_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_group_id.setter
    def message_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipeTargetParametersStepFunctionStateMachineParametersArgsDict(TypedDict):
    invocation_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipeTargetParametersStepFunctionStateMachineParametersArgs:
    def __init__(__self__, *, invocation_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> pulumi.Input[_builtins.str]: ...
    @invocation_type.setter
    def invocation_type(self, value: pulumi.Input[_builtins.str]): ...
