

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobConfigArgs', 'JobConfigArgsDict', 'JobConfigAdBreakArgs', 'JobConfigAdBreakArgsDict', 'JobConfigEditListArgs', 'JobConfigEditListArgsDict', 'JobConfigElementaryStreamArgs', 'JobConfigElementaryStreamArgsDict', 'JobConfigElementaryStreamAudioStreamArgs', 'JobConfigElementaryStreamAudioStreamArgsDict', 'JobConfigElementaryStreamVideoStreamArgs', 'JobConfigElementaryStreamVideoStreamArgsDict', 'JobConfigElementaryStreamVideoStreamH264Args', 'JobConfigElementaryStreamVideoStreamH264ArgsDict', 'JobConfigElementaryStreamVideoStreamH264HlgArgs', ..., 'JobConfigElementaryStreamVideoStreamH264SdrArgs', ..., 'JobConfigEncryptionArgs', 'JobConfigEncryptionArgsDict', 'JobConfigEncryptionAes128Args', 'JobConfigEncryptionAes128ArgsDict', 'JobConfigEncryptionDrmSystemsArgs', 'JobConfigEncryptionDrmSystemsArgsDict', 'JobConfigEncryptionDrmSystemsClearkeyArgs', 'JobConfigEncryptionDrmSystemsClearkeyArgsDict', 'JobConfigEncryptionDrmSystemsFairplayArgs', 'JobConfigEncryptionDrmSystemsFairplayArgsDict', 'JobConfigEncryptionDrmSystemsPlayreadyArgs', 'JobConfigEncryptionDrmSystemsPlayreadyArgsDict', 'JobConfigEncryptionDrmSystemsWidevineArgs', 'JobConfigEncryptionDrmSystemsWidevineArgsDict', 'JobConfigEncryptionMpegCencArgs', 'JobConfigEncryptionMpegCencArgsDict', 'JobConfigEncryptionSampleAesArgs', 'JobConfigEncryptionSampleAesArgsDict', 'JobConfigEncryptionSecretManagerKeySourceArgs', 'JobConfigEncryptionSecretManagerKeySourceArgsDict', 'JobConfigInputArgs', 'JobConfigInputArgsDict', 'JobConfigManifestArgs', 'JobConfigManifestArgsDict', 'JobConfigMuxStreamArgs', 'JobConfigMuxStreamArgsDict', 'JobConfigMuxStreamSegmentSettingsArgs', 'JobConfigMuxStreamSegmentSettingsArgsDict', 'JobConfigOutputArgs', 'JobConfigOutputArgsDict', 'JobConfigOverlayArgs', 'JobConfigOverlayArgsDict', 'JobConfigOverlayAnimationArgs', 'JobConfigOverlayAnimationArgsDict', 'JobConfigOverlayAnimationAnimationFadeArgs', 'JobConfigOverlayAnimationAnimationFadeArgsDict', 'JobConfigOverlayAnimationAnimationFadeXyArgs', 'JobConfigOverlayAnimationAnimationFadeXyArgsDict', 'JobConfigOverlayImageArgs', 'JobConfigOverlayImageArgsDict', 'JobConfigPubsubDestinationArgs', 'JobConfigPubsubDestinationArgsDict', 'JobTemplateConfigArgs', 'JobTemplateConfigArgsDict', 'JobTemplateConfigAdBreakArgs', 'JobTemplateConfigAdBreakArgsDict', 'JobTemplateConfigEditListArgs', 'JobTemplateConfigEditListArgsDict', 'JobTemplateConfigElementaryStreamArgs', 'JobTemplateConfigElementaryStreamArgsDict', 'JobTemplateConfigElementaryStreamAudioStreamArgs', ..., 'JobTemplateConfigElementaryStreamVideoStreamArgs', ..., ..., ..., ..., ..., ..., ..., 'JobTemplateConfigEncryptionArgs', 'JobTemplateConfigEncryptionArgsDict', 'JobTemplateConfigEncryptionAes128Args', 'JobTemplateConfigEncryptionAes128ArgsDict', 'JobTemplateConfigEncryptionDrmSystemsArgs', 'JobTemplateConfigEncryptionDrmSystemsArgsDict', 'JobTemplateConfigEncryptionDrmSystemsClearkeyArgs', ..., 'JobTemplateConfigEncryptionDrmSystemsFairplayArgs', ..., 'JobTemplateConfigEncryptionDrmSystemsPlayreadyArgs', ..., 'JobTemplateConfigEncryptionDrmSystemsWidevineArgs', ..., 'JobTemplateConfigEncryptionMpegCencArgs', 'JobTemplateConfigEncryptionMpegCencArgsDict', 'JobTemplateConfigEncryptionSampleAesArgs', 'JobTemplateConfigEncryptionSampleAesArgsDict', ..., ..., 'JobTemplateConfigInputArgs', 'JobTemplateConfigInputArgsDict', 'JobTemplateConfigManifestArgs', 'JobTemplateConfigManifestArgsDict', 'JobTemplateConfigMuxStreamArgs', 'JobTemplateConfigMuxStreamArgsDict', 'JobTemplateConfigMuxStreamSegmentSettingsArgs', 'JobTemplateConfigMuxStreamSegmentSettingsArgsDict', 'JobTemplateConfigOutputArgs', 'JobTemplateConfigOutputArgsDict', 'JobTemplateConfigOverlayArgs', 'JobTemplateConfigOverlayArgsDict', 'JobTemplateConfigOverlayAnimationArgs', 'JobTemplateConfigOverlayAnimationArgsDict', 'JobTemplateConfigOverlayAnimationAnimationFadeArgs', ..., ..., ..., 'JobTemplateConfigOverlayImageArgs', 'JobTemplateConfigOverlayImageArgsDict', 'JobTemplateConfigPubsubDestinationArgs', 'JobTemplateConfigPubsubDestinationArgsDict']
class JobConfigArgsDict(TypedDict):
    ad_breaks: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigAdBreakArgsDict]]]]
    edit_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigEditListArgsDict]]]]
    elementary_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigElementaryStreamArgsDict]]]]
    encryptions: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigEncryptionArgsDict]]]]
    inputs: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigInputArgsDict]]]]
    manifests: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigManifestArgsDict]]]]
    mux_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigMuxStreamArgsDict]]]]
    output: NotRequired[pulumi.Input[JobConfigOutputArgsDict]]
    overlays: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayArgsDict]]]]
    pubsub_destination: NotRequired[pulumi.Input[JobConfigPubsubDestinationArgsDict]]


@pulumi.input_type
class JobConfigArgs:
    def __init__(__self__, *, ad_breaks: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigAdBreakArgs]]]] = ..., edit_lists: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEditListArgs]]]] = ..., elementary_streams: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigElementaryStreamArgs]]]] = ..., encryptions: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEncryptionArgs]]]] = ..., inputs: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigInputArgs]]]] = ..., manifests: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigManifestArgs]]]] = ..., mux_streams: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigMuxStreamArgs]]]] = ..., output: Optional[pulumi.Input[JobConfigOutputArgs]] = ..., overlays: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayArgs]]]] = ..., pubsub_destination: Optional[pulumi.Input[JobConfigPubsubDestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adBreaks")
    def ad_breaks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigAdBreakArgs]]]]:
        
        ...
    
    @ad_breaks.setter
    def ad_breaks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigAdBreakArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="editLists")
    def edit_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEditListArgs]]]]:
        
        ...
    
    @edit_lists.setter
    def edit_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEditListArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigElementaryStreamArgs]]]]:
        
        ...
    
    @elementary_streams.setter
    def elementary_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigElementaryStreamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEncryptionArgs]]]]:
        
        ...
    
    @encryptions.setter
    def encryptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigEncryptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigInputArgs]]]]:
        
        ...
    
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigInputArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigManifestArgs]]]]:
        
        ...
    
    @manifests.setter
    def manifests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigManifestArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigMuxStreamArgs]]]]:
        
        ...
    
    @mux_streams.setter
    def mux_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigMuxStreamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input[JobConfigOutputArgs]]:
        
        ...
    
    @output.setter
    def output(self, value: Optional[pulumi.Input[JobConfigOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overlays(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayArgs]]]]:
        
        ...
    
    @overlays.setter
    def overlays(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> Optional[pulumi.Input[JobConfigPubsubDestinationArgs]]:
        
        ...
    
    @pubsub_destination.setter
    def pubsub_destination(self, value: Optional[pulumi.Input[JobConfigPubsubDestinationArgs]]): # -> None:
        ...
    


class JobConfigAdBreakArgsDict(TypedDict):
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigAdBreakArgs:
    def __init__(__self__, *, start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigEditListArgsDict(TypedDict):
    inputs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigEditListArgs:
    def __init__(__self__, *, inputs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigElementaryStreamArgsDict(TypedDict):
    audio_stream: NotRequired[pulumi.Input[JobConfigElementaryStreamAudioStreamArgsDict]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    video_stream: NotRequired[pulumi.Input[JobConfigElementaryStreamVideoStreamArgsDict]]


@pulumi.input_type
class JobConfigElementaryStreamArgs:
    def __init__(__self__, *, audio_stream: Optional[pulumi.Input[JobConfigElementaryStreamAudioStreamArgs]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., video_stream: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioStream")
    def audio_stream(self) -> Optional[pulumi.Input[JobConfigElementaryStreamAudioStreamArgs]]:
        
        ...
    
    @audio_stream.setter
    def audio_stream(self, value: Optional[pulumi.Input[JobConfigElementaryStreamAudioStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoStream")
    def video_stream(self) -> Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamArgs]]:
        
        ...
    
    @video_stream.setter
    def video_stream(self, value: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamArgs]]): # -> None:
        ...
    


class JobConfigElementaryStreamAudioStreamArgsDict(TypedDict):
    bitrate_bps: pulumi.Input[_builtins.int]
    channel_count: NotRequired[pulumi.Input[_builtins.int]]
    channel_layouts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    codec: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate_hertz: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobConfigElementaryStreamAudioStreamArgs:
    def __init__(__self__, *, bitrate_bps: pulumi.Input[_builtins.int], channel_count: Optional[pulumi.Input[_builtins.int]] = ..., channel_layouts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., codec: Optional[pulumi.Input[_builtins.str]] = ..., sample_rate_hertz: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bitrate_bps.setter
    def bitrate_bps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelCount")
    def channel_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @channel_count.setter
    def channel_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelLayouts")
    def channel_layouts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @channel_layouts.setter
    def channel_layouts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @codec.setter
    def codec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sample_rate_hertz.setter
    def sample_rate_hertz(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobConfigElementaryStreamVideoStreamArgsDict(TypedDict):
    h264: NotRequired[pulumi.Input[JobConfigElementaryStreamVideoStreamH264ArgsDict]]


@pulumi.input_type
class JobConfigElementaryStreamVideoStreamArgs:
    def __init__(__self__, *, h264: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def h264(self) -> Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264Args]]:
        
        ...
    
    @h264.setter
    def h264(self, value: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264Args]]): # -> None:
        ...
    


class JobConfigElementaryStreamVideoStreamH264ArgsDict(TypedDict):
    bitrate_bps: pulumi.Input[_builtins.int]
    frame_rate: pulumi.Input[_builtins.int]
    crf_level: NotRequired[pulumi.Input[_builtins.int]]
    entropy_coder: NotRequired[pulumi.Input[_builtins.str]]
    gop_duration: NotRequired[pulumi.Input[_builtins.str]]
    height_pixels: NotRequired[pulumi.Input[_builtins.int]]
    hlg: NotRequired[pulumi.Input[JobConfigElementaryStreamVideoStreamH264HlgArgsDict]]
    pixel_format: NotRequired[pulumi.Input[_builtins.str]]
    preset: NotRequired[pulumi.Input[_builtins.str]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    rate_control_mode: NotRequired[pulumi.Input[_builtins.str]]
    sdr: NotRequired[pulumi.Input[JobConfigElementaryStreamVideoStreamH264SdrArgsDict]]
    vbv_fullness_bits: NotRequired[pulumi.Input[_builtins.int]]
    vbv_size_bits: NotRequired[pulumi.Input[_builtins.int]]
    width_pixels: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobConfigElementaryStreamVideoStreamH264Args:
    def __init__(__self__, *, bitrate_bps: pulumi.Input[_builtins.int], frame_rate: pulumi.Input[_builtins.int], crf_level: Optional[pulumi.Input[_builtins.int]] = ..., entropy_coder: Optional[pulumi.Input[_builtins.str]] = ..., gop_duration: Optional[pulumi.Input[_builtins.str]] = ..., height_pixels: Optional[pulumi.Input[_builtins.int]] = ..., hlg: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264HlgArgs]] = ..., pixel_format: Optional[pulumi.Input[_builtins.str]] = ..., preset: Optional[pulumi.Input[_builtins.str]] = ..., profile: Optional[pulumi.Input[_builtins.str]] = ..., rate_control_mode: Optional[pulumi.Input[_builtins.str]] = ..., sdr: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264SdrArgs]] = ..., vbv_fullness_bits: Optional[pulumi.Input[_builtins.int]] = ..., vbv_size_bits: Optional[pulumi.Input[_builtins.int]] = ..., width_pixels: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bitrate_bps.setter
    def bitrate_bps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @frame_rate.setter
    def frame_rate(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crfLevel")
    def crf_level(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @crf_level.setter
    def crf_level(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entropyCoder")
    def entropy_coder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entropy_coder.setter
    def entropy_coder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gopDuration")
    def gop_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gop_duration.setter
    def gop_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heightPixels")
    def height_pixels(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @height_pixels.setter
    def height_pixels(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hlg(self) -> Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264HlgArgs]]:
        
        ...
    
    @hlg.setter
    def hlg(self, value: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264HlgArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pixelFormat")
    def pixel_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pixel_format.setter
    def pixel_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preset.setter
    def preset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rate_control_mode.setter
    def rate_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sdr(self) -> Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264SdrArgs]]:
        
        ...
    
    @sdr.setter
    def sdr(self, value: Optional[pulumi.Input[JobConfigElementaryStreamVideoStreamH264SdrArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vbvFullnessBits")
    def vbv_fullness_bits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vbv_fullness_bits.setter
    def vbv_fullness_bits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vbvSizeBits")
    def vbv_size_bits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vbv_size_bits.setter
    def vbv_size_bits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="widthPixels")
    def width_pixels(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @width_pixels.setter
    def width_pixels(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobConfigElementaryStreamVideoStreamH264HlgArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigElementaryStreamVideoStreamH264HlgArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigElementaryStreamVideoStreamH264SdrArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigElementaryStreamVideoStreamH264SdrArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    aes128: NotRequired[pulumi.Input[JobConfigEncryptionAes128ArgsDict]]
    drm_systems: NotRequired[pulumi.Input[JobConfigEncryptionDrmSystemsArgsDict]]
    mpeg_cenc: NotRequired[pulumi.Input[JobConfigEncryptionMpegCencArgsDict]]
    sample_aes: NotRequired[pulumi.Input[JobConfigEncryptionSampleAesArgsDict]]
    secret_manager_key_source: NotRequired[pulumi.Input[JobConfigEncryptionSecretManagerKeySourceArgsDict]]


@pulumi.input_type
class JobConfigEncryptionArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], aes128: Optional[pulumi.Input[JobConfigEncryptionAes128Args]] = ..., drm_systems: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsArgs]] = ..., mpeg_cenc: Optional[pulumi.Input[JobConfigEncryptionMpegCencArgs]] = ..., sample_aes: Optional[pulumi.Input[JobConfigEncryptionSampleAesArgs]] = ..., secret_manager_key_source: Optional[pulumi.Input[JobConfigEncryptionSecretManagerKeySourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aes128(self) -> Optional[pulumi.Input[JobConfigEncryptionAes128Args]]:
        
        ...
    
    @aes128.setter
    def aes128(self, value: Optional[pulumi.Input[JobConfigEncryptionAes128Args]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="drmSystems")
    def drm_systems(self) -> Optional[pulumi.Input[JobConfigEncryptionDrmSystemsArgs]]:
        
        ...
    
    @drm_systems.setter
    def drm_systems(self, value: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mpegCenc")
    def mpeg_cenc(self) -> Optional[pulumi.Input[JobConfigEncryptionMpegCencArgs]]:
        
        ...
    
    @mpeg_cenc.setter
    def mpeg_cenc(self, value: Optional[pulumi.Input[JobConfigEncryptionMpegCencArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleAes")
    def sample_aes(self) -> Optional[pulumi.Input[JobConfigEncryptionSampleAesArgs]]:
        
        ...
    
    @sample_aes.setter
    def sample_aes(self, value: Optional[pulumi.Input[JobConfigEncryptionSampleAesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerKeySource")
    def secret_manager_key_source(self) -> Optional[pulumi.Input[JobConfigEncryptionSecretManagerKeySourceArgs]]:
        
        ...
    
    @secret_manager_key_source.setter
    def secret_manager_key_source(self, value: Optional[pulumi.Input[JobConfigEncryptionSecretManagerKeySourceArgs]]): # -> None:
        ...
    


class JobConfigEncryptionAes128ArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionAes128Args:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionDrmSystemsArgsDict(TypedDict):
    clearkey: NotRequired[pulumi.Input[JobConfigEncryptionDrmSystemsClearkeyArgsDict]]
    fairplay: NotRequired[pulumi.Input[JobConfigEncryptionDrmSystemsFairplayArgsDict]]
    playready: NotRequired[pulumi.Input[JobConfigEncryptionDrmSystemsPlayreadyArgsDict]]
    widevine: NotRequired[pulumi.Input[JobConfigEncryptionDrmSystemsWidevineArgsDict]]


@pulumi.input_type
class JobConfigEncryptionDrmSystemsArgs:
    def __init__(__self__, *, clearkey: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsClearkeyArgs]] = ..., fairplay: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsFairplayArgs]] = ..., playready: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsPlayreadyArgs]] = ..., widevine: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsWidevineArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clearkey(self) -> Optional[pulumi.Input[JobConfigEncryptionDrmSystemsClearkeyArgs]]:
        
        ...
    
    @clearkey.setter
    def clearkey(self, value: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsClearkeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fairplay(self) -> Optional[pulumi.Input[JobConfigEncryptionDrmSystemsFairplayArgs]]:
        
        ...
    
    @fairplay.setter
    def fairplay(self, value: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsFairplayArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def playready(self) -> Optional[pulumi.Input[JobConfigEncryptionDrmSystemsPlayreadyArgs]]:
        
        ...
    
    @playready.setter
    def playready(self, value: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsPlayreadyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def widevine(self) -> Optional[pulumi.Input[JobConfigEncryptionDrmSystemsWidevineArgs]]:
        
        ...
    
    @widevine.setter
    def widevine(self, value: Optional[pulumi.Input[JobConfigEncryptionDrmSystemsWidevineArgs]]): # -> None:
        ...
    


class JobConfigEncryptionDrmSystemsClearkeyArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionDrmSystemsClearkeyArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionDrmSystemsFairplayArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionDrmSystemsFairplayArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionDrmSystemsPlayreadyArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionDrmSystemsPlayreadyArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionDrmSystemsWidevineArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionDrmSystemsWidevineArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionMpegCencArgsDict(TypedDict):
    scheme: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobConfigEncryptionMpegCencArgs:
    def __init__(__self__, *, scheme: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scheme.setter
    def scheme(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobConfigEncryptionSampleAesArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobConfigEncryptionSampleAesArgs:
    def __init__(__self__) -> None:
        ...
    


class JobConfigEncryptionSecretManagerKeySourceArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobConfigEncryptionSecretManagerKeySourceArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobConfigInputArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigInputArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigManifestArgsDict(TypedDict):
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    mux_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigManifestArgs:
    def __init__(__self__, *, file_name: Optional[pulumi.Input[_builtins.str]] = ..., mux_streams: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @mux_streams.setter
    def mux_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigMuxStreamArgsDict(TypedDict):
    container: NotRequired[pulumi.Input[_builtins.str]]
    elementary_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    segment_settings: NotRequired[pulumi.Input[JobConfigMuxStreamSegmentSettingsArgsDict]]


@pulumi.input_type
class JobConfigMuxStreamArgs:
    def __init__(__self__, *, container: Optional[pulumi.Input[_builtins.str]] = ..., elementary_streams: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., file_name: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., segment_settings: Optional[pulumi.Input[JobConfigMuxStreamSegmentSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container.setter
    def container(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @elementary_streams.setter
    def elementary_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionId")
    def encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_id.setter
    def encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentSettings")
    def segment_settings(self) -> Optional[pulumi.Input[JobConfigMuxStreamSegmentSettingsArgs]]:
        
        ...
    
    @segment_settings.setter
    def segment_settings(self, value: Optional[pulumi.Input[JobConfigMuxStreamSegmentSettingsArgs]]): # -> None:
        ...
    


class JobConfigMuxStreamSegmentSettingsArgsDict(TypedDict):
    segment_duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigMuxStreamSegmentSettingsArgs:
    def __init__(__self__, *, segment_duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentDuration")
    def segment_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @segment_duration.setter
    def segment_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigOutputArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigOutputArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigOverlayArgsDict(TypedDict):
    animations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayAnimationArgsDict]]]]
    image: NotRequired[pulumi.Input[JobConfigOverlayImageArgsDict]]


@pulumi.input_type
class JobConfigOverlayArgs:
    def __init__(__self__, *, animations: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayAnimationArgs]]]] = ..., image: Optional[pulumi.Input[JobConfigOverlayImageArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def animations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayAnimationArgs]]]]:
        
        ...
    
    @animations.setter
    def animations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConfigOverlayAnimationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[JobConfigOverlayImageArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[JobConfigOverlayImageArgs]]): # -> None:
        ...
    


class JobConfigOverlayAnimationArgsDict(TypedDict):
    animation_fade: NotRequired[pulumi.Input[JobConfigOverlayAnimationAnimationFadeArgsDict]]


@pulumi.input_type
class JobConfigOverlayAnimationArgs:
    def __init__(__self__, *, animation_fade: Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="animationFade")
    def animation_fade(self) -> Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeArgs]]:
        
        ...
    
    @animation_fade.setter
    def animation_fade(self, value: Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeArgs]]): # -> None:
        ...
    


class JobConfigOverlayAnimationAnimationFadeArgsDict(TypedDict):
    fade_type: pulumi.Input[_builtins.str]
    end_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    xy: NotRequired[pulumi.Input[JobConfigOverlayAnimationAnimationFadeXyArgsDict]]


@pulumi.input_type
class JobConfigOverlayAnimationAnimationFadeArgs:
    def __init__(__self__, *, fade_type: pulumi.Input[_builtins.str], end_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., xy: Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeXyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fadeType")
    def fade_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fade_type.setter
    def fade_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_offset.setter
    def end_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def xy(self) -> Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeXyArgs]]:
        
        ...
    
    @xy.setter
    def xy(self, value: Optional[pulumi.Input[JobConfigOverlayAnimationAnimationFadeXyArgs]]): # -> None:
        ...
    


class JobConfigOverlayAnimationAnimationFadeXyArgsDict(TypedDict):
    x: NotRequired[pulumi.Input[_builtins.float]]
    y: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class JobConfigOverlayAnimationAnimationFadeXyArgs:
    def __init__(__self__, *, x: Optional[pulumi.Input[_builtins.float]] = ..., y: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @x.setter
    def x(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @y.setter
    def y(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class JobConfigOverlayImageArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobConfigOverlayImageArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobConfigPubsubDestinationArgsDict(TypedDict):
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobConfigPubsubDestinationArgs:
    def __init__(__self__, *, topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigArgsDict(TypedDict):
    ad_breaks: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigAdBreakArgsDict]]]]
    edit_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEditListArgsDict]]]]
    elementary_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigElementaryStreamArgsDict]]]]
    encryptions: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEncryptionArgsDict]]]]
    inputs: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigInputArgsDict]]]]
    manifests: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigManifestArgsDict]]]]
    mux_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigMuxStreamArgsDict]]]]
    output: NotRequired[pulumi.Input[JobTemplateConfigOutputArgsDict]]
    overlays: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayArgsDict]]]]
    pubsub_destination: NotRequired[pulumi.Input[JobTemplateConfigPubsubDestinationArgsDict]]


@pulumi.input_type
class JobTemplateConfigArgs:
    def __init__(__self__, *, ad_breaks: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigAdBreakArgs]]]] = ..., edit_lists: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEditListArgs]]]] = ..., elementary_streams: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigElementaryStreamArgs]]]] = ..., encryptions: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEncryptionArgs]]]] = ..., inputs: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigInputArgs]]]] = ..., manifests: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigManifestArgs]]]] = ..., mux_streams: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigMuxStreamArgs]]]] = ..., output: Optional[pulumi.Input[JobTemplateConfigOutputArgs]] = ..., overlays: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayArgs]]]] = ..., pubsub_destination: Optional[pulumi.Input[JobTemplateConfigPubsubDestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adBreaks")
    def ad_breaks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigAdBreakArgs]]]]:
        
        ...
    
    @ad_breaks.setter
    def ad_breaks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigAdBreakArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="editLists")
    def edit_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEditListArgs]]]]:
        
        ...
    
    @edit_lists.setter
    def edit_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEditListArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigElementaryStreamArgs]]]]:
        
        ...
    
    @elementary_streams.setter
    def elementary_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigElementaryStreamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEncryptionArgs]]]]:
        
        ...
    
    @encryptions.setter
    def encryptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigEncryptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigInputArgs]]]]:
        
        ...
    
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigInputArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigManifestArgs]]]]:
        
        ...
    
    @manifests.setter
    def manifests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigManifestArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigMuxStreamArgs]]]]:
        
        ...
    
    @mux_streams.setter
    def mux_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigMuxStreamArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input[JobTemplateConfigOutputArgs]]:
        
        ...
    
    @output.setter
    def output(self, value: Optional[pulumi.Input[JobTemplateConfigOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overlays(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayArgs]]]]:
        
        ...
    
    @overlays.setter
    def overlays(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(self) -> Optional[pulumi.Input[JobTemplateConfigPubsubDestinationArgs]]:
        
        ...
    
    @pubsub_destination.setter
    def pubsub_destination(self, value: Optional[pulumi.Input[JobTemplateConfigPubsubDestinationArgs]]): # -> None:
        ...
    


class JobTemplateConfigAdBreakArgsDict(TypedDict):
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigAdBreakArgs:
    def __init__(__self__, *, start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigEditListArgsDict(TypedDict):
    inputs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigEditListArgs:
    def __init__(__self__, *, inputs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigElementaryStreamArgsDict(TypedDict):
    audio_stream: NotRequired[pulumi.Input[JobTemplateConfigElementaryStreamAudioStreamArgsDict]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    video_stream: NotRequired[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamArgsDict]]


@pulumi.input_type
class JobTemplateConfigElementaryStreamArgs:
    def __init__(__self__, *, audio_stream: Optional[pulumi.Input[JobTemplateConfigElementaryStreamAudioStreamArgs]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., video_stream: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioStream")
    def audio_stream(self) -> Optional[pulumi.Input[JobTemplateConfigElementaryStreamAudioStreamArgs]]:
        
        ...
    
    @audio_stream.setter
    def audio_stream(self, value: Optional[pulumi.Input[JobTemplateConfigElementaryStreamAudioStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoStream")
    def video_stream(self) -> Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamArgs]]:
        
        ...
    
    @video_stream.setter
    def video_stream(self, value: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamArgs]]): # -> None:
        ...
    


class JobTemplateConfigElementaryStreamAudioStreamArgsDict(TypedDict):
    bitrate_bps: pulumi.Input[_builtins.int]
    channel_count: NotRequired[pulumi.Input[_builtins.int]]
    channel_layouts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    codec: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate_hertz: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobTemplateConfigElementaryStreamAudioStreamArgs:
    def __init__(__self__, *, bitrate_bps: pulumi.Input[_builtins.int], channel_count: Optional[pulumi.Input[_builtins.int]] = ..., channel_layouts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., codec: Optional[pulumi.Input[_builtins.str]] = ..., sample_rate_hertz: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bitrate_bps.setter
    def bitrate_bps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelCount")
    def channel_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @channel_count.setter
    def channel_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelLayouts")
    def channel_layouts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @channel_layouts.setter
    def channel_layouts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @codec.setter
    def codec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sample_rate_hertz.setter
    def sample_rate_hertz(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobTemplateConfigElementaryStreamVideoStreamArgsDict(TypedDict):
    h264: NotRequired[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264ArgsDict]]


@pulumi.input_type
class JobTemplateConfigElementaryStreamVideoStreamArgs:
    def __init__(__self__, *, h264: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def h264(self) -> Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264Args]]:
        
        ...
    
    @h264.setter
    def h264(self, value: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264Args]]): # -> None:
        ...
    


class JobTemplateConfigElementaryStreamVideoStreamH264ArgsDict(TypedDict):
    bitrate_bps: pulumi.Input[_builtins.int]
    frame_rate: pulumi.Input[_builtins.int]
    crf_level: NotRequired[pulumi.Input[_builtins.int]]
    entropy_coder: NotRequired[pulumi.Input[_builtins.str]]
    gop_duration: NotRequired[pulumi.Input[_builtins.str]]
    height_pixels: NotRequired[pulumi.Input[_builtins.int]]
    hlg: NotRequired[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264HlgArgsDict]]
    pixel_format: NotRequired[pulumi.Input[_builtins.str]]
    preset: NotRequired[pulumi.Input[_builtins.str]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    rate_control_mode: NotRequired[pulumi.Input[_builtins.str]]
    sdr: NotRequired[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264SdrArgsDict]]
    vbv_fullness_bits: NotRequired[pulumi.Input[_builtins.int]]
    vbv_size_bits: NotRequired[pulumi.Input[_builtins.int]]
    width_pixels: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobTemplateConfigElementaryStreamVideoStreamH264Args:
    def __init__(__self__, *, bitrate_bps: pulumi.Input[_builtins.int], frame_rate: pulumi.Input[_builtins.int], crf_level: Optional[pulumi.Input[_builtins.int]] = ..., entropy_coder: Optional[pulumi.Input[_builtins.str]] = ..., gop_duration: Optional[pulumi.Input[_builtins.str]] = ..., height_pixels: Optional[pulumi.Input[_builtins.int]] = ..., hlg: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264HlgArgs]] = ..., pixel_format: Optional[pulumi.Input[_builtins.str]] = ..., preset: Optional[pulumi.Input[_builtins.str]] = ..., profile: Optional[pulumi.Input[_builtins.str]] = ..., rate_control_mode: Optional[pulumi.Input[_builtins.str]] = ..., sdr: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264SdrArgs]] = ..., vbv_fullness_bits: Optional[pulumi.Input[_builtins.int]] = ..., vbv_size_bits: Optional[pulumi.Input[_builtins.int]] = ..., width_pixels: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitrateBps")
    def bitrate_bps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bitrate_bps.setter
    def bitrate_bps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @frame_rate.setter
    def frame_rate(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crfLevel")
    def crf_level(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @crf_level.setter
    def crf_level(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entropyCoder")
    def entropy_coder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entropy_coder.setter
    def entropy_coder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gopDuration")
    def gop_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gop_duration.setter
    def gop_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heightPixels")
    def height_pixels(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @height_pixels.setter
    def height_pixels(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hlg(self) -> Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264HlgArgs]]:
        
        ...
    
    @hlg.setter
    def hlg(self, value: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264HlgArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pixelFormat")
    def pixel_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pixel_format.setter
    def pixel_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preset.setter
    def preset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateControlMode")
    def rate_control_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rate_control_mode.setter
    def rate_control_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sdr(self) -> Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264SdrArgs]]:
        
        ...
    
    @sdr.setter
    def sdr(self, value: Optional[pulumi.Input[JobTemplateConfigElementaryStreamVideoStreamH264SdrArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vbvFullnessBits")
    def vbv_fullness_bits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vbv_fullness_bits.setter
    def vbv_fullness_bits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vbvSizeBits")
    def vbv_size_bits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vbv_size_bits.setter
    def vbv_size_bits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="widthPixels")
    def width_pixels(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @width_pixels.setter
    def width_pixels(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobTemplateConfigElementaryStreamVideoStreamH264HlgArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigElementaryStreamVideoStreamH264HlgArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigElementaryStreamVideoStreamH264SdrArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigElementaryStreamVideoStreamH264SdrArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    aes128: NotRequired[pulumi.Input[JobTemplateConfigEncryptionAes128ArgsDict]]
    drm_systems: NotRequired[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsArgsDict]]
    mpeg_cenc: NotRequired[pulumi.Input[JobTemplateConfigEncryptionMpegCencArgsDict]]
    sample_aes: NotRequired[pulumi.Input[JobTemplateConfigEncryptionSampleAesArgsDict]]
    secret_manager_key_source: NotRequired[pulumi.Input[JobTemplateConfigEncryptionSecretManagerKeySourceArgsDict]]


@pulumi.input_type
class JobTemplateConfigEncryptionArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], aes128: Optional[pulumi.Input[JobTemplateConfigEncryptionAes128Args]] = ..., drm_systems: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsArgs]] = ..., mpeg_cenc: Optional[pulumi.Input[JobTemplateConfigEncryptionMpegCencArgs]] = ..., sample_aes: Optional[pulumi.Input[JobTemplateConfigEncryptionSampleAesArgs]] = ..., secret_manager_key_source: Optional[pulumi.Input[JobTemplateConfigEncryptionSecretManagerKeySourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aes128(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionAes128Args]]:
        
        ...
    
    @aes128.setter
    def aes128(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionAes128Args]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="drmSystems")
    def drm_systems(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsArgs]]:
        
        ...
    
    @drm_systems.setter
    def drm_systems(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mpegCenc")
    def mpeg_cenc(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionMpegCencArgs]]:
        
        ...
    
    @mpeg_cenc.setter
    def mpeg_cenc(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionMpegCencArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleAes")
    def sample_aes(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionSampleAesArgs]]:
        
        ...
    
    @sample_aes.setter
    def sample_aes(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionSampleAesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerKeySource")
    def secret_manager_key_source(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionSecretManagerKeySourceArgs]]:
        
        ...
    
    @secret_manager_key_source.setter
    def secret_manager_key_source(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionSecretManagerKeySourceArgs]]): # -> None:
        ...
    


class JobTemplateConfigEncryptionAes128ArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionAes128Args:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionDrmSystemsArgsDict(TypedDict):
    clearkey: NotRequired[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsClearkeyArgsDict]]
    fairplay: NotRequired[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsFairplayArgsDict]]
    playready: NotRequired[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsPlayreadyArgsDict]]
    widevine: NotRequired[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsWidevineArgsDict]]


@pulumi.input_type
class JobTemplateConfigEncryptionDrmSystemsArgs:
    def __init__(__self__, *, clearkey: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsClearkeyArgs]] = ..., fairplay: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsFairplayArgs]] = ..., playready: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsPlayreadyArgs]] = ..., widevine: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsWidevineArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clearkey(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsClearkeyArgs]]:
        
        ...
    
    @clearkey.setter
    def clearkey(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsClearkeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fairplay(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsFairplayArgs]]:
        
        ...
    
    @fairplay.setter
    def fairplay(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsFairplayArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def playready(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsPlayreadyArgs]]:
        
        ...
    
    @playready.setter
    def playready(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsPlayreadyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def widevine(self) -> Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsWidevineArgs]]:
        
        ...
    
    @widevine.setter
    def widevine(self, value: Optional[pulumi.Input[JobTemplateConfigEncryptionDrmSystemsWidevineArgs]]): # -> None:
        ...
    


class JobTemplateConfigEncryptionDrmSystemsClearkeyArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionDrmSystemsClearkeyArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionDrmSystemsFairplayArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionDrmSystemsFairplayArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionDrmSystemsPlayreadyArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionDrmSystemsPlayreadyArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionDrmSystemsWidevineArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionDrmSystemsWidevineArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionMpegCencArgsDict(TypedDict):
    scheme: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobTemplateConfigEncryptionMpegCencArgs:
    def __init__(__self__, *, scheme: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scheme.setter
    def scheme(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobTemplateConfigEncryptionSampleAesArgsDict(TypedDict):
    ...


@pulumi.input_type
class JobTemplateConfigEncryptionSampleAesArgs:
    def __init__(__self__) -> None:
        ...
    


class JobTemplateConfigEncryptionSecretManagerKeySourceArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobTemplateConfigEncryptionSecretManagerKeySourceArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobTemplateConfigInputArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigInputArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigManifestArgsDict(TypedDict):
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    mux_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigManifestArgs:
    def __init__(__self__, *, file_name: Optional[pulumi.Input[_builtins.str]] = ..., mux_streams: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muxStreams")
    def mux_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @mux_streams.setter
    def mux_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigMuxStreamArgsDict(TypedDict):
    container: NotRequired[pulumi.Input[_builtins.str]]
    elementary_streams: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    segment_settings: NotRequired[pulumi.Input[JobTemplateConfigMuxStreamSegmentSettingsArgsDict]]


@pulumi.input_type
class JobTemplateConfigMuxStreamArgs:
    def __init__(__self__, *, container: Optional[pulumi.Input[_builtins.str]] = ..., elementary_streams: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., file_name: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., segment_settings: Optional[pulumi.Input[JobTemplateConfigMuxStreamSegmentSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container.setter
    def container(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elementaryStreams")
    def elementary_streams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @elementary_streams.setter
    def elementary_streams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionId")
    def encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_id.setter
    def encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentSettings")
    def segment_settings(self) -> Optional[pulumi.Input[JobTemplateConfigMuxStreamSegmentSettingsArgs]]:
        
        ...
    
    @segment_settings.setter
    def segment_settings(self, value: Optional[pulumi.Input[JobTemplateConfigMuxStreamSegmentSettingsArgs]]): # -> None:
        ...
    


class JobTemplateConfigMuxStreamSegmentSettingsArgsDict(TypedDict):
    segment_duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigMuxStreamSegmentSettingsArgs:
    def __init__(__self__, *, segment_duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentDuration")
    def segment_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @segment_duration.setter
    def segment_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigOutputArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigOutputArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobTemplateConfigOverlayArgsDict(TypedDict):
    animations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayAnimationArgsDict]]]]
    image: NotRequired[pulumi.Input[JobTemplateConfigOverlayImageArgsDict]]


@pulumi.input_type
class JobTemplateConfigOverlayArgs:
    def __init__(__self__, *, animations: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayAnimationArgs]]]] = ..., image: Optional[pulumi.Input[JobTemplateConfigOverlayImageArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def animations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayAnimationArgs]]]]:
        
        ...
    
    @animations.setter
    def animations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTemplateConfigOverlayAnimationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[JobTemplateConfigOverlayImageArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[JobTemplateConfigOverlayImageArgs]]): # -> None:
        ...
    


class JobTemplateConfigOverlayAnimationArgsDict(TypedDict):
    animation_fade: NotRequired[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeArgsDict]]


@pulumi.input_type
class JobTemplateConfigOverlayAnimationArgs:
    def __init__(__self__, *, animation_fade: Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="animationFade")
    def animation_fade(self) -> Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeArgs]]:
        
        ...
    
    @animation_fade.setter
    def animation_fade(self, value: Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeArgs]]): # -> None:
        ...
    


class JobTemplateConfigOverlayAnimationAnimationFadeArgsDict(TypedDict):
    fade_type: pulumi.Input[_builtins.str]
    end_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    xy: NotRequired[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeXyArgsDict]]


@pulumi.input_type
class JobTemplateConfigOverlayAnimationAnimationFadeArgs:
    def __init__(__self__, *, fade_type: pulumi.Input[_builtins.str], end_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., xy: Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeXyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fadeType")
    def fade_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fade_type.setter
    def fade_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_offset.setter
    def end_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def xy(self) -> Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeXyArgs]]:
        
        ...
    
    @xy.setter
    def xy(self, value: Optional[pulumi.Input[JobTemplateConfigOverlayAnimationAnimationFadeXyArgs]]): # -> None:
        ...
    


class JobTemplateConfigOverlayAnimationAnimationFadeXyArgsDict(TypedDict):
    x: NotRequired[pulumi.Input[_builtins.float]]
    y: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class JobTemplateConfigOverlayAnimationAnimationFadeXyArgs:
    def __init__(__self__, *, x: Optional[pulumi.Input[_builtins.float]] = ..., y: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @x.setter
    def x(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @y.setter
    def y(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class JobTemplateConfigOverlayImageArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobTemplateConfigOverlayImageArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobTemplateConfigPubsubDestinationArgsDict(TypedDict):
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobTemplateConfigPubsubDestinationArgs:
    def __init__(__self__, *, topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


