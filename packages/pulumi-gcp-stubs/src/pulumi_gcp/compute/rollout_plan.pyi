

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
__all__ = ['RolloutPlanArgs', 'RolloutPlan']
@pulumi.input_type
class RolloutPlanArgs:
    def __init__(__self__, *, waves: pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]], description: Optional[pulumi.Input[_builtins.str]] = ..., location_scope: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def waves(self) -> pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]]:
        
        ...
    
    @waves.setter
    def waves(self, value: pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationScope")
    def location_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_scope.setter
    def location_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _RolloutPlanState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., location_scope: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., waves: Optional[pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationScope")
    def location_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_scope.setter
    def location_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def waves(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]]]:
        
        ...
    
    @waves.setter
    def waves(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RolloutPlanWaveArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/rolloutPlan:RolloutPlan")
class RolloutPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location_scope: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., waves: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RolloutPlanWaveArgs, RolloutPlanWaveArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RolloutPlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., location_scope: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., waves: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RolloutPlanWaveArgs, RolloutPlanWaveArgsDict]]]]] = ...) -> RolloutPlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationScope")
    def location_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def waves(self) -> pulumi.Output[Sequence[outputs.RolloutPlanWave]]:
        
        ...
    


