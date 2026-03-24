

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
__all__ = ['FeatureGroupArgs', 'FeatureGroup']
@pulumi.input_type
class FeatureGroupArgs:
    def __init__(__self__, *, event_time_feature_name: pulumi.Input[_builtins.str], feature_definitions: pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]], feature_group_name: pulumi.Input[_builtins.str], record_identifier_feature_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., offline_store_config: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]] = ..., online_store_config: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput_config: Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTimeFeatureName")
    def event_time_feature_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_time_feature_name.setter
    def event_time_feature_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]]:
        
        ...
    
    @feature_definitions.setter
    def feature_definitions(self, value: pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureGroupName")
    def feature_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @feature_group_name.setter
    def feature_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_identifier_feature_name.setter
    def record_identifier_feature_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineStoreConfig")
    def offline_store_config(self) -> Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]]:
        
        ...
    
    @offline_store_config.setter
    def offline_store_config(self, value: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineStoreConfig")
    def online_store_config(self) -> Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]]:
        
        ...
    
    @online_store_config.setter
    def online_store_config(self, value: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputConfig")
    def throughput_config(self) -> Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]]:
        ...
    
    @throughput_config.setter
    def throughput_config(self, value: Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FeatureGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_time_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., feature_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]]] = ..., feature_group_name: Optional[pulumi.Input[_builtins.str]] = ..., offline_store_config: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]] = ..., online_store_config: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]] = ..., record_identifier_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput_config: Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]] = ...) -> None:
        
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTimeFeatureName")
    def event_time_feature_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_time_feature_name.setter
    def event_time_feature_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]]]:
        
        ...
    
    @feature_definitions.setter
    def feature_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FeatureGroupFeatureDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureGroupName")
    def feature_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feature_group_name.setter
    def feature_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineStoreConfig")
    def offline_store_config(self) -> Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]]:
        
        ...
    
    @offline_store_config.setter
    def offline_store_config(self, value: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineStoreConfig")
    def online_store_config(self) -> Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]]:
        
        ...
    
    @online_store_config.setter
    def online_store_config(self, value: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_identifier_feature_name.setter
    def record_identifier_feature_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputConfig")
    def throughput_config(self) -> Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]]:
        ...
    
    @throughput_config.setter
    def throughput_config(self, value: Optional[pulumi.Input[FeatureGroupThroughputConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:sagemaker/featureGroup:FeatureGroup")
class FeatureGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_time_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., feature_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FeatureGroupFeatureDefinitionArgs, FeatureGroupFeatureDefinitionArgsDict]]]]] = ..., feature_group_name: Optional[pulumi.Input[_builtins.str]] = ..., offline_store_config: Optional[pulumi.Input[Union[FeatureGroupOfflineStoreConfigArgs, FeatureGroupOfflineStoreConfigArgsDict]]] = ..., online_store_config: Optional[pulumi.Input[Union[FeatureGroupOnlineStoreConfigArgs, FeatureGroupOnlineStoreConfigArgsDict]]] = ..., record_identifier_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput_config: Optional[pulumi.Input[Union[FeatureGroupThroughputConfigArgs, FeatureGroupThroughputConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FeatureGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_time_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., feature_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FeatureGroupFeatureDefinitionArgs, FeatureGroupFeatureDefinitionArgsDict]]]]] = ..., feature_group_name: Optional[pulumi.Input[_builtins.str]] = ..., offline_store_config: Optional[pulumi.Input[Union[FeatureGroupOfflineStoreConfigArgs, FeatureGroupOfflineStoreConfigArgsDict]]] = ..., online_store_config: Optional[pulumi.Input[Union[FeatureGroupOnlineStoreConfigArgs, FeatureGroupOnlineStoreConfigArgsDict]]] = ..., record_identifier_feature_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput_config: Optional[pulumi.Input[Union[FeatureGroupThroughputConfigArgs, FeatureGroupThroughputConfigArgsDict]]] = ...) -> FeatureGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTimeFeatureName")
    def event_time_feature_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> pulumi.Output[Sequence[outputs.FeatureGroupFeatureDefinition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureGroupName")
    def feature_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineStoreConfig")
    def offline_store_config(self) -> pulumi.Output[Optional[outputs.FeatureGroupOfflineStoreConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineStoreConfig")
    def online_store_config(self) -> pulumi.Output[Optional[outputs.FeatureGroupOnlineStoreConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputConfig")
    def throughput_config(self) -> pulumi.Output[outputs.FeatureGroupThroughputConfig]:
        ...
    


