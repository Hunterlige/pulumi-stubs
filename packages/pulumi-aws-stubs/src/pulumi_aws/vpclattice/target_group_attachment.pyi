

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
__all__ = ['TargetGroupAttachmentArgs', 'TargetGroupAttachment']
@pulumi.input_type
class TargetGroupAttachmentArgs:
    def __init__(__self__, *, target: pulumi.Input[TargetGroupAttachmentTargetArgs], target_group_identifier: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[TargetGroupAttachmentTargetArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[TargetGroupAttachmentTargetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_group_identifier.setter
    def target_group_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TargetGroupAttachmentState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[TargetGroupAttachmentTargetArgs]] = ..., target_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def target(self) -> Optional[pulumi.Input[TargetGroupAttachmentTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[TargetGroupAttachmentTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_group_identifier.setter
    def target_group_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TargetGroupAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[TargetGroupAttachmentTargetArgs, TargetGroupAttachmentTargetArgsDict]]] = ..., target_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TargetGroupAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[TargetGroupAttachmentTargetArgs, TargetGroupAttachmentTargetArgsDict]]] = ..., target_group_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> TargetGroupAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[outputs.TargetGroupAttachmentTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


