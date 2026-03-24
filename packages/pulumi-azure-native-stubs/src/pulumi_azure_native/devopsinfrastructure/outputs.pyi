

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
__all__ = ['AutomaticResourcePredictionsProfileResponse', 'AzureDevOpsOrganizationProfileResponse', 'AzureDevOpsPermissionProfileResponse', 'DataDiskResponse', 'DevOpsAzureSkuResponse', 'GitHubOrganizationProfileResponse', 'GitHubOrganizationResponse', 'ManagedServiceIdentityResponse', 'ManualResourcePredictionsProfileResponse', 'NetworkProfileResponse', 'OrganizationResponse', 'OsProfileResponse', 'PoolImageResponse', 'SecretsManagementSettingsResponse', 'StatefulResponse', 'StatelessAgentProfileResponse', 'StorageProfileResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', 'VmssFabricProfileResponse']
@pulumi.output_type
class AutomaticResourcePredictionsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, prediction_preference: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictionPreference")
    def prediction_preference(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureDevOpsOrganizationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, organizations: Sequence[outputs.OrganizationResponse], permission_profile: Optional[outputs.AzureDevOpsPermissionProfileResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organizations(self) -> Sequence[outputs.OrganizationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionProfile")
    def permission_profile(self) -> Optional[outputs.AzureDevOpsPermissionProfileResponse]:
        
        ...
    


@pulumi.output_type
class AzureDevOpsPermissionProfileResponse(dict):
    
    def __init__(__self__, *, kind: _builtins.str, groups: Optional[Sequence[_builtins.str]] = ..., users: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DataDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, caching: Optional[_builtins.str] = ..., disk_size_gi_b: Optional[_builtins.int] = ..., drive_letter: Optional[_builtins.str] = ..., storage_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGiB")
    def disk_size_gi_b(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveLetter")
    def drive_letter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DevOpsAzureSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GitHubOrganizationProfileResponse(dict):
    
    def __init__(__self__, *, kind: _builtins.str, organizations: Sequence[outputs.GitHubOrganizationResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organizations(self) -> Sequence[outputs.GitHubOrganizationResponse]:
        
        ...
    


@pulumi.output_type
class GitHubOrganizationResponse(dict):
    
    def __init__(__self__, *, url: _builtins.str, repositories: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repositories(self) -> Optional[Sequence[_builtins.str]]:
        
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
class ManualResourcePredictionsProfileResponse(dict):
    
    def __init__(__self__, *, kind: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OrganizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, open_access: Optional[_builtins.bool] = ..., parallelism: Optional[_builtins.int] = ..., projects: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAccess")
    def open_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def projects(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class OsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, logon_type: Optional[_builtins.str] = ..., secrets_management_settings: Optional[outputs.SecretsManagementSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logonType")
    def logon_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsManagementSettings")
    def secrets_management_settings(self) -> Optional[outputs.SecretsManagementSettingsResponse]:
        
        ...
    


@pulumi.output_type
class PoolImageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aliases: Optional[Sequence[_builtins.str]] = ..., buffer: Optional[_builtins.str] = ..., ephemeral_type: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., well_known_image_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buffer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralType")
    def ephemeral_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wellKnownImageName")
    def well_known_image_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretsManagementSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_exportable: _builtins.bool, observed_certificates: Sequence[_builtins.str], certificate_store_location: Optional[_builtins.str] = ..., certificate_store_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyExportable")
    def key_exportable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedCertificates")
    def observed_certificates(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateStoreLocation")
    def certificate_store_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateStoreName")
    def certificate_store_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StatefulResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, grace_period_time_span: Optional[_builtins.str] = ..., max_agent_lifetime: Optional[_builtins.str] = ..., resource_predictions: Optional[Any] = ..., resource_predictions_profile: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gracePeriodTimeSpan")
    def grace_period_time_span(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgentLifetime")
    def max_agent_lifetime(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePredictions")
    def resource_predictions(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePredictionsProfile")
    def resource_predictions_profile(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class StatelessAgentProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, resource_predictions: Optional[Any] = ..., resource_predictions_profile: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePredictions")
    def resource_predictions(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePredictionsProfile")
    def resource_predictions_profile(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class StorageProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_disks: Optional[Sequence[outputs.DataDiskResponse]] = ..., os_disk_storage_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[Sequence[outputs.DataDiskResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskStorageAccountType")
    def os_disk_storage_account_type(self) -> Optional[_builtins.str]:
        
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
class VmssFabricProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, images: Sequence[outputs.PoolImageResponse], kind: _builtins.str, sku: outputs.DevOpsAzureSkuResponse, network_profile: Optional[outputs.NetworkProfileResponse] = ..., os_profile: Optional[outputs.OsProfileResponse] = ..., storage_profile: Optional[outputs.StorageProfileResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Sequence[outputs.PoolImageResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.DevOpsAzureSkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OsProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]:
        
        ...
    


