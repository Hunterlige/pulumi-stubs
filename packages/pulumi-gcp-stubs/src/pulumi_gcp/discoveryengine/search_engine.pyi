

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
__all__ = ['SearchEngineArgs', 'SearchEngine']
@pulumi.input_type
class SearchEngineArgs:
    def __init__(__self__, *, collection_id: pulumi.Input[_builtins.str], data_store_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], display_name: pulumi.Input[_builtins.str], engine_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], search_engine_config: pulumi.Input[SearchEngineSearchEngineConfigArgs], app_type: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[SearchEngineCommonConfigArgs]] = ..., disable_analytics: Optional[pulumi.Input[_builtins.bool]] = ..., features: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_graph_config: Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="searchEngineConfig")
    def search_engine_config(self) -> pulumi.Input[SearchEngineSearchEngineConfigArgs]:
        
        ...
    
    @search_engine_config.setter
    def search_engine_config(self, value: pulumi.Input[SearchEngineSearchEngineConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_type.setter
    def app_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> Optional[pulumi.Input[SearchEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[SearchEngineCommonConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAnalytics")
    def disable_analytics(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_analytics.setter
    def disable_analytics(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @features.setter
    def features(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeGraphConfig")
    def knowledge_graph_config(self) -> Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]]:
        
        ...
    
    @knowledge_graph_config.setter
    def knowledge_graph_config(self, value: Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SearchEngineState:
    def __init__(__self__, *, app_type: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[SearchEngineCommonConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., disable_analytics: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., features: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_graph_config: Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., search_engine_config: Optional[pulumi.Input[SearchEngineSearchEngineConfigArgs]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_type.setter
    def app_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def common_config(self) -> Optional[pulumi.Input[SearchEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[SearchEngineCommonConfigArgs]]): # -> None:
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
    @pulumi.getter(name="disableAnalytics")
    def disable_analytics(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_analytics.setter
    def disable_analytics(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @features.setter
    def features(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeGraphConfig")
    def knowledge_graph_config(self) -> Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]]:
        
        ...
    
    @knowledge_graph_config.setter
    def knowledge_graph_config(self, value: Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigArgs]]): # -> None:
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
    @pulumi.getter(name="searchEngineConfig")
    def search_engine_config(self) -> Optional[pulumi.Input[SearchEngineSearchEngineConfigArgs]]:
        
        ...
    
    @search_engine_config.setter
    def search_engine_config(self, value: Optional[pulumi.Input[SearchEngineSearchEngineConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/searchEngine:SearchEngine")
class SearchEngine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_type: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[Union[SearchEngineCommonConfigArgs, SearchEngineCommonConfigArgsDict]]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., disable_analytics: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., features: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_graph_config: Optional[pulumi.Input[Union[SearchEngineKnowledgeGraphConfigArgs, SearchEngineKnowledgeGraphConfigArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., search_engine_config: Optional[pulumi.Input[Union[SearchEngineSearchEngineConfigArgs, SearchEngineSearchEngineConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SearchEngineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_type: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., common_config: Optional[pulumi.Input[Union[SearchEngineCommonConfigArgs, SearchEngineCommonConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., disable_analytics: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., features: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_graph_config: Optional[pulumi.Input[Union[SearchEngineKnowledgeGraphConfigArgs, SearchEngineKnowledgeGraphConfigArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., search_engine_config: Optional[pulumi.Input[Union[SearchEngineSearchEngineConfigArgs, SearchEngineSearchEngineConfigArgsDict]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> SearchEngine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> pulumi.Output[Optional[outputs.SearchEngineCommonConfig]]:
        
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
    @pulumi.getter(name="disableAnalytics")
    def disable_analytics(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter
    def features(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeGraphConfig")
    def knowledge_graph_config(self) -> pulumi.Output[outputs.SearchEngineKnowledgeGraphConfig]:
        
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
    @pulumi.getter(name="searchEngineConfig")
    def search_engine_config(self) -> pulumi.Output[outputs.SearchEngineSearchEngineConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


