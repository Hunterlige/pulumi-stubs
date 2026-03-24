

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserSettingsAssociationArgs', 'UserSettingsAssociation']
@pulumi.input_type
class UserSettingsAssociationArgs:
    def __init__(__self__, *, portal_arn: pulumi.Input[_builtins.str], user_settings_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_settings_arn.setter
    def user_settings_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UserSettingsAssociationState:
    def __init__(__self__, *, portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_settings_arn.setter
    def user_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class UserSettingsAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserSettingsAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> UserSettingsAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


