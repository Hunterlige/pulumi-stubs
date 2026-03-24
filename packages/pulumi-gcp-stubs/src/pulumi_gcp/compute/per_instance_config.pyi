

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
__all__ = ['PerInstanceConfigArgs', 'PerInstanceConfig']
@pulumi.input_type
class PerInstanceConfigArgs:
    def __init__(__self__, *, instance_group_manager: pulumi.Input[_builtins.str], minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_group_manager.setter
    def instance_group_manager(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def preserved_state(self) -> Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]]:
        
        ...
    
    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PerInstanceConfigState:
    def __init__(__self__, *, instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_group_manager.setter
    def instance_group_manager(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def preserved_state(self) -> Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]]:
        
        ...
    
    @preserved_state.setter
    def preserved_state(self, value: Optional[pulumi.Input[PerInstanceConfigPreservedStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/perInstanceConfig:PerInstanceConfig")
class PerInstanceConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[Union[PerInstanceConfigPreservedStateArgs, PerInstanceConfigPreservedStateArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PerInstanceConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_group_manager: Optional[pulumi.Input[_builtins.str]] = ..., minimal_action: Optional[pulumi.Input[_builtins.str]] = ..., most_disruptive_allowed_action: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preserved_state: Optional[pulumi.Input[Union[PerInstanceConfigPreservedStateArgs, PerInstanceConfigPreservedStateArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remove_instance_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., remove_instance_state_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> PerInstanceConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> pulumi.Output[_builtins.str]:
        
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
    def preserved_state(self) -> pulumi.Output[Optional[outputs.PerInstanceConfigPreservedState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceOnDestroy")
    def remove_instance_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


