

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
__all__ = ['CxIntentArgs', 'CxIntent']
@pulumi.input_type
class CxIntentArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., is_default_negative_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_default_welcome_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., training_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultNegativeIntent")
    def is_default_negative_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default_negative_intent.setter
    def is_default_negative_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultWelcomeIntent")
    def is_default_welcome_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default_welcome_intent.setter
    def is_default_welcome_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_fallback.setter
    def is_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trainingPhrases")
    def training_phrases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]]:
        
        ...
    
    @training_phrases.setter
    def training_phrases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CxIntentState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., is_default_negative_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_default_welcome_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., training_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultNegativeIntent")
    def is_default_negative_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default_negative_intent.setter
    def is_default_negative_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultWelcomeIntent")
    def is_default_welcome_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default_welcome_intent.setter
    def is_default_welcome_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_fallback.setter
    def is_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trainingPhrases")
    def training_phrases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]]:
        
        ...
    
    @training_phrases.setter
    def training_phrases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhraseArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxIntent:CxIntent")
class CxIntent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_default_negative_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_default_welcome_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxIntentParameterArgs, CxIntentParameterArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., training_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxIntentTrainingPhraseArgs, CxIntentTrainingPhraseArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxIntentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., is_default_negative_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_default_welcome_intent: Optional[pulumi.Input[_builtins.bool]] = ..., is_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxIntentParameterArgs, CxIntentParameterArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., training_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxIntentTrainingPhraseArgs, CxIntentTrainingPhraseArgsDict]]]]] = ...) -> CxIntent:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultNegativeIntent")
    def is_default_negative_intent(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultWelcomeIntent")
    def is_default_welcome_intent(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[outputs.CxIntentParameter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trainingPhrases")
    def training_phrases(self) -> pulumi.Output[Optional[Sequence[outputs.CxIntentTrainingPhrase]]]:
        
        ...
    


