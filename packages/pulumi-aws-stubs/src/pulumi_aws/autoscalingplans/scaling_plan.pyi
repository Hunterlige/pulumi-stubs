

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
__all__ = ['ScalingPlanArgs', 'ScalingPlan']
@pulumi.input_type
class ScalingPlanArgs:
    def __init__(__self__, *, application_source: pulumi.Input[ScalingPlanApplicationSourceArgs], scaling_instructions: pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSource")
    def application_source(self) -> pulumi.Input[ScalingPlanApplicationSourceArgs]:
        
        ...
    
    @application_source.setter
    def application_source(self, value: pulumi.Input[ScalingPlanApplicationSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingInstructions")
    def scaling_instructions(self) -> pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]]:
        
        ...
    
    @scaling_instructions.setter
    def scaling_instructions(self, value: pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]]): # -> None:
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
    


@pulumi.input_type
class _ScalingPlanState:
    def __init__(__self__, *, application_source: Optional[pulumi.Input[ScalingPlanApplicationSourceArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_instructions: Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]]] = ..., scaling_plan_version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSource")
    def application_source(self) -> Optional[pulumi.Input[ScalingPlanApplicationSourceArgs]]:
        
        ...
    
    @application_source.setter
    def application_source(self, value: Optional[pulumi.Input[ScalingPlanApplicationSourceArgs]]): # -> None:
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
    @pulumi.getter(name="scalingInstructions")
    def scaling_instructions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]]]:
        
        ...
    
    @scaling_instructions.setter
    def scaling_instructions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPlanScalingInstructionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanVersion")
    def scaling_plan_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scaling_plan_version.setter
    def scaling_plan_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscalingplans/scalingPlan:ScalingPlan")
class ScalingPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_source: Optional[pulumi.Input[Union[ScalingPlanApplicationSourceArgs, ScalingPlanApplicationSourceArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_instructions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScalingPlanScalingInstructionArgs, ScalingPlanScalingInstructionArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScalingPlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_source: Optional[pulumi.Input[Union[ScalingPlanApplicationSourceArgs, ScalingPlanApplicationSourceArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_instructions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScalingPlanScalingInstructionArgs, ScalingPlanScalingInstructionArgsDict]]]]] = ..., scaling_plan_version: Optional[pulumi.Input[_builtins.int]] = ...) -> ScalingPlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSource")
    def application_source(self) -> pulumi.Output[outputs.ScalingPlanApplicationSource]:
        
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
    @pulumi.getter(name="scalingInstructions")
    def scaling_instructions(self) -> pulumi.Output[Sequence[outputs.ScalingPlanScalingInstruction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanVersion")
    def scaling_plan_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


