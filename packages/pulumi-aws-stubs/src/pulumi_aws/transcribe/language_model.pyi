

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LanguageModelArgs', 'LanguageModel']
@pulumi.input_type
class LanguageModelArgs:
    def __init__(__self__, *, base_model_name: pulumi.Input[_builtins.str], input_data_config: pulumi.Input[LanguageModelInputDataConfigArgs], language_code: pulumi.Input[_builtins.str], model_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseModelName")
    def base_model_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @base_model_name.setter
    def base_model_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Input[LanguageModelInputDataConfigArgs]:
        
        ...
    
    @input_data_config.setter
    def input_data_config(self, value: pulumi.Input[LanguageModelInputDataConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @model_name.setter
    def model_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


@pulumi.input_type
class _LanguageModelState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., base_model_name: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[LanguageModelInputDataConfigArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., model_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseModelName")
    def base_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_model_name.setter
    def base_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> Optional[pulumi.Input[LanguageModelInputDataConfigArgs]]:
        
        ...
    
    @input_data_config.setter
    def input_data_config(self, value: Optional[pulumi.Input[LanguageModelInputDataConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:transcribe/languageModel:LanguageModel")
class LanguageModel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., base_model_name: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[Union[LanguageModelInputDataConfigArgs, LanguageModelInputDataConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., model_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LanguageModelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., base_model_name: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[Union[LanguageModelInputDataConfigArgs, LanguageModelInputDataConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., model_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> LanguageModel:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseModelName")
    def base_model_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Output[outputs.LanguageModelInputDataConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    


