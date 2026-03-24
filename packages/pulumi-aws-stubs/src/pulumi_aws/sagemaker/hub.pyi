

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
__all__ = ['HubArgs', 'Hub']
@pulumi.input_type
class HubArgs:
    def __init__(__self__, *, hub_description: pulumi.Input[_builtins.str], hub_name: pulumi.Input[_builtins.str], hub_display_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_search_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_storage_config: Optional[pulumi.Input[HubS3StorageConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDescription")
    def hub_description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hub_description.setter
    def hub_description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDisplayName")
    def hub_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hub_display_name.setter
    def hub_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubSearchKeywords")
    def hub_search_keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hub_search_keywords.setter
    def hub_search_keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3StorageConfig")
    def s3_storage_config(self) -> Optional[pulumi.Input[HubS3StorageConfigArgs]]:
        
        ...
    
    @s3_storage_config.setter
    def s3_storage_config(self, value: Optional[pulumi.Input[HubS3StorageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _HubState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., hub_description: Optional[pulumi.Input[_builtins.str]] = ..., hub_display_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_search_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_storage_config: Optional[pulumi.Input[HubS3StorageConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDescription")
    def hub_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hub_description.setter
    def hub_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDisplayName")
    def hub_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hub_display_name.setter
    def hub_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hub_name.setter
    def hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubSearchKeywords")
    def hub_search_keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hub_search_keywords.setter
    def hub_search_keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3StorageConfig")
    def s3_storage_config(self) -> Optional[pulumi.Input[HubS3StorageConfigArgs]]:
        
        ...
    
    @s3_storage_config.setter
    def s3_storage_config(self, value: Optional[pulumi.Input[HubS3StorageConfigArgs]]): # -> None:
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
    


@pulumi.type_token("aws:sagemaker/hub:Hub")
class Hub(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., hub_description: Optional[pulumi.Input[_builtins.str]] = ..., hub_display_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_search_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_storage_config: Optional[pulumi.Input[Union[HubS3StorageConfigArgs, HubS3StorageConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HubArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., hub_description: Optional[pulumi.Input[_builtins.str]] = ..., hub_display_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_search_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_storage_config: Optional[pulumi.Input[Union[HubS3StorageConfigArgs, HubS3StorageConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Hub:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDescription")
    def hub_description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubDisplayName")
    def hub_display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubSearchKeywords")
    def hub_search_keywords(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3StorageConfig")
    def s3_storage_config(self) -> pulumi.Output[Optional[outputs.HubS3StorageConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


