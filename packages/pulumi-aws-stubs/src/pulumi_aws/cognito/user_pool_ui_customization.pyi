

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserPoolUICustomizationArgs', 'UserPoolUICustomization']
@pulumi.input_type
class UserPoolUICustomizationArgs:
    def __init__(__self__, *, user_pool_id: pulumi.Input[_builtins.str], client_id: Optional[pulumi.Input[_builtins.str]] = ..., css: Optional[pulumi.Input[_builtins.str]] = ..., image_file: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def css(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @css.setter
    def css(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageFile")
    def image_file(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_file.setter
    def image_file(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UserPoolUICustomizationState:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., css: Optional[pulumi.Input[_builtins.str]] = ..., css_version: Optional[pulumi.Input[_builtins.str]] = ..., image_file: Optional[pulumi.Input[_builtins.str]] = ..., image_url: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_date: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def css(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @css.setter
    def css(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cssVersion")
    def css_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @css_version.setter
    def css_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageFile")
    def image_file(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_file.setter
    def image_file(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_url.setter
    def image_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_date.setter
    def last_modified_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class UserPoolUICustomization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., css: Optional[pulumi.Input[_builtins.str]] = ..., image_file: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserPoolUICustomizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., css: Optional[pulumi.Input[_builtins.str]] = ..., css_version: Optional[pulumi.Input[_builtins.str]] = ..., image_file: Optional[pulumi.Input[_builtins.str]] = ..., image_url: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_date: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> UserPoolUICustomization:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def css(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cssVersion")
    def css_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageFile")
    def image_file(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


