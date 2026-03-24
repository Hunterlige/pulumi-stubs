import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ChannelCdiInputSpecification",
    "ChannelDestination",
    "ChannelDestinationMediaPackageSetting",
    "ChannelDestinationMultiplexSettings",
    "ChannelDestinationSetting",
    "ChannelEncoderSettings",
    "ChannelEncoderSettingsAudioDescription",
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
    "ChannelEncoderSettingsAvailBlanking",
    ...,
    "ChannelEncoderSettingsCaptionDescription",
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
    "ChannelEncoderSettingsGlobalConfiguration",
    ...,
    ...,
    "ChannelEncoderSettingsMotionGraphicsConfiguration",
    ...,
    ...,
    "ChannelEncoderSettingsNielsenConfiguration",
    "ChannelEncoderSettingsOutputGroup",
    "ChannelEncoderSettingsOutputGroupOutput",
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
    "ChannelEncoderSettingsTimecodeConfig",
    "ChannelEncoderSettingsVideoDescription",
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
    "ChannelInputAttachment",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelInputAttachmentInputSettings",
    "ChannelInputAttachmentInputSettingsAudioSelector",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ChannelInputAttachmentInputSettingsCaptionSelector",
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
    "ChannelInputAttachmentInputSettingsVideoSelector",
    "ChannelInputSpecification",
    "ChannelMaintenance",
    "ChannelVpc",
    "InputDestination",
    "InputInputDevice",
    "InputMediaConnectFlow",
    "InputSecurityGroupWhitelistRule",
    "InputSource",
    "InputVpc",
    "MultiplexMultiplexSettings",
    "MultiplexProgramMultiplexProgramSettings",
    ...,
    ...,
    ...,
    "MultiplexProgramTimeouts",
    "GetInputDestinationResult",
    "GetInputDestinationVpcResult",
    "GetInputInputDeviceResult",
    "GetInputMediaConnectFlowResult",
    "GetInputSourceResult",
]

@pulumi.output_type
class ChannelCdiInputSpecification(dict):
    def __init__(__self__, *, resolution: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        media_package_settings: Optional[
            Sequence[outputs.ChannelDestinationMediaPackageSetting]
        ] = ...,
        multiplex_settings: Optional[outputs.ChannelDestinationMultiplexSettings] = ...,
        settings: Optional[Sequence[outputs.ChannelDestinationSetting]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageSettings")
    def media_package_settings(
        self,
    ) -> Optional[Sequence[outputs.ChannelDestinationMediaPackageSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="multiplexSettings")
    def multiplex_settings(
        self,
    ) -> Optional[outputs.ChannelDestinationMultiplexSettings]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Sequence[outputs.ChannelDestinationSetting]]: ...

@pulumi.output_type
class ChannelDestinationMediaPackageSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, channel_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelDestinationMultiplexSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, multiplex_id: _builtins.str, program_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiplexId")
    def multiplex_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="programName")
    def program_name(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelDestinationSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password_param: Optional[_builtins.str] = ...,
        stream_name: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_groups: Sequence[outputs.ChannelEncoderSettingsOutputGroup],
        timecode_config: outputs.ChannelEncoderSettingsTimecodeConfig,
        audio_descriptions: Optional[
            Sequence[outputs.ChannelEncoderSettingsAudioDescription]
        ] = ...,
        avail_blanking: Optional[outputs.ChannelEncoderSettingsAvailBlanking] = ...,
        caption_descriptions: Optional[
            Sequence[outputs.ChannelEncoderSettingsCaptionDescription]
        ] = ...,
        global_configuration: Optional[
            outputs.ChannelEncoderSettingsGlobalConfiguration
        ] = ...,
        motion_graphics_configuration: Optional[
            outputs.ChannelEncoderSettingsMotionGraphicsConfiguration
        ] = ...,
        nielsen_configuration: Optional[
            outputs.ChannelEncoderSettingsNielsenConfiguration
        ] = ...,
        video_descriptions: Optional[
            Sequence[outputs.ChannelEncoderSettingsVideoDescription]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputGroups")
    def output_groups(self) -> Sequence[outputs.ChannelEncoderSettingsOutputGroup]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeConfig")
    def timecode_config(self) -> outputs.ChannelEncoderSettingsTimecodeConfig: ...
    @_builtins.property
    @pulumi.getter(name="audioDescriptions")
    def audio_descriptions(
        self,
    ) -> Optional[Sequence[outputs.ChannelEncoderSettingsAudioDescription]]: ...
    @_builtins.property
    @pulumi.getter(name="availBlanking")
    def avail_blanking(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsAvailBlanking]: ...
    @_builtins.property
    @pulumi.getter(name="captionDescriptions")
    def caption_descriptions(
        self,
    ) -> Optional[Sequence[outputs.ChannelEncoderSettingsCaptionDescription]]: ...
    @_builtins.property
    @pulumi.getter(name="globalConfiguration")
    def global_configuration(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsGlobalConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsConfiguration")
    def motion_graphics_configuration(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsMotionGraphicsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenConfiguration")
    def nielsen_configuration(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsNielsenConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="videoDescriptions")
    def video_descriptions(
        self,
    ) -> Optional[Sequence[outputs.ChannelEncoderSettingsVideoDescription]]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_selector_name: _builtins.str,
        name: _builtins.str,
        audio_normalization_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettings
        ] = ...,
        audio_type: Optional[_builtins.str] = ...,
        audio_type_control: Optional[_builtins.str] = ...,
        audio_watermark_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettings
        ] = ...,
        codec_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettings
        ] = ...,
        language_code: Optional[_builtins.str] = ...,
        language_code_control: Optional[_builtins.str] = ...,
        remix_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionRemixSettings
        ] = ...,
        stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectorName")
    def audio_selector_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="audioNormalizationSettings")
    def audio_normalization_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="audioType")
    def audio_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioTypeControl")
    def audio_type_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioWatermarkSettings")
    def audio_watermark_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="codecSettings")
    def codec_settings(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsAudioDescriptionCodecSettings]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageCodeControl")
    def language_code_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remixSettings")
    def remix_settings(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsAudioDescriptionRemixSettings]: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionAudioNormalizationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: Optional[_builtins.str] = ...,
        algorithm_control: Optional[_builtins.str] = ...,
        target_lkfs: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="algorithmControl")
    def algorithm_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetLkfs")
    def target_lkfs(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        nielsen_watermarks_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nielsenWatermarksSettings")
    def nielsen_watermarks_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        nielsen_cbet_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings
        ] = ...,
        nielsen_distribution_type: Optional[_builtins.str] = ...,
        nielsen_naes_ii_nw_settings: Optional[
            Sequence[
                outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSetting
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nielsenCbetSettings")
    def nielsen_cbet_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenDistributionType")
    def nielsen_distribution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenNaesIiNwSettings")
    def nielsen_naes_ii_nw_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSetting
        ]
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cbet_check_digit_string: _builtins.str,
        cbet_stepaside: _builtins.str,
        csid: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cbetCheckDigitString")
    def cbet_check_digit_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cbetStepaside")
    def cbet_stepaside(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def csid(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenNaesIiNwSetting(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, check_digit_string: _builtins.str, sid: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkDigitString")
    def check_digit_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> _builtins.float: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aac_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettings
        ] = ...,
        ac3_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3Settings
        ] = ...,
        eac3_atmos_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettings
        ] = ...,
        eac3_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3Settings
        ] = ...,
        mp2_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2Settings
        ] = ...,
        pass_through_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettings
        ] = ...,
        wav_settings: Optional[
            outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aacSettings")
    def aac_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ac3Settings")
    def ac3_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eac3AtmosSettings")
    def eac3_atmos_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eac3Settings")
    def eac3_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mp2Settings")
    def mp2_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="passThroughSettings")
    def pass_through_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="wavSettings")
    def wav_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsAacSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate: Optional[_builtins.float] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        input_type: Optional[_builtins.str] = ...,
        profile: Optional[_builtins.str] = ...,
        rate_control_mode: Optional[_builtins.str] = ...,
        raw_format: Optional[_builtins.str] = ...,
        sample_rate: Optional[_builtins.float] = ...,
        spec: Optional[_builtins.str] = ...,
        vbr_quality: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputType")
    def input_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rawFormat")
    def raw_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vbrQuality")
    def vbr_quality(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsAc3Settings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate: Optional[_builtins.float] = ...,
        bitstream_mode: Optional[_builtins.str] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        dialnorm: Optional[_builtins.int] = ...,
        drc_profile: Optional[_builtins.str] = ...,
        lfe_filter: Optional[_builtins.str] = ...,
        metadata_control: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="bitstreamMode")
    def bitstream_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="drcProfile")
    def drc_profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lfeFilter")
    def lfe_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataControl")
    def metadata_control(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3AtmosSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate: Optional[_builtins.float] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        dialnorm: Optional[_builtins.float] = ...,
        drc_line: Optional[_builtins.str] = ...,
        drc_rf: Optional[_builtins.str] = ...,
        height_trim: Optional[_builtins.float] = ...,
        surround_trim: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="drcLine")
    def drc_line(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="drcRf")
    def drc_rf(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="heightTrim")
    def height_trim(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="surroundTrim")
    def surround_trim(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsEac3Settings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attenuation_control: Optional[_builtins.str] = ...,
        bitrate: Optional[_builtins.float] = ...,
        bitstream_mode: Optional[_builtins.str] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        dc_filter: Optional[_builtins.str] = ...,
        dialnorm: Optional[_builtins.int] = ...,
        drc_line: Optional[_builtins.str] = ...,
        drc_rf: Optional[_builtins.str] = ...,
        lfe_control: Optional[_builtins.str] = ...,
        lfe_filter: Optional[_builtins.str] = ...,
        lo_ro_center_mix_level: Optional[_builtins.float] = ...,
        lo_ro_surround_mix_level: Optional[_builtins.float] = ...,
        lt_rt_center_mix_level: Optional[_builtins.float] = ...,
        lt_rt_surround_mix_level: Optional[_builtins.float] = ...,
        metadata_control: Optional[_builtins.str] = ...,
        passthrough_control: Optional[_builtins.str] = ...,
        phase_control: Optional[_builtins.str] = ...,
        stereo_downmix: Optional[_builtins.str] = ...,
        surround_ex_mode: Optional[_builtins.str] = ...,
        surround_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attenuationControl")
    def attenuation_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="bitstreamMode")
    def bitstream_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dcFilter")
    def dc_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dialnorm(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="drcLine")
    def drc_line(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="drcRf")
    def drc_rf(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lfeControl")
    def lfe_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lfeFilter")
    def lfe_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loRoCenterMixLevel")
    def lo_ro_center_mix_level(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="loRoSurroundMixLevel")
    def lo_ro_surround_mix_level(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="ltRtCenterMixLevel")
    def lt_rt_center_mix_level(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="ltRtSurroundMixLevel")
    def lt_rt_surround_mix_level(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="metadataControl")
    def metadata_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passthroughControl")
    def passthrough_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phaseControl")
    def phase_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stereoDownmix")
    def stereo_downmix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="surroundExMode")
    def surround_ex_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="surroundMode")
    def surround_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsMp2Settings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate: Optional[_builtins.float] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        sample_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsPassThroughSettings(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionCodecSettingsWavSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bit_depth: Optional[_builtins.float] = ...,
        coding_mode: Optional[_builtins.str] = ...,
        sample_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitDepth")
    def bit_depth(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="codingMode")
    def coding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionRemixSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel_mappings: Sequence[
            outputs.ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMapping
        ],
        channels_in: Optional[_builtins.int] = ...,
        channels_out: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelMappings")
    def channel_mappings(
        self,
    ) -> Sequence[
        outputs.ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMapping
    ]: ...
    @_builtins.property
    @pulumi.getter(name="channelsIn")
    def channels_in(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="channelsOut")
    def channels_out(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_channel_levels: Sequence[
            outputs.ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevel
        ],
        output_channel: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputChannelLevels")
    def input_channel_levels(
        self,
    ) -> Sequence[
        outputs.ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevel
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputChannel")
    def output_channel(self) -> _builtins.int: ...

@pulumi.output_type
class ChannelEncoderSettingsAudioDescriptionRemixSettingsChannelMappingInputChannelLevel(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gain: _builtins.int, input_channel: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gain(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="inputChannel")
    def input_channel(self) -> _builtins.int: ...

@pulumi.output_type
class ChannelEncoderSettingsAvailBlanking(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        avail_blanking_image: Optional[
            outputs.ChannelEncoderSettingsAvailBlankingAvailBlankingImage
        ] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availBlankingImage")
    def avail_blanking_image(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsAvailBlankingAvailBlankingImage]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsAvailBlankingAvailBlankingImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        caption_selector_name: _builtins.str,
        name: _builtins.str,
        accessibility: Optional[_builtins.str] = ...,
        destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettings
        ] = ...,
        language_code: Optional[_builtins.str] = ...,
        language_description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captionSelectorName")
    def caption_selector_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def accessibility(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationSettings")
    def destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageDescription")
    def language_description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arib_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettings
        ] = ...,
        burn_in_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettings
        ] = ...,
        dvb_sub_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettings
        ] = ...,
        ebu_tt_d_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettings
        ] = ...,
        embedded_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettings
        ] = ...,
        embedded_plus_scte20_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettings
        ] = ...,
        rtmp_caption_info_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettings
        ] = ...,
        scte20_plus_embedded_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettings
        ] = ...,
        scte27_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettings
        ] = ...,
        smpte_tt_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettings
        ] = ...,
        teletext_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettings
        ] = ...,
        ttml_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettings
        ] = ...,
        webvtt_destination_settings: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aribDestinationSettings")
    def arib_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="burnInDestinationSettings")
    def burn_in_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSubDestinationSettings")
    def dvb_sub_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ebuTtDDestinationSettings")
    def ebu_tt_d_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="embeddedDestinationSettings")
    def embedded_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="embeddedPlusScte20DestinationSettings")
    def embedded_plus_scte20_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rtmpCaptionInfoDestinationSettings")
    def rtmp_caption_info_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scte20PlusEmbeddedDestinationSettings")
    def scte20_plus_embedded_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scte27DestinationSettings")
    def scte27_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="smpteTtDestinationSettings")
    def smpte_tt_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="teletextDestinationSettings")
    def teletext_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ttmlDestinationSettings")
    def ttml_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="webvttDestinationSettings")
    def webvtt_destination_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsAribDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        outline_color: _builtins.str,
        teletext_grid_control: _builtins.str,
        alignment: Optional[_builtins.str] = ...,
        background_color: Optional[_builtins.str] = ...,
        background_opacity: Optional[_builtins.int] = ...,
        font: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFont
        ] = ...,
        font_color: Optional[_builtins.str] = ...,
        font_opacity: Optional[_builtins.int] = ...,
        font_resolution: Optional[_builtins.int] = ...,
        font_size: Optional[_builtins.str] = ...,
        outline_size: Optional[_builtins.int] = ...,
        shadow_color: Optional[_builtins.str] = ...,
        shadow_opacity: Optional[_builtins.int] = ...,
        shadow_x_offset: Optional[_builtins.int] = ...,
        shadow_y_offset: Optional[_builtins.int] = ...,
        x_position: Optional[_builtins.int] = ...,
        y_position: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outlineColor")
    def outline_color(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="teletextGridControl")
    def teletext_grid_control(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def alignment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backgroundColor")
    def background_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backgroundOpacity")
    def background_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def font(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFont
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fontColor")
    def font_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fontOpacity")
    def font_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fontResolution")
    def font_resolution(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outlineSize")
    def outline_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowColor")
    def shadow_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shadowOpacity")
    def shadow_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowXOffset")
    def shadow_x_offset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowYOffset")
    def shadow_y_offset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="xPosition")
    def x_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="yPosition")
    def y_position(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsBurnInDestinationSettingsFont(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alignment: Optional[_builtins.str] = ...,
        background_color: Optional[_builtins.str] = ...,
        background_opacity: Optional[_builtins.int] = ...,
        font: Optional[
            outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFont
        ] = ...,
        font_color: Optional[_builtins.str] = ...,
        font_opacity: Optional[_builtins.int] = ...,
        font_resolution: Optional[_builtins.int] = ...,
        font_size: Optional[_builtins.str] = ...,
        outline_color: Optional[_builtins.str] = ...,
        outline_size: Optional[_builtins.int] = ...,
        shadow_color: Optional[_builtins.str] = ...,
        shadow_opacity: Optional[_builtins.int] = ...,
        shadow_x_offset: Optional[_builtins.int] = ...,
        shadow_y_offset: Optional[_builtins.int] = ...,
        teletext_grid_control: Optional[_builtins.str] = ...,
        x_position: Optional[_builtins.int] = ...,
        y_position: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alignment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backgroundColor")
    def background_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backgroundOpacity")
    def background_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def font(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFont
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fontColor")
    def font_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fontOpacity")
    def font_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fontResolution")
    def font_resolution(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outlineColor")
    def outline_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outlineSize")
    def outline_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowColor")
    def shadow_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shadowOpacity")
    def shadow_opacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowXOffset")
    def shadow_x_offset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shadowYOffset")
    def shadow_y_offset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="teletextGridControl")
    def teletext_grid_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="xPosition")
    def x_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="yPosition")
    def y_position(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsDvbSubDestinationSettingsFont(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEbuTtDDestinationSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        copyright_holder: Optional[_builtins.str] = ...,
        fill_line_gap: Optional[_builtins.str] = ...,
        font_family: Optional[_builtins.str] = ...,
        style_control: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyrightHolder")
    def copyright_holder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fillLineGap")
    def fill_line_gap(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fontFamily")
    def font_family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsEmbeddedPlusScte20DestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsRtmpCaptionInfoDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte20PlusEmbeddedDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsScte27DestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsSmpteTtDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTeletextDestinationSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsTtmlDestinationSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, style_control: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsCaptionDescriptionDestinationSettingsWebvttDestinationSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, style_control: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="styleControl")
    def style_control(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsGlobalConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        initial_audio_gain: Optional[_builtins.int] = ...,
        input_end_action: Optional[_builtins.str] = ...,
        input_loss_behavior: Optional[
            outputs.ChannelEncoderSettingsGlobalConfigurationInputLossBehavior
        ] = ...,
        output_locking_mode: Optional[_builtins.str] = ...,
        output_timing_source: Optional[_builtins.str] = ...,
        support_low_framerate_inputs: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialAudioGain")
    def initial_audio_gain(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inputEndAction")
    def input_end_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossBehavior")
    def input_loss_behavior(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsGlobalConfigurationInputLossBehavior
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputLockingMode")
    def output_locking_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputTimingSource")
    def output_timing_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportLowFramerateInputs")
    def support_low_framerate_inputs(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsGlobalConfigurationInputLossBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        black_frame_msec: Optional[_builtins.int] = ...,
        input_loss_image_color: Optional[_builtins.str] = ...,
        input_loss_image_slate: Optional[
            outputs.ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlate
        ] = ...,
        input_loss_image_type: Optional[_builtins.str] = ...,
        repeat_frame_msec: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blackFrameMsec")
    def black_frame_msec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageColor")
    def input_loss_image_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageSlate")
    def input_loss_image_slate(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlate
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossImageType")
    def input_loss_image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repeatFrameMsec")
    def repeat_frame_msec(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlate(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsMotionGraphicsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        motion_graphics_settings: outputs.ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettings,
        motion_graphics_insertion: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsSettings")
    def motion_graphics_settings(
        self,
    ) -> (
        outputs.ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettings
    ): ...
    @_builtins.property
    @pulumi.getter(name="motionGraphicsInsertion")
    def motion_graphics_insertion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        html_motion_graphics_settings: Optional[
            outputs.ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="htmlMotionGraphicsSettings")
    def html_motion_graphics_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsMotionGraphicsConfigurationMotionGraphicsSettingsHtmlMotionGraphicsSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsNielsenConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        distributor_id: Optional[_builtins.str] = ...,
        nielsen_pcm_to_id3_tagging: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributorId")
    def distributor_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenPcmToId3Tagging")
    def nielsen_pcm_to_id3_tagging(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_group_settings: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettings,
        outputs: Sequence[outputs.ChannelEncoderSettingsOutputGroupOutput],
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputGroupSettings")
    def output_group_settings(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettings: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Sequence[outputs.ChannelEncoderSettingsOutputGroupOutput]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_settings: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettings,
        audio_description_names: Optional[Sequence[_builtins.str]] = ...,
        caption_description_names: Optional[Sequence[_builtins.str]] = ...,
        output_name: Optional[_builtins.str] = ...,
        video_description_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSettings")
    def output_settings(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettings: ...
    @_builtins.property
    @pulumi.getter(name="audioDescriptionNames")
    def audio_description_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="captionDescriptionNames")
    def caption_description_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="videoDescriptionName")
    def video_description_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_group_settings: Optional[
            Sequence[
                outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSetting
            ]
        ] = ...,
        frame_capture_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettings
        ] = ...,
        hls_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettings
        ] = ...,
        media_package_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettings
        ] = ...,
        ms_smooth_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettings
        ] = ...,
        multiplex_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettings
        ] = ...,
        rtmp_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettings
        ] = ...,
        udp_group_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveGroupSettings")
    def archive_group_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSetting
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureGroupSettings")
    def frame_capture_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsGroupSettings")
    def hls_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageGroupSettings")
    def media_package_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="msSmoothGroupSettings")
    def ms_smooth_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="multiplexGroupSettings")
    def multiplex_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rtmpGroupSettings")
    def rtmp_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="udpGroupSettings")
    def udp_group_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestination,
        archive_cdn_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettings
        ] = ...,
        rollover_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestination: ...
    @_builtins.property
    @pulumi.getter(name="archiveCdnSettings")
    def archive_cdn_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rolloverInterval")
    def rollover_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_s3_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3Settings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveS3Settings")
    def archive_s3_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3Settings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingArchiveCdnSettingsArchiveS3Settings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, canned_acl: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsArchiveGroupSettingDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestination,
        frame_capture_cdn_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestination: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureCdnSettings")
    def frame_capture_cdn_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        frame_capture_s3_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3Settings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureS3Settings")
    def frame_capture_s3_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3Settings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsFrameCaptureGroupSettingsFrameCaptureCdnSettingsFrameCaptureS3Settings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, canned_acl: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestination,
        ad_markers: Optional[Sequence[_builtins.str]] = ...,
        base_url_content: Optional[_builtins.str] = ...,
        base_url_content1: Optional[_builtins.str] = ...,
        base_url_manifest: Optional[_builtins.str] = ...,
        base_url_manifest1: Optional[_builtins.str] = ...,
        caption_language_mappings: Optional[
            Sequence[
                outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMapping
            ]
        ] = ...,
        caption_language_setting: Optional[_builtins.str] = ...,
        client_cache: Optional[_builtins.str] = ...,
        codec_specification: Optional[_builtins.str] = ...,
        constant_iv: Optional[_builtins.str] = ...,
        directory_structure: Optional[_builtins.str] = ...,
        discontinuity_tags: Optional[_builtins.str] = ...,
        encryption_type: Optional[_builtins.str] = ...,
        hls_cdn_settings: Optional[
            Sequence[
                outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSetting
            ]
        ] = ...,
        hls_id3_segment_tagging: Optional[_builtins.str] = ...,
        iframe_only_playlists: Optional[_builtins.str] = ...,
        incomplete_segment_behavior: Optional[_builtins.str] = ...,
        index_n_segments: Optional[_builtins.int] = ...,
        input_loss_action: Optional[_builtins.str] = ...,
        iv_in_manifest: Optional[_builtins.str] = ...,
        iv_source: Optional[_builtins.str] = ...,
        keep_segments: Optional[_builtins.int] = ...,
        key_format: Optional[_builtins.str] = ...,
        key_format_versions: Optional[_builtins.str] = ...,
        key_provider_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettings
        ] = ...,
        manifest_compression: Optional[_builtins.str] = ...,
        manifest_duration_format: Optional[_builtins.str] = ...,
        min_segment_length: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        output_selection: Optional[_builtins.str] = ...,
        program_date_time: Optional[_builtins.str] = ...,
        program_date_time_clock: Optional[_builtins.str] = ...,
        program_date_time_period: Optional[_builtins.int] = ...,
        redundant_manifest: Optional[_builtins.str] = ...,
        segment_length: Optional[_builtins.int] = ...,
        segments_per_subdirectory: Optional[_builtins.int] = ...,
        stream_inf_resolution: Optional[_builtins.str] = ...,
        timed_metadata_id3_frame: Optional[_builtins.str] = ...,
        timed_metadata_id3_period: Optional[_builtins.int] = ...,
        timestamp_delta_milliseconds: Optional[_builtins.int] = ...,
        ts_file_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestination: ...
    @_builtins.property
    @pulumi.getter(name="adMarkers")
    def ad_markers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="baseUrlContent")
    def base_url_content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseUrlContent1")
    def base_url_content1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseUrlManifest")
    def base_url_manifest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseUrlManifest1")
    def base_url_manifest1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="captionLanguageMappings")
    def caption_language_mappings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMapping
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="captionLanguageSetting")
    def caption_language_setting(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCache")
    def client_cache(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codecSpecification")
    def codec_specification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="constantIv")
    def constant_iv(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryStructure")
    def directory_structure(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discontinuityTags")
    def discontinuity_tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hlsCdnSettings")
    def hls_cdn_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSetting
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsId3SegmentTagging")
    def hls_id3_segment_tagging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iframeOnlyPlaylists")
    def iframe_only_playlists(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incompleteSegmentBehavior")
    def incomplete_segment_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexNSegments")
    def index_n_segments(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ivInManifest")
    def iv_in_manifest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ivSource")
    def iv_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keepSegments")
    def keep_segments(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="keyFormat")
    def key_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyFormatVersions")
    def key_format_versions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyProviderSettings")
    def key_provider_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="manifestCompression")
    def manifest_compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manifestDurationFormat")
    def manifest_duration_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minSegmentLength")
    def min_segment_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputSelection")
    def output_selection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programDateTime")
    def program_date_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programDateTimeClock")
    def program_date_time_clock(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programDateTimePeriod")
    def program_date_time_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="redundantManifest")
    def redundant_manifest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentLength")
    def segment_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="segmentsPerSubdirectory")
    def segments_per_subdirectory(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="streamInfResolution")
    def stream_inf_resolution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Frame")
    def timed_metadata_id3_frame(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Period")
    def timed_metadata_id3_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timestampDeltaMilliseconds")
    def timestamp_delta_milliseconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tsFileMode")
    def ts_file_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsCaptionLanguageMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        caption_channel: _builtins.int,
        language_code: _builtins.str,
        language_description: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captionChannel")
    def caption_channel(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="languageDescription")
    def language_description(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSetting(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hls_akamai_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettings
        ] = ...,
        hls_basic_put_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettings
        ] = ...,
        hls_media_store_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettings
        ] = ...,
        hls_s3_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3Settings
        ] = ...,
        hls_webdav_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsAkamaiSettings")
    def hls_akamai_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsBasicPutSettings")
    def hls_basic_put_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsMediaStoreSettings")
    def hls_media_store_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsS3Settings")
    def hls_s3_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsWebdavSettings")
    def hls_webdav_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsAkamaiSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[_builtins.int] = ...,
        filecache_duration: Optional[_builtins.int] = ...,
        http_transfer_mode: Optional[_builtins.str] = ...,
        num_retries: Optional[_builtins.int] = ...,
        restart_delay: Optional[_builtins.int] = ...,
        salt: Optional[_builtins.str] = ...,
        token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpTransferMode")
    def http_transfer_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def salt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsBasicPutSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[_builtins.int] = ...,
        filecache_duration: Optional[_builtins.int] = ...,
        num_retries: Optional[_builtins.int] = ...,
        restart_delay: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsMediaStoreSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[_builtins.int] = ...,
        filecache_duration: Optional[_builtins.int] = ...,
        media_store_storage_class: Optional[_builtins.str] = ...,
        num_retries: Optional[_builtins.int] = ...,
        restart_delay: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mediaStoreStorageClass")
    def media_store_storage_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsS3Settings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, canned_acl: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsHlsCdnSettingHlsWebdavSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_retry_interval: Optional[_builtins.int] = ...,
        filecache_duration: Optional[_builtins.int] = ...,
        http_transfer_mode: Optional[_builtins.str] = ...,
        num_retries: Optional[_builtins.int] = ...,
        restart_delay: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpTransferMode")
    def http_transfer_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        static_key_settings: Optional[
            Sequence[
                outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySetting
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="staticKeySettings")
    def static_key_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySetting
        ]
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySetting(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        static_key_value: _builtins.str,
        key_provider_server: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServer
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="staticKeyValue")
    def static_key_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyProviderServer")
    def key_provider_server(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServer
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsHlsGroupSettingsKeyProviderSettingsStaticKeySettingKeyProviderServer(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettings(
    dict
):
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestination,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestination: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMediaPackageGroupSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestination,
        acquisition_point_id: Optional[_builtins.str] = ...,
        audio_only_timecode_control: Optional[_builtins.str] = ...,
        certificate_mode: Optional[_builtins.str] = ...,
        connection_retry_interval: Optional[_builtins.int] = ...,
        event_id: Optional[_builtins.str] = ...,
        event_id_mode: Optional[_builtins.str] = ...,
        event_stop_behavior: Optional[_builtins.str] = ...,
        filecache_duration: Optional[_builtins.int] = ...,
        fragment_length: Optional[_builtins.int] = ...,
        input_loss_action: Optional[_builtins.str] = ...,
        num_retries: Optional[_builtins.int] = ...,
        restart_delay: Optional[_builtins.int] = ...,
        segmentation_mode: Optional[_builtins.str] = ...,
        send_delay_ms: Optional[_builtins.int] = ...,
        sparse_track_type: Optional[_builtins.str] = ...,
        stream_manifest_behavior: Optional[_builtins.str] = ...,
        timestamp_offset: Optional[_builtins.str] = ...,
        timestamp_offset_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestination: ...
    @_builtins.property
    @pulumi.getter(name="acquisitionPointId")
    def acquisition_point_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyTimecodeControl")
    def audio_only_timecode_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="eventId")
    def event_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventIdMode")
    def event_id_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventStopBehavior")
    def event_stop_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filecacheDuration")
    def filecache_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fragmentLength")
    def fragment_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationMode")
    def segmentation_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendDelayMs")
    def send_delay_ms(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sparseTrackType")
    def sparse_track_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamManifestBehavior")
    def stream_manifest_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timestampOffset")
    def timestamp_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timestampOffsetMode")
    def timestamp_offset_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMsSmoothGroupSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsMultiplexGroupSettings(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsRtmpGroupSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ad_markers: Optional[Sequence[_builtins.str]] = ...,
        authentication_scheme: Optional[_builtins.str] = ...,
        cache_full_behavior: Optional[_builtins.str] = ...,
        cache_length: Optional[_builtins.int] = ...,
        caption_data: Optional[_builtins.str] = ...,
        input_loss_action: Optional[_builtins.str] = ...,
        restart_delay: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adMarkers")
    def ad_markers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationScheme")
    def authentication_scheme(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheFullBehavior")
    def cache_full_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheLength")
    def cache_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="captionData")
    def caption_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restartDelay")
    def restart_delay(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputGroupSettingsUdpGroupSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_loss_action: Optional[_builtins.str] = ...,
        timed_metadata_id3_frame: Optional[_builtins.str] = ...,
        timed_metadata_id3_period: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputLossAction")
    def input_loss_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Frame")
    def timed_metadata_id3_frame(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataId3Period")
    def timed_metadata_id3_period(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettings
        ] = ...,
        frame_capture_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettings
        ] = ...,
        hls_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettings
        ] = ...,
        media_package_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettings
        ] = ...,
        ms_smooth_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettings
        ] = ...,
        multiplex_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettings
        ] = ...,
        rtmp_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettings
        ] = ...,
        udp_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveOutputSettings")
    def archive_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureOutputSettings")
    def frame_capture_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hlsOutputSettings")
    def hls_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mediaPackageOutputSettings")
    def media_package_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="msSmoothOutputSettings")
    def ms_smooth_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="multiplexOutputSettings")
    def multiplex_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rtmpOutputSettings")
    def rtmp_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="udpOutputSettings")
    def udp_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettings
        ] = ...,
        extension: Optional[_builtins.str] = ...,
        name_modifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettings
    ]: ...
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        m2ts_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettings
        ] = ...,
        raw_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m2tsSettings")
    def m2ts_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rawSettings")
    def raw_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        absent_input_audio_behavior: Optional[_builtins.str] = ...,
        arib: Optional[_builtins.str] = ...,
        arib_captions_pid: Optional[_builtins.str] = ...,
        arib_captions_pid_control: Optional[_builtins.str] = ...,
        audio_buffer_model: Optional[_builtins.str] = ...,
        audio_frames_per_pes: Optional[_builtins.int] = ...,
        audio_pids: Optional[_builtins.str] = ...,
        audio_stream_type: Optional[_builtins.str] = ...,
        bitrate: Optional[_builtins.int] = ...,
        buffer_model: Optional[_builtins.str] = ...,
        cc_descriptor: Optional[_builtins.str] = ...,
        dvb_nit_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings
        ] = ...,
        dvb_sdt_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings
        ] = ...,
        dvb_sub_pids: Optional[_builtins.str] = ...,
        dvb_tdt_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings
        ] = ...,
        dvb_teletext_pid: Optional[_builtins.str] = ...,
        ebif: Optional[_builtins.str] = ...,
        ebp_audio_interval: Optional[_builtins.str] = ...,
        ebp_lookahead_ms: Optional[_builtins.int] = ...,
        ebp_placement: Optional[_builtins.str] = ...,
        ecm_pid: Optional[_builtins.str] = ...,
        es_rate_in_pes: Optional[_builtins.str] = ...,
        etv_platform_pid: Optional[_builtins.str] = ...,
        etv_signal_pid: Optional[_builtins.str] = ...,
        fragment_time: Optional[_builtins.float] = ...,
        klv: Optional[_builtins.str] = ...,
        klv_data_pids: Optional[_builtins.str] = ...,
        nielsen_id3_behavior: Optional[_builtins.str] = ...,
        null_packet_bitrate: Optional[_builtins.float] = ...,
        pat_interval: Optional[_builtins.int] = ...,
        pcr_control: Optional[_builtins.str] = ...,
        pcr_period: Optional[_builtins.int] = ...,
        pcr_pid: Optional[_builtins.str] = ...,
        pmt_interval: Optional[_builtins.int] = ...,
        pmt_pid: Optional[_builtins.str] = ...,
        program_num: Optional[_builtins.int] = ...,
        rate_mode: Optional[_builtins.str] = ...,
        scte27_pids: Optional[_builtins.str] = ...,
        scte35_control: Optional[_builtins.str] = ...,
        scte35_pid: Optional[_builtins.str] = ...,
        segmentation_markers: Optional[_builtins.str] = ...,
        segmentation_style: Optional[_builtins.str] = ...,
        segmentation_time: Optional[_builtins.float] = ...,
        timed_metadata_behavior: Optional[_builtins.str] = ...,
        timed_metadata_pid: Optional[_builtins.str] = ...,
        transport_stream_id: Optional[_builtins.int] = ...,
        video_pid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="absentInputAudioBehavior")
    def absent_input_audio_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arib(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPid")
    def arib_captions_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPidControl")
    def arib_captions_pid_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioBufferModel")
    def audio_buffer_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioStreamType")
    def audio_stream_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferModel")
    def buffer_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ccDescriptor")
    def cc_descriptor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dvbNitSettings")
    def dvb_nit_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSdtSettings")
    def dvb_sdt_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSubPids")
    def dvb_sub_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dvbTdtSettings")
    def dvb_tdt_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbTeletextPid")
    def dvb_teletext_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ebif(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebpAudioInterval")
    def ebp_audio_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebpLookaheadMs")
    def ebp_lookahead_ms(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ebpPlacement")
    def ebp_placement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="esRateInPes")
    def es_rate_in_pes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etvPlatformPid")
    def etv_platform_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etvSignalPid")
    def etv_signal_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fragmentTime")
    def fragment_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def klv(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="klvDataPids")
    def klv_data_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nullPacketBitrate")
    def null_packet_bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateMode")
    def rate_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte27Pids")
    def scte27_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Control")
    def scte35_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationMarkers")
    def segmentation_markers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationStyle")
    def segmentation_style(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationTime")
    def segmentation_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_id: _builtins.int,
        network_name: _builtins.str,
        rep_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_sdt: Optional[_builtins.str] = ...,
        rep_interval: Optional[_builtins.int] = ...,
        service_name: Optional[_builtins.str] = ...,
        service_provider_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSdt")
    def output_sdt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderName")
    def service_provider_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, rep_interval: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsArchiveOutputSettingsContainerSettingsRawSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsFrameCaptureOutputSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, name_modifier: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hls_settings: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettings,
        h265_packaging_type: Optional[_builtins.str] = ...,
        name_modifier: Optional[_builtins.str] = ...,
        segment_modifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsSettings")
    def hls_settings(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettings: ...
    @_builtins.property
    @pulumi.getter(name="h265PackagingType")
    def h265_packaging_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentModifier")
    def segment_modifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_only_hls_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettings
        ] = ...,
        fmp4_hls_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettings
        ] = ...,
        frame_capture_hls_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettings
        ] = ...,
        standard_hls_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyHlsSettings")
    def audio_only_hls_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fmp4HlsSettings")
    def fmp4_hls_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureHlsSettings")
    def frame_capture_hls_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="standardHlsSettings")
    def standard_hls_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_group_id: Optional[_builtins.str] = ...,
        audio_only_image: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImage
        ] = ...,
        audio_track_type: Optional[_builtins.str] = ...,
        segment_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioGroupId")
    def audio_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioOnlyImage")
    def audio_only_image(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImage
    ]: ...
    @_builtins.property
    @pulumi.getter(name="audioTrackType")
    def audio_track_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentType")
    def segment_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsAudioOnlyHlsSettingsAudioOnlyImage(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password_param: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFmp4HlsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_rendition_sets: Optional[_builtins.str] = ...,
        nielsen_id3_behavior: Optional[_builtins.str] = ...,
        timed_metadata_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioRenditionSets")
    def audio_rendition_sets(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsFrameCaptureHlsSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        m3u8_settings: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8Settings,
        audio_rendition_sets: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m3u8Settings")
    def m3u8_settings(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8Settings: ...
    @_builtins.property
    @pulumi.getter(name="audioRenditionSets")
    def audio_rendition_sets(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsHlsOutputSettingsHlsSettingsStandardHlsSettingsM3u8Settings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_frames_per_pes: Optional[_builtins.int] = ...,
        audio_pids: Optional[_builtins.str] = ...,
        ecm_pid: Optional[_builtins.str] = ...,
        nielsen_id3_behavior: Optional[_builtins.str] = ...,
        pat_interval: Optional[_builtins.int] = ...,
        pcr_control: Optional[_builtins.str] = ...,
        pcr_period: Optional[_builtins.int] = ...,
        pcr_pid: Optional[_builtins.str] = ...,
        pmt_interval: Optional[_builtins.int] = ...,
        pmt_pid: Optional[_builtins.str] = ...,
        program_num: Optional[_builtins.int] = ...,
        scte35_behavior: Optional[_builtins.str] = ...,
        scte35_pid: Optional[_builtins.str] = ...,
        timed_metadata_behavior: Optional[_builtins.str] = ...,
        timed_metadata_pid: Optional[_builtins.str] = ...,
        transport_stream_id: Optional[_builtins.int] = ...,
        video_pid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Behavior")
    def scte35_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMediaPackageOutputSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMsSmoothOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        h265_packaging_type: Optional[_builtins.str] = ...,
        name_modifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="h265PackagingType")
    def h265_packaging_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nameModifier")
    def name_modifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettings(
    dict
):
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestination,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestination: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsMultiplexOutputSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestination,
        certificate_mode: Optional[_builtins.str] = ...,
        connection_retry_interval: Optional[_builtins.int] = ...,
        num_retries: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestination: ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionRetryInterval")
    def connection_retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsRtmpOutputSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_settings: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettings,
        destination: outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestination,
        buffer_msec: Optional[_builtins.int] = ...,
        fec_output_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettings: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestination: ...
    @_builtins.property
    @pulumi.getter(name="bufferMsec")
    def buffer_msec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fecOutputSettings")
    def fec_output_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        m2ts_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="m2tsSettings")
    def m2ts_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        absent_input_audio_behavior: Optional[_builtins.str] = ...,
        arib: Optional[_builtins.str] = ...,
        arib_captions_pid: Optional[_builtins.str] = ...,
        arib_captions_pid_control: Optional[_builtins.str] = ...,
        audio_buffer_model: Optional[_builtins.str] = ...,
        audio_frames_per_pes: Optional[_builtins.int] = ...,
        audio_pids: Optional[_builtins.str] = ...,
        audio_stream_type: Optional[_builtins.str] = ...,
        bitrate: Optional[_builtins.int] = ...,
        buffer_model: Optional[_builtins.str] = ...,
        cc_descriptor: Optional[_builtins.str] = ...,
        dvb_nit_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings
        ] = ...,
        dvb_sdt_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings
        ] = ...,
        dvb_sub_pids: Optional[_builtins.str] = ...,
        dvb_tdt_settings: Optional[
            outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings
        ] = ...,
        dvb_teletext_pid: Optional[_builtins.str] = ...,
        ebif: Optional[_builtins.str] = ...,
        ebp_audio_interval: Optional[_builtins.str] = ...,
        ebp_lookahead_ms: Optional[_builtins.int] = ...,
        ebp_placement: Optional[_builtins.str] = ...,
        ecm_pid: Optional[_builtins.str] = ...,
        es_rate_in_pes: Optional[_builtins.str] = ...,
        etv_platform_pid: Optional[_builtins.str] = ...,
        etv_signal_pid: Optional[_builtins.str] = ...,
        fragment_time: Optional[_builtins.float] = ...,
        klv: Optional[_builtins.str] = ...,
        klv_data_pids: Optional[_builtins.str] = ...,
        nielsen_id3_behavior: Optional[_builtins.str] = ...,
        null_packet_bitrate: Optional[_builtins.float] = ...,
        pat_interval: Optional[_builtins.int] = ...,
        pcr_control: Optional[_builtins.str] = ...,
        pcr_period: Optional[_builtins.int] = ...,
        pcr_pid: Optional[_builtins.str] = ...,
        pmt_interval: Optional[_builtins.int] = ...,
        pmt_pid: Optional[_builtins.str] = ...,
        program_num: Optional[_builtins.int] = ...,
        rate_mode: Optional[_builtins.str] = ...,
        scte27_pids: Optional[_builtins.str] = ...,
        scte35_control: Optional[_builtins.str] = ...,
        scte35_pid: Optional[_builtins.str] = ...,
        segmentation_markers: Optional[_builtins.str] = ...,
        segmentation_style: Optional[_builtins.str] = ...,
        segmentation_time: Optional[_builtins.float] = ...,
        timed_metadata_behavior: Optional[_builtins.str] = ...,
        timed_metadata_pid: Optional[_builtins.str] = ...,
        transport_stream_id: Optional[_builtins.int] = ...,
        video_pid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="absentInputAudioBehavior")
    def absent_input_audio_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arib(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPid")
    def arib_captions_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aribCaptionsPidControl")
    def arib_captions_pid_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioBufferModel")
    def audio_buffer_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioFramesPerPes")
    def audio_frames_per_pes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioStreamType")
    def audio_stream_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferModel")
    def buffer_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ccDescriptor")
    def cc_descriptor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dvbNitSettings")
    def dvb_nit_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSdtSettings")
    def dvb_sdt_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSubPids")
    def dvb_sub_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dvbTdtSettings")
    def dvb_tdt_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbTeletextPid")
    def dvb_teletext_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ebif(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebpAudioInterval")
    def ebp_audio_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebpLookaheadMs")
    def ebp_lookahead_ms(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ebpPlacement")
    def ebp_placement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ecmPid")
    def ecm_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="esRateInPes")
    def es_rate_in_pes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etvPlatformPid")
    def etv_platform_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etvSignalPid")
    def etv_signal_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fragmentTime")
    def fragment_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def klv(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="klvDataPids")
    def klv_data_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nielsenId3Behavior")
    def nielsen_id3_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nullPacketBitrate")
    def null_packet_bitrate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="patInterval")
    def pat_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrControl")
    def pcr_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPeriod")
    def pcr_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pmtInterval")
    def pmt_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programNum")
    def program_num(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateMode")
    def rate_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte27Pids")
    def scte27_pids(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Control")
    def scte35_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationMarkers")
    def segmentation_markers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationStyle")
    def segmentation_style(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentationTime")
    def segmentation_time(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataBehavior")
    def timed_metadata_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbNitSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_id: _builtins.int,
        network_name: _builtins.str,
        rep_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbSdtSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_sdt: Optional[_builtins.str] = ...,
        rep_interval: Optional[_builtins.int] = ...,
        service_name: Optional[_builtins.str] = ...,
        service_provider_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSdt")
    def output_sdt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderName")
    def service_provider_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsContainerSettingsM2tsSettingsDvbTdtSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, rep_interval: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repInterval")
    def rep_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_ref_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationRefId")
    def destination_ref_id(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelEncoderSettingsOutputGroupOutputOutputSettingsUdpOutputSettingsFecOutputSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_depth: Optional[_builtins.int] = ...,
        include_fec: Optional[_builtins.str] = ...,
        row_length: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnDepth")
    def column_depth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="includeFec")
    def include_fec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rowLength")
    def row_length(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsTimecodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: _builtins.str,
        sync_threshold: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncThreshold")
    def sync_threshold(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        codec_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettings
        ] = ...,
        height: Optional[_builtins.int] = ...,
        respond_to_afd: Optional[_builtins.str] = ...,
        scaling_behavior: Optional[_builtins.str] = ...,
        sharpness: Optional[_builtins.int] = ...,
        width: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="codecSettings")
    def codec_settings(
        self,
    ) -> Optional[outputs.ChannelEncoderSettingsVideoDescriptionCodecSettings]: ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="respondToAfd")
    def respond_to_afd(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingBehavior")
    def scaling_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sharpness(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        frame_capture_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettings
        ] = ...,
        h264_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264Settings
        ] = ...,
        h265_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265Settings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameCaptureSettings")
    def frame_capture_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="h264Settings")
    def h264_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="h265Settings")
    def h265_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265Settings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsFrameCaptureSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capture_interval: Optional[_builtins.int] = ...,
        capture_interval_units: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captureInterval")
    def capture_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="captureIntervalUnits")
    def capture_interval_units(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264Settings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        adaptive_quantization: Optional[_builtins.str] = ...,
        afd_signaling: Optional[_builtins.str] = ...,
        bitrate: Optional[_builtins.int] = ...,
        buf_fill_pct: Optional[_builtins.int] = ...,
        buf_size: Optional[_builtins.int] = ...,
        color_metadata: Optional[_builtins.str] = ...,
        entropy_encoding: Optional[_builtins.str] = ...,
        filter_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettings
        ] = ...,
        fixed_afd: Optional[_builtins.str] = ...,
        flicker_aq: Optional[_builtins.str] = ...,
        force_field_pictures: Optional[_builtins.str] = ...,
        framerate_control: Optional[_builtins.str] = ...,
        framerate_denominator: Optional[_builtins.int] = ...,
        framerate_numerator: Optional[_builtins.int] = ...,
        gop_b_reference: Optional[_builtins.str] = ...,
        gop_closed_cadence: Optional[_builtins.int] = ...,
        gop_num_b_frames: Optional[_builtins.int] = ...,
        gop_size: Optional[_builtins.float] = ...,
        gop_size_units: Optional[_builtins.str] = ...,
        level: Optional[_builtins.str] = ...,
        look_ahead_rate_control: Optional[_builtins.str] = ...,
        max_bitrate: Optional[_builtins.int] = ...,
        min_i_interval: Optional[_builtins.int] = ...,
        num_ref_frames: Optional[_builtins.int] = ...,
        par_control: Optional[_builtins.str] = ...,
        par_denominator: Optional[_builtins.int] = ...,
        par_numerator: Optional[_builtins.int] = ...,
        profile: Optional[_builtins.str] = ...,
        quality_level: Optional[_builtins.str] = ...,
        qvbr_quality_level: Optional[_builtins.int] = ...,
        rate_control_mode: Optional[_builtins.str] = ...,
        scan_type: Optional[_builtins.str] = ...,
        scene_change_detect: Optional[_builtins.str] = ...,
        slices: Optional[_builtins.int] = ...,
        softness: Optional[_builtins.int] = ...,
        spatial_aq: Optional[_builtins.str] = ...,
        subgop_length: Optional[_builtins.str] = ...,
        syntax: Optional[_builtins.str] = ...,
        temporal_aq: Optional[_builtins.str] = ...,
        timecode_insertion: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveQuantization")
    def adaptive_quantization(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="afdSignaling")
    def afd_signaling(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufFillPct")
    def buf_fill_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufSize")
    def buf_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="colorMetadata")
    def color_metadata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entropyEncoding")
    def entropy_encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterSettings")
    def filter_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fixedAfd")
    def fixed_afd(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flickerAq")
    def flicker_aq(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceFieldPictures")
    def force_field_pictures(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="framerateControl")
    def framerate_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="framerateDenominator")
    def framerate_denominator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="framerateNumerator")
    def framerate_numerator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gopBReference")
    def gop_b_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gopClosedCadence")
    def gop_closed_cadence(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gopNumBFrames")
    def gop_num_b_frames(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gopSize")
    def gop_size(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="gopSizeUnits")
    def gop_size_units(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lookAheadRateControl")
    def look_ahead_rate_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBitrate")
    def max_bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIInterval")
    def min_i_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="numRefFrames")
    def num_ref_frames(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parControl")
    def par_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parDenominator")
    def par_denominator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parNumerator")
    def par_numerator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="qualityLevel")
    def quality_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="qvbrQualityLevel")
    def qvbr_quality_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sceneChangeDetect")
    def scene_change_detect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def slices(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def softness(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="spatialAq")
    def spatial_aq(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subgopLength")
    def subgop_length(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def syntax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="temporalAq")
    def temporal_aq(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeInsertion")
    def timecode_insertion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        temporal_filter_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="temporalFilterSettings")
    def temporal_filter_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH264SettingsFilterSettingsTemporalFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        post_filter_sharpening: Optional[_builtins.str] = ...,
        strength: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postFilterSharpening")
    def post_filter_sharpening(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def strength(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265Settings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate: _builtins.int,
        framerate_denominator: _builtins.int,
        framerate_numerator: _builtins.int,
        adaptive_quantization: Optional[_builtins.str] = ...,
        afd_signaling: Optional[_builtins.str] = ...,
        alternative_transfer_function: Optional[_builtins.str] = ...,
        buf_size: Optional[_builtins.int] = ...,
        color_metadata: Optional[_builtins.str] = ...,
        color_space_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettings
        ] = ...,
        filter_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettings
        ] = ...,
        fixed_afd: Optional[_builtins.str] = ...,
        flicker_aq: Optional[_builtins.str] = ...,
        gop_closed_cadence: Optional[_builtins.int] = ...,
        gop_size: Optional[_builtins.float] = ...,
        gop_size_units: Optional[_builtins.str] = ...,
        level: Optional[_builtins.str] = ...,
        look_ahead_rate_control: Optional[_builtins.str] = ...,
        max_bitrate: Optional[_builtins.int] = ...,
        min_i_interval: Optional[_builtins.int] = ...,
        min_qp: Optional[_builtins.int] = ...,
        mv_over_picture_boundaries: Optional[_builtins.str] = ...,
        mv_temporal_predictor: Optional[_builtins.str] = ...,
        par_denominator: Optional[_builtins.int] = ...,
        par_numerator: Optional[_builtins.int] = ...,
        profile: Optional[_builtins.str] = ...,
        qvbr_quality_level: Optional[_builtins.int] = ...,
        rate_control_mode: Optional[_builtins.str] = ...,
        scan_type: Optional[_builtins.str] = ...,
        scene_change_detect: Optional[_builtins.str] = ...,
        slices: Optional[_builtins.int] = ...,
        tier: Optional[_builtins.str] = ...,
        tile_height: Optional[_builtins.int] = ...,
        tile_padding: Optional[_builtins.str] = ...,
        tile_width: Optional[_builtins.int] = ...,
        timecode_burnin_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettings
        ] = ...,
        timecode_insertion: Optional[_builtins.str] = ...,
        treeblock_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitrate(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="framerateDenominator")
    def framerate_denominator(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="framerateNumerator")
    def framerate_numerator(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveQuantization")
    def adaptive_quantization(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="afdSignaling")
    def afd_signaling(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="alternativeTransferFunction")
    def alternative_transfer_function(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bufSize")
    def buf_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="colorMetadata")
    def color_metadata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="colorSpaceSettings")
    def color_space_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="filterSettings")
    def filter_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fixedAfd")
    def fixed_afd(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flickerAq")
    def flicker_aq(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gopClosedCadence")
    def gop_closed_cadence(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gopSize")
    def gop_size(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="gopSizeUnits")
    def gop_size_units(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lookAheadRateControl")
    def look_ahead_rate_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBitrate")
    def max_bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIInterval")
    def min_i_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minQp")
    def min_qp(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mvOverPictureBoundaries")
    def mv_over_picture_boundaries(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mvTemporalPredictor")
    def mv_temporal_predictor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parDenominator")
    def par_denominator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parNumerator")
    def par_numerator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="qvbrQualityLevel")
    def qvbr_quality_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sceneChangeDetect")
    def scene_change_detect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def slices(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tileHeight")
    def tile_height(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tilePadding")
    def tile_padding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tileWidth")
    def tile_width(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninSettings")
    def timecode_burnin_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeInsertion")
    def timecode_insertion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="treeblockSize")
    def treeblock_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        color_space_passthrough_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettings
        ] = ...,
        dolby_vision81_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81Settings
        ] = ...,
        hdr10_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10Settings
        ] = ...,
        rec601_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601Settings
        ] = ...,
        rec709_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709Settings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="colorSpacePassthroughSettings")
    def color_space_passthrough_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dolbyVision81Settings")
    def dolby_vision81_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hdr10Settings")
    def hdr10_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rec601Settings")
    def rec601_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601Settings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rec709Settings")
    def rec709_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709Settings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsColorSpacePassthroughSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsDolbyVision81Settings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsHdr10Settings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_cll: Optional[_builtins.int] = ...,
        max_fall: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCll")
    def max_cll(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxFall")
    def max_fall(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec601Settings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsColorSpaceSettingsRec709Settings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        temporal_filter_settings: Optional[
            outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="temporalFilterSettings")
    def temporal_filter_settings(
        self,
    ) -> Optional[
        outputs.ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettings
    ]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsFilterSettingsTemporalFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        post_filter_sharpening: Optional[_builtins.str] = ...,
        strength: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postFilterSharpening")
    def post_filter_sharpening(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def strength(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelEncoderSettingsVideoDescriptionCodecSettingsH265SettingsTimecodeBurninSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prefix: Optional[_builtins.str] = ...,
        timecode_burnin_font_size: Optional[_builtins.str] = ...,
        timecode_burnin_position: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninFontSize")
    def timecode_burnin_font_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timecodeBurninPosition")
    def timecode_burnin_position(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_attachment_name: _builtins.str,
        input_id: _builtins.str,
        automatic_input_failover_settings: Optional[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettings
        ] = ...,
        input_settings: Optional[outputs.ChannelInputAttachmentInputSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputAttachmentName")
    def input_attachment_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputId")
    def input_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="automaticInputFailoverSettings")
    def automatic_input_failover_settings(
        self,
    ) -> Optional[outputs.ChannelInputAttachmentAutomaticInputFailoverSettings]: ...
    @_builtins.property
    @pulumi.getter(name="inputSettings")
    def input_settings(
        self,
    ) -> Optional[outputs.ChannelInputAttachmentInputSettings]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secondary_input_id: _builtins.str,
        error_clear_time_msec: Optional[_builtins.int] = ...,
        failover_conditions: Optional[
            Sequence[
                outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverCondition
            ]
        ] = ...,
        input_preference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secondaryInputId")
    def secondary_input_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorClearTimeMsec")
    def error_clear_time_msec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="failoverConditions")
    def failover_conditions(
        self,
    ) -> Optional[
        Sequence[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverCondition
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputPreference")
    def input_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failover_condition_settings: Optional[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverConditionSettings")
    def failover_condition_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettings
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_silence_settings: Optional[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettings
        ] = ...,
        input_loss_settings: Optional[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettings
        ] = ...,
        video_black_settings: Optional[
            outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSilenceSettings")
    def audio_silence_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputLossSettings")
    def input_loss_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="videoBlackSettings")
    def video_black_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettings
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsAudioSilenceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_selector_name: _builtins.str,
        audio_silence_threshold_msec: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectorName")
    def audio_selector_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="audioSilenceThresholdMsec")
    def audio_silence_threshold_msec(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsInputLossSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, input_loss_threshold_msec: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputLossThresholdMsec")
    def input_loss_threshold_msec(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentAutomaticInputFailoverSettingsFailoverConditionFailoverConditionSettingsVideoBlackSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        black_detect_threshold: Optional[_builtins.float] = ...,
        video_black_threshold_msec: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blackDetectThreshold")
    def black_detect_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="videoBlackThresholdMsec")
    def video_black_threshold_msec(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_selectors: Optional[
            Sequence[outputs.ChannelInputAttachmentInputSettingsAudioSelector]
        ] = ...,
        caption_selectors: Optional[
            Sequence[outputs.ChannelInputAttachmentInputSettingsCaptionSelector]
        ] = ...,
        deblock_filter: Optional[_builtins.str] = ...,
        denoise_filter: Optional[_builtins.str] = ...,
        filter_strength: Optional[_builtins.int] = ...,
        input_filter: Optional[_builtins.str] = ...,
        network_input_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsNetworkInputSettings
        ] = ...,
        scte35_pid: Optional[_builtins.int] = ...,
        smpte2038_data_preference: Optional[_builtins.str] = ...,
        source_end_behavior: Optional[_builtins.str] = ...,
        video_selector: Optional[
            outputs.ChannelInputAttachmentInputSettingsVideoSelector
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioSelectors")
    def audio_selectors(
        self,
    ) -> Optional[
        Sequence[outputs.ChannelInputAttachmentInputSettingsAudioSelector]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="captionSelectors")
    def caption_selectors(
        self,
    ) -> Optional[
        Sequence[outputs.ChannelInputAttachmentInputSettingsCaptionSelector]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deblockFilter")
    def deblock_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="denoiseFilter")
    def denoise_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterStrength")
    def filter_strength(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="inputFilter")
    def input_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInputSettings")
    def network_input_settings(
        self,
    ) -> Optional[outputs.ChannelInputAttachmentInputSettingsNetworkInputSettings]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="smpte2038DataPreference")
    def smpte2038_data_preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEndBehavior")
    def source_end_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="videoSelector")
    def video_selector(
        self,
    ) -> Optional[outputs.ChannelInputAttachmentInputSettingsVideoSelector]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        selector_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selectorSettings")
    def selector_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettings
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_hls_rendition_selection: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelection
        ] = ...,
        audio_language_selection: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelection
        ] = ...,
        audio_pid_selection: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelection
        ] = ...,
        audio_track_selection: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioHlsRenditionSelection")
    def audio_hls_rendition_selection(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="audioLanguageSelection")
    def audio_language_selection(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="audioPidSelection")
    def audio_pid_selection(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelection
    ]: ...
    @_builtins.property
    @pulumi.getter(name="audioTrackSelection")
    def audio_track_selection(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelection
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioHlsRenditionSelection(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, group_id: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioLanguageSelection(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        language_code: _builtins.str,
        language_selection_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="languageSelectionPolicy")
    def language_selection_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioPidSelection(
    dict
):
    def __init__(__self__, *, pid: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> _builtins.int: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelection(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tracks: Sequence[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrack
        ],
        dolby_e_decode: Optional[
            outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecode
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tracks(
        self,
    ) -> Sequence[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrack
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dolbyEDecode")
    def dolby_e_decode(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecode
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionDolbyEDecode(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, program_selection: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="programSelection")
    def program_selection(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsAudioSelectorSelectorSettingsAudioTrackSelectionTrack(
    dict
):
    def __init__(__self__, *, track: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def track(self) -> _builtins.int: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        language_code: Optional[_builtins.str] = ...,
        selector_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selectorSettings")
    def selector_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettings
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ancillary_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettings
        ] = ...,
        arib_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettings
        ] = ...,
        dvb_sub_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettings
        ] = ...,
        embedded_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettings
        ] = ...,
        scte20_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettings
        ] = ...,
        scte27_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettings
        ] = ...,
        teletext_source_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ancillarySourceSettings")
    def ancillary_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="aribSourceSettings")
    def arib_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dvbSubSourceSettings")
    def dvb_sub_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="embeddedSourceSettings")
    def embedded_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scte20SourceSettings")
    def scte20_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scte27SourceSettings")
    def scte27_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="teletextSourceSettings")
    def teletext_source_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettings
    ]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAncillarySourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_ancillary_channel_number: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceAncillaryChannelNumber")
    def source_ancillary_channel_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsAribSourceSettings(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsDvbSubSourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ocr_language: Optional[_builtins.str] = ...,
        pid: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ocrLanguage")
    def ocr_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsEmbeddedSourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        convert608_to708: Optional[_builtins.str] = ...,
        scte20_detection: Optional[_builtins.str] = ...,
        source608_channel_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="convert608To708")
    def convert608_to708(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scte20Detection")
    def scte20_detection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="source608ChannelNumber")
    def source608_channel_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte20SourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        convert608_to708: Optional[_builtins.str] = ...,
        source608_channel_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="convert608To708")
    def convert608_to708(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="source608ChannelNumber")
    def source608_channel_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsScte27SourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ocr_language: Optional[_builtins.str] = ...,
        pid: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ocrLanguage")
    def ocr_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pid(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_rectangle: Optional[
            outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangle
        ] = ...,
        page_number: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputRectangle")
    def output_rectangle(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangle
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsCaptionSelectorSelectorSettingsTeletextSourceSettingsOutputRectangle(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        height: _builtins.float,
        left_offset: _builtins.float,
        top_offset: _builtins.float,
        width: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="leftOffset")
    def left_offset(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="topOffset")
    def top_offset(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> _builtins.float: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsNetworkInputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hls_input_settings: Optional[
            outputs.ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettings
        ] = ...,
        server_validation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hlsInputSettings")
    def hls_input_settings(
        self,
    ) -> Optional[
        outputs.ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serverValidation")
    def server_validation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsNetworkInputSettingsHlsInputSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bandwidth: Optional[_builtins.int] = ...,
        buffer_segments: Optional[_builtins.int] = ...,
        retries: Optional[_builtins.int] = ...,
        retry_interval: Optional[_builtins.int] = ...,
        scte35_source: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bufferSegments")
    def buffer_segments(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retryInterval")
    def retry_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scte35Source")
    def scte35_source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputAttachmentInputSettingsVideoSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        color_space: Optional[_builtins.str] = ...,
        color_space_usage: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="colorSpace")
    def color_space(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="colorSpaceUsage")
    def color_space_usage(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChannelInputSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        codec: _builtins.str,
        input_resolution: _builtins.str,
        maximum_bitrate: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputResolution")
    def input_resolution(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maximumBitrate")
    def maximum_bitrate(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelMaintenance(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maintenance_day: _builtins.str,
        maintenance_start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceDay")
    def maintenance_day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceStartTime")
    def maintenance_start_time(self) -> _builtins.str: ...

@pulumi.output_type
class ChannelVpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_address_allocation_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        network_interface_ids: Optional[Sequence[_builtins.str]] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicAddressAllocationIds")
    def public_address_allocation_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class InputDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, stream_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> _builtins.str: ...

@pulumi.output_type
class InputInputDevice(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class InputMediaConnectFlow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, flow_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowArn")
    def flow_arn(self) -> _builtins.str: ...

@pulumi.output_type
class InputSecurityGroupWhitelistRule(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...

@pulumi.output_type
class InputSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password_param: _builtins.str,
        url: _builtins.str,
        username: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class InputVpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_ids: Sequence[_builtins.str],
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultiplexMultiplexSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        transport_stream_bitrate: _builtins.int,
        transport_stream_id: _builtins.int,
        maximum_video_buffer_delay_milliseconds: Optional[_builtins.int] = ...,
        transport_stream_reserved_bitrate: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamBitrate")
    def transport_stream_bitrate(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumVideoBufferDelayMilliseconds")
    def maximum_video_buffer_delay_milliseconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="transportStreamReservedBitrate")
    def transport_stream_reserved_bitrate(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MultiplexProgramMultiplexProgramSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preferred_channel_pipeline: _builtins.str,
        program_number: _builtins.int,
        service_descriptor: Optional[
            outputs.MultiplexProgramMultiplexProgramSettingsServiceDescriptor
        ] = ...,
        video_settings: Optional[
            outputs.MultiplexProgramMultiplexProgramSettingsVideoSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredChannelPipeline")
    def preferred_channel_pipeline(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="programNumber")
    def program_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="serviceDescriptor")
    def service_descriptor(
        self,
    ) -> Optional[
        outputs.MultiplexProgramMultiplexProgramSettingsServiceDescriptor
    ]: ...
    @_builtins.property
    @pulumi.getter(name="videoSettings")
    def video_settings(
        self,
    ) -> Optional[outputs.MultiplexProgramMultiplexProgramSettingsVideoSettings]: ...

@pulumi.output_type
class MultiplexProgramMultiplexProgramSettingsServiceDescriptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, provider_name: _builtins.str, service_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class MultiplexProgramMultiplexProgramSettingsVideoSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        constant_bitrate: Optional[_builtins.int] = ...,
        statmux_settings: Optional[
            outputs.MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="constantBitrate")
    def constant_bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="statmuxSettings")
    def statmux_settings(
        self,
    ) -> Optional[
        outputs.MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings
    ]: ...

@pulumi.output_type
class MultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_bitrate: Optional[_builtins.int] = ...,
        minimum_bitrate: Optional[_builtins.int] = ...,
        priority: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBitrate")
    def maximum_bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minimumBitrate")
    def minimum_bitrate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MultiplexProgramTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetInputDestinationResult(dict):
    def __init__(
        __self__,
        *,
        ip: _builtins.str,
        port: _builtins.str,
        url: _builtins.str,
        vpcs: Sequence[outputs.GetInputDestinationVpcResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Sequence[outputs.GetInputDestinationVpcResult]: ...

@pulumi.output_type
class GetInputDestinationVpcResult(dict):
    def __init__(
        __self__,
        *,
        availability_zone: _builtins.str,
        network_interface_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetInputInputDeviceResult(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class GetInputMediaConnectFlowResult(dict):
    def __init__(__self__, *, flow_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowArn")
    def flow_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetInputSourceResult(dict):
    def __init__(
        __self__,
        *,
        password_param: _builtins.str,
        url: _builtins.str,
        username: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordParam")
    def password_param(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
