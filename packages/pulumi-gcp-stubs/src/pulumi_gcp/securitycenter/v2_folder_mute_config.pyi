

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['V2FolderMuteConfigArgs', 'V2FolderMuteConfig']
@pulumi.input_type
class V2FolderMuteConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], folder: pulumi.Input[_builtins.str], mute_config_id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mute_config_id.setter
    def mute_config_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _V2FolderMuteConfigState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., most_recent_editor: Optional[pulumi.Input[_builtins.str]] = ..., mute_config_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecentEditor")
    def most_recent_editor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @most_recent_editor.setter
    def most_recent_editor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mute_config_id.setter
    def mute_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class V2FolderMuteConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mute_config_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2FolderMuteConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., most_recent_editor: Optional[pulumi.Input[_builtins.str]] = ..., mute_config_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> V2FolderMuteConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecentEditor")
    def most_recent_editor(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


