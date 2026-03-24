

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
__all__ = ['RecommendationEngineArgs', 'RecommendationEngine']
@pulumi.input_type
class RecommendationEngineArgs:
    def __init__(__self__, *, data_store_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], display_name: pulumi.Input[_builtins.str], engine_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], common_config: Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., media_recommendation_engine_config: Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def common_config(self) -> Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="industryVertical")
    def industry_vertical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @industry_vertical.setter
    def industry_vertical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaRecommendationEngineConfig")
    def media_recommendation_engine_config(self) -> Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]]:
        
        ...
    
    @media_recommendation_engine_config.setter
    def media_recommendation_engine_config(self, value: Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RecommendationEngineState:
    def __init__(__self__, *, common_config: Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., media_recommendation_engine_config: Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]]:
        
        ...
    
    @common_config.setter
    def common_config(self, value: Optional[pulumi.Input[RecommendationEngineCommonConfigArgs]]): # -> None:
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
    @pulumi.getter(name="mediaRecommendationEngineConfig")
    def media_recommendation_engine_config(self) -> Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]]:
        
        ...
    
    @media_recommendation_engine_config.setter
    def media_recommendation_engine_config(self, value: Optional[pulumi.Input[RecommendationEngineMediaRecommendationEngineConfigArgs]]): # -> None:
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
    


@pulumi.type_token(...)
class RecommendationEngine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., common_config: Optional[pulumi.Input[Union[RecommendationEngineCommonConfigArgs, RecommendationEngineCommonConfigArgsDict]]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., media_recommendation_engine_config: Optional[pulumi.Input[Union[RecommendationEngineMediaRecommendationEngineConfigArgs, RecommendationEngineMediaRecommendationEngineConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RecommendationEngineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., common_config: Optional[pulumi.Input[Union[RecommendationEngineCommonConfigArgs, RecommendationEngineCommonConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., industry_vertical: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., media_recommendation_engine_config: Optional[pulumi.Input[Union[RecommendationEngineMediaRecommendationEngineConfigArgs, RecommendationEngineMediaRecommendationEngineConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> RecommendationEngine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonConfig")
    def common_config(self) -> pulumi.Output[Optional[outputs.RecommendationEngineCommonConfig]]:
        
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
    @pulumi.getter(name="mediaRecommendationEngineConfig")
    def media_recommendation_engine_config(self) -> pulumi.Output[Optional[outputs.RecommendationEngineMediaRecommendationEngineConfig]]:
        
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
    


