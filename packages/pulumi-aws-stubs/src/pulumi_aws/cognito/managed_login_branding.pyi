

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
__all__ = ['ManagedLoginBrandingArgs', 'ManagedLoginBranding']
@pulumi.input_type
class ManagedLoginBrandingArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], user_pool_id: pulumi.Input[_builtins.str], assets: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[_builtins.str]] = ..., use_cognito_provided_values: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def assets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]]:
        
        ...
    
    @assets.setter
    def assets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]]): # -> None:
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
    def settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useCognitoProvidedValues")
    def use_cognito_provided_values(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_cognito_provided_values.setter
    def use_cognito_provided_values(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ManagedLoginBrandingState:
    def __init__(__self__, *, assets: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_login_branding_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[_builtins.str]] = ..., settings_all: Optional[pulumi.Input[_builtins.str]] = ..., use_cognito_provided_values: Optional[pulumi.Input[_builtins.bool]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]]:
        
        ...
    
    @assets.setter
    def assets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedLoginBrandingAssetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedLoginBrandingId")
    def managed_login_branding_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_login_branding_id.setter
    def managed_login_branding_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingsAll")
    def settings_all(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @settings_all.setter
    def settings_all(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useCognitoProvidedValues")
    def use_cognito_provided_values(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_cognito_provided_values.setter
    def use_cognito_provided_values(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagedLoginBranding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagedLoginBrandingAssetArgs, ManagedLoginBrandingAssetArgsDict]]]]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[_builtins.str]] = ..., use_cognito_provided_values: Optional[pulumi.Input[_builtins.bool]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedLoginBrandingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., assets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ManagedLoginBrandingAssetArgs, ManagedLoginBrandingAssetArgsDict]]]]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_login_branding_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[_builtins.str]] = ..., settings_all: Optional[pulumi.Input[_builtins.str]] = ..., use_cognito_provided_values: Optional[pulumi.Input[_builtins.bool]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ManagedLoginBranding:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assets(self) -> pulumi.Output[Optional[Sequence[outputs.ManagedLoginBrandingAsset]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedLoginBrandingId")
    def managed_login_branding_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingsAll")
    def settings_all(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useCognitoProvidedValues")
    def use_cognito_provided_values(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


