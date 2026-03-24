

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
__all__ = ['V2modelsBotLocaleArgs', 'V2modelsBotLocale']
@pulumi.input_type
class V2modelsBotLocaleArgs:
    def __init__(__self__, *, bot_id: pulumi.Input[_builtins.str], bot_version: pulumi.Input[_builtins.str], locale_id: pulumi.Input[_builtins.str], n_lu_intent_confidence_threshold: pulumi.Input[_builtins.float], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]] = ..., voice_settings: Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_id.setter
    def bot_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @locale_id.setter
    def locale_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nLuIntentConfidenceThreshold")
    def n_lu_intent_confidence_threshold(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @n_lu_intent_confidence_threshold.setter
    def n_lu_intent_confidence_threshold(self, value: pulumi.Input[_builtins.float]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceSettings")
    def voice_settings(self) -> Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]]:
        
        ...
    
    @voice_settings.setter
    def voice_settings(self, value: Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _V2modelsBotLocaleState:
    def __init__(__self__, *, bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., n_lu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]] = ..., voice_settings: Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_id.setter
    def bot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale_id.setter
    def locale_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nLuIntentConfidenceThreshold")
    def n_lu_intent_confidence_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @n_lu_intent_confidence_threshold.setter
    def n_lu_intent_confidence_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsBotLocaleTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceSettings")
    def voice_settings(self) -> Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]]:
        
        ...
    
    @voice_settings.setter
    def voice_settings(self, value: Optional[pulumi.Input[V2modelsBotLocaleVoiceSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lex/v2modelsBotLocale:V2modelsBotLocale")
class V2modelsBotLocale(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., n_lu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsBotLocaleTimeoutsArgs, V2modelsBotLocaleTimeoutsArgsDict]]] = ..., voice_settings: Optional[pulumi.Input[Union[V2modelsBotLocaleVoiceSettingsArgs, V2modelsBotLocaleVoiceSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2modelsBotLocaleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., n_lu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsBotLocaleTimeoutsArgs, V2modelsBotLocaleTimeoutsArgsDict]]] = ..., voice_settings: Optional[pulumi.Input[Union[V2modelsBotLocaleVoiceSettingsArgs, V2modelsBotLocaleVoiceSettingsArgsDict]]] = ...) -> V2modelsBotLocale:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nLuIntentConfidenceThreshold")
    def n_lu_intent_confidence_threshold(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.V2modelsBotLocaleTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceSettings")
    def voice_settings(self) -> pulumi.Output[Optional[outputs.V2modelsBotLocaleVoiceSettings]]:
        
        ...
    


