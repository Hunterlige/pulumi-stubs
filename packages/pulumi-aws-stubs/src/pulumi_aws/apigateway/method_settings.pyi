

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
__all__ = ['MethodSettingsArgs', 'MethodSettings']
@pulumi.input_type
class MethodSettingsArgs:
    def __init__(__self__, *, method_path: pulumi.Input[_builtins.str], rest_api: pulumi.Input[_builtins.str], settings: pulumi.Input[MethodSettingsSettingsArgs], stage_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="methodPath")
    def method_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @method_path.setter
    def method_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Input[MethodSettingsSettingsArgs]:
        
        ...
    
    @settings.setter
    def settings(self, value: pulumi.Input[MethodSettingsSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MethodSettingsState:
    def __init__(__self__, *, method_path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[MethodSettingsSettingsArgs]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="methodPath")
    def method_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @method_path.setter
    def method_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[MethodSettingsSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[MethodSettingsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/methodSettings:MethodSettings")
class MethodSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., method_path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Union[MethodSettingsSettingsArgs, MethodSettingsSettingsArgsDict]]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MethodSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., method_path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Union[MethodSettingsSettingsArgs, MethodSettingsSettingsArgsDict]]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ...) -> MethodSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="methodPath")
    def method_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[outputs.MethodSettingsSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


