

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
__all__ = ['LfTagExpressionArgs', 'LfTagExpression']
@pulumi.input_type
class LfTagExpressionArgs:
    def __init__(__self__, *, expressions: pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]], catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]]:
        
        ...
    
    @expressions.setter
    def expressions(self, value: pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _LfTagExpressionState:
    def __init__(__self__, *, catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., expressions: Optional[pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]]]:
        
        ...
    
    @expressions.setter
    def expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LfTagExpressionExpressionArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:lakeformation/lfTagExpression:LfTagExpression")
class LfTagExpression(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., expressions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LfTagExpressionExpressionArgs, LfTagExpressionExpressionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LfTagExpressionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., expressions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LfTagExpressionExpressionArgs, LfTagExpressionExpressionArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> LfTagExpression:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> pulumi.Output[Sequence[outputs.LfTagExpressionExpression]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


