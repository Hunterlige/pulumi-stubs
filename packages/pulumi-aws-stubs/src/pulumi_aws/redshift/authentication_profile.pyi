

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthenticationProfileArgs', 'AuthenticationProfile']
@pulumi.input_type
class AuthenticationProfileArgs:
    def __init__(__self__, *, authentication_profile_content: pulumi.Input[_builtins.str], authentication_profile_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileContent")
    def authentication_profile_content(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_profile_content.setter
    def authentication_profile_content(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileName")
    def authentication_profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_profile_name.setter
    def authentication_profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AuthenticationProfileState:
    def __init__(__self__, *, authentication_profile_content: Optional[pulumi.Input[_builtins.str]] = ..., authentication_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileContent")
    def authentication_profile_content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_profile_content.setter
    def authentication_profile_content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileName")
    def authentication_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_profile_name.setter
    def authentication_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AuthenticationProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authentication_profile_content: Optional[pulumi.Input[_builtins.str]] = ..., authentication_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthenticationProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authentication_profile_content: Optional[pulumi.Input[_builtins.str]] = ..., authentication_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> AuthenticationProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileContent")
    def authentication_profile_content(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProfileName")
    def authentication_profile_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


