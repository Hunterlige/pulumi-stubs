

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
__all__ = ['SettingsArgs', 'Settings']
@pulumi.input_type
class SettingsArgs:
    def __init__(__self__, *, access_settings: Optional[pulumi.Input[SettingsAccessSettingsArgs]] = ..., application_settings: Optional[pulumi.Input[SettingsApplicationSettingsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsArgs]]:
        
        ...
    
    @access_settings.setter
    def access_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> Optional[pulumi.Input[SettingsApplicationSettingsArgs]]:
        
        ...
    
    @application_settings.setter
    def application_settings(self, value: Optional[pulumi.Input[SettingsApplicationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SettingsState:
    def __init__(__self__, *, access_settings: Optional[pulumi.Input[SettingsAccessSettingsArgs]] = ..., application_settings: Optional[pulumi.Input[SettingsApplicationSettingsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsArgs]]:
        
        ...
    
    @access_settings.setter
    def access_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> Optional[pulumi.Input[SettingsApplicationSettingsArgs]]:
        
        ...
    
    @application_settings.setter
    def application_settings(self, value: Optional[pulumi.Input[SettingsApplicationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:iap/settings:Settings")
class Settings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_settings: Optional[pulumi.Input[Union[SettingsAccessSettingsArgs, SettingsAccessSettingsArgsDict]]] = ..., application_settings: Optional[pulumi.Input[Union[SettingsApplicationSettingsArgs, SettingsApplicationSettingsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[SettingsArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_settings: Optional[pulumi.Input[Union[SettingsAccessSettingsArgs, SettingsAccessSettingsArgsDict]]] = ..., application_settings: Optional[pulumi.Input[Union[SettingsApplicationSettingsArgs, SettingsApplicationSettingsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> Settings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> pulumi.Output[Optional[outputs.SettingsAccessSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> pulumi.Output[Optional[outputs.SettingsApplicationSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


