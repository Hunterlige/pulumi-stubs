import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipelineContentConfigArgs",
    "PipelineContentConfigArgsDict",
    "PipelineContentConfigPermissionArgs",
    "PipelineContentConfigPermissionArgsDict",
    "PipelineNotificationsArgs",
    "PipelineNotificationsArgsDict",
    "PipelineThumbnailConfigArgs",
    "PipelineThumbnailConfigArgsDict",
    "PipelineThumbnailConfigPermissionArgs",
    "PipelineThumbnailConfigPermissionArgsDict",
    "PresetAudioArgs",
    "PresetAudioArgsDict",
    "PresetAudioCodecOptionsArgs",
    "PresetAudioCodecOptionsArgsDict",
    "PresetThumbnailsArgs",
    "PresetThumbnailsArgsDict",
    "PresetVideoArgs",
    "PresetVideoArgsDict",
    "PresetVideoWatermarkArgs",
    "PresetVideoWatermarkArgsDict",
]

class PipelineContentConfigArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineContentConfigArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineContentConfigPermissionArgsDict(TypedDict):
    accesses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    grantee: NotRequired[pulumi.Input[_builtins.str]]
    grantee_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineContentConfigPermissionArgs:
    def __init__(
        __self__,
        *,
        accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        grantee: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accesses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accesses.setter
    def accesses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grantee_type.setter
    def grantee_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineNotificationsArgsDict(TypedDict):
    completed: NotRequired[pulumi.Input[_builtins.str]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    progressing: NotRequired[pulumi.Input[_builtins.str]]
    warning: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineNotificationsArgs:
    def __init__(
        __self__,
        *,
        completed: Optional[pulumi.Input[_builtins.str]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        progressing: Optional[pulumi.Input[_builtins.str]] = ...,
        warning: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def completed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @completed.setter
    def completed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def progressing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @progressing.setter
    def progressing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def warning(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warning.setter
    def warning(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineThumbnailConfigArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineThumbnailConfigArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineThumbnailConfigPermissionArgsDict(TypedDict):
    accesses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    grantee: NotRequired[pulumi.Input[_builtins.str]]
    grantee_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineThumbnailConfigPermissionArgs:
    def __init__(
        __self__,
        *,
        accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        grantee: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accesses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accesses.setter
    def accesses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grantee_type.setter
    def grantee_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PresetAudioArgsDict(TypedDict):
    audio_packing_mode: NotRequired[pulumi.Input[_builtins.str]]
    bit_rate: NotRequired[pulumi.Input[_builtins.str]]
    channels: NotRequired[pulumi.Input[_builtins.str]]
    codec: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PresetAudioArgs:
    def __init__(
        __self__,
        *,
        audio_packing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        bit_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        channels: Optional[pulumi.Input[_builtins.str]] = ...,
        codec: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioPackingMode")
    def audio_packing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audio_packing_mode.setter
    def audio_packing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bitRate")
    def bit_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bit_rate.setter
    def bit_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def channels(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channels.setter
    def channels(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codec.setter
    def codec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PresetAudioCodecOptionsArgsDict(TypedDict):
    bit_depth: NotRequired[pulumi.Input[_builtins.str]]
    bit_order: NotRequired[pulumi.Input[_builtins.str]]
    profile: NotRequired[pulumi.Input[_builtins.str]]
    signed: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PresetAudioCodecOptionsArgs:
    def __init__(
        __self__,
        *,
        bit_depth: Optional[pulumi.Input[_builtins.str]] = ...,
        bit_order: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        signed: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitDepth")
    def bit_depth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bit_depth.setter
    def bit_depth(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bitOrder")
    def bit_order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bit_order.setter
    def bit_order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def signed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signed.setter
    def signed(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PresetThumbnailsArgsDict(TypedDict):
    aspect_ratio: NotRequired[pulumi.Input[_builtins.str]]
    format: NotRequired[pulumi.Input[_builtins.str]]
    interval: NotRequired[pulumi.Input[_builtins.str]]
    max_height: NotRequired[pulumi.Input[_builtins.str]]
    max_width: NotRequired[pulumi.Input[_builtins.str]]
    padding_policy: NotRequired[pulumi.Input[_builtins.str]]
    resolution: NotRequired[pulumi.Input[_builtins.str]]
    sizing_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PresetThumbnailsArgs:
    def __init__(
        __self__,
        *,
        aspect_ratio: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        interval: Optional[pulumi.Input[_builtins.str]] = ...,
        max_height: Optional[pulumi.Input[_builtins.str]] = ...,
        max_width: Optional[pulumi.Input[_builtins.str]] = ...,
        padding_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resolution: Optional[pulumi.Input[_builtins.str]] = ...,
        sizing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aspectRatio")
    def aspect_ratio(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aspect_ratio.setter
    def aspect_ratio(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_height.setter
    def max_height(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_width.setter
    def max_width(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="paddingPolicy")
    def padding_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @padding_policy.setter
    def padding_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolution.setter
    def resolution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sizing_policy.setter
    def sizing_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PresetVideoArgsDict(TypedDict):
    aspect_ratio: NotRequired[pulumi.Input[_builtins.str]]
    bit_rate: NotRequired[pulumi.Input[_builtins.str]]
    codec: NotRequired[pulumi.Input[_builtins.str]]
    display_aspect_ratio: NotRequired[pulumi.Input[_builtins.str]]
    fixed_gop: NotRequired[pulumi.Input[_builtins.str]]
    frame_rate: NotRequired[pulumi.Input[_builtins.str]]
    keyframes_max_dist: NotRequired[pulumi.Input[_builtins.str]]
    max_frame_rate: NotRequired[pulumi.Input[_builtins.str]]
    max_height: NotRequired[pulumi.Input[_builtins.str]]
    max_width: NotRequired[pulumi.Input[_builtins.str]]
    padding_policy: NotRequired[pulumi.Input[_builtins.str]]
    resolution: NotRequired[pulumi.Input[_builtins.str]]
    sizing_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PresetVideoArgs:
    def __init__(
        __self__,
        *,
        aspect_ratio: Optional[pulumi.Input[_builtins.str]] = ...,
        bit_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        codec: Optional[pulumi.Input[_builtins.str]] = ...,
        display_aspect_ratio: Optional[pulumi.Input[_builtins.str]] = ...,
        fixed_gop: Optional[pulumi.Input[_builtins.str]] = ...,
        frame_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        keyframes_max_dist: Optional[pulumi.Input[_builtins.str]] = ...,
        max_frame_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        max_height: Optional[pulumi.Input[_builtins.str]] = ...,
        max_width: Optional[pulumi.Input[_builtins.str]] = ...,
        padding_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resolution: Optional[pulumi.Input[_builtins.str]] = ...,
        sizing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aspectRatio")
    def aspect_ratio(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aspect_ratio.setter
    def aspect_ratio(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bitRate")
    def bit_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bit_rate.setter
    def bit_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codec.setter
    def codec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayAspectRatio")
    def display_aspect_ratio(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_aspect_ratio.setter
    def display_aspect_ratio(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fixedGop")
    def fixed_gop(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_gop.setter
    def fixed_gop(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frame_rate.setter
    def frame_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyframesMaxDist")
    def keyframes_max_dist(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyframes_max_dist.setter
    def keyframes_max_dist(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFrameRate")
    def max_frame_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_frame_rate.setter
    def max_frame_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_height.setter
    def max_height(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_width.setter
    def max_width(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="paddingPolicy")
    def padding_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @padding_policy.setter
    def padding_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolution.setter
    def resolution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sizing_policy.setter
    def sizing_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PresetVideoWatermarkArgsDict(TypedDict):
    horizontal_align: NotRequired[pulumi.Input[_builtins.str]]
    horizontal_offset: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    max_height: NotRequired[pulumi.Input[_builtins.str]]
    max_width: NotRequired[pulumi.Input[_builtins.str]]
    opacity: NotRequired[pulumi.Input[_builtins.str]]
    sizing_policy: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    vertical_align: NotRequired[pulumi.Input[_builtins.str]]
    vertical_offset: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PresetVideoWatermarkArgs:
    def __init__(
        __self__,
        *,
        horizontal_align: Optional[pulumi.Input[_builtins.str]] = ...,
        horizontal_offset: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        max_height: Optional[pulumi.Input[_builtins.str]] = ...,
        max_width: Optional[pulumi.Input[_builtins.str]] = ...,
        opacity: Optional[pulumi.Input[_builtins.str]] = ...,
        sizing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        vertical_align: Optional[pulumi.Input[_builtins.str]] = ...,
        vertical_offset: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="horizontalAlign")
    def horizontal_align(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @horizontal_align.setter
    def horizontal_align(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="horizontalOffset")
    def horizontal_offset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @horizontal_offset.setter
    def horizontal_offset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_height.setter
    def max_height(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_width.setter
    def max_width(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def opacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opacity.setter
    def opacity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sizing_policy.setter
    def sizing_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verticalAlign")
    def vertical_align(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vertical_align.setter
    def vertical_align(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verticalOffset")
    def vertical_offset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vertical_offset.setter
    def vertical_offset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
