

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
__all__ = ['DefenderForStorageArgs', 'DefenderForStorage']
@pulumi.input_type
class DefenderForStorageArgs:
    def __init__(__self__, *, resource_id: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[DefenderForStorageSettingPropertiesArgs]] = ..., setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[DefenderForStorageSettingPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[DefenderForStorageSettingPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @setting_name.setter
    def setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:DefenderForStorage")
class DefenderForStorage(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., properties: Optional[pulumi.Input[Union[DefenderForStorageSettingPropertiesArgs, DefenderForStorageSettingPropertiesArgsDict]]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., setting_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefenderForStorageArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DefenderForStorage:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.DefenderForStorageSettingPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


