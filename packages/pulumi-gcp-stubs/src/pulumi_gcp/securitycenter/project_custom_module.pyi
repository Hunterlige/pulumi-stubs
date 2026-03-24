

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
__all__ = ['ProjectCustomModuleArgs', 'ProjectCustomModule']
@pulumi.input_type
class ProjectCustomModuleArgs:
    def __init__(__self__, *, custom_config: pulumi.Input[ProjectCustomModuleCustomConfigArgs], display_name: pulumi.Input[_builtins.str], enablement_state: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> pulumi.Input[ProjectCustomModuleCustomConfigArgs]:
        
        ...
    
    @custom_config.setter
    def custom_config(self, value: pulumi.Input[ProjectCustomModuleCustomConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @enablement_state.setter
    def enablement_state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ProjectCustomModuleState:
    def __init__(__self__, *, ancestor_module: Optional[pulumi.Input[_builtins.str]] = ..., custom_config: Optional[pulumi.Input[ProjectCustomModuleCustomConfigArgs]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enablement_state: Optional[pulumi.Input[_builtins.str]] = ..., last_editor: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ancestorModule")
    def ancestor_module(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ancestor_module.setter
    def ancestor_module(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> Optional[pulumi.Input[ProjectCustomModuleCustomConfigArgs]]:
        
        ...
    
    @custom_config.setter
    def custom_config(self, value: Optional[pulumi.Input[ProjectCustomModuleCustomConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enablement_state.setter
    def enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_editor.setter
    def last_editor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class ProjectCustomModule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_config: Optional[pulumi.Input[Union[ProjectCustomModuleCustomConfigArgs, ProjectCustomModuleCustomConfigArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enablement_state: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProjectCustomModuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., ancestor_module: Optional[pulumi.Input[_builtins.str]] = ..., custom_config: Optional[pulumi.Input[Union[ProjectCustomModuleCustomConfigArgs, ProjectCustomModuleCustomConfigArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enablement_state: Optional[pulumi.Input[_builtins.str]] = ..., last_editor: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> ProjectCustomModule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ancestorModule")
    def ancestor_module(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConfig")
    def custom_config(self) -> pulumi.Output[outputs.ProjectCustomModuleCustomConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> pulumi.Output[_builtins.str]:
        
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
    


