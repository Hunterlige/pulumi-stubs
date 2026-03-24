

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueueArgs', 'Queue']
@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *, content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., deduplication_scope: Optional[pulumi.Input[_builtins.str]] = ..., delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., fifo_queue: Optional[pulumi.Input[_builtins.bool]] = ..., fifo_throughput_limit: Optional[pulumi.Input[_builtins.str]] = ..., kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_message_size: Optional[pulumi.Input[_builtins.int]] = ..., message_retention_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., receive_wait_time_seconds: Optional[pulumi.Input[_builtins.int]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sqs_managed_sse_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., visibility_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @content_based_deduplication.setter
    def content_based_deduplication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deduplicationScope")
    def deduplication_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deduplication_scope.setter
    def deduplication_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @delay_seconds.setter
    def delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoQueue")
    def fifo_queue(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fifo_queue.setter
    def fifo_queue(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputLimit")
    def fifo_throughput_limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fifo_throughput_limit.setter
    def fifo_throughput_limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @kms_data_key_reuse_period_seconds.setter
    def kms_data_key_reuse_period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_message_size.setter
    def max_message_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @message_retention_seconds.setter
    def message_retention_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="receiveWaitTimeSeconds")
    def receive_wait_time_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @receive_wait_time_seconds.setter
    def receive_wait_time_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_policy.setter
    def redrive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsManagedSseEnabled")
    def sqs_managed_sse_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sqs_managed_sse_enabled.setter
    def sqs_managed_sse_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityTimeoutSeconds")
    def visibility_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @visibility_timeout_seconds.setter
    def visibility_timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _QueueState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., deduplication_scope: Optional[pulumi.Input[_builtins.str]] = ..., delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., fifo_queue: Optional[pulumi.Input[_builtins.bool]] = ..., fifo_throughput_limit: Optional[pulumi.Input[_builtins.str]] = ..., kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_message_size: Optional[pulumi.Input[_builtins.int]] = ..., message_retention_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., receive_wait_time_seconds: Optional[pulumi.Input[_builtins.int]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sqs_managed_sse_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., visibility_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @content_based_deduplication.setter
    def content_based_deduplication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deduplicationScope")
    def deduplication_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deduplication_scope.setter
    def deduplication_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @delay_seconds.setter
    def delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoQueue")
    def fifo_queue(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fifo_queue.setter
    def fifo_queue(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputLimit")
    def fifo_throughput_limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fifo_throughput_limit.setter
    def fifo_throughput_limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @kms_data_key_reuse_period_seconds.setter
    def kms_data_key_reuse_period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_message_size.setter
    def max_message_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @message_retention_seconds.setter
    def message_retention_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="receiveWaitTimeSeconds")
    def receive_wait_time_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @receive_wait_time_seconds.setter
    def receive_wait_time_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_policy.setter
    def redrive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsManagedSseEnabled")
    def sqs_managed_sse_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sqs_managed_sse_enabled.setter
    def sqs_managed_sse_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityTimeoutSeconds")
    def visibility_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @visibility_timeout_seconds.setter
    def visibility_timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:sqs/queue:Queue")
class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., deduplication_scope: Optional[pulumi.Input[_builtins.str]] = ..., delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., fifo_queue: Optional[pulumi.Input[_builtins.bool]] = ..., fifo_throughput_limit: Optional[pulumi.Input[_builtins.str]] = ..., kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_message_size: Optional[pulumi.Input[_builtins.int]] = ..., message_retention_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., receive_wait_time_seconds: Optional[pulumi.Input[_builtins.int]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sqs_managed_sse_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., visibility_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[QueueArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., content_based_deduplication: Optional[pulumi.Input[_builtins.bool]] = ..., deduplication_scope: Optional[pulumi.Input[_builtins.str]] = ..., delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., fifo_queue: Optional[pulumi.Input[_builtins.bool]] = ..., fifo_throughput_limit: Optional[pulumi.Input[_builtins.str]] = ..., kms_data_key_reuse_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_message_size: Optional[pulumi.Input[_builtins.int]] = ..., message_retention_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., receive_wait_time_seconds: Optional[pulumi.Input[_builtins.int]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sqs_managed_sse_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., visibility_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> Queue:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBasedDeduplication")
    def content_based_deduplication(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deduplicationScope")
    def deduplication_scope(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoQueue")
    def fifo_queue(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fifoThroughputLimit")
    def fifo_throughput_limit(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsDataKeyReusePeriodSeconds")
    def kms_data_key_reuse_period_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiveWaitTimeSeconds")
    def receive_wait_time_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsManagedSseEnabled")
    def sqs_managed_sse_enabled(self) -> pulumi.Output[_builtins.bool]:
        
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
    def url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityTimeoutSeconds")
    def visibility_timeout_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


