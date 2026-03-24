

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
__all__ = ['RegionPerInstanceConfigArgs', 'RegionPerInstanceConfig']
@pulumi.input_type
class RegionPerInstanceConfigArgs:
    def __init__(__self__, *, region_instance_group_manager: pulumi.Input[_builtins.str], minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_instance_group_manager.setter
    def region_instance_group_manager(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimal_action.setter
    def minimal_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]]:
        
        ...
    
    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceOnDestroy")
    def remove_instance_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_instance_on_destroy.setter
    def remove_instance_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_instance_state_on_destroy.setter
    def remove_instance_state_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionPerInstanceConfigState:
    def __init__(__self__, *, minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimal_action.setter
    def minimal_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]]:
        
        ...
    
    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input[RegionPerInstanceConfigPreservedStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_instance_group_manager.setter
    def region_instance_group_manager(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceOnDestroy")
    def remove_instance_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_instance_on_destroy.setter
    def remove_instance_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_instance_state_on_destroy.setter
    def remove_instance_state_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionPerInstanceConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[Union[RegionPerInstanceConfigPreservedStateArgs, RegionPerInstanceConfigPreservedStateArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionPerInstanceConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[Union[RegionPerInstanceConfigPreservedStateArgs, RegionPerInstanceConfigPreservedStateArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> RegionPerInstanceConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> pulumi.Output[Optional[outputs.RegionPerInstanceConfigPreservedState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceOnDestroy")
    def remove_instance_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


