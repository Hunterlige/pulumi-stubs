

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['B2CResourceSKUResponse', 'B2CTenantResourcePropertiesResponseBillingConfig', 'CIAMResourceSKUResponse', 'CreateCIAMTenantPropertiesResponse', 'SystemDataResponse']
@pulumi.output_type
class B2CResourceSKUResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class B2CTenantResourcePropertiesResponseBillingConfig(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_start_date_utc: _builtins.str, billing_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveStartDateUtc")
    def effective_start_date_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CIAMResourceSKUResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CreateCIAMTenantPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_code: _builtins.str, display_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
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
    


