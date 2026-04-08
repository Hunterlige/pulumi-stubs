import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalCapabilitiesArgs",
    "AdditionalCapabilitiesArgsDict",
    "AdditionalLocationsProfileArgs",
    "AdditionalLocationsProfileArgsDict",
    "AdditionalUnattendContentArgs",
    "AdditionalUnattendContentArgsDict",
    "ApiEntityReferenceArgs",
    "ApiEntityReferenceArgsDict",
    "ApplicationProfileArgs",
    "ApplicationProfileArgsDict",
    "BaseVirtualMachineProfileArgs",
    "BaseVirtualMachineProfileArgsDict",
    "BootDiagnosticsArgs",
    "BootDiagnosticsArgsDict",
    "CapacityReservationProfileArgs",
    "CapacityReservationProfileArgsDict",
    "ComputeProfileArgs",
    "ComputeProfileArgsDict",
    "DiagnosticsProfileArgs",
    "DiagnosticsProfileArgsDict",
    "DiffDiskSettingsArgs",
    "DiffDiskSettingsArgsDict",
    "DiskEncryptionSetParametersArgs",
    "DiskEncryptionSetParametersArgsDict",
    "EncryptionIdentityArgs",
    "EncryptionIdentityArgsDict",
    "ImageReferenceArgs",
    "ImageReferenceArgsDict",
    "KeyVaultSecretReferenceArgs",
    "KeyVaultSecretReferenceArgsDict",
    "LinuxConfigurationArgs",
    "LinuxConfigurationArgsDict",
    "LinuxPatchSettingsArgs",
    "LinuxPatchSettingsArgsDict",
    "LinuxVMGuestPatchAutomaticByPlatformSettingsArgs",
    ...,
    "LocationProfileArgs",
    "LocationProfileArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "OSImageNotificationProfileArgs",
    "OSImageNotificationProfileArgsDict",
    "PatchSettingsArgs",
    "PatchSettingsArgsDict",
    "PlanArgs",
    "PlanArgsDict",
    "ProxyAgentSettingsArgs",
    "ProxyAgentSettingsArgsDict",
    "PublicIPAddressSkuArgs",
    "PublicIPAddressSkuArgsDict",
    "RegularPriorityProfileArgs",
    "RegularPriorityProfileArgsDict",
    "ScheduledEventsProfileArgs",
    "ScheduledEventsProfileArgsDict",
    "SecurityPostureReferenceArgs",
    "SecurityPostureReferenceArgsDict",
    "SecurityProfileArgs",
    "SecurityProfileArgsDict",
    "ServiceArtifactReferenceArgs",
    "ServiceArtifactReferenceArgsDict",
    "SpotPriorityProfileArgs",
    "SpotPriorityProfileArgsDict",
    "SshConfigurationArgs",
    "SshConfigurationArgsDict",
    "SshPublicKeyArgs",
    "SshPublicKeyArgsDict",
    "SubResourceArgs",
    "SubResourceArgsDict",
    "TerminateNotificationProfileArgs",
    "TerminateNotificationProfileArgsDict",
    "UefiSettingsArgs",
    "UefiSettingsArgsDict",
    "VMAttributeMinMaxDoubleArgs",
    "VMAttributeMinMaxDoubleArgsDict",
    "VMAttributeMinMaxIntegerArgs",
    "VMAttributeMinMaxIntegerArgsDict",
    "VMAttributesArgs",
    "VMAttributesArgsDict",
    "VMDiskSecurityProfileArgs",
    "VMDiskSecurityProfileArgsDict",
    "VMGalleryApplicationArgs",
    "VMGalleryApplicationArgsDict",
    "VMSizePropertiesArgs",
    "VMSizePropertiesArgsDict",
    "VaultCertificateArgs",
    "VaultCertificateArgsDict",
    "VaultSecretGroupArgs",
    "VaultSecretGroupArgsDict",
    "VirtualHardDiskArgs",
    "VirtualHardDiskArgsDict",
    "VirtualMachineScaleSetDataDiskArgs",
    "VirtualMachineScaleSetDataDiskArgsDict",
    "VirtualMachineScaleSetExtensionProfileArgs",
    "VirtualMachineScaleSetExtensionProfileArgsDict",
    "VirtualMachineScaleSetExtensionPropertiesArgs",
    "VirtualMachineScaleSetExtensionPropertiesArgsDict",
    "VirtualMachineScaleSetExtensionArgs",
    "VirtualMachineScaleSetExtensionArgsDict",
    "VirtualMachineScaleSetHardwareProfileArgs",
    "VirtualMachineScaleSetHardwareProfileArgsDict",
    ...,
    ...,
    "VirtualMachineScaleSetIPConfigurationArgs",
    "VirtualMachineScaleSetIPConfigurationArgsDict",
    "VirtualMachineScaleSetIpTagArgs",
    "VirtualMachineScaleSetIpTagArgsDict",
    "VirtualMachineScaleSetManagedDiskParametersArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "VirtualMachineScaleSetNetworkConfigurationArgs",
    "VirtualMachineScaleSetNetworkConfigurationArgsDict",
    "VirtualMachineScaleSetNetworkProfileArgs",
    "VirtualMachineScaleSetNetworkProfileArgsDict",
    "VirtualMachineScaleSetOSDiskArgs",
    "VirtualMachineScaleSetOSDiskArgsDict",
    "VirtualMachineScaleSetOSProfileArgs",
    "VirtualMachineScaleSetOSProfileArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "VirtualMachineScaleSetStorageProfileArgs",
    "VirtualMachineScaleSetStorageProfileArgsDict",
    "VmSizeProfileArgs",
    "VmSizeProfileArgsDict",
    "WinRMConfigurationArgs",
    "WinRMConfigurationArgsDict",
    "WinRMListenerArgs",
    "WinRMListenerArgsDict",
    "WindowsConfigurationArgs",
    "WindowsConfigurationArgsDict",
    "WindowsVMGuestPatchAutomaticByPlatformSettingsArgs",
    ...,
]

class AdditionalCapabilitiesArgsDict(TypedDict):
    hibernation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ultra_ssd_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AdditionalCapabilitiesArgs:
    def __init__(
        __self__,
        *,
        hibernation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ultra_ssd_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hibernationEnabled")
    def hibernation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @hibernation_enabled.setter
    def hibernation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ultraSSDEnabled")
    def ultra_ssd_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AdditionalLocationsProfileArgsDict(TypedDict):
    location_profiles: pulumi.Input[Sequence[pulumi.Input[LocationProfileArgsDict]]]

@pulumi.input_type
class AdditionalLocationsProfileArgs:
    def __init__(
        __self__,
        *,
        location_profiles: pulumi.Input[Sequence[pulumi.Input[LocationProfileArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationProfiles")
    def location_profiles(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LocationProfileArgs]]]: ...
    @location_profiles.setter
    def location_profiles(
        self, value: pulumi.Input[Sequence[pulumi.Input[LocationProfileArgs]]]
    ): ...

class AdditionalUnattendContentArgsDict(TypedDict):
    component_name: NotRequired[pulumi.Input[ComponentName]]
    content: NotRequired[pulumi.Input[_builtins.str]]
    pass_name: NotRequired[pulumi.Input[PassName]]
    setting_name: NotRequired[pulumi.Input[Union[_builtins.str, SettingNames]]]

@pulumi.input_type
class AdditionalUnattendContentArgs:
    def __init__(
        __self__,
        *,
        component_name: Optional[pulumi.Input[ComponentName]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        pass_name: Optional[pulumi.Input[PassName]] = ...,
        setting_name: Optional[pulumi.Input[Union[_builtins.str, SettingNames]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[pulumi.Input[ComponentName]]: ...
    @component_name.setter
    def component_name(self, value: Optional[pulumi.Input[ComponentName]]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passName")
    def pass_name(self) -> Optional[pulumi.Input[PassName]]: ...
    @pass_name.setter
    def pass_name(self, value: Optional[pulumi.Input[PassName]]): ...
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SettingNames]]]: ...
    @setting_name.setter
    def setting_name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SettingNames]]]
    ): ...

class ApiEntityReferenceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationProfileArgsDict(TypedDict):
    gallery_applications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgsDict]]]
    ]

@pulumi.input_type
class ApplicationProfileArgs:
    def __init__(
        __self__,
        *,
        gallery_applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryApplications")
    def gallery_applications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]]: ...
    @gallery_applications.setter
    def gallery_applications(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]],
    ): ...

class BaseVirtualMachineProfileArgsDict(TypedDict):
    application_profile: NotRequired[pulumi.Input[ApplicationProfileArgsDict]]
    capacity_reservation: NotRequired[pulumi.Input[CapacityReservationProfileArgsDict]]
    diagnostics_profile: NotRequired[pulumi.Input[DiagnosticsProfileArgsDict]]
    extension_profile: NotRequired[
        pulumi.Input[VirtualMachineScaleSetExtensionProfileArgsDict]
    ]
    hardware_profile: NotRequired[
        pulumi.Input[VirtualMachineScaleSetHardwareProfileArgsDict]
    ]
    license_type: NotRequired[pulumi.Input[_builtins.str]]
    network_profile: NotRequired[
        pulumi.Input[VirtualMachineScaleSetNetworkProfileArgsDict]
    ]
    os_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetOSProfileArgsDict]]
    scheduled_events_profile: NotRequired[pulumi.Input[ScheduledEventsProfileArgsDict]]
    security_posture_reference: NotRequired[
        pulumi.Input[SecurityPostureReferenceArgsDict]
    ]
    security_profile: NotRequired[pulumi.Input[SecurityProfileArgsDict]]
    service_artifact_reference: NotRequired[
        pulumi.Input[ServiceArtifactReferenceArgsDict]
    ]
    storage_profile: NotRequired[
        pulumi.Input[VirtualMachineScaleSetStorageProfileArgsDict]
    ]
    user_data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BaseVirtualMachineProfileArgs:
    def __init__(
        __self__,
        *,
        application_profile: Optional[pulumi.Input[ApplicationProfileArgs]] = ...,
        capacity_reservation: Optional[
            pulumi.Input[CapacityReservationProfileArgs]
        ] = ...,
        diagnostics_profile: Optional[pulumi.Input[DiagnosticsProfileArgs]] = ...,
        extension_profile: Optional[
            pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]
        ] = ...,
        hardware_profile: Optional[
            pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]
        ] = ...,
        license_type: Optional[pulumi.Input[_builtins.str]] = ...,
        network_profile: Optional[
            pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]
        ] = ...,
        os_profile: Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]] = ...,
        scheduled_events_profile: Optional[
            pulumi.Input[ScheduledEventsProfileArgs]
        ] = ...,
        security_posture_reference: Optional[
            pulumi.Input[SecurityPostureReferenceArgs]
        ] = ...,
        security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ...,
        service_artifact_reference: Optional[
            pulumi.Input[ServiceArtifactReferenceArgs]
        ] = ...,
        storage_profile: Optional[
            pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]
        ] = ...,
        user_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[pulumi.Input[ApplicationProfileArgs]]: ...
    @application_profile.setter
    def application_profile(
        self, value: Optional[pulumi.Input[ApplicationProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(
        self,
    ) -> Optional[pulumi.Input[CapacityReservationProfileArgs]]: ...
    @capacity_reservation.setter
    def capacity_reservation(
        self, value: Optional[pulumi.Input[CapacityReservationProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[pulumi.Input[DiagnosticsProfileArgs]]: ...
    @diagnostics_profile.setter
    def diagnostics_profile(
        self, value: Optional[pulumi.Input[DiagnosticsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extensionProfile")
    def extension_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]]: ...
    @extension_profile.setter
    def extension_profile(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]]: ...
    @hardware_profile.setter
    def hardware_profile(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]]: ...
    @os_profile.setter
    def os_profile(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(
        self,
    ) -> Optional[pulumi.Input[ScheduledEventsProfileArgs]]: ...
    @scheduled_events_profile.setter
    def scheduled_events_profile(
        self, value: Optional[pulumi.Input[ScheduledEventsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityPostureReference")
    def security_posture_reference(
        self,
    ) -> Optional[pulumi.Input[SecurityPostureReferenceArgs]]: ...
    @security_posture_reference.setter
    def security_posture_reference(
        self, value: Optional[pulumi.Input[SecurityPostureReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReference")
    def service_artifact_reference(
        self,
    ) -> Optional[pulumi.Input[ServiceArtifactReferenceArgs]]: ...
    @service_artifact_reference.setter
    def service_artifact_reference(
        self, value: Optional[pulumi.Input[ServiceArtifactReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BootDiagnosticsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    storage_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BootDiagnosticsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_uri.setter
    def storage_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapacityReservationProfileArgsDict(TypedDict):
    capacity_reservation_group: NotRequired[pulumi.Input[SubResourceArgsDict]]

@pulumi.input_type
class CapacityReservationProfileArgs:
    def __init__(
        __self__,
        *,
        capacity_reservation_group: Optional[pulumi.Input[SubResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroup")
    def capacity_reservation_group(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @capacity_reservation_group.setter
    def capacity_reservation_group(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...

class ComputeProfileArgsDict(TypedDict):
    base_virtual_machine_profile: pulumi.Input[BaseVirtualMachineProfileArgsDict]
    additional_virtual_machine_capabilities: NotRequired[
        pulumi.Input[AdditionalCapabilitiesArgsDict]
    ]
    compute_api_version: NotRequired[pulumi.Input[_builtins.str]]
    platform_fault_domain_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ComputeProfileArgs:
    def __init__(
        __self__,
        *,
        base_virtual_machine_profile: pulumi.Input[BaseVirtualMachineProfileArgs],
        additional_virtual_machine_capabilities: Optional[
            pulumi.Input[AdditionalCapabilitiesArgs]
        ] = ...,
        compute_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_fault_domain_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseVirtualMachineProfile")
    def base_virtual_machine_profile(
        self,
    ) -> pulumi.Input[BaseVirtualMachineProfileArgs]: ...
    @base_virtual_machine_profile.setter
    def base_virtual_machine_profile(
        self, value: pulumi.Input[BaseVirtualMachineProfileArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalVirtualMachineCapabilities")
    def additional_virtual_machine_capabilities(
        self,
    ) -> Optional[pulumi.Input[AdditionalCapabilitiesArgs]]: ...
    @additional_virtual_machine_capabilities.setter
    def additional_virtual_machine_capabilities(
        self, value: Optional[pulumi.Input[AdditionalCapabilitiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeApiVersion")
    def compute_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_api_version.setter
    def compute_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @platform_fault_domain_count.setter
    def platform_fault_domain_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class DiagnosticsProfileArgsDict(TypedDict):
    boot_diagnostics: NotRequired[pulumi.Input[BootDiagnosticsArgsDict]]

@pulumi.input_type
class DiagnosticsProfileArgs:
    def __init__(
        __self__, *, boot_diagnostics: Optional[pulumi.Input[BootDiagnosticsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiagnostics")
    def boot_diagnostics(self) -> Optional[pulumi.Input[BootDiagnosticsArgs]]: ...
    @boot_diagnostics.setter
    def boot_diagnostics(self, value: Optional[pulumi.Input[BootDiagnosticsArgs]]): ...

class DiffDiskSettingsArgsDict(TypedDict):
    option: NotRequired[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]
    placement: NotRequired[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]

@pulumi.input_type
class DiffDiskSettingsArgs:
    def __init__(
        __self__,
        *,
        option: Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]] = ...,
        placement: Optional[
            pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]: ...
    @option.setter
    def option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def placement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]: ...
    @placement.setter
    def placement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]
    ): ...

class DiskEncryptionSetParametersArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiskEncryptionSetParametersArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionIdentityArgsDict(TypedDict):
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(
        __self__,
        *,
        user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ImageReferenceArgsDict(TypedDict):
    community_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    offer: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    shared_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageReferenceArgs:
    def __init__(
        __self__,
        *,
        community_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        offer: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @community_gallery_image_id.setter
    def community_gallery_image_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_gallery_image_id.setter
    def shared_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultSecretReferenceArgsDict(TypedDict):
    secret_url: pulumi.Input[_builtins.str]
    source_vault: pulumi.Input[SubResourceArgsDict]

@pulumi.input_type
class KeyVaultSecretReferenceArgs:
    def __init__(
        __self__,
        *,
        secret_url: pulumi.Input[_builtins.str],
        source_vault: pulumi.Input[SubResourceArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> pulumi.Input[_builtins.str]: ...
    @secret_url.setter
    def secret_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SubResourceArgs]: ...
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SubResourceArgs]): ...

class LinuxConfigurationArgsDict(TypedDict):
    disable_password_authentication: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vm_agent_platform_updates: NotRequired[pulumi.Input[_builtins.bool]]
    patch_settings: NotRequired[pulumi.Input[LinuxPatchSettingsArgsDict]]
    provision_vm_agent: NotRequired[pulumi.Input[_builtins.bool]]
    ssh: NotRequired[pulumi.Input[SshConfigurationArgsDict]]

@pulumi.input_type
class LinuxConfigurationArgs:
    def __init__(
        __self__,
        *,
        disable_password_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vm_agent_platform_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        patch_settings: Optional[pulumi.Input[LinuxPatchSettingsArgs]] = ...,
        provision_vm_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        ssh: Optional[pulumi.Input[SshConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disablePasswordAuthentication")
    def disable_password_authentication(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_password_authentication.setter
    def disable_password_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vm_agent_platform_updates.setter
    def enable_vm_agent_platform_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[pulumi.Input[LinuxPatchSettingsArgs]]: ...
    @patch_settings.setter
    def patch_settings(self, value: Optional[pulumi.Input[LinuxPatchSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @provision_vm_agent.setter
    def provision_vm_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[pulumi.Input[SshConfigurationArgs]]: ...
    @ssh.setter
    def ssh(self, value: Optional[pulumi.Input[SshConfigurationArgs]]): ...

class LinuxPatchSettingsArgsDict(TypedDict):
    assessment_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]
    ]
    automatic_by_platform_settings: NotRequired[
        pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgsDict]
    ]
    patch_mode: NotRequired[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]

@pulumi.input_type
class LinuxPatchSettingsArgs:
    def __init__(
        __self__,
        *,
        assessment_mode: Optional[
            pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]
        ] = ...,
        automatic_by_platform_settings: Optional[
            pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]
        ] = ...,
        patch_mode: Optional[
            pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]]: ...
    @assessment_mode.setter
    def assessment_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(
        self,
    ) -> Optional[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]]: ...
    @automatic_by_platform_settings.setter
    def automatic_by_platform_settings(
        self,
        value: Optional[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]: ...
    @patch_mode.setter
    def patch_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]
    ): ...

class LinuxVMGuestPatchAutomaticByPlatformSettingsArgsDict(TypedDict):
    bypass_platform_safety_checks_on_user_schedule: NotRequired[
        pulumi.Input[_builtins.bool]
    ]
    reboot_setting: NotRequired[
        pulumi.Input[
            Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]
        ]
    ]

@pulumi.input_type
class LinuxVMGuestPatchAutomaticByPlatformSettingsArgs:
    def __init__(
        __self__,
        *,
        bypass_platform_safety_checks_on_user_schedule: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        reboot_setting: Optional[
            pulumi.Input[
                Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_platform_safety_checks_on_user_schedule.setter
    def bypass_platform_safety_checks_on_user_schedule(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]
        ]
    ]: ...
    @reboot_setting.setter
    def reboot_setting(
        self,
        value: Optional[
            pulumi.Input[
                Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]
            ]
        ],
    ): ...

class LocationProfileArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    virtual_machine_profile_override: NotRequired[
        pulumi.Input[BaseVirtualMachineProfileArgsDict]
    ]

@pulumi.input_type
class LocationProfileArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        virtual_machine_profile_override: Optional[
            pulumi.Input[BaseVirtualMachineProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfileOverride")
    def virtual_machine_profile_override(
        self,
    ) -> Optional[pulumi.Input[BaseVirtualMachineProfileArgs]]: ...
    @virtual_machine_profile_override.setter
    def virtual_machine_profile_override(
        self, value: Optional[pulumi.Input[BaseVirtualMachineProfileArgs]]
    ): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OSImageNotificationProfileArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    not_before_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OSImageNotificationProfileArgs:
    def __init__(
        __self__,
        *,
        enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        not_before_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_before_timeout.setter
    def not_before_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchSettingsArgsDict(TypedDict):
    assessment_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]
    ]
    automatic_by_platform_settings: NotRequired[
        pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgsDict]
    ]
    enable_hotpatching: NotRequired[pulumi.Input[_builtins.bool]]
    patch_mode: NotRequired[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]]

@pulumi.input_type
class PatchSettingsArgs:
    def __init__(
        __self__,
        *,
        assessment_mode: Optional[
            pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]
        ] = ...,
        automatic_by_platform_settings: Optional[
            pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]
        ] = ...,
        enable_hotpatching: Optional[pulumi.Input[_builtins.bool]] = ...,
        patch_mode: Optional[
            pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]]: ...
    @assessment_mode.setter
    def assessment_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(
        self,
    ) -> Optional[pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]]: ...
    @automatic_by_platform_settings.setter
    def automatic_by_platform_settings(
        self,
        value: Optional[
            pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_hotpatching.setter
    def enable_hotpatching(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]]: ...
    @patch_mode.setter
    def patch_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]],
    ): ...

class PlanArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    product: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PlanArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        product: pulumi.Input[_builtins.str],
        publisher: pulumi.Input[_builtins.str],
        promotion_code: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Input[_builtins.str]: ...
    @product.setter
    def product(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]: ...
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProxyAgentSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    key_incarnation_id: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Mode]]]

@pulumi.input_type
class ProxyAgentSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_incarnation_id: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyIncarnationId")
    def key_incarnation_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @key_incarnation_id.setter
    def key_incarnation_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): ...

class PublicIPAddressSkuArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]]

@pulumi.input_type
class PublicIPAddressSkuArgs:
    def __init__(
        __self__,
        *,
        name: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]
        ] = ...,
        tier: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]]: ...
    @name.setter
    def name(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]]: ...
    @tier.setter
    def tier(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]],
    ): ...

class RegularPriorityProfileArgsDict(TypedDict):
    allocation_strategy: NotRequired[
        pulumi.Input[Union[_builtins.str, RegularPriorityAllocationStrategy]]
    ]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    min_capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RegularPriorityProfileArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[
            pulumi.Input[Union[_builtins.str, RegularPriorityAllocationStrategy]]
        ] = ...,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, RegularPriorityAllocationStrategy]]
    ]: ...
    @allocation_strategy.setter
    def allocation_strategy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, RegularPriorityAllocationStrategy]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScheduledEventsProfileArgsDict(TypedDict):
    os_image_notification_profile: NotRequired[
        pulumi.Input[OSImageNotificationProfileArgsDict]
    ]
    terminate_notification_profile: NotRequired[
        pulumi.Input[TerminateNotificationProfileArgsDict]
    ]

@pulumi.input_type
class ScheduledEventsProfileArgs:
    def __init__(
        __self__,
        *,
        os_image_notification_profile: Optional[
            pulumi.Input[OSImageNotificationProfileArgs]
        ] = ...,
        terminate_notification_profile: Optional[
            pulumi.Input[TerminateNotificationProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osImageNotificationProfile")
    def os_image_notification_profile(
        self,
    ) -> Optional[pulumi.Input[OSImageNotificationProfileArgs]]: ...
    @os_image_notification_profile.setter
    def os_image_notification_profile(
        self, value: Optional[pulumi.Input[OSImageNotificationProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="terminateNotificationProfile")
    def terminate_notification_profile(
        self,
    ) -> Optional[pulumi.Input[TerminateNotificationProfileArgs]]: ...
    @terminate_notification_profile.setter
    def terminate_notification_profile(
        self, value: Optional[pulumi.Input[TerminateNotificationProfileArgs]]
    ): ...

class SecurityPostureReferenceArgsDict(TypedDict):
    exclude_extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_overridable: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SecurityPostureReferenceArgs:
    def __init__(
        __self__,
        *,
        exclude_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_overridable: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeExtensions")
    def exclude_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_extensions.setter
    def exclude_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isOverridable")
    def is_overridable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_overridable.setter
    def is_overridable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SecurityProfileArgsDict(TypedDict):
    encryption_at_host: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_identity: NotRequired[pulumi.Input[EncryptionIdentityArgsDict]]
    proxy_agent_settings: NotRequired[pulumi.Input[ProxyAgentSettingsArgsDict]]
    security_type: NotRequired[pulumi.Input[Union[_builtins.str, SecurityTypes]]]
    uefi_settings: NotRequired[pulumi.Input[UefiSettingsArgsDict]]

@pulumi.input_type
class SecurityProfileArgs:
    def __init__(
        __self__,
        *,
        encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_identity: Optional[pulumi.Input[EncryptionIdentityArgs]] = ...,
        proxy_agent_settings: Optional[pulumi.Input[ProxyAgentSettingsArgs]] = ...,
        security_type: Optional[
            pulumi.Input[Union[_builtins.str, SecurityTypes]]
        ] = ...,
        uefi_settings: Optional[pulumi.Input[UefiSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[pulumi.Input[EncryptionIdentityArgs]]: ...
    @encryption_identity.setter
    def encryption_identity(
        self, value: Optional[pulumi.Input[EncryptionIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyAgentSettings")
    def proxy_agent_settings(
        self,
    ) -> Optional[pulumi.Input[ProxyAgentSettingsArgs]]: ...
    @proxy_agent_settings.setter
    def proxy_agent_settings(
        self, value: Optional[pulumi.Input[ProxyAgentSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityTypes]]]: ...
    @security_type.setter
    def security_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[pulumi.Input[UefiSettingsArgs]]: ...
    @uefi_settings.setter
    def uefi_settings(self, value: Optional[pulumi.Input[UefiSettingsArgs]]): ...

class ServiceArtifactReferenceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceArtifactReferenceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SpotPriorityProfileArgsDict(TypedDict):
    allocation_strategy: NotRequired[
        pulumi.Input[Union[_builtins.str, SpotAllocationStrategy]]
    ]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    eviction_policy: NotRequired[pulumi.Input[Union[_builtins.str, EvictionPolicy]]]
    maintain: NotRequired[pulumi.Input[_builtins.bool]]
    max_price_per_vm: NotRequired[pulumi.Input[_builtins.float]]
    min_capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SpotPriorityProfileArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: Optional[
            pulumi.Input[Union[_builtins.str, SpotAllocationStrategy]]
        ] = ...,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        eviction_policy: Optional[
            pulumi.Input[Union[_builtins.str, EvictionPolicy]]
        ] = ...,
        maintain: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_price_per_vm: Optional[pulumi.Input[_builtins.float]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SpotAllocationStrategy]]]: ...
    @allocation_strategy.setter
    def allocation_strategy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, SpotAllocationStrategy]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]]: ...
    @eviction_policy.setter
    def eviction_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EvictionPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def maintain(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @maintain.setter
    def maintain(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPricePerVM")
    def max_price_per_vm(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_price_per_vm.setter
    def max_price_per_vm(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SshConfigurationArgsDict(TypedDict):
    public_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgsDict]]]]

@pulumi.input_type
class SshConfigurationArgs:
    def __init__(
        __self__,
        *,
        public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]: ...
    @public_keys.setter
    def public_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]
    ): ...

class SshPublicKeyArgsDict(TypedDict):
    key_data: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(
        __self__,
        *,
        key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_data.setter
    def key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubResourceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TerminateNotificationProfileArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    not_before_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TerminateNotificationProfileArgs:
    def __init__(
        __self__,
        *,
        enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        not_before_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_before_timeout.setter
    def not_before_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UefiSettingsArgsDict(TypedDict):
    secure_boot_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    v_tpm_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UefiSettingsArgs:
    def __init__(
        __self__,
        *,
        secure_boot_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        v_tpm_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @secure_boot_enabled.setter
    def secure_boot_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="vTpmEnabled")
    def v_tpm_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @v_tpm_enabled.setter
    def v_tpm_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VMAttributeMinMaxDoubleArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class VMAttributeMinMaxDoubleArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.float]] = ...,
        min: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class VMAttributeMinMaxIntegerArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VMAttributeMinMaxIntegerArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VMAttributesArgsDict(TypedDict):
    memory_in_gi_b: pulumi.Input[VMAttributeMinMaxDoubleArgsDict]
    v_cpu_count: pulumi.Input[VMAttributeMinMaxIntegerArgsDict]
    accelerator_count: NotRequired[pulumi.Input[VMAttributeMinMaxIntegerArgsDict]]
    accelerator_manufacturers: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AcceleratorManufacturer]]]
        ]
    ]
    accelerator_support: NotRequired[
        pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
    ]
    accelerator_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AcceleratorType]]]]
    ]
    architecture_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ArchitectureType]]]]
    ]
    burstable_support: NotRequired[
        pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
    ]
    cpu_manufacturers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CpuManufacturer]]]]
    ]
    data_disk_count: NotRequired[pulumi.Input[VMAttributeMinMaxIntegerArgsDict]]
    excluded_vm_sizes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    local_storage_disk_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LocalStorageDiskType]]]]
    ]
    local_storage_in_gi_b: NotRequired[pulumi.Input[VMAttributeMinMaxDoubleArgsDict]]
    local_storage_support: NotRequired[
        pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
    ]
    memory_in_gi_b_per_v_cpu: NotRequired[pulumi.Input[VMAttributeMinMaxDoubleArgsDict]]
    network_bandwidth_in_mbps: NotRequired[
        pulumi.Input[VMAttributeMinMaxDoubleArgsDict]
    ]
    network_interface_count: NotRequired[pulumi.Input[VMAttributeMinMaxIntegerArgsDict]]
    rdma_network_interface_count: NotRequired[
        pulumi.Input[VMAttributeMinMaxIntegerArgsDict]
    ]
    rdma_support: NotRequired[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]
    vm_categories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VMCategory]]]]
    ]

@pulumi.input_type
class VMAttributesArgs:
    def __init__(
        __self__,
        *,
        memory_in_gi_b: pulumi.Input[VMAttributeMinMaxDoubleArgs],
        v_cpu_count: pulumi.Input[VMAttributeMinMaxIntegerArgs],
        accelerator_count: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]] = ...,
        accelerator_manufacturers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AcceleratorManufacturer]]]
            ]
        ] = ...,
        accelerator_support: Optional[
            pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
        ] = ...,
        accelerator_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AcceleratorType]]]]
        ] = ...,
        architecture_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ArchitectureType]]]]
        ] = ...,
        burstable_support: Optional[
            pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
        ] = ...,
        cpu_manufacturers: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CpuManufacturer]]]]
        ] = ...,
        data_disk_count: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]] = ...,
        excluded_vm_sizes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        local_storage_disk_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, LocalStorageDiskType]]]
            ]
        ] = ...,
        local_storage_in_gi_b: Optional[
            pulumi.Input[VMAttributeMinMaxDoubleArgs]
        ] = ...,
        local_storage_support: Optional[
            pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
        ] = ...,
        memory_in_gi_b_per_v_cpu: Optional[
            pulumi.Input[VMAttributeMinMaxDoubleArgs]
        ] = ...,
        network_bandwidth_in_mbps: Optional[
            pulumi.Input[VMAttributeMinMaxDoubleArgs]
        ] = ...,
        network_interface_count: Optional[
            pulumi.Input[VMAttributeMinMaxIntegerArgs]
        ] = ...,
        rdma_network_interface_count: Optional[
            pulumi.Input[VMAttributeMinMaxIntegerArgs]
        ] = ...,
        rdma_support: Optional[
            pulumi.Input[Union[_builtins.str, VMAttributeSupport]]
        ] = ...,
        vm_categories: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VMCategory]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryInGiB")
    def memory_in_gi_b(self) -> pulumi.Input[VMAttributeMinMaxDoubleArgs]: ...
    @memory_in_gi_b.setter
    def memory_in_gi_b(self, value: pulumi.Input[VMAttributeMinMaxDoubleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="vCpuCount")
    def v_cpu_count(self) -> pulumi.Input[VMAttributeMinMaxIntegerArgs]: ...
    @v_cpu_count.setter
    def v_cpu_count(self, value: pulumi.Input[VMAttributeMinMaxIntegerArgs]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]: ...
    @accelerator_count.setter
    def accelerator_count(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AcceleratorManufacturer]]]
        ]
    ]: ...
    @accelerator_manufacturers.setter
    def accelerator_manufacturers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AcceleratorManufacturer]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorSupport")
    def accelerator_support(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]: ...
    @accelerator_support.setter
    def accelerator_support(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AcceleratorType]]]]
    ]: ...
    @accelerator_types.setter
    def accelerator_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AcceleratorType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="architectureTypes")
    def architecture_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ArchitectureType]]]]
    ]: ...
    @architecture_types.setter
    def architecture_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ArchitectureType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="burstableSupport")
    def burstable_support(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]: ...
    @burstable_support.setter
    def burstable_support(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CpuManufacturer]]]]
    ]: ...
    @cpu_manufacturers.setter
    def cpu_manufacturers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, CpuManufacturer]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskCount")
    def data_disk_count(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]: ...
    @data_disk_count.setter
    def data_disk_count(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedVMSizes")
    def excluded_vm_sizes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_vm_sizes.setter
    def excluded_vm_sizes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localStorageDiskTypes")
    def local_storage_disk_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LocalStorageDiskType]]]]
    ]: ...
    @local_storage_disk_types.setter
    def local_storage_disk_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, LocalStorageDiskType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localStorageInGiB")
    def local_storage_in_gi_b(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]: ...
    @local_storage_in_gi_b.setter
    def local_storage_in_gi_b(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localStorageSupport")
    def local_storage_support(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]: ...
    @local_storage_support.setter
    def local_storage_support(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryInGiBPerVCpu")
    def memory_in_gi_b_per_v_cpu(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]: ...
    @memory_in_gi_b_per_v_cpu.setter
    def memory_in_gi_b_per_v_cpu(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkBandwidthInMbps")
    def network_bandwidth_in_mbps(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]: ...
    @network_bandwidth_in_mbps.setter
    def network_bandwidth_in_mbps(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxDoubleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]: ...
    @network_interface_count.setter
    def network_interface_count(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rdmaNetworkInterfaceCount")
    def rdma_network_interface_count(
        self,
    ) -> Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]: ...
    @rdma_network_interface_count.setter
    def rdma_network_interface_count(
        self, value: Optional[pulumi.Input[VMAttributeMinMaxIntegerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rdmaSupport")
    def rdma_support(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]: ...
    @rdma_support.setter
    def rdma_support(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VMAttributeSupport]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmCategories")
    def vm_categories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VMCategory]]]]
    ]: ...
    @vm_categories.setter
    def vm_categories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VMCategory]]]]
        ],
    ): ...

class VMDiskSecurityProfileArgsDict(TypedDict):
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    security_encryption_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]
    ]

@pulumi.input_type
class VMDiskSecurityProfileArgs:
    def __init__(
        __self__,
        *,
        disk_encryption_set: Optional[
            pulumi.Input[DiskEncryptionSetParametersArgs]
        ] = ...,
        security_encryption_type: Optional[
            pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]: ...
    @disk_encryption_set.setter
    def disk_encryption_set(
        self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]]: ...
    @security_encryption_type.setter
    def security_encryption_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]],
    ): ...

class VMGalleryApplicationArgsDict(TypedDict):
    package_reference_id: pulumi.Input[_builtins.str]
    configuration_reference: NotRequired[pulumi.Input[_builtins.str]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    tags: NotRequired[pulumi.Input[_builtins.str]]
    treat_failure_as_deployment_failure: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VMGalleryApplicationArgs:
    def __init__(
        __self__,
        *,
        package_reference_id: pulumi.Input[_builtins.str],
        configuration_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        order: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[_builtins.str]] = ...,
        treat_failure_as_deployment_failure: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packageReferenceId")
    def package_reference_id(self) -> pulumi.Input[_builtins.str]: ...
    @package_reference_id.setter
    def package_reference_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationReference")
    def configuration_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_reference.setter
    def configuration_reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @treat_failure_as_deployment_failure.setter
    def treat_failure_as_deployment_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class VMSizePropertiesArgsDict(TypedDict):
    v_cpus_available: NotRequired[pulumi.Input[_builtins.int]]
    v_cpus_per_core: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VMSizePropertiesArgs:
    def __init__(
        __self__,
        *,
        v_cpus_available: Optional[pulumi.Input[_builtins.int]] = ...,
        v_cpus_per_core: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vCPUsAvailable")
    def v_cpus_available(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @v_cpus_available.setter
    def v_cpus_available(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vCPUsPerCore")
    def v_cpus_per_core(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @v_cpus_per_core.setter
    def v_cpus_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VaultCertificateArgsDict(TypedDict):
    certificate_store: NotRequired[pulumi.Input[_builtins.str]]
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VaultCertificateArgs:
    def __init__(
        __self__,
        *,
        certificate_store: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_store.setter
    def certificate_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VaultSecretGroupArgsDict(TypedDict):
    source_vault: NotRequired[pulumi.Input[SubResourceArgsDict]]
    vault_certificates: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgsDict]]]
    ]

@pulumi.input_type
class VaultSecretGroupArgs:
    def __init__(
        __self__,
        *,
        source_vault: Optional[pulumi.Input[SubResourceArgs]] = ...,
        vault_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @source_vault.setter
    def source_vault(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]]: ...
    @vault_certificates.setter
    def vault_certificates(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]],
    ): ...

class VirtualHardDiskArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualHardDiskArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineScaleSetDataDiskArgsDict(TypedDict):
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    lun: pulumi.Input[_builtins.int]
    caching: NotRequired[pulumi.Input[Union[_builtins.str, CachingTypes]]]
    delete_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]
    ]
    disk_iops_read_write: NotRequired[pulumi.Input[_builtins.float]]
    disk_m_bps_read_write: NotRequired[pulumi.Input[_builtins.float]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    managed_disk: NotRequired[
        pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VirtualMachineScaleSetDataDiskArgs:
    def __init__(
        __self__,
        *,
        create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]],
        lun: pulumi.Input[_builtins.int],
        caching: Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]] = ...,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]
        ] = ...,
        disk_iops_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_m_bps_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        managed_disk: Optional[
            pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]: ...
    @create_option.setter
    def create_option(
        self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]: ...
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]]: ...
    @caching.setter
    def caching(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]: ...
    @delete_option.setter
    def delete_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_iops_read_write.setter
    def disk_iops_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_m_bps_read_write.setter
    def disk_m_bps_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]: ...
    @managed_disk.setter
    def managed_disk(
        self,
        value: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class VirtualMachineScaleSetExtensionProfileArgsDict(TypedDict):
    extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgsDict]]]
    ]
    extensions_time_budget: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineScaleSetExtensionProfileArgs:
    def __init__(
        __self__,
        *,
        extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]
        ] = ...,
        extensions_time_budget: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]
    ]: ...
    @extensions.setter
    def extensions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extensions_time_budget.setter
    def extensions_time_budget(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineScaleSetExtensionPropertiesArgsDict(TypedDict):
    auto_upgrade_minor_version: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    force_update_tag: NotRequired[pulumi.Input[_builtins.str]]
    protected_settings: NotRequired[Any]
    protected_settings_from_key_vault: NotRequired[
        pulumi.Input[KeyVaultSecretReferenceArgsDict]
    ]
    provision_after_extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[Any]
    suppress_failures: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    type_handler_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineScaleSetExtensionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_settings: Optional[Any] = ...,
        protected_settings_from_key_vault: Optional[
            pulumi.Input[KeyVaultSecretReferenceArgs]
        ] = ...,
        provision_after_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[Any] = ...,
        suppress_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(
        self,
    ) -> Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]: ...
    @protected_settings_from_key_vault.setter
    def protected_settings_from_key_vault(
        self, value: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @provision_after_extensions.setter
    def provision_after_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @settings.setter
    def settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suppress_failures.setter
    def suppress_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineScaleSetExtensionArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[
        pulumi.Input[VirtualMachineScaleSetExtensionPropertiesArgsDict]
    ]

@pulumi.input_type
class VirtualMachineScaleSetExtensionArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[VirtualMachineScaleSetExtensionPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetExtensionPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[pulumi.Input[VirtualMachineScaleSetExtensionPropertiesArgs]],
    ): ...

class VirtualMachineScaleSetHardwareProfileArgsDict(TypedDict):
    vm_size_properties: NotRequired[pulumi.Input[VMSizePropertiesArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetHardwareProfileArgs:
    def __init__(
        __self__,
        *,
        vm_size_properties: Optional[pulumi.Input[VMSizePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vmSizeProperties")
    def vm_size_properties(self) -> Optional[pulumi.Input[VMSizePropertiesArgs]]: ...
    @vm_size_properties.setter
    def vm_size_properties(
        self, value: Optional[pulumi.Input[VMSizePropertiesArgs]]
    ): ...

class VirtualMachineScaleSetIPConfigurationPropertiesArgsDict(TypedDict):
    application_gateway_backend_address_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    application_security_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    load_balancer_backend_address_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    load_balancer_inbound_nat_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address_version: NotRequired[
        pulumi.Input[Union[_builtins.str, IPVersion]]
    ]
    public_ip_address_configuration: NotRequired[
        pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgsDict]
    ]
    subnet: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetIPConfigurationPropertiesArgs:
    def __init__(
        __self__,
        *,
        application_gateway_backend_address_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        application_security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        load_balancer_backend_address_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        load_balancer_inbound_nat_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        private_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_address_configuration: Optional[
            pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]
        ] = ...,
        subnet: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @application_gateway_backend_address_pools.setter
    def application_gateway_backend_address_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @application_security_groups.setter
    def application_security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @load_balancer_backend_address_pools.setter
    def load_balancer_backend_address_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPools")
    def load_balancer_inbound_nat_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @load_balancer_inbound_nat_pools.setter
    def load_balancer_inbound_nat_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]: ...
    @private_ip_address_version.setter
    def private_ip_address_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]
    ]: ...
    @public_ip_address_configuration.setter
    def public_ip_address_configuration(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): ...

class VirtualMachineScaleSetIPConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    properties: NotRequired[
        pulumi.Input[VirtualMachineScaleSetIPConfigurationPropertiesArgsDict]
    ]

@pulumi.input_type
class VirtualMachineScaleSetIPConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[VirtualMachineScaleSetIPConfigurationPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetIPConfigurationPropertiesArgs]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineScaleSetIPConfigurationPropertiesArgs]
        ],
    ): ...

class VirtualMachineScaleSetIpTagArgsDict(TypedDict):
    ip_tag_type: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineScaleSetIpTagArgs:
    def __init__(
        __self__,
        *,
        ip_tag_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_tag_type.setter
    def ip_tag_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineScaleSetManagedDiskParametersArgsDict(TypedDict):
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    security_profile: NotRequired[pulumi.Input[VMDiskSecurityProfileArgsDict]]
    storage_account_type: NotRequired[
        pulumi.Input[Union[_builtins.str, StorageAccountTypes]]
    ]

@pulumi.input_type
class VirtualMachineScaleSetManagedDiskParametersArgs:
    def __init__(
        __self__,
        *,
        disk_encryption_set: Optional[
            pulumi.Input[DiskEncryptionSetParametersArgs]
        ] = ...,
        security_profile: Optional[pulumi.Input[VMDiskSecurityProfileArgs]] = ...,
        storage_account_type: Optional[
            pulumi.Input[Union[_builtins.str, StorageAccountTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]: ...
    @disk_encryption_set.setter
    def disk_encryption_set(
        self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[VMDiskSecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(
        self, value: Optional[pulumi.Input[VMDiskSecurityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]: ...
    @storage_account_type.setter
    def storage_account_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]
    ): ...

class VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgsDict(TypedDict):
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs:
    def __init__(
        __self__,
        *,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VirtualMachineScaleSetNetworkConfigurationPropertiesArgsDict(TypedDict):
    ip_configurations: pulumi.Input[
        Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgsDict]]
    ]
    auxiliary_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]
    ]
    auxiliary_sku: NotRequired[
        pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]
    ]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    disable_tcp_state_tracking: NotRequired[pulumi.Input[_builtins.bool]]
    dns_settings: NotRequired[
        pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgsDict]
    ]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]
    enable_fpga: NotRequired[pulumi.Input[_builtins.bool]]
    enable_ip_forwarding: NotRequired[pulumi.Input[_builtins.bool]]
    network_security_group: NotRequired[pulumi.Input[SubResourceArgsDict]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VirtualMachineScaleSetNetworkConfigurationPropertiesArgs:
    def __init__(
        __self__,
        *,
        ip_configurations: pulumi.Input[
            Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]
        ],
        auxiliary_mode: Optional[
            pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]
        ] = ...,
        auxiliary_sku: Optional[
            pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]
        ] = ...,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOptions]]
        ] = ...,
        disable_tcp_state_tracking: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_settings: Optional[
            pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]
        ] = ...,
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_fpga: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ip_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_security_group: Optional[pulumi.Input[SubResourceArgs]] = ...,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]
    ]: ...
    @ip_configurations.setter
    def ip_configurations(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]
    ]: ...
    @auxiliary_mode.setter
    def auxiliary_mode(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]: ...
    @auxiliary_sku.setter
    def auxiliary_sku(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]: ...
    @delete_option.setter
    def delete_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_tcp_state_tracking.setter
    def disable_tcp_state_tracking(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]
    ]: ...
    @dns_settings.setter
    def dns_settings(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableFpga")
    def enable_fpga(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fpga.setter
    def enable_fpga(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ip_forwarding.setter
    def enable_ip_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @network_security_group.setter
    def network_security_group(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VirtualMachineScaleSetNetworkConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    properties: NotRequired[
        pulumi.Input[VirtualMachineScaleSetNetworkConfigurationPropertiesArgsDict]
    ]

@pulumi.input_type
class VirtualMachineScaleSetNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[VirtualMachineScaleSetNetworkConfigurationPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetNetworkConfigurationPropertiesArgs]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[VirtualMachineScaleSetNetworkConfigurationPropertiesArgs]
        ],
    ): ...

class VirtualMachineScaleSetNetworkProfileArgsDict(TypedDict):
    health_probe: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]
    network_api_version: NotRequired[
        pulumi.Input[Union[_builtins.str, NetworkApiVersion]]
    ]
    network_interface_configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgsDict]]
        ]
    ]

@pulumi.input_type
class VirtualMachineScaleSetNetworkProfileArgs:
    def __init__(
        __self__,
        *,
        health_probe: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...,
        network_api_version: Optional[
            pulumi.Input[Union[_builtins.str, NetworkApiVersion]]
        ] = ...,
        network_interface_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthProbe")
    def health_probe(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]: ...
    @health_probe.setter
    def health_probe(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="networkApiVersion")
    def network_api_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]: ...
    @network_api_version.setter
    def network_api_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]
        ]
    ]: ...
    @network_interface_configurations.setter
    def network_interface_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]
            ]
        ],
    ): ...

class VirtualMachineScaleSetOSDiskArgsDict(TypedDict):
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    caching: NotRequired[pulumi.Input[Union[_builtins.str, CachingTypes]]]
    delete_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]
    ]
    diff_disk_settings: NotRequired[pulumi.Input[DiffDiskSettingsArgsDict]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    image: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    managed_disk: NotRequired[
        pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]
    vhd_containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VirtualMachineScaleSetOSDiskArgs:
    def __init__(
        __self__,
        *,
        create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]],
        caching: Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]] = ...,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]
        ] = ...,
        diff_disk_settings: Optional[pulumi.Input[DiffDiskSettingsArgs]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        image: Optional[pulumi.Input[VirtualHardDiskArgs]] = ...,
        managed_disk: Optional[
            pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_type: Optional[
            pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]
        ] = ...,
        vhd_containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]: ...
    @create_option.setter
    def create_option(
        self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]]: ...
    @caching.setter
    def caching(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CachingTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]: ...
    @delete_option.setter
    def delete_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diffDiskSettings")
    def diff_disk_settings(self) -> Optional[pulumi.Input[DiffDiskSettingsArgs]]: ...
    @diff_disk_settings.setter
    def diff_disk_settings(
        self, value: Optional[pulumi.Input[DiffDiskSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]: ...
    @managed_disk.setter
    def managed_disk(
        self,
        value: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]: ...
    @os_type.setter
    def os_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vhdContainers")
    def vhd_containers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vhd_containers.setter
    def vhd_containers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class VirtualMachineScaleSetOSProfileArgsDict(TypedDict):
    admin_password: NotRequired[pulumi.Input[_builtins.str]]
    admin_username: NotRequired[pulumi.Input[_builtins.str]]
    allow_extension_operations: NotRequired[pulumi.Input[_builtins.bool]]
    computer_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    custom_data: NotRequired[pulumi.Input[_builtins.str]]
    linux_configuration: NotRequired[pulumi.Input[LinuxConfigurationArgsDict]]
    require_guest_provision_signal: NotRequired[pulumi.Input[_builtins.bool]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgsDict]]]]
    windows_configuration: NotRequired[pulumi.Input[WindowsConfigurationArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetOSProfileArgs:
    def __init__(
        __self__,
        *,
        admin_password: Optional[pulumi.Input[_builtins.str]] = ...,
        admin_username: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_extension_operations: Optional[pulumi.Input[_builtins.bool]] = ...,
        computer_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_data: Optional[pulumi.Input[_builtins.str]] = ...,
        linux_configuration: Optional[pulumi.Input[LinuxConfigurationArgs]] = ...,
        require_guest_provision_signal: Optional[pulumi.Input[_builtins.bool]] = ...,
        secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]
        ] = ...,
        windows_configuration: Optional[pulumi.Input[WindowsConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_extension_operations.setter
    def allow_extension_operations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @computer_name_prefix.setter
    def computer_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[pulumi.Input[LinuxConfigurationArgs]]: ...
    @linux_configuration.setter
    def linux_configuration(
        self, value: Optional[pulumi.Input[LinuxConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireGuestProvisionSignal")
    def require_guest_provision_signal(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_guest_provision_signal.setter
    def require_guest_provision_signal(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def secrets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]: ...
    @secrets.setter
    def secrets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsConfigurationArgs]]: ...
    @windows_configuration.setter
    def windows_configuration(
        self, value: Optional[pulumi.Input[WindowsConfigurationArgs]]
    ): ...

class VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgsDict(TypedDict):
    domain_name_label: pulumi.Input[_builtins.str]
    domain_name_label_scope: NotRequired[
        pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]
    ]

@pulumi.input_type
class VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs:
    def __init__(
        __self__,
        *,
        domain_name_label: pulumi.Input[_builtins.str],
        domain_name_label_scope: Optional[
            pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name_label.setter
    def domain_name_label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainNameLabelScope")
    def domain_name_label_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]: ...
    @domain_name_label_scope.setter
    def domain_name_label_scope(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]],
    ): ...

class VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgsDict(TypedDict):
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    dns_settings: NotRequired[
        pulumi.Input[
            VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgsDict
        ]
    ]
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ip_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgsDict]]]
    ]
    public_ip_address_version: NotRequired[
        pulumi.Input[Union[_builtins.str, IPVersion]]
    ]
    public_ip_prefix: NotRequired[pulumi.Input[SubResourceArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgs:
    def __init__(
        __self__,
        *,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOptions]]
        ] = ...,
        dns_settings: Optional[
            pulumi.Input[
                VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs
            ]
        ] = ...,
        idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]
        ] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_prefix: Optional[pulumi.Input[SubResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]: ...
    @delete_option.setter
    def delete_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs]
    ]: ...
    @dns_settings.setter
    def dns_settings(
        self,
        value: Optional[
            pulumi.Input[
                VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]
    ]: ...
    @ip_tags.setter
    def ip_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]: ...
    @public_ip_address_version.setter
    def public_ip_address_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @public_ip_prefix.setter
    def public_ip_prefix(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...

class VirtualMachineScaleSetPublicIPAddressConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    properties: NotRequired[
        pulumi.Input[
            VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgsDict
        ]
    ]
    sku: NotRequired[pulumi.Input[PublicIPAddressSkuArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetPublicIPAddressConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[
                VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgs
            ]
        ] = ...,
        sku: Optional[pulumi.Input[PublicIPAddressSkuArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgs]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                VirtualMachineScaleSetPublicIPAddressConfigurationPropertiesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[PublicIPAddressSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[PublicIPAddressSkuArgs]]): ...

class VirtualMachineScaleSetStorageProfileArgsDict(TypedDict):
    data_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgsDict]]]
    ]
    disk_controller_type: NotRequired[
        pulumi.Input[Union[_builtins.str, DiskControllerTypes]]
    ]
    image_reference: NotRequired[pulumi.Input[ImageReferenceArgsDict]]
    os_disk: NotRequired[pulumi.Input[VirtualMachineScaleSetOSDiskArgsDict]]

@pulumi.input_type
class VirtualMachineScaleSetStorageProfileArgs:
    def __init__(
        __self__,
        *,
        data_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]
        ] = ...,
        disk_controller_type: Optional[
            pulumi.Input[Union[_builtins.str, DiskControllerTypes]]
        ] = ...,
        image_reference: Optional[pulumi.Input[ImageReferenceArgs]] = ...,
        os_disk: Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]
    ]: ...
    @data_disks.setter
    def data_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskControllerType")
    def disk_controller_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]: ...
    @disk_controller_type.setter
    def disk_controller_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[pulumi.Input[ImageReferenceArgs]]: ...
    @image_reference.setter
    def image_reference(self, value: Optional[pulumi.Input[ImageReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]]: ...
    @os_disk.setter
    def os_disk(
        self, value: Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]]
    ): ...

class VmSizeProfileArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    rank: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VmSizeProfileArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        rank: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WinRMConfigurationArgsDict(TypedDict):
    listeners: NotRequired[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgsDict]]]]

@pulumi.input_type
class WinRMConfigurationArgs:
    def __init__(
        __self__,
        *,
        listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]]: ...
    @listeners.setter
    def listeners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]]
    ): ...

class WinRMListenerArgsDict(TypedDict):
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]

@pulumi.input_type
class WinRMListenerArgs:
    def __init__(
        __self__,
        *,
        certificate_url: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolTypes]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]
    ): ...

class WindowsConfigurationArgsDict(TypedDict):
    additional_unattend_content: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgsDict]]]
    ]
    enable_automatic_updates: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vm_agent_platform_updates: NotRequired[pulumi.Input[_builtins.bool]]
    patch_settings: NotRequired[pulumi.Input[PatchSettingsArgsDict]]
    provision_vm_agent: NotRequired[pulumi.Input[_builtins.bool]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    win_rm: NotRequired[pulumi.Input[WinRMConfigurationArgsDict]]

@pulumi.input_type
class WindowsConfigurationArgs:
    def __init__(
        __self__,
        *,
        additional_unattend_content: Optional[
            pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]
        ] = ...,
        enable_automatic_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vm_agent_platform_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        patch_settings: Optional[pulumi.Input[PatchSettingsArgs]] = ...,
        provision_vm_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        win_rm: Optional[pulumi.Input[WinRMConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalUnattendContent")
    def additional_unattend_content(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]
    ]: ...
    @additional_unattend_content.setter
    def additional_unattend_content(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vm_agent_platform_updates.setter
    def enable_vm_agent_platform_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[pulumi.Input[PatchSettingsArgs]]: ...
    @patch_settings.setter
    def patch_settings(self, value: Optional[pulumi.Input[PatchSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @provision_vm_agent.setter
    def provision_vm_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="winRM")
    def win_rm(self) -> Optional[pulumi.Input[WinRMConfigurationArgs]]: ...
    @win_rm.setter
    def win_rm(self, value: Optional[pulumi.Input[WinRMConfigurationArgs]]): ...

class WindowsVMGuestPatchAutomaticByPlatformSettingsArgsDict(TypedDict):
    bypass_platform_safety_checks_on_user_schedule: NotRequired[
        pulumi.Input[_builtins.bool]
    ]
    reboot_setting: NotRequired[
        pulumi.Input[
            Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]
        ]
    ]

@pulumi.input_type
class WindowsVMGuestPatchAutomaticByPlatformSettingsArgs:
    def __init__(
        __self__,
        *,
        bypass_platform_safety_checks_on_user_schedule: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        reboot_setting: Optional[
            pulumi.Input[
                Union[
                    _builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bypass_platform_safety_checks_on_user_schedule.setter
    def bypass_platform_safety_checks_on_user_schedule(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]
        ]
    ]: ...
    @reboot_setting.setter
    def reboot_setting(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    _builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting
                ]
            ]
        ],
    ): ...
