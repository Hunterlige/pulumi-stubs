

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TagBindingArgs', 'TagBinding']
@pulumi.input_type
class TagBindingArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], tag_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tag_value.setter
    def tag_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _TagBindingState:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tag_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_value.setter
    def tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:tags/tagBinding:TagBinding")
class TagBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tag_value: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TagBindingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tag_value: Optional[pulumi.Input[_builtins.str]] = ...) -> TagBinding:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


