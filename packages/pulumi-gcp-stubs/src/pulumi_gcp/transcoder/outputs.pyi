import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "JobConfig",
    "JobConfigAdBreak",
    "JobConfigEditList",
    "JobConfigElementaryStream",
    "JobConfigElementaryStreamAudioStream",
    "JobConfigElementaryStreamVideoStream",
    "JobConfigElementaryStreamVideoStreamH264",
    "JobConfigElementaryStreamVideoStreamH264Hlg",
    "JobConfigElementaryStreamVideoStreamH264Sdr",
    "JobConfigEncryption",
    "JobConfigEncryptionAes128",
    "JobConfigEncryptionDrmSystems",
    "JobConfigEncryptionDrmSystemsClearkey",
    "JobConfigEncryptionDrmSystemsFairplay",
    "JobConfigEncryptionDrmSystemsPlayready",
    "JobConfigEncryptionDrmSystemsWidevine",
    "JobConfigEncryptionMpegCenc",
    "JobConfigEncryptionSampleAes",
    "JobConfigEncryptionSecretManagerKeySource",
    "JobConfigInput",
    "JobConfigManifest",
    "JobConfigMuxStream",
    "JobConfigMuxStreamSegmentSettings",
    "JobConfigOutput",
    "JobConfigOverlay",
    "JobConfigOverlayAnimation",
    "JobConfigOverlayAnimationAnimationFade",
    "JobConfigOverlayAnimationAnimationFadeXy",
    "JobConfigOverlayImage",
    "JobConfigPubsubDestination",
    "JobTemplateConfig",
    "JobTemplateConfigAdBreak",
    "JobTemplateConfigEditList",
    "JobTemplateConfigElementaryStream",
    "JobTemplateConfigElementaryStreamAudioStream",
    "JobTemplateConfigElementaryStreamVideoStream",
    "JobTemplateConfigElementaryStreamVideoStreamH264",
    ...,
    ...,
    "JobTemplateConfigEncryption",
    "JobTemplateConfigEncryptionAes128",
    "JobTemplateConfigEncryptionDrmSystems",
    "JobTemplateConfigEncryptionDrmSystemsClearkey",
    "JobTemplateConfigEncryptionDrmSystemsFairplay",
    "JobTemplateConfigEncryptionDrmSystemsPlayready",
    "JobTemplateConfigEncryptionDrmSystemsWidevine",
    "JobTemplateConfigEncryptionMpegCenc",
    "JobTemplateConfigEncryptionSampleAes",
    "JobTemplateConfigEncryptionSecretManagerKeySource",
    "JobTemplateConfigInput",
    "JobTemplateConfigManifest",
    "JobTemplateConfigMuxStream",
    "JobTemplateConfigMuxStreamSegmentSettings",
    "JobTemplateConfigOutput",
    "JobTemplateConfigOverlay",
    "JobTemplateConfigOverlayAnimation",
    "JobTemplateConfigOverlayAnimationAnimationFade",
    "JobTemplateConfigOverlayAnimationAnimationFadeXy",
    "JobTemplateConfigOverlayImage",
    "JobTemplateConfigPubsubDestination",
]

@pulumi.output_type
class JobConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ad_breaks: Optional[Sequence[outputs.JobConfigAdBreak]] = ...,
        edit_lists: Optional[Sequence[outputs.JobConfigEditList]] = ...,
        elementary_streams: Optional[Sequence[outputs.JobConfigElementaryStream]] = ...,
        encryptions: Optional[Sequence[outputs.JobConfigEncryption]] = ...,
        inputs: Optional[Sequence[outputs.JobConfigInput]] = ...,
        manifests: Optional[Sequence[outputs.JobConfigManifest]] = ...,
        mux_streams: Optional[Sequence[outputs.JobConfigMuxStream]] = ...,
        output: Optional[outputs.JobConfigOutput] = ...,
        overlays: Optional[Sequence[outputs.JobConfigOverlay]] = ...,
        pubsub_destination: Optional[outputs.JobConfigPubsubDestination] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adBreaks")
    def ad_breaks(self) -> Optional[Sequence[outputs.JobConfigAdBreak]]: ...
    @_builtins.property
    @pulumi.getter(name="editLists")
    def edit_lists(self) -> Optional[Sequence[outputs.JobConfigEditList]]: ...
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(
        self,
    ) -> Optional[Sequence[outputs.JobConfigElementaryStream]]: ...
    @_builtins.property
    @pulumi.getter
    def encryptions(self) -> Optional[Sequence[outputs.JobConfigEncryption]]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.JobConfigInput]]: ...
    @_builtins.property
    @pulumi.getter
    def manifests(self) -> Optional[Sequence[outputs.JobConfigManifest]]: ...
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[Sequence[outputs.JobConfigMuxStream]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[outputs.JobConfigOutput]: ...
    @_builtins.property
    @pulumi.getter
    def overlays(self) -> Optional[Sequence[outputs.JobConfigOverlay]]: ...
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> Optional[outputs.JobConfigPubsubDestination]: ...

@pulumi.output_type
class JobConfigAdBreak(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, start_time_offset: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigEditList(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inputs: Optional[Sequence[_builtins.str]] = ...,
        key: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigElementaryStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_stream: Optional[outputs.JobConfigElementaryStreamAudioStream] = ...,
        key: Optional[_builtins.str] = ...,
        video_stream: Optional[outputs.JobConfigElementaryStreamVideoStream] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioStream")
    def audio_stream(
        self,
    ) -> Optional[outputs.JobConfigElementaryStreamAudioStream]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="videoStream")
    def video_stream(
        self,
    ) -> Optional[outputs.JobConfigElementaryStreamVideoStream]: ...

@pulumi.output_type
class JobConfigElementaryStreamAudioStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate_bps: _builtins.int,
        channel_count: Optional[_builtins.int] = ...,
        channel_layouts: Optional[Sequence[_builtins.str]] = ...,
        codec: Optional[_builtins.str] = ...,
        sample_rate_hertz: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="channelCount")
    def channel_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="channelLayouts")
    def channel_layouts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobConfigElementaryStreamVideoStream(dict):
    def __init__(
        __self__,
        *,
        h264: Optional[outputs.JobConfigElementaryStreamVideoStreamH264] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def h264(self) -> Optional[outputs.JobConfigElementaryStreamVideoStreamH264]: ...

@pulumi.output_type
class JobConfigElementaryStreamVideoStreamH264(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate_bps: _builtins.int,
        frame_rate: _builtins.int,
        crf_level: Optional[_builtins.int] = ...,
        entropy_coder: Optional[_builtins.str] = ...,
        gop_duration: Optional[_builtins.str] = ...,
        height_pixels: Optional[_builtins.int] = ...,
        hlg: Optional[outputs.JobConfigElementaryStreamVideoStreamH264Hlg] = ...,
        pixel_format: Optional[_builtins.str] = ...,
        preset: Optional[_builtins.str] = ...,
        profile: Optional[_builtins.str] = ...,
        rate_control_mode: Optional[_builtins.str] = ...,
        sdr: Optional[outputs.JobConfigElementaryStreamVideoStreamH264Sdr] = ...,
        vbv_fullness_bits: Optional[_builtins.int] = ...,
        vbv_size_bits: Optional[_builtins.int] = ...,
        width_pixels: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="crfLevel")
    def crf_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="entropyCoder")
    def entropy_coder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gopDuration")
    def gop_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="heightPixels")
    def height_pixels(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def hlg(self) -> Optional[outputs.JobConfigElementaryStreamVideoStreamH264Hlg]: ...
    @_builtins.property
    @pulumi.getter(name="pixelFormat")
    def pixel_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sdr(self) -> Optional[outputs.JobConfigElementaryStreamVideoStreamH264Sdr]: ...
    @_builtins.property
    @pulumi.getter(name="vbvFullnessBits")
    def vbv_fullness_bits(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vbvSizeBits")
    def vbv_size_bits(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="widthPixels")
    def width_pixels(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobConfigElementaryStreamVideoStreamH264Hlg(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigElementaryStreamVideoStreamH264Sdr(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        aes128: Optional[outputs.JobConfigEncryptionAes128] = ...,
        drm_systems: Optional[outputs.JobConfigEncryptionDrmSystems] = ...,
        mpeg_cenc: Optional[outputs.JobConfigEncryptionMpegCenc] = ...,
        sample_aes: Optional[outputs.JobConfigEncryptionSampleAes] = ...,
        secret_manager_key_source: Optional[
            outputs.JobConfigEncryptionSecretManagerKeySource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def aes128(self) -> Optional[outputs.JobConfigEncryptionAes128]: ...
    @_builtins.property
    @pulumi.getter(name="drmSystems")
    def drm_systems(self) -> Optional[outputs.JobConfigEncryptionDrmSystems]: ...
    @_builtins.property
    @pulumi.getter(name="mpegCenc")
    def mpeg_cenc(self) -> Optional[outputs.JobConfigEncryptionMpegCenc]: ...
    @_builtins.property
    @pulumi.getter(name="sampleAes")
    def sample_aes(self) -> Optional[outputs.JobConfigEncryptionSampleAes]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerKeySource")
    def secret_manager_key_source(
        self,
    ) -> Optional[outputs.JobConfigEncryptionSecretManagerKeySource]: ...

@pulumi.output_type
class JobConfigEncryptionAes128(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionDrmSystems(dict):
    def __init__(
        __self__,
        *,
        clearkey: Optional[outputs.JobConfigEncryptionDrmSystemsClearkey] = ...,
        fairplay: Optional[outputs.JobConfigEncryptionDrmSystemsFairplay] = ...,
        playready: Optional[outputs.JobConfigEncryptionDrmSystemsPlayready] = ...,
        widevine: Optional[outputs.JobConfigEncryptionDrmSystemsWidevine] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clearkey(self) -> Optional[outputs.JobConfigEncryptionDrmSystemsClearkey]: ...
    @_builtins.property
    @pulumi.getter
    def fairplay(self) -> Optional[outputs.JobConfigEncryptionDrmSystemsFairplay]: ...
    @_builtins.property
    @pulumi.getter
    def playready(self) -> Optional[outputs.JobConfigEncryptionDrmSystemsPlayready]: ...
    @_builtins.property
    @pulumi.getter
    def widevine(self) -> Optional[outputs.JobConfigEncryptionDrmSystemsWidevine]: ...

@pulumi.output_type
class JobConfigEncryptionDrmSystemsClearkey(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionDrmSystemsFairplay(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionDrmSystemsPlayready(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionDrmSystemsWidevine(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionMpegCenc(dict):
    def __init__(__self__, *, scheme: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...

@pulumi.output_type
class JobConfigEncryptionSampleAes(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobConfigEncryptionSecretManagerKeySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class JobConfigInput(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigManifest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_name: Optional[_builtins.str] = ...,
        mux_streams: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigMuxStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container: Optional[_builtins.str] = ...,
        elementary_streams: Optional[Sequence[_builtins.str]] = ...,
        encryption_id: Optional[_builtins.str] = ...,
        file_name: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        segment_settings: Optional[outputs.JobConfigMuxStreamSegmentSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionId")
    def encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentSettings")
    def segment_settings(
        self,
    ) -> Optional[outputs.JobConfigMuxStreamSegmentSettings]: ...

@pulumi.output_type
class JobConfigMuxStreamSegmentSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, segment_duration: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="segmentDuration")
    def segment_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigOutput(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobConfigOverlay(dict):
    def __init__(
        __self__,
        *,
        animations: Optional[Sequence[outputs.JobConfigOverlayAnimation]] = ...,
        image: Optional[outputs.JobConfigOverlayImage] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def animations(self) -> Optional[Sequence[outputs.JobConfigOverlayAnimation]]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.JobConfigOverlayImage]: ...

@pulumi.output_type
class JobConfigOverlayAnimation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        animation_fade: Optional[outputs.JobConfigOverlayAnimationAnimationFade] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="animationFade")
    def animation_fade(
        self,
    ) -> Optional[outputs.JobConfigOverlayAnimationAnimationFade]: ...

@pulumi.output_type
class JobConfigOverlayAnimationAnimationFade(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fade_type: _builtins.str,
        end_time_offset: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
        xy: Optional[outputs.JobConfigOverlayAnimationAnimationFadeXy] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fadeType")
    def fade_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def xy(self) -> Optional[outputs.JobConfigOverlayAnimationAnimationFadeXy]: ...

@pulumi.output_type
class JobConfigOverlayAnimationAnimationFadeXy(dict):
    def __init__(
        __self__,
        *,
        x: Optional[_builtins.float] = ...,
        y: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class JobConfigOverlayImage(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class JobConfigPubsubDestination(dict):
    def __init__(__self__, *, topic: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ad_breaks: Optional[Sequence[outputs.JobTemplateConfigAdBreak]] = ...,
        edit_lists: Optional[Sequence[outputs.JobTemplateConfigEditList]] = ...,
        elementary_streams: Optional[
            Sequence[outputs.JobTemplateConfigElementaryStream]
        ] = ...,
        encryptions: Optional[Sequence[outputs.JobTemplateConfigEncryption]] = ...,
        inputs: Optional[Sequence[outputs.JobTemplateConfigInput]] = ...,
        manifests: Optional[Sequence[outputs.JobTemplateConfigManifest]] = ...,
        mux_streams: Optional[Sequence[outputs.JobTemplateConfigMuxStream]] = ...,
        output: Optional[outputs.JobTemplateConfigOutput] = ...,
        overlays: Optional[Sequence[outputs.JobTemplateConfigOverlay]] = ...,
        pubsub_destination: Optional[outputs.JobTemplateConfigPubsubDestination] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adBreaks")
    def ad_breaks(self) -> Optional[Sequence[outputs.JobTemplateConfigAdBreak]]: ...
    @_builtins.property
    @pulumi.getter(name="editLists")
    def edit_lists(self) -> Optional[Sequence[outputs.JobTemplateConfigEditList]]: ...
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(
        self,
    ) -> Optional[Sequence[outputs.JobTemplateConfigElementaryStream]]: ...
    @_builtins.property
    @pulumi.getter
    def encryptions(
        self,
    ) -> Optional[Sequence[outputs.JobTemplateConfigEncryption]]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.JobTemplateConfigInput]]: ...
    @_builtins.property
    @pulumi.getter
    def manifests(self) -> Optional[Sequence[outputs.JobTemplateConfigManifest]]: ...
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[Sequence[outputs.JobTemplateConfigMuxStream]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[outputs.JobTemplateConfigOutput]: ...
    @_builtins.property
    @pulumi.getter
    def overlays(self) -> Optional[Sequence[outputs.JobTemplateConfigOverlay]]: ...
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(
        self,
    ) -> Optional[outputs.JobTemplateConfigPubsubDestination]: ...

@pulumi.output_type
class JobTemplateConfigAdBreak(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, start_time_offset: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigEditList(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inputs: Optional[Sequence[_builtins.str]] = ...,
        key: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigElementaryStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_stream: Optional[
            outputs.JobTemplateConfigElementaryStreamAudioStream
        ] = ...,
        key: Optional[_builtins.str] = ...,
        video_stream: Optional[
            outputs.JobTemplateConfigElementaryStreamVideoStream
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioStream")
    def audio_stream(
        self,
    ) -> Optional[outputs.JobTemplateConfigElementaryStreamAudioStream]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="videoStream")
    def video_stream(
        self,
    ) -> Optional[outputs.JobTemplateConfigElementaryStreamVideoStream]: ...

@pulumi.output_type
class JobTemplateConfigElementaryStreamAudioStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate_bps: _builtins.int,
        channel_count: Optional[_builtins.int] = ...,
        channel_layouts: Optional[Sequence[_builtins.str]] = ...,
        codec: Optional[_builtins.str] = ...,
        sample_rate_hertz: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="channelCount")
    def channel_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="channelLayouts")
    def channel_layouts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobTemplateConfigElementaryStreamVideoStream(dict):
    def __init__(
        __self__,
        *,
        h264: Optional[outputs.JobTemplateConfigElementaryStreamVideoStreamH264] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def h264(
        self,
    ) -> Optional[outputs.JobTemplateConfigElementaryStreamVideoStreamH264]: ...

@pulumi.output_type
class JobTemplateConfigElementaryStreamVideoStreamH264(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitrate_bps: _builtins.int,
        frame_rate: _builtins.int,
        crf_level: Optional[_builtins.int] = ...,
        entropy_coder: Optional[_builtins.str] = ...,
        gop_duration: Optional[_builtins.str] = ...,
        height_pixels: Optional[_builtins.int] = ...,
        hlg: Optional[
            outputs.JobTemplateConfigElementaryStreamVideoStreamH264Hlg
        ] = ...,
        pixel_format: Optional[_builtins.str] = ...,
        preset: Optional[_builtins.str] = ...,
        profile: Optional[_builtins.str] = ...,
        rate_control_mode: Optional[_builtins.str] = ...,
        sdr: Optional[
            outputs.JobTemplateConfigElementaryStreamVideoStreamH264Sdr
        ] = ...,
        vbv_fullness_bits: Optional[_builtins.int] = ...,
        vbv_size_bits: Optional[_builtins.int] = ...,
        width_pixels: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="crfLevel")
    def crf_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="entropyCoder")
    def entropy_coder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gopDuration")
    def gop_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="heightPixels")
    def height_pixels(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def hlg(
        self,
    ) -> Optional[outputs.JobTemplateConfigElementaryStreamVideoStreamH264Hlg]: ...
    @_builtins.property
    @pulumi.getter(name="pixelFormat")
    def pixel_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sdr(
        self,
    ) -> Optional[outputs.JobTemplateConfigElementaryStreamVideoStreamH264Sdr]: ...
    @_builtins.property
    @pulumi.getter(name="vbvFullnessBits")
    def vbv_fullness_bits(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vbvSizeBits")
    def vbv_size_bits(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="widthPixels")
    def width_pixels(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobTemplateConfigElementaryStreamVideoStreamH264Hlg(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigElementaryStreamVideoStreamH264Sdr(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        aes128: Optional[outputs.JobTemplateConfigEncryptionAes128] = ...,
        drm_systems: Optional[outputs.JobTemplateConfigEncryptionDrmSystems] = ...,
        mpeg_cenc: Optional[outputs.JobTemplateConfigEncryptionMpegCenc] = ...,
        sample_aes: Optional[outputs.JobTemplateConfigEncryptionSampleAes] = ...,
        secret_manager_key_source: Optional[
            outputs.JobTemplateConfigEncryptionSecretManagerKeySource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def aes128(self) -> Optional[outputs.JobTemplateConfigEncryptionAes128]: ...
    @_builtins.property
    @pulumi.getter(name="drmSystems")
    def drm_systems(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionDrmSystems]: ...
    @_builtins.property
    @pulumi.getter(name="mpegCenc")
    def mpeg_cenc(self) -> Optional[outputs.JobTemplateConfigEncryptionMpegCenc]: ...
    @_builtins.property
    @pulumi.getter(name="sampleAes")
    def sample_aes(self) -> Optional[outputs.JobTemplateConfigEncryptionSampleAes]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerKeySource")
    def secret_manager_key_source(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionSecretManagerKeySource]: ...

@pulumi.output_type
class JobTemplateConfigEncryptionAes128(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionDrmSystems(dict):
    def __init__(
        __self__,
        *,
        clearkey: Optional[outputs.JobTemplateConfigEncryptionDrmSystemsClearkey] = ...,
        fairplay: Optional[outputs.JobTemplateConfigEncryptionDrmSystemsFairplay] = ...,
        playready: Optional[
            outputs.JobTemplateConfigEncryptionDrmSystemsPlayready
        ] = ...,
        widevine: Optional[outputs.JobTemplateConfigEncryptionDrmSystemsWidevine] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clearkey(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionDrmSystemsClearkey]: ...
    @_builtins.property
    @pulumi.getter
    def fairplay(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionDrmSystemsFairplay]: ...
    @_builtins.property
    @pulumi.getter
    def playready(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionDrmSystemsPlayready]: ...
    @_builtins.property
    @pulumi.getter
    def widevine(
        self,
    ) -> Optional[outputs.JobTemplateConfigEncryptionDrmSystemsWidevine]: ...

@pulumi.output_type
class JobTemplateConfigEncryptionDrmSystemsClearkey(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionDrmSystemsFairplay(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionDrmSystemsPlayready(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionDrmSystemsWidevine(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionMpegCenc(dict):
    def __init__(__self__, *, scheme: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...

@pulumi.output_type
class JobTemplateConfigEncryptionSampleAes(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class JobTemplateConfigEncryptionSecretManagerKeySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class JobTemplateConfigInput(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigManifest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_name: Optional[_builtins.str] = ...,
        mux_streams: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigMuxStream(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container: Optional[_builtins.str] = ...,
        elementary_streams: Optional[Sequence[_builtins.str]] = ...,
        encryption_id: Optional[_builtins.str] = ...,
        file_name: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        segment_settings: Optional[
            outputs.JobTemplateConfigMuxStreamSegmentSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionId")
    def encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentSettings")
    def segment_settings(
        self,
    ) -> Optional[outputs.JobTemplateConfigMuxStreamSegmentSettings]: ...

@pulumi.output_type
class JobTemplateConfigMuxStreamSegmentSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, segment_duration: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="segmentDuration")
    def segment_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigOutput(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobTemplateConfigOverlay(dict):
    def __init__(
        __self__,
        *,
        animations: Optional[Sequence[outputs.JobTemplateConfigOverlayAnimation]] = ...,
        image: Optional[outputs.JobTemplateConfigOverlayImage] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def animations(
        self,
    ) -> Optional[Sequence[outputs.JobTemplateConfigOverlayAnimation]]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.JobTemplateConfigOverlayImage]: ...

@pulumi.output_type
class JobTemplateConfigOverlayAnimation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        animation_fade: Optional[
            outputs.JobTemplateConfigOverlayAnimationAnimationFade
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="animationFade")
    def animation_fade(
        self,
    ) -> Optional[outputs.JobTemplateConfigOverlayAnimationAnimationFade]: ...

@pulumi.output_type
class JobTemplateConfigOverlayAnimationAnimationFade(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fade_type: _builtins.str,
        end_time_offset: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
        xy: Optional[outputs.JobTemplateConfigOverlayAnimationAnimationFadeXy] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fadeType")
    def fade_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def xy(
        self,
    ) -> Optional[outputs.JobTemplateConfigOverlayAnimationAnimationFadeXy]: ...

@pulumi.output_type
class JobTemplateConfigOverlayAnimationAnimationFadeXy(dict):
    def __init__(
        __self__,
        *,
        x: Optional[_builtins.float] = ...,
        y: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class JobTemplateConfigOverlayImage(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class JobTemplateConfigPubsubDestination(dict):
    def __init__(__self__, *, topic: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...
