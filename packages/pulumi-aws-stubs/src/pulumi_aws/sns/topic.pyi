

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TopicArgs', 'Topic']
@pulumi.input_type
class TopicArgs:
    def __init__(__self__, *, application_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., archive_policy: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., fifo_throughput_scope: Optional[pulumi.Input[_builtins.str]] = ..., fifo_topic: Optional[pulumi.Input[_builtins.bool]] = ..., firehose_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., http_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lambda_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., signature_version: Optional[pulumi.Input[_builtins.int]] = ..., sqs_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationFailureFeedbackRoleArn")
    def application_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_failure_feedback_role_arn.setter
    def application_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackRoleArn")
    def application_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_success_feedback_role_arn.setter
    def application_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackSampleRate")
    def application_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @application_success_feedback_sample_rate.setter
    def application_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archivePolicy")
    def archive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @archive_policy.setter
    def archive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @content_based_deduplication.setter
    def content_based_deduplication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_policy.setter
    def delivery_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputScope")
    def fifo_throughput_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fifo_throughput_scope.setter
    def fifo_throughput_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoTopic")
    def fifo_topic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fifo_topic.setter
    def fifo_topic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseFailureFeedbackRoleArn")
    def firehose_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firehose_failure_feedback_role_arn.setter
    def firehose_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackRoleArn")
    def firehose_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firehose_success_feedback_role_arn.setter
    def firehose_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackSampleRate")
    def firehose_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @firehose_success_feedback_sample_rate.setter
    def firehose_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpFailureFeedbackRoleArn")
    def http_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_failure_feedback_role_arn.setter
    def http_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackRoleArn")
    def http_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_success_feedback_role_arn.setter
    def http_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackSampleRate")
    def http_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_success_feedback_sample_rate.setter
    def http_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFailureFeedbackRoleArn")
    def lambda_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_failure_feedback_role_arn.setter
    def lambda_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackRoleArn")
    def lambda_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_success_feedback_role_arn.setter
    def lambda_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackSampleRate")
    def lambda_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lambda_success_feedback_sample_rate.setter
    def lambda_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureVersion")
    def signature_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @signature_version.setter
    def signature_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsFailureFeedbackRoleArn")
    def sqs_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sqs_failure_feedback_role_arn.setter
    def sqs_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackRoleArn")
    def sqs_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sqs_success_feedback_role_arn.setter
    def sqs_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackSampleRate")
    def sqs_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sqs_success_feedback_sample_rate.setter
    def sqs_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracing_config.setter
    def tracing_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TopicState:
    def __init__(__self__, *, application_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., archive_policy: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., beginning_archive_time: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., fifo_throughput_scope: Optional[pulumi.Input[_builtins.str]] = ..., fifo_topic: Optional[pulumi.Input[_builtins.bool]] = ..., firehose_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., http_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lambda_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., signature_version: Optional[pulumi.Input[_builtins.int]] = ..., sqs_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationFailureFeedbackRoleArn")
    def application_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_failure_feedback_role_arn.setter
    def application_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackRoleArn")
    def application_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_success_feedback_role_arn.setter
    def application_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackSampleRate")
    def application_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @application_success_feedback_sample_rate.setter
    def application_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archivePolicy")
    def archive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @archive_policy.setter
    def archive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beginningArchiveTime")
    def beginning_archive_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @beginning_archive_time.setter
    def beginning_archive_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @content_based_deduplication.setter
    def content_based_deduplication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_policy.setter
    def delivery_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputScope")
    def fifo_throughput_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fifo_throughput_scope.setter
    def fifo_throughput_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoTopic")
    def fifo_topic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fifo_topic.setter
    def fifo_topic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseFailureFeedbackRoleArn")
    def firehose_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firehose_failure_feedback_role_arn.setter
    def firehose_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackRoleArn")
    def firehose_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firehose_success_feedback_role_arn.setter
    def firehose_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackSampleRate")
    def firehose_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @firehose_success_feedback_sample_rate.setter
    def firehose_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpFailureFeedbackRoleArn")
    def http_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_failure_feedback_role_arn.setter
    def http_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackRoleArn")
    def http_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_success_feedback_role_arn.setter
    def http_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackSampleRate")
    def http_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_success_feedback_sample_rate.setter
    def http_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFailureFeedbackRoleArn")
    def lambda_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_failure_feedback_role_arn.setter
    def lambda_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackRoleArn")
    def lambda_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_success_feedback_role_arn.setter
    def lambda_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackSampleRate")
    def lambda_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lambda_success_feedback_sample_rate.setter
    def lambda_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureVersion")
    def signature_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @signature_version.setter
    def signature_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsFailureFeedbackRoleArn")
    def sqs_failure_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sqs_failure_feedback_role_arn.setter
    def sqs_failure_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackRoleArn")
    def sqs_success_feedback_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sqs_success_feedback_role_arn.setter
    def sqs_success_feedback_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackSampleRate")
    def sqs_success_feedback_sample_rate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sqs_success_feedback_sample_rate.setter
    def sqs_success_feedback_sample_rate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracing_config.setter
    def tracing_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sns/topic:Topic")
class Topic(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., archive_policy: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., fifo_throughput_scope: Optional[pulumi.Input[_builtins.str]] = ..., fifo_topic: Optional[pulumi.Input[_builtins.bool]] = ..., firehose_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., http_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lambda_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., signature_version: Optional[pulumi.Input[_builtins.int]] = ..., sqs_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_config: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[TopicArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., application_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., archive_policy: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., beginning_archive_time: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., fifo_throughput_scope: Optional[pulumi.Input[_builtins.str]] = ..., fifo_topic: Optional[pulumi.Input[_builtins.bool]] = ..., firehose_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., firehose_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., http_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., http_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., lambda_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., lambda_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., signature_version: Optional[pulumi.Input[_builtins.int]] = ..., sqs_failure_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., sqs_success_feedback_sample_rate: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tracing_config: Optional[pulumi.Input[_builtins.str]] = ...) -> Topic:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationFailureFeedbackRoleArn")
    def application_failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackRoleArn")
    def application_success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSuccessFeedbackSampleRate")
    def application_success_feedback_sample_rate(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archivePolicy")
    def archive_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beginningArchiveTime")
    def beginning_archive_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputScope")
    def fifo_throughput_scope(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoTopic")
    def fifo_topic(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseFailureFeedbackRoleArn")
    def firehose_failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackRoleArn")
    def firehose_success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseSuccessFeedbackSampleRate")
    def firehose_success_feedback_sample_rate(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpFailureFeedbackRoleArn")
    def http_failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackRoleArn")
    def http_success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSuccessFeedbackSampleRate")
    def http_success_feedback_sample_rate(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFailureFeedbackRoleArn")
    def lambda_failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackRoleArn")
    def lambda_success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaSuccessFeedbackSampleRate")
    def lambda_success_feedback_sample_rate(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureVersion")
    def signature_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsFailureFeedbackRoleArn")
    def sqs_failure_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackRoleArn")
    def sqs_success_feedback_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsSuccessFeedbackSampleRate")
    def sqs_success_feedback_sample_rate(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    @pulumi.getter(name="tracingConfig")
    def tracing_config(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


