

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
__all__ = ['WebTypeComputeIamBindingArgs', 'WebTypeComputeIamBinding']
@pulumi.input_type
class WebTypeComputeIamBindingArgs:
    def __init__(__self__, *, members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], role: pulumi.Input[_builtins.str], condition: Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WebTypeComputeIamBindingState:
    def __init__(__self__, *, condition: Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[WebTypeComputeIamBindingConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WebTypeComputeIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[WebTypeComputeIamBindingConditionArgs, WebTypeComputeIamBindingConditionArgsDict]]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebTypeComputeIamBindingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[WebTypeComputeIamBindingConditionArgs, WebTypeComputeIamBindingConditionArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> WebTypeComputeIamBinding:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.WebTypeComputeIamBindingCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


