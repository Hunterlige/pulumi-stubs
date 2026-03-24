

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssignmentResponse', 'AssignmentStatusResponse', 'AzureDiskResponse', 'DiskResponse', 'ElasticSanResponse', 'ElasticSanVolumePropertiesResponse', 'EncryptionResponse', 'EphemeralDiskResponse', 'ManagedServiceIdentityResponse', 'PoolTypeResponse', 'RequestsResponse', 'ResourceOperationalStatusResponse', 'ResourcesResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', 'VolumeTypeResponse']
@pulumi.output_type
class AssignmentResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, status: outputs.AssignmentStatusResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.AssignmentStatusResponse:
        
        ...
    


@pulumi.output_type
class AssignmentStatusResponse(dict):
    
    def __init__(__self__, *, state: _builtins.str, message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: _builtins.str, disks: Optional[Sequence[outputs.DiskResponse]] = ..., encryption: Optional[outputs.EncryptionResponse] = ..., sku_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.DiskResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, reference: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ElasticSanResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: _builtins.str, encryption: Optional[outputs.EncryptionResponse] = ..., sku_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ElasticSanVolumePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_iqn: _builtins.str, target_portal_hostname: _builtins.str, target_portal_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPortalHostname")
    def target_portal_hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPortalPort")
    def target_portal_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: _builtins.str, key_vault_uri: _builtins.str, identity: Optional[outputs.ManagedServiceIdentityResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    


@pulumi.output_type
class EphemeralDiskResponse(dict):
    
    def __init__(__self__, *, disks: Optional[Sequence[outputs.DiskResponse]] = ..., replicas: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.DiskResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
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
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class PoolTypeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_disk: Optional[outputs.AzureDiskResponse] = ..., elastic_san: Optional[outputs.ElasticSanResponse] = ..., ephemeral_disk: Optional[outputs.EphemeralDiskResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDisk")
    def azure_disk(self) -> Optional[outputs.AzureDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSan")
    def elastic_san(self) -> Optional[outputs.ElasticSanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralDisk")
    def ephemeral_disk(self) -> Optional[outputs.EphemeralDiskResponse]:
        
        ...
    


@pulumi.output_type
class RequestsResponse(dict):
    
    def __init__(__self__, *, storage: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ResourceOperationalStatusResponse(dict):
    
    def __init__(__self__, *, state: _builtins.str, message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourcesResponse(dict):
    
    def __init__(__self__, *, requests: Optional[outputs.RequestsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[outputs.RequestsResponse]:
        
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
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VolumeTypeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elastic_san: outputs.ElasticSanVolumePropertiesResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSan")
    def elastic_san(self) -> outputs.ElasticSanVolumePropertiesResponse:
        
        ...
    


