

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PresetArgs', 'Preset']
@pulumi.input_type
class PresetArgs:
    def __init__(__self__, *, container: pulumi.Input[_builtins.str], audio: Optional[pulumi.Input[PresetAudioArgs]] = ..., audio_codec_options: Optional[pulumi.Input[PresetAudioCodecOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thumbnails: Optional[pulumi.Input[PresetThumbnailsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., video: Optional[pulumi.Input[PresetVideoArgs]] = ..., video_codec_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., video_watermarks: Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container.setter
    def container(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[pulumi.Input[PresetAudioArgs]]:
        
        ...
    
    @audio.setter
    def audio(self, value: Optional[pulumi.Input[PresetAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioCodecOptions")
    def audio_codec_options(self) -> Optional[pulumi.Input[PresetAudioCodecOptionsArgs]]:
        
        ...
    
    @audio_codec_options.setter
    def audio_codec_options(self, value: Optional[pulumi.Input[PresetAudioCodecOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbnails(self) -> Optional[pulumi.Input[PresetThumbnailsArgs]]:
        
        ...
    
    @thumbnails.setter
    def thumbnails(self, value: Optional[pulumi.Input[PresetThumbnailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def video(self) -> Optional[pulumi.Input[PresetVideoArgs]]:
        
        ...
    
    @video.setter
    def video(self, value: Optional[pulumi.Input[PresetVideoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoCodecOptions")
    def video_codec_options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @video_codec_options.setter
    def video_codec_options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoWatermarks")
    def video_watermarks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]]:
        
        ...
    
    @video_watermarks.setter
    def video_watermarks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _PresetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., audio: Optional[pulumi.Input[PresetAudioArgs]] = ..., audio_codec_options: Optional[pulumi.Input[PresetAudioCodecOptionsArgs]] = ..., container: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thumbnails: Optional[pulumi.Input[PresetThumbnailsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., video: Optional[pulumi.Input[PresetVideoArgs]] = ..., video_codec_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., video_watermarks: Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[pulumi.Input[PresetAudioArgs]]:
        
        ...
    
    @audio.setter
    def audio(self, value: Optional[pulumi.Input[PresetAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioCodecOptions")
    def audio_codec_options(self) -> Optional[pulumi.Input[PresetAudioCodecOptionsArgs]]:
        
        ...
    
    @audio_codec_options.setter
    def audio_codec_options(self, value: Optional[pulumi.Input[PresetAudioCodecOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container.setter
    def container(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbnails(self) -> Optional[pulumi.Input[PresetThumbnailsArgs]]:
        
        ...
    
    @thumbnails.setter
    def thumbnails(self, value: Optional[pulumi.Input[PresetThumbnailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def video(self) -> Optional[pulumi.Input[PresetVideoArgs]]:
        
        ...
    
    @video.setter
    def video(self, value: Optional[pulumi.Input[PresetVideoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoCodecOptions")
    def video_codec_options(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @video_codec_options.setter
    def video_codec_options(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoWatermarks")
    def video_watermarks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]]:
        
        ...
    
    @video_watermarks.setter
    def video_watermarks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PresetVideoWatermarkArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:elastictranscoder/preset:Preset")
class Preset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., audio: Optional[pulumi.Input[Union[PresetAudioArgs, PresetAudioArgsDict]]] = ..., audio_codec_options: Optional[pulumi.Input[Union[PresetAudioCodecOptionsArgs, PresetAudioCodecOptionsArgsDict]]] = ..., container: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thumbnails: Optional[pulumi.Input[Union[PresetThumbnailsArgs, PresetThumbnailsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., video: Optional[pulumi.Input[Union[PresetVideoArgs, PresetVideoArgsDict]]] = ..., video_codec_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., video_watermarks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PresetVideoWatermarkArgs, PresetVideoWatermarkArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PresetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., audio: Optional[pulumi.Input[Union[PresetAudioArgs, PresetAudioArgsDict]]] = ..., audio_codec_options: Optional[pulumi.Input[Union[PresetAudioCodecOptionsArgs, PresetAudioCodecOptionsArgsDict]]] = ..., container: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., thumbnails: Optional[pulumi.Input[Union[PresetThumbnailsArgs, PresetThumbnailsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., video: Optional[pulumi.Input[Union[PresetVideoArgs, PresetVideoArgsDict]]] = ..., video_codec_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., video_watermarks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PresetVideoWatermarkArgs, PresetVideoWatermarkArgsDict]]]]] = ...) -> Preset:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audio(self) -> pulumi.Output[Optional[outputs.PresetAudio]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioCodecOptions")
    def audio_codec_options(self) -> pulumi.Output[outputs.PresetAudioCodecOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbnails(self) -> pulumi.Output[Optional[outputs.PresetThumbnails]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def video(self) -> pulumi.Output[Optional[outputs.PresetVideo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoCodecOptions")
    def video_codec_options(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="videoWatermarks")
    def video_watermarks(self) -> pulumi.Output[Optional[Sequence[outputs.PresetVideoWatermark]]]:
        
        ...
    


