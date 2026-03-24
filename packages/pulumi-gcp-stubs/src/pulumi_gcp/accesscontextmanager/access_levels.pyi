

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
__all__ = ['AccessLevelsArgs', 'AccessLevels']
@pulumi.input_type
class AccessLevelsArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]]:
        
        ...
    
    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AccessLevelsState:
    def __init__(__self__, *, access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]]:
        
        ...
    
    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelsAccessLevelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:accesscontextmanager/accessLevels:AccessLevels")
class AccessLevels(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessLevelsAccessLevelArgs, AccessLevelsAccessLevelArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessLevelsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessLevelsAccessLevelArgs, AccessLevelsAccessLevelArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> AccessLevels:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> pulumi.Output[Optional[Sequence[outputs.AccessLevelsAccessLevel]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


