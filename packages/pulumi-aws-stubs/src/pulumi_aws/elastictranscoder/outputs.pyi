

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PipelineContentConfig', 'PipelineContentConfigPermission', 'PipelineNotifications', 'PipelineThumbnailConfig', 'PipelineThumbnailConfigPermission', 'PresetAudio', 'PresetAudioCodecOptions', 'PresetThumbnails', 'PresetVideo', 'PresetVideoWatermark']
@pulumi.output_type
class PipelineContentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., storage_class: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineContentConfigPermission(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accesses: Optional[Sequence[_builtins.str]] = ..., grantee: Optional[_builtins.str] = ..., grantee_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accesses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineNotifications(dict):
    def __init__(__self__, *, completed: Optional[_builtins.str] = ..., error: Optional[_builtins.str] = ..., progressing: Optional[_builtins.str] = ..., warning: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def completed(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def progressing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def warning(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineThumbnailConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., storage_class: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PipelineThumbnailConfigPermission(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accesses: Optional[Sequence[_builtins.str]] = ..., grantee: Optional[_builtins.str] = ..., grantee_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accesses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PresetAudio(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audio_packing_mode: Optional[_builtins.str] = ..., bit_rate: Optional[_builtins.str] = ..., channels: Optional[_builtins.str] = ..., codec: Optional[_builtins.str] = ..., sample_rate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioPackingMode")
    def audio_packing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitRate")
    def bit_rate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channels(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PresetAudioCodecOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bit_depth: Optional[_builtins.str] = ..., bit_order: Optional[_builtins.str] = ..., profile: Optional[_builtins.str] = ..., signed: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitDepth")
    def bit_depth(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitOrder")
    def bit_order(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def signed(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PresetThumbnails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aspect_ratio: Optional[_builtins.str] = ..., format: Optional[_builtins.str] = ..., interval: Optional[_builtins.str] = ..., max_height: Optional[_builtins.str] = ..., max_width: Optional[_builtins.str] = ..., padding_policy: Optional[_builtins.str] = ..., resolution: Optional[_builtins.str] = ..., sizing_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aspectRatio")
    def aspect_ratio(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paddingPolicy")
    def padding_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PresetVideo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aspect_ratio: Optional[_builtins.str] = ..., bit_rate: Optional[_builtins.str] = ..., codec: Optional[_builtins.str] = ..., display_aspect_ratio: Optional[_builtins.str] = ..., fixed_gop: Optional[_builtins.str] = ..., frame_rate: Optional[_builtins.str] = ..., keyframes_max_dist: Optional[_builtins.str] = ..., max_frame_rate: Optional[_builtins.str] = ..., max_height: Optional[_builtins.str] = ..., max_width: Optional[_builtins.str] = ..., padding_policy: Optional[_builtins.str] = ..., resolution: Optional[_builtins.str] = ..., sizing_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aspectRatio")
    def aspect_ratio(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitRate")
    def bit_rate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def codec(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayAspectRatio")
    def display_aspect_ratio(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedGop")
    def fixed_gop(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameRate")
    def frame_rate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyframesMaxDist")
    def keyframes_max_dist(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFrameRate")
    def max_frame_rate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paddingPolicy")
    def padding_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resolution(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PresetVideoWatermark(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, horizontal_align: Optional[_builtins.str] = ..., horizontal_offset: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., max_height: Optional[_builtins.str] = ..., max_width: Optional[_builtins.str] = ..., opacity: Optional[_builtins.str] = ..., sizing_policy: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ..., vertical_align: Optional[_builtins.str] = ..., vertical_offset: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="horizontalAlign")
    def horizontal_align(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="horizontalOffset")
    def horizontal_offset(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHeight")
    def max_height(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWidth")
    def max_width(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def opacity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingPolicy")
    def sizing_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalAlign")
    def vertical_align(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalOffset")
    def vertical_offset(self) -> Optional[_builtins.str]:
        
        ...
    


