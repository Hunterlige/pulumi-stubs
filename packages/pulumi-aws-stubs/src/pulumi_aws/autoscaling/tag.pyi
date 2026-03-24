

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
__all__ = ['TagArgs', 'Tag']
@pulumi.input_type
class TagArgs:
    def __init__(__self__, *, autoscaling_group_name: pulumi.Input[_builtins.str], tag: pulumi.Input[TagTagArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> pulumi.Input[TagTagArgs]:
        
        ...
    
    @tag.setter
    def tag(self, value: pulumi.Input[TagTagArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TagState:
    def __init__(__self__, *, autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[TagTagArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tag(self) -> Optional[pulumi.Input[TagTagArgs]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[TagTagArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscaling/tag:Tag")
class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[Union[TagTagArgs, TagTagArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TagArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[Union[TagTagArgs, TagTagArgsDict]]] = ...) -> Tag:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> pulumi.Output[outputs.TagTag]:
        
        ...
    


