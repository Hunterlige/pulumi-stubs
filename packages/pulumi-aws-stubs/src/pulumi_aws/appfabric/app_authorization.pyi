

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppAuthorizationArgs', 'AppAuthorization']
@pulumi.input_type
class AppAuthorizationArgs:
    def __init__(__self__, *, app: pulumi.Input[_builtins.str], app_bundle_arn: pulumi.Input[_builtins.str], auth_type: pulumi.Input[_builtins.str], credential: pulumi.Input[AppAuthorizationCredentialArgs], tenants: pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app.setter
    def app(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> pulumi.Input[AppAuthorizationCredentialArgs]:
        
        ...
    
    @credential.setter
    def credential(self, value: pulumi.Input[AppAuthorizationCredentialArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenants(self) -> pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]]:
        
        ...
    
    @tenants.setter
    def tenants(self, value: pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AppAuthorizationState:
    def __init__(__self__, *, app: Optional[pulumi.Input[_builtins.str]] = ..., app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auth_type: Optional[pulumi.Input[_builtins.str]] = ..., auth_url: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., credential: Optional[pulumi.Input[AppAuthorizationCredentialArgs]] = ..., persona: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenants: Optional[pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]]] = ..., timeouts: Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_url.setter
    def auth_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> Optional[pulumi.Input[AppAuthorizationCredentialArgs]]:
        
        ...
    
    @credential.setter
    def credential(self, value: Optional[pulumi.Input[AppAuthorizationCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @persona.setter
    def persona(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]]]:
        
        ...
    
    @tenants.setter
    def tenants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppAuthorizationTenantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AppAuthorizationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:appfabric/appAuthorization:AppAuthorization")
class AppAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ..., auth_type: Optional[pulumi.Input[_builtins.str]] = ..., credential: Optional[pulumi.Input[Union[AppAuthorizationCredentialArgs, AppAuthorizationCredentialArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppAuthorizationTenantArgs, AppAuthorizationTenantArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[AppAuthorizationTimeoutsArgs, AppAuthorizationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppAuthorizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auth_type: Optional[pulumi.Input[_builtins.str]] = ..., auth_url: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., credential: Optional[pulumi.Input[Union[AppAuthorizationCredentialArgs, AppAuthorizationCredentialArgsDict]]] = ..., persona: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppAuthorizationTenantArgs, AppAuthorizationTenantArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[AppAuthorizationTimeoutsArgs, AppAuthorizationTimeoutsArgsDict]]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> AppAuthorization:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credential(self) -> pulumi.Output[outputs.AppAuthorizationCredential]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def persona(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenants(self) -> pulumi.Output[Sequence[outputs.AppAuthorizationTenant]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AppAuthorizationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        ...
    


