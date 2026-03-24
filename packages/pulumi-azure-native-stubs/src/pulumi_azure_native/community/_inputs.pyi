

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentityConfigurationPropertiesArgs', 'IdentityConfigurationPropertiesArgsDict', 'SkuArgs', 'SkuArgsDict']
class IdentityConfigurationPropertiesArgsDict(TypedDict):
    
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    domain_name: pulumi.Input[_builtins.str]
    identity_type: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]
    b2c_authentication_policy: NotRequired[pulumi.Input[_builtins.str]]
    b2c_password_reset_policy: NotRequired[pulumi.Input[_builtins.str]]
    custom_login_parameters: NotRequired[pulumi.Input[_builtins.str]]
    teams_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class IdentityConfigurationPropertiesArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], domain_name: pulumi.Input[_builtins.str], identity_type: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], b2c_authentication_policy: Optional[pulumi.Input[_builtins.str]] = ..., b2c_password_reset_policy: Optional[pulumi.Input[_builtins.str]] = ..., custom_login_parameters: Optional[pulumi.Input[_builtins.str]] = ..., teams_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="b2cAuthenticationPolicy")
    def b2c_authentication_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @b2c_authentication_policy.setter
    def b2c_authentication_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="b2cPasswordResetPolicy")
    def b2c_password_reset_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @b2c_password_reset_policy.setter
    def b2c_password_reset_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLoginParameters")
    def custom_login_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_login_parameters.setter
    def custom_login_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamsEnabled")
    def teams_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @teams_enabled.setter
    def teams_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    


