

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
__all__ = ['AnalysisRuleArgs', 'AnalysisRule']
@pulumi.input_type
class AnalysisRuleArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], active: Optional[pulumi.Input[_builtins.bool]] = ..., analysis_percentage: Optional[pulumi.Input[_builtins.float]] = ..., annotator_selector: Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]] = ..., conversation_filter: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @active.setter
    def active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisPercentage")
    def analysis_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @analysis_percentage.setter
    def analysis_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotatorSelector")
    def annotator_selector(self) -> Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]]:
        
        ...
    
    @annotator_selector.setter
    def annotator_selector(self, value: Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationFilter")
    def conversation_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @conversation_filter.setter
    def conversation_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AnalysisRuleState:
    def __init__(__self__, *, active: Optional[pulumi.Input[_builtins.bool]] = ..., analysis_percentage: Optional[pulumi.Input[_builtins.float]] = ..., annotator_selector: Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]] = ..., conversation_filter: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @active.setter
    def active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisPercentage")
    def analysis_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @analysis_percentage.setter
    def analysis_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotatorSelector")
    def annotator_selector(self) -> Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]]:
        
        ...
    
    @annotator_selector.setter
    def annotator_selector(self, value: Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationFilter")
    def conversation_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @conversation_filter.setter
    def conversation_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token(...)
class AnalysisRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., active: Optional[pulumi.Input[_builtins.bool]] = ..., analysis_percentage: Optional[pulumi.Input[_builtins.float]] = ..., annotator_selector: Optional[pulumi.Input[Union[AnalysisRuleAnnotatorSelectorArgs, AnalysisRuleAnnotatorSelectorArgsDict]]] = ..., conversation_filter: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AnalysisRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., active: Optional[pulumi.Input[_builtins.bool]] = ..., analysis_percentage: Optional[pulumi.Input[_builtins.float]] = ..., annotator_selector: Optional[pulumi.Input[Union[AnalysisRuleAnnotatorSelectorArgs, AnalysisRuleAnnotatorSelectorArgsDict]]] = ..., conversation_filter: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> AnalysisRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisPercentage")
    def analysis_percentage(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotatorSelector")
    def annotator_selector(self) -> pulumi.Output[Optional[outputs.AnalysisRuleAnnotatorSelector]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationFilter")
    def conversation_filter(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    


