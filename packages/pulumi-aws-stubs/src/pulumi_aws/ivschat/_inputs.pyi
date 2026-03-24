import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LoggingConfigurationDestinationConfigurationArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "LoggingConfigurationDestinationConfigurationS3Args",
    ...,
    "RoomMessageReviewHandlerArgs",
    "RoomMessageReviewHandlerArgsDict",
]

class LoggingConfigurationDestinationConfigurationArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[
        pulumi.Input[LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict]
    ]
    firehose: NotRequired[
        pulumi.Input[LoggingConfigurationDestinationConfigurationFirehoseArgsDict]
    ]
    s3: NotRequired[
        pulumi.Input[LoggingConfigurationDestinationConfigurationS3ArgsDict]
    ]
    ...

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs]
        ] = ...,
        firehose: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationFirehoseArgs]
        ] = ...,
        s3: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationS3Args]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[
        pulumi.Input[LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs]
    ]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self,
        value: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def firehose(
        self,
    ) -> Optional[
        pulumi.Input[LoggingConfigurationDestinationConfigurationFirehoseArgs]
    ]: ...
    @firehose.setter
    def firehose(
        self,
        value: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationFirehoseArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[pulumi.Input[LoggingConfigurationDestinationConfigurationS3Args]]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[LoggingConfigurationDestinationConfigurationS3Args]
        ],
    ): ...

class LoggingConfigurationDestinationConfigurationCloudwatchLogsArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationCloudwatchLogsArgs:
    def __init__(__self__, *, log_group_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...

class LoggingConfigurationDestinationConfigurationFirehoseArgsDict(TypedDict):
    delivery_stream_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationFirehoseArgs:
    def __init__(
        __self__, *, delivery_stream_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @delivery_stream_name.setter
    def delivery_stream_name(self, value: pulumi.Input[_builtins.str]): ...

class LoggingConfigurationDestinationConfigurationS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LoggingConfigurationDestinationConfigurationS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...

class RoomMessageReviewHandlerArgsDict(TypedDict):
    fallback_result: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RoomMessageReviewHandlerArgs:
    def __init__(
        __self__,
        *,
        fallback_result: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fallbackResult")
    def fallback_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_result.setter
    def fallback_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
