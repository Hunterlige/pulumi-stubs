

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ChatEngineArgs', 'ChatEngine']
@pulumi.input_type
class ChatEngineArgs:
    def __init__(__self__, *, chat_engine_config: pulumi.Input[ChatEngineChatEngineConfigArgs], collection_id: pulumi.Input[_builtins.str], data_store_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], display_name: pulumi.Input[_builtins.str], engine_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], common_config: Optional[pulumi.Input[ChatEngineCommonConfigArgs]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatEngineConfig")
    def chat_engine_config(self) -> pulumi.Input[ChatEngineChatEngineConfigArgs]:
        
        ...
    
    @chat_engine_config.setter
    def chat_engine_config(self, value: pulumi.Input[ChatEngineChatEngineConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreIds")
    def data_store_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @data_store_ids.setter
    def data_store_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @engine_id.setter
    def engine_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> Optional[pulumi.Input[ChatEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[ChatEngineCommonConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ChatEngineState:
    def __init__(__self__, *, chat_engine_config: Optional[pulumi.Input[ChatEngineChatEngineConfigArgs]] = ..., chat_engine_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[ChatEngineChatEngineMetadataArgs]]]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[ChatEngineCommonConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatEngineConfig")
    def chat_engine_config(self) -> Optional[pulumi.Input[ChatEngineChatEngineConfigArgs]]:
        
        ...
    
    @chat_engine_config.setter
    def chat_engine_config(self, value: Optional[pulumi.Input[ChatEngineChatEngineConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatEngineMetadatas")
    def chat_engine_metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChatEngineChatEngineMetadataArgs]]]]:
        
        ...
    
    @chat_engine_metadatas.setter
    def chat_engine_metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ChatEngineChatEngineMetadataArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> Optional[pulumi.Input[ChatEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[ChatEngineCommonConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreIds")
    def data_store_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_store_ids.setter
    def data_store_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_id.setter
    def engine_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/chatEngine:ChatEngine")
class ChatEngine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., chat_engine_config: Optional[pulumi.Input[Union[ChatEngineChatEngineConfigArgs, ChatEngineChatEngineConfigArgsDict]]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[Union[ChatEngineCommonConfigArgs, ChatEngineCommonConfigArgsDict]]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChatEngineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., chat_engine_config: Optional[pulumi.Input[Union[ChatEngineChatEngineConfigArgs, ChatEngineChatEngineConfigArgsDict]]] = ..., chat_engine_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ChatEngineChatEngineMetadataArgs, ChatEngineChatEngineMetadataArgsDict]]]]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[Union[ChatEngineCommonConfigArgs, ChatEngineCommonConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> ChatEngine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatEngineConfig")
    def chat_engine_config(self) -> pulumi.Output[outputs.ChatEngineChatEngineConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chatEngineMetadatas")
    def chat_engine_metadatas(self) -> pulumi.Output[Sequence[outputs.ChatEngineChatEngineMetadata]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> pulumi.Output[Optional[outputs.ChatEngineCommonConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreIds")
    def data_store_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


