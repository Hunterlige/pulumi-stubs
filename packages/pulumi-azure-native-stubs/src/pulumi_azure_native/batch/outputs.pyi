

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
__all__ = ['ApplicationPackageReferenceResponse', 'AutoScaleRunErrorResponse', 'AutoScaleRunResponse', 'AutoScaleSettingsResponse', 'AutoStoragePropertiesResponse', 'AutoUserSpecificationResponse', 'AutomaticOSUpgradePolicyResponse', 'AzureBlobFileSystemConfigurationResponse', 'AzureFileShareConfigurationResponse', 'BatchAccountIdentityResponse', 'BatchPoolIdentityResponse', 'CIFSMountConfigurationResponse', 'CertificateReferenceResponse', 'ComputeNodeIdentityReferenceResponse', 'ContainerConfigurationResponse', 'ContainerHostBatchBindMountEntryResponse', 'ContainerRegistryResponse', 'DataDiskResponse', 'DeploymentConfigurationResponse', 'DiffDiskSettingsResponse', 'DiskEncryptionConfigurationResponse', 'EncryptionPropertiesResponse', 'EndpointAccessProfileResponse', 'EnvironmentSettingResponse', 'FixedScaleSettingsResponse', 'IPRuleResponse', 'ImageReferenceResponse', 'InboundNatPoolResponse', 'KeyVaultPropertiesResponse', 'KeyVaultReferenceResponse', 'LinuxUserConfigurationResponse', 'ManagedDiskResponse', 'MetadataItemResponse', 'MountConfigurationResponse', 'NFSMountConfigurationResponse', 'NetworkConfigurationResponse', 'NetworkProfileResponse', 'NetworkSecurityGroupRuleResponse', 'NodePlacementConfigurationResponse', 'OSDiskResponse', 'PoolEndpointConfigurationResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'PublicIPAddressConfigurationResponse', 'ResizeErrorResponse', 'ResizeOperationStatusResponse', 'ResourceFileResponse', 'RollingUpgradePolicyResponse', 'ScaleSettingsResponse', 'SecurityProfileResponse', 'ServiceArtifactReferenceResponse', 'StartTaskResponse', 'SystemDataResponse', 'TaskContainerSettingsResponse', 'TaskSchedulingPolicyResponse', 'UefiSettingsResponse', 'UpgradePolicyResponse', 'UserAccountResponse', 'UserAssignedIdentitiesResponse', 'UserIdentityResponse', 'VMDiskSecurityProfileResponse', 'VMExtensionResponse', 'VirtualMachineConfigurationResponse', 'VirtualMachineFamilyCoreQuotaResponse', 'WindowsConfigurationResponse', 'WindowsUserConfigurationResponse']
@pulumi.output_type
class ApplicationPackageReferenceResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoScaleRunErrorResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, details: Optional[Sequence[outputs.AutoScaleRunErrorResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.AutoScaleRunErrorResponse]]:
        
        ...
    


@pulumi.output_type
class AutoScaleRunResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, evaluation_time: _builtins.str, error: Optional[outputs.AutoScaleRunErrorResponse] = ..., results: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationTime")
    def evaluation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.AutoScaleRunErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def results(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoScaleSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, formula: _builtins.str, evaluation_interval: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formula(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoStoragePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_key_sync: _builtins.str, storage_account_id: _builtins.str, authentication_mode: Optional[_builtins.str] = ..., node_identity_reference: Optional[outputs.ComputeNodeIdentityReferenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastKeySync")
    def last_key_sync(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIdentityReference")
    def node_identity_reference(self) -> Optional[outputs.ComputeNodeIdentityReferenceResponse]:
        
        ...
    


@pulumi.output_type
class AutoUserSpecificationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elevation_level: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elevationLevel")
    def elevation_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomaticOSUpgradePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_automatic_rollback: Optional[_builtins.bool] = ..., enable_automatic_os_upgrade: Optional[_builtins.bool] = ..., os_rolling_upgrade_deferral: Optional[_builtins.bool] = ..., use_rolling_upgrade_policy: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAutomaticRollback")
    def disable_automatic_rollback(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticOSUpgrade")
    def enable_automatic_os_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osRollingUpgradeDeferral")
    def os_rolling_upgrade_deferral(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useRollingUpgradePolicy")
    def use_rolling_upgrade_policy(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AzureBlobFileSystemConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_name: _builtins.str, container_name: _builtins.str, relative_mount_path: _builtins.str, account_key: Optional[_builtins.str] = ..., blobfuse_options: Optional[_builtins.str] = ..., identity_reference: Optional[outputs.ComputeNodeIdentityReferenceResponse] = ..., sas_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobfuseOptions")
    def blobfuse_options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(self) -> Optional[outputs.ComputeNodeIdentityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasKey")
    def sas_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureFileShareConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_key: _builtins.str, account_name: _builtins.str, azure_file_url: _builtins.str, relative_mount_path: _builtins.str, mount_options: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileUrl")
    def azure_file_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchAccountIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentitiesResponse]] = ...) -> None:
        
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
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentitiesResponse]]:
        
        ...
    


@pulumi.output_type
class BatchPoolIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentitiesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentitiesResponse]]:
        
        ...
    


@pulumi.output_type
class CIFSMountConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: _builtins.str, relative_mount_path: _builtins.str, source: _builtins.str, user_name: _builtins.str, mount_options: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, store_location: Optional[_builtins.str] = ..., store_name: Optional[_builtins.str] = ..., visibility: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storeLocation")
    def store_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storeName")
    def store_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ComputeNodeIdentityReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, container_image_names: Optional[Sequence[_builtins.str]] = ..., container_registries: Optional[Sequence[outputs.ContainerRegistryResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImageNames")
    def container_image_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRegistries")
    def container_registries(self) -> Optional[Sequence[outputs.ContainerRegistryResponse]]:
        
        ...
    


@pulumi.output_type
class ContainerHostBatchBindMountEntryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_read_only: Optional[_builtins.bool] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerRegistryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_reference: Optional[outputs.ComputeNodeIdentityReferenceResponse] = ..., password: Optional[_builtins.str] = ..., registry_server: Optional[_builtins.str] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(self) -> Optional[outputs.ComputeNodeIdentityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryServer")
    def registry_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: _builtins.int, lun: _builtins.int, caching: Optional[_builtins.str] = ..., storage_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, virtual_machine_configuration: Optional[outputs.VirtualMachineConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(self) -> Optional[outputs.VirtualMachineConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class DiffDiskSettingsResponse(dict):
    
    def __init__(__self__, *, placement: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionConfigurationResponse(dict):
    
    def __init__(__self__, *, targets: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EncryptionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_source: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class EndpointAccessProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_action: _builtins.str, ip_rules: Optional[Sequence[outputs.IPRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence[outputs.IPRuleResponse]]:
        
        ...
    


@pulumi.output_type
class EnvironmentSettingResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FixedScaleSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resize_timeout: Optional[_builtins.str] = ..., target_dedicated_nodes: Optional[_builtins.int] = ..., target_low_priority_nodes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeTimeout")
    def resize_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDedicatedNodes")
    def target_dedicated_nodes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLowPriorityNodes")
    def target_low_priority_nodes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IPRuleResponse(dict):
    
    def __init__(__self__, *, action: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ImageReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, community_gallery_image_id: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., offer: Optional[_builtins.str] = ..., publisher: Optional[_builtins.str] = ..., shared_gallery_image_id: Optional[_builtins.str] = ..., sku: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InboundNatPoolResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backend_port: _builtins.int, frontend_port_range_end: _builtins.int, frontend_port_range_start: _builtins.int, name: _builtins.str, protocol: _builtins.str, network_security_group_rules: Optional[Sequence[outputs.NetworkSecurityGroupRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupRules")
    def network_security_group_rules(self) -> Optional[Sequence[outputs.NetworkSecurityGroupRuleResponse]]:
        
        ...
    


@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_identifier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeyVaultReferenceResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LinuxUserConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gid: Optional[_builtins.int] = ..., ssh_private_key: Optional[_builtins.str] = ..., uid: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPrivateKey")
    def ssh_private_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ManagedDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_profile: Optional[outputs.VMDiskSecurityProfileResponse] = ..., storage_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.VMDiskSecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetadataItemResponse(dict):
    
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
class MountConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_blob_file_system_configuration: Optional[outputs.AzureBlobFileSystemConfigurationResponse] = ..., azure_file_share_configuration: Optional[outputs.AzureFileShareConfigurationResponse] = ..., cifs_mount_configuration: Optional[outputs.CIFSMountConfigurationResponse] = ..., nfs_mount_configuration: Optional[outputs.NFSMountConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlobFileSystemConfiguration")
    def azure_blob_file_system_configuration(self) -> Optional[outputs.AzureBlobFileSystemConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFileShareConfiguration")
    def azure_file_share_configuration(self) -> Optional[outputs.AzureFileShareConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cifsMountConfiguration")
    def cifs_mount_configuration(self) -> Optional[outputs.CIFSMountConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsMountConfiguration")
    def nfs_mount_configuration(self) -> Optional[outputs.NFSMountConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class NFSMountConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, relative_mount_path: _builtins.str, source: _builtins.str, mount_options: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dynamic_vnet_assignment_scope: Optional[_builtins.str] = ..., enable_accelerated_networking: Optional[_builtins.bool] = ..., endpoint_configuration: Optional[outputs.PoolEndpointConfigurationResponse] = ..., public_ip_address_configuration: Optional[outputs.PublicIPAddressConfigurationResponse] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicVnetAssignmentScope")
    def dynamic_vnet_assignment_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> Optional[outputs.PoolEndpointConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(self) -> Optional[outputs.PublicIPAddressConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_access: Optional[outputs.EndpointAccessProfileResponse] = ..., node_management_access: Optional[outputs.EndpointAccessProfileResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountAccess")
    def account_access(self) -> Optional[outputs.EndpointAccessProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeManagementAccess")
    def node_management_access(self) -> Optional[outputs.EndpointAccessProfileResponse]:
        
        ...
    


@pulumi.output_type
class NetworkSecurityGroupRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access: _builtins.str, priority: _builtins.int, source_address_prefix: _builtins.str, source_port_ranges: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def access(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class NodePlacementConfigurationResponse(dict):
    
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, caching: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., ephemeral_os_disk_settings: Optional[outputs.DiffDiskSettingsResponse] = ..., managed_disk: Optional[outputs.ManagedDiskResponse] = ..., write_accelerator_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralOSDiskSettings")
    def ephemeral_os_disk_settings(self) -> Optional[outputs.DiffDiskSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[outputs.ManagedDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PoolEndpointConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inbound_nat_pools: Sequence[outputs.InboundNatPoolResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundNatPools")
    def inbound_nat_pools(self) -> Sequence[outputs.InboundNatPoolResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, group_ids: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, private_endpoint: outputs.PrivateEndpointResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, status: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PublicIPAddressConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address_ids: Optional[Sequence[_builtins.str]] = ..., provision: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressIds")
    def ip_address_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provision(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResizeErrorResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, details: Optional[Sequence[outputs.ResizeErrorResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.ResizeErrorResponse]]:
        
        ...
    


@pulumi.output_type
class ResizeOperationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, errors: Optional[Sequence[outputs.ResizeErrorResponse]] = ..., resize_timeout: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., target_dedicated_nodes: Optional[_builtins.int] = ..., target_low_priority_nodes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ResizeErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeTimeout")
    def resize_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDedicatedNodes")
    def target_dedicated_nodes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLowPriorityNodes")
    def target_low_priority_nodes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ResourceFileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_storage_container_name: Optional[_builtins.str] = ..., blob_prefix: Optional[_builtins.str] = ..., file_mode: Optional[_builtins.str] = ..., file_path: Optional[_builtins.str] = ..., http_url: Optional[_builtins.str] = ..., identity_reference: Optional[outputs.ComputeNodeIdentityReferenceResponse] = ..., storage_container_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoStorageContainerName")
    def auto_storage_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobPrefix")
    def blob_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpUrl")
    def http_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(self) -> Optional[outputs.ComputeNodeIdentityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerUrl")
    def storage_container_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RollingUpgradePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_cross_zone_upgrade: Optional[_builtins.bool] = ..., max_batch_instance_percent: Optional[_builtins.int] = ..., max_unhealthy_instance_percent: Optional[_builtins.int] = ..., max_unhealthy_upgraded_instance_percent: Optional[_builtins.int] = ..., pause_time_between_batches: Optional[_builtins.str] = ..., prioritize_unhealthy_instances: Optional[_builtins.bool] = ..., rollback_failed_instances_on_policy_breach: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneUpgrade")
    def enable_cross_zone_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBatchInstancePercent")
    def max_batch_instance_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyInstancePercent")
    def max_unhealthy_instance_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyUpgradedInstancePercent")
    def max_unhealthy_upgraded_instance_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pauseTimeBetweenBatches")
    def pause_time_between_batches(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prioritizeUnhealthyInstances")
    def prioritize_unhealthy_instances(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollbackFailedInstancesOnPolicyBreach")
    def rollback_failed_instances_on_policy_breach(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ScaleSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_scale: Optional[outputs.AutoScaleSettingsResponse] = ..., fixed_scale: Optional[outputs.FixedScaleSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[outputs.AutoScaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedScale")
    def fixed_scale(self) -> Optional[outputs.FixedScaleSettingsResponse]:
        
        ...
    


@pulumi.output_type
class SecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_at_host: Optional[_builtins.bool] = ..., security_type: Optional[_builtins.str] = ..., uefi_settings: Optional[outputs.UefiSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[outputs.UefiSettingsResponse]:
        
        ...
    


@pulumi.output_type
class ServiceArtifactReferenceResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StartTaskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, command_line: Optional[_builtins.str] = ..., container_settings: Optional[outputs.TaskContainerSettingsResponse] = ..., environment_settings: Optional[Sequence[outputs.EnvironmentSettingResponse]] = ..., max_task_retry_count: Optional[_builtins.int] = ..., resource_files: Optional[Sequence[outputs.ResourceFileResponse]] = ..., user_identity: Optional[outputs.UserIdentityResponse] = ..., wait_for_success: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandLine")
    def command_line(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(self) -> Optional[outputs.TaskContainerSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentSettings")
    def environment_settings(self) -> Optional[Sequence[outputs.EnvironmentSettingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTaskRetryCount")
    def max_task_retry_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceFiles")
    def resource_files(self) -> Optional[Sequence[outputs.ResourceFileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[outputs.UserIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSuccess")
    def wait_for_success(self) -> Optional[_builtins.bool]:
        
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
class TaskContainerSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_name: _builtins.str, container_host_batch_bind_mounts: Optional[Sequence[outputs.ContainerHostBatchBindMountEntryResponse]] = ..., container_run_options: Optional[_builtins.str] = ..., registry: Optional[outputs.ContainerRegistryResponse] = ..., working_directory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerHostBatchBindMounts")
    def container_host_batch_bind_mounts(self) -> Optional[Sequence[outputs.ContainerHostBatchBindMountEntryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRunOptions")
    def container_run_options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registry(self) -> Optional[outputs.ContainerRegistryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskSchedulingPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_fill_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeFillType")
    def node_fill_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UefiSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secure_boot_enabled: Optional[_builtins.bool] = ..., v_tpm_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vTpmEnabled")
    def v_tpm_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UpgradePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: _builtins.str, automatic_os_upgrade_policy: Optional[outputs.AutomaticOSUpgradePolicyResponse] = ..., rolling_upgrade_policy: Optional[outputs.RollingUpgradePolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticOSUpgradePolicy")
    def automatic_os_upgrade_policy(self) -> Optional[outputs.AutomaticOSUpgradePolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingUpgradePolicy")
    def rolling_upgrade_policy(self) -> Optional[outputs.RollingUpgradePolicyResponse]:
        
        ...
    


@pulumi.output_type
class UserAccountResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, password: _builtins.str, elevation_level: Optional[_builtins.str] = ..., linux_user_configuration: Optional[outputs.LinuxUserConfigurationResponse] = ..., windows_user_configuration: Optional[outputs.WindowsUserConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elevationLevel")
    def elevation_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxUserConfiguration")
    def linux_user_configuration(self) -> Optional[outputs.LinuxUserConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsUserConfiguration")
    def windows_user_configuration(self) -> Optional[outputs.WindowsUserConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentitiesResponse(dict):
    
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
class UserIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_user: Optional[outputs.AutoUserSpecificationResponse] = ..., user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUser")
    def auto_user(self) -> Optional[outputs.AutoUserSpecificationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMDiskSecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_encryption_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMExtensionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, publisher: _builtins.str, type: _builtins.str, auto_upgrade_minor_version: Optional[_builtins.bool] = ..., enable_automatic_upgrade: Optional[_builtins.bool] = ..., protected_settings: Optional[Any] = ..., provision_after_extensions: Optional[Sequence[_builtins.str]] = ..., settings: Optional[Any] = ..., type_handler_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_reference: outputs.ImageReferenceResponse, node_agent_sku_id: _builtins.str, container_configuration: Optional[outputs.ContainerConfigurationResponse] = ..., data_disks: Optional[Sequence[outputs.DataDiskResponse]] = ..., disk_encryption_configuration: Optional[outputs.DiskEncryptionConfigurationResponse] = ..., extensions: Optional[Sequence[outputs.VMExtensionResponse]] = ..., license_type: Optional[_builtins.str] = ..., node_placement_configuration: Optional[outputs.NodePlacementConfigurationResponse] = ..., os_disk: Optional[outputs.OSDiskResponse] = ..., security_profile: Optional[outputs.SecurityProfileResponse] = ..., service_artifact_reference: Optional[outputs.ServiceArtifactReferenceResponse] = ..., windows_configuration: Optional[outputs.WindowsConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> outputs.ImageReferenceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAgentSkuId")
    def node_agent_sku_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerConfiguration")
    def container_configuration(self) -> Optional[outputs.ContainerConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[Sequence[outputs.DataDiskResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionConfiguration")
    def disk_encryption_configuration(self) -> Optional[outputs.DiskEncryptionConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[outputs.VMExtensionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePlacementConfiguration")
    def node_placement_configuration(self) -> Optional[outputs.NodePlacementConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[outputs.OSDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReference")
    def service_artifact_reference(self) -> Optional[outputs.ServiceArtifactReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[outputs.WindowsConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class VirtualMachineFamilyCoreQuotaResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, core_quota: _builtins.int, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreQuota")
    def core_quota(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WindowsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_automatic_updates: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WindowsUserConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginMode")
    def login_mode(self) -> Optional[_builtins.str]:
        
        ...
    


