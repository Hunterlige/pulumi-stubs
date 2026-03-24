

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentityPoolProviderPrincipalTagArgs', 'IdentityPoolProviderPrincipalTag']
@pulumi.input_type
class IdentityPoolProviderPrincipalTagArgs:
    def __init__(__self__, *, identity_pool_id: pulumi.Input[_builtins.str], identity_provider_name: pulumi.Input[_builtins.str], principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., use_defaults: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_provider_name.setter
    def identity_provider_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @principal_tags.setter
    def principal_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_defaults.setter
    def use_defaults(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _IdentityPoolProviderPrincipalTagState:
    def __init__(__self__, *, identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_provider_name: Optional[pulumi.Input[_builtins.str]] = ..., principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., use_defaults: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_provider_name.setter
    def identity_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @principal_tags.setter
    def principal_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_defaults.setter
    def use_defaults(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IdentityPoolProviderPrincipalTag(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_provider_name: Optional[pulumi.Input[_builtins.str]] = ..., principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., use_defaults: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IdentityPoolProviderPrincipalTagArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_provider_name: Optional[pulumi.Input[_builtins.str]] = ..., principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., use_defaults: Optional[pulumi.Input[_builtins.bool]] = ...) -> IdentityPoolProviderPrincipalTag:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


