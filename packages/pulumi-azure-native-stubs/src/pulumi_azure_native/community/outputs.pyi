

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IdentityConfigurationPropertiesResponse', 'SkuResponse', 'SystemDataResponse']
@pulumi.output_type
class IdentityConfigurationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret: _builtins.str, domain_name: _builtins.str, identity_type: _builtins.str, tenant_id: _builtins.str, b2c_authentication_policy: Optional[_builtins.str] = ..., b2c_password_reset_policy: Optional[_builtins.str] = ..., custom_login_parameters: Optional[_builtins.str] = ..., teams_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="b2cAuthenticationPolicy")
    def b2c_authentication_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="b2cPasswordResetPolicy")
    def b2c_password_reset_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLoginParameters")
    def custom_login_parameters(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamsEnabled")
    def teams_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


