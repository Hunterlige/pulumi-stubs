

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
__all__ = ['SizeConstraintSetArgs', 'SizeConstraintSet']
@pulumi.input_type
class SizeConstraintSetArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]] = ...) -> None:
        
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
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]]:
        
        ...
    
    @size_constraints.setter
    def size_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _SizeConstraintSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]]:
        
        ...
    
    @size_constraints.setter
    def size_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SizeConstraintSetSizeConstraintArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SizeConstraintSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SizeConstraintSetSizeConstraintArgs, SizeConstraintSetSizeConstraintArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[SizeConstraintSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., size_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SizeConstraintSetSizeConstraintArgs, SizeConstraintSetSizeConstraintArgsDict]]]]] = ...) -> SizeConstraintSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
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
    @pulumi.getter(name="sizeConstraints")
    def size_constraints(self) -> pulumi.Output[Optional[Sequence[outputs.SizeConstraintSetSizeConstraint]]]:
        
        ...
    


