

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkforcePoolProviderScimTokenArgs', 'WorkforcePoolProviderScimToken']
@pulumi.input_type
class WorkforcePoolProviderScimTokenArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], provider_id: pulumi.Input[_builtins.str], scim_tenant_id: pulumi.Input[_builtins.str], scim_token_id: pulumi.Input[_builtins.str], workforce_pool_id: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scim_tenant_id.setter
    def scim_tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTokenId")
    def scim_token_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scim_token_id.setter
    def scim_token_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkforcePoolProviderScimTokenState:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_token_id: Optional[pulumi.Input[_builtins.str]] = ..., security_token: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scim_tenant_id.setter
    def scim_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTokenId")
    def scim_token_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scim_token_id.setter
    def scim_token_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkforcePoolProviderScimToken(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_token_id: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkforcePoolProviderScimTokenArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., scim_token_id: Optional[pulumi.Input[_builtins.str]] = ..., security_token: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkforcePoolProviderScimToken:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTenantId")
    def scim_tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimTokenId")
    def scim_token_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


