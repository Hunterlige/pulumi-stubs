

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BotAssociationLexBotArgs', 'BotAssociationLexBotArgsDict', 'HoursOfOperationConfigArgs', 'HoursOfOperationConfigArgsDict', 'HoursOfOperationConfigEndTimeArgs', 'HoursOfOperationConfigEndTimeArgsDict', 'HoursOfOperationConfigStartTimeArgs', 'HoursOfOperationConfigStartTimeArgsDict', 'InstanceStorageConfigStorageConfigArgs', 'InstanceStorageConfigStorageConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'InstanceStorageConfigStorageConfigS3ConfigArgs', 'InstanceStorageConfigStorageConfigS3ConfigArgsDict', ..., ..., 'PhoneNumberStatusArgs', 'PhoneNumberStatusArgsDict', 'QueueOutboundCallerConfigArgs', 'QueueOutboundCallerConfigArgsDict', 'QuickConnectQuickConnectConfigArgs', 'QuickConnectQuickConnectConfigArgsDict', 'QuickConnectQuickConnectConfigPhoneConfigArgs', 'QuickConnectQuickConnectConfigPhoneConfigArgsDict', 'QuickConnectQuickConnectConfigQueueConfigArgs', 'QuickConnectQuickConnectConfigQueueConfigArgsDict', 'QuickConnectQuickConnectConfigUserConfigArgs', 'QuickConnectQuickConnectConfigUserConfigArgsDict', 'RoutingProfileMediaConcurrencyArgs', 'RoutingProfileMediaConcurrencyArgsDict', ..., ..., 'RoutingProfileQueueConfigArgs', 'RoutingProfileQueueConfigArgsDict', 'UserHierarchyGroupHierarchyPathArgs', 'UserHierarchyGroupHierarchyPathArgsDict', 'UserHierarchyGroupHierarchyPathLevelFifeArgs', 'UserHierarchyGroupHierarchyPathLevelFifeArgsDict', 'UserHierarchyGroupHierarchyPathLevelFourArgs', 'UserHierarchyGroupHierarchyPathLevelFourArgsDict', 'UserHierarchyGroupHierarchyPathLevelOneArgs', 'UserHierarchyGroupHierarchyPathLevelOneArgsDict', 'UserHierarchyGroupHierarchyPathLevelThreeArgs', 'UserHierarchyGroupHierarchyPathLevelThreeArgsDict', 'UserHierarchyGroupHierarchyPathLevelTwoArgs', 'UserHierarchyGroupHierarchyPathLevelTwoArgsDict', 'UserHierarchyStructureHierarchyStructureArgs', 'UserHierarchyStructureHierarchyStructureArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'UserIdentityInfoArgs', 'UserIdentityInfoArgsDict', 'UserPhoneConfigArgs', 'UserPhoneConfigArgsDict', 'GetBotAssociationLexBotArgs', 'GetBotAssociationLexBotArgsDict']
class BotAssociationLexBotArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    lex_region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BotAssociationLexBotArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], lex_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexRegion")
    def lex_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lex_region.setter
    def lex_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HoursOfOperationConfigArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    end_time: pulumi.Input[HoursOfOperationConfigEndTimeArgsDict]
    start_time: pulumi.Input[HoursOfOperationConfigStartTimeArgsDict]


@pulumi.input_type
class HoursOfOperationConfigArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.str], end_time: pulumi.Input[HoursOfOperationConfigEndTimeArgs], start_time: pulumi.Input[HoursOfOperationConfigStartTimeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[HoursOfOperationConfigEndTimeArgs]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: pulumi.Input[HoursOfOperationConfigEndTimeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[HoursOfOperationConfigStartTimeArgs]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[HoursOfOperationConfigStartTimeArgs]): # -> None:
        ...
    


class HoursOfOperationConfigEndTimeArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]
    minutes: pulumi.Input[_builtins.int]


@pulumi.input_type
class HoursOfOperationConfigEndTimeArgs:
    def __init__(__self__, *, hours: pulumi.Input[_builtins.int], minutes: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class HoursOfOperationConfigStartTimeArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]
    minutes: pulumi.Input[_builtins.int]


@pulumi.input_type
class HoursOfOperationConfigStartTimeArgs:
    def __init__(__self__, *, hours: pulumi.Input[_builtins.int], minutes: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigArgsDict(TypedDict):
    storage_type: pulumi.Input[_builtins.str]
    kinesis_firehose_config: NotRequired[pulumi.Input[InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgsDict]]
    kinesis_stream_config: NotRequired[pulumi.Input[InstanceStorageConfigStorageConfigKinesisStreamConfigArgsDict]]
    kinesis_video_stream_config: NotRequired[pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgsDict]]
    s3_config: NotRequired[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigArgsDict]]


@pulumi.input_type
class InstanceStorageConfigStorageConfigArgs:
    def __init__(__self__, *, storage_type: pulumi.Input[_builtins.str], kinesis_firehose_config: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgs]] = ..., kinesis_stream_config: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisStreamConfigArgs]] = ..., kinesis_video_stream_config: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgs]] = ..., s3_config: Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseConfig")
    def kinesis_firehose_config(self) -> Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgs]]:
        
        ...
    
    @kinesis_firehose_config.setter
    def kinesis_firehose_config(self, value: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfig")
    def kinesis_stream_config(self) -> Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisStreamConfigArgs]]:
        
        ...
    
    @kinesis_stream_config.setter
    def kinesis_stream_config(self, value: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisStreamConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisVideoStreamConfig")
    def kinesis_video_stream_config(self) -> Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgs]]:
        
        ...
    
    @kinesis_video_stream_config.setter
    def kinesis_video_stream_config(self, value: Optional[pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigArgs]]:
        
        ...
    
    @s3_config.setter
    def s3_config(self, value: Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigArgs]]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgsDict(TypedDict):
    firehose_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstanceStorageConfigStorageConfigKinesisFirehoseConfigArgs:
    def __init__(__self__, *, firehose_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @firehose_arn.setter
    def firehose_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigKinesisStreamConfigArgsDict(TypedDict):
    stream_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstanceStorageConfigStorageConfigKinesisStreamConfigArgs:
    def __init__(__self__, *, stream_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgsDict(TypedDict):
    encryption_config: pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgsDict]
    prefix: pulumi.Input[_builtins.str]
    retention_period_hours: pulumi.Input[_builtins.int]


@pulumi.input_type
class InstanceStorageConfigStorageConfigKinesisVideoStreamConfigArgs:
    def __init__(__self__, *, encryption_config: pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgs], prefix: pulumi.Input[_builtins.str], retention_period_hours: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgs]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: pulumi.Input[InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodHours")
    def retention_period_hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @retention_period_hours.setter
    def retention_period_hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgsDict(TypedDict):
    encryption_type: pulumi.Input[_builtins.str]
    key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigArgs:
    def __init__(__self__, *, encryption_type: pulumi.Input[_builtins.str], key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigS3ConfigArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    bucket_prefix: pulumi.Input[_builtins.str]
    encryption_config: NotRequired[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgsDict]]


@pulumi.input_type
class InstanceStorageConfigStorageConfigS3ConfigArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], bucket_prefix: pulumi.Input[_builtins.str], encryption_config: Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgs]]): # -> None:
        ...
    


class InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgsDict(TypedDict):
    encryption_type: pulumi.Input[_builtins.str]
    key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstanceStorageConfigStorageConfigS3ConfigEncryptionConfigArgs:
    def __init__(__self__, *, encryption_type: pulumi.Input[_builtins.str], key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PhoneNumberStatusArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PhoneNumberStatusArgs:
    def __init__(__self__, *, message: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class QueueOutboundCallerConfigArgsDict(TypedDict):
    outbound_caller_id_name: NotRequired[pulumi.Input[_builtins.str]]
    outbound_caller_id_number_id: NotRequired[pulumi.Input[_builtins.str]]
    outbound_flow_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class QueueOutboundCallerConfigArgs:
    def __init__(__self__, *, outbound_caller_id_name: Optional[pulumi.Input[_builtins.str]] = ..., outbound_caller_id_number_id: Optional[pulumi.Input[_builtins.str]] = ..., outbound_flow_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdName")
    def outbound_caller_id_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outbound_caller_id_name.setter
    def outbound_caller_id_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdNumberId")
    def outbound_caller_id_number_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outbound_caller_id_number_id.setter
    def outbound_caller_id_number_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundFlowId")
    def outbound_flow_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outbound_flow_id.setter
    def outbound_flow_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class QuickConnectQuickConnectConfigArgsDict(TypedDict):
    quick_connect_type: pulumi.Input[_builtins.str]
    phone_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigPhoneConfigArgsDict]]]]
    queue_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigQueueConfigArgsDict]]]]
    user_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigUserConfigArgsDict]]]]


@pulumi.input_type
class QuickConnectQuickConnectConfigArgs:
    def __init__(__self__, *, quick_connect_type: pulumi.Input[_builtins.str], phone_configs: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigPhoneConfigArgs]]]] = ..., queue_configs: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigQueueConfigArgs]]]] = ..., user_configs: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigUserConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quickConnectType")
    def quick_connect_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @quick_connect_type.setter
    def quick_connect_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneConfigs")
    def phone_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigPhoneConfigArgs]]]]:
        
        ...
    
    @phone_configs.setter
    def phone_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigPhoneConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigQueueConfigArgs]]]]:
        
        ...
    
    @queue_configs.setter
    def queue_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigQueueConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userConfigs")
    def user_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigUserConfigArgs]]]]:
        
        ...
    
    @user_configs.setter
    def user_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QuickConnectQuickConnectConfigUserConfigArgs]]]]): # -> None:
        ...
    


class QuickConnectQuickConnectConfigPhoneConfigArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class QuickConnectQuickConnectConfigPhoneConfigArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class QuickConnectQuickConnectConfigQueueConfigArgsDict(TypedDict):
    contact_flow_id: pulumi.Input[_builtins.str]
    queue_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class QuickConnectQuickConnectConfigQueueConfigArgs:
    def __init__(__self__, *, contact_flow_id: pulumi.Input[_builtins.str], queue_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_flow_id.setter
    def contact_flow_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @queue_id.setter
    def queue_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class QuickConnectQuickConnectConfigUserConfigArgsDict(TypedDict):
    contact_flow_id: pulumi.Input[_builtins.str]
    user_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class QuickConnectQuickConnectConfigUserConfigArgs:
    def __init__(__self__, *, contact_flow_id: pulumi.Input[_builtins.str], user_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_flow_id.setter
    def contact_flow_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_id.setter
    def user_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RoutingProfileMediaConcurrencyArgsDict(TypedDict):
    channel: pulumi.Input[_builtins.str]
    concurrency: pulumi.Input[_builtins.int]
    cross_channel_behavior: NotRequired[pulumi.Input[RoutingProfileMediaConcurrencyCrossChannelBehaviorArgsDict]]


@pulumi.input_type
class RoutingProfileMediaConcurrencyArgs:
    def __init__(__self__, *, channel: pulumi.Input[_builtins.str], concurrency: pulumi.Input[_builtins.int], cross_channel_behavior: Optional[pulumi.Input[RoutingProfileMediaConcurrencyCrossChannelBehaviorArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel.setter
    def channel(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @concurrency.setter
    def concurrency(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossChannelBehavior")
    def cross_channel_behavior(self) -> Optional[pulumi.Input[RoutingProfileMediaConcurrencyCrossChannelBehaviorArgs]]:
        
        ...
    
    @cross_channel_behavior.setter
    def cross_channel_behavior(self, value: Optional[pulumi.Input[RoutingProfileMediaConcurrencyCrossChannelBehaviorArgs]]): # -> None:
        ...
    


class RoutingProfileMediaConcurrencyCrossChannelBehaviorArgsDict(TypedDict):
    behavior_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class RoutingProfileMediaConcurrencyCrossChannelBehaviorArgs:
    def __init__(__self__, *, behavior_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorType")
    def behavior_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @behavior_type.setter
    def behavior_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RoutingProfileQueueConfigArgsDict(TypedDict):
    channel: pulumi.Input[_builtins.str]
    delay: pulumi.Input[_builtins.int]
    priority: pulumi.Input[_builtins.int]
    queue_id: pulumi.Input[_builtins.str]
    queue_arn: NotRequired[pulumi.Input[_builtins.str]]
    queue_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RoutingProfileQueueConfigArgs:
    def __init__(__self__, *, channel: pulumi.Input[_builtins.str], delay: pulumi.Input[_builtins.int], priority: pulumi.Input[_builtins.int], queue_id: pulumi.Input[_builtins.str], queue_arn: Optional[pulumi.Input[_builtins.str]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel.setter
    def channel(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delay(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @delay.setter
    def delay(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @queue_id.setter
    def queue_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_arn.setter
    def queue_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathArgsDict(TypedDict):
    level_fives: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFifeArgsDict]]]]
    level_fours: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFourArgsDict]]]]
    level_ones: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelOneArgsDict]]]]
    level_threes: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelThreeArgsDict]]]]
    level_twos: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelTwoArgsDict]]]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathArgs:
    def __init__(__self__, *, level_fives: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFifeArgs]]]] = ..., level_fours: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFourArgs]]]] = ..., level_ones: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelOneArgs]]]] = ..., level_threes: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelThreeArgs]]]] = ..., level_twos: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelTwoArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelFives")
    def level_fives(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFifeArgs]]]]:
        
        ...
    
    @level_fives.setter
    def level_fives(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFifeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelFours")
    def level_fours(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFourArgs]]]]:
        
        ...
    
    @level_fours.setter
    def level_fours(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelFourArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelOnes")
    def level_ones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelOneArgs]]]]:
        
        ...
    
    @level_ones.setter
    def level_ones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelOneArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelThrees")
    def level_threes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelThreeArgs]]]]:
        
        ...
    
    @level_threes.setter
    def level_threes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelThreeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelTwos")
    def level_twos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelTwoArgs]]]]:
        
        ...
    
    @level_twos.setter
    def level_twos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHierarchyGroupHierarchyPathLevelTwoArgs]]]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathLevelFifeArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathLevelFifeArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathLevelFourArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathLevelFourArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathLevelOneArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathLevelOneArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathLevelThreeArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathLevelThreeArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyGroupHierarchyPathLevelTwoArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyGroupHierarchyPathLevelTwoArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureArgsDict(TypedDict):
    level_five: NotRequired[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFiveArgsDict]]
    level_four: NotRequired[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFourArgsDict]]
    level_one: NotRequired[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelOneArgsDict]]
    level_three: NotRequired[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelThreeArgsDict]]
    level_two: NotRequired[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelTwoArgsDict]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureArgs:
    def __init__(__self__, *, level_five: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFiveArgs]] = ..., level_four: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFourArgs]] = ..., level_one: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelOneArgs]] = ..., level_three: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelThreeArgs]] = ..., level_two: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelTwoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelFive")
    def level_five(self) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFiveArgs]]:
        
        ...
    
    @level_five.setter
    def level_five(self, value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFiveArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelFour")
    def level_four(self) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFourArgs]]:
        
        ...
    
    @level_four.setter
    def level_four(self, value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelFourArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelOne")
    def level_one(self) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelOneArgs]]:
        
        ...
    
    @level_one.setter
    def level_one(self, value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelOneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelThree")
    def level_three(self) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelThreeArgs]]:
        
        ...
    
    @level_three.setter
    def level_three(self, value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelThreeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelTwo")
    def level_two(self) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelTwoArgs]]:
        
        ...
    
    @level_two.setter
    def level_two(self, value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureLevelTwoArgs]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureLevelFiveArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureLevelFiveArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureLevelFourArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureLevelFourArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureLevelOneArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureLevelOneArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureLevelThreeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureLevelThreeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserHierarchyStructureHierarchyStructureLevelTwoArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserHierarchyStructureHierarchyStructureLevelTwoArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserIdentityInfoArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]
    secondary_email: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserIdentityInfoArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., secondary_email: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryEmail")
    def secondary_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_email.setter
    def secondary_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserPhoneConfigArgsDict(TypedDict):
    phone_type: pulumi.Input[_builtins.str]
    after_contact_work_time_limit: NotRequired[pulumi.Input[_builtins.int]]
    auto_accept: NotRequired[pulumi.Input[_builtins.bool]]
    desk_phone_number: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserPhoneConfigArgs:
    def __init__(__self__, *, phone_type: pulumi.Input[_builtins.str], after_contact_work_time_limit: Optional[pulumi.Input[_builtins.int]] = ..., auto_accept: Optional[pulumi.Input[_builtins.bool]] = ..., desk_phone_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneType")
    def phone_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_type.setter
    def phone_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterContactWorkTimeLimit")
    def after_contact_work_time_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @after_contact_work_time_limit.setter
    def after_contact_work_time_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_accept.setter
    def auto_accept(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deskPhoneNumber")
    def desk_phone_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desk_phone_number.setter
    def desk_phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GetBotAssociationLexBotArgsDict(TypedDict):
    lex_region: _builtins.str
    name: _builtins.str


@pulumi.input_type
class GetBotAssociationLexBotArgs:
    def __init__(__self__, *, lex_region: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexRegion")
    def lex_region(self) -> _builtins.str:
        
        ...
    
    @lex_region.setter
    def lex_region(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    


