

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
__all__ = ['AuthenticationSettingArgs', 'AuthenticationSetting']
@pulumi.input_type
class AuthenticationSettingArgs:
    def __init__(__self__, *, health_model_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], authentication_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[ManagedIdentityAuthenticationSettingPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthModelName")
    def health_model_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @health_model_name.setter
    def health_model_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationSettingName")
    def authentication_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_setting_name.setter
    def authentication_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[ManagedIdentityAuthenticationSettingPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[ManagedIdentityAuthenticationSettingPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cloudhealth:AuthenticationSetting")
class AuthenticationSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authentication_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., health_model_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[ManagedIdentityAuthenticationSettingPropertiesArgs, ManagedIdentityAuthenticationSettingPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthenticationSettingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AuthenticationSetting:
        
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
    def properties(self) -> pulumi.Output[outputs.ManagedIdentityAuthenticationSettingPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


