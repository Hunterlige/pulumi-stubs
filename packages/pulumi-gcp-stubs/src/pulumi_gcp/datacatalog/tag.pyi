

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
__all__ = ['TagArgs', 'Tag']
@pulumi.input_type
class TagArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]], template: pulumi.Input[_builtins.str], column: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @template.setter
    def template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TagState:
    def __init__(__self__, *, column: Optional[pulumi.Input[_builtins.str]] = ..., fields: Optional[pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., template: Optional[pulumi.Input[_builtins.str]] = ..., template_displayname: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TagFieldArgs]]]]): # -> None:
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
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template.setter
    def template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateDisplayname")
    def template_displayname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_displayname.setter
    def template_displayname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:datacatalog/tag:Tag")
class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., column: Optional[pulumi.Input[_builtins.str]] = ..., fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TagFieldArgs, TagFieldArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., template: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TagArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., column: Optional[pulumi.Input[_builtins.str]] = ..., fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TagFieldArgs, TagFieldArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., template: Optional[pulumi.Input[_builtins.str]] = ..., template_displayname: Optional[pulumi.Input[_builtins.str]] = ...) -> Tag:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[outputs.TagField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateDisplayname")
    def template_displayname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


