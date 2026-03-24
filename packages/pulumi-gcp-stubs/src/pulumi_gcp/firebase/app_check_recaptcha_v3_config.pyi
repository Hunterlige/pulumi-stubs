

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppCheckRecaptchaV3ConfigArgs', 'AppCheckRecaptchaV3Config']
@pulumi.input_type
class AppCheckRecaptchaV3ConfigArgs:
    def __init__(__self__, *, app_id: pulumi.Input[_builtins.str], site_secret: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ..., token_ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @site_secret.setter
    def site_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AppCheckRecaptchaV3ConfigState:
    def __init__(__self__, *, app_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., site_secret: Optional[pulumi.Input[_builtins.str]] = ..., site_secret_set: Optional[pulumi.Input[_builtins.bool]] = ..., token_ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site_secret.setter
    def site_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteSecretSet")
    def site_secret_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @site_secret_set.setter
    def site_secret_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AppCheckRecaptchaV3Config(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., site_secret: Optional[pulumi.Input[_builtins.str]] = ..., token_ttl: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AppCheckRecaptchaV3ConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., site_secret: Optional[pulumi.Input[_builtins.str]] = ..., site_secret_set: Optional[pulumi.Input[_builtins.bool]] = ..., token_ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> AppCheckRecaptchaV3Config:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteSecret")
    def site_secret(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteSecretSet")
    def site_secret_set(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


