import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalCapabilitiesResponse",
    "AdditionalLocationsProfileResponse",
    "AdditionalUnattendContentResponse",
    "ApiEntityReferenceResponse",
    "ApplicationProfileResponse",
    "BaseVirtualMachineProfileResponse",
    "BootDiagnosticsResponse",
    "CapacityReservationProfileResponse",
    "ComputeProfileResponse",
    "DiagnosticsProfileResponse",
    "DiffDiskSettingsResponse",
    "DiskEncryptionSetParametersResponse",
    "EncryptionIdentityResponse",
    "ImageReferenceResponse",
    "KeyVaultSecretReferenceResponse",
    "LinuxConfigurationResponse",
    "LinuxPatchSettingsResponse",
    ...,
    "LocationProfileResponse",
    "ManagedServiceIdentityResponse",
    "OSImageNotificationProfileResponse",
    "PatchSettingsResponse",
    "PlanResponse",
    "ProxyAgentSettingsResponse",
    "PublicIPAddressSkuResponse",
    "RegularPriorityProfileResponse",
    "ScheduledEventsProfileResponse",
    "SecurityPostureReferenceResponse",
    "SecurityProfileResponse",
    "ServiceArtifactReferenceResponse",
    "SpotPriorityProfileResponse",
    "SshConfigurationResponse",
    "SshPublicKeyResponse",
    "SubResourceResponse",
    "SystemDataResponse",
    "TerminateNotificationProfileResponse",
    "UefiSettingsResponse",
    "UserAssignedIdentityResponse",
    "VMAttributeMinMaxDoubleResponse",
    "VMAttributeMinMaxIntegerResponse",
    "VMAttributesResponse",
    "VMDiskSecurityProfileResponse",
    "VMGalleryApplicationResponse",
    "VMSizePropertiesResponse",
    "VaultCertificateResponse",
    "VaultSecretGroupResponse",
    "VirtualHardDiskResponse",
    "VirtualMachineScaleSetDataDiskResponse",
    "VirtualMachineScaleSetExtensionProfileResponse",
    "VirtualMachineScaleSetExtensionPropertiesResponse",
    "VirtualMachineScaleSetExtensionResponse",
    "VirtualMachineScaleSetHardwareProfileResponse",
    ...,
    "VirtualMachineScaleSetIPConfigurationResponse",
    "VirtualMachineScaleSetIpTagResponse",
    ...,
    ...,
    ...,
    "VirtualMachineScaleSetNetworkConfigurationResponse",
    "VirtualMachineScaleSetNetworkProfileResponse",
    "VirtualMachineScaleSetOSDiskResponse",
    "VirtualMachineScaleSetOSProfileResponse",
    ...,
    ...,
    ...,
    "VirtualMachineScaleSetStorageProfileResponse",
    "VmSizeProfileResponse",
    "WinRMConfigurationResponse",
    "WinRMListenerResponse",
    "WindowsConfigurationResponse",
    ...,
]

@pulumi.output_type
class AdditionalCapabilitiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hibernation_enabled: Optional[_builtins.bool] = ...,
        ultra_ssd_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hibernationEnabled")
    def hibernation_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ultraSSDEnabled")
    def ultra_ssd_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AdditionalLocationsProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, location_profiles: Sequence[outputs.LocationProfileResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationProfiles")
    def location_profiles(self) -> Sequence[outputs.LocationProfileResponse]: ...

@pulumi.output_type
class AdditionalUnattendContentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_name: Optional[_builtins.str] = ...,
        pass_name: Optional[_builtins.str] = ...,
        setting_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passName")
    def pass_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiEntityReferenceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gallery_applications: Optional[
            Sequence[outputs.VMGalleryApplicationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryApplications")
    def gallery_applications(
        self,
    ) -> Optional[Sequence[outputs.VMGalleryApplicationResponse]]: ...

@pulumi.output_type
class BaseVirtualMachineProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        time_created: _builtins.str,
        application_profile: Optional[outputs.ApplicationProfileResponse] = ...,
        capacity_reservation: Optional[
            outputs.CapacityReservationProfileResponse
        ] = ...,
        diagnostics_profile: Optional[outputs.DiagnosticsProfileResponse] = ...,
        extension_profile: Optional[
            outputs.VirtualMachineScaleSetExtensionProfileResponse
        ] = ...,
        hardware_profile: Optional[
            outputs.VirtualMachineScaleSetHardwareProfileResponse
        ] = ...,
        license_type: Optional[_builtins.str] = ...,
        network_profile: Optional[
            outputs.VirtualMachineScaleSetNetworkProfileResponse
        ] = ...,
        os_profile: Optional[outputs.VirtualMachineScaleSetOSProfileResponse] = ...,
        scheduled_events_profile: Optional[
            outputs.ScheduledEventsProfileResponse
        ] = ...,
        security_posture_reference: Optional[
            outputs.SecurityPostureReferenceResponse
        ] = ...,
        security_profile: Optional[outputs.SecurityProfileResponse] = ...,
        service_artifact_reference: Optional[
            outputs.ServiceArtifactReferenceResponse
        ] = ...,
        storage_profile: Optional[
            outputs.VirtualMachineScaleSetStorageProfileResponse
        ] = ...,
        user_data: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[outputs.ApplicationProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(
        self,
    ) -> Optional[outputs.CapacityReservationProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[outputs.DiagnosticsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="extensionProfile")
    def extension_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetExtensionProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetHardwareProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetNetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetOSProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(
        self,
    ) -> Optional[outputs.ScheduledEventsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityPostureReference")
    def security_posture_reference(
        self,
    ) -> Optional[outputs.SecurityPostureReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReference")
    def service_artifact_reference(
        self,
    ) -> Optional[outputs.ServiceArtifactReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetStorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BootDiagnosticsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        storage_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CapacityReservationProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_reservation_group: Optional[outputs.SubResourceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroup")
    def capacity_reservation_group(self) -> Optional[outputs.SubResourceResponse]: ...

@pulumi.output_type
class ComputeProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_virtual_machine_profile: outputs.BaseVirtualMachineProfileResponse,
        additional_virtual_machine_capabilities: Optional[
            outputs.AdditionalCapabilitiesResponse
        ] = ...,
        compute_api_version: Optional[_builtins.str] = ...,
        platform_fault_domain_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseVirtualMachineProfile")
    def base_virtual_machine_profile(
        self,
    ) -> outputs.BaseVirtualMachineProfileResponse: ...
    @_builtins.property
    @pulumi.getter(name="additionalVirtualMachineCapabilities")
    def additional_virtual_machine_capabilities(
        self,
    ) -> Optional[outputs.AdditionalCapabilitiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="computeApiVersion")
    def compute_api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DiagnosticsProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, boot_diagnostics: Optional[outputs.BootDiagnosticsResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiagnostics")
    def boot_diagnostics(self) -> Optional[outputs.BootDiagnosticsResponse]: ...

@pulumi.output_type
class DiffDiskSettingsResponse(dict):
    def __init__(
        __self__,
        *,
        option: Optional[_builtins.str] = ...,
        placement: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiskEncryptionSetParametersResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EncryptionIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, user_assigned_identity_resource_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exact_version: _builtins.str,
        community_gallery_image_id: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        offer: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
        shared_gallery_image_id: Optional[_builtins.str] = ...,
        sku: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultSecretReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_url: _builtins.str,
        source_vault: outputs.SubResourceResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> outputs.SubResourceResponse: ...

@pulumi.output_type
class LinuxConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_password_authentication: Optional[_builtins.bool] = ...,
        enable_vm_agent_platform_updates: Optional[_builtins.bool] = ...,
        patch_settings: Optional[outputs.LinuxPatchSettingsResponse] = ...,
        provision_vm_agent: Optional[_builtins.bool] = ...,
        ssh: Optional[outputs.SshConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disablePasswordAuthentication")
    def disable_password_authentication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[outputs.LinuxPatchSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[outputs.SshConfigurationResponse]: ...

@pulumi.output_type
class LinuxPatchSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assessment_mode: Optional[_builtins.str] = ...,
        automatic_by_platform_settings: Optional[
            outputs.LinuxVMGuestPatchAutomaticByPlatformSettingsResponse
        ] = ...,
        patch_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(
        self,
    ) -> Optional[outputs.LinuxVMGuestPatchAutomaticByPlatformSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinuxVMGuestPatchAutomaticByPlatformSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bypass_platform_safety_checks_on_user_schedule: Optional[_builtins.bool] = ...,
        reboot_setting: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        virtual_machine_profile_override: Optional[
            outputs.BaseVirtualMachineProfileResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfileOverride")
    def virtual_machine_profile_override(
        self,
    ) -> Optional[outputs.BaseVirtualMachineProfileResponse]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class OSImageNotificationProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        not_before_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PatchSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assessment_mode: Optional[_builtins.str] = ...,
        automatic_by_platform_settings: Optional[
            outputs.WindowsVMGuestPatchAutomaticByPlatformSettingsResponse
        ] = ...,
        enable_hotpatching: Optional[_builtins.bool] = ...,
        patch_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(
        self,
    ) -> Optional[outputs.WindowsVMGuestPatchAutomaticByPlatformSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        product: _builtins.str,
        publisher: _builtins.str,
        promotion_code: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProxyAgentSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        key_incarnation_id: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyIncarnationId")
    def key_incarnation_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PublicIPAddressSkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegularPriorityProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[_builtins.str] = ...,
        capacity: Optional[_builtins.int] = ...,
        min_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledEventsProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_image_notification_profile: Optional[
            outputs.OSImageNotificationProfileResponse
        ] = ...,
        terminate_notification_profile: Optional[
            outputs.TerminateNotificationProfileResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osImageNotificationProfile")
    def os_image_notification_profile(
        self,
    ) -> Optional[outputs.OSImageNotificationProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="terminateNotificationProfile")
    def terminate_notification_profile(
        self,
    ) -> Optional[outputs.TerminateNotificationProfileResponse]: ...

@pulumi.output_type
class SecurityPostureReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclude_extensions: Optional[Sequence[_builtins.str]] = ...,
        id: Optional[_builtins.str] = ...,
        is_overridable: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeExtensions")
    def exclude_extensions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isOverridable")
    def is_overridable(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SecurityProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_at_host: Optional[_builtins.bool] = ...,
        encryption_identity: Optional[outputs.EncryptionIdentityResponse] = ...,
        proxy_agent_settings: Optional[outputs.ProxyAgentSettingsResponse] = ...,
        security_type: Optional[_builtins.str] = ...,
        uefi_settings: Optional[outputs.UefiSettingsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[outputs.EncryptionIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="proxyAgentSettings")
    def proxy_agent_settings(self) -> Optional[outputs.ProxyAgentSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[outputs.UefiSettingsResponse]: ...

@pulumi.output_type
class ServiceArtifactReferenceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpotPriorityProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[_builtins.str] = ...,
        capacity: Optional[_builtins.int] = ...,
        eviction_policy: Optional[_builtins.str] = ...,
        maintain: Optional[_builtins.bool] = ...,
        max_price_per_vm: Optional[_builtins.float] = ...,
        min_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def maintain(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxPricePerVM")
    def max_price_per_vm(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SshConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, public_keys: Optional[Sequence[outputs.SshPublicKeyResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[Sequence[outputs.SshPublicKeyResponse]]: ...

@pulumi.output_type
class SshPublicKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_data: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubResourceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TerminateNotificationProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        not_before_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UefiSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secure_boot_enabled: Optional[_builtins.bool] = ...,
        v_tpm_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vTpmEnabled")
    def v_tpm_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class VMAttributeMinMaxDoubleResponse(dict):
    def __init__(
        __self__,
        *,
        max: Optional[_builtins.float] = ...,
        min: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class VMAttributeMinMaxIntegerResponse(dict):
    def __init__(
        __self__,
        *,
        max: Optional[_builtins.int] = ...,
        min: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VMAttributesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        memory_in_gi_b: outputs.VMAttributeMinMaxDoubleResponse,
        v_cpu_count: outputs.VMAttributeMinMaxIntegerResponse,
        accelerator_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ...,
        accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ...,
        accelerator_support: Optional[_builtins.str] = ...,
        accelerator_types: Optional[Sequence[_builtins.str]] = ...,
        architecture_types: Optional[Sequence[_builtins.str]] = ...,
        burstable_support: Optional[_builtins.str] = ...,
        cpu_manufacturers: Optional[Sequence[_builtins.str]] = ...,
        data_disk_count: Optional[outputs.VMAttributeMinMaxIntegerResponse] = ...,
        excluded_vm_sizes: Optional[Sequence[_builtins.str]] = ...,
        local_storage_disk_types: Optional[Sequence[_builtins.str]] = ...,
        local_storage_in_gi_b: Optional[outputs.VMAttributeMinMaxDoubleResponse] = ...,
        local_storage_support: Optional[_builtins.str] = ...,
        memory_in_gi_b_per_v_cpu: Optional[
            outputs.VMAttributeMinMaxDoubleResponse
        ] = ...,
        network_bandwidth_in_mbps: Optional[
            outputs.VMAttributeMinMaxDoubleResponse
        ] = ...,
        network_interface_count: Optional[
            outputs.VMAttributeMinMaxIntegerResponse
        ] = ...,
        rdma_network_interface_count: Optional[
            outputs.VMAttributeMinMaxIntegerResponse
        ] = ...,
        rdma_support: Optional[_builtins.str] = ...,
        vm_categories: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGiB")
    def memory_in_gi_b(self) -> outputs.VMAttributeMinMaxDoubleResponse: ...
    @_builtins.property
    @pulumi.getter(name="vCpuCount")
    def v_cpu_count(self) -> outputs.VMAttributeMinMaxIntegerResponse: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorSupport")
    def accelerator_support(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="architectureTypes")
    def architecture_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="burstableSupport")
    def burstable_support(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskCount")
    def data_disk_count(self) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="excludedVMSizes")
    def excluded_vm_sizes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localStorageDiskTypes")
    def local_storage_disk_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localStorageInGiB")
    def local_storage_in_gi_b(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="localStorageSupport")
    def local_storage_support(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGiBPerVCpu")
    def memory_in_gi_b_per_v_cpu(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkBandwidthInMbps")
    def network_bandwidth_in_mbps(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxDoubleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rdmaNetworkInterfaceCount")
    def rdma_network_interface_count(
        self,
    ) -> Optional[outputs.VMAttributeMinMaxIntegerResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rdmaSupport")
    def rdma_support(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmCategories")
    def vm_categories(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class VMDiskSecurityProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_encryption_set: Optional[
            outputs.DiskEncryptionSetParametersResponse
        ] = ...,
        security_encryption_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(
        self,
    ) -> Optional[outputs.DiskEncryptionSetParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VMGalleryApplicationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        package_reference_id: _builtins.str,
        configuration_reference: Optional[_builtins.str] = ...,
        enable_automatic_upgrade: Optional[_builtins.bool] = ...,
        order: Optional[_builtins.int] = ...,
        tags: Optional[_builtins.str] = ...,
        treat_failure_as_deployment_failure: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageReferenceId")
    def package_reference_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationReference")
    def configuration_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class VMSizePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        v_cpus_available: Optional[_builtins.int] = ...,
        v_cpus_per_core: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vCPUsAvailable")
    def v_cpus_available(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vCPUsPerCore")
    def v_cpus_per_core(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VaultCertificateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_store: Optional[_builtins.str] = ...,
        certificate_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VaultSecretGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_vault: Optional[outputs.SubResourceResponse] = ...,
        vault_certificates: Optional[Sequence[outputs.VaultCertificateResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(
        self,
    ) -> Optional[Sequence[outputs.VaultCertificateResponse]]: ...

@pulumi.output_type
class VirtualHardDiskResponse(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetDataDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_option: _builtins.str,
        lun: _builtins.int,
        caching: Optional[_builtins.str] = ...,
        delete_option: Optional[_builtins.str] = ...,
        disk_iops_read_write: Optional[_builtins.float] = ...,
        disk_m_bps_read_write: Optional[_builtins.float] = ...,
        disk_size_gb: Optional[_builtins.int] = ...,
        managed_disk: Optional[
            outputs.VirtualMachineScaleSetManagedDiskParametersResponse
        ] = ...,
        name: Optional[_builtins.str] = ...,
        write_accelerator_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetManagedDiskParametersResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class VirtualMachineScaleSetExtensionProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extensions: Optional[
            Sequence[outputs.VirtualMachineScaleSetExtensionResponse]
        ] = ...,
        extensions_time_budget: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineScaleSetExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetExtensionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        auto_upgrade_minor_version: Optional[_builtins.bool] = ...,
        enable_automatic_upgrade: Optional[_builtins.bool] = ...,
        force_update_tag: Optional[_builtins.str] = ...,
        protected_settings_from_key_vault: Optional[
            outputs.KeyVaultSecretReferenceResponse
        ] = ...,
        provision_after_extensions: Optional[Sequence[_builtins.str]] = ...,
        publisher: Optional[_builtins.str] = ...,
        settings: Optional[Any] = ...,
        suppress_failures: Optional[_builtins.bool] = ...,
        type: Optional[_builtins.str] = ...,
        type_handler_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(
        self,
    ) -> Optional[outputs.KeyVaultSecretReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetExtensionResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        properties: Optional[
            outputs.VirtualMachineScaleSetExtensionPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetExtensionPropertiesResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetHardwareProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vm_size_properties: Optional[outputs.VMSizePropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmSizeProperties")
    def vm_size_properties(self) -> Optional[outputs.VMSizePropertiesResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetIPConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_gateway_backend_address_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        application_security_groups: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        load_balancer_backend_address_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        load_balancer_inbound_nat_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        primary: Optional[_builtins.bool] = ...,
        private_ip_address_version: Optional[_builtins.str] = ...,
        public_ip_address_configuration: Optional[
            outputs.VirtualMachineScaleSetPublicIPAddressConfigurationResponse
        ] = ...,
        subnet: Optional[outputs.ApiEntityReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPools")
    def load_balancer_inbound_nat_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetPublicIPAddressConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.ApiEntityReferenceResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetIPConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        properties: Optional[
            outputs.VirtualMachineScaleSetIPConfigurationPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetIPConfigurationPropertiesResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetIpTagResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_tag_type: Optional[_builtins.str] = ...,
        tag: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetManagedDiskParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_encryption_set: Optional[
            outputs.DiskEncryptionSetParametersResponse
        ] = ...,
        security_profile: Optional[outputs.VMDiskSecurityProfileResponse] = ...,
        storage_account_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(
        self,
    ) -> Optional[outputs.DiskEncryptionSetParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.VMDiskSecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetNetworkConfigurationDnsSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dns_servers: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class VirtualMachineScaleSetNetworkConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_configurations: Sequence[
            outputs.VirtualMachineScaleSetIPConfigurationResponse
        ],
        auxiliary_mode: Optional[_builtins.str] = ...,
        auxiliary_sku: Optional[_builtins.str] = ...,
        delete_option: Optional[_builtins.str] = ...,
        disable_tcp_state_tracking: Optional[_builtins.bool] = ...,
        dns_settings: Optional[
            outputs.VirtualMachineScaleSetNetworkConfigurationDnsSettingsResponse
        ] = ...,
        enable_accelerated_networking: Optional[_builtins.bool] = ...,
        enable_fpga: Optional[_builtins.bool] = ...,
        enable_ip_forwarding: Optional[_builtins.bool] = ...,
        network_security_group: Optional[outputs.SubResourceResponse] = ...,
        primary: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Sequence[outputs.VirtualMachineScaleSetIPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetNetworkConfigurationDnsSettingsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableFpga")
    def enable_fpga(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class VirtualMachineScaleSetNetworkConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        properties: Optional[
            outputs.VirtualMachineScaleSetNetworkConfigurationPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetNetworkConfigurationPropertiesResponse
    ]: ...

@pulumi.output_type
class VirtualMachineScaleSetNetworkProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        health_probe: Optional[outputs.ApiEntityReferenceResponse] = ...,
        network_api_version: Optional[_builtins.str] = ...,
        network_interface_configurations: Optional[
            Sequence[outputs.VirtualMachineScaleSetNetworkConfigurationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthProbe")
    def health_probe(self) -> Optional[outputs.ApiEntityReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkApiVersion")
    def network_api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.VirtualMachineScaleSetNetworkConfigurationResponse]
    ]: ...

@pulumi.output_type
class VirtualMachineScaleSetOSDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_option: _builtins.str,
        caching: Optional[_builtins.str] = ...,
        delete_option: Optional[_builtins.str] = ...,
        diff_disk_settings: Optional[outputs.DiffDiskSettingsResponse] = ...,
        disk_size_gb: Optional[_builtins.int] = ...,
        image: Optional[outputs.VirtualHardDiskResponse] = ...,
        managed_disk: Optional[
            outputs.VirtualMachineScaleSetManagedDiskParametersResponse
        ] = ...,
        name: Optional[_builtins.str] = ...,
        os_type: Optional[_builtins.str] = ...,
        vhd_containers: Optional[Sequence[_builtins.str]] = ...,
        write_accelerator_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diffDiskSettings")
    def diff_disk_settings(self) -> Optional[outputs.DiffDiskSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.VirtualHardDiskResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetManagedDiskParametersResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vhdContainers")
    def vhd_containers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class VirtualMachineScaleSetOSProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_username: Optional[_builtins.str] = ...,
        allow_extension_operations: Optional[_builtins.bool] = ...,
        computer_name_prefix: Optional[_builtins.str] = ...,
        linux_configuration: Optional[outputs.LinuxConfigurationResponse] = ...,
        require_guest_provision_signal: Optional[_builtins.bool] = ...,
        secrets: Optional[Sequence[outputs.VaultSecretGroupResponse]] = ...,
        windows_configuration: Optional[outputs.WindowsConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[outputs.LinuxConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="requireGuestProvisionSignal")
    def require_guest_provision_signal(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.VaultSecretGroupResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(
        self,
    ) -> Optional[outputs.WindowsConfigurationResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name_label: _builtins.str,
        domain_name_label_scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainNameLabelScope")
    def domain_name_label_scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delete_option: Optional[_builtins.str] = ...,
        dns_settings: Optional[
            outputs.VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsResponse
        ] = ...,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        ip_tags: Optional[Sequence[outputs.VirtualMachineScaleSetIpTagResponse]] = ...,
        public_ip_address_version: Optional[_builtins.str] = ...,
        public_ip_prefix: Optional[outputs.SubResourceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineScaleSetIpTagResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[outputs.SubResourceResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetPublicIPAddressConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        properties: Optional[
            outputs.VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesResponse
        ] = ...,
        sku: Optional[outputs.PublicIPAddressSkuResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        outputs.VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesResponse
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.PublicIPAddressSkuResponse]: ...

@pulumi.output_type
class VirtualMachineScaleSetStorageProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_disks: Optional[
            Sequence[outputs.VirtualMachineScaleSetDataDiskResponse]
        ] = ...,
        disk_controller_type: Optional[_builtins.str] = ...,
        image_reference: Optional[outputs.ImageReferenceResponse] = ...,
        os_disk: Optional[outputs.VirtualMachineScaleSetOSDiskResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(
        self,
    ) -> Optional[Sequence[outputs.VirtualMachineScaleSetDataDiskResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="diskControllerType")
    def disk_controller_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[outputs.ImageReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[outputs.VirtualMachineScaleSetOSDiskResponse]: ...

@pulumi.output_type
class VmSizeProfileResponse(dict):
    def __init__(
        __self__, *, name: _builtins.str, rank: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class WinRMConfigurationResponse(dict):
    def __init__(
        __self__, *, listeners: Optional[Sequence[outputs.WinRMListenerResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Optional[Sequence[outputs.WinRMListenerResponse]]: ...

@pulumi.output_type
class WinRMListenerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_url: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WindowsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_unattend_content: Optional[
            Sequence[outputs.AdditionalUnattendContentResponse]
        ] = ...,
        enable_automatic_updates: Optional[_builtins.bool] = ...,
        enable_vm_agent_platform_updates: Optional[_builtins.bool] = ...,
        patch_settings: Optional[outputs.PatchSettingsResponse] = ...,
        provision_vm_agent: Optional[_builtins.bool] = ...,
        time_zone: Optional[_builtins.str] = ...,
        win_rm: Optional[outputs.WinRMConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalUnattendContent")
    def additional_unattend_content(
        self,
    ) -> Optional[Sequence[outputs.AdditionalUnattendContentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[outputs.PatchSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="winRM")
    def win_rm(self) -> Optional[outputs.WinRMConfigurationResponse]: ...

@pulumi.output_type
class WindowsVMGuestPatchAutomaticByPlatformSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bypass_platform_safety_checks_on_user_schedule: Optional[_builtins.bool] = ...,
        reboot_setting: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]: ...
