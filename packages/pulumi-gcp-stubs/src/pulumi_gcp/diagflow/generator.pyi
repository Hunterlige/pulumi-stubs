

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
__all__ = ['GeneratorArgs', 'Generator']
@pulumi.input_type
class GeneratorArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], summarization_context: pulumi.Input[GeneratorSummarizationContextArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., generator_id: Optional[pulumi.Input[_builtins.str]] = ..., inference_parameter: Optional[pulumi.Input[GeneratorInferenceParameterArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., published_model: Optional[pulumi.Input[_builtins.str]] = ..., trigger_event: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationContext")
    def summarization_context(self) -> pulumi.Input[GeneratorSummarizationContextArgs]:
        
        ...
    
    @summarization_context.setter
    def summarization_context(self, value: pulumi.Input[GeneratorSummarizationContextArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatorId")
    def generator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generator_id.setter
    def generator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceParameter")
    def inference_parameter(self) -> Optional[pulumi.Input[GeneratorInferenceParameterArgs]]:
        
        ...
    
    @inference_parameter.setter
    def inference_parameter(self, value: Optional[pulumi.Input[GeneratorInferenceParameterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishedModel")
    def published_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @published_model.setter
    def published_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerEvent")
    def trigger_event(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trigger_event.setter
    def trigger_event(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GeneratorState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., generator_id: Optional[pulumi.Input[_builtins.str]] = ..., inference_parameter: Optional[pulumi.Input[GeneratorInferenceParameterArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., published_model: Optional[pulumi.Input[_builtins.str]] = ..., summarization_context: Optional[pulumi.Input[GeneratorSummarizationContextArgs]] = ..., trigger_event: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatorId")
    def generator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generator_id.setter
    def generator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceParameter")
    def inference_parameter(self) -> Optional[pulumi.Input[GeneratorInferenceParameterArgs]]:
        
        ...
    
    @inference_parameter.setter
    def inference_parameter(self, value: Optional[pulumi.Input[GeneratorInferenceParameterArgs]]): # -> None:
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
    @pulumi.getter(name="publishedModel")
    def published_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @published_model.setter
    def published_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationContext")
    def summarization_context(self) -> Optional[pulumi.Input[GeneratorSummarizationContextArgs]]:
        
        ...
    
    @summarization_context.setter
    def summarization_context(self, value: Optional[pulumi.Input[GeneratorSummarizationContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerEvent")
    def trigger_event(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trigger_event.setter
    def trigger_event(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/generator:Generator")
class Generator(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., generator_id: Optional[pulumi.Input[_builtins.str]] = ..., inference_parameter: Optional[pulumi.Input[Union[GeneratorInferenceParameterArgs, GeneratorInferenceParameterArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., published_model: Optional[pulumi.Input[_builtins.str]] = ..., summarization_context: Optional[pulumi.Input[Union[GeneratorSummarizationContextArgs, GeneratorSummarizationContextArgsDict]]] = ..., trigger_event: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GeneratorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., generator_id: Optional[pulumi.Input[_builtins.str]] = ..., inference_parameter: Optional[pulumi.Input[Union[GeneratorInferenceParameterArgs, GeneratorInferenceParameterArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., published_model: Optional[pulumi.Input[_builtins.str]] = ..., summarization_context: Optional[pulumi.Input[Union[GeneratorSummarizationContextArgs, GeneratorSummarizationContextArgsDict]]] = ..., trigger_event: Optional[pulumi.Input[_builtins.str]] = ...) -> Generator:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatorId")
    def generator_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceParameter")
    def inference_parameter(self) -> pulumi.Output[Optional[outputs.GeneratorInferenceParameter]]:
        
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
    @pulumi.getter(name="publishedModel")
    def published_model(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationContext")
    def summarization_context(self) -> pulumi.Output[outputs.GeneratorSummarizationContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerEvent")
    def trigger_event(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


