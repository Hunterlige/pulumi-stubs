import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ChannelCdiInputSpecificationArgs",
    "ChannelCdiInputSpecificationArgsDict",
    "ChannelDestinationArgs",
    "ChannelDestinationArgsDict",
    "ChannelDestinationMediaPackageSettingArgs",
    "ChannelDestinationMediaPackageSettingArgsDict",
    "ChannelDestinationMultiplexSettingsArgs",
    "ChannelDestinationMultiplexSettingsArgsDict",
    "ChannelDestinationSettingArgs",
    "ChannelDestinationSettingArgsDict",
    "ChannelEncoderSettingsArgs",
    "ChannelEncoderSettingsArgsDict",
    "ChannelEncoderSettingsAudioDescriptionArgs",
    "ChannelEncoderSettingsAudioDescriptionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelEncoderSettingsAvailBlankingArgs",
    "ChannelEncoderSettingsAvailBlankingArgsDict",
    ...,
    ...,
    "ChannelEncoderSettingsCaptionDescriptionArgs",
    "ChannelEncoderSettingsCaptionDescriptionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelEncoderSettingsGlobalConfigurationArgs",
    "ChannelEncoderSettingsGlobalConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelEncoderSettingsNielsenConfigurationArgs",
    "ChannelEncoderSettingsNielsenConfigurationArgsDict",
    "ChannelEncoderSettingsOutputGroupArgs",
    "ChannelEncoderSettingsOutputGroupArgsDict",
    "ChannelEncoderSettingsOutputGroupOutputArgs",
    "ChannelEncoderSettingsOutputGroupOutputArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelEncoderSettingsTimecodeConfigArgs",
    "ChannelEncoderSettingsTimecodeConfigArgsDict",
    "ChannelEncoderSettingsVideoDescriptionArgs",
    "ChannelEncoderSettingsVideoDescriptionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelInputAttachmentArgs",
    "ChannelInputAttachmentArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelInputAttachmentInputSettingsArgs",
    "ChannelInputAttachmentInputSettingsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelInputSpecificationArgs",
    "ChannelInputSpecificationArgsDict",
    "ChannelMaintenanceArgs",
    "ChannelMaintenanceArgsDict",
    "ChannelVpcArgs",
    "ChannelVpcArgsDict",
    "InputDestinationArgs",
    "InputDestinationArgsDict",
    "InputInputDeviceArgs",
    "InputInputDeviceArgsDict",
    "InputMediaConnectFlowArgs",
    "InputMediaConnectFlowArgsDict",
    "InputSecurityGroupWhitelistRuleArgs",
    "InputSecurityGroupWhitelistRuleArgsDict",
    "InputSourceArgs",
    "InputSourceArgsDict",
    "InputVpcArgs",
    "InputVpcArgsDict",
    "MultiplexMultiplexSettingsArgs",
    "MultiplexMultiplexSettingsArgsDict",
    "MultiplexProgramMultiplexProgramSettingsArgs",
    "MultiplexProgramMultiplexProgramSettingsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "MultiplexProgramTimeoutsArgs",
    "MultiplexProgramTimeoutsArgsDict",
]

class ChannelCdiInputSpecificationArgsDict(TypedDict):
    resolution: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelCdiInputSpecificationArgs:
    def __init__(__self__, *, resolution: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> pulumi.Input[_builtins.str]: ...
    @resolution.setter
    def resolution(self, value: pulumi.Input[_builtins.str]): ...

class ChannelDestinationArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    media_package_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelDestinationMediaPackageSettingArgsDict]]
        ]
    ]
    multiplex_settings: NotRequired[
        pulumi.Input[ChannelDestinationMultiplexSettingsArgsDict]
    ]
    settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ChannelDestinationSettingArgsDict]]]
    ]

@pulumi.input_type
class ChannelDestinationArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        media_package_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelDestinationMediaPackageSettingArgs]]
            ]
        ] = ...,
        multiplex_settings: Optional[
            pulumi.Input[ChannelDestinationMultiplexSettingsArgs]
        ] = ...,
        settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelDestinationSettingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageSettings")
    def media_package_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ChannelDestinationMediaPackageSettingArgs]]]
    ]: ...
    @media_package_settings.setter
    def media_package_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelDestinationMediaPackageSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiplexSettings")
    def multiplex_settings(
        self,
    ) -> Optional[pulumi.Input[ChannelDestinationMultiplexSettingsArgs]]: ...
    @multiplex_settings.setter
    def multiplex_settings(
        self, value: Optional[pulumi.Input[ChannelDestinationMultiplexSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ChannelDestinationSettingArgs]]]
    ]: ...
    @settings.setter
    def settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelDestinationSettingArgs]]]
        ],
    ): ...

class ChannelDestinationMediaPackageSettingArgsDict(TypedDict):
    channel_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelDestinationMediaPackageSettingArgs:
    def __init__(__self__, *, channel_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[_builtins.str]: ...
    @channel_id.setter
    def channel_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelDestinationMultiplexSettingsArgsDict(TypedDict):
    multiplex_id: pulumi.Input[_builtins.str]
    program_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelDestinationMultiplexSettingsArgs:
    def __init__(
        __self__,
        *,
        multiplex_id: pulumi.Input[_builtins.str],
        program_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiplexId")
    def multiplex_id(self) -> pulumi.Input[_builtins.str]: ...
    @multiplex_id.setter
    def multiplex_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="programName")
    def program_name(self) -> pulumi.Input[_builtins.str]: ...
    @program_name.setter
    def program_name(self, value: pulumi.Input[_builtins.str]): ...

class ChannelDestinationSettingArgsDict(TypedDict):
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    stream_name: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelDestinationSettingArgs:
    def __init__(
        __self__,
        *,
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_name.setter
    def stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsArgsDict(TypedDict):
    output_groups: pulumi.Input[
        Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupArgsDict]]
    ]
    timecode_config: pulumi.Input[ChannelEncoderSettingsTimecodeConfigArgsDict]
    audio_descriptions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsAudioDescriptionArgsDict]]
        ]
    ]
    avail_blanking: NotRequired[
        pulumi.Input[ChannelEncoderSettingsAvailBlankingArgsDict]
    ]
    caption_descriptions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsCaptionDescriptionArgsDict]]
        ]
    ]
    global_configuration: NotRequired[
        pulumi.Input[ChannelEncoderSettingsGlobalConfigurationArgsDict]
    ]
    motion_graphics_configuration: NotRequired[
        pulumi.Input[ChannelEncoderSettingsMotionGraphicsConfigurationArgsDict]
    ]
    nielsen_configuration: NotRequired[
        pulumi.Input[ChannelEncoderSettingsNielsenConfigurationArgsDict]
    ]
    video_descriptions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsVideoDescriptionArgsDict]]
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsArgs:
    def __init__(
        __self__,
        *,
        output_groups: pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupArgs]]
        ],
        timecode_config: pulumi.Input[ChannelEncoderSettingsTimecodeConfigArgs],
        audio_descriptions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsAudioDescriptionArgs]]
            ]
        ] = ...,
        avail_blanking: Optional[
            pulumi.Input[ChannelEncoderSettingsAvailBlankingArgs]
        ] = ...,
        caption_descriptions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsCaptionDescriptionArgs]]
            ]
        ] = ...,
        global_configuration: Optional[
            pulumi.Input[ChannelEncoderSettingsGlobalConfigurationArgs]
        ] = ...,
        motion_graphics_configuration: Optional[
            pulumi.Input[ChannelEncoderSettingsMotionGraphicsConfigurationArgs]
        ] = ...,
        nielsen_configuration: Optional[
            pulumi.Input[ChannelEncoderSettingsNielsenConfigurationArgs]
        ] = ...,
        video_descriptions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsVideoDescriptionArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputGroups")
    def output_groups(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupArgs]]
    ]: ...
    @output_groups.setter
    def output_groups(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timecodeConfig")
    def timecode_config(
        self,
    ) -> pulumi.Input[ChannelEncoderSettingsTimecodeConfigArgs]: ...
    @timecode_config.setter
    def timecode_config(
        self, value: pulumi.Input[ChannelEncoderSettingsTimecodeConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioDescriptions")
    def audio_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ChannelEncoderSettingsAudioDescriptionArgs]]]
    ]: ...
    @audio_descriptions.setter
    def audio_descriptions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsAudioDescriptionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="availBlanking")
    def avail_blanking(
        self,
    ) -> Optional[pulumi.Input[ChannelEncoderSettingsAvailBlankingArgs]]: ...
    @avail_blanking.setter
    def avail_blanking(
        self, value: Optional[pulumi.Input[ChannelEncoderSettingsAvailBlankingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="captionDescriptions")
    def caption_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsCaptionDescriptionArgs]]
        ]
    ]: ...
    @caption_descriptions.setter
    def caption_descriptions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsCaptionDescriptionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalConfiguration")
    def global_configuration(
        self,
    ) -> Optional[pulumi.Input[ChannelEncoderSettingsGlobalConfigurationArgs]]: ...
    @global_configuration.setter
    def global_configuration(
        self,
        value: Optional[pulumi.Input[ChannelEncoderSettingsGlobalConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsConfiguration")
    def motion_graphics_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsMotionGraphicsConfigurationArgs]
    ]: ...
    @motion_graphics_configuration.setter
    def motion_graphics_configuration(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsMotionGraphicsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nielsenConfiguration")
    def nielsen_configuration(
        self,
    ) -> Optional[pulumi.Input[ChannelEncoderSettingsNielsenConfigurationArgs]]: ...
    @nielsen_configuration.setter
    def nielsen_configuration(
        self,
        value: Optional[pulumi.Input[ChannelEncoderSettingsNielsenConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="videoDescriptions")
    def video_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ChannelEncoderSettingsVideoDescriptionArgs]]]
    ]: ...
    @video_descriptions.setter
    def video_descriptions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ChannelEncoderSettingsVideoDescriptionArgs]]
            ]
        ],
    ): ...

class ChannelEncoderSettingsAudioDescriptionArgsDict(TypedDict):
    audio_selector_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    audio_normalization_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgsDict
        ]
    ]
    audio_type: NotRequired[pulumi.Input[_builtins.str]]
    audio_type_control: NotRequired[pulumi.Input[_builtins.str]]
    audio_watermark_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgsDict
        ]
    ]
    codec_settings: NotRequired[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsArgsDict]
    ]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    language_code_control: NotRequired[pulumi.Input[_builtins.str]]
    remix_settings: NotRequired[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionRemixSettingsArgsDict]
    ]
    stream_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionArgs:
    def __init__(
        __self__,
        *,
        audio_selector_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        audio_normalization_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgs
            ]
        ] = ...,
        audio_type: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_type_control: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_watermark_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgs
            ]
        ] = ...,
        codec_settings: Optional[
            pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code_control: Optional[pulumi.Input[_builtins.str]] = ...,
        remix_settings: Optional[
            pulumi.Input[ChannelEncoderSettingsAudioDescriptionRemixSettingsArgs]
        ] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectorName")
    def audio_selector_name(self) -> pulumi.Input[_builtins.str]: ...
    @audio_selector_name.setter
    def audio_selector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="audioNormalizationSettings")
    def audio_normalization_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgs
        ]
    ]: ...
    @audio_normalization_settings.setter
    def audio_normalization_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioType")
    def audio_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_type.setter
    def audio_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioTypeControl")
    def audio_type_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_type_control.setter
    def audio_type_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioWatermarkSettings")
    def audio_watermark_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgs]
    ]: ...
    @audio_watermark_settings.setter
    def audio_watermark_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codecSettings")
    def codec_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsArgs]
    ]: ...
    @codec_settings.setter
    def codec_settings(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageCodeControl")
    def language_code_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code_control.setter
    def language_code_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remixSettings")
    def remix_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionRemixSettingsArgs]
    ]: ...
    @remix_settings.setter
    def remix_settings(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsAudioDescriptionRemixSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_name.setter
    def stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgsDict(
    TypedDict
):
    algorithm: NotRequired[pulumi.Input[_builtins.str]]
    algorithm_control: NotRequired[pulumi.Input[_builtins.str]]
    target_lkfs: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettingsArgs:
    def __init__(
        __self__,
        *,
        algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        algorithm_control: Optional[pulumi.Input[_builtins.str]] = ...,
        target_lkfs: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="algorithmControl")
    def algorithm_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @algorithm_control.setter
    def algorithm_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetLkfs")
    def target_lkfs(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_lkfs.setter
    def target_lkfs(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgsDict(TypedDict):
    nielsen_watermarks_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsArgs:
    def __init__(
        __self__,
        *,
        nielsen_watermarks_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nielsenWatermarksSettings")
    def nielsen_watermarks_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgs
        ]
    ]: ...
    @nielsen_watermarks_settings.setter
    def nielsen_watermarks_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgsDict(
    TypedDict
):
    nielsen_cbet_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgsDict
        ]
    ]
    nielsen_distribution_type: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_naes_ii_nw_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsArgs:
    def __init__(
        __self__,
        *,
        nielsen_cbet_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgs
            ]
        ] = ...,
        nielsen_distribution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_naes_ii_nw_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nielsenCbetSettings")
    def nielsen_cbet_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgs
        ]
    ]: ...
    @nielsen_cbet_settings.setter
    def nielsen_cbet_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nielsenDistributionType")
    def nielsen_distribution_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_distribution_type.setter
    def nielsen_distribution_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nielsenNaesIiNwSettings")
    def nielsen_naes_ii_nw_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgs
                ]
            ]
        ]
    ]: ...
    @nielsen_naes_ii_nw_settings.setter
    def nielsen_naes_ii_nw_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgs
                    ]
                ]
            ]
        ],
    ): ...

class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgsDict(
    TypedDict
):
    cbet_check_digit_string: pulumi.Input[_builtins.str]
    cbet_stepaside: pulumi.Input[_builtins.str]
    csid: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettingsArgs:
    def __init__(
        __self__,
        *,
        cbet_check_digit_string: pulumi.Input[_builtins.str],
        cbet_stepaside: pulumi.Input[_builtins.str],
        csid: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cbetCheckDigitString")
    def cbet_check_digit_string(self) -> pulumi.Input[_builtins.str]: ...
    @cbet_check_digit_string.setter
    def cbet_check_digit_string(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cbetStepaside")
    def cbet_stepaside(self) -> pulumi.Input[_builtins.str]: ...
    @cbet_stepaside.setter
    def cbet_stepaside(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def csid(self) -> pulumi.Input[_builtins.str]: ...
    @csid.setter
    def csid(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgsDict(
    TypedDict
):
    check_digit_string: pulumi.Input[_builtins.str]
    sid: pulumi.Input[_builtins.float]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSettingArgs:
    def __init__(
        __self__,
        *,
        check_digit_string: pulumi.Input[_builtins.str],
        sid: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkDigitString")
    def check_digit_string(self) -> pulumi.Input[_builtins.str]: ...
    @check_digit_string.setter
    def check_digit_string(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> pulumi.Input[_builtins.float]: ...
    @sid.setter
    def sid(self, value: pulumi.Input[_builtins.float]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsArgsDict(TypedDict):
    aac_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgsDict
        ]
    ]
    ac3_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgsDict
        ]
    ]
    eac3_atmos_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgsDict
        ]
    ]
    eac3_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgsDict
        ]
    ]
    mp2_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgsDict
        ]
    ]
    pass_through_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgsDict
        ]
    ]
    wav_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsArgs:
    def __init__(
        __self__,
        *,
        aac_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgs
            ]
        ] = ...,
        ac3_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgs
            ]
        ] = ...,
        eac3_atmos_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgs
            ]
        ] = ...,
        eac3_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgs
            ]
        ] = ...,
        mp2_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgs
            ]
        ] = ...,
        pass_through_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgs
            ]
        ] = ...,
        wav_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aacSettings")
    def aac_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgs]
    ]: ...
    @aac_settings.setter
    def aac_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ac3Settings")
    def ac3_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgs]
    ]: ...
    @ac3_settings.setter
    def ac3_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eac3AtmosSettings")
    def eac3_atmos_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgs
        ]
    ]: ...
    @eac3_atmos_settings.setter
    def eac3_atmos_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eac3Settings")
    def eac3_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgs
        ]
    ]: ...
    @eac3_settings.setter
    def eac3_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mp2Settings")
    def mp2_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgs]
    ]: ...
    @mp2_settings.setter
    def mp2_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="passThroughSettings")
    def pass_through_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgs
        ]
    ]: ...
    @pass_through_settings.setter
    def pass_through_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wavSettings")
    def wav_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgs]
    ]: ...
    @wav_settings.setter
    def wav_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgsDict(TypedDict):
    bitrate: NotRequired[pulumi.Input[_builtins.float]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    input_type: NotRequired[pulumi.Input[_builtins.str]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    rate_control_mode: NotRequired[pulumi.Input[_builtins.str]]
    raw_format: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate: NotRequired[pulumi.Input[_builtins.float]]
    spec: NotRequired[pulumi.Input[_builtins.str]]
    vbr_quality: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettingsArgs:
    def __init__(
        __self__,
        *,
        bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        input_type: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_control_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        raw_format: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        spec: Optional[pulumi.Input[_builtins.str]] = ...,
        vbr_quality: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputType")
    def input_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_type.setter
    def input_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rate_control_mode.setter
    def rate_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rawFormat")
    def raw_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @raw_format.setter
    def raw_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vbrQuality")
    def vbr_quality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vbr_quality.setter
    def vbr_quality(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgsDict(TypedDict):
    bitrate: NotRequired[pulumi.Input[_builtins.float]]
    bitstream_mode: NotRequired[pulumi.Input[_builtins.str]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    dialnorm: NotRequired[pulumi.Input[_builtins.int]]
    drc_profile: NotRequired[pulumi.Input[_builtins.str]]
    lfe_filter: NotRequired[pulumi.Input[_builtins.str]]
    metadata_control: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3SettingsArgs:
    def __init__(
        __self__,
        *,
        bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        bitstream_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dialnorm: Optional[pulumi.Input[_builtins.int]] = ...,
        drc_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        lfe_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_control: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="bitstreamMode")
    def bitstream_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bitstream_mode.setter
    def bitstream_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dialnorm.setter
    def dialnorm(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="drcProfile")
    def drc_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drc_profile.setter
    def drc_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lfeFilter")
    def lfe_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lfe_filter.setter
    def lfe_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataControl")
    def metadata_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_control.setter
    def metadata_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgsDict(
    TypedDict
):
    bitrate: NotRequired[pulumi.Input[_builtins.float]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    dialnorm: NotRequired[pulumi.Input[_builtins.float]]
    drc_line: NotRequired[pulumi.Input[_builtins.str]]
    drc_rf: NotRequired[pulumi.Input[_builtins.str]]
    height_trim: NotRequired[pulumi.Input[_builtins.float]]
    surround_trim: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettingsArgs:
    def __init__(
        __self__,
        *,
        bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dialnorm: Optional[pulumi.Input[_builtins.float]] = ...,
        drc_line: Optional[pulumi.Input[_builtins.str]] = ...,
        drc_rf: Optional[pulumi.Input[_builtins.str]] = ...,
        height_trim: Optional[pulumi.Input[_builtins.float]] = ...,
        surround_trim: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @dialnorm.setter
    def dialnorm(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="drcLine")
    def drc_line(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drc_line.setter
    def drc_line(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="drcRf")
    def drc_rf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drc_rf.setter
    def drc_rf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="heightTrim")
    def height_trim(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @height_trim.setter
    def height_trim(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="surroundTrim")
    def surround_trim(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @surround_trim.setter
    def surround_trim(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgsDict(
    TypedDict
):
    attenuation_control: NotRequired[pulumi.Input[_builtins.str]]
    bitrate: NotRequired[pulumi.Input[_builtins.float]]
    bitstream_mode: NotRequired[pulumi.Input[_builtins.str]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    dc_filter: NotRequired[pulumi.Input[_builtins.str]]
    dialnorm: NotRequired[pulumi.Input[_builtins.int]]
    drc_line: NotRequired[pulumi.Input[_builtins.str]]
    drc_rf: NotRequired[pulumi.Input[_builtins.str]]
    lfe_control: NotRequired[pulumi.Input[_builtins.str]]
    lfe_filter: NotRequired[pulumi.Input[_builtins.str]]
    lo_ro_center_mix_level: NotRequired[pulumi.Input[_builtins.float]]
    lo_ro_surround_mix_level: NotRequired[pulumi.Input[_builtins.float]]
    lt_rt_center_mix_level: NotRequired[pulumi.Input[_builtins.float]]
    lt_rt_surround_mix_level: NotRequired[pulumi.Input[_builtins.float]]
    metadata_control: NotRequired[pulumi.Input[_builtins.str]]
    passthrough_control: NotRequired[pulumi.Input[_builtins.str]]
    phase_control: NotRequired[pulumi.Input[_builtins.str]]
    stereo_downmix: NotRequired[pulumi.Input[_builtins.str]]
    surround_ex_mode: NotRequired[pulumi.Input[_builtins.str]]
    surround_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3SettingsArgs:
    def __init__(
        __self__,
        *,
        attenuation_control: Optional[pulumi.Input[_builtins.str]] = ...,
        bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        bitstream_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        dc_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        dialnorm: Optional[pulumi.Input[_builtins.int]] = ...,
        drc_line: Optional[pulumi.Input[_builtins.str]] = ...,
        drc_rf: Optional[pulumi.Input[_builtins.str]] = ...,
        lfe_control: Optional[pulumi.Input[_builtins.str]] = ...,
        lfe_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        lo_ro_center_mix_level: Optional[pulumi.Input[_builtins.float]] = ...,
        lo_ro_surround_mix_level: Optional[pulumi.Input[_builtins.float]] = ...,
        lt_rt_center_mix_level: Optional[pulumi.Input[_builtins.float]] = ...,
        lt_rt_surround_mix_level: Optional[pulumi.Input[_builtins.float]] = ...,
        metadata_control: Optional[pulumi.Input[_builtins.str]] = ...,
        passthrough_control: Optional[pulumi.Input[_builtins.str]] = ...,
        phase_control: Optional[pulumi.Input[_builtins.str]] = ...,
        stereo_downmix: Optional[pulumi.Input[_builtins.str]] = ...,
        surround_ex_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        surround_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attenuationControl")
    def attenuation_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attenuation_control.setter
    def attenuation_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="bitstreamMode")
    def bitstream_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bitstream_mode.setter
    def bitstream_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dcFilter")
    def dc_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dc_filter.setter
    def dc_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dialnorm.setter
    def dialnorm(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="drcLine")
    def drc_line(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drc_line.setter
    def drc_line(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="drcRf")
    def drc_rf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drc_rf.setter
    def drc_rf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lfeControl")
    def lfe_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lfe_control.setter
    def lfe_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lfeFilter")
    def lfe_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lfe_filter.setter
    def lfe_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loRoCenterMixLevel")
    def lo_ro_center_mix_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lo_ro_center_mix_level.setter
    def lo_ro_center_mix_level(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loRoSurroundMixLevel")
    def lo_ro_surround_mix_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lo_ro_surround_mix_level.setter
    def lo_ro_surround_mix_level(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ltRtCenterMixLevel")
    def lt_rt_center_mix_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lt_rt_center_mix_level.setter
    def lt_rt_center_mix_level(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ltRtSurroundMixLevel")
    def lt_rt_surround_mix_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lt_rt_surround_mix_level.setter
    def lt_rt_surround_mix_level(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metadataControl")
    def metadata_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_control.setter
    def metadata_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passthroughControl")
    def passthrough_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passthrough_control.setter
    def passthrough_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phaseControl")
    def phase_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phase_control.setter
    def phase_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stereoDownmix")
    def stereo_downmix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stereo_downmix.setter
    def stereo_downmix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="surroundExMode")
    def surround_ex_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @surround_ex_mode.setter
    def surround_ex_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="surroundMode")
    def surround_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @surround_mode.setter
    def surround_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgsDict(TypedDict):
    bitrate: NotRequired[pulumi.Input[_builtins.float]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2SettingsArgs:
    def __init__(
        __self__,
        *,
        bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgsDict(TypedDict):
    bit_depth: NotRequired[pulumi.Input[_builtins.float]]
    coding_mode: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettingsArgs:
    def __init__(
        __self__,
        *,
        bit_depth: Optional[pulumi.Input[_builtins.float]] = ...,
        coding_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitDepth")
    def bit_depth(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bit_depth.setter
    def bit_depth(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coding_mode.setter
    def coding_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ChannelEncoderSettingsAudioDescriptionRemixSettingsArgsDict(TypedDict):
    channel_mappings: pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgsDict
            ]
        ]
    ]
    channels_in: NotRequired[pulumi.Input[_builtins.int]]
    channels_out: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionRemixSettingsArgs:
    def __init__(
        __self__,
        *,
        channel_mappings: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgs
                ]
            ]
        ],
        channels_in: Optional[pulumi.Input[_builtins.int]] = ...,
        channels_out: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelMappings")
    def channel_mappings(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgs
            ]
        ]
    ]: ...
    @channel_mappings.setter
    def channel_mappings(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="channelsIn")
    def channels_in(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @channels_in.setter
    def channels_in(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="channelsOut")
    def channels_out(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @channels_out.setter
    def channels_out(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgsDict(
    TypedDict
):
    input_channel_levels: pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgsDict
            ]
        ]
    ]
    output_channel: pulumi.Input[_builtins.int]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingArgs:
    def __init__(
        __self__,
        *,
        input_channel_levels: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgs
                ]
            ]
        ],
        output_channel: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputChannelLevels")
    def input_channel_levels(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgs
            ]
        ]
    ]: ...
    @input_channel_levels.setter
    def input_channel_levels(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputChannel")
    def output_channel(self) -> pulumi.Input[_builtins.int]: ...
    @output_channel.setter
    def output_channel(self, value: pulumi.Input[_builtins.int]): ...

class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgsDict(
    TypedDict
):
    gain: pulumi.Input[_builtins.int]
    input_channel: pulumi.Input[_builtins.int]

@pulumi.input_type
class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevelArgs:
    def __init__(
        __self__,
        *,
        gain: pulumi.Input[_builtins.int],
        input_channel: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gain(self) -> pulumi.Input[_builtins.int]: ...
    @gain.setter
    def gain(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="inputChannel")
    def input_channel(self) -> pulumi.Input[_builtins.int]: ...
    @input_channel.setter
    def input_channel(self, value: pulumi.Input[_builtins.int]): ...

class ChannelEncoderSettingsAvailBlankingArgsDict(TypedDict):
    avail_blanking_image: NotRequired[
        pulumi.Input[ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgsDict]
    ]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAvailBlankingArgs:
    def __init__(
        __self__,
        *,
        avail_blanking_image: Optional[
            pulumi.Input[ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availBlankingImage")
    def avail_blanking_image(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgs]
    ]: ...
    @avail_blanking_image.setter
    def avail_blanking_image(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsAvailBlankingAvailBlankingImageArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsCaptionDescriptionArgsDict(TypedDict):
    caption_selector_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    accessibility: NotRequired[pulumi.Input[_builtins.str]]
    destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgsDict
        ]
    ]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    language_description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionArgs:
    def __init__(
        __self__,
        *,
        caption_selector_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        accessibility: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgs
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        language_description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captionSelectorName")
    def caption_selector_name(self) -> pulumi.Input[_builtins.str]: ...
    @caption_selector_name.setter
    def caption_selector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def accessibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accessibility.setter
    def accessibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationSettings")
    def destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgs]
    ]: ...
    @destination_settings.setter
    def destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageDescription")
    def language_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_description.setter
    def language_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgsDict(TypedDict):
    arib_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgsDict
        ]
    ]
    burn_in_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgsDict
        ]
    ]
    dvb_sub_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgsDict
        ]
    ]
    ebu_tt_d_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgsDict
        ]
    ]
    embedded_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgsDict
        ]
    ]
    embedded_plus_scte20_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgsDict
        ]
    ]
    rtmp_caption_info_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgsDict
        ]
    ]
    scte20_plus_embedded_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgsDict
        ]
    ]
    scte27_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgsDict
        ]
    ]
    smpte_tt_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgsDict
        ]
    ]
    teletext_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgsDict
        ]
    ]
    ttml_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgsDict
        ]
    ]
    webvtt_destination_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsArgs:
    def __init__(
        __self__,
        *,
        arib_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgs
            ]
        ] = ...,
        burn_in_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgs
            ]
        ] = ...,
        dvb_sub_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgs
            ]
        ] = ...,
        ebu_tt_d_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgs
            ]
        ] = ...,
        embedded_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgs
            ]
        ] = ...,
        embedded_plus_scte20_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgs
            ]
        ] = ...,
        rtmp_caption_info_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgs
            ]
        ] = ...,
        scte20_plus_embedded_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgs
            ]
        ] = ...,
        scte27_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgs
            ]
        ] = ...,
        smpte_tt_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgs
            ]
        ] = ...,
        teletext_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgs
            ]
        ] = ...,
        ttml_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgs
            ]
        ] = ...,
        webvtt_destination_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aribDestinationSettings")
    def arib_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgs
        ]
    ]: ...
    @arib_destination_settings.setter
    def arib_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="burnInDestinationSettings")
    def burn_in_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgs
        ]
    ]: ...
    @burn_in_destination_settings.setter
    def burn_in_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSubDestinationSettings")
    def dvb_sub_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgs
        ]
    ]: ...
    @dvb_sub_destination_settings.setter
    def dvb_sub_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebuTtDDestinationSettings")
    def ebu_tt_d_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgs
        ]
    ]: ...
    @ebu_tt_d_destination_settings.setter
    def ebu_tt_d_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="embeddedDestinationSettings")
    def embedded_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgs
        ]
    ]: ...
    @embedded_destination_settings.setter
    def embedded_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="embeddedPlusScte20DestinationSettings")
    def embedded_plus_scte20_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgs
        ]
    ]: ...
    @embedded_plus_scte20_destination_settings.setter
    def embedded_plus_scte20_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rtmpCaptionInfoDestinationSettings")
    def rtmp_caption_info_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgs
        ]
    ]: ...
    @rtmp_caption_info_destination_settings.setter
    def rtmp_caption_info_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scte20PlusEmbeddedDestinationSettings")
    def scte20_plus_embedded_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgs
        ]
    ]: ...
    @scte20_plus_embedded_destination_settings.setter
    def scte20_plus_embedded_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scte27DestinationSettings")
    def scte27_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgs
        ]
    ]: ...
    @scte27_destination_settings.setter
    def scte27_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="smpteTtDestinationSettings")
    def smpte_tt_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgs
        ]
    ]: ...
    @smpte_tt_destination_settings.setter
    def smpte_tt_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="teletextDestinationSettings")
    def teletext_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgs
        ]
    ]: ...
    @teletext_destination_settings.setter
    def teletext_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ttmlDestinationSettings")
    def ttml_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgs
        ]
    ]: ...
    @ttml_destination_settings.setter
    def ttml_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webvttDestinationSettings")
    def webvtt_destination_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgs
        ]
    ]: ...
    @webvtt_destination_settings.setter
    def webvtt_destination_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgsDict(
    TypedDict
):
    outline_color: pulumi.Input[_builtins.str]
    teletext_grid_control: pulumi.Input[_builtins.str]
    alignment: NotRequired[pulumi.Input[_builtins.str]]
    background_color: NotRequired[pulumi.Input[_builtins.str]]
    background_opacity: NotRequired[pulumi.Input[_builtins.int]]
    font: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgsDict
        ]
    ]
    font_color: NotRequired[pulumi.Input[_builtins.str]]
    font_opacity: NotRequired[pulumi.Input[_builtins.int]]
    font_resolution: NotRequired[pulumi.Input[_builtins.int]]
    font_size: NotRequired[pulumi.Input[_builtins.str]]
    outline_size: NotRequired[pulumi.Input[_builtins.int]]
    shadow_color: NotRequired[pulumi.Input[_builtins.str]]
    shadow_opacity: NotRequired[pulumi.Input[_builtins.int]]
    shadow_x_offset: NotRequired[pulumi.Input[_builtins.int]]
    shadow_y_offset: NotRequired[pulumi.Input[_builtins.int]]
    x_position: NotRequired[pulumi.Input[_builtins.int]]
    y_position: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsArgs:
    def __init__(
        __self__,
        *,
        outline_color: pulumi.Input[_builtins.str],
        teletext_grid_control: pulumi.Input[_builtins.str],
        alignment: Optional[pulumi.Input[_builtins.str]] = ...,
        background_color: Optional[pulumi.Input[_builtins.str]] = ...,
        background_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        font: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgs
            ]
        ] = ...,
        font_color: Optional[pulumi.Input[_builtins.str]] = ...,
        font_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        font_resolution: Optional[pulumi.Input[_builtins.int]] = ...,
        font_size: Optional[pulumi.Input[_builtins.str]] = ...,
        outline_size: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_color: Optional[pulumi.Input[_builtins.str]] = ...,
        shadow_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_x_offset: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_y_offset: Optional[pulumi.Input[_builtins.int]] = ...,
        x_position: Optional[pulumi.Input[_builtins.int]] = ...,
        y_position: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outlineColor")
    def outline_color(self) -> pulumi.Input[_builtins.str]: ...
    @outline_color.setter
    def outline_color(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="teletextGridControl")
    def teletext_grid_control(self) -> pulumi.Input[_builtins.str]: ...
    @teletext_grid_control.setter
    def teletext_grid_control(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def alignment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alignment.setter
    def alignment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backgroundColor")
    def background_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @background_color.setter
    def background_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backgroundOpacity")
    def background_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @background_opacity.setter
    def background_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def font(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgs
        ]
    ]: ...
    @font.setter
    def font(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fontColor")
    def font_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_color.setter
    def font_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fontOpacity")
    def font_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @font_opacity.setter
    def font_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fontResolution")
    def font_resolution(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @font_resolution.setter
    def font_resolution(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_size.setter
    def font_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outlineSize")
    def outline_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @outline_size.setter
    def outline_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowColor")
    def shadow_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shadow_color.setter
    def shadow_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowOpacity")
    def shadow_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_opacity.setter
    def shadow_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowXOffset")
    def shadow_x_offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_x_offset.setter
    def shadow_x_offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowYOffset")
    def shadow_y_offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_y_offset.setter
    def shadow_y_offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="xPosition")
    def x_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @x_position.setter
    def x_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="yPosition")
    def y_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @y_position.setter
    def y_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFontArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgsDict(
    TypedDict
):
    alignment: NotRequired[pulumi.Input[_builtins.str]]
    background_color: NotRequired[pulumi.Input[_builtins.str]]
    background_opacity: NotRequired[pulumi.Input[_builtins.int]]
    font: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgsDict
        ]
    ]
    font_color: NotRequired[pulumi.Input[_builtins.str]]
    font_opacity: NotRequired[pulumi.Input[_builtins.int]]
    font_resolution: NotRequired[pulumi.Input[_builtins.int]]
    font_size: NotRequired[pulumi.Input[_builtins.str]]
    outline_color: NotRequired[pulumi.Input[_builtins.str]]
    outline_size: NotRequired[pulumi.Input[_builtins.int]]
    shadow_color: NotRequired[pulumi.Input[_builtins.str]]
    shadow_opacity: NotRequired[pulumi.Input[_builtins.int]]
    shadow_x_offset: NotRequired[pulumi.Input[_builtins.int]]
    shadow_y_offset: NotRequired[pulumi.Input[_builtins.int]]
    teletext_grid_control: NotRequired[pulumi.Input[_builtins.str]]
    x_position: NotRequired[pulumi.Input[_builtins.int]]
    y_position: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsArgs:
    def __init__(
        __self__,
        *,
        alignment: Optional[pulumi.Input[_builtins.str]] = ...,
        background_color: Optional[pulumi.Input[_builtins.str]] = ...,
        background_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        font: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgs
            ]
        ] = ...,
        font_color: Optional[pulumi.Input[_builtins.str]] = ...,
        font_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        font_resolution: Optional[pulumi.Input[_builtins.int]] = ...,
        font_size: Optional[pulumi.Input[_builtins.str]] = ...,
        outline_color: Optional[pulumi.Input[_builtins.str]] = ...,
        outline_size: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_color: Optional[pulumi.Input[_builtins.str]] = ...,
        shadow_opacity: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_x_offset: Optional[pulumi.Input[_builtins.int]] = ...,
        shadow_y_offset: Optional[pulumi.Input[_builtins.int]] = ...,
        teletext_grid_control: Optional[pulumi.Input[_builtins.str]] = ...,
        x_position: Optional[pulumi.Input[_builtins.int]] = ...,
        y_position: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alignment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alignment.setter
    def alignment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backgroundColor")
    def background_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @background_color.setter
    def background_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backgroundOpacity")
    def background_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @background_opacity.setter
    def background_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def font(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgs
        ]
    ]: ...
    @font.setter
    def font(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fontColor")
    def font_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_color.setter
    def font_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fontOpacity")
    def font_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @font_opacity.setter
    def font_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fontResolution")
    def font_resolution(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @font_resolution.setter
    def font_resolution(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_size.setter
    def font_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outlineColor")
    def outline_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outline_color.setter
    def outline_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outlineSize")
    def outline_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @outline_size.setter
    def outline_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowColor")
    def shadow_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shadow_color.setter
    def shadow_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowOpacity")
    def shadow_opacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_opacity.setter
    def shadow_opacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowXOffset")
    def shadow_x_offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_x_offset.setter
    def shadow_x_offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shadowYOffset")
    def shadow_y_offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shadow_y_offset.setter
    def shadow_y_offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="teletextGridControl")
    def teletext_grid_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @teletext_grid_control.setter
    def teletext_grid_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="xPosition")
    def x_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @x_position.setter
    def x_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="yPosition")
    def y_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @y_position.setter
    def y_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFontArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgsDict(
    TypedDict
):
    copyright_holder: NotRequired[pulumi.Input[_builtins.str]]
    fill_line_gap: NotRequired[pulumi.Input[_builtins.str]]
    font_family: NotRequired[pulumi.Input[_builtins.str]]
    style_control: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettingsArgs:
    def __init__(
        __self__,
        *,
        copyright_holder: Optional[pulumi.Input[_builtins.str]] = ...,
        fill_line_gap: Optional[pulumi.Input[_builtins.str]] = ...,
        font_family: Optional[pulumi.Input[_builtins.str]] = ...,
        style_control: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyrightHolder")
    def copyright_holder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copyright_holder.setter
    def copyright_holder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fillLineGap")
    def fill_line_gap(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fill_line_gap.setter
    def fill_line_gap(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fontFamily")
    def font_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_family.setter
    def font_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @style_control.setter
    def style_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgsDict(
    TypedDict
):
    style_control: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettingsArgs:
    def __init__(__self__, *, style_control: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> pulumi.Input[_builtins.str]: ...
    @style_control.setter
    def style_control(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgsDict(
    TypedDict
):
    style_control: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettingsArgs:
    def __init__(__self__, *, style_control: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> pulumi.Input[_builtins.str]: ...
    @style_control.setter
    def style_control(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsGlobalConfigurationArgsDict(TypedDict):
    initial_audio_gain: NotRequired[pulumi.Input[_builtins.int]]
    input_end_action: NotRequired[pulumi.Input[_builtins.str]]
    input_loss_behavior: NotRequired[
        pulumi.Input[ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgsDict]
    ]
    output_locking_mode: NotRequired[pulumi.Input[_builtins.str]]
    output_timing_source: NotRequired[pulumi.Input[_builtins.str]]
    support_low_framerate_inputs: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsGlobalConfigurationArgs:
    def __init__(
        __self__,
        *,
        initial_audio_gain: Optional[pulumi.Input[_builtins.int]] = ...,
        input_end_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_loss_behavior: Optional[
            pulumi.Input[ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs]
        ] = ...,
        output_locking_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        output_timing_source: Optional[pulumi.Input[_builtins.str]] = ...,
        support_low_framerate_inputs: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialAudioGain")
    def initial_audio_gain(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_audio_gain.setter
    def initial_audio_gain(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEndAction")
    def input_end_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_end_action.setter
    def input_end_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossBehavior")
    def input_loss_behavior(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs]
    ]: ...
    @input_loss_behavior.setter
    def input_loss_behavior(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputLockingMode")
    def output_locking_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_locking_mode.setter
    def output_locking_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputTimingSource")
    def output_timing_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_timing_source.setter
    def output_timing_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportLowFramerateInputs")
    def support_low_framerate_inputs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @support_low_framerate_inputs.setter
    def support_low_framerate_inputs(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgsDict(TypedDict):
    black_frame_msec: NotRequired[pulumi.Input[_builtins.int]]
    input_loss_image_color: NotRequired[pulumi.Input[_builtins.str]]
    input_loss_image_slate: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgsDict
        ]
    ]
    input_loss_image_type: NotRequired[pulumi.Input[_builtins.str]]
    repeat_frame_msec: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs:
    def __init__(
        __self__,
        *,
        black_frame_msec: Optional[pulumi.Input[_builtins.int]] = ...,
        input_loss_image_color: Optional[pulumi.Input[_builtins.str]] = ...,
        input_loss_image_slate: Optional[
            pulumi.Input[
                ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs
            ]
        ] = ...,
        input_loss_image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        repeat_frame_msec: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blackFrameMsec")
    def black_frame_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @black_frame_msec.setter
    def black_frame_msec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageColor")
    def input_loss_image_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_image_color.setter
    def input_loss_image_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageSlate")
    def input_loss_image_slate(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs
        ]
    ]: ...
    @input_loss_image_slate.setter
    def input_loss_image_slate(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageType")
    def input_loss_image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_image_type.setter
    def input_loss_image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repeatFrameMsec")
    def repeat_frame_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @repeat_frame_msec.setter
    def repeat_frame_msec(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsMotionGraphicsConfigurationArgsDict(TypedDict):
    motion_graphics_settings: pulumi.Input[
        ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgsDict
    ]
    motion_graphics_insertion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsMotionGraphicsConfigurationArgs:
    def __init__(
        __self__,
        *,
        motion_graphics_settings: pulumi.Input[
            ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgs
        ],
        motion_graphics_insertion: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsSettings")
    def motion_graphics_settings(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgs
    ]: ...
    @motion_graphics_settings.setter
    def motion_graphics_settings(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsInsertion")
    def motion_graphics_insertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @motion_graphics_insertion.setter
    def motion_graphics_insertion(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgsDict(
    TypedDict
):
    html_motion_graphics_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsArgs:
    def __init__(
        __self__,
        *,
        html_motion_graphics_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="htmlMotionGraphicsSettings")
    def html_motion_graphics_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgs
        ]
    ]: ...
    @html_motion_graphics_settings.setter
    def html_motion_graphics_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsNielsenConfigurationArgsDict(TypedDict):
    distributor_id: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_pcm_to_id3_tagging: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsNielsenConfigurationArgs:
    def __init__(
        __self__,
        *,
        distributor_id: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_pcm_to_id3_tagging: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributorId")
    def distributor_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distributor_id.setter
    def distributor_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nielsenPcmToId3Tagging")
    def nielsen_pcm_to_id3_tagging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_pcm_to_id3_tagging.setter
    def nielsen_pcm_to_id3_tagging(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChannelEncoderSettingsOutputGroupArgsDict(TypedDict):
    output_group_settings: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgsDict
    ]
    outputs: pulumi.Input[
        Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupOutputArgsDict]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupArgs:
    def __init__(
        __self__,
        *,
        output_group_settings: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgs
        ],
        outputs: pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupOutputArgs]]
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputGroupSettings")
    def output_group_settings(
        self,
    ) -> pulumi.Input[ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgs]: ...
    @output_group_settings.setter
    def output_group_settings(
        self,
        value: pulumi.Input[ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupOutputArgs]]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ChannelEncoderSettingsOutputGroupOutputArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputArgsDict(TypedDict):
    output_settings: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgsDict
    ]
    audio_description_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    caption_description_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    output_name: NotRequired[pulumi.Input[_builtins.str]]
    video_description_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputArgs:
    def __init__(
        __self__,
        *,
        output_settings: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgs
        ],
        audio_description_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        caption_description_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        output_name: Optional[pulumi.Input[_builtins.str]] = ...,
        video_description_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSettings")
    def output_settings(
        self,
    ) -> pulumi.Input[ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgs]: ...
    @output_settings.setter
    def output_settings(
        self,
        value: pulumi.Input[ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioDescriptionNames")
    def audio_description_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @audio_description_names.setter
    def audio_description_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="captionDescriptionNames")
    def caption_description_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @caption_description_names.setter
    def caption_description_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_name.setter
    def output_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="videoDescriptionName")
    def video_description_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @video_description_name.setter
    def video_description_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgsDict(TypedDict):
    archive_group_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgsDict
                ]
            ]
        ]
    ]
    frame_capture_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgsDict
        ]
    ]
    hls_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgsDict
        ]
    ]
    media_package_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgsDict
        ]
    ]
    ms_smooth_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgsDict
        ]
    ]
    multiplex_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgsDict
        ]
    ]
    rtmp_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgsDict
        ]
    ]
    udp_group_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        archive_group_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgs
                    ]
                ]
            ]
        ] = ...,
        frame_capture_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgs
            ]
        ] = ...,
        hls_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgs
            ]
        ] = ...,
        media_package_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgs
            ]
        ] = ...,
        ms_smooth_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgs
            ]
        ] = ...,
        multiplex_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgs
            ]
        ] = ...,
        rtmp_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgs
            ]
        ] = ...,
        udp_group_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveGroupSettings")
    def archive_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgs
                ]
            ]
        ]
    ]: ...
    @archive_group_settings.setter
    def archive_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureGroupSettings")
    def frame_capture_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgs
        ]
    ]: ...
    @frame_capture_group_settings.setter
    def frame_capture_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsGroupSettings")
    def hls_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgs
        ]
    ]: ...
    @hls_group_settings.setter
    def hls_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageGroupSettings")
    def media_package_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgs
        ]
    ]: ...
    @media_package_group_settings.setter
    def media_package_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="msSmoothGroupSettings")
    def ms_smooth_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgs
        ]
    ]: ...
    @ms_smooth_group_settings.setter
    def ms_smooth_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiplexGroupSettings")
    def multiplex_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgs
        ]
    ]: ...
    @multiplex_group_settings.setter
    def multiplex_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rtmpGroupSettings")
    def rtmp_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgs
        ]
    ]: ...
    @rtmp_group_settings.setter
    def rtmp_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="udpGroupSettings")
    def udp_group_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgs
        ]
    ]: ...
    @udp_group_settings.setter
    def udp_group_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgsDict
    ]
    archive_cdn_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgsDict
        ]
    ]
    rollover_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgs
        ],
        archive_cdn_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgs
            ]
        ] = ...,
        rollover_interval: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="archiveCdnSettings")
    def archive_cdn_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgs
        ]
    ]: ...
    @archive_cdn_settings.setter
    def archive_cdn_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rolloverInterval")
    def rollover_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rollover_interval.setter
    def rollover_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgsDict(
    TypedDict
):
    archive_s3_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArgs:
    def __init__(
        __self__,
        *,
        archive_s3_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveS3Settings")
    def archive_s3_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgs
        ]
    ]: ...
    @archive_s3_settings.setter
    def archive_s3_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgsDict(
    TypedDict
):
    canned_acl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3SettingsArgs:
    def __init__(
        __self__, *, canned_acl: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl.setter
    def canned_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgsDict
    ]
    frame_capture_cdn_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgs
        ],
        frame_capture_cdn_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureCdnSettings")
    def frame_capture_cdn_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgs
        ]
    ]: ...
    @frame_capture_cdn_settings.setter
    def frame_capture_cdn_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgsDict(
    TypedDict
):
    frame_capture_s3_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsArgs:
    def __init__(
        __self__,
        *,
        frame_capture_s3_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureS3Settings")
    def frame_capture_s3_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgs
        ]
    ]: ...
    @frame_capture_s3_settings.setter
    def frame_capture_s3_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgsDict(
    TypedDict
):
    canned_acl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3SettingsArgs:
    def __init__(
        __self__, *, canned_acl: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl.setter
    def canned_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgsDict
    ]
    ad_markers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    base_url_content: NotRequired[pulumi.Input[_builtins.str]]
    base_url_content1: NotRequired[pulumi.Input[_builtins.str]]
    base_url_manifest: NotRequired[pulumi.Input[_builtins.str]]
    base_url_manifest1: NotRequired[pulumi.Input[_builtins.str]]
    caption_language_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgsDict
                ]
            ]
        ]
    ]
    caption_language_setting: NotRequired[pulumi.Input[_builtins.str]]
    client_cache: NotRequired[pulumi.Input[_builtins.str]]
    codec_specification: NotRequired[pulumi.Input[_builtins.str]]
    constant_iv: NotRequired[pulumi.Input[_builtins.str]]
    directory_structure: NotRequired[pulumi.Input[_builtins.str]]
    discontinuity_tags: NotRequired[pulumi.Input[_builtins.str]]
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    hls_cdn_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgsDict
                ]
            ]
        ]
    ]
    hls_id3_segment_tagging: NotRequired[pulumi.Input[_builtins.str]]
    iframe_only_playlists: NotRequired[pulumi.Input[_builtins.str]]
    incomplete_segment_behavior: NotRequired[pulumi.Input[_builtins.str]]
    index_n_segments: NotRequired[pulumi.Input[_builtins.int]]
    input_loss_action: NotRequired[pulumi.Input[_builtins.str]]
    iv_in_manifest: NotRequired[pulumi.Input[_builtins.str]]
    iv_source: NotRequired[pulumi.Input[_builtins.str]]
    keep_segments: NotRequired[pulumi.Input[_builtins.int]]
    key_format: NotRequired[pulumi.Input[_builtins.str]]
    key_format_versions: NotRequired[pulumi.Input[_builtins.str]]
    key_provider_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgsDict
        ]
    ]
    manifest_compression: NotRequired[pulumi.Input[_builtins.str]]
    manifest_duration_format: NotRequired[pulumi.Input[_builtins.str]]
    min_segment_length: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    output_selection: NotRequired[pulumi.Input[_builtins.str]]
    program_date_time: NotRequired[pulumi.Input[_builtins.str]]
    program_date_time_clock: NotRequired[pulumi.Input[_builtins.str]]
    program_date_time_period: NotRequired[pulumi.Input[_builtins.int]]
    redundant_manifest: NotRequired[pulumi.Input[_builtins.str]]
    segment_length: NotRequired[pulumi.Input[_builtins.int]]
    segments_per_subdirectory: NotRequired[pulumi.Input[_builtins.int]]
    stream_inf_resolution: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_id3_frame: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_id3_period: NotRequired[pulumi.Input[_builtins.int]]
    timestamp_delta_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    ts_file_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgs
        ],
        ad_markers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        base_url_content: Optional[pulumi.Input[_builtins.str]] = ...,
        base_url_content1: Optional[pulumi.Input[_builtins.str]] = ...,
        base_url_manifest: Optional[pulumi.Input[_builtins.str]] = ...,
        base_url_manifest1: Optional[pulumi.Input[_builtins.str]] = ...,
        caption_language_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgs
                    ]
                ]
            ]
        ] = ...,
        caption_language_setting: Optional[pulumi.Input[_builtins.str]] = ...,
        client_cache: Optional[pulumi.Input[_builtins.str]] = ...,
        codec_specification: Optional[pulumi.Input[_builtins.str]] = ...,
        constant_iv: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_structure: Optional[pulumi.Input[_builtins.str]] = ...,
        discontinuity_tags: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        hls_cdn_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgs
                    ]
                ]
            ]
        ] = ...,
        hls_id3_segment_tagging: Optional[pulumi.Input[_builtins.str]] = ...,
        iframe_only_playlists: Optional[pulumi.Input[_builtins.str]] = ...,
        incomplete_segment_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        index_n_segments: Optional[pulumi.Input[_builtins.int]] = ...,
        input_loss_action: Optional[pulumi.Input[_builtins.str]] = ...,
        iv_in_manifest: Optional[pulumi.Input[_builtins.str]] = ...,
        iv_source: Optional[pulumi.Input[_builtins.str]] = ...,
        keep_segments: Optional[pulumi.Input[_builtins.int]] = ...,
        key_format: Optional[pulumi.Input[_builtins.str]] = ...,
        key_format_versions: Optional[pulumi.Input[_builtins.str]] = ...,
        key_provider_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgs
            ]
        ] = ...,
        manifest_compression: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_duration_format: Optional[pulumi.Input[_builtins.str]] = ...,
        min_segment_length: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        output_selection: Optional[pulumi.Input[_builtins.str]] = ...,
        program_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        program_date_time_clock: Optional[pulumi.Input[_builtins.str]] = ...,
        program_date_time_period: Optional[pulumi.Input[_builtins.int]] = ...,
        redundant_manifest: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_length: Optional[pulumi.Input[_builtins.int]] = ...,
        segments_per_subdirectory: Optional[pulumi.Input[_builtins.int]] = ...,
        stream_inf_resolution: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_id3_frame: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_id3_period: Optional[pulumi.Input[_builtins.int]] = ...,
        timestamp_delta_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        ts_file_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="adMarkers")
    def ad_markers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ad_markers.setter
    def ad_markers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="baseUrlContent")
    def base_url_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_url_content.setter
    def base_url_content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baseUrlContent1")
    def base_url_content1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_url_content1.setter
    def base_url_content1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baseUrlManifest")
    def base_url_manifest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_url_manifest.setter
    def base_url_manifest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baseUrlManifest1")
    def base_url_manifest1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_url_manifest1.setter
    def base_url_manifest1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="captionLanguageMappings")
    def caption_language_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgs
                ]
            ]
        ]
    ]: ...
    @caption_language_mappings.setter
    def caption_language_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="captionLanguageSetting")
    def caption_language_setting(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @caption_language_setting.setter
    def caption_language_setting(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCache")
    def client_cache(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_cache.setter
    def client_cache(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="codecSpecification")
    def codec_specification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codec_specification.setter
    def codec_specification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="constantIv")
    def constant_iv(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @constant_iv.setter
    def constant_iv(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryStructure")
    def directory_structure(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_structure.setter
    def directory_structure(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="discontinuityTags")
    def discontinuity_tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discontinuity_tags.setter
    def discontinuity_tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hlsCdnSettings")
    def hls_cdn_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgs
                ]
            ]
        ]
    ]: ...
    @hls_cdn_settings.setter
    def hls_cdn_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsId3SegmentTagging")
    def hls_id3_segment_tagging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hls_id3_segment_tagging.setter
    def hls_id3_segment_tagging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iframeOnlyPlaylists")
    def iframe_only_playlists(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iframe_only_playlists.setter
    def iframe_only_playlists(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incompleteSegmentBehavior")
    def incomplete_segment_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incomplete_segment_behavior.setter
    def incomplete_segment_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="indexNSegments")
    def index_n_segments(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @index_n_segments.setter
    def index_n_segments(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_action.setter
    def input_loss_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ivInManifest")
    def iv_in_manifest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iv_in_manifest.setter
    def iv_in_manifest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ivSource")
    def iv_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iv_source.setter
    def iv_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keepSegments")
    def keep_segments(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @keep_segments.setter
    def keep_segments(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="keyFormat")
    def key_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_format.setter
    def key_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyFormatVersions")
    def key_format_versions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_format_versions.setter
    def key_format_versions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyProviderSettings")
    def key_provider_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgs
        ]
    ]: ...
    @key_provider_settings.setter
    def key_provider_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestCompression")
    def manifest_compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manifest_compression.setter
    def manifest_compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manifestDurationFormat")
    def manifest_duration_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manifest_duration_format.setter
    def manifest_duration_format(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minSegmentLength")
    def min_segment_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_segment_length.setter
    def min_segment_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputSelection")
    def output_selection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_selection.setter
    def output_selection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programDateTime")
    def program_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @program_date_time.setter
    def program_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programDateTimeClock")
    def program_date_time_clock(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @program_date_time_clock.setter
    def program_date_time_clock(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programDateTimePeriod")
    def program_date_time_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @program_date_time_period.setter
    def program_date_time_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redundantManifest")
    def redundant_manifest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redundant_manifest.setter
    def redundant_manifest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentLength")
    def segment_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @segment_length.setter
    def segment_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentsPerSubdirectory")
    def segments_per_subdirectory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @segments_per_subdirectory.setter
    def segments_per_subdirectory(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="streamInfResolution")
    def stream_inf_resolution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_inf_resolution.setter
    def stream_inf_resolution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Frame")
    def timed_metadata_id3_frame(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_id3_frame.setter
    def timed_metadata_id3_frame(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Period")
    def timed_metadata_id3_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timed_metadata_id3_period.setter
    def timed_metadata_id3_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampDeltaMilliseconds")
    def timestamp_delta_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timestamp_delta_milliseconds.setter
    def timestamp_delta_milliseconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tsFileMode")
    def ts_file_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ts_file_mode.setter
    def ts_file_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgsDict(
    TypedDict
):
    caption_channel: pulumi.Input[_builtins.int]
    language_code: pulumi.Input[_builtins.str]
    language_description: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMappingArgs:
    def __init__(
        __self__,
        *,
        caption_channel: pulumi.Input[_builtins.int],
        language_code: pulumi.Input[_builtins.str],
        language_description: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captionChannel")
    def caption_channel(self) -> pulumi.Input[_builtins.int]: ...
    @caption_channel.setter
    def caption_channel(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]: ...
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="languageDescription")
    def language_description(self) -> pulumi.Input[_builtins.str]: ...
    @language_description.setter
    def language_description(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgsDict(
    TypedDict
):
    hls_akamai_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgsDict
        ]
    ]
    hls_basic_put_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgsDict
        ]
    ]
    hls_media_store_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgsDict
        ]
    ]
    hls_s3_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgsDict
        ]
    ]
    hls_webdav_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingArgs:
    def __init__(
        __self__,
        *,
        hls_akamai_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgs
            ]
        ] = ...,
        hls_basic_put_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgs
            ]
        ] = ...,
        hls_media_store_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgs
            ]
        ] = ...,
        hls_s3_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgs
            ]
        ] = ...,
        hls_webdav_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsAkamaiSettings")
    def hls_akamai_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgs
        ]
    ]: ...
    @hls_akamai_settings.setter
    def hls_akamai_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsBasicPutSettings")
    def hls_basic_put_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgs
        ]
    ]: ...
    @hls_basic_put_settings.setter
    def hls_basic_put_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsMediaStoreSettings")
    def hls_media_store_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgs
        ]
    ]: ...
    @hls_media_store_settings.setter
    def hls_media_store_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsS3Settings")
    def hls_s3_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgs
        ]
    ]: ...
    @hls_s3_settings.setter
    def hls_s3_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsWebdavSettings")
    def hls_webdav_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgs
        ]
    ]: ...
    @hls_webdav_settings.setter
    def hls_webdav_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgsDict(
    TypedDict
):
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    filecache_duration: NotRequired[pulumi.Input[_builtins.int]]
    http_transfer_mode: NotRequired[pulumi.Input[_builtins.str]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]
    salt: NotRequired[pulumi.Input[_builtins.str]]
    token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettingsArgs:
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        filecache_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        http_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        salt: Optional[pulumi.Input[_builtins.str]] = ...,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filecache_duration.setter
    def filecache_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTransferMode")
    def http_transfer_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_transfer_mode.setter
    def http_transfer_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def salt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @salt.setter
    def salt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgsDict(
    TypedDict
):
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    filecache_duration: NotRequired[pulumi.Input[_builtins.int]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettingsArgs:
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        filecache_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filecache_duration.setter
    def filecache_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgsDict(
    TypedDict
):
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    filecache_duration: NotRequired[pulumi.Input[_builtins.int]]
    media_store_storage_class: NotRequired[pulumi.Input[_builtins.str]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettingsArgs:
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        filecache_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        media_store_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filecache_duration.setter
    def filecache_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="mediaStoreStorageClass")
    def media_store_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @media_store_storage_class.setter
    def media_store_storage_class(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgsDict(
    TypedDict
):
    canned_acl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3SettingsArgs:
    def __init__(
        __self__, *, canned_acl: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl.setter
    def canned_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgsDict(
    TypedDict
):
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    filecache_duration: NotRequired[pulumi.Input[_builtins.int]]
    http_transfer_mode: NotRequired[pulumi.Input[_builtins.str]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettingsArgs:
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        filecache_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        http_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filecache_duration.setter
    def filecache_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTransferMode")
    def http_transfer_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_transfer_mode.setter
    def http_transfer_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgsDict(
    TypedDict
):
    static_key_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsArgs:
    def __init__(
        __self__,
        *,
        static_key_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="staticKeySettings")
    def static_key_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgs
                ]
            ]
        ]
    ]: ...
    @static_key_settings.setter
    def static_key_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgs
                    ]
                ]
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgsDict(
    TypedDict
):
    static_key_value: pulumi.Input[_builtins.str]
    key_provider_server: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingArgs:
    def __init__(
        __self__,
        *,
        static_key_value: pulumi.Input[_builtins.str],
        key_provider_server: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="staticKeyValue")
    def static_key_value(self) -> pulumi.Input[_builtins.str]: ...
    @static_key_value.setter
    def static_key_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyProviderServer")
    def key_provider_server(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgs
        ]
    ]: ...
    @key_provider_server.setter
    def key_provider_server(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServerArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgsDict
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgs
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgsDict
    ]
    acquisition_point_id: NotRequired[pulumi.Input[_builtins.str]]
    audio_only_timecode_control: NotRequired[pulumi.Input[_builtins.str]]
    certificate_mode: NotRequired[pulumi.Input[_builtins.str]]
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    event_id: NotRequired[pulumi.Input[_builtins.str]]
    event_id_mode: NotRequired[pulumi.Input[_builtins.str]]
    event_stop_behavior: NotRequired[pulumi.Input[_builtins.str]]
    filecache_duration: NotRequired[pulumi.Input[_builtins.int]]
    fragment_length: NotRequired[pulumi.Input[_builtins.int]]
    input_loss_action: NotRequired[pulumi.Input[_builtins.str]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]
    segmentation_mode: NotRequired[pulumi.Input[_builtins.str]]
    send_delay_ms: NotRequired[pulumi.Input[_builtins.int]]
    sparse_track_type: NotRequired[pulumi.Input[_builtins.str]]
    stream_manifest_behavior: NotRequired[pulumi.Input[_builtins.str]]
    timestamp_offset: NotRequired[pulumi.Input[_builtins.str]]
    timestamp_offset_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgs
        ],
        acquisition_point_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_only_timecode_control: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        event_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_id_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        event_stop_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        filecache_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        fragment_length: Optional[pulumi.Input[_builtins.int]] = ...,
        input_loss_action: Optional[pulumi.Input[_builtins.str]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        segmentation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        send_delay_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        sparse_track_type: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_manifest_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        timestamp_offset: Optional[pulumi.Input[_builtins.str]] = ...,
        timestamp_offset_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acquisitionPointId")
    def acquisition_point_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acquisition_point_id.setter
    def acquisition_point_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyTimecodeControl")
    def audio_only_timecode_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_only_timecode_control.setter
    def audio_only_timecode_control(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventId")
    def event_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_id.setter
    def event_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventIdMode")
    def event_id_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_id_mode.setter
    def event_id_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventStopBehavior")
    def event_stop_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_stop_behavior.setter
    def event_stop_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filecache_duration.setter
    def filecache_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fragmentLength")
    def fragment_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fragment_length.setter
    def fragment_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_action.setter
    def input_loss_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationMode")
    def segmentation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segmentation_mode.setter
    def segmentation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sendDelayMs")
    def send_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @send_delay_ms.setter
    def send_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sparseTrackType")
    def sparse_track_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sparse_track_type.setter
    def sparse_track_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamManifestBehavior")
    def stream_manifest_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_manifest_behavior.setter
    def stream_manifest_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampOffset")
    def timestamp_offset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_offset.setter
    def timestamp_offset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timestampOffsetMode")
    def timestamp_offset_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_offset_mode.setter
    def timestamp_offset_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgsDict(
    TypedDict
):
    ad_markers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    authentication_scheme: NotRequired[pulumi.Input[_builtins.str]]
    cache_full_behavior: NotRequired[pulumi.Input[_builtins.str]]
    cache_length: NotRequired[pulumi.Input[_builtins.int]]
    caption_data: NotRequired[pulumi.Input[_builtins.str]]
    input_loss_action: NotRequired[pulumi.Input[_builtins.str]]
    restart_delay: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        ad_markers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        authentication_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_full_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_length: Optional[pulumi.Input[_builtins.int]] = ...,
        caption_data: Optional[pulumi.Input[_builtins.str]] = ...,
        input_loss_action: Optional[pulumi.Input[_builtins.str]] = ...,
        restart_delay: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adMarkers")
    def ad_markers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ad_markers.setter
    def ad_markers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationScheme")
    def authentication_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_scheme.setter
    def authentication_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheFullBehavior")
    def cache_full_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_full_behavior.setter
    def cache_full_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheLength")
    def cache_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_length.setter
    def cache_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="captionData")
    def caption_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @caption_data.setter
    def caption_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_action.setter
    def input_loss_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @restart_delay.setter
    def restart_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgsDict(
    TypedDict
):
    input_loss_action: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_id3_frame: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_id3_period: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        input_loss_action: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_id3_frame: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_id3_period: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_loss_action.setter
    def input_loss_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Frame")
    def timed_metadata_id3_frame(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_id3_frame.setter
    def timed_metadata_id3_frame(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Period")
    def timed_metadata_id3_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timed_metadata_id3_period.setter
    def timed_metadata_id3_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgsDict(TypedDict):
    archive_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgsDict
        ]
    ]
    frame_capture_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgsDict
        ]
    ]
    hls_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgsDict
        ]
    ]
    media_package_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgsDict
        ]
    ]
    ms_smooth_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgsDict
        ]
    ]
    multiplex_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgsDict
        ]
    ]
    rtmp_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgsDict
        ]
    ]
    udp_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        archive_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgs
            ]
        ] = ...,
        frame_capture_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgs
            ]
        ] = ...,
        hls_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgs
            ]
        ] = ...,
        media_package_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgs
            ]
        ] = ...,
        ms_smooth_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgs
            ]
        ] = ...,
        multiplex_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgs
            ]
        ] = ...,
        rtmp_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgs
            ]
        ] = ...,
        udp_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveOutputSettings")
    def archive_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgs
        ]
    ]: ...
    @archive_output_settings.setter
    def archive_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureOutputSettings")
    def frame_capture_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgs
        ]
    ]: ...
    @frame_capture_output_settings.setter
    def frame_capture_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hlsOutputSettings")
    def hls_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgs
        ]
    ]: ...
    @hls_output_settings.setter
    def hls_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageOutputSettings")
    def media_package_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgs
        ]
    ]: ...
    @media_package_output_settings.setter
    def media_package_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="msSmoothOutputSettings")
    def ms_smooth_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgs
        ]
    ]: ...
    @ms_smooth_output_settings.setter
    def ms_smooth_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiplexOutputSettings")
    def multiplex_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgs
        ]
    ]: ...
    @multiplex_output_settings.setter
    def multiplex_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rtmpOutputSettings")
    def rtmp_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgs
        ]
    ]: ...
    @rtmp_output_settings.setter
    def rtmp_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="udpOutputSettings")
    def udp_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgs
        ]
    ]: ...
    @udp_output_settings.setter
    def udp_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgsDict(
    TypedDict
):
    container_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgsDict
        ]
    ]
    extension: NotRequired[pulumi.Input[_builtins.str]]
    name_modifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        container_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgs
            ]
        ] = ...,
        extension: Optional[pulumi.Input[_builtins.str]] = ...,
        name_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgs
        ]
    ]: ...
    @container_settings.setter
    def container_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension.setter
    def extension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_modifier.setter
    def name_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgsDict(
    TypedDict
):
    m2ts_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgsDict
        ]
    ]
    raw_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsArgs:
    def __init__(
        __self__,
        *,
        m2ts_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgs
            ]
        ] = ...,
        raw_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m2tsSettings")
    def m2ts_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgs
        ]
    ]: ...
    @m2ts_settings.setter
    def m2ts_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rawSettings")
    def raw_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgs
        ]
    ]: ...
    @raw_settings.setter
    def raw_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgsDict(
    TypedDict
):
    absent_input_audio_behavior: NotRequired[pulumi.Input[_builtins.str]]
    arib: NotRequired[pulumi.Input[_builtins.str]]
    arib_captions_pid: NotRequired[pulumi.Input[_builtins.str]]
    arib_captions_pid_control: NotRequired[pulumi.Input[_builtins.str]]
    audio_buffer_model: NotRequired[pulumi.Input[_builtins.str]]
    audio_frames_per_pes: NotRequired[pulumi.Input[_builtins.int]]
    audio_pids: NotRequired[pulumi.Input[_builtins.str]]
    audio_stream_type: NotRequired[pulumi.Input[_builtins.str]]
    bitrate: NotRequired[pulumi.Input[_builtins.int]]
    buffer_model: NotRequired[pulumi.Input[_builtins.str]]
    cc_descriptor: NotRequired[pulumi.Input[_builtins.str]]
    dvb_nit_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgsDict
        ]
    ]
    dvb_sdt_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgsDict
        ]
    ]
    dvb_sub_pids: NotRequired[pulumi.Input[_builtins.str]]
    dvb_tdt_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgsDict
        ]
    ]
    dvb_teletext_pid: NotRequired[pulumi.Input[_builtins.str]]
    ebif: NotRequired[pulumi.Input[_builtins.str]]
    ebp_audio_interval: NotRequired[pulumi.Input[_builtins.str]]
    ebp_lookahead_ms: NotRequired[pulumi.Input[_builtins.int]]
    ebp_placement: NotRequired[pulumi.Input[_builtins.str]]
    ecm_pid: NotRequired[pulumi.Input[_builtins.str]]
    es_rate_in_pes: NotRequired[pulumi.Input[_builtins.str]]
    etv_platform_pid: NotRequired[pulumi.Input[_builtins.str]]
    etv_signal_pid: NotRequired[pulumi.Input[_builtins.str]]
    fragment_time: NotRequired[pulumi.Input[_builtins.float]]
    klv: NotRequired[pulumi.Input[_builtins.str]]
    klv_data_pids: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_id3_behavior: NotRequired[pulumi.Input[_builtins.str]]
    null_packet_bitrate: NotRequired[pulumi.Input[_builtins.float]]
    pat_interval: NotRequired[pulumi.Input[_builtins.int]]
    pcr_control: NotRequired[pulumi.Input[_builtins.str]]
    pcr_period: NotRequired[pulumi.Input[_builtins.int]]
    pcr_pid: NotRequired[pulumi.Input[_builtins.str]]
    pmt_interval: NotRequired[pulumi.Input[_builtins.int]]
    pmt_pid: NotRequired[pulumi.Input[_builtins.str]]
    program_num: NotRequired[pulumi.Input[_builtins.int]]
    rate_mode: NotRequired[pulumi.Input[_builtins.str]]
    scte27_pids: NotRequired[pulumi.Input[_builtins.str]]
    scte35_control: NotRequired[pulumi.Input[_builtins.str]]
    scte35_pid: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_markers: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_style: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_time: NotRequired[pulumi.Input[_builtins.float]]
    timed_metadata_behavior: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_pid: NotRequired[pulumi.Input[_builtins.str]]
    transport_stream_id: NotRequired[pulumi.Input[_builtins.int]]
    video_pid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsArgs:
    def __init__(
        __self__,
        *,
        absent_input_audio_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        arib: Optional[pulumi.Input[_builtins.str]] = ...,
        arib_captions_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        arib_captions_pid_control: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_buffer_model: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_frames_per_pes: Optional[pulumi.Input[_builtins.int]] = ...,
        audio_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_stream_type: Optional[pulumi.Input[_builtins.str]] = ...,
        bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        buffer_model: Optional[pulumi.Input[_builtins.str]] = ...,
        cc_descriptor: Optional[pulumi.Input[_builtins.str]] = ...,
        dvb_nit_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
            ]
        ] = ...,
        dvb_sdt_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
            ]
        ] = ...,
        dvb_sub_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        dvb_tdt_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
            ]
        ] = ...,
        dvb_teletext_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        ebif: Optional[pulumi.Input[_builtins.str]] = ...,
        ebp_audio_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        ebp_lookahead_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        ebp_placement: Optional[pulumi.Input[_builtins.str]] = ...,
        ecm_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        es_rate_in_pes: Optional[pulumi.Input[_builtins.str]] = ...,
        etv_platform_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        etv_signal_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        fragment_time: Optional[pulumi.Input[_builtins.float]] = ...,
        klv: Optional[pulumi.Input[_builtins.str]] = ...,
        klv_data_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_id3_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        null_packet_bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        pat_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_control: Optional[pulumi.Input[_builtins.str]] = ...,
        pcr_period: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        pmt_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pmt_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        program_num: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scte27_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        scte35_control: Optional[pulumi.Input[_builtins.str]] = ...,
        scte35_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_markers: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_style: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_time: Optional[pulumi.Input[_builtins.float]] = ...,
        timed_metadata_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_stream_id: Optional[pulumi.Input[_builtins.int]] = ...,
        video_pid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="absentInputAudioBehavior")
    def absent_input_audio_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @absent_input_audio_behavior.setter
    def absent_input_audio_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arib(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib.setter
    def arib(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPid")
    def arib_captions_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib_captions_pid.setter
    def arib_captions_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPidControl")
    def arib_captions_pid_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib_captions_pid_control.setter
    def arib_captions_pid_control(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioBufferModel")
    def audio_buffer_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_buffer_model.setter
    def audio_buffer_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @audio_frames_per_pes.setter
    def audio_frames_per_pes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_pids.setter
    def audio_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioStreamType")
    def audio_stream_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_stream_type.setter
    def audio_stream_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bufferModel")
    def buffer_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @buffer_model.setter
    def buffer_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ccDescriptor")
    def cc_descriptor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cc_descriptor.setter
    def cc_descriptor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dvbNitSettings")
    def dvb_nit_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
        ]
    ]: ...
    @dvb_nit_settings.setter
    def dvb_nit_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSdtSettings")
    def dvb_sdt_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
        ]
    ]: ...
    @dvb_sdt_settings.setter
    def dvb_sdt_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSubPids")
    def dvb_sub_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dvb_sub_pids.setter
    def dvb_sub_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dvbTdtSettings")
    def dvb_tdt_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
        ]
    ]: ...
    @dvb_tdt_settings.setter
    def dvb_tdt_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbTeletextPid")
    def dvb_teletext_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dvb_teletext_pid.setter
    def dvb_teletext_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ebif(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebif.setter
    def ebif(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpAudioInterval")
    def ebp_audio_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebp_audio_interval.setter
    def ebp_audio_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpLookaheadMs")
    def ebp_lookahead_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ebp_lookahead_ms.setter
    def ebp_lookahead_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpPlacement")
    def ebp_placement(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebp_placement.setter
    def ebp_placement(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecm_pid.setter
    def ecm_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="esRateInPes")
    def es_rate_in_pes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @es_rate_in_pes.setter
    def es_rate_in_pes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="etvPlatformPid")
    def etv_platform_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etv_platform_pid.setter
    def etv_platform_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="etvSignalPid")
    def etv_signal_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etv_signal_pid.setter
    def etv_signal_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fragmentTime")
    def fragment_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @fragment_time.setter
    def fragment_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def klv(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @klv.setter
    def klv(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="klvDataPids")
    def klv_data_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @klv_data_pids.setter
    def klv_data_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_id3_behavior.setter
    def nielsen_id3_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nullPacketBitrate")
    def null_packet_bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @null_packet_bitrate.setter
    def null_packet_bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pat_interval.setter
    def pat_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_control.setter
    def pcr_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pcr_period.setter
    def pcr_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_pid.setter
    def pcr_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pmt_interval.setter
    def pmt_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pmt_pid.setter
    def pmt_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @program_num.setter
    def program_num(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateMode")
    def rate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rate_mode.setter
    def rate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte27Pids")
    def scte27_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte27_pids.setter
    def scte27_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Control")
    def scte35_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_control.setter
    def scte35_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_pid.setter
    def scte35_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationMarkers")
    def segmentation_markers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segmentation_markers.setter
    def segmentation_markers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationStyle")
    def segmentation_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segmentation_style.setter
    def segmentation_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationTime")
    def segmentation_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @segmentation_time.setter
    def segmentation_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_behavior.setter
    def timed_metadata_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_pid.setter
    def timed_metadata_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transport_stream_id.setter
    def transport_stream_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @video_pid.setter
    def video_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgsDict(
    TypedDict
):
    network_id: pulumi.Input[_builtins.int]
    network_name: pulumi.Input[_builtins.str]
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs:
    def __init__(
        __self__,
        *,
        network_id: pulumi.Input[_builtins.int],
        network_name: pulumi.Input[_builtins.str],
        rep_interval: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[_builtins.int]: ...
    @network_id.setter
    def network_id(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_name.setter
    def network_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgsDict(
    TypedDict
):
    output_sdt: NotRequired[pulumi.Input[_builtins.str]]
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    service_provider_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs:
    def __init__(
        __self__,
        *,
        output_sdt: Optional[pulumi.Input[_builtins.str]] = ...,
        rep_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSdt")
    def output_sdt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_sdt.setter
    def output_sdt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderName")
    def service_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_provider_name.setter
    def service_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgsDict(
    TypedDict
):
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs:
    def __init__(
        __self__, *, rep_interval: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgsDict(
    TypedDict
):
    name_modifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettingsArgs:
    def __init__(
        __self__, *, name_modifier: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_modifier.setter
    def name_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgsDict(
    TypedDict
):
    hls_settings: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgsDict
    ]
    h265_packaging_type: NotRequired[pulumi.Input[_builtins.str]]
    name_modifier: NotRequired[pulumi.Input[_builtins.str]]
    segment_modifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        hls_settings: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgs
        ],
        h265_packaging_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsSettings")
    def hls_settings(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgs
    ]: ...
    @hls_settings.setter
    def hls_settings(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="h265PackagingType")
    def h265_packaging_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @h265_packaging_type.setter
    def h265_packaging_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_modifier.setter
    def name_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentModifier")
    def segment_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segment_modifier.setter
    def segment_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgsDict(
    TypedDict
):
    audio_only_hls_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgsDict
        ]
    ]
    fmp4_hls_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgsDict
        ]
    ]
    frame_capture_hls_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgsDict
        ]
    ]
    standard_hls_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_only_hls_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgs
            ]
        ] = ...,
        fmp4_hls_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgs
            ]
        ] = ...,
        frame_capture_hls_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgs
            ]
        ] = ...,
        standard_hls_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyHlsSettings")
    def audio_only_hls_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgs
        ]
    ]: ...
    @audio_only_hls_settings.setter
    def audio_only_hls_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fmp4HlsSettings")
    def fmp4_hls_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgs
        ]
    ]: ...
    @fmp4_hls_settings.setter
    def fmp4_hls_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureHlsSettings")
    def frame_capture_hls_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgs
        ]
    ]: ...
    @frame_capture_hls_settings.setter
    def frame_capture_hls_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="standardHlsSettings")
    def standard_hls_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgs
        ]
    ]: ...
    @standard_hls_settings.setter
    def standard_hls_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgsDict(
    TypedDict
):
    audio_group_id: NotRequired[pulumi.Input[_builtins.str]]
    audio_only_image: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgsDict
        ]
    ]
    audio_track_type: NotRequired[pulumi.Input[_builtins.str]]
    segment_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_only_image: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgs
            ]
        ] = ...,
        audio_track_type: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioGroupId")
    def audio_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_group_id.setter
    def audio_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyImage")
    def audio_only_image(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgs
        ]
    ]: ...
    @audio_only_image.setter
    def audio_only_image(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioTrackType")
    def audio_track_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_track_type.setter
    def audio_track_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentType")
    def segment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segment_type.setter
    def segment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]
    password_param: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImageArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        password_param: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_param.setter
    def password_param(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgsDict(
    TypedDict
):
    audio_rendition_sets: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_id3_behavior: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_behavior: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_rendition_sets: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_id3_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioRenditionSets")
    def audio_rendition_sets(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_rendition_sets.setter
    def audio_rendition_sets(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_id3_behavior.setter
    def nielsen_id3_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_behavior.setter
    def timed_metadata_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgsDict(
    TypedDict
):
    m3u8_settings: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgsDict
    ]
    audio_rendition_sets: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsArgs:
    def __init__(
        __self__,
        *,
        m3u8_settings: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgs
        ],
        audio_rendition_sets: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m3u8Settings")
    def m3u8_settings(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgs
    ]: ...
    @m3u8_settings.setter
    def m3u8_settings(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioRenditionSets")
    def audio_rendition_sets(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_rendition_sets.setter
    def audio_rendition_sets(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgsDict(
    TypedDict
):
    audio_frames_per_pes: NotRequired[pulumi.Input[_builtins.int]]
    audio_pids: NotRequired[pulumi.Input[_builtins.str]]
    ecm_pid: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_id3_behavior: NotRequired[pulumi.Input[_builtins.str]]
    pat_interval: NotRequired[pulumi.Input[_builtins.int]]
    pcr_control: NotRequired[pulumi.Input[_builtins.str]]
    pcr_period: NotRequired[pulumi.Input[_builtins.int]]
    pcr_pid: NotRequired[pulumi.Input[_builtins.str]]
    pmt_interval: NotRequired[pulumi.Input[_builtins.int]]
    pmt_pid: NotRequired[pulumi.Input[_builtins.str]]
    program_num: NotRequired[pulumi.Input[_builtins.int]]
    scte35_behavior: NotRequired[pulumi.Input[_builtins.str]]
    scte35_pid: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_behavior: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_pid: NotRequired[pulumi.Input[_builtins.str]]
    transport_stream_id: NotRequired[pulumi.Input[_builtins.int]]
    video_pid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8SettingsArgs:
    def __init__(
        __self__,
        *,
        audio_frames_per_pes: Optional[pulumi.Input[_builtins.int]] = ...,
        audio_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        ecm_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_id3_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        pat_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_control: Optional[pulumi.Input[_builtins.str]] = ...,
        pcr_period: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        pmt_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pmt_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        program_num: Optional[pulumi.Input[_builtins.int]] = ...,
        scte35_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        scte35_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_stream_id: Optional[pulumi.Input[_builtins.int]] = ...,
        video_pid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @audio_frames_per_pes.setter
    def audio_frames_per_pes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_pids.setter
    def audio_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecm_pid.setter
    def ecm_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_id3_behavior.setter
    def nielsen_id3_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pat_interval.setter
    def pat_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_control.setter
    def pcr_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pcr_period.setter
    def pcr_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_pid.setter
    def pcr_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pmt_interval.setter
    def pmt_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pmt_pid.setter
    def pmt_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @program_num.setter
    def program_num(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Behavior")
    def scte35_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_behavior.setter
    def scte35_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_pid.setter
    def scte35_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_behavior.setter
    def timed_metadata_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_pid.setter
    def timed_metadata_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transport_stream_id.setter
    def transport_stream_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @video_pid.setter
    def video_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgsDict(
    TypedDict
):
    h265_packaging_type: NotRequired[pulumi.Input[_builtins.str]]
    name_modifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        h265_packaging_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="h265PackagingType")
    def h265_packaging_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @h265_packaging_type.setter
    def h265_packaging_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_modifier.setter
    def name_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgsDict
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgs
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgsDict(
    TypedDict
):
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgsDict
    ]
    certificate_mode: NotRequired[pulumi.Input[_builtins.str]]
    connection_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    num_retries: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgs
        ],
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_retry_interval.setter
    def connection_retry_interval(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgsDict(
    TypedDict
):
    container_settings: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgsDict
    ]
    destination: pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgsDict
    ]
    buffer_msec: NotRequired[pulumi.Input[_builtins.int]]
    fec_output_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        container_settings: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgs
        ],
        destination: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgs
        ],
        buffer_msec: Optional[pulumi.Input[_builtins.int]] = ...,
        fec_output_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgs
    ]: ...
    @container_settings.setter
    def container_settings(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bufferMsec")
    def buffer_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @buffer_msec.setter
    def buffer_msec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fecOutputSettings")
    def fec_output_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgs
        ]
    ]: ...
    @fec_output_settings.setter
    def fec_output_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgsDict(
    TypedDict
):
    m2ts_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsArgs:
    def __init__(
        __self__,
        *,
        m2ts_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m2tsSettings")
    def m2ts_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgs
        ]
    ]: ...
    @m2ts_settings.setter
    def m2ts_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgsDict(
    TypedDict
):
    absent_input_audio_behavior: NotRequired[pulumi.Input[_builtins.str]]
    arib: NotRequired[pulumi.Input[_builtins.str]]
    arib_captions_pid: NotRequired[pulumi.Input[_builtins.str]]
    arib_captions_pid_control: NotRequired[pulumi.Input[_builtins.str]]
    audio_buffer_model: NotRequired[pulumi.Input[_builtins.str]]
    audio_frames_per_pes: NotRequired[pulumi.Input[_builtins.int]]
    audio_pids: NotRequired[pulumi.Input[_builtins.str]]
    audio_stream_type: NotRequired[pulumi.Input[_builtins.str]]
    bitrate: NotRequired[pulumi.Input[_builtins.int]]
    buffer_model: NotRequired[pulumi.Input[_builtins.str]]
    cc_descriptor: NotRequired[pulumi.Input[_builtins.str]]
    dvb_nit_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgsDict
        ]
    ]
    dvb_sdt_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgsDict
        ]
    ]
    dvb_sub_pids: NotRequired[pulumi.Input[_builtins.str]]
    dvb_tdt_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgsDict
        ]
    ]
    dvb_teletext_pid: NotRequired[pulumi.Input[_builtins.str]]
    ebif: NotRequired[pulumi.Input[_builtins.str]]
    ebp_audio_interval: NotRequired[pulumi.Input[_builtins.str]]
    ebp_lookahead_ms: NotRequired[pulumi.Input[_builtins.int]]
    ebp_placement: NotRequired[pulumi.Input[_builtins.str]]
    ecm_pid: NotRequired[pulumi.Input[_builtins.str]]
    es_rate_in_pes: NotRequired[pulumi.Input[_builtins.str]]
    etv_platform_pid: NotRequired[pulumi.Input[_builtins.str]]
    etv_signal_pid: NotRequired[pulumi.Input[_builtins.str]]
    fragment_time: NotRequired[pulumi.Input[_builtins.float]]
    klv: NotRequired[pulumi.Input[_builtins.str]]
    klv_data_pids: NotRequired[pulumi.Input[_builtins.str]]
    nielsen_id3_behavior: NotRequired[pulumi.Input[_builtins.str]]
    null_packet_bitrate: NotRequired[pulumi.Input[_builtins.float]]
    pat_interval: NotRequired[pulumi.Input[_builtins.int]]
    pcr_control: NotRequired[pulumi.Input[_builtins.str]]
    pcr_period: NotRequired[pulumi.Input[_builtins.int]]
    pcr_pid: NotRequired[pulumi.Input[_builtins.str]]
    pmt_interval: NotRequired[pulumi.Input[_builtins.int]]
    pmt_pid: NotRequired[pulumi.Input[_builtins.str]]
    program_num: NotRequired[pulumi.Input[_builtins.int]]
    rate_mode: NotRequired[pulumi.Input[_builtins.str]]
    scte27_pids: NotRequired[pulumi.Input[_builtins.str]]
    scte35_control: NotRequired[pulumi.Input[_builtins.str]]
    scte35_pid: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_markers: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_style: NotRequired[pulumi.Input[_builtins.str]]
    segmentation_time: NotRequired[pulumi.Input[_builtins.float]]
    timed_metadata_behavior: NotRequired[pulumi.Input[_builtins.str]]
    timed_metadata_pid: NotRequired[pulumi.Input[_builtins.str]]
    transport_stream_id: NotRequired[pulumi.Input[_builtins.int]]
    video_pid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsArgs:
    def __init__(
        __self__,
        *,
        absent_input_audio_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        arib: Optional[pulumi.Input[_builtins.str]] = ...,
        arib_captions_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        arib_captions_pid_control: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_buffer_model: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_frames_per_pes: Optional[pulumi.Input[_builtins.int]] = ...,
        audio_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_stream_type: Optional[pulumi.Input[_builtins.str]] = ...,
        bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        buffer_model: Optional[pulumi.Input[_builtins.str]] = ...,
        cc_descriptor: Optional[pulumi.Input[_builtins.str]] = ...,
        dvb_nit_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
            ]
        ] = ...,
        dvb_sdt_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
            ]
        ] = ...,
        dvb_sub_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        dvb_tdt_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
            ]
        ] = ...,
        dvb_teletext_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        ebif: Optional[pulumi.Input[_builtins.str]] = ...,
        ebp_audio_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        ebp_lookahead_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        ebp_placement: Optional[pulumi.Input[_builtins.str]] = ...,
        ecm_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        es_rate_in_pes: Optional[pulumi.Input[_builtins.str]] = ...,
        etv_platform_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        etv_signal_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        fragment_time: Optional[pulumi.Input[_builtins.float]] = ...,
        klv: Optional[pulumi.Input[_builtins.str]] = ...,
        klv_data_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        nielsen_id3_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        null_packet_bitrate: Optional[pulumi.Input[_builtins.float]] = ...,
        pat_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_control: Optional[pulumi.Input[_builtins.str]] = ...,
        pcr_period: Optional[pulumi.Input[_builtins.int]] = ...,
        pcr_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        pmt_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        pmt_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        program_num: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scte27_pids: Optional[pulumi.Input[_builtins.str]] = ...,
        scte35_control: Optional[pulumi.Input[_builtins.str]] = ...,
        scte35_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_markers: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_style: Optional[pulumi.Input[_builtins.str]] = ...,
        segmentation_time: Optional[pulumi.Input[_builtins.float]] = ...,
        timed_metadata_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        timed_metadata_pid: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_stream_id: Optional[pulumi.Input[_builtins.int]] = ...,
        video_pid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="absentInputAudioBehavior")
    def absent_input_audio_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @absent_input_audio_behavior.setter
    def absent_input_audio_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arib(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib.setter
    def arib(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPid")
    def arib_captions_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib_captions_pid.setter
    def arib_captions_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPidControl")
    def arib_captions_pid_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arib_captions_pid_control.setter
    def arib_captions_pid_control(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioBufferModel")
    def audio_buffer_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_buffer_model.setter
    def audio_buffer_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @audio_frames_per_pes.setter
    def audio_frames_per_pes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_pids.setter
    def audio_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioStreamType")
    def audio_stream_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_stream_type.setter
    def audio_stream_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bufferModel")
    def buffer_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @buffer_model.setter
    def buffer_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ccDescriptor")
    def cc_descriptor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cc_descriptor.setter
    def cc_descriptor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dvbNitSettings")
    def dvb_nit_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
        ]
    ]: ...
    @dvb_nit_settings.setter
    def dvb_nit_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSdtSettings")
    def dvb_sdt_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
        ]
    ]: ...
    @dvb_sdt_settings.setter
    def dvb_sdt_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSubPids")
    def dvb_sub_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dvb_sub_pids.setter
    def dvb_sub_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dvbTdtSettings")
    def dvb_tdt_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
        ]
    ]: ...
    @dvb_tdt_settings.setter
    def dvb_tdt_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbTeletextPid")
    def dvb_teletext_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dvb_teletext_pid.setter
    def dvb_teletext_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ebif(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebif.setter
    def ebif(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpAudioInterval")
    def ebp_audio_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebp_audio_interval.setter
    def ebp_audio_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpLookaheadMs")
    def ebp_lookahead_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ebp_lookahead_ms.setter
    def ebp_lookahead_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ebpPlacement")
    def ebp_placement(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebp_placement.setter
    def ebp_placement(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecm_pid.setter
    def ecm_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="esRateInPes")
    def es_rate_in_pes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @es_rate_in_pes.setter
    def es_rate_in_pes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="etvPlatformPid")
    def etv_platform_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etv_platform_pid.setter
    def etv_platform_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="etvSignalPid")
    def etv_signal_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etv_signal_pid.setter
    def etv_signal_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fragmentTime")
    def fragment_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @fragment_time.setter
    def fragment_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def klv(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @klv.setter
    def klv(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="klvDataPids")
    def klv_data_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @klv_data_pids.setter
    def klv_data_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nielsen_id3_behavior.setter
    def nielsen_id3_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nullPacketBitrate")
    def null_packet_bitrate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @null_packet_bitrate.setter
    def null_packet_bitrate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pat_interval.setter
    def pat_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_control.setter
    def pcr_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pcr_period.setter
    def pcr_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcr_pid.setter
    def pcr_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pmt_interval.setter
    def pmt_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pmt_pid.setter
    def pmt_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @program_num.setter
    def program_num(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateMode")
    def rate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rate_mode.setter
    def rate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte27Pids")
    def scte27_pids(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte27_pids.setter
    def scte27_pids(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Control")
    def scte35_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_control.setter
    def scte35_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_pid.setter
    def scte35_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationMarkers")
    def segmentation_markers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segmentation_markers.setter
    def segmentation_markers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationStyle")
    def segmentation_style(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segmentation_style.setter
    def segmentation_style(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentationTime")
    def segmentation_time(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @segmentation_time.setter
    def segmentation_time(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_behavior.setter
    def timed_metadata_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timed_metadata_pid.setter
    def timed_metadata_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transport_stream_id.setter
    def transport_stream_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @video_pid.setter
    def video_pid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgsDict(
    TypedDict
):
    network_id: pulumi.Input[_builtins.int]
    network_name: pulumi.Input[_builtins.str]
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettingsArgs:
    def __init__(
        __self__,
        *,
        network_id: pulumi.Input[_builtins.int],
        network_name: pulumi.Input[_builtins.str],
        rep_interval: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[_builtins.int]: ...
    @network_id.setter
    def network_id(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_name.setter
    def network_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgsDict(
    TypedDict
):
    output_sdt: NotRequired[pulumi.Input[_builtins.str]]
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    service_provider_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettingsArgs:
    def __init__(
        __self__,
        *,
        output_sdt: Optional[pulumi.Input[_builtins.str]] = ...,
        rep_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSdt")
    def output_sdt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_sdt.setter
    def output_sdt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderName")
    def service_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_provider_name.setter
    def service_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgsDict(
    TypedDict
):
    rep_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettingsArgs:
    def __init__(
        __self__, *, rep_interval: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rep_interval.setter
    def rep_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgsDict(
    TypedDict
):
    destination_ref_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestinationArgs:
    def __init__(
        __self__, *, destination_ref_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> pulumi.Input[_builtins.str]: ...
    @destination_ref_id.setter
    def destination_ref_id(self, value: pulumi.Input[_builtins.str]): ...

class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgsDict(
    TypedDict
):
    column_depth: NotRequired[pulumi.Input[_builtins.int]]
    include_fec: NotRequired[pulumi.Input[_builtins.str]]
    row_length: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettingsArgs:
    def __init__(
        __self__,
        *,
        column_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        include_fec: Optional[pulumi.Input[_builtins.str]] = ...,
        row_length: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnDepth")
    def column_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @column_depth.setter
    def column_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="includeFec")
    def include_fec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_fec.setter
    def include_fec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowLength")
    def row_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @row_length.setter
    def row_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsTimecodeConfigArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    sync_threshold: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsTimecodeConfigArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        sync_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="syncThreshold")
    def sync_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sync_threshold.setter
    def sync_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsVideoDescriptionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    codec_settings: NotRequired[
        pulumi.Input[ChannelEncoderSettingsVideoDescriptionCodecSettingsArgsDict]
    ]
    height: NotRequired[pulumi.Input[_builtins.int]]
    respond_to_afd: NotRequired[pulumi.Input[_builtins.str]]
    scaling_behavior: NotRequired[pulumi.Input[_builtins.str]]
    sharpness: NotRequired[pulumi.Input[_builtins.int]]
    width: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        codec_settings: Optional[
            pulumi.Input[ChannelEncoderSettingsVideoDescriptionCodecSettingsArgs]
        ] = ...,
        height: Optional[pulumi.Input[_builtins.int]] = ...,
        respond_to_afd: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        sharpness: Optional[pulumi.Input[_builtins.int]] = ...,
        width: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codecSettings")
    def codec_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelEncoderSettingsVideoDescriptionCodecSettingsArgs]
    ]: ...
    @codec_settings.setter
    def codec_settings(
        self,
        value: Optional[
            pulumi.Input[ChannelEncoderSettingsVideoDescriptionCodecSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @height.setter
    def height(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="respondToAfd")
    def respond_to_afd(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @respond_to_afd.setter
    def respond_to_afd(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingBehavior")
    def scaling_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_behavior.setter
    def scaling_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sharpness(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sharpness.setter
    def sharpness(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @width.setter
    def width(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsArgsDict(TypedDict):
    frame_capture_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgsDict
        ]
    ]
    h264_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgsDict
        ]
    ]
    h265_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsArgs:
    def __init__(
        __self__,
        *,
        frame_capture_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgs
            ]
        ] = ...,
        h264_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgs
            ]
        ] = ...,
        h265_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureSettings")
    def frame_capture_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgs
        ]
    ]: ...
    @frame_capture_settings.setter
    def frame_capture_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="h264Settings")
    def h264_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgs
        ]
    ]: ...
    @h264_settings.setter
    def h264_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="h265Settings")
    def h265_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgs
        ]
    ]: ...
    @h265_settings.setter
    def h265_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgsDict(
    TypedDict
):
    capture_interval: NotRequired[pulumi.Input[_builtins.int]]
    capture_interval_units: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettingsArgs:
    def __init__(
        __self__,
        *,
        capture_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        capture_interval_units: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captureInterval")
    def capture_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capture_interval.setter
    def capture_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="captureIntervalUnits")
    def capture_interval_units(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capture_interval_units.setter
    def capture_interval_units(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgsDict(
    TypedDict
):
    adaptive_quantization: NotRequired[pulumi.Input[_builtins.str]]
    afd_signaling: NotRequired[pulumi.Input[_builtins.str]]
    bitrate: NotRequired[pulumi.Input[_builtins.int]]
    buf_fill_pct: NotRequired[pulumi.Input[_builtins.int]]
    buf_size: NotRequired[pulumi.Input[_builtins.int]]
    color_metadata: NotRequired[pulumi.Input[_builtins.str]]
    entropy_encoding: NotRequired[pulumi.Input[_builtins.str]]
    filter_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgsDict
        ]
    ]
    fixed_afd: NotRequired[pulumi.Input[_builtins.str]]
    flicker_aq: NotRequired[pulumi.Input[_builtins.str]]
    force_field_pictures: NotRequired[pulumi.Input[_builtins.str]]
    framerate_control: NotRequired[pulumi.Input[_builtins.str]]
    framerate_denominator: NotRequired[pulumi.Input[_builtins.int]]
    framerate_numerator: NotRequired[pulumi.Input[_builtins.int]]
    gop_b_reference: NotRequired[pulumi.Input[_builtins.str]]
    gop_closed_cadence: NotRequired[pulumi.Input[_builtins.int]]
    gop_num_b_frames: NotRequired[pulumi.Input[_builtins.int]]
    gop_size: NotRequired[pulumi.Input[_builtins.float]]
    gop_size_units: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[_builtins.str]]
    look_ahead_rate_control: NotRequired[pulumi.Input[_builtins.str]]
    max_bitrate: NotRequired[pulumi.Input[_builtins.int]]
    min_i_interval: NotRequired[pulumi.Input[_builtins.int]]
    num_ref_frames: NotRequired[pulumi.Input[_builtins.int]]
    par_control: NotRequired[pulumi.Input[_builtins.str]]
    par_denominator: NotRequired[pulumi.Input[_builtins.int]]
    par_numerator: NotRequired[pulumi.Input[_builtins.int]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    quality_level: NotRequired[pulumi.Input[_builtins.str]]
    qvbr_quality_level: NotRequired[pulumi.Input[_builtins.int]]
    rate_control_mode: NotRequired[pulumi.Input[_builtins.str]]
    scan_type: NotRequired[pulumi.Input[_builtins.str]]
    scene_change_detect: NotRequired[pulumi.Input[_builtins.str]]
    slices: NotRequired[pulumi.Input[_builtins.int]]
    softness: NotRequired[pulumi.Input[_builtins.int]]
    spatial_aq: NotRequired[pulumi.Input[_builtins.str]]
    subgop_length: NotRequired[pulumi.Input[_builtins.str]]
    syntax: NotRequired[pulumi.Input[_builtins.str]]
    temporal_aq: NotRequired[pulumi.Input[_builtins.str]]
    timecode_insertion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsArgs:
    def __init__(
        __self__,
        *,
        adaptive_quantization: Optional[pulumi.Input[_builtins.str]] = ...,
        afd_signaling: Optional[pulumi.Input[_builtins.str]] = ...,
        bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        buf_fill_pct: Optional[pulumi.Input[_builtins.int]] = ...,
        buf_size: Optional[pulumi.Input[_builtins.int]] = ...,
        color_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        entropy_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgs
            ]
        ] = ...,
        fixed_afd: Optional[pulumi.Input[_builtins.str]] = ...,
        flicker_aq: Optional[pulumi.Input[_builtins.str]] = ...,
        force_field_pictures: Optional[pulumi.Input[_builtins.str]] = ...,
        framerate_control: Optional[pulumi.Input[_builtins.str]] = ...,
        framerate_denominator: Optional[pulumi.Input[_builtins.int]] = ...,
        framerate_numerator: Optional[pulumi.Input[_builtins.int]] = ...,
        gop_b_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        gop_closed_cadence: Optional[pulumi.Input[_builtins.int]] = ...,
        gop_num_b_frames: Optional[pulumi.Input[_builtins.int]] = ...,
        gop_size: Optional[pulumi.Input[_builtins.float]] = ...,
        gop_size_units: Optional[pulumi.Input[_builtins.str]] = ...,
        level: Optional[pulumi.Input[_builtins.str]] = ...,
        look_ahead_rate_control: Optional[pulumi.Input[_builtins.str]] = ...,
        max_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        min_i_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        num_ref_frames: Optional[pulumi.Input[_builtins.int]] = ...,
        par_control: Optional[pulumi.Input[_builtins.str]] = ...,
        par_denominator: Optional[pulumi.Input[_builtins.int]] = ...,
        par_numerator: Optional[pulumi.Input[_builtins.int]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        quality_level: Optional[pulumi.Input[_builtins.str]] = ...,
        qvbr_quality_level: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_control_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scene_change_detect: Optional[pulumi.Input[_builtins.str]] = ...,
        slices: Optional[pulumi.Input[_builtins.int]] = ...,
        softness: Optional[pulumi.Input[_builtins.int]] = ...,
        spatial_aq: Optional[pulumi.Input[_builtins.str]] = ...,
        subgop_length: Optional[pulumi.Input[_builtins.str]] = ...,
        syntax: Optional[pulumi.Input[_builtins.str]] = ...,
        temporal_aq: Optional[pulumi.Input[_builtins.str]] = ...,
        timecode_insertion: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveQuantization")
    def adaptive_quantization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @adaptive_quantization.setter
    def adaptive_quantization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="afdSignaling")
    def afd_signaling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @afd_signaling.setter
    def afd_signaling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bitrate.setter
    def bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bufFillPct")
    def buf_fill_pct(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @buf_fill_pct.setter
    def buf_fill_pct(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bufSize")
    def buf_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @buf_size.setter
    def buf_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="colorMetadata")
    def color_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @color_metadata.setter
    def color_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entropyEncoding")
    def entropy_encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entropy_encoding.setter
    def entropy_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterSettings")
    def filter_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgs
        ]
    ]: ...
    @filter_settings.setter
    def filter_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixedAfd")
    def fixed_afd(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_afd.setter
    def fixed_afd(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flickerAq")
    def flicker_aq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flicker_aq.setter
    def flicker_aq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceFieldPictures")
    def force_field_pictures(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_field_pictures.setter
    def force_field_pictures(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="framerateControl")
    def framerate_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @framerate_control.setter
    def framerate_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="framerateDenominator")
    def framerate_denominator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @framerate_denominator.setter
    def framerate_denominator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="framerateNumerator")
    def framerate_numerator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @framerate_numerator.setter
    def framerate_numerator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gopBReference")
    def gop_b_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gop_b_reference.setter
    def gop_b_reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gopClosedCadence")
    def gop_closed_cadence(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gop_closed_cadence.setter
    def gop_closed_cadence(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gopNumBFrames")
    def gop_num_b_frames(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gop_num_b_frames.setter
    def gop_num_b_frames(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gopSize")
    def gop_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gop_size.setter
    def gop_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="gopSizeUnits")
    def gop_size_units(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gop_size_units.setter
    def gop_size_units(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookAheadRateControl")
    def look_ahead_rate_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @look_ahead_rate_control.setter
    def look_ahead_rate_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBitrate")
    def max_bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_bitrate.setter
    def max_bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minIInterval")
    def min_i_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_i_interval.setter
    def min_i_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numRefFrames")
    def num_ref_frames(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_ref_frames.setter
    def num_ref_frames(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parControl")
    def par_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @par_control.setter
    def par_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parDenominator")
    def par_denominator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @par_denominator.setter
    def par_denominator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parNumerator")
    def par_numerator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @par_numerator.setter
    def par_numerator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qualityLevel")
    def quality_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quality_level.setter
    def quality_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qvbrQualityLevel")
    def qvbr_quality_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @qvbr_quality_level.setter
    def qvbr_quality_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rate_control_mode.setter
    def rate_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scan_type.setter
    def scan_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sceneChangeDetect")
    def scene_change_detect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scene_change_detect.setter
    def scene_change_detect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def slices(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slices.setter
    def slices(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def softness(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @softness.setter
    def softness(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="spatialAq")
    def spatial_aq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spatial_aq.setter
    def spatial_aq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subgopLength")
    def subgop_length(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subgop_length.setter
    def subgop_length(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def syntax(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @syntax.setter
    def syntax(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="temporalAq")
    def temporal_aq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @temporal_aq.setter
    def temporal_aq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timecodeInsertion")
    def timecode_insertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timecode_insertion.setter
    def timecode_insertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgsDict(
    TypedDict
):
    temporal_filter_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsArgs:
    def __init__(
        __self__,
        *,
        temporal_filter_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="temporalFilterSettings")
    def temporal_filter_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgs
        ]
    ]: ...
    @temporal_filter_settings.setter
    def temporal_filter_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgsDict(
    TypedDict
):
    post_filter_sharpening: NotRequired[pulumi.Input[_builtins.str]]
    strength: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettingsArgs:
    def __init__(
        __self__,
        *,
        post_filter_sharpening: Optional[pulumi.Input[_builtins.str]] = ...,
        strength: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postFilterSharpening")
    def post_filter_sharpening(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_filter_sharpening.setter
    def post_filter_sharpening(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def strength(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strength.setter
    def strength(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgsDict(
    TypedDict
):
    bitrate: pulumi.Input[_builtins.int]
    framerate_denominator: pulumi.Input[_builtins.int]
    framerate_numerator: pulumi.Input[_builtins.int]
    adaptive_quantization: NotRequired[pulumi.Input[_builtins.str]]
    afd_signaling: NotRequired[pulumi.Input[_builtins.str]]
    alternative_transfer_function: NotRequired[pulumi.Input[_builtins.str]]
    buf_size: NotRequired[pulumi.Input[_builtins.int]]
    color_metadata: NotRequired[pulumi.Input[_builtins.str]]
    color_space_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgsDict
        ]
    ]
    filter_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgsDict
        ]
    ]
    fixed_afd: NotRequired[pulumi.Input[_builtins.str]]
    flicker_aq: NotRequired[pulumi.Input[_builtins.str]]
    gop_closed_cadence: NotRequired[pulumi.Input[_builtins.int]]
    gop_size: NotRequired[pulumi.Input[_builtins.float]]
    gop_size_units: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[_builtins.str]]
    look_ahead_rate_control: NotRequired[pulumi.Input[_builtins.str]]
    max_bitrate: NotRequired[pulumi.Input[_builtins.int]]
    min_i_interval: NotRequired[pulumi.Input[_builtins.int]]
    min_qp: NotRequired[pulumi.Input[_builtins.int]]
    mv_over_picture_boundaries: NotRequired[pulumi.Input[_builtins.str]]
    mv_temporal_predictor: NotRequired[pulumi.Input[_builtins.str]]
    par_denominator: NotRequired[pulumi.Input[_builtins.int]]
    par_numerator: NotRequired[pulumi.Input[_builtins.int]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    qvbr_quality_level: NotRequired[pulumi.Input[_builtins.int]]
    rate_control_mode: NotRequired[pulumi.Input[_builtins.str]]
    scan_type: NotRequired[pulumi.Input[_builtins.str]]
    scene_change_detect: NotRequired[pulumi.Input[_builtins.str]]
    slices: NotRequired[pulumi.Input[_builtins.int]]
    tier: NotRequired[pulumi.Input[_builtins.str]]
    tile_height: NotRequired[pulumi.Input[_builtins.int]]
    tile_padding: NotRequired[pulumi.Input[_builtins.str]]
    tile_width: NotRequired[pulumi.Input[_builtins.int]]
    timecode_burnin_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgsDict
        ]
    ]
    timecode_insertion: NotRequired[pulumi.Input[_builtins.str]]
    treeblock_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsArgs:
    def __init__(
        __self__,
        *,
        bitrate: pulumi.Input[_builtins.int],
        framerate_denominator: pulumi.Input[_builtins.int],
        framerate_numerator: pulumi.Input[_builtins.int],
        adaptive_quantization: Optional[pulumi.Input[_builtins.str]] = ...,
        afd_signaling: Optional[pulumi.Input[_builtins.str]] = ...,
        alternative_transfer_function: Optional[pulumi.Input[_builtins.str]] = ...,
        buf_size: Optional[pulumi.Input[_builtins.int]] = ...,
        color_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        color_space_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgs
            ]
        ] = ...,
        filter_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgs
            ]
        ] = ...,
        fixed_afd: Optional[pulumi.Input[_builtins.str]] = ...,
        flicker_aq: Optional[pulumi.Input[_builtins.str]] = ...,
        gop_closed_cadence: Optional[pulumi.Input[_builtins.int]] = ...,
        gop_size: Optional[pulumi.Input[_builtins.float]] = ...,
        gop_size_units: Optional[pulumi.Input[_builtins.str]] = ...,
        level: Optional[pulumi.Input[_builtins.str]] = ...,
        look_ahead_rate_control: Optional[pulumi.Input[_builtins.str]] = ...,
        max_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        min_i_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        min_qp: Optional[pulumi.Input[_builtins.int]] = ...,
        mv_over_picture_boundaries: Optional[pulumi.Input[_builtins.str]] = ...,
        mv_temporal_predictor: Optional[pulumi.Input[_builtins.str]] = ...,
        par_denominator: Optional[pulumi.Input[_builtins.int]] = ...,
        par_numerator: Optional[pulumi.Input[_builtins.int]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        qvbr_quality_level: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_control_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scene_change_detect: Optional[pulumi.Input[_builtins.str]] = ...,
        slices: Optional[pulumi.Input[_builtins.int]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_height: Optional[pulumi.Input[_builtins.int]] = ...,
        tile_padding: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_width: Optional[pulumi.Input[_builtins.int]] = ...,
        timecode_burnin_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgs
            ]
        ] = ...,
        timecode_insertion: Optional[pulumi.Input[_builtins.str]] = ...,
        treeblock_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> pulumi.Input[_builtins.int]: ...
    @bitrate.setter
    def bitrate(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="framerateDenominator")
    def framerate_denominator(self) -> pulumi.Input[_builtins.int]: ...
    @framerate_denominator.setter
    def framerate_denominator(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="framerateNumerator")
    def framerate_numerator(self) -> pulumi.Input[_builtins.int]: ...
    @framerate_numerator.setter
    def framerate_numerator(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="adaptiveQuantization")
    def adaptive_quantization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @adaptive_quantization.setter
    def adaptive_quantization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="afdSignaling")
    def afd_signaling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @afd_signaling.setter
    def afd_signaling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="alternativeTransferFunction")
    def alternative_transfer_function(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alternative_transfer_function.setter
    def alternative_transfer_function(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bufSize")
    def buf_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @buf_size.setter
    def buf_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="colorMetadata")
    def color_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @color_metadata.setter
    def color_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="colorSpaceSettings")
    def color_space_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgs
        ]
    ]: ...
    @color_space_settings.setter
    def color_space_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterSettings")
    def filter_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgs
        ]
    ]: ...
    @filter_settings.setter
    def filter_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixedAfd")
    def fixed_afd(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_afd.setter
    def fixed_afd(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flickerAq")
    def flicker_aq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flicker_aq.setter
    def flicker_aq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gopClosedCadence")
    def gop_closed_cadence(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gop_closed_cadence.setter
    def gop_closed_cadence(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gopSize")
    def gop_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gop_size.setter
    def gop_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="gopSizeUnits")
    def gop_size_units(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gop_size_units.setter
    def gop_size_units(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lookAheadRateControl")
    def look_ahead_rate_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @look_ahead_rate_control.setter
    def look_ahead_rate_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBitrate")
    def max_bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_bitrate.setter
    def max_bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minIInterval")
    def min_i_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_i_interval.setter
    def min_i_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minQp")
    def min_qp(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_qp.setter
    def min_qp(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="mvOverPictureBoundaries")
    def mv_over_picture_boundaries(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mv_over_picture_boundaries.setter
    def mv_over_picture_boundaries(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mvTemporalPredictor")
    def mv_temporal_predictor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mv_temporal_predictor.setter
    def mv_temporal_predictor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parDenominator")
    def par_denominator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @par_denominator.setter
    def par_denominator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parNumerator")
    def par_numerator(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @par_numerator.setter
    def par_numerator(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qvbrQualityLevel")
    def qvbr_quality_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @qvbr_quality_level.setter
    def qvbr_quality_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rate_control_mode.setter
    def rate_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scan_type.setter
    def scan_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sceneChangeDetect")
    def scene_change_detect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scene_change_detect.setter
    def scene_change_detect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def slices(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slices.setter
    def slices(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tileHeight")
    def tile_height(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tile_height.setter
    def tile_height(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tilePadding")
    def tile_padding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tile_padding.setter
    def tile_padding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tileWidth")
    def tile_width(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tile_width.setter
    def tile_width(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninSettings")
    def timecode_burnin_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgs
        ]
    ]: ...
    @timecode_burnin_settings.setter
    def timecode_burnin_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timecodeInsertion")
    def timecode_insertion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timecode_insertion.setter
    def timecode_insertion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="treeblockSize")
    def treeblock_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @treeblock_size.setter
    def treeblock_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgsDict(
    TypedDict
):
    color_space_passthrough_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgsDict
        ]
    ]
    dolby_vision81_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgsDict
        ]
    ]
    hdr10_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgsDict
        ]
    ]
    rec601_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgsDict
        ]
    ]
    rec709_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsArgs:
    def __init__(
        __self__,
        *,
        color_space_passthrough_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgs
            ]
        ] = ...,
        dolby_vision81_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgs
            ]
        ] = ...,
        hdr10_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgs
            ]
        ] = ...,
        rec601_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgs
            ]
        ] = ...,
        rec709_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="colorSpacePassthroughSettings")
    def color_space_passthrough_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgs
        ]
    ]: ...
    @color_space_passthrough_settings.setter
    def color_space_passthrough_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dolbyVision81Settings")
    def dolby_vision81_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgs
        ]
    ]: ...
    @dolby_vision81_settings.setter
    def dolby_vision81_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hdr10Settings")
    def hdr10_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgs
        ]
    ]: ...
    @hdr10_settings.setter
    def hdr10_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rec601Settings")
    def rec601_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgs
        ]
    ]: ...
    @rec601_settings.setter
    def rec601_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rec709Settings")
    def rec709_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgs
        ]
    ]: ...
    @rec709_settings.setter
    def rec709_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81SettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgsDict(
    TypedDict
):
    max_cll: NotRequired[pulumi.Input[_builtins.int]]
    max_fall: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10SettingsArgs:
    def __init__(
        __self__,
        *,
        max_cll: Optional[pulumi.Input[_builtins.int]] = ...,
        max_fall: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCll")
    def max_cll(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_cll.setter
    def max_cll(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFall")
    def max_fall(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_fall.setter
    def max_fall(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601SettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709SettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgsDict(
    TypedDict
):
    temporal_filter_settings: NotRequired[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsArgs:
    def __init__(
        __self__,
        *,
        temporal_filter_settings: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="temporalFilterSettings")
    def temporal_filter_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgs
        ]
    ]: ...
    @temporal_filter_settings.setter
    def temporal_filter_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgs
            ]
        ],
    ): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgsDict(
    TypedDict
):
    post_filter_sharpening: NotRequired[pulumi.Input[_builtins.str]]
    strength: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettingsArgs:
    def __init__(
        __self__,
        *,
        post_filter_sharpening: Optional[pulumi.Input[_builtins.str]] = ...,
        strength: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postFilterSharpening")
    def post_filter_sharpening(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_filter_sharpening.setter
    def post_filter_sharpening(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def strength(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strength.setter
    def strength(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgsDict(
    TypedDict
):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    timecode_burnin_font_size: NotRequired[pulumi.Input[_builtins.str]]
    timecode_burnin_position: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettingsArgs:
    def __init__(
        __self__,
        *,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        timecode_burnin_font_size: Optional[pulumi.Input[_builtins.str]] = ...,
        timecode_burnin_position: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninFontSize")
    def timecode_burnin_font_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timecode_burnin_font_size.setter
    def timecode_burnin_font_size(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninPosition")
    def timecode_burnin_position(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timecode_burnin_position.setter
    def timecode_burnin_position(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChannelInputAttachmentArgsDict(TypedDict):
    input_attachment_name: pulumi.Input[_builtins.str]
    input_id: pulumi.Input[_builtins.str]
    automatic_input_failover_settings: NotRequired[
        pulumi.Input[ChannelInputAttachmentAutomaticInputFailoverSettingsArgsDict]
    ]
    input_settings: NotRequired[
        pulumi.Input[ChannelInputAttachmentInputSettingsArgsDict]
    ]

@pulumi.input_type
class ChannelInputAttachmentArgs:
    def __init__(
        __self__,
        *,
        input_attachment_name: pulumi.Input[_builtins.str],
        input_id: pulumi.Input[_builtins.str],
        automatic_input_failover_settings: Optional[
            pulumi.Input[ChannelInputAttachmentAutomaticInputFailoverSettingsArgs]
        ] = ...,
        input_settings: Optional[
            pulumi.Input[ChannelInputAttachmentInputSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputAttachmentName")
    def input_attachment_name(self) -> pulumi.Input[_builtins.str]: ...
    @input_attachment_name.setter
    def input_attachment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputId")
    def input_id(self) -> pulumi.Input[_builtins.str]: ...
    @input_id.setter
    def input_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="automaticInputFailoverSettings")
    def automatic_input_failover_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelInputAttachmentAutomaticInputFailoverSettingsArgs]
    ]: ...
    @automatic_input_failover_settings.setter
    def automatic_input_failover_settings(
        self,
        value: Optional[
            pulumi.Input[ChannelInputAttachmentAutomaticInputFailoverSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputSettings")
    def input_settings(
        self,
    ) -> Optional[pulumi.Input[ChannelInputAttachmentInputSettingsArgs]]: ...
    @input_settings.setter
    def input_settings(
        self, value: Optional[pulumi.Input[ChannelInputAttachmentInputSettingsArgs]]
    ): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsArgsDict(TypedDict):
    secondary_input_id: pulumi.Input[_builtins.str]
    error_clear_time_msec: NotRequired[pulumi.Input[_builtins.int]]
    failover_conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgsDict
                ]
            ]
        ]
    ]
    input_preference: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsArgs:
    def __init__(
        __self__,
        *,
        secondary_input_id: pulumi.Input[_builtins.str],
        error_clear_time_msec: Optional[pulumi.Input[_builtins.int]] = ...,
        failover_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgs
                    ]
                ]
            ]
        ] = ...,
        input_preference: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secondaryInputId")
    def secondary_input_id(self) -> pulumi.Input[_builtins.str]: ...
    @secondary_input_id.setter
    def secondary_input_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="errorClearTimeMsec")
    def error_clear_time_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @error_clear_time_msec.setter
    def error_clear_time_msec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverConditions")
    def failover_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgs
                ]
            ]
        ]
    ]: ...
    @failover_conditions.setter
    def failover_conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputPreference")
    def input_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_preference.setter
    def input_preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgsDict(
    TypedDict
):
    failover_condition_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionArgs:
    def __init__(
        __self__,
        *,
        failover_condition_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverConditionSettings")
    def failover_condition_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgs
        ]
    ]: ...
    @failover_condition_settings.setter
    def failover_condition_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgsDict(
    TypedDict
):
    audio_silence_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgsDict
        ]
    ]
    input_loss_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgsDict
        ]
    ]
    video_black_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_silence_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgs
            ]
        ] = ...,
        input_loss_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgs
            ]
        ] = ...,
        video_black_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSilenceSettings")
    def audio_silence_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgs
        ]
    ]: ...
    @audio_silence_settings.setter
    def audio_silence_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputLossSettings")
    def input_loss_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgs
        ]
    ]: ...
    @input_loss_settings.setter
    def input_loss_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="videoBlackSettings")
    def video_black_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgs
        ]
    ]: ...
    @video_black_settings.setter
    def video_black_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgsDict(
    TypedDict
):
    audio_selector_name: pulumi.Input[_builtins.str]
    audio_silence_threshold_msec: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_selector_name: pulumi.Input[_builtins.str],
        audio_silence_threshold_msec: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectorName")
    def audio_selector_name(self) -> pulumi.Input[_builtins.str]: ...
    @audio_selector_name.setter
    def audio_selector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="audioSilenceThresholdMsec")
    def audio_silence_threshold_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @audio_silence_threshold_msec.setter
    def audio_silence_threshold_msec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgsDict(
    TypedDict
):
    input_loss_threshold_msec: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettingsArgs:
    def __init__(
        __self__,
        *,
        input_loss_threshold_msec: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputLossThresholdMsec")
    def input_loss_threshold_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @input_loss_threshold_msec.setter
    def input_loss_threshold_msec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgsDict(
    TypedDict
):
    black_detect_threshold: NotRequired[pulumi.Input[_builtins.float]]
    video_black_threshold_msec: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettingsArgs:
    def __init__(
        __self__,
        *,
        black_detect_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        video_black_threshold_msec: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blackDetectThreshold")
    def black_detect_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @black_detect_threshold.setter
    def black_detect_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="videoBlackThresholdMsec")
    def video_black_threshold_msec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @video_black_threshold_msec.setter
    def video_black_threshold_msec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentInputSettingsArgsDict(TypedDict):
    audio_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ChannelInputAttachmentInputSettingsAudioSelectorArgsDict]
            ]
        ]
    ]
    caption_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ChannelInputAttachmentInputSettingsCaptionSelectorArgsDict]
            ]
        ]
    ]
    deblock_filter: NotRequired[pulumi.Input[_builtins.str]]
    denoise_filter: NotRequired[pulumi.Input[_builtins.str]]
    filter_strength: NotRequired[pulumi.Input[_builtins.int]]
    input_filter: NotRequired[pulumi.Input[_builtins.str]]
    network_input_settings: NotRequired[
        pulumi.Input[ChannelInputAttachmentInputSettingsNetworkInputSettingsArgsDict]
    ]
    scte35_pid: NotRequired[pulumi.Input[_builtins.int]]
    smpte2038_data_preference: NotRequired[pulumi.Input[_builtins.str]]
    source_end_behavior: NotRequired[pulumi.Input[_builtins.str]]
    video_selector: NotRequired[
        pulumi.Input[ChannelInputAttachmentInputSettingsVideoSelectorArgsDict]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ChannelInputAttachmentInputSettingsAudioSelectorArgs]
                ]
            ]
        ] = ...,
        caption_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ChannelInputAttachmentInputSettingsCaptionSelectorArgs]
                ]
            ]
        ] = ...,
        deblock_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        denoise_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_strength: Optional[pulumi.Input[_builtins.int]] = ...,
        input_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        network_input_settings: Optional[
            pulumi.Input[ChannelInputAttachmentInputSettingsNetworkInputSettingsArgs]
        ] = ...,
        scte35_pid: Optional[pulumi.Input[_builtins.int]] = ...,
        smpte2038_data_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        source_end_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        video_selector: Optional[
            pulumi.Input[ChannelInputAttachmentInputSettingsVideoSelectorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectors")
    def audio_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ChannelInputAttachmentInputSettingsAudioSelectorArgs]]
        ]
    ]: ...
    @audio_selectors.setter
    def audio_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ChannelInputAttachmentInputSettingsAudioSelectorArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="captionSelectors")
    def caption_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ChannelInputAttachmentInputSettingsCaptionSelectorArgs]
            ]
        ]
    ]: ...
    @caption_selectors.setter
    def caption_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ChannelInputAttachmentInputSettingsCaptionSelectorArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deblockFilter")
    def deblock_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deblock_filter.setter
    def deblock_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="denoiseFilter")
    def denoise_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @denoise_filter.setter
    def denoise_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterStrength")
    def filter_strength(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @filter_strength.setter
    def filter_strength(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inputFilter")
    def input_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_filter.setter
    def input_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInputSettings")
    def network_input_settings(
        self,
    ) -> Optional[
        pulumi.Input[ChannelInputAttachmentInputSettingsNetworkInputSettingsArgs]
    ]: ...
    @network_input_settings.setter
    def network_input_settings(
        self,
        value: Optional[
            pulumi.Input[ChannelInputAttachmentInputSettingsNetworkInputSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scte35_pid.setter
    def scte35_pid(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="smpte2038DataPreference")
    def smpte2038_data_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @smpte2038_data_preference.setter
    def smpte2038_data_preference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceEndBehavior")
    def source_end_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_end_behavior.setter
    def source_end_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="videoSelector")
    def video_selector(
        self,
    ) -> Optional[
        pulumi.Input[ChannelInputAttachmentInputSettingsVideoSelectorArgs]
    ]: ...
    @video_selector.setter
    def video_selector(
        self,
        value: Optional[
            pulumi.Input[ChannelInputAttachmentInputSettingsVideoSelectorArgs]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsAudioSelectorArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    selector_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        selector_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="selectorSettings")
    def selector_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgs
        ]
    ]: ...
    @selector_settings.setter
    def selector_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgsDict(
    TypedDict
):
    audio_hls_rendition_selection: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgsDict
        ]
    ]
    audio_language_selection: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgsDict
        ]
    ]
    audio_pid_selection: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgsDict
        ]
    ]
    audio_track_selection: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_hls_rendition_selection: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgs
            ]
        ] = ...,
        audio_language_selection: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgs
            ]
        ] = ...,
        audio_pid_selection: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgs
            ]
        ] = ...,
        audio_track_selection: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioHlsRenditionSelection")
    def audio_hls_rendition_selection(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgs
        ]
    ]: ...
    @audio_hls_rendition_selection.setter
    def audio_hls_rendition_selection(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioLanguageSelection")
    def audio_language_selection(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgs
        ]
    ]: ...
    @audio_language_selection.setter
    def audio_language_selection(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioPidSelection")
    def audio_pid_selection(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgs
        ]
    ]: ...
    @audio_pid_selection.setter
    def audio_pid_selection(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="audioTrackSelection")
    def audio_track_selection(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgs
        ]
    ]: ...
    @audio_track_selection.setter
    def audio_track_selection(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgsDict(
    TypedDict
):
    group_id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelectionArgs:
    def __init__(
        __self__,
        *,
        group_id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]: ...
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgsDict(
    TypedDict
):
    language_code: pulumi.Input[_builtins.str]
    language_selection_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelectionArgs:
    def __init__(
        __self__,
        *,
        language_code: pulumi.Input[_builtins.str],
        language_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]: ...
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="languageSelectionPolicy")
    def language_selection_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_selection_policy.setter
    def language_selection_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgsDict(
    TypedDict
):
    pid: pulumi.Input[_builtins.int]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelectionArgs:
    def __init__(__self__, *, pid: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> pulumi.Input[_builtins.int]: ...
    @pid.setter
    def pid(self, value: pulumi.Input[_builtins.int]): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgsDict(
    TypedDict
):
    tracks: pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgsDict
            ]
        ]
    ]
    dolby_e_decode: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionArgs:
    def __init__(
        __self__,
        *,
        tracks: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgs
                ]
            ]
        ],
        dolby_e_decode: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tracks(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgs
            ]
        ]
    ]: ...
    @tracks.setter
    def tracks(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dolbyEDecode")
    def dolby_e_decode(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgs
        ]
    ]: ...
    @dolby_e_decode.setter
    def dolby_e_decode(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgsDict(
    TypedDict
):
    program_selection: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecodeArgs:
    def __init__(
        __self__, *, program_selection: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="programSelection")
    def program_selection(self) -> pulumi.Input[_builtins.str]: ...
    @program_selection.setter
    def program_selection(self, value: pulumi.Input[_builtins.str]): ...

class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgsDict(
    TypedDict
):
    track: pulumi.Input[_builtins.int]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrackArgs:
    def __init__(__self__, *, track: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def track(self) -> pulumi.Input[_builtins.int]: ...
    @track.setter
    def track(self, value: pulumi.Input[_builtins.int]): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    selector_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        selector_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectorSettings")
    def selector_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgs
        ]
    ]: ...
    @selector_settings.setter
    def selector_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgsDict(
    TypedDict
):
    ancillary_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgsDict
        ]
    ]
    arib_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgsDict
        ]
    ]
    dvb_sub_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgsDict
        ]
    ]
    embedded_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgsDict
        ]
    ]
    scte20_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgsDict
        ]
    ]
    scte27_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgsDict
        ]
    ]
    teletext_source_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsArgs:
    def __init__(
        __self__,
        *,
        ancillary_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgs
            ]
        ] = ...,
        arib_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgs
            ]
        ] = ...,
        dvb_sub_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgs
            ]
        ] = ...,
        embedded_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgs
            ]
        ] = ...,
        scte20_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgs
            ]
        ] = ...,
        scte27_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgs
            ]
        ] = ...,
        teletext_source_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ancillarySourceSettings")
    def ancillary_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgs
        ]
    ]: ...
    @ancillary_source_settings.setter
    def ancillary_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aribSourceSettings")
    def arib_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgs
        ]
    ]: ...
    @arib_source_settings.setter
    def arib_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dvbSubSourceSettings")
    def dvb_sub_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgs
        ]
    ]: ...
    @dvb_sub_source_settings.setter
    def dvb_sub_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="embeddedSourceSettings")
    def embedded_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgs
        ]
    ]: ...
    @embedded_source_settings.setter
    def embedded_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scte20SourceSettings")
    def scte20_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgs
        ]
    ]: ...
    @scte20_source_settings.setter
    def scte20_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scte27SourceSettings")
    def scte27_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgs
        ]
    ]: ...
    @scte27_source_settings.setter
    def scte27_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="teletextSourceSettings")
    def teletext_source_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgs
        ]
    ]: ...
    @teletext_source_settings.setter
    def teletext_source_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgs
            ]
        ],
    ): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgsDict(
    TypedDict
):
    source_ancillary_channel_number: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettingsArgs:
    def __init__(
        __self__,
        *,
        source_ancillary_channel_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceAncillaryChannelNumber")
    def source_ancillary_channel_number(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @source_ancillary_channel_number.setter
    def source_ancillary_channel_number(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettingsArgs:
    def __init__(__self__) -> None: ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgsDict(
    TypedDict
):
    ocr_language: NotRequired[pulumi.Input[_builtins.str]]
    pid: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettingsArgs:
    def __init__(
        __self__,
        *,
        ocr_language: Optional[pulumi.Input[_builtins.str]] = ...,
        pid: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ocrLanguage")
    def ocr_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocr_language.setter
    def ocr_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pid.setter
    def pid(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgsDict(
    TypedDict
):
    convert608_to708: NotRequired[pulumi.Input[_builtins.str]]
    scte20_detection: NotRequired[pulumi.Input[_builtins.str]]
    source608_channel_number: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettingsArgs:
    def __init__(
        __self__,
        *,
        convert608_to708: Optional[pulumi.Input[_builtins.str]] = ...,
        scte20_detection: Optional[pulumi.Input[_builtins.str]] = ...,
        source608_channel_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="convert608To708")
    def convert608_to708(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @convert608_to708.setter
    def convert608_to708(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scte20Detection")
    def scte20_detection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte20_detection.setter
    def scte20_detection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="source608ChannelNumber")
    def source608_channel_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @source608_channel_number.setter
    def source608_channel_number(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgsDict(
    TypedDict
):
    convert608_to708: NotRequired[pulumi.Input[_builtins.str]]
    source608_channel_number: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettingsArgs:
    def __init__(
        __self__,
        *,
        convert608_to708: Optional[pulumi.Input[_builtins.str]] = ...,
        source608_channel_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="convert608To708")
    def convert608_to708(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @convert608_to708.setter
    def convert608_to708(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="source608ChannelNumber")
    def source608_channel_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @source608_channel_number.setter
    def source608_channel_number(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgsDict(
    TypedDict
):
    ocr_language: NotRequired[pulumi.Input[_builtins.str]]
    pid: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettingsArgs:
    def __init__(
        __self__,
        *,
        ocr_language: Optional[pulumi.Input[_builtins.str]] = ...,
        pid: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ocrLanguage")
    def ocr_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocr_language.setter
    def ocr_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pid.setter
    def pid(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgsDict(
    TypedDict
):
    output_rectangle: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgsDict
        ]
    ]
    page_number: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsArgs:
    def __init__(
        __self__,
        *,
        output_rectangle: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgs
            ]
        ] = ...,
        page_number: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputRectangle")
    def output_rectangle(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgs
        ]
    ]: ...
    @output_rectangle.setter
    def output_rectangle(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @page_number.setter
    def page_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgsDict(
    TypedDict
):
    height: pulumi.Input[_builtins.float]
    left_offset: pulumi.Input[_builtins.float]
    top_offset: pulumi.Input[_builtins.float]
    width: pulumi.Input[_builtins.float]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangleArgs:
    def __init__(
        __self__,
        *,
        height: pulumi.Input[_builtins.float],
        left_offset: pulumi.Input[_builtins.float],
        top_offset: pulumi.Input[_builtins.float],
        width: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> pulumi.Input[_builtins.float]: ...
    @height.setter
    def height(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="leftOffset")
    def left_offset(self) -> pulumi.Input[_builtins.float]: ...
    @left_offset.setter
    def left_offset(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="topOffset")
    def top_offset(self) -> pulumi.Input[_builtins.float]: ...
    @top_offset.setter
    def top_offset(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> pulumi.Input[_builtins.float]: ...
    @width.setter
    def width(self, value: pulumi.Input[_builtins.float]): ...

class ChannelInputAttachmentInputSettingsNetworkInputSettingsArgsDict(TypedDict):
    hls_input_settings: NotRequired[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgsDict
        ]
    ]
    server_validation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsNetworkInputSettingsArgs:
    def __init__(
        __self__,
        *,
        hls_input_settings: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgs
            ]
        ] = ...,
        server_validation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsInputSettings")
    def hls_input_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgs
        ]
    ]: ...
    @hls_input_settings.setter
    def hls_input_settings(
        self,
        value: Optional[
            pulumi.Input[
                ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverValidation")
    def server_validation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_validation.setter
    def server_validation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgsDict(
    TypedDict
):
    bandwidth: NotRequired[pulumi.Input[_builtins.int]]
    buffer_segments: NotRequired[pulumi.Input[_builtins.int]]
    retries: NotRequired[pulumi.Input[_builtins.int]]
    retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    scte35_source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettingsArgs:
    def __init__(
        __self__,
        *,
        bandwidth: Optional[pulumi.Input[_builtins.int]] = ...,
        buffer_segments: Optional[pulumi.Input[_builtins.int]] = ...,
        retries: Optional[pulumi.Input[_builtins.int]] = ...,
        retry_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        scte35_source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bufferSegments")
    def buffer_segments(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @buffer_segments.setter
    def buffer_segments(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retries.setter
    def retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_interval.setter
    def retry_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scte35Source")
    def scte35_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scte35_source.setter
    def scte35_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelInputAttachmentInputSettingsVideoSelectorArgsDict(TypedDict):
    color_space: NotRequired[pulumi.Input[_builtins.str]]
    color_space_usage: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelInputAttachmentInputSettingsVideoSelectorArgs:
    def __init__(
        __self__,
        *,
        color_space: Optional[pulumi.Input[_builtins.str]] = ...,
        color_space_usage: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="colorSpace")
    def color_space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @color_space.setter
    def color_space(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="colorSpaceUsage")
    def color_space_usage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @color_space_usage.setter
    def color_space_usage(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelInputSpecificationArgsDict(TypedDict):
    codec: pulumi.Input[_builtins.str]
    input_resolution: pulumi.Input[_builtins.str]
    maximum_bitrate: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelInputSpecificationArgs:
    def __init__(
        __self__,
        *,
        codec: pulumi.Input[_builtins.str],
        input_resolution: pulumi.Input[_builtins.str],
        maximum_bitrate: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> pulumi.Input[_builtins.str]: ...
    @codec.setter
    def codec(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputResolution")
    def input_resolution(self) -> pulumi.Input[_builtins.str]: ...
    @input_resolution.setter
    def input_resolution(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBitrate")
    def maximum_bitrate(self) -> pulumi.Input[_builtins.str]: ...
    @maximum_bitrate.setter
    def maximum_bitrate(self, value: pulumi.Input[_builtins.str]): ...

class ChannelMaintenanceArgsDict(TypedDict):
    maintenance_day: pulumi.Input[_builtins.str]
    maintenance_start_time: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelMaintenanceArgs:
    def __init__(
        __self__,
        *,
        maintenance_day: pulumi.Input[_builtins.str],
        maintenance_start_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceDay")
    def maintenance_day(self) -> pulumi.Input[_builtins.str]: ...
    @maintenance_day.setter
    def maintenance_day(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceStartTime")
    def maintenance_start_time(self) -> pulumi.Input[_builtins.str]: ...
    @maintenance_start_time.setter
    def maintenance_start_time(self, value: pulumi.Input[_builtins.str]): ...

class ChannelVpcArgsDict(TypedDict):
    public_address_allocation_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    availability_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network_interface_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ChannelVpcArgs:
    def __init__(
        __self__,
        *,
        public_address_allocation_ids: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicAddressAllocationIds")
    def public_address_allocation_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @public_address_allocation_ids.setter
    def public_address_allocation_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_interface_ids.setter
    def network_interface_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InputDestinationArgsDict(TypedDict):
    stream_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class InputDestinationArgs:
    def __init__(__self__, *, stream_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): ...

class InputInputDeviceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class InputInputDeviceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class InputMediaConnectFlowArgsDict(TypedDict):
    flow_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class InputMediaConnectFlowArgs:
    def __init__(__self__, *, flow_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowArn")
    def flow_arn(self) -> pulumi.Input[_builtins.str]: ...
    @flow_arn.setter
    def flow_arn(self, value: pulumi.Input[_builtins.str]): ...

class InputSecurityGroupWhitelistRuleArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InputSecurityGroupWhitelistRuleArgs:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InputSourceArgsDict(TypedDict):
    password_param: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class InputSourceArgs:
    def __init__(
        __self__,
        *,
        password_param: pulumi.Input[_builtins.str],
        url: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> pulumi.Input[_builtins.str]: ...
    @password_param.setter
    def password_param(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class InputVpcArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class InputVpcArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MultiplexMultiplexSettingsArgsDict(TypedDict):
    transport_stream_bitrate: pulumi.Input[_builtins.int]
    transport_stream_id: pulumi.Input[_builtins.int]
    maximum_video_buffer_delay_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    transport_stream_reserved_bitrate: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MultiplexMultiplexSettingsArgs:
    def __init__(
        __self__,
        *,
        transport_stream_bitrate: pulumi.Input[_builtins.int],
        transport_stream_id: pulumi.Input[_builtins.int],
        maximum_video_buffer_delay_milliseconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        transport_stream_reserved_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamBitrate")
    def transport_stream_bitrate(self) -> pulumi.Input[_builtins.int]: ...
    @transport_stream_bitrate.setter
    def transport_stream_bitrate(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> pulumi.Input[_builtins.int]: ...
    @transport_stream_id.setter
    def transport_stream_id(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maximumVideoBufferDelayMilliseconds")
    def maximum_video_buffer_delay_milliseconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_video_buffer_delay_milliseconds.setter
    def maximum_video_buffer_delay_milliseconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transportStreamReservedBitrate")
    def transport_stream_reserved_bitrate(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transport_stream_reserved_bitrate.setter
    def transport_stream_reserved_bitrate(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class MultiplexProgramMultiplexProgramSettingsArgsDict(TypedDict):
    preferred_channel_pipeline: pulumi.Input[_builtins.str]
    program_number: pulumi.Input[_builtins.int]
    service_descriptor: NotRequired[
        pulumi.Input[MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgsDict]
    ]
    video_settings: NotRequired[
        pulumi.Input[MultiplexProgramMultiplexProgramSettingsVideoSettingsArgsDict]
    ]

@pulumi.input_type
class MultiplexProgramMultiplexProgramSettingsArgs:
    def __init__(
        __self__,
        *,
        preferred_channel_pipeline: pulumi.Input[_builtins.str],
        program_number: pulumi.Input[_builtins.int],
        service_descriptor: Optional[
            pulumi.Input[MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgs]
        ] = ...,
        video_settings: Optional[
            pulumi.Input[MultiplexProgramMultiplexProgramSettingsVideoSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredChannelPipeline")
    def preferred_channel_pipeline(self) -> pulumi.Input[_builtins.str]: ...
    @preferred_channel_pipeline.setter
    def preferred_channel_pipeline(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="programNumber")
    def program_number(self) -> pulumi.Input[_builtins.int]: ...
    @program_number.setter
    def program_number(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDescriptor")
    def service_descriptor(
        self,
    ) -> Optional[
        pulumi.Input[MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgs]
    ]: ...
    @service_descriptor.setter
    def service_descriptor(
        self,
        value: Optional[
            pulumi.Input[MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="videoSettings")
    def video_settings(
        self,
    ) -> Optional[
        pulumi.Input[MultiplexProgramMultiplexProgramSettingsVideoSettingsArgs]
    ]: ...
    @video_settings.setter
    def video_settings(
        self,
        value: Optional[
            pulumi.Input[MultiplexProgramMultiplexProgramSettingsVideoSettingsArgs]
        ],
    ): ...

class MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgsDict(TypedDict):
    provider_name: pulumi.Input[_builtins.str]
    service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class MultiplexProgramMultiplexProgramSettingsServiceDescriptorArgs:
    def __init__(
        __self__,
        *,
        provider_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[_builtins.str]: ...
    @provider_name.setter
    def provider_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...

class MultiplexProgramMultiplexProgramSettingsVideoSettingsArgsDict(TypedDict):
    constant_bitrate: NotRequired[pulumi.Input[_builtins.int]]
    statmux_settings: NotRequired[
        pulumi.Input[
            MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgsDict
        ]
    ]

@pulumi.input_type
class MultiplexProgramMultiplexProgramSettingsVideoSettingsArgs:
    def __init__(
        __self__,
        *,
        constant_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        statmux_settings: Optional[
            pulumi.Input[
                MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="constantBitrate")
    def constant_bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @constant_bitrate.setter
    def constant_bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="statmuxSettings")
    def statmux_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgs
        ]
    ]: ...
    @statmux_settings.setter
    def statmux_settings(
        self,
        value: Optional[
            pulumi.Input[
                MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgs
            ]
        ],
    ): ...

class MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgsDict(
    TypedDict
):
    maximum_bitrate: NotRequired[pulumi.Input[_builtins.int]]
    minimum_bitrate: NotRequired[pulumi.Input[_builtins.int]]
    priority: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsArgs:
    def __init__(
        __self__,
        *,
        maximum_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_bitrate: Optional[pulumi.Input[_builtins.int]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBitrate")
    def maximum_bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_bitrate.setter
    def maximum_bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumBitrate")
    def minimum_bitrate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_bitrate.setter
    def minimum_bitrate(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MultiplexProgramTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MultiplexProgramTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
