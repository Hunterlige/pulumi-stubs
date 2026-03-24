

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IndexTimeoutsArgs', 'IndexTimeoutsArgsDict', 'ViewFiltersArgs', 'ViewFiltersArgsDict', 'ViewIncludedPropertyArgs', 'ViewIncludedPropertyArgsDict']
class IndexTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IndexTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ViewFiltersArgsDict(TypedDict):
    filter_string: pulumi.Input[_builtins.str]


@pulumi.input_type
class ViewFiltersArgs:
    def __init__(__self__, *, filter_string: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterString")
    def filter_string(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter_string.setter
    def filter_string(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ViewIncludedPropertyArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ViewIncludedPropertyArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


