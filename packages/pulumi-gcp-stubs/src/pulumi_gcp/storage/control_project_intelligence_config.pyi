

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
__all__ = ['ControlProjectIntelligenceConfigArgs', 'ControlProjectIntelligenceConfig']
@pulumi.input_type
class ControlProjectIntelligenceConfigArgs:
    def __init__(__self__, *, edition_config: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="editionConfig")
    def edition_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition_config.setter
    def edition_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ControlProjectIntelligenceConfigState:
    def __init__(__self__, *, edition_config: Optional[pulumi.Input[_builtins.str]] = ..., effective_intelligence_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgs]]]] = ..., filter: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., trial_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigTrialConfigArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="editionConfig")
    def edition_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition_config.setter
    def edition_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveIntelligenceConfigs")
    def effective_intelligence_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgs]]]]:
        
        ...
    
    @effective_intelligence_configs.setter
    def effective_intelligence_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trialConfigs")
    def trial_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigTrialConfigArgs]]]]:
        
        ...
    
    @trial_configs.setter
    def trial_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ControlProjectIntelligenceConfigTrialConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ControlProjectIntelligenceConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., edition_config: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Union[ControlProjectIntelligenceConfigFilterArgs, ControlProjectIntelligenceConfigFilterArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ControlProjectIntelligenceConfigArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., edition_config: Optional[pulumi.Input[_builtins.str]] = ..., effective_intelligence_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgs, ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgsDict]]]]] = ..., filter: Optional[pulumi.Input[Union[ControlProjectIntelligenceConfigFilterArgs, ControlProjectIntelligenceConfigFilterArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., trial_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ControlProjectIntelligenceConfigTrialConfigArgs, ControlProjectIntelligenceConfigTrialConfigArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> ControlProjectIntelligenceConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="editionConfig")
    def edition_config(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveIntelligenceConfigs")
    def effective_intelligence_configs(self) -> pulumi.Output[Sequence[outputs.ControlProjectIntelligenceConfigEffectiveIntelligenceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[outputs.ControlProjectIntelligenceConfigFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trialConfigs")
    def trial_configs(self) -> pulumi.Output[Sequence[outputs.ControlProjectIntelligenceConfigTrialConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


