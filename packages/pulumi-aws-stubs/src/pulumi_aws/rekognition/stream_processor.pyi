import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StreamProcessorArgs", "StreamProcessor"]

@pulumi.input_type
class StreamProcessorArgs:
    def __init__(
        __self__,
        *,
        input: pulumi.Input[StreamProcessorInputArgs],
        output: pulumi.Input[StreamProcessorOutputArgs],
        role_arn: pulumi.Input[_builtins.str],
        settings: pulumi.Input[StreamProcessorSettingsArgs],
        data_sharing_preference: Optional[
            pulumi.Input[StreamProcessorDataSharingPreferenceArgs]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channel: Optional[
            pulumi.Input[StreamProcessorNotificationChannelArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions_of_interests: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[StreamProcessorTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> pulumi.Input[StreamProcessorInputArgs]: ...
    @input.setter
    def input(self, value: pulumi.Input[StreamProcessorInputArgs]): ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> pulumi.Input[StreamProcessorOutputArgs]: ...
    @output.setter
    def output(self, value: pulumi.Input[StreamProcessorOutputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Input[StreamProcessorSettingsArgs]: ...
    @settings.setter
    def settings(self, value: pulumi.Input[StreamProcessorSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="dataSharingPreference")
    def data_sharing_preference(
        self,
    ) -> Optional[pulumi.Input[StreamProcessorDataSharingPreferenceArgs]]: ...
    @data_sharing_preference.setter
    def data_sharing_preference(
        self, value: Optional[pulumi.Input[StreamProcessorDataSharingPreferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationChannel")
    def notification_channel(
        self,
    ) -> Optional[pulumi.Input[StreamProcessorNotificationChannelArgs]]: ...
    @notification_channel.setter
    def notification_channel(
        self, value: Optional[pulumi.Input[StreamProcessorNotificationChannelArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionsOfInterests")
    def regions_of_interests(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
    ]: ...
    @regions_of_interests.setter
    def regions_of_interests(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
        ],
    ): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[StreamProcessorTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[StreamProcessorTimeoutsArgs]]): ...

@pulumi.input_type
class _StreamProcessorState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sharing_preference: Optional[
            pulumi.Input[StreamProcessorDataSharingPreferenceArgs]
        ] = ...,
        input: Optional[pulumi.Input[StreamProcessorInputArgs]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channel: Optional[
            pulumi.Input[StreamProcessorNotificationChannelArgs]
        ] = ...,
        output: Optional[pulumi.Input[StreamProcessorOutputArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions_of_interests: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[pulumi.Input[StreamProcessorSettingsArgs]] = ...,
        stream_processor_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[StreamProcessorTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSharingPreference")
    def data_sharing_preference(
        self,
    ) -> Optional[pulumi.Input[StreamProcessorDataSharingPreferenceArgs]]: ...
    @data_sharing_preference.setter
    def data_sharing_preference(
        self, value: Optional[pulumi.Input[StreamProcessorDataSharingPreferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[StreamProcessorInputArgs]]: ...
    @input.setter
    def input(self, value: Optional[pulumi.Input[StreamProcessorInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationChannel")
    def notification_channel(
        self,
    ) -> Optional[pulumi.Input[StreamProcessorNotificationChannelArgs]]: ...
    @notification_channel.setter
    def notification_channel(
        self, value: Optional[pulumi.Input[StreamProcessorNotificationChannelArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input[StreamProcessorOutputArgs]]: ...
    @output.setter
    def output(self, value: Optional[pulumi.Input[StreamProcessorOutputArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionsOfInterests")
    def regions_of_interests(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
    ]: ...
    @regions_of_interests.setter
    def regions_of_interests(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[StreamProcessorSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[StreamProcessorSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="streamProcessorArn")
    @_utilities.deprecated(...)
    def stream_processor_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_processor_arn.setter
    def stream_processor_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[StreamProcessorTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[StreamProcessorTimeoutsArgs]]): ...

@pulumi.type_token("aws:rekognition/streamProcessor:StreamProcessor")
class StreamProcessor(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_sharing_preference: Optional[
            pulumi.Input[
                Union[
                    StreamProcessorDataSharingPreferenceArgs,
                    StreamProcessorDataSharingPreferenceArgsDict,
                ]
            ]
        ] = ...,
        input: Optional[
            pulumi.Input[Union[StreamProcessorInputArgs, StreamProcessorInputArgsDict]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channel: Optional[
            pulumi.Input[
                Union[
                    StreamProcessorNotificationChannelArgs,
                    StreamProcessorNotificationChannelArgsDict,
                ]
            ]
        ] = ...,
        output: Optional[
            pulumi.Input[
                Union[StreamProcessorOutputArgs, StreamProcessorOutputArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions_of_interests: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StreamProcessorRegionsOfInterestArgs,
                            StreamProcessorRegionsOfInterestArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Union[StreamProcessorSettingsArgs, StreamProcessorSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[StreamProcessorTimeoutsArgs, StreamProcessorTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StreamProcessorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sharing_preference: Optional[
            pulumi.Input[
                Union[
                    StreamProcessorDataSharingPreferenceArgs,
                    StreamProcessorDataSharingPreferenceArgsDict,
                ]
            ]
        ] = ...,
        input: Optional[
            pulumi.Input[Union[StreamProcessorInputArgs, StreamProcessorInputArgsDict]]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_channel: Optional[
            pulumi.Input[
                Union[
                    StreamProcessorNotificationChannelArgs,
                    StreamProcessorNotificationChannelArgsDict,
                ]
            ]
        ] = ...,
        output: Optional[
            pulumi.Input[
                Union[StreamProcessorOutputArgs, StreamProcessorOutputArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regions_of_interests: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            StreamProcessorRegionsOfInterestArgs,
                            StreamProcessorRegionsOfInterestArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Union[StreamProcessorSettingsArgs, StreamProcessorSettingsArgsDict]
            ]
        ] = ...,
        stream_processor_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[StreamProcessorTimeoutsArgs, StreamProcessorTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> StreamProcessor: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataSharingPreference")
    def data_sharing_preference(
        self,
    ) -> pulumi.Output[Optional[outputs.StreamProcessorDataSharingPreference]]: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> pulumi.Output[outputs.StreamProcessorInput]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationChannel")
    def notification_channel(
        self,
    ) -> pulumi.Output[Optional[outputs.StreamProcessorNotificationChannel]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> pulumi.Output[outputs.StreamProcessorOutput]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionsOfInterests")
    def regions_of_interests(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.StreamProcessorRegionsOfInterest]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[outputs.StreamProcessorSettings]: ...
    @_builtins.property
    @pulumi.getter(name="streamProcessorArn")
    @_utilities.deprecated(...)
    def stream_processor_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.StreamProcessorTimeouts]]: ...
