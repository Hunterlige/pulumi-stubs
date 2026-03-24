

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureMonitorWorkspacePropertiesResponse', 'ConfigurationProfileResourcePropertiesResponse', 'NotificationSettingsResponse', 'ResourceIdentityResponse', 'SystemDataResponse']
@pulumi.output_type
class AzureMonitorWorkspacePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_change_details: Optional[_builtins.str] = ..., workspace_id: Optional[_builtins.str] = ..., workspace_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChangeDetails")
    def include_change_details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConfigurationProfileResourcePropertiesResponse(dict):
    
    def __init__(__self__, *, notifications: Optional[outputs.NotificationSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[outputs.NotificationSettingsResponse]:
        
        ...
    


@pulumi.output_type
class NotificationSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activation_state: Optional[_builtins.str] = ..., azure_monitor_workspace_properties: Optional[outputs.AzureMonitorWorkspacePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceProperties")
    def azure_monitor_workspace_properties(self) -> Optional[outputs.AzureMonitorWorkspacePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ResourceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: _builtins.str, created_by: _builtins.str, created_by_type: _builtins.str, last_modified_at: _builtins.str, last_modified_by: _builtins.str, last_modified_by_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> _builtins.str:
        
        ...
    


