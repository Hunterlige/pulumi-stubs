import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BotAssociationLexBot",
    "HoursOfOperationConfig",
    "HoursOfOperationConfigEndTime",
    "HoursOfOperationConfigStartTime",
    "InstanceStorageConfigStorageConfig",
    ...,
    ...,
    ...,
    ...,
    "InstanceStorageConfigStorageConfigS3Config",
    ...,
    "PhoneNumberStatus",
    "QueueOutboundCallerConfig",
    "QuickConnectQuickConnectConfig",
    "QuickConnectQuickConnectConfigPhoneConfig",
    "QuickConnectQuickConnectConfigQueueConfig",
    "QuickConnectQuickConnectConfigUserConfig",
    "RoutingProfileMediaConcurrency",
    "RoutingProfileMediaConcurrencyCrossChannelBehavior",
    "RoutingProfileQueueConfig",
    "UserHierarchyGroupHierarchyPath",
    "UserHierarchyGroupHierarchyPathLevelFife",
    "UserHierarchyGroupHierarchyPathLevelFour",
    "UserHierarchyGroupHierarchyPathLevelOne",
    "UserHierarchyGroupHierarchyPathLevelThree",
    "UserHierarchyGroupHierarchyPathLevelTwo",
    "UserHierarchyStructureHierarchyStructure",
    "UserHierarchyStructureHierarchyStructureLevelFive",
    "UserHierarchyStructureHierarchyStructureLevelFour",
    "UserHierarchyStructureHierarchyStructureLevelOne",
    "UserHierarchyStructureHierarchyStructureLevelThree",
    "UserHierarchyStructureHierarchyStructureLevelTwo",
    "UserIdentityInfo",
    "UserPhoneConfig",
    "GetBotAssociationLexBotResult",
    "GetHoursOfOperationConfigResult",
    "GetHoursOfOperationConfigEndTimeResult",
    "GetHoursOfOperationConfigStartTimeResult",
    "GetInstanceStorageConfigStorageConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetQueueOutboundCallerConfigResult",
    "GetQuickConnectQuickConnectConfigResult",
    "GetQuickConnectQuickConnectConfigPhoneConfigResult",
    "GetQuickConnectQuickConnectConfigQueueConfigResult",
    "GetQuickConnectQuickConnectConfigUserConfigResult",
    "GetRoutingProfileMediaConcurrencyResult",
    ...,
    "GetRoutingProfileQueueConfigResult",
    "GetUserHierarchyGroupHierarchyPathResult",
    "GetUserHierarchyGroupHierarchyPathLevelFifeResult",
    "GetUserHierarchyGroupHierarchyPathLevelFourResult",
    "GetUserHierarchyGroupHierarchyPathLevelOneResult",
    "GetUserHierarchyGroupHierarchyPathLevelThreeResult",
    "GetUserHierarchyGroupHierarchyPathLevelTwoResult",
    "GetUserHierarchyStructureHierarchyStructureResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetUserIdentityInfoResult",
    "GetUserPhoneConfigResult",
]

@pulumi.output_type
class BotAssociationLexBot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, lex_region: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lexRegion")
    def lex_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HoursOfOperationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        end_time: outputs.HoursOfOperationConfigEndTime,
        start_time: outputs.HoursOfOperationConfigStartTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> outputs.HoursOfOperationConfigEndTime: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.HoursOfOperationConfigStartTime: ...

@pulumi.output_type
class HoursOfOperationConfigEndTime(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class HoursOfOperationConfigStartTime(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_type: _builtins.str,
        kinesis_firehose_config: Optional[
            outputs.InstanceStorageConfigStorageConfigKinesisFirehoseConfig
        ] = ...,
        kinesis_stream_config: Optional[
            outputs.InstanceStorageConfigStorageConfigKinesisStreamConfig
        ] = ...,
        kinesis_video_stream_config: Optional[
            outputs.InstanceStorageConfigStorageConfigKinesisVideoStreamConfig
        ] = ...,
        s3_config: Optional[outputs.InstanceStorageConfigStorageConfigS3Config] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseConfig")
    def kinesis_firehose_config(
        self,
    ) -> Optional[outputs.InstanceStorageConfigStorageConfigKinesisFirehoseConfig]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfig")
    def kinesis_stream_config(
        self,
    ) -> Optional[outputs.InstanceStorageConfigStorageConfigKinesisStreamConfig]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisVideoStreamConfig")
    def kinesis_video_stream_config(
        self,
    ) -> Optional[
        outputs.InstanceStorageConfigStorageConfigKinesisVideoStreamConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(
        self,
    ) -> Optional[outputs.InstanceStorageConfigStorageConfigS3Config]: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigKinesisFirehoseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, firehose_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigKinesisStreamConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, stream_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigKinesisVideoStreamConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_config: outputs.InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig,
        prefix: _builtins.str,
        retention_period_hours: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> outputs.InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodHours")
    def retention_period_hours(self) -> _builtins.int: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, encryption_type: _builtins.str, key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigS3Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        bucket_prefix: _builtins.str,
        encryption_config: Optional[
            outputs.InstanceStorageConfigStorageConfigS3ConfigEncryptionConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[
        outputs.InstanceStorageConfigStorageConfigS3ConfigEncryptionConfig
    ]: ...

@pulumi.output_type
class InstanceStorageConfigStorageConfigS3ConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, encryption_type: _builtins.str, key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class PhoneNumberStatus(dict):
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QueueOutboundCallerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        outbound_caller_id_name: Optional[_builtins.str] = ...,
        outbound_caller_id_number_id: Optional[_builtins.str] = ...,
        outbound_flow_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdName")
    def outbound_caller_id_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdNumberId")
    def outbound_caller_id_number_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outboundFlowId")
    def outbound_flow_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QuickConnectQuickConnectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        quick_connect_type: _builtins.str,
        phone_configs: Optional[
            Sequence[outputs.QuickConnectQuickConnectConfigPhoneConfig]
        ] = ...,
        queue_configs: Optional[
            Sequence[outputs.QuickConnectQuickConnectConfigQueueConfig]
        ] = ...,
        user_configs: Optional[
            Sequence[outputs.QuickConnectQuickConnectConfigUserConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="quickConnectType")
    def quick_connect_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneConfigs")
    def phone_configs(
        self,
    ) -> Optional[Sequence[outputs.QuickConnectQuickConnectConfigPhoneConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(
        self,
    ) -> Optional[Sequence[outputs.QuickConnectQuickConnectConfigQueueConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="userConfigs")
    def user_configs(
        self,
    ) -> Optional[Sequence[outputs.QuickConnectQuickConnectConfigUserConfig]]: ...

@pulumi.output_type
class QuickConnectQuickConnectConfigPhoneConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class QuickConnectQuickConnectConfigQueueConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, contact_flow_id: _builtins.str, queue_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> _builtins.str: ...

@pulumi.output_type
class QuickConnectQuickConnectConfigUserConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, contact_flow_id: _builtins.str, user_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...

@pulumi.output_type
class RoutingProfileMediaConcurrency(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: _builtins.str,
        concurrency: _builtins.int,
        cross_channel_behavior: Optional[
            outputs.RoutingProfileMediaConcurrencyCrossChannelBehavior
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="crossChannelBehavior")
    def cross_channel_behavior(
        self,
    ) -> Optional[outputs.RoutingProfileMediaConcurrencyCrossChannelBehavior]: ...

@pulumi.output_type
class RoutingProfileMediaConcurrencyCrossChannelBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, behavior_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="behaviorType")
    def behavior_type(self) -> _builtins.str: ...

@pulumi.output_type
class RoutingProfileQueueConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: _builtins.str,
        delay: _builtins.int,
        priority: _builtins.int,
        queue_id: _builtins.str,
        queue_arn: Optional[_builtins.str] = ...,
        queue_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def delay(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPath(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        level_fives: Optional[
            Sequence[outputs.UserHierarchyGroupHierarchyPathLevelFife]
        ] = ...,
        level_fours: Optional[
            Sequence[outputs.UserHierarchyGroupHierarchyPathLevelFour]
        ] = ...,
        level_ones: Optional[
            Sequence[outputs.UserHierarchyGroupHierarchyPathLevelOne]
        ] = ...,
        level_threes: Optional[
            Sequence[outputs.UserHierarchyGroupHierarchyPathLevelThree]
        ] = ...,
        level_twos: Optional[
            Sequence[outputs.UserHierarchyGroupHierarchyPathLevelTwo]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="levelFives")
    def level_fives(
        self,
    ) -> Optional[Sequence[outputs.UserHierarchyGroupHierarchyPathLevelFife]]: ...
    @_builtins.property
    @pulumi.getter(name="levelFours")
    def level_fours(
        self,
    ) -> Optional[Sequence[outputs.UserHierarchyGroupHierarchyPathLevelFour]]: ...
    @_builtins.property
    @pulumi.getter(name="levelOnes")
    def level_ones(
        self,
    ) -> Optional[Sequence[outputs.UserHierarchyGroupHierarchyPathLevelOne]]: ...
    @_builtins.property
    @pulumi.getter(name="levelThrees")
    def level_threes(
        self,
    ) -> Optional[Sequence[outputs.UserHierarchyGroupHierarchyPathLevelThree]]: ...
    @_builtins.property
    @pulumi.getter(name="levelTwos")
    def level_twos(
        self,
    ) -> Optional[Sequence[outputs.UserHierarchyGroupHierarchyPathLevelTwo]]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPathLevelFife(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPathLevelFour(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPathLevelOne(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPathLevelThree(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyGroupHierarchyPathLevelTwo(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructure(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        level_five: Optional[
            outputs.UserHierarchyStructureHierarchyStructureLevelFive
        ] = ...,
        level_four: Optional[
            outputs.UserHierarchyStructureHierarchyStructureLevelFour
        ] = ...,
        level_one: Optional[
            outputs.UserHierarchyStructureHierarchyStructureLevelOne
        ] = ...,
        level_three: Optional[
            outputs.UserHierarchyStructureHierarchyStructureLevelThree
        ] = ...,
        level_two: Optional[
            outputs.UserHierarchyStructureHierarchyStructureLevelTwo
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="levelFive")
    def level_five(
        self,
    ) -> Optional[outputs.UserHierarchyStructureHierarchyStructureLevelFive]: ...
    @_builtins.property
    @pulumi.getter(name="levelFour")
    def level_four(
        self,
    ) -> Optional[outputs.UserHierarchyStructureHierarchyStructureLevelFour]: ...
    @_builtins.property
    @pulumi.getter(name="levelOne")
    def level_one(
        self,
    ) -> Optional[outputs.UserHierarchyStructureHierarchyStructureLevelOne]: ...
    @_builtins.property
    @pulumi.getter(name="levelThree")
    def level_three(
        self,
    ) -> Optional[outputs.UserHierarchyStructureHierarchyStructureLevelThree]: ...
    @_builtins.property
    @pulumi.getter(name="levelTwo")
    def level_two(
        self,
    ) -> Optional[outputs.UserHierarchyStructureHierarchyStructureLevelTwo]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructureLevelFive(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructureLevelFour(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructureLevelOne(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructureLevelThree(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserHierarchyStructureHierarchyStructureLevelTwo(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserIdentityInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        secondary_email: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryEmail")
    def secondary_email(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserPhoneConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        phone_type: _builtins.str,
        after_contact_work_time_limit: Optional[_builtins.int] = ...,
        auto_accept: Optional[_builtins.bool] = ...,
        desk_phone_number: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneType")
    def phone_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="afterContactWorkTimeLimit")
    def after_contact_work_time_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deskPhoneNumber")
    def desk_phone_number(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetBotAssociationLexBotResult(dict):
    def __init__(
        __self__, *, lex_region: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lexRegion")
    def lex_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetHoursOfOperationConfigResult(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        end_times: Sequence[outputs.GetHoursOfOperationConfigEndTimeResult],
        start_times: Sequence[outputs.GetHoursOfOperationConfigStartTimeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimes")
    def end_times(self) -> Sequence[outputs.GetHoursOfOperationConfigEndTimeResult]: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[outputs.GetHoursOfOperationConfigStartTimeResult]: ...

@pulumi.output_type
class GetHoursOfOperationConfigEndTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetHoursOfOperationConfigStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigResult(dict):
    def __init__(
        __self__,
        *,
        kinesis_firehose_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigKinesisFirehoseConfigResult
        ],
        kinesis_stream_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigKinesisStreamConfigResult
        ],
        kinesis_video_stream_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigResult
        ],
        s3_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigS3ConfigResult
        ],
        storage_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseConfigs")
    def kinesis_firehose_configs(
        self,
    ) -> Sequence[
        outputs.GetInstanceStorageConfigStorageConfigKinesisFirehoseConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfigs")
    def kinesis_stream_configs(
        self,
    ) -> Sequence[
        outputs.GetInstanceStorageConfigStorageConfigKinesisStreamConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisVideoStreamConfigs")
    def kinesis_video_stream_configs(
        self,
    ) -> Sequence[
        outputs.GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3Configs")
    def s3_configs(
        self,
    ) -> Sequence[outputs.GetInstanceStorageConfigStorageConfigS3ConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigKinesisFirehoseConfigResult(dict):
    def __init__(__self__, *, firehose_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firehoseArn")
    def firehose_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigKinesisStreamConfigResult(dict):
    def __init__(__self__, *, stream_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigResult(dict):
    def __init__(
        __self__,
        *,
        encryption_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigResult
        ],
        prefix: _builtins.str,
        retention_period_hours: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(
        self,
    ) -> Sequence[
        outputs.GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodHours")
    def retention_period_hours(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigResult(
    dict
):
    def __init__(
        __self__, *, encryption_type: _builtins.str, key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigS3ConfigResult(dict):
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        bucket_prefix: _builtins.str,
        encryption_configs: Sequence[
            outputs.GetInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(
        self,
    ) -> Sequence[
        outputs.GetInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigResult
    ]: ...

@pulumi.output_type
class GetInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigResult(dict):
    def __init__(
        __self__, *, encryption_type: _builtins.str, key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetQueueOutboundCallerConfigResult(dict):
    def __init__(
        __self__,
        *,
        outbound_caller_id_name: _builtins.str,
        outbound_caller_id_number_id: _builtins.str,
        outbound_flow_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdName")
    def outbound_caller_id_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outboundCallerIdNumberId")
    def outbound_caller_id_number_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outboundFlowId")
    def outbound_flow_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetQuickConnectQuickConnectConfigResult(dict):
    def __init__(
        __self__,
        *,
        phone_configs: Sequence[
            outputs.GetQuickConnectQuickConnectConfigPhoneConfigResult
        ],
        queue_configs: Sequence[
            outputs.GetQuickConnectQuickConnectConfigQueueConfigResult
        ],
        quick_connect_type: _builtins.str,
        user_configs: Sequence[
            outputs.GetQuickConnectQuickConnectConfigUserConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneConfigs")
    def phone_configs(
        self,
    ) -> Sequence[outputs.GetQuickConnectQuickConnectConfigPhoneConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(
        self,
    ) -> Sequence[outputs.GetQuickConnectQuickConnectConfigQueueConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="quickConnectType")
    def quick_connect_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userConfigs")
    def user_configs(
        self,
    ) -> Sequence[outputs.GetQuickConnectQuickConnectConfigUserConfigResult]: ...

@pulumi.output_type
class GetQuickConnectQuickConnectConfigPhoneConfigResult(dict):
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class GetQuickConnectQuickConnectConfigQueueConfigResult(dict):
    def __init__(
        __self__, *, contact_flow_id: _builtins.str, queue_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetQuickConnectQuickConnectConfigUserConfigResult(dict):
    def __init__(
        __self__, *, contact_flow_id: _builtins.str, user_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowId")
    def contact_flow_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetRoutingProfileMediaConcurrencyResult(dict):
    def __init__(
        __self__,
        *,
        channel: _builtins.str,
        concurrency: _builtins.int,
        cross_channel_behaviors: Sequence[
            outputs.GetRoutingProfileMediaConcurrencyCrossChannelBehaviorResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="crossChannelBehaviors")
    def cross_channel_behaviors(
        self,
    ) -> Sequence[
        outputs.GetRoutingProfileMediaConcurrencyCrossChannelBehaviorResult
    ]: ...

@pulumi.output_type
class GetRoutingProfileMediaConcurrencyCrossChannelBehaviorResult(dict):
    def __init__(__self__, *, behavior_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="behaviorType")
    def behavior_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetRoutingProfileQueueConfigResult(dict):
    def __init__(
        __self__,
        *,
        channel: _builtins.str,
        delay: _builtins.int,
        priority: _builtins.int,
        queue_arn: _builtins.str,
        queue_id: _builtins.str,
        queue_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def delay(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathResult(dict):
    def __init__(
        __self__,
        *,
        level_fives: Sequence[
            outputs.GetUserHierarchyGroupHierarchyPathLevelFifeResult
        ],
        level_fours: Sequence[
            outputs.GetUserHierarchyGroupHierarchyPathLevelFourResult
        ],
        level_ones: Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelOneResult],
        level_threes: Sequence[
            outputs.GetUserHierarchyGroupHierarchyPathLevelThreeResult
        ],
        level_twos: Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelTwoResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="levelFives")
    def level_fives(
        self,
    ) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelFifeResult]: ...
    @_builtins.property
    @pulumi.getter(name="levelFours")
    def level_fours(
        self,
    ) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelFourResult]: ...
    @_builtins.property
    @pulumi.getter(name="levelOnes")
    def level_ones(
        self,
    ) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelOneResult]: ...
    @_builtins.property
    @pulumi.getter(name="levelThrees")
    def level_threes(
        self,
    ) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelThreeResult]: ...
    @_builtins.property
    @pulumi.getter(name="levelTwos")
    def level_twos(
        self,
    ) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathLevelTwoResult]: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathLevelFifeResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathLevelFourResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathLevelOneResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathLevelThreeResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyGroupHierarchyPathLevelTwoResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureResult(dict):
    def __init__(
        __self__,
        *,
        level_fives: Sequence[
            outputs.GetUserHierarchyStructureHierarchyStructureLevelFifeResult
        ],
        level_fours: Sequence[
            outputs.GetUserHierarchyStructureHierarchyStructureLevelFourResult
        ],
        level_ones: Sequence[
            outputs.GetUserHierarchyStructureHierarchyStructureLevelOneResult
        ],
        level_threes: Sequence[
            outputs.GetUserHierarchyStructureHierarchyStructureLevelThreeResult
        ],
        level_twos: Sequence[
            outputs.GetUserHierarchyStructureHierarchyStructureLevelTwoResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="levelFives")
    def level_fives(
        self,
    ) -> Sequence[
        outputs.GetUserHierarchyStructureHierarchyStructureLevelFifeResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="levelFours")
    def level_fours(
        self,
    ) -> Sequence[
        outputs.GetUserHierarchyStructureHierarchyStructureLevelFourResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="levelOnes")
    def level_ones(
        self,
    ) -> Sequence[
        outputs.GetUserHierarchyStructureHierarchyStructureLevelOneResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="levelThrees")
    def level_threes(
        self,
    ) -> Sequence[
        outputs.GetUserHierarchyStructureHierarchyStructureLevelThreeResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="levelTwos")
    def level_twos(
        self,
    ) -> Sequence[
        outputs.GetUserHierarchyStructureHierarchyStructureLevelTwoResult
    ]: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureLevelFifeResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureLevelFourResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureLevelOneResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureLevelThreeResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserHierarchyStructureHierarchyStructureLevelTwoResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserIdentityInfoResult(dict):
    def __init__(
        __self__,
        *,
        email: _builtins.str,
        first_name: _builtins.str,
        last_name: _builtins.str,
        secondary_email: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryEmail")
    def secondary_email(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserPhoneConfigResult(dict):
    def __init__(
        __self__,
        *,
        after_contact_work_time_limit: _builtins.int,
        auto_accept: _builtins.bool,
        desk_phone_number: _builtins.str,
        phone_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterContactWorkTimeLimit")
    def after_contact_work_time_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deskPhoneNumber")
    def desk_phone_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneType")
    def phone_type(self) -> _builtins.str: ...
