import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RecordingConfigurationDestinationConfigurationArgs",
    ...,
    ...,
    ...,
    "RecordingConfigurationThumbnailConfigurationArgs",
    ...,
]

class RecordingConfigurationDestinationConfigurationArgsDict(TypedDict):
    s3: pulumi.Input[RecordingConfigurationDestinationConfigurationS3ArgsDict]

@pulumi.input_type
class RecordingConfigurationDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3: pulumi.Input[RecordingConfigurationDestinationConfigurationS3Args],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> pulumi.Input[RecordingConfigurationDestinationConfigurationS3Args]: ...
    @s3.setter
    def s3(
        self, value: pulumi.Input[RecordingConfigurationDestinationConfigurationS3Args]
    ): ...

class RecordingConfigurationDestinationConfigurationS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class RecordingConfigurationDestinationConfigurationS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...

class RecordingConfigurationThumbnailConfigurationArgsDict(TypedDict):
    recording_mode: NotRequired[pulumi.Input[_builtins.str]]
    target_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RecordingConfigurationThumbnailConfigurationArgs:
    def __init__(
        __self__,
        *,
        recording_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        target_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recording_mode.setter
    def recording_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetIntervalSeconds")
    def target_interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_interval_seconds.setter
    def target_interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
