import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RecordingConfigurationArgs", "RecordingConfiguration"]

@pulumi.input_type
class RecordingConfigurationArgs:
    def __init__(
        __self__,
        *,
        destination_configuration: pulumi.Input[
            RecordingConfigurationDestinationConfigurationArgs
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recording_reconnect_window_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        thumbnail_configuration: Optional[
            pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> pulumi.Input[RecordingConfigurationDestinationConfigurationArgs]: ...
    @destination_configuration.setter
    def destination_configuration(
        self, value: pulumi.Input[RecordingConfigurationDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recording_reconnect_window_seconds.setter
    def recording_reconnect_window_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> Optional[pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]]: ...
    @thumbnail_configuration.setter
    def thumbnail_configuration(
        self,
        value: Optional[pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]],
    ): ...

@pulumi.input_type
class _RecordingConfigurationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configuration: Optional[
            pulumi.Input[RecordingConfigurationDestinationConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recording_reconnect_window_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        thumbnail_configuration: Optional[
            pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> Optional[pulumi.Input[RecordingConfigurationDestinationConfigurationArgs]]: ...
    @destination_configuration.setter
    def destination_configuration(
        self,
        value: Optional[
            pulumi.Input[RecordingConfigurationDestinationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recording_reconnect_window_seconds.setter
    def recording_reconnect_window_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> Optional[pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]]: ...
    @thumbnail_configuration.setter
    def thumbnail_configuration(
        self,
        value: Optional[pulumi.Input[RecordingConfigurationThumbnailConfigurationArgs]],
    ): ...

@pulumi.type_token(...)
class RecordingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination_configuration: Optional[
            pulumi.Input[
                Union[
                    RecordingConfigurationDestinationConfigurationArgs,
                    RecordingConfigurationDestinationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recording_reconnect_window_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        thumbnail_configuration: Optional[
            pulumi.Input[
                Union[
                    RecordingConfigurationThumbnailConfigurationArgs,
                    RecordingConfigurationThumbnailConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RecordingConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configuration: Optional[
            pulumi.Input[
                Union[
                    RecordingConfigurationDestinationConfigurationArgs,
                    RecordingConfigurationDestinationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recording_reconnect_window_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        thumbnail_configuration: Optional[
            pulumi.Input[
                Union[
                    RecordingConfigurationThumbnailConfigurationArgs,
                    RecordingConfigurationThumbnailConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> RecordingConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> pulumi.Output[outputs.RecordingConfigurationDestinationConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> pulumi.Output[outputs.RecordingConfigurationThumbnailConfiguration]: ...
