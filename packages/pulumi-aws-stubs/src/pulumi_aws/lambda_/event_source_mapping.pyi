

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EventSourceMappingArgs', 'EventSourceMapping']
@pulumi.input_type
class EventSourceMappingArgs:
    def __init__(__self__, *, function_name: pulumi.Input[_builtins.str], amazon_managed_kafka_event_source_config: Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]] = ..., batch_size: Optional[pulumi.Input[_builtins.int]] = ..., bisect_batch_on_function_error: Optional[pulumi.Input[_builtins.bool]] = ..., destination_config: Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]] = ..., document_db_event_source_config: Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_source_arn: Optional[pulumi.Input[_builtins.str]] = ..., filter_criteria: Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]] = ..., function_response_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., metrics_config: Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]] = ..., parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_poller_config: Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]] = ..., queues: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]] = ..., self_managed_event_source: Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]] = ..., self_managed_kafka_event_source_config: Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]] = ..., source_access_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]] = ..., starting_position: Optional[pulumi.Input[_builtins.str]] = ..., starting_position_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tumbling_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonManagedKafkaEventSourceConfig")
    def amazon_managed_kafka_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]]:
        
        ...
    
    @amazon_managed_kafka_event_source_config.setter
    def amazon_managed_kafka_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bisectBatchOnFunctionError")
    def bisect_batch_on_function_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bisect_batch_on_function_error.setter
    def bisect_batch_on_function_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]]:
        
        ...
    
    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentDbEventSourceConfig")
    def document_db_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]]:
        
        ...
    
    @document_db_event_source_config.setter
    def document_db_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceArn")
    def event_source_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_source_arn.setter
    def event_source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]]:
        
        ...
    
    @filter_criteria.setter
    def filter_criteria(self, value: Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionResponseTypes")
    def function_response_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @function_response_types.setter
    def function_response_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_record_age_in_seconds.setter
    def maximum_record_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsConfig")
    def metrics_config(self) -> Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]]:
        
        ...
    
    @metrics_config.setter
    def metrics_config(self, value: Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelization_factor.setter
    def parallelization_factor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedPollerConfig")
    def provisioned_poller_config(self) -> Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]]:
        
        ...
    
    @provisioned_poller_config.setter
    def provisioned_poller_config(self, value: Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def queues(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queues.setter
    def queues(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]]:
        
        ...
    
    @scaling_config.setter
    def scaling_config(self, value: Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedEventSource")
    def self_managed_event_source(self) -> Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]]:
        
        ...
    
    @self_managed_event_source.setter
    def self_managed_event_source(self, value: Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedKafkaEventSourceConfig")
    def self_managed_kafka_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]]:
        
        ...
    
    @self_managed_kafka_event_source_config.setter
    def self_managed_kafka_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccessConfigurations")
    def source_access_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]]:
        
        ...
    
    @source_access_configurations.setter
    def source_access_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starting_position_timestamp.setter
    def starting_position_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @topics.setter
    def topics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tumblingWindowInSeconds")
    def tumbling_window_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tumbling_window_in_seconds.setter
    def tumbling_window_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _EventSourceMappingState:
    def __init__(__self__, *, amazon_managed_kafka_event_source_config: Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., batch_size: Optional[pulumi.Input[_builtins.int]] = ..., bisect_batch_on_function_error: Optional[pulumi.Input[_builtins.bool]] = ..., destination_config: Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]] = ..., document_db_event_source_config: Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_source_arn: Optional[pulumi.Input[_builtins.str]] = ..., filter_criteria: Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]] = ..., function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_response_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., last_processing_result: Optional[pulumi.Input[_builtins.str]] = ..., maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., metrics_config: Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]] = ..., parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_poller_config: Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]] = ..., queues: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]] = ..., self_managed_event_source: Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]] = ..., self_managed_kafka_event_source_config: Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]] = ..., source_access_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]] = ..., starting_position: Optional[pulumi.Input[_builtins.str]] = ..., starting_position_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_transition_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tumbling_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., uuid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonManagedKafkaEventSourceConfig")
    def amazon_managed_kafka_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]]:
        
        ...
    
    @amazon_managed_kafka_event_source_config.setter
    def amazon_managed_kafka_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bisectBatchOnFunctionError")
    def bisect_batch_on_function_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bisect_batch_on_function_error.setter
    def bisect_batch_on_function_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]]:
        
        ...
    
    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input[EventSourceMappingDestinationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentDbEventSourceConfig")
    def document_db_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]]:
        
        ...
    
    @document_db_event_source_config.setter
    def document_db_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingDocumentDbEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceArn")
    def event_source_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_source_arn.setter
    def event_source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]]:
        
        ...
    
    @filter_criteria.setter
    def filter_criteria(self, value: Optional[pulumi.Input[EventSourceMappingFilterCriteriaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionResponseTypes")
    def function_response_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @function_response_types.setter
    def function_response_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastProcessingResult")
    def last_processing_result(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_processing_result.setter
    def last_processing_result(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_batching_window_in_seconds.setter
    def maximum_batching_window_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_record_age_in_seconds.setter
    def maximum_record_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsConfig")
    def metrics_config(self) -> Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]]:
        
        ...
    
    @metrics_config.setter
    def metrics_config(self, value: Optional[pulumi.Input[EventSourceMappingMetricsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelization_factor.setter
    def parallelization_factor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedPollerConfig")
    def provisioned_poller_config(self) -> Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]]:
        
        ...
    
    @provisioned_poller_config.setter
    def provisioned_poller_config(self, value: Optional[pulumi.Input[EventSourceMappingProvisionedPollerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def queues(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queues.setter
    def queues(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]]:
        
        ...
    
    @scaling_config.setter
    def scaling_config(self, value: Optional[pulumi.Input[EventSourceMappingScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedEventSource")
    def self_managed_event_source(self) -> Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]]:
        
        ...
    
    @self_managed_event_source.setter
    def self_managed_event_source(self, value: Optional[pulumi.Input[EventSourceMappingSelfManagedEventSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedKafkaEventSourceConfig")
    def self_managed_kafka_event_source_config(self) -> Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]]:
        
        ...
    
    @self_managed_kafka_event_source_config.setter
    def self_managed_kafka_event_source_config(self, value: Optional[pulumi.Input[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccessConfigurations")
    def source_access_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]]:
        
        ...
    
    @source_access_configurations.setter
    def source_access_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventSourceMappingSourceAccessConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starting_position.setter
    def starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starting_position_timestamp.setter
    def starting_position_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateTransitionReason")
    def state_transition_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_transition_reason.setter
    def state_transition_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @topics.setter
    def topics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tumblingWindowInSeconds")
    def tumbling_window_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tumbling_window_in_seconds.setter
    def tumbling_window_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/eventSourceMapping:EventSourceMapping")
class EventSourceMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., amazon_managed_kafka_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs, EventSourceMappingAmazonManagedKafkaEventSourceConfigArgsDict]]] = ..., batch_size: Optional[pulumi.Input[_builtins.int]] = ..., bisect_batch_on_function_error: Optional[pulumi.Input[_builtins.bool]] = ..., destination_config: Optional[pulumi.Input[Union[EventSourceMappingDestinationConfigArgs, EventSourceMappingDestinationConfigArgsDict]]] = ..., document_db_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingDocumentDbEventSourceConfigArgs, EventSourceMappingDocumentDbEventSourceConfigArgsDict]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_source_arn: Optional[pulumi.Input[_builtins.str]] = ..., filter_criteria: Optional[pulumi.Input[Union[EventSourceMappingFilterCriteriaArgs, EventSourceMappingFilterCriteriaArgsDict]]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_response_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., metrics_config: Optional[pulumi.Input[Union[EventSourceMappingMetricsConfigArgs, EventSourceMappingMetricsConfigArgsDict]]] = ..., parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_poller_config: Optional[pulumi.Input[Union[EventSourceMappingProvisionedPollerConfigArgs, EventSourceMappingProvisionedPollerConfigArgsDict]]] = ..., queues: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[Union[EventSourceMappingScalingConfigArgs, EventSourceMappingScalingConfigArgsDict]]] = ..., self_managed_event_source: Optional[pulumi.Input[Union[EventSourceMappingSelfManagedEventSourceArgs, EventSourceMappingSelfManagedEventSourceArgsDict]]] = ..., self_managed_kafka_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs, EventSourceMappingSelfManagedKafkaEventSourceConfigArgsDict]]] = ..., source_access_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventSourceMappingSourceAccessConfigurationArgs, EventSourceMappingSourceAccessConfigurationArgsDict]]]]] = ..., starting_position: Optional[pulumi.Input[_builtins.str]] = ..., starting_position_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tumbling_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventSourceMappingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., amazon_managed_kafka_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs, EventSourceMappingAmazonManagedKafkaEventSourceConfigArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., batch_size: Optional[pulumi.Input[_builtins.int]] = ..., bisect_batch_on_function_error: Optional[pulumi.Input[_builtins.bool]] = ..., destination_config: Optional[pulumi.Input[Union[EventSourceMappingDestinationConfigArgs, EventSourceMappingDestinationConfigArgsDict]]] = ..., document_db_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingDocumentDbEventSourceConfigArgs, EventSourceMappingDocumentDbEventSourceConfigArgsDict]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., event_source_arn: Optional[pulumi.Input[_builtins.str]] = ..., filter_criteria: Optional[pulumi.Input[Union[EventSourceMappingFilterCriteriaArgs, EventSourceMappingFilterCriteriaArgsDict]]] = ..., function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_response_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., last_processing_result: Optional[pulumi.Input[_builtins.str]] = ..., maximum_batching_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_record_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., metrics_config: Optional[pulumi.Input[Union[EventSourceMappingMetricsConfigArgs, EventSourceMappingMetricsConfigArgsDict]]] = ..., parallelization_factor: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_poller_config: Optional[pulumi.Input[Union[EventSourceMappingProvisionedPollerConfigArgs, EventSourceMappingProvisionedPollerConfigArgsDict]]] = ..., queues: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[Union[EventSourceMappingScalingConfigArgs, EventSourceMappingScalingConfigArgsDict]]] = ..., self_managed_event_source: Optional[pulumi.Input[Union[EventSourceMappingSelfManagedEventSourceArgs, EventSourceMappingSelfManagedEventSourceArgsDict]]] = ..., self_managed_kafka_event_source_config: Optional[pulumi.Input[Union[EventSourceMappingSelfManagedKafkaEventSourceConfigArgs, EventSourceMappingSelfManagedKafkaEventSourceConfigArgsDict]]] = ..., source_access_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventSourceMappingSourceAccessConfigurationArgs, EventSourceMappingSourceAccessConfigurationArgsDict]]]]] = ..., starting_position: Optional[pulumi.Input[_builtins.str]] = ..., starting_position_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_transition_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tumbling_window_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., uuid: Optional[pulumi.Input[_builtins.str]] = ...) -> EventSourceMapping:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonManagedKafkaEventSourceConfig")
    def amazon_managed_kafka_event_source_config(self) -> pulumi.Output[outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bisectBatchOnFunctionError")
    def bisect_batch_on_function_error(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Output[Optional[outputs.EventSourceMappingDestinationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentDbEventSourceConfig")
    def document_db_event_source_config(self) -> pulumi.Output[Optional[outputs.EventSourceMappingDocumentDbEventSourceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceArn")
    def event_source_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> pulumi.Output[Optional[outputs.EventSourceMappingFilterCriteria]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionResponseTypes")
    def function_response_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastProcessingResult")
    def last_processing_result(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchingWindowInSeconds")
    def maximum_batching_window_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRecordAgeInSeconds")
    def maximum_record_age_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsConfig")
    def metrics_config(self) -> pulumi.Output[Optional[outputs.EventSourceMappingMetricsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelizationFactor")
    def parallelization_factor(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedPollerConfig")
    def provisioned_poller_config(self) -> pulumi.Output[Optional[outputs.EventSourceMappingProvisionedPollerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queues(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> pulumi.Output[Optional[outputs.EventSourceMappingScalingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedEventSource")
    def self_managed_event_source(self) -> pulumi.Output[Optional[outputs.EventSourceMappingSelfManagedEventSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedKafkaEventSourceConfig")
    def self_managed_kafka_event_source_config(self) -> pulumi.Output[outputs.EventSourceMappingSelfManagedKafkaEventSourceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccessConfigurations")
    def source_access_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.EventSourceMappingSourceAccessConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPosition")
    def starting_position(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startingPositionTimestamp")
    def starting_position_timestamp(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateTransitionReason")
    def state_transition_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tumblingWindowInSeconds")
    def tumbling_window_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


