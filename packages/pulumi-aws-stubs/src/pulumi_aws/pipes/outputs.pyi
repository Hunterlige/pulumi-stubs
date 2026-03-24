

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PipeEnrichmentParameters', 'PipeEnrichmentParametersHttpParameters', 'PipeLogConfiguration', 'PipeLogConfigurationCloudwatchLogsLogDestination', 'PipeLogConfigurationFirehoseLogDestination', 'PipeLogConfigurationS3LogDestination', 'PipeSourceParameters', 'PipeSourceParametersActivemqBrokerParameters', ..., 'PipeSourceParametersDynamodbStreamParameters', ..., 'PipeSourceParametersFilterCriteria', 'PipeSourceParametersFilterCriteriaFilter', 'PipeSourceParametersKinesisStreamParameters', ..., ..., ..., 'PipeSourceParametersRabbitmqBrokerParameters', ..., 'PipeSourceParametersSelfManagedKafkaParameters', ..., 'PipeSourceParametersSelfManagedKafkaParametersVpc', 'PipeSourceParametersSqsQueueParameters', 'PipeTargetParameters', 'PipeTargetParametersBatchJobParameters', ..., ..., ..., ..., 'PipeTargetParametersBatchJobParametersDependsOn', ..., 'PipeTargetParametersCloudwatchLogsParameters', 'PipeTargetParametersEcsTaskParameters', ..., ..., ..., 'PipeTargetParametersEcsTaskParametersOverrides', ..., ..., ..., ..., ..., ..., ..., ..., 'PipeTargetParametersEventbridgeEventBusParameters', 'PipeTargetParametersHttpParameters', 'PipeTargetParametersKinesisStreamParameters', 'PipeTargetParametersLambdaFunctionParameters', 'PipeTargetParametersRedshiftDataParameters', 'PipeTargetParametersSagemakerPipelineParameters', ..., 'PipeTargetParametersSqsQueueParameters', ...]
@pulumi.output_type
class PipeEnrichmentParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_parameters: Optional[outputs.PipeEnrichmentParametersHttpParameters] = ..., input_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpParameters")
    def http_parameters(self) -> Optional[outputs.PipeEnrichmentParametersHttpParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeEnrichmentParametersHttpParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_parameters: Optional[Mapping[str, _builtins.str]] = ..., path_parameter_values: Optional[_builtins.str] = ..., query_string_parameters: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


@pulumi.output_type
class PipeLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, level: _builtins.str, cloudwatch_logs_log_destination: Optional[outputs.PipeLogConfigurationCloudwatchLogsLogDestination] = ..., firehose_log_destination: Optional[outputs.PipeLogConfigurationFirehoseLogDestination] = ..., include_execution_datas: Optional[Sequence[_builtins.str]] = ..., s3_log_destination: Optional[outputs.PipeLogConfigurationS3LogDestination] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsLogDestination")
    def cloudwatch_logs_log_destination(self) -> Optional[outputs.PipeLogConfigurationCloudwatchLogsLogDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseLogDestination")
    def firehose_log_destination(self) -> Optional[outputs.PipeLogConfigurationFirehoseLogDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeExecutionDatas")
    def include_execution_datas(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3LogDestination")
    def s3_log_destination(self) -> Optional[outputs.PipeLogConfigurationS3LogDestination]:
        
        ...
    


@pulumi.output_type
class PipeLogConfigurationCloudwatchLogsLogDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeLogConfigurationFirehoseLogDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delivery_stream_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryStreamArn")
    def delivery_stream_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeLogConfigurationS3LogDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, bucket_owner: _builtins.str, output_format: Optional[_builtins.str] = ..., prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activemq_broker_parameters: Optional[outputs.PipeSourceParametersActivemqBrokerParameters] = ..., dynamodb_stream_parameters: Optional[outputs.PipeSourceParametersDynamodbStreamParameters] = ..., filter_criteria: Optional[outputs.PipeSourceParametersFilterCriteria] = ..., kinesis_stream_parameters: Optional[outputs.PipeSourceParametersKinesisStreamParameters] = ..., managed_streaming_kafka_parameters: Optional[outputs.PipeSourceParametersManagedStreamingKafkaParameters] = ..., rabbitmq_broker_parameters: Optional[outputs.PipeSourceParametersRabbitmqBrokerParameters] = ..., self_managed_kafka_parameters: Optional[outputs.PipeSourceParametersSelfManagedKafkaParameters] = ..., sqs_queue_parameters: Optional[outputs.PipeSourceParametersSqsQueueParameters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activemqBrokerParameters")
    def activemq_broker_parameters(self) -> Optional[outputs.PipeSourceParametersActivemqBrokerParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamodbStreamParameters")
    def dynamodb_stream_parameters(self) -> Optional[outputs.PipeSourceParametersDynamodbStreamParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> Optional[outputs.PipeSourceParametersFilterCriteria]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamParameters")
    def kinesis_stream_parameters(self) -> Optional[outputs.PipeSourceParametersKinesisStreamParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedStreamingKafkaParameters")
    def managed_streaming_kafka_parameters(self) -> Optional[outputs.PipeSourceParametersManagedStreamingKafkaParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rabbitmqBrokerParameters")
    def rabbitmq_broker_parameters(self) -> Optional[outputs.PipeSourceParametersRabbitmqBrokerParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedKafkaParameters")
    def self_managed_kafka_parameters(self) -> Optional[outputs.PipeSourceParametersSelfManagedKafkaParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsQueueParameters")
    def sqs_queue_parameters(self) -> Optional[outputs.PipeSourceParametersSqsQueueParameters]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersActivemqBrokerParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, credentials: outputs.PipeSourceParametersActivemqBrokerParametersCredentials, queue_name: _builtins.str, batch_size: Optional[_builtins.int] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> outputs.PipeSourceParametersActivemqBrokerParametersCredentials:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersActivemqBrokerParametersCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_auth: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersDynamodbStreamParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, starting_position: _builtins.str, batch_size: Optional[_builtins.int] = ..., dead_letter_config: Optional[outputs.PipeSourceParametersDynamodbStreamParametersDeadLetterConfig] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ..., maximum_record_age_in_seconds: Optional[_builtins.int] = ..., maximum_retry_attempts: Optional[_builtins.int] = ..., on_partial_batch_item_failure: Optional[_builtins.str] = ..., parallelization_factor: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[outputs.PipeSourceParametersDynamodbStreamParametersDeadLetterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPartialBatchItemFailure")
    def on_partial_batch_item_failure(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersDynamodbStreamParametersDeadLetterConfig(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersFilterCriteria(dict):
    def __init__(__self__, *, filters: Optional[Sequence[outputs.PipeSourceParametersFilterCriteriaFilter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.PipeSourceParametersFilterCriteriaFilter]]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersFilterCriteriaFilter(dict):
    def __init__(__self__, *, pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersKinesisStreamParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, starting_position: _builtins.str, batch_size: Optional[_builtins.int] = ..., dead_letter_config: Optional[outputs.PipeSourceParametersKinesisStreamParametersDeadLetterConfig] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ..., maximum_record_age_in_seconds: Optional[_builtins.int] = ..., maximum_retry_attempts: Optional[_builtins.int] = ..., on_partial_batch_item_failure: Optional[_builtins.str] = ..., parallelization_factor: Optional[_builtins.int] = ..., starting_position_timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterConfig")
    def dead_letter_config(self) -> Optional[outputs.PipeSourceParametersKinesisStreamParametersDeadLetterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPartialBatchItemFailure")
    def on_partial_batch_item_failure(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersKinesisStreamParametersDeadLetterConfig(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersManagedStreamingKafkaParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, topic_name: _builtins.str, batch_size: Optional[_builtins.int] = ..., consumer_group_id: Optional[_builtins.str] = ..., credentials: Optional[outputs.PipeSourceParametersManagedStreamingKafkaParametersCredentials] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ..., starting_position: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.PipeSourceParametersManagedStreamingKafkaParametersCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersManagedStreamingKafkaParametersCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_certificate_tls_auth: Optional[_builtins.str] = ..., sasl_scram512_auth: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateTlsAuth")
    def client_certificate_tls_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslScram512Auth")
    def sasl_scram512_auth(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersRabbitmqBrokerParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, credentials: outputs.PipeSourceParametersRabbitmqBrokerParametersCredentials, queue_name: _builtins.str, batch_size: Optional[_builtins.int] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ..., virtual_host: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> outputs.PipeSourceParametersRabbitmqBrokerParametersCredentials:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHost")
    def virtual_host(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersRabbitmqBrokerParametersCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_auth: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersSelfManagedKafkaParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, topic_name: _builtins.str, additional_bootstrap_servers: Optional[Sequence[_builtins.str]] = ..., batch_size: Optional[_builtins.int] = ..., consumer_group_id: Optional[_builtins.str] = ..., credentials: Optional[outputs.PipeSourceParametersSelfManagedKafkaParametersCredentials] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ..., server_root_ca_certificate: Optional[_builtins.str] = ..., starting_position: Optional[_builtins.str] = ..., vpc: Optional[outputs.PipeSourceParametersSelfManagedKafkaParametersVpc] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalBootstrapServers")
    def additional_bootstrap_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.PipeSourceParametersSelfManagedKafkaParametersCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRootCaCertificate")
    def server_root_ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[outputs.PipeSourceParametersSelfManagedKafkaParametersVpc]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersSelfManagedKafkaParametersCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_auth: Optional[_builtins.str] = ..., client_certificate_tls_auth: Optional[_builtins.str] = ..., sasl_scram256_auth: Optional[_builtins.str] = ..., sasl_scram512_auth: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateTlsAuth")
    def client_certificate_tls_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslScram256Auth")
    def sasl_scram256_auth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saslScram512Auth")
    def sasl_scram512_auth(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeSourceParametersSelfManagedKafkaParametersVpc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_groups: Optional[Sequence[_builtins.str]] = ..., subnets: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class PipeSourceParametersSqsQueueParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, batch_size: Optional[_builtins.int] = ..., maximum_batching_window_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeTargetParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, batch_job_parameters: Optional[outputs.PipeTargetParametersBatchJobParameters] = ..., cloudwatch_logs_parameters: Optional[outputs.PipeTargetParametersCloudwatchLogsParameters] = ..., ecs_task_parameters: Optional[outputs.PipeTargetParametersEcsTaskParameters] = ..., eventbridge_event_bus_parameters: Optional[outputs.PipeTargetParametersEventbridgeEventBusParameters] = ..., http_parameters: Optional[outputs.PipeTargetParametersHttpParameters] = ..., input_template: Optional[_builtins.str] = ..., kinesis_stream_parameters: Optional[outputs.PipeTargetParametersKinesisStreamParameters] = ..., lambda_function_parameters: Optional[outputs.PipeTargetParametersLambdaFunctionParameters] = ..., redshift_data_parameters: Optional[outputs.PipeTargetParametersRedshiftDataParameters] = ..., sagemaker_pipeline_parameters: Optional[outputs.PipeTargetParametersSagemakerPipelineParameters] = ..., sqs_queue_parameters: Optional[outputs.PipeTargetParametersSqsQueueParameters] = ..., step_function_state_machine_parameters: Optional[outputs.PipeTargetParametersStepFunctionStateMachineParameters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchJobParameters")
    def batch_job_parameters(self) -> Optional[outputs.PipeTargetParametersBatchJobParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsParameters")
    def cloudwatch_logs_parameters(self) -> Optional[outputs.PipeTargetParametersCloudwatchLogsParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecsTaskParameters")
    def ecs_task_parameters(self) -> Optional[outputs.PipeTargetParametersEcsTaskParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventbridgeEventBusParameters")
    def eventbridge_event_bus_parameters(self) -> Optional[outputs.PipeTargetParametersEventbridgeEventBusParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpParameters")
    def http_parameters(self) -> Optional[outputs.PipeTargetParametersHttpParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamParameters")
    def kinesis_stream_parameters(self) -> Optional[outputs.PipeTargetParametersKinesisStreamParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionParameters")
    def lambda_function_parameters(self) -> Optional[outputs.PipeTargetParametersLambdaFunctionParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftDataParameters")
    def redshift_data_parameters(self) -> Optional[outputs.PipeTargetParametersRedshiftDataParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerPipelineParameters")
    def sagemaker_pipeline_parameters(self) -> Optional[outputs.PipeTargetParametersSagemakerPipelineParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsQueueParameters")
    def sqs_queue_parameters(self) -> Optional[outputs.PipeTargetParametersSqsQueueParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctionStateMachineParameters")
    def step_function_state_machine_parameters(self) -> Optional[outputs.PipeTargetParametersStepFunctionStateMachineParameters]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_definition: _builtins.str, job_name: _builtins.str, array_properties: Optional[outputs.PipeTargetParametersBatchJobParametersArrayProperties] = ..., container_overrides: Optional[outputs.PipeTargetParametersBatchJobParametersContainerOverrides] = ..., depends_ons: Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersDependsOn]] = ..., parameters: Optional[Mapping[str, _builtins.str]] = ..., retry_strategy: Optional[outputs.PipeTargetParametersBatchJobParametersRetryStrategy] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayProperties")
    def array_properties(self) -> Optional[outputs.PipeTargetParametersBatchJobParametersArrayProperties]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(self) -> Optional[outputs.PipeTargetParametersBatchJobParametersContainerOverrides]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(self) -> Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersDependsOn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryStrategy")
    def retry_strategy(self) -> Optional[outputs.PipeTargetParametersBatchJobParametersRetryStrategy]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersArrayProperties(dict):
    def __init__(__self__, *, size: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersContainerOverrides(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Optional[Sequence[_builtins.str]] = ..., environments: Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersContainerOverridesEnvironment]] = ..., instance_type: Optional[_builtins.str] = ..., resource_requirements: Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirement]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environments(self) -> Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersContainerOverridesEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(self) -> Optional[Sequence[outputs.PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirement]]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersContainerOverridesEnvironment(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersContainerOverridesResourceRequirement(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersDependsOn(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersBatchJobParametersRetryStrategy(dict):
    def __init__(__self__, *, attempts: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersCloudwatchLogsParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_stream_name: Optional[_builtins.str] = ..., timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamName")
    def log_stream_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, task_definition_arn: _builtins.str, capacity_provider_strategies: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersCapacityProviderStrategy]] = ..., enable_ecs_managed_tags: Optional[_builtins.bool] = ..., enable_execute_command: Optional[_builtins.bool] = ..., group: Optional[_builtins.str] = ..., launch_type: Optional[_builtins.str] = ..., network_configuration: Optional[outputs.PipeTargetParametersEcsTaskParametersNetworkConfiguration] = ..., overrides: Optional[outputs.PipeTargetParametersEcsTaskParametersOverrides] = ..., placement_constraints: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersPlacementConstraint]] = ..., placement_strategies: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersPlacementStrategy]] = ..., platform_version: Optional[_builtins.str] = ..., propagate_tags: Optional[_builtins.str] = ..., reference_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., task_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersCapacityProviderStrategy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[outputs.PipeTargetParametersEcsTaskParametersNetworkConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[outputs.PipeTargetParametersEcsTaskParametersOverrides]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersPlacementConstraint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersPlacementStrategy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_provider: _builtins.str, base: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_vpc_configuration: Optional[outputs.PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsVpcConfiguration")
    def aws_vpc_configuration(self) -> Optional[outputs.PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfiguration]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersNetworkConfigurationAwsVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assign_public_ip: Optional[_builtins.str] = ..., security_groups: Optional[Sequence[_builtins.str]] = ..., subnets: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverrides(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_overrides: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverride]] = ..., cpu: Optional[_builtins.str] = ..., ephemeral_storage: Optional[outputs.PipeTargetParametersEcsTaskParametersOverridesEphemeralStorage] = ..., execution_role_arn: Optional[_builtins.str] = ..., inference_accelerator_overrides: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverride]] = ..., memory: Optional[_builtins.str] = ..., task_role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[outputs.PipeTargetParametersEcsTaskParametersOverridesEphemeralStorage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceAcceleratorOverrides")
    def inference_accelerator_overrides(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commands: Optional[Sequence[_builtins.str]] = ..., cpu: Optional[_builtins.int] = ..., environment_files: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFile]] = ..., environments: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironment]] = ..., memory: Optional[_builtins.int] = ..., memory_reservation: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ..., resource_requirements: Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirement]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentFiles")
    def environment_files(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environments(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(self) -> Optional[Sequence[outputs.PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirement]]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironment(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideEnvironmentFile(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesContainerOverrideResourceRequirement(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesEphemeralStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, size_in_gib: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersOverridesInferenceAcceleratorOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_name: Optional[_builtins.str] = ..., device_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersPlacementConstraint(dict):
    def __init__(__self__, *, expression: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEcsTaskParametersPlacementStrategy(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersEventbridgeEventBusParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, detail_type: Optional[_builtins.str] = ..., endpoint_id: Optional[_builtins.str] = ..., resources: Optional[Sequence[_builtins.str]] = ..., source: Optional[_builtins.str] = ..., time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersHttpParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_parameters: Optional[Mapping[str, _builtins.str]] = ..., path_parameter_values: Optional[_builtins.str] = ..., query_string_parameters: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


@pulumi.output_type
class PipeTargetParametersKinesisStreamParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, partition_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersLambdaFunctionParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invocation_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersRedshiftDataParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database: _builtins.str, sqls: Sequence[_builtins.str], db_user: Optional[_builtins.str] = ..., secret_manager_arn: Optional[_builtins.str] = ..., statement_name: Optional[_builtins.str] = ..., with_event: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sqls(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerArn")
    def secret_manager_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersSagemakerPipelineParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pipeline_parameters: Optional[Sequence[outputs.PipeTargetParametersSagemakerPipelineParametersPipelineParameter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineParameters")
    def pipeline_parameters(self) -> Optional[Sequence[outputs.PipeTargetParametersSagemakerPipelineParametersPipelineParameter]]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersSagemakerPipelineParametersPipelineParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersSqsQueueParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message_deduplication_id: Optional[_builtins.str] = ..., message_group_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageDeduplicationId")
    def message_deduplication_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipeTargetParametersStepFunctionStateMachineParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invocation_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> _builtins.str:
        
        ...
    


