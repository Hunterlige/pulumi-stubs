

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ViewArgs', 'View']
@pulumi.input_type
class ViewArgs:
    def __init__(__self__, *, default_view: Optional[pulumi.Input[_builtins.bool]] = ..., filters: Optional[pulumi.Input[ViewFiltersArgs]] = ..., included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultView")
    def default_view(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @default_view.setter
    def default_view(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[ViewFiltersArgs]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[ViewFiltersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]]:
        
        ...
    
    @included_properties.setter
    def included_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]]): # -> None:
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
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ViewState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., default_view: Optional[pulumi.Input[_builtins.bool]] = ..., filters: Optional[pulumi.Input[ViewFiltersArgs]] = ..., included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultView")
    def default_view(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @default_view.setter
    def default_view(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[ViewFiltersArgs]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[ViewFiltersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]]:
        
        ...
    
    @included_properties.setter
    def included_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ViewIncludedPropertyArgs]]]]): # -> None:
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
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:resourceexplorer/view:View")
class View(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_view: Optional[pulumi.Input[_builtins.bool]] = ..., filters: Optional[pulumi.Input[Union[ViewFiltersArgs, ViewFiltersArgsDict]]] = ..., included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ViewIncludedPropertyArgs, ViewIncludedPropertyArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ViewArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., default_view: Optional[pulumi.Input[_builtins.bool]] = ..., filters: Optional[pulumi.Input[Union[ViewFiltersArgs, ViewFiltersArgsDict]]] = ..., included_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ViewIncludedPropertyArgs, ViewIncludedPropertyArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> View:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultView")
    def default_view(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[outputs.ViewFilters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> pulumi.Output[Optional[Sequence[outputs.ViewIncludedProperty]]]:
        
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
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


