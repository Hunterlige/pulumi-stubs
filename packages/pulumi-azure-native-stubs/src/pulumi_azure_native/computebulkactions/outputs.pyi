

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
__all__ = ['AdditionalCapabilitiesResponse', 'AdditionalUnattendContentResponse', 'AllInstancesDownResponse', 'ApiEntityReferenceResponse', 'ApplicationProfileResponse', 'BootDiagnosticsResponse', 'CapacityReservationProfileResponse', 'ComputeProfileResponse', 'DataDiskResponse', 'DiagnosticsProfileResponse', 'DiffDiskSettingsResponse', 'DiskEncryptionSetParametersResponse', 'DiskEncryptionSettingsResponse', 'EncryptionIdentityResponse', 'EventGridAndResourceGraphResponse', 'HostEndpointSettingsResponse', 'ImageReferenceResponse', 'KeyVaultKeyReferenceResponse', 'KeyVaultSecretReferenceResponse', 'LaunchBulkInstancesOperationPropertiesResponse', 'LinuxConfigurationResponse', 'LinuxPatchSettingsResponse', ..., 'ManagedDiskParametersResponse', 'ManagedServiceIdentityResponse', 'NetworkInterfaceReferencePropertiesResponse', 'NetworkInterfaceReferenceResponse', 'NetworkProfileResponse', 'OSDiskResponse', 'OSImageNotificationProfileResponse', 'OSProfileResponse', 'PatchSettingsResponse', 'PlanResponse', 'PriorityProfileResponse', 'ProxyAgentSettingsResponse', 'PublicIPAddressSkuResponse', 'RetryPolicyResponse', 'ScheduledEventsAdditionalPublishingTargetsResponse', 'ScheduledEventsPolicyResponse', 'ScheduledEventsProfileResponse', 'SecurityProfileResponse', 'SshConfigurationResponse', 'SshPublicKeyResponse', 'StorageProfileResponse', 'SubResourceResponse', 'SystemDataResponse', 'TerminateNotificationProfileResponse', 'UefiSettingsResponse', 'UserAssignedIdentityResponse', 'UserInitiatedRebootResponse', 'UserInitiatedRedeployResponse', 'VMAttributeMinMaxDoubleResponse', 'VMAttributeMinMaxIntegerResponse', 'VMAttributesResponse', 'VMDiskSecurityProfileResponse', 'VMGalleryApplicationResponse', 'VaultCertificateResponse', 'VaultSecretGroupResponse', 'VirtualHardDiskResponse', 'VirtualMachineExtensionPropertiesResponse', 'VirtualMachineExtensionResponse', 'VirtualMachineIpTagResponse', ..., ..., ..., ..., ..., 'VirtualMachineProfileResponse', ..., 'VirtualMachinePublicIPAddressConfigurationResponse', ..., 'VmSizeProfileResponse', 'WinRMConfigurationResponse', 'WinRMListenerResponse', 'WindowsConfigurationResponse', ..., 'ZoneAllocationPolicyResponse', 'ZonePreferenceResponse']
@pulumi.output_type
class AdditionalCapabilitiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hibernation_enabled: Optional[_builtins.bool] = ..., ultra_ssd_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationEnabled")
    def hibernation_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ultraSSDEnabled")
    def ultra_ssd_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AdditionalUnattendContentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_name: Optional[_builtins.str] = ..., content: Optional[_builtins.str] = ..., pass_name: Optional[_builtins.str] = ..., setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passName")
    def pass_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AllInstancesDownResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatically_approve: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticallyApprove")
    def automatically_approve(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApiEntityReferenceResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gallery_applications: Optional[Sequence[outputs.VMGalleryApplicationResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryApplications")
    def gallery_applications(self) -> Optional[Sequence[outputs.VMGalleryApplicationResponse]]:
        
        ...
    


@pulumi.output_type
class BootDiagnosticsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., storage_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapacityReservationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_group: Optional[outputs.SubResourceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroup")
    def capacity_reservation_group(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    


@pulumi.output_type
class ComputeProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, virtual_machine_profile: outputs.VirtualMachineProfileResponse, compute_api_version: Optional[_builtins.str] = ..., extensions: Optional[Sequence[outputs.VirtualMachineExtensionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> outputs.VirtualMachineProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeApiVersion")
    def compute_api_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[outputs.VirtualMachineExtensionResponse]]:
        
        ...
    


@pulumi.output_type
class DataDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_option: _builtins.str, lun: _builtins.int, caching: Optional[_builtins.str] = ..., delete_option: Optional[_builtins.str] = ..., detach_option: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., image: Optional[outputs.VirtualHardDiskResponse] = ..., managed_disk: Optional[outputs.ManagedDiskParametersResponse] = ..., name: Optional[_builtins.str] = ..., source_resource: Optional[outputs.ApiEntityReferenceResponse] = ..., to_be_detached: Optional[_builtins.bool] = ..., vhd: Optional[outputs.VirtualHardDiskResponse] = ..., write_accelerator_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> _builtins.str:
        
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
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detachOption")
    def detach_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.VirtualHardDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[outputs.ManagedDiskParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResource")
    def source_resource(self) -> Optional[outputs.ApiEntityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toBeDetached")
    def to_be_detached(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vhd(self) -> Optional[outputs.VirtualHardDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DiagnosticsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_diagnostics: Optional[outputs.BootDiagnosticsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiagnostics")
    def boot_diagnostics(self) -> Optional[outputs.BootDiagnosticsResponse]:
        
        ...
    


@pulumi.output_type
class DiffDiskSettingsResponse(dict):
    
    def __init__(__self__, *, option: Optional[_builtins.str] = ..., placement: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionSetParametersResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_key: Optional[outputs.KeyVaultSecretReferenceResponse] = ..., enabled: Optional[_builtins.bool] = ..., key_encryption_key: Optional[outputs.KeyVaultKeyReferenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[outputs.KeyVaultSecretReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[outputs.KeyVaultKeyReferenceResponse]:
        
        ...
    


@pulumi.output_type
class EncryptionIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_assigned_identity_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EventGridAndResourceGraphResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable: Optional[_builtins.bool] = ..., scheduled_events_api_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsApiVersion")
    def scheduled_events_api_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostEndpointSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, in_vm_access_control_profile_reference_id: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inVMAccessControlProfileReferenceId")
    def in_vm_access_control_profile_reference_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
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
class KeyVaultKeyReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_url: _builtins.str, source_vault: outputs.SubResourceResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> outputs.SubResourceResponse:
        
        ...
    


@pulumi.output_type
class KeyVaultSecretReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_url: _builtins.str, source_vault: outputs.SubResourceResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> outputs.SubResourceResponse:
        
        ...
    


@pulumi.output_type
class LaunchBulkInstancesOperationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity: _builtins.int, compute_profile: outputs.ComputeProfileResponse, priority_profile: outputs.PriorityProfileResponse, provisioning_state: _builtins.str, capacity_type: Optional[_builtins.str] = ..., retry_policy: Optional[outputs.RetryPolicyResponse] = ..., vm_attributes: Optional[outputs.VMAttributesResponse] = ..., vm_sizes_profile: Optional[Sequence[outputs.VmSizeProfileResponse]] = ..., zone_allocation_policy: Optional[outputs.ZoneAllocationPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> outputs.ComputeProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="priorityProfile")
    def priority_profile(self) -> outputs.PriorityProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RetryPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmAttributes")
    def vm_attributes(self) -> Optional[outputs.VMAttributesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSizesProfile")
    def vm_sizes_profile(self) -> Optional[Sequence[outputs.VmSizeProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneAllocationPolicy")
    def zone_allocation_policy(self) -> Optional[outputs.ZoneAllocationPolicyResponse]:
        
        ...
    


@pulumi.output_type
class LinuxConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_password_authentication: Optional[_builtins.bool] = ..., enable_vm_agent_platform_updates: Optional[_builtins.bool] = ..., patch_settings: Optional[outputs.LinuxPatchSettingsResponse] = ..., provision_vm_agent: Optional[_builtins.bool] = ..., ssh: Optional[outputs.SshConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disablePasswordAuthentication")
    def disable_password_authentication(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[outputs.LinuxPatchSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[outputs.SshConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class LinuxPatchSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_mode: Optional[_builtins.str] = ..., automatic_by_platform_settings: Optional[outputs.LinuxVMGuestPatchAutomaticByPlatformSettingsResponse] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(self) -> Optional[outputs.LinuxVMGuestPatchAutomaticByPlatformSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LinuxVMGuestPatchAutomaticByPlatformSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bypass_platform_safety_checks_on_user_schedule: Optional[_builtins.bool] = ..., reboot_setting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedDiskParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_set: Optional[outputs.DiskEncryptionSetParametersResponse] = ..., id: Optional[_builtins.str] = ..., security_profile: Optional[outputs.VMDiskSecurityProfileResponse] = ..., storage_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[outputs.DiskEncryptionSetParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
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
class NetworkInterfaceReferencePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_option: Optional[_builtins.str] = ..., primary: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class NetworkInterfaceReferenceResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., properties: Optional[outputs.NetworkInterfaceReferencePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.NetworkInterfaceReferencePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_api_version: Optional[_builtins.str] = ..., network_interface_configurations: Optional[Sequence[outputs.VirtualMachineNetworkInterfaceConfigurationResponse]] = ..., network_interfaces: Optional[Sequence[outputs.NetworkInterfaceReferenceResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkApiVersion")
    def network_api_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(self) -> Optional[Sequence[outputs.VirtualMachineNetworkInterfaceConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.NetworkInterfaceReferenceResponse]]:
        
        ...
    


@pulumi.output_type
class OSDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_option: _builtins.str, caching: Optional[_builtins.str] = ..., delete_option: Optional[_builtins.str] = ..., diff_disk_settings: Optional[outputs.DiffDiskSettingsResponse] = ..., disk_size_gb: Optional[_builtins.int] = ..., encryption_settings: Optional[outputs.DiskEncryptionSettingsResponse] = ..., image: Optional[outputs.VirtualHardDiskResponse] = ..., managed_disk: Optional[outputs.ManagedDiskParametersResponse] = ..., name: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., vhd: Optional[outputs.VirtualHardDiskResponse] = ..., write_accelerator_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diffDiskSettings")
    def diff_disk_settings(self) -> Optional[outputs.DiffDiskSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[outputs.DiskEncryptionSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.VirtualHardDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[outputs.ManagedDiskParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vhd(self) -> Optional[outputs.VirtualHardDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OSImageNotificationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable: Optional[_builtins.bool] = ..., not_before_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_password: Optional[_builtins.str] = ..., admin_username: Optional[_builtins.str] = ..., allow_extension_operations: Optional[_builtins.bool] = ..., computer_name: Optional[_builtins.str] = ..., custom_data: Optional[_builtins.str] = ..., linux_configuration: Optional[outputs.LinuxConfigurationResponse] = ..., require_guest_provision_signal: Optional[_builtins.bool] = ..., secrets: Optional[Sequence[outputs.VaultSecretGroupResponse]] = ..., windows_configuration: Optional[outputs.WindowsConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[outputs.LinuxConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireGuestProvisionSignal")
    def require_guest_provision_signal(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.VaultSecretGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[outputs.WindowsConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class PatchSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_mode: Optional[_builtins.str] = ..., automatic_by_platform_settings: Optional[outputs.WindowsVMGuestPatchAutomaticByPlatformSettingsResponse] = ..., enable_hotpatching: Optional[_builtins.bool] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(self) -> Optional[outputs.WindowsVMGuestPatchAutomaticByPlatformSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, product: _builtins.str, publisher: _builtins.str, promotion_code: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PriorityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_strategy: Optional[_builtins.str] = ..., eviction_policy: Optional[_builtins.str] = ..., max_price_per_vm: Optional[_builtins.float] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPricePerVM")
    def max_price_per_vm(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProxyAgentSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, add_proxy_agent_extension: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., imds: Optional[outputs.HostEndpointSettingsResponse] = ..., key_incarnation_id: Optional[_builtins.int] = ..., mode: Optional[_builtins.str] = ..., wire_server: Optional[outputs.HostEndpointSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addProxyAgentExtension")
    def add_proxy_agent_extension(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def imds(self) -> Optional[outputs.HostEndpointSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyIncarnationId")
    def key_incarnation_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wireServer")
    def wire_server(self) -> Optional[outputs.HostEndpointSettingsResponse]:
        
        ...
    


@pulumi.output_type
class PublicIPAddressSkuResponse(dict):
    
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
class RetryPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retry_count: Optional[_builtins.int] = ..., retry_window_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryWindowInMinutes")
    def retry_window_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ScheduledEventsAdditionalPublishingTargetsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_grid_and_resource_graph: Optional[outputs.EventGridAndResourceGraphResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventGridAndResourceGraph")
    def event_grid_and_resource_graph(self) -> Optional[outputs.EventGridAndResourceGraphResponse]:
        
        ...
    


@pulumi.output_type
class ScheduledEventsPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_instances_down: Optional[outputs.AllInstancesDownResponse] = ..., scheduled_events_additional_publishing_targets: Optional[outputs.ScheduledEventsAdditionalPublishingTargetsResponse] = ..., user_initiated_reboot: Optional[outputs.UserInitiatedRebootResponse] = ..., user_initiated_redeploy: Optional[outputs.UserInitiatedRedeployResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allInstancesDown")
    def all_instances_down(self) -> Optional[outputs.AllInstancesDownResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsAdditionalPublishingTargets")
    def scheduled_events_additional_publishing_targets(self) -> Optional[outputs.ScheduledEventsAdditionalPublishingTargetsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInitiatedReboot")
    def user_initiated_reboot(self) -> Optional[outputs.UserInitiatedRebootResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInitiatedRedeploy")
    def user_initiated_redeploy(self) -> Optional[outputs.UserInitiatedRedeployResponse]:
        
        ...
    


@pulumi.output_type
class ScheduledEventsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_image_notification_profile: Optional[outputs.OSImageNotificationProfileResponse] = ..., terminate_notification_profile: Optional[outputs.TerminateNotificationProfileResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osImageNotificationProfile")
    def os_image_notification_profile(self) -> Optional[outputs.OSImageNotificationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateNotificationProfile")
    def terminate_notification_profile(self) -> Optional[outputs.TerminateNotificationProfileResponse]:
        
        ...
    


@pulumi.output_type
class SecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_at_host: Optional[_builtins.bool] = ..., encryption_identity: Optional[outputs.EncryptionIdentityResponse] = ..., proxy_agent_settings: Optional[outputs.ProxyAgentSettingsResponse] = ..., security_type: Optional[_builtins.str] = ..., uefi_settings: Optional[outputs.UefiSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[outputs.EncryptionIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyAgentSettings")
    def proxy_agent_settings(self) -> Optional[outputs.ProxyAgentSettingsResponse]:
        
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
class SshConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, public_keys: Optional[Sequence[outputs.SshPublicKeyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[Sequence[outputs.SshPublicKeyResponse]]:
        
        ...
    


@pulumi.output_type
class SshPublicKeyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_data: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_disks: Optional[Sequence[outputs.DataDiskResponse]] = ..., disk_controller_type: Optional[_builtins.str] = ..., image_reference: Optional[outputs.ImageReferenceResponse] = ..., os_disk: Optional[outputs.OSDiskResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[Sequence[outputs.DataDiskResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskControllerType")
    def disk_controller_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[outputs.ImageReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[outputs.OSDiskResponse]:
        
        ...
    


@pulumi.output_type
class SubResourceResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
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
class TerminateNotificationProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable: Optional[_builtins.bool] = ..., not_before_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[_builtins.str]:
        
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
class UserInitiatedRebootResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatically_approve: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticallyApprove")
    def automatically_approve(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UserInitiatedRedeployResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatically_approve: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticallyApprove")
    def automatically_approve(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VMAttributeMinMaxDoubleResponse(dict):
    
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class VMAttributeMinMaxIntegerResponse(dict):
    
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VMAttributesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, architecture_types: Sequence[_builtins.str], memory_in_gi_b: outputs.VMAttributeMinMaxDoubleResponse, v_cpu_count: outputs.VMAttributeMinMaxIntegerResponse, accelerator_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_support: Optional[_builtins.str] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_vm_sizes: Optional[Sequence[_builtins.str]] = ..., burstable_support: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., data_disk_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ..., excluded_vm_sizes: Optional[Sequence[_builtins.str]] = ..., hyper_v_generations: Optional[Sequence[_builtins.str]] = ..., local_storage_disk_types: Optional[Sequence[_builtins.str]] = ..., local_storage_in_gi_b: Optional[outputs.VMAttributeMinMaxDoubleResponse] = ..., local_storage_support: Optional[_builtins.str] = ..., memory_in_gi_b_per_v_cpu: Optional[outputs.VMAttributeMinMaxDoubleResponse] = ..., network_bandwidth_in_mbps: Optional[outputs.VMAttributeMinMaxDoubleResponse] = ..., network_interface_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ..., rdma_network_interface_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ..., rdma_support: Optional[_builtins.str] = ..., vm_categories: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="architectureTypes")
    def architecture_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInGiB")
    def memory_in_gi_b(self) -> outputs.VMAttributeMinMaxDoubleResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCpuCount")
    def v_cpu_count(self) -> outputs.VMAttributeMinMaxIntegerResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorSupport")
    def accelerator_support(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedVMSizes")
    def allowed_vm_sizes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstableSupport")
    def burstable_support(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskCount")
    def data_disk_count(self) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedVMSizes")
    def excluded_vm_sizes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVGenerations")
    def hyper_v_generations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageDiskTypes")
    def local_storage_disk_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageInGiB")
    def local_storage_in_gi_b(self) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageSupport")
    def local_storage_support(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInGiBPerVCpu")
    def memory_in_gi_b_per_v_cpu(self) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthInMbps")
    def network_bandwidth_in_mbps(self) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdmaNetworkInterfaceCount")
    def rdma_network_interface_count(self) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdmaSupport")
    def rdma_support(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCategories")
    def vm_categories(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VMDiskSecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_set: Optional[outputs.DiskEncryptionSetParametersResponse] = ..., security_encryption_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[outputs.DiskEncryptionSetParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMGalleryApplicationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, package_reference_id: _builtins.str, configuration_reference: Optional[_builtins.str] = ..., enable_automatic_upgrade: Optional[_builtins.bool] = ..., order: Optional[_builtins.int] = ..., tags: Optional[_builtins.str] = ..., treat_failure_as_deployment_failure: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageReferenceId")
    def package_reference_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationReference")
    def configuration_reference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VaultCertificateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_store: Optional[_builtins.str] = ..., certificate_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VaultSecretGroupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_vault: Optional[outputs.SubResourceResponse] = ..., vault_certificates: Optional[Sequence[outputs.VaultCertificateResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(self) -> Optional[Sequence[outputs.VaultCertificateResponse]]:
        
        ...
    


@pulumi.output_type
class VirtualHardDiskResponse(dict):
    
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineExtensionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_upgrade_minor_version: Optional[_builtins.bool] = ..., enable_automatic_upgrade: Optional[_builtins.bool] = ..., force_update_tag: Optional[_builtins.str] = ..., protected_settings: Optional[Any] = ..., protected_settings_from_key_vault: Optional[outputs.KeyVaultSecretReferenceResponse] = ..., provision_after_extensions: Optional[Sequence[_builtins.str]] = ..., publisher: Optional[_builtins.str] = ..., settings: Optional[Any] = ..., suppress_failures: Optional[_builtins.bool] = ..., type: Optional[_builtins.str] = ..., type_handler_version: Optional[_builtins.str] = ...) -> None:
        
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
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(self) -> Optional[outputs.KeyVaultSecretReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineExtensionResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, properties: outputs.VirtualMachineExtensionPropertiesResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.VirtualMachineExtensionPropertiesResponse:
        
        ...
    


@pulumi.output_type
class VirtualMachineIpTagResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_tag_type: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineNetworkInterfaceConfigurationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_configurations: Sequence[outputs.VirtualMachineNetworkInterfaceIPConfigurationResponse], auxiliary_mode: Optional[_builtins.str] = ..., auxiliary_sku: Optional[_builtins.str] = ..., delete_option: Optional[_builtins.str] = ..., disable_tcp_state_tracking: Optional[_builtins.bool] = ..., dns_settings: Optional[outputs.VirtualMachineNetworkInterfaceDnsSettingsConfigurationResponse] = ..., dscp_configuration: Optional[outputs.SubResourceResponse] = ..., enable_accelerated_networking: Optional[_builtins.bool] = ..., enable_fpga: Optional[_builtins.bool] = ..., enable_ip_forwarding: Optional[_builtins.bool] = ..., network_security_group: Optional[outputs.SubResourceResponse] = ..., primary: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.VirtualMachineNetworkInterfaceIPConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[outputs.VirtualMachineNetworkInterfaceDnsSettingsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dscpConfiguration")
    def dscp_configuration(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFpga")
    def enable_fpga(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VirtualMachineNetworkInterfaceConfigurationResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, properties: Optional[outputs.VirtualMachineNetworkInterfaceConfigurationPropertiesResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.VirtualMachineNetworkInterfaceConfigurationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class VirtualMachineNetworkInterfaceDnsSettingsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_servers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VirtualMachineNetworkInterfaceIPConfigurationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_gateway_backend_address_pools: Optional[Sequence[outputs.SubResourceResponse]] = ..., application_security_groups: Optional[Sequence[outputs.SubResourceResponse]] = ..., load_balancer_backend_address_pools: Optional[Sequence[outputs.SubResourceResponse]] = ..., primary: Optional[_builtins.bool] = ..., private_ip_address_version: Optional[_builtins.str] = ..., public_ip_address_configuration: Optional[outputs.VirtualMachinePublicIPAddressConfigurationResponse] = ..., subnet: Optional[outputs.SubResourceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(self) -> Optional[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(self) -> Optional[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(self) -> Optional[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(self) -> Optional[outputs.VirtualMachinePublicIPAddressConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    


@pulumi.output_type
class VirtualMachineNetworkInterfaceIPConfigurationResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, properties: Optional[outputs.VirtualMachineNetworkInterfaceIPConfigurationPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.VirtualMachineNetworkInterfaceIPConfigurationPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class VirtualMachineProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_capabilities: Optional[outputs.AdditionalCapabilitiesResponse] = ..., application_profile: Optional[outputs.ApplicationProfileResponse] = ..., capacity_reservation: Optional[outputs.CapacityReservationProfileResponse] = ..., diagnostics_profile: Optional[outputs.DiagnosticsProfileResponse] = ..., extensions_time_budget: Optional[_builtins.str] = ..., license_type: Optional[_builtins.str] = ..., network_profile: Optional[outputs.NetworkProfileResponse] = ..., os_profile: Optional[outputs.OSProfileResponse] = ..., scheduled_events_policy: Optional[outputs.ScheduledEventsPolicyResponse] = ..., scheduled_events_profile: Optional[outputs.ScheduledEventsProfileResponse] = ..., security_profile: Optional[outputs.SecurityProfileResponse] = ..., storage_profile: Optional[outputs.StorageProfileResponse] = ..., user_data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[outputs.AdditionalCapabilitiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[outputs.ApplicationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(self) -> Optional[outputs.CapacityReservationProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[outputs.DiagnosticsProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OSProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(self) -> Optional[outputs.ScheduledEventsPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(self) -> Optional[outputs.ScheduledEventsProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachinePublicIPAddressConfigurationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_option: Optional[_builtins.str] = ..., dns_settings: Optional[outputs.VirtualMachinePublicIPAddressDnsSettingsConfigurationResponse] = ..., idle_timeout_in_minutes: Optional[_builtins.int] = ..., ip_tags: Optional[Sequence[outputs.VirtualMachineIpTagResponse]] = ..., public_ip_address_version: Optional[_builtins.str] = ..., public_ip_allocation_method: Optional[_builtins.str] = ..., public_ip_prefix: Optional[outputs.SubResourceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[outputs.VirtualMachinePublicIPAddressDnsSettingsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[Sequence[outputs.VirtualMachineIpTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    


@pulumi.output_type
class VirtualMachinePublicIPAddressConfigurationResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, properties: Optional[outputs.VirtualMachinePublicIPAddressConfigurationPropertiesResponse] = ..., sku: Optional[outputs.PublicIPAddressSkuResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.VirtualMachinePublicIPAddressConfigurationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.PublicIPAddressSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class VirtualMachinePublicIPAddressDnsSettingsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name_label: _builtins.str, domain_name_label_scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabelScope")
    def domain_name_label_scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmSizeProfileResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, rank: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WinRMConfigurationResponse(dict):
    
    def __init__(__self__, *, listeners: Optional[Sequence[outputs.WinRMListenerResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Optional[Sequence[outputs.WinRMListenerResponse]]:
        
        ...
    


@pulumi.output_type
class WinRMListenerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_url: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WindowsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_unattend_content: Optional[Sequence[outputs.AdditionalUnattendContentResponse]] = ..., enable_automatic_updates: Optional[_builtins.bool] = ..., patch_settings: Optional[outputs.PatchSettingsResponse] = ..., provision_vm_agent: Optional[_builtins.bool] = ..., time_zone: Optional[_builtins.str] = ..., win_rm: Optional[outputs.WinRMConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalUnattendContent")
    def additional_unattend_content(self) -> Optional[Sequence[outputs.AdditionalUnattendContentResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[outputs.PatchSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="winRM")
    def win_rm(self) -> Optional[outputs.WinRMConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class WindowsVMGuestPatchAutomaticByPlatformSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bypass_platform_safety_checks_on_user_schedule: Optional[_builtins.bool] = ..., reboot_setting: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ZoneAllocationPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, distribution_strategy: _builtins.str, zone_preferences: Optional[Sequence[outputs.ZonePreferenceResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionStrategy")
    def distribution_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonePreferences")
    def zone_preferences(self) -> Optional[Sequence[outputs.ZonePreferenceResponse]]:
        
        ...
    


@pulumi.output_type
class ZonePreferenceResponse(dict):
    
    def __init__(__self__, *, zone: _builtins.str, rank: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    


