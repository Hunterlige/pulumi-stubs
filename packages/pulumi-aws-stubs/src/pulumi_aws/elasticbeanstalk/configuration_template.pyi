

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
__all__ = ['ConfigurationTemplateArgs', 'ConfigurationTemplate']
@pulumi.input_type
class ConfigurationTemplateArgs:
    def __init__(__self__, *, application: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]] = ..., solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def application(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application.setter
    def application(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ConfigurationTemplateState:
    def __init__(__self__, *, application: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]] = ..., solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application.setter
    def application(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationTemplateSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @solution_stack_name.setter
    def solution_stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConfigurationTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConfigurationTemplateSettingArgs, ConfigurationTemplateSettingArgsDict]]]]] = ..., solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConfigurationTemplateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConfigurationTemplateSettingArgs, ConfigurationTemplateSettingArgsDict]]]]] = ..., solution_stack_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ConfigurationTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def application(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def settings(self) -> pulumi.Output[Sequence[outputs.ConfigurationTemplateSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="solutionStackName")
    def solution_stack_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


