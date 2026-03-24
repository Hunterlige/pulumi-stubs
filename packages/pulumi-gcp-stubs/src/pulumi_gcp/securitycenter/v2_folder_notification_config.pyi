

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
__all__ = ['V2FolderNotificationConfigArgs', 'V2FolderNotificationConfig']
@pulumi.input_type
class V2FolderNotificationConfigArgs:
    def __init__(__self__, *, config_id: pulumi.Input[_builtins.str], folder: pulumi.Input[_builtins.str], pubsub_topic: pulumi.Input[_builtins.str], streaming_config: pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @config_id.setter
    def config_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingConfig")
    def streaming_config(self) -> pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs]:
        
        ...
    
    @streaming_config.setter
    def streaming_config(self, value: pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs]): # -> None:
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
class _V2FolderNotificationConfigState:
    def __init__(__self__, *, config_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., streaming_config: Optional[pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingConfig")
    def streaming_config(self) -> Optional[pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs]]:
        
        ...
    
    @streaming_config.setter
    def streaming_config(self, value: Optional[pulumi.Input[V2FolderNotificationConfigStreamingConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class V2FolderNotificationConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., config_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., streaming_config: Optional[pulumi.Input[Union[V2FolderNotificationConfigStreamingConfigArgs, V2FolderNotificationConfigStreamingConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2FolderNotificationConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., config_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., streaming_config: Optional[pulumi.Input[Union[V2FolderNotificationConfigStreamingConfigArgs, V2FolderNotificationConfigStreamingConfigArgsDict]]] = ...) -> V2FolderNotificationConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamingConfig")
    def streaming_config(self) -> pulumi.Output[outputs.V2FolderNotificationConfigStreamingConfig]:
        
        ...
    


