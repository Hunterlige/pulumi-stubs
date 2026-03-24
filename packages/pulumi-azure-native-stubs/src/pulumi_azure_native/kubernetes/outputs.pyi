

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AadProfileResponse', 'AgentErrorResponse', 'ArcAgentProfileResponse', 'ConnectedClusterIdentityResponse', 'CredentialResultResponse', 'HybridConnectionConfigResponse', 'SystemComponentResponse', 'SystemDataResponse']
@pulumi.output_type
class AadProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_group_object_ids: Optional[Sequence[_builtins.str]] = ..., enable_azure_rbac: Optional[_builtins.bool] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminGroupObjectIDs")
    def admin_group_object_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAzureRBAC")
    def enable_azure_rbac(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AgentErrorResponse(dict):
    
    def __init__(__self__, *, component: _builtins.str, message: _builtins.str, severity: _builtins.str, time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def component(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ArcAgentProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_auto_upgrade: Optional[_builtins.str] = ..., agent_errors: Optional[Sequence[outputs.AgentErrorResponse]] = ..., desired_agent_version: Optional[_builtins.str] = ..., system_components: Optional[Sequence[outputs.SystemComponentResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentAutoUpgrade")
    def agent_auto_upgrade(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentErrors")
    def agent_errors(self) -> Optional[Sequence[outputs.AgentErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredAgentVersion")
    def desired_agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemComponents")
    def system_components(self) -> Optional[Sequence[outputs.SystemComponentResponse]]:
        
        ...
    


@pulumi.output_type
class ConnectedClusterIdentityResponse(dict):
    
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
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CredentialResultResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HybridConnectionConfigResponse(dict):
    
    def __init__(__self__, *, expiration_time: _builtins.float, hybrid_connection_name: _builtins.str, relay: _builtins.str, token: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridConnectionName")
    def hybrid_connection_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def relay(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SystemComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, current_version: _builtins.str, major_version: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ..., user_specified_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorVersion")
    def major_version(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSpecifiedVersion")
    def user_specified_version(self) -> Optional[_builtins.str]:
        
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
    


