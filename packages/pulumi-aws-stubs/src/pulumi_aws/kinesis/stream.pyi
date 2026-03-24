

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
__all__ = ['StreamArgs', 'Stream']
@pulumi.input_type
class StreamArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., enforce_consumer_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_record_size_in_kib: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., shard_level_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., stream_mode_details: Optional[pulumi.Input[StreamStreamModeDetailsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceConsumerDeletion")
    def enforce_consumer_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce_consumer_deletion.setter
    def enforce_consumer_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRecordSizeInKib")
    def max_record_size_in_kib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_record_size_in_kib.setter
    def max_record_size_in_kib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardLevelMetrics")
    def shard_level_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @shard_level_metrics.setter
    def shard_level_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamModeDetails")
    def stream_mode_details(self) -> Optional[pulumi.Input[StreamStreamModeDetailsArgs]]:
        
        ...
    
    @stream_mode_details.setter
    def stream_mode_details(self, value: Optional[pulumi.Input[StreamStreamModeDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _StreamState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., enforce_consumer_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_record_size_in_kib: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., shard_level_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., stream_mode_details: Optional[pulumi.Input[StreamStreamModeDetailsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceConsumerDeletion")
    def enforce_consumer_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce_consumer_deletion.setter
    def enforce_consumer_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRecordSizeInKib")
    def max_record_size_in_kib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_record_size_in_kib.setter
    def max_record_size_in_kib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardLevelMetrics")
    def shard_level_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @shard_level_metrics.setter
    def shard_level_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamModeDetails")
    def stream_mode_details(self) -> Optional[pulumi.Input[StreamStreamModeDetailsArgs]]:
        
        ...
    
    @stream_mode_details.setter
    def stream_mode_details(self, value: Optional[pulumi.Input[StreamStreamModeDetailsArgs]]): # -> None:
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
    


@pulumi.type_token("aws:kinesis/stream:Stream")
class Stream(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., enforce_consumer_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_record_size_in_kib: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., shard_level_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., stream_mode_details: Optional[pulumi.Input[Union[StreamStreamModeDetailsArgs, StreamStreamModeDetailsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[StreamArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., enforce_consumer_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., max_record_size_in_kib: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., shard_level_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., stream_mode_details: Optional[pulumi.Input[Union[StreamStreamModeDetailsArgs, StreamStreamModeDetailsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Stream:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceConsumerDeletion")
    def enforce_consumer_deletion(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRecordSizeInKib")
    def max_record_size_in_kib(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardLevelMetrics")
    def shard_level_metrics(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamModeDetails")
    def stream_mode_details(self) -> pulumi.Output[outputs.StreamStreamModeDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


