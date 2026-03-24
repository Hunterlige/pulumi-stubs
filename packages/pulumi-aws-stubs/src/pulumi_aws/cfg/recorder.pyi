

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RecorderArgs', 'Recorder']
@pulumi.input_type
class RecorderArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., recording_group: Optional[pulumi.Input[RecorderRecordingGroupArgs]] = ..., recording_mode: Optional[pulumi.Input[RecorderRecordingModeArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingGroup")
    def recording_group(self) -> Optional[pulumi.Input[RecorderRecordingGroupArgs]]:
        
        ...
    
    @recording_group.setter
    def recording_group(self, value: Optional[pulumi.Input[RecorderRecordingGroupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[pulumi.Input[RecorderRecordingModeArgs]]:
        
        ...
    
    @recording_mode.setter
    def recording_mode(self, value: Optional[pulumi.Input[RecorderRecordingModeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RecorderState:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., recording_group: Optional[pulumi.Input[RecorderRecordingGroupArgs]] = ..., recording_mode: Optional[pulumi.Input[RecorderRecordingModeArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingGroup")
    def recording_group(self) -> Optional[pulumi.Input[RecorderRecordingGroupArgs]]:
        
        ...
    
    @recording_group.setter
    def recording_group(self, value: Optional[pulumi.Input[RecorderRecordingGroupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[pulumi.Input[RecorderRecordingModeArgs]]:
        
        ...
    
    @recording_mode.setter
    def recording_mode(self, value: Optional[pulumi.Input[RecorderRecordingModeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cfg/recorder:Recorder")
class Recorder(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recording_group: Optional[pulumi.Input[Union[RecorderRecordingGroupArgs, RecorderRecordingGroupArgsDict]]] = ..., recording_mode: Optional[pulumi.Input[Union[RecorderRecordingModeArgs, RecorderRecordingModeArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RecorderArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., recording_group: Optional[pulumi.Input[Union[RecorderRecordingGroupArgs, RecorderRecordingGroupArgsDict]]] = ..., recording_mode: Optional[pulumi.Input[Union[RecorderRecordingModeArgs, RecorderRecordingModeArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> Recorder:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingGroup")
    def recording_group(self) -> pulumi.Output[outputs.RecorderRecordingGroup]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> pulumi.Output[outputs.RecorderRecordingMode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


