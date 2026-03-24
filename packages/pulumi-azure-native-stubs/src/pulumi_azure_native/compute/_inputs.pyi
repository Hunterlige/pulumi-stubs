

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessControlRulesIdentityArgs', 'AccessControlRulesIdentityArgsDict', 'AccessControlRulesPrivilegeArgs', 'AccessControlRulesPrivilegeArgsDict', 'AccessControlRulesRoleAssignmentArgs', 'AccessControlRulesRoleAssignmentArgsDict', 'AccessControlRulesRoleArgs', 'AccessControlRulesRoleArgsDict', 'AccessControlRulesArgs', 'AccessControlRulesArgsDict', 'AdditionalCapabilitiesArgs', 'AdditionalCapabilitiesArgsDict', 'AdditionalReplicaSetArgs', 'AdditionalReplicaSetArgsDict', 'AdditionalUnattendContentArgs', 'AdditionalUnattendContentArgsDict', 'ApiEntityReferenceArgs', 'ApiEntityReferenceArgsDict', 'ApplicationProfileArgs', 'ApplicationProfileArgsDict', 'AutomaticOSUpgradePolicyArgs', 'AutomaticOSUpgradePolicyArgsDict', 'AutomaticRepairsPolicyArgs', 'AutomaticRepairsPolicyArgsDict', 'AutomaticZoneRebalancingPolicyArgs', 'AutomaticZoneRebalancingPolicyArgsDict', 'BillingProfileArgs', 'BillingProfileArgsDict', 'BootDiagnosticsArgs', 'BootDiagnosticsArgsDict', 'CapacityReservationProfileArgs', 'CapacityReservationProfileArgsDict', 'CloudServiceExtensionProfileArgs', 'CloudServiceExtensionProfileArgsDict', 'CloudServiceExtensionPropertiesArgs', 'CloudServiceExtensionPropertiesArgsDict', 'CloudServiceNetworkProfileArgs', 'CloudServiceNetworkProfileArgsDict', 'CloudServiceOsProfileArgs', 'CloudServiceOsProfileArgsDict', 'CloudServicePropertiesArgs', 'CloudServicePropertiesArgsDict', 'CloudServiceRoleProfilePropertiesArgs', 'CloudServiceRoleProfilePropertiesArgsDict', 'CloudServiceRoleProfileArgs', 'CloudServiceRoleProfileArgsDict', 'CloudServiceRoleSkuArgs', 'CloudServiceRoleSkuArgsDict', 'CloudServiceVaultAndSecretReferenceArgs', 'CloudServiceVaultAndSecretReferenceArgsDict', 'CloudServiceVaultCertificateArgs', 'CloudServiceVaultCertificateArgsDict', 'CloudServiceVaultSecretGroupArgs', 'CloudServiceVaultSecretGroupArgsDict', 'CommunityGalleryInfoArgs', 'CommunityGalleryInfoArgsDict', 'CopyCompletionErrorArgs', 'CopyCompletionErrorArgsDict', 'CreationDataArgs', 'CreationDataArgsDict', 'DataDiskImageEncryptionArgs', 'DataDiskImageEncryptionArgsDict', 'DataDiskArgs', 'DataDiskArgsDict', ..., ..., 'DiagnosticsProfileArgs', 'DiagnosticsProfileArgsDict', 'DiffDiskSettingsArgs', 'DiffDiskSettingsArgsDict', 'DisallowedArgs', 'DisallowedArgsDict', 'DiskEncryptionSetParametersArgs', 'DiskEncryptionSetParametersArgsDict', 'DiskEncryptionSettingsArgs', 'DiskEncryptionSettingsArgsDict', 'DiskPurchasePlanArgs', 'DiskPurchasePlanArgsDict', 'DiskRestorePointAttributesArgs', 'DiskRestorePointAttributesArgsDict', 'DiskSecurityProfileArgs', 'DiskSecurityProfileArgsDict', 'DiskSkuArgs', 'DiskSkuArgsDict', 'EncryptionIdentityArgs', 'EncryptionIdentityArgsDict', 'EncryptionImagesArgs', 'EncryptionImagesArgsDict', 'EncryptionSetIdentityArgs', 'EncryptionSetIdentityArgsDict', 'EncryptionSettingsCollectionArgs', 'EncryptionSettingsCollectionArgsDict', 'EncryptionSettingsElementArgs', 'EncryptionSettingsElementArgsDict', 'EncryptionArgs', 'EncryptionArgsDict', 'EventGridAndResourceGraphArgs', 'EventGridAndResourceGraphArgsDict', 'ExtendedLocationArgs', 'ExtendedLocationArgsDict', 'ExtensionArgs', 'ExtensionArgsDict', 'GalleryApplicationCustomActionParameterArgs', 'GalleryApplicationCustomActionParameterArgsDict', 'GalleryApplicationCustomActionArgs', 'GalleryApplicationCustomActionArgsDict', 'GalleryApplicationVersionPublishingProfileArgs', 'GalleryApplicationVersionPublishingProfileArgsDict', 'GalleryApplicationVersionSafetyProfileArgs', 'GalleryApplicationVersionSafetyProfileArgsDict', 'GalleryArtifactVersionFullSourceArgs', 'GalleryArtifactVersionFullSourceArgsDict', 'GalleryDataDiskImageArgs', 'GalleryDataDiskImageArgsDict', 'GalleryDiskImageSourceArgs', 'GalleryDiskImageSourceArgsDict', 'GalleryExtendedLocationArgs', 'GalleryExtendedLocationArgsDict', 'GalleryIdentityArgs', 'GalleryIdentityArgsDict', 'GalleryImageFeatureArgs', 'GalleryImageFeatureArgsDict', 'GalleryImageIdentifierArgs', 'GalleryImageIdentifierArgsDict', 'GalleryImageVersionPublishingProfileArgs', 'GalleryImageVersionPublishingProfileArgsDict', 'GalleryImageVersionSafetyProfileArgs', 'GalleryImageVersionSafetyProfileArgsDict', 'GalleryImageVersionStorageProfileArgs', 'GalleryImageVersionStorageProfileArgsDict', 'GalleryImageVersionUefiSettingsArgs', 'GalleryImageVersionUefiSettingsArgsDict', 'GalleryInVMAccessControlProfilePropertiesArgs', 'GalleryInVMAccessControlProfilePropertiesArgsDict', 'GalleryOSDiskImageArgs', 'GalleryOSDiskImageArgsDict', 'GalleryScriptParameterArgs', 'GalleryScriptParameterArgsDict', 'GalleryScriptPropertiesArgs', 'GalleryScriptPropertiesArgsDict', 'GalleryScriptVersionPropertiesArgs', 'GalleryScriptVersionPropertiesArgsDict', 'GalleryScriptVersionPublishingProfileArgs', 'GalleryScriptVersionPublishingProfileArgsDict', 'GalleryScriptVersionSafetyProfileArgs', 'GalleryScriptVersionSafetyProfileArgsDict', 'GalleryTargetExtendedLocationArgs', 'GalleryTargetExtendedLocationArgsDict', 'HardwareProfileArgs', 'HardwareProfileArgsDict', 'HostEndpointSettingsArgs', 'HostEndpointSettingsArgsDict', 'ImageDataDiskArgs', 'ImageDataDiskArgsDict', 'ImageDiskReferenceArgs', 'ImageDiskReferenceArgsDict', 'ImageOSDiskArgs', 'ImageOSDiskArgsDict', 'ImagePurchasePlanArgs', 'ImagePurchasePlanArgsDict', 'ImageReferenceArgs', 'ImageReferenceArgsDict', 'ImageStorageProfileArgs', 'ImageStorageProfileArgsDict', 'ImageVersionSecurityProfileArgs', 'ImageVersionSecurityProfileArgsDict', 'InstanceViewStatusArgs', 'InstanceViewStatusArgsDict', 'KeyForDiskEncryptionSetArgs', 'KeyForDiskEncryptionSetArgsDict', 'KeyVaultAndKeyReferenceArgs', 'KeyVaultAndKeyReferenceArgsDict', 'KeyVaultAndSecretReferenceArgs', 'KeyVaultAndSecretReferenceArgsDict', 'KeyVaultKeyReferenceArgs', 'KeyVaultKeyReferenceArgsDict', 'KeyVaultSecretReferenceArgs', 'KeyVaultSecretReferenceArgsDict', 'LinuxConfigurationArgs', 'LinuxConfigurationArgsDict', 'LinuxPatchSettingsArgs', 'LinuxPatchSettingsArgsDict', 'LinuxVMGuestPatchAutomaticByPlatformSettingsArgs', ..., 'LoadBalancerConfigurationPropertiesArgs', 'LoadBalancerConfigurationPropertiesArgsDict', 'LoadBalancerConfigurationArgs', 'LoadBalancerConfigurationArgsDict', 'LoadBalancerFrontendIpConfigurationPropertiesArgs', ..., 'LoadBalancerFrontendIpConfigurationArgs', 'LoadBalancerFrontendIpConfigurationArgsDict', 'ManagedDiskParametersArgs', 'ManagedDiskParametersArgsDict', 'NetworkInterfaceReferenceArgs', 'NetworkInterfaceReferenceArgsDict', 'NetworkProfileArgs', 'NetworkProfileArgsDict', 'OSDiskImageEncryptionArgs', 'OSDiskImageEncryptionArgsDict', 'OSDiskImageSecurityProfileArgs', 'OSDiskImageSecurityProfileArgsDict', 'OSDiskArgs', 'OSDiskArgsDict', 'OSImageNotificationProfileArgs', 'OSImageNotificationProfileArgsDict', 'OSProfileArgs', 'OSProfileArgsDict', 'PatchSettingsArgs', 'PatchSettingsArgsDict', 'PlacementArgs', 'PlacementArgsDict', 'PlanArgs', 'PlanArgsDict', 'PriorityMixPolicyArgs', 'PriorityMixPolicyArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'ProximityPlacementGroupPropertiesIntentArgs', 'ProximityPlacementGroupPropertiesIntentArgsDict', 'ProxyAgentSettingsArgs', 'ProxyAgentSettingsArgsDict', 'PublicIPAddressSkuArgs', 'PublicIPAddressSkuArgsDict', 'RecommendedMachineConfigurationArgs', 'RecommendedMachineConfigurationArgsDict', 'ResiliencyPolicyArgs', 'ResiliencyPolicyArgsDict', 'ResilientVMCreationPolicyArgs', 'ResilientVMCreationPolicyArgsDict', 'ResilientVMDeletionPolicyArgs', 'ResilientVMDeletionPolicyArgsDict', 'ResourceRangeArgs', 'ResourceRangeArgsDict', 'ResourceSharingProfileArgs', 'ResourceSharingProfileArgsDict', 'RestorePointCollectionSourcePropertiesArgs', 'RestorePointCollectionSourcePropertiesArgsDict', 'RestorePointEncryptionArgs', 'RestorePointEncryptionArgsDict', 'RestorePointSourceMetadataArgs', 'RestorePointSourceMetadataArgsDict', 'RestorePointSourceVMDataDiskArgs', 'RestorePointSourceVMDataDiskArgsDict', 'RestorePointSourceVMOSDiskArgs', 'RestorePointSourceVMOSDiskArgsDict', 'RestorePointSourceVMStorageProfileArgs', 'RestorePointSourceVMStorageProfileArgsDict', 'RollingUpgradePolicyArgs', 'RollingUpgradePolicyArgsDict', 'RunCommandInputParameterArgs', 'RunCommandInputParameterArgsDict', 'RunCommandManagedIdentityArgs', 'RunCommandManagedIdentityArgsDict', 'ScaleInPolicyArgs', 'ScaleInPolicyArgsDict', 'ScheduledEventsAdditionalPublishingTargetsArgs', 'ScheduledEventsAdditionalPublishingTargetsArgsDict', 'ScheduledEventsPolicyArgs', 'ScheduledEventsPolicyArgsDict', 'ScheduledEventsProfileArgs', 'ScheduledEventsProfileArgsDict', 'ScriptSourceArgs', 'ScriptSourceArgsDict', 'SecurityPostureReferenceArgs', 'SecurityPostureReferenceArgsDict', 'SecurityProfileArgs', 'SecurityProfileArgsDict', 'ServiceArtifactReferenceArgs', 'ServiceArtifactReferenceArgsDict', 'SharingProfileArgs', 'SharingProfileArgsDict', 'SkuProfileVMSizeArgs', 'SkuProfileVMSizeArgsDict', 'SkuProfileArgs', 'SkuProfileArgsDict', 'SkuArgs', 'SkuArgsDict', 'SnapshotSkuArgs', 'SnapshotSkuArgsDict', 'SoftDeletePolicyArgs', 'SoftDeletePolicyArgsDict', 'SourceVaultArgs', 'SourceVaultArgsDict', 'SpotRestorePolicyArgs', 'SpotRestorePolicyArgsDict', 'SshConfigurationArgs', 'SshConfigurationArgsDict', 'SshPublicKeyArgs', 'SshPublicKeyArgsDict', 'StorageProfileArgs', 'StorageProfileArgsDict', 'SubResourceArgs', 'SubResourceArgsDict', 'SupportedCapabilitiesArgs', 'SupportedCapabilitiesArgsDict', 'TargetRegionArgs', 'TargetRegionArgsDict', 'TerminateNotificationProfileArgs', 'TerminateNotificationProfileArgsDict', 'UefiKeySignaturesArgs', 'UefiKeySignaturesArgsDict', 'UefiKeyArgs', 'UefiKeyArgsDict', 'UefiSettingsArgs', 'UefiSettingsArgsDict', 'UpgradePolicyArgs', 'UpgradePolicyArgsDict', 'UserArtifactManageArgs', 'UserArtifactManageArgsDict', 'UserArtifactSettingsArgs', 'UserArtifactSettingsArgsDict', 'UserArtifactSourceArgs', 'UserArtifactSourceArgsDict', 'UserInitiatedRebootArgs', 'UserInitiatedRebootArgsDict', 'UserInitiatedRedeployArgs', 'UserInitiatedRedeployArgsDict', 'VMDiskSecurityProfileArgs', 'VMDiskSecurityProfileArgsDict', 'VMGalleryApplicationArgs', 'VMGalleryApplicationArgsDict', 'VMSizePropertiesArgs', 'VMSizePropertiesArgsDict', 'VaultCertificateArgs', 'VaultCertificateArgsDict', 'VaultSecretGroupArgs', 'VaultSecretGroupArgsDict', 'VirtualHardDiskArgs', 'VirtualHardDiskArgsDict', 'VirtualMachineExtensionInstanceViewArgs', 'VirtualMachineExtensionInstanceViewArgsDict', 'VirtualMachineIdentityArgs', 'VirtualMachineIdentityArgsDict', 'VirtualMachineIpTagArgs', 'VirtualMachineIpTagArgsDict', 'VirtualMachineNetworkInterfaceConfigurationArgs', ..., ..., ..., 'VirtualMachineNetworkInterfaceIPConfigurationArgs', ..., 'VirtualMachinePublicIPAddressConfigurationArgs', 'VirtualMachinePublicIPAddressConfigurationArgsDict', ..., ..., 'VirtualMachineRunCommandScriptSourceArgs', 'VirtualMachineRunCommandScriptSourceArgsDict', 'VirtualMachineScaleSetDataDiskArgs', 'VirtualMachineScaleSetDataDiskArgsDict', 'VirtualMachineScaleSetExtensionProfileArgs', 'VirtualMachineScaleSetExtensionProfileArgsDict', 'VirtualMachineScaleSetExtensionArgs', 'VirtualMachineScaleSetExtensionArgsDict', 'VirtualMachineScaleSetHardwareProfileArgs', 'VirtualMachineScaleSetHardwareProfileArgsDict', 'VirtualMachineScaleSetIPConfigurationArgs', 'VirtualMachineScaleSetIPConfigurationArgsDict', 'VirtualMachineScaleSetIdentityArgs', 'VirtualMachineScaleSetIdentityArgsDict', 'VirtualMachineScaleSetIpTagArgs', 'VirtualMachineScaleSetIpTagArgsDict', 'VirtualMachineScaleSetManagedDiskParametersArgs', ..., ..., ..., 'VirtualMachineScaleSetNetworkConfigurationArgs', 'VirtualMachineScaleSetNetworkConfigurationArgsDict', 'VirtualMachineScaleSetNetworkProfileArgs', 'VirtualMachineScaleSetNetworkProfileArgsDict', 'VirtualMachineScaleSetOSDiskArgs', 'VirtualMachineScaleSetOSDiskArgsDict', 'VirtualMachineScaleSetOSProfileArgs', 'VirtualMachineScaleSetOSProfileArgsDict', ..., ..., ..., ..., 'VirtualMachineScaleSetStorageProfileArgs', 'VirtualMachineScaleSetStorageProfileArgsDict', ..., ..., 'VirtualMachineScaleSetVMProfileArgs', 'VirtualMachineScaleSetVMProfileArgsDict', 'VirtualMachineScaleSetVMProtectionPolicyArgs', 'VirtualMachineScaleSetVMProtectionPolicyArgsDict', 'WinRMConfigurationArgs', 'WinRMConfigurationArgsDict', 'WinRMListenerArgs', 'WinRMListenerArgsDict', 'WindowsConfigurationArgs', 'WindowsConfigurationArgsDict', 'WindowsVMGuestPatchAutomaticByPlatformSettingsArgs', ...]
class AccessControlRulesIdentityArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    exe_path: NotRequired[pulumi.Input[_builtins.str]]
    group_name: NotRequired[pulumi.Input[_builtins.str]]
    process_name: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AccessControlRulesIdentityArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], exe_path: Optional[pulumi.Input[_builtins.str]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., process_name: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exePath")
    def exe_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exe_path.setter
    def exe_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processName")
    def process_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @process_name.setter
    def process_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AccessControlRulesPrivilegeArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    query_parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AccessControlRulesPrivilegeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], path: pulumi.Input[_builtins.str], query_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AccessControlRulesRoleAssignmentArgsDict(TypedDict):
    
    identities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    role: pulumi.Input[_builtins.str]


@pulumi.input_type
class AccessControlRulesRoleAssignmentArgs:
    def __init__(__self__, *, identities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], role: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AccessControlRulesRoleArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    privileges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class AccessControlRulesRoleArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], privileges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def privileges(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @privileges.setter
    def privileges(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class AccessControlRulesArgsDict(TypedDict):
    
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesIdentityArgsDict]]]]
    privileges: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesPrivilegeArgsDict]]]]
    role_assignments: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleAssignmentArgsDict]]]]
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleArgsDict]]]]


@pulumi.input_type
class AccessControlRulesArgs:
    def __init__(__self__, *, identities: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesIdentityArgs]]]] = ..., privileges: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesPrivilegeArgs]]]] = ..., role_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleAssignmentArgs]]]] = ..., roles: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesIdentityArgs]]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesIdentityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesPrivilegeArgs]]]]:
        
        ...
    
    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesPrivilegeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleAssignments")
    def role_assignments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleAssignmentArgs]]]]:
        
        ...
    
    @role_assignments.setter
    def role_assignments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleAssignmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleArgs]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlRulesRoleArgs]]]]): # -> None:
        ...
    


class AdditionalCapabilitiesArgsDict(TypedDict):
    
    hibernation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ultra_ssd_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AdditionalCapabilitiesArgs:
    def __init__(__self__, *, hibernation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., ultra_ssd_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationEnabled")
    def hibernation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hibernation_enabled.setter
    def hibernation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ultraSSDEnabled")
    def ultra_ssd_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AdditionalReplicaSetArgsDict(TypedDict):
    
    regional_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountType]]]


@pulumi.input_type
class AdditionalReplicaSetArgs:
    def __init__(__self__, *, regional_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalReplicaCount")
    def regional_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @regional_replica_count.setter
    def regional_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]): # -> None:
        ...
    


class AdditionalUnattendContentArgsDict(TypedDict):
    
    component_name: NotRequired[pulumi.Input[ComponentName]]
    content: NotRequired[pulumi.Input[_builtins.str]]
    pass_name: NotRequired[pulumi.Input[PassName]]
    setting_name: NotRequired[pulumi.Input[SettingNames]]


@pulumi.input_type
class AdditionalUnattendContentArgs:
    def __init__(__self__, *, component_name: Optional[pulumi.Input[ComponentName]] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., pass_name: Optional[pulumi.Input[PassName]] = ..., setting_name: Optional[pulumi.Input[SettingNames]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[pulumi.Input[ComponentName]]:
        
        ...
    
    @component_name.setter
    def component_name(self, value: Optional[pulumi.Input[ComponentName]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passName")
    def pass_name(self) -> Optional[pulumi.Input[PassName]]:
        
        ...
    
    @pass_name.setter
    def pass_name(self, value: Optional[pulumi.Input[PassName]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[pulumi.Input[SettingNames]]:
        
        ...
    
    @setting_name.setter
    def setting_name(self, value: Optional[pulumi.Input[SettingNames]]): # -> None:
        ...
    


class ApiEntityReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationProfileArgsDict(TypedDict):
    
    gallery_applications: NotRequired[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgsDict]]]]


@pulumi.input_type
class ApplicationProfileArgs:
    def __init__(__self__, *, gallery_applications: Optional[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryApplications")
    def gallery_applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]]:
        
        ...
    
    @gallery_applications.setter
    def gallery_applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VMGalleryApplicationArgs]]]]): # -> None:
        ...
    


class AutomaticOSUpgradePolicyArgsDict(TypedDict):
    
    disable_automatic_rollback: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_os_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    os_rolling_upgrade_deferral: NotRequired[pulumi.Input[_builtins.bool]]
    use_rolling_upgrade_policy: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AutomaticOSUpgradePolicyArgs:
    def __init__(__self__, *, disable_automatic_rollback: Optional[pulumi.Input[_builtins.bool]] = ..., enable_automatic_os_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., os_rolling_upgrade_deferral: Optional[pulumi.Input[_builtins.bool]] = ..., use_rolling_upgrade_policy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAutomaticRollback")
    def disable_automatic_rollback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_automatic_rollback.setter
    def disable_automatic_rollback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticOSUpgrade")
    def enable_automatic_os_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_os_upgrade.setter
    def enable_automatic_os_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osRollingUpgradeDeferral")
    def os_rolling_upgrade_deferral(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @os_rolling_upgrade_deferral.setter
    def os_rolling_upgrade_deferral(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useRollingUpgradePolicy")
    def use_rolling_upgrade_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_rolling_upgrade_policy.setter
    def use_rolling_upgrade_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AutomaticRepairsPolicyArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    grace_period: NotRequired[pulumi.Input[_builtins.str]]
    repair_action: NotRequired[pulumi.Input[Union[_builtins.str, RepairAction]]]


@pulumi.input_type
class AutomaticRepairsPolicyArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., grace_period: Optional[pulumi.Input[_builtins.str]] = ..., repair_action: Optional[pulumi.Input[Union[_builtins.str, RepairAction]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gracePeriod")
    def grace_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grace_period.setter
    def grace_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repairAction")
    def repair_action(self) -> Optional[pulumi.Input[Union[_builtins.str, RepairAction]]]:
        
        ...
    
    @repair_action.setter
    def repair_action(self, value: Optional[pulumi.Input[Union[_builtins.str, RepairAction]]]): # -> None:
        ...
    


class AutomaticZoneRebalancingPolicyArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    rebalance_behavior: NotRequired[pulumi.Input[Union[_builtins.str, RebalanceBehavior]]]
    rebalance_strategy: NotRequired[pulumi.Input[Union[_builtins.str, RebalanceStrategy]]]


@pulumi.input_type
class AutomaticZoneRebalancingPolicyArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., rebalance_behavior: Optional[pulumi.Input[Union[_builtins.str, RebalanceBehavior]]] = ..., rebalance_strategy: Optional[pulumi.Input[Union[_builtins.str, RebalanceStrategy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebalanceBehavior")
    def rebalance_behavior(self) -> Optional[pulumi.Input[Union[_builtins.str, RebalanceBehavior]]]:
        
        ...
    
    @rebalance_behavior.setter
    def rebalance_behavior(self, value: Optional[pulumi.Input[Union[_builtins.str, RebalanceBehavior]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebalanceStrategy")
    def rebalance_strategy(self) -> Optional[pulumi.Input[Union[_builtins.str, RebalanceStrategy]]]:
        
        ...
    
    @rebalance_strategy.setter
    def rebalance_strategy(self, value: Optional[pulumi.Input[Union[_builtins.str, RebalanceStrategy]]]): # -> None:
        ...
    


class BillingProfileArgsDict(TypedDict):
    
    max_price: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class BillingProfileArgs:
    def __init__(__self__, *, max_price: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrice")
    def max_price(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_price.setter
    def max_price(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class BootDiagnosticsArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    storage_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BootDiagnosticsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., storage_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_uri.setter
    def storage_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CapacityReservationProfileArgsDict(TypedDict):
    
    capacity_reservation_group: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class CapacityReservationProfileArgs:
    def __init__(__self__, *, capacity_reservation_group: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroup")
    def capacity_reservation_group(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @capacity_reservation_group.setter
    def capacity_reservation_group(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class CloudServiceExtensionProfileArgsDict(TypedDict):
    
    extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExtensionArgsDict]]]]


@pulumi.input_type
class CloudServiceExtensionProfileArgs:
    def __init__(__self__, *, extensions: Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]]:
        
        ...
    
    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionArgs]]]]): # -> None:
        ...
    


class CloudServiceExtensionPropertiesArgsDict(TypedDict):
    
    auto_upgrade_minor_version: NotRequired[pulumi.Input[_builtins.bool]]
    force_update_tag: NotRequired[pulumi.Input[_builtins.str]]
    protected_settings: NotRequired[Any]
    protected_settings_from_key_vault: NotRequired[pulumi.Input[CloudServiceVaultAndSecretReferenceArgsDict]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    roles_applied_to: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    settings: NotRequired[Any]
    type: NotRequired[pulumi.Input[_builtins.str]]
    type_handler_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CloudServiceExtensionPropertiesArgs:
    def __init__(__self__, *, auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ..., force_update_tag: Optional[pulumi.Input[_builtins.str]] = ..., protected_settings: Optional[Any] = ..., protected_settings_from_key_vault: Optional[pulumi.Input[CloudServiceVaultAndSecretReferenceArgs]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., roles_applied_to: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., settings: Optional[Any] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(self) -> Optional[pulumi.Input[CloudServiceVaultAndSecretReferenceArgs]]:
        
        ...
    
    @protected_settings_from_key_vault.setter
    def protected_settings_from_key_vault(self, value: Optional[pulumi.Input[CloudServiceVaultAndSecretReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolesAppliedTo")
    def roles_applied_to(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @roles_applied_to.setter
    def roles_applied_to(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CloudServiceNetworkProfileArgsDict(TypedDict):
    
    load_balancer_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[LoadBalancerConfigurationArgsDict]]]]
    slot_type: NotRequired[pulumi.Input[Union[_builtins.str, CloudServiceSlotType]]]
    swappable_cloud_service: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class CloudServiceNetworkProfileArgs:
    def __init__(__self__, *, load_balancer_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerConfigurationArgs]]]] = ..., slot_type: Optional[pulumi.Input[Union[_builtins.str, CloudServiceSlotType]]] = ..., swappable_cloud_service: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerConfigurations")
    def load_balancer_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerConfigurationArgs]]]]:
        
        ...
    
    @load_balancer_configurations.setter
    def load_balancer_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotType")
    def slot_type(self) -> Optional[pulumi.Input[Union[_builtins.str, CloudServiceSlotType]]]:
        
        ...
    
    @slot_type.setter
    def slot_type(self, value: Optional[pulumi.Input[Union[_builtins.str, CloudServiceSlotType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="swappableCloudService")
    def swappable_cloud_service(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @swappable_cloud_service.setter
    def swappable_cloud_service(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class CloudServiceOsProfileArgsDict(TypedDict):
    
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultSecretGroupArgsDict]]]]


@pulumi.input_type
class CloudServiceOsProfileArgs:
    def __init__(__self__, *, secrets: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultSecretGroupArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultSecretGroupArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultSecretGroupArgs]]]]): # -> None:
        ...
    


class CloudServicePropertiesArgsDict(TypedDict):
    
    allow_model_override: NotRequired[pulumi.Input[_builtins.bool]]
    configuration: NotRequired[pulumi.Input[_builtins.str]]
    configuration_url: NotRequired[pulumi.Input[_builtins.str]]
    extension_profile: NotRequired[pulumi.Input[CloudServiceExtensionProfileArgsDict]]
    network_profile: NotRequired[pulumi.Input[CloudServiceNetworkProfileArgsDict]]
    os_profile: NotRequired[pulumi.Input[CloudServiceOsProfileArgsDict]]
    package_url: NotRequired[pulumi.Input[_builtins.str]]
    role_profile: NotRequired[pulumi.Input[CloudServiceRoleProfileArgsDict]]
    start_cloud_service: NotRequired[pulumi.Input[_builtins.bool]]
    upgrade_mode: NotRequired[pulumi.Input[Union[_builtins.str, CloudServiceUpgradeMode]]]


@pulumi.input_type
class CloudServicePropertiesArgs:
    def __init__(__self__, *, allow_model_override: Optional[pulumi.Input[_builtins.bool]] = ..., configuration: Optional[pulumi.Input[_builtins.str]] = ..., configuration_url: Optional[pulumi.Input[_builtins.str]] = ..., extension_profile: Optional[pulumi.Input[CloudServiceExtensionProfileArgs]] = ..., network_profile: Optional[pulumi.Input[CloudServiceNetworkProfileArgs]] = ..., os_profile: Optional[pulumi.Input[CloudServiceOsProfileArgs]] = ..., package_url: Optional[pulumi.Input[_builtins.str]] = ..., role_profile: Optional[pulumi.Input[CloudServiceRoleProfileArgs]] = ..., start_cloud_service: Optional[pulumi.Input[_builtins.bool]] = ..., upgrade_mode: Optional[pulumi.Input[Union[_builtins.str, CloudServiceUpgradeMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowModelOverride")
    def allow_model_override(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_model_override.setter
    def allow_model_override(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationUrl")
    def configuration_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_url.setter
    def configuration_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionProfile")
    def extension_profile(self) -> Optional[pulumi.Input[CloudServiceExtensionProfileArgs]]:
        
        ...
    
    @extension_profile.setter
    def extension_profile(self, value: Optional[pulumi.Input[CloudServiceExtensionProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[CloudServiceNetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[CloudServiceNetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[CloudServiceOsProfileArgs]]:
        
        ...
    
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[CloudServiceOsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageUrl")
    def package_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_url.setter
    def package_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleProfile")
    def role_profile(self) -> Optional[pulumi.Input[CloudServiceRoleProfileArgs]]:
        
        ...
    
    @role_profile.setter
    def role_profile(self, value: Optional[pulumi.Input[CloudServiceRoleProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startCloudService")
    def start_cloud_service(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @start_cloud_service.setter
    def start_cloud_service(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeMode")
    def upgrade_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, CloudServiceUpgradeMode]]]:
        
        ...
    
    @upgrade_mode.setter
    def upgrade_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, CloudServiceUpgradeMode]]]): # -> None:
        ...
    


class CloudServiceRoleProfilePropertiesArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[CloudServiceRoleSkuArgsDict]]


@pulumi.input_type
class CloudServiceRoleProfilePropertiesArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[CloudServiceRoleSkuArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[CloudServiceRoleSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[CloudServiceRoleSkuArgs]]): # -> None:
        ...
    


class CloudServiceRoleProfileArgsDict(TypedDict):
    
    roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[CloudServiceRoleProfilePropertiesArgsDict]]]]


@pulumi.input_type
class CloudServiceRoleProfileArgs:
    def __init__(__self__, *, roles: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceRoleProfilePropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceRoleProfilePropertiesArgs]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceRoleProfilePropertiesArgs]]]]): # -> None:
        ...
    


class CloudServiceRoleSkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.float]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CloudServiceRoleSkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CloudServiceVaultAndSecretReferenceArgsDict(TypedDict):
    
    secret_url: NotRequired[pulumi.Input[_builtins.str]]
    source_vault: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class CloudServiceVaultAndSecretReferenceArgs:
    def __init__(__self__, *, secret_url: Optional[pulumi.Input[_builtins.str]] = ..., source_vault: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_url.setter
    def secret_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class CloudServiceVaultCertificateArgsDict(TypedDict):
    
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CloudServiceVaultCertificateArgs:
    def __init__(__self__, *, certificate_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CloudServiceVaultSecretGroupArgsDict(TypedDict):
    
    source_vault: NotRequired[pulumi.Input[SubResourceArgsDict]]
    vault_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultCertificateArgsDict]]]]


@pulumi.input_type
class CloudServiceVaultSecretGroupArgs:
    def __init__(__self__, *, source_vault: Optional[pulumi.Input[SubResourceArgs]] = ..., vault_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultCertificateArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultCertificateArgs]]]]:
        
        ...
    
    @vault_certificates.setter
    def vault_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudServiceVaultCertificateArgs]]]]): # -> None:
        ...
    


class CommunityGalleryInfoArgsDict(TypedDict):
    
    eula: NotRequired[pulumi.Input[_builtins.str]]
    public_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    publisher_contact: NotRequired[pulumi.Input[_builtins.str]]
    publisher_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CommunityGalleryInfoArgs:
    def __init__(__self__, *, eula: Optional[pulumi.Input[_builtins.str]] = ..., public_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., publisher_contact: Optional[pulumi.Input[_builtins.str]] = ..., publisher_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eula(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eula.setter
    def eula(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNamePrefix")
    def public_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_name_prefix.setter
    def public_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherContact")
    def publisher_contact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher_contact.setter
    def publisher_contact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherUri")
    def publisher_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher_uri.setter
    def publisher_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CopyCompletionErrorArgsDict(TypedDict):
    
    error_code: pulumi.Input[Union[_builtins.str, CopyCompletionErrorReason]]
    error_message: pulumi.Input[_builtins.str]


@pulumi.input_type
class CopyCompletionErrorArgs:
    def __init__(__self__, *, error_code: pulumi.Input[Union[_builtins.str, CopyCompletionErrorReason]], error_message: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> pulumi.Input[Union[_builtins.str, CopyCompletionErrorReason]]:
        
        ...
    
    @error_code.setter
    def error_code(self, value: pulumi.Input[Union[_builtins.str, CopyCompletionErrorReason]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @error_message.setter
    def error_message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CreationDataArgsDict(TypedDict):
    
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOption]]
    elastic_san_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    gallery_image_reference: NotRequired[pulumi.Input[ImageDiskReferenceArgsDict]]
    image_reference: NotRequired[pulumi.Input[ImageDiskReferenceArgsDict]]
    logical_sector_size: NotRequired[pulumi.Input[_builtins.int]]
    performance_plus: NotRequired[pulumi.Input[_builtins.bool]]
    provisioned_bandwidth_copy_speed: NotRequired[pulumi.Input[Union[_builtins.str, ProvisionedBandwidthCopyOption]]]
    security_data_uri: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    source_uri: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    upload_size_bytes: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class CreationDataArgs:
    def __init__(__self__, *, create_option: pulumi.Input[Union[_builtins.str, DiskCreateOption]], elastic_san_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., gallery_image_reference: Optional[pulumi.Input[ImageDiskReferenceArgs]] = ..., image_reference: Optional[pulumi.Input[ImageDiskReferenceArgs]] = ..., logical_sector_size: Optional[pulumi.Input[_builtins.int]] = ..., performance_plus: Optional[pulumi.Input[_builtins.bool]] = ..., provisioned_bandwidth_copy_speed: Optional[pulumi.Input[Union[_builtins.str, ProvisionedBandwidthCopyOption]]] = ..., security_data_uri: Optional[pulumi.Input[_builtins.str]] = ..., source_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., source_uri: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_id: Optional[pulumi.Input[_builtins.str]] = ..., upload_size_bytes: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[Union[_builtins.str, DiskCreateOption]]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[Union[_builtins.str, DiskCreateOption]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSanResourceId")
    def elastic_san_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_san_resource_id.setter
    def elastic_san_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(self) -> Optional[pulumi.Input[ImageDiskReferenceArgs]]:
        
        ...
    
    @gallery_image_reference.setter
    def gallery_image_reference(self, value: Optional[pulumi.Input[ImageDiskReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[pulumi.Input[ImageDiskReferenceArgs]]:
        
        ...
    
    @image_reference.setter
    def image_reference(self, value: Optional[pulumi.Input[ImageDiskReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalSectorSize")
    def logical_sector_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @logical_sector_size.setter
    def logical_sector_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performancePlus")
    def performance_plus(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @performance_plus.setter
    def performance_plus(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedBandwidthCopySpeed")
    def provisioned_bandwidth_copy_speed(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisionedBandwidthCopyOption]]]:
        
        ...
    
    @provisioned_bandwidth_copy_speed.setter
    def provisioned_bandwidth_copy_speed(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisionedBandwidthCopyOption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityDataUri")
    def security_data_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_data_uri.setter
    def security_data_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadSizeBytes")
    def upload_size_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @upload_size_bytes.setter
    def upload_size_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class DataDiskImageEncryptionArgsDict(TypedDict):
    
    lun: pulumi.Input[_builtins.int]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataDiskImageEncryptionArgs:
    def __init__(__self__, *, lun: pulumi.Input[_builtins.int], disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataDiskArgsDict(TypedDict):
    
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    lun: pulumi.Input[_builtins.int]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    detach_option: NotRequired[pulumi.Input[Union[_builtins.str, DiskDetachOptionTypes]]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    image: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    managed_disk: NotRequired[pulumi.Input[ManagedDiskParametersArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_resource: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]
    to_be_detached: NotRequired[pulumi.Input[_builtins.bool]]
    vhd: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DataDiskArgs:
    def __init__(__self__, *, create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]], lun: pulumi.Input[_builtins.int], caching: Optional[pulumi.Input[CachingTypes]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]] = ..., detach_option: Optional[pulumi.Input[Union[_builtins.str, DiskDetachOptionTypes]]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., image: Optional[pulumi.Input[VirtualHardDiskArgs]] = ..., managed_disk: Optional[pulumi.Input[ManagedDiskParametersArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., source_resource: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ..., to_be_detached: Optional[pulumi.Input[_builtins.bool]] = ..., vhd: Optional[pulumi.Input[VirtualHardDiskArgs]] = ..., write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detachOption")
    def detach_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskDetachOptionTypes]]]:
        
        ...
    
    @detach_option.setter
    def detach_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDetachOptionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[ManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[ManagedDiskParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResource")
    def source_resource(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]:
        
        ...
    
    @source_resource.setter
    def source_resource(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toBeDetached")
    def to_be_detached(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @to_be_detached.setter
    def to_be_detached(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vhd(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]:
        
        ...
    
    @vhd.setter
    def vhd(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DedicatedHostGroupPropertiesAdditionalCapabilitiesArgsDict(TypedDict):
    
    ultra_ssd_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DedicatedHostGroupPropertiesAdditionalCapabilitiesArgs:
    def __init__(__self__, *, ultra_ssd_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ultraSSDEnabled")
    def ultra_ssd_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DiagnosticsProfileArgsDict(TypedDict):
    
    boot_diagnostics: NotRequired[pulumi.Input[BootDiagnosticsArgsDict]]


@pulumi.input_type
class DiagnosticsProfileArgs:
    def __init__(__self__, *, boot_diagnostics: Optional[pulumi.Input[BootDiagnosticsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiagnostics")
    def boot_diagnostics(self) -> Optional[pulumi.Input[BootDiagnosticsArgs]]:
        
        ...
    
    @boot_diagnostics.setter
    def boot_diagnostics(self, value: Optional[pulumi.Input[BootDiagnosticsArgs]]): # -> None:
        ...
    


class DiffDiskSettingsArgsDict(TypedDict):
    
    option: NotRequired[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]
    placement: NotRequired[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]


@pulumi.input_type
class DiffDiskSettingsArgs:
    def __init__(__self__, *, option: Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]] = ..., placement: Optional[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]:
        
        ...
    
    @option.setter
    def option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiffDiskOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[Union[_builtins.str, DiffDiskPlacement]]]): # -> None:
        ...
    


class DisallowedArgsDict(TypedDict):
    
    disk_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DisallowedArgs:
    def __init__(__self__, *, disk_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskTypes")
    def disk_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @disk_types.setter
    def disk_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DiskEncryptionSetParametersArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiskEncryptionSetParametersArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiskEncryptionSettingsArgsDict(TypedDict):
    
    disk_encryption_key: NotRequired[pulumi.Input[KeyVaultSecretReferenceArgsDict]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    key_encryption_key: NotRequired[pulumi.Input[KeyVaultKeyReferenceArgsDict]]


@pulumi.input_type
class DiskEncryptionSettingsArgs:
    def __init__(__self__, *, disk_encryption_key: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_encryption_key: Optional[pulumi.Input[KeyVaultKeyReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]:
        
        ...
    
    @disk_encryption_key.setter
    def disk_encryption_key(self, value: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyVaultKeyReferenceArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyVaultKeyReferenceArgs]]): # -> None:
        ...
    


class DiskPurchasePlanArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    product: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiskPurchasePlanArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], product: pulumi.Input[_builtins.str], publisher: pulumi.Input[_builtins.str], promotion_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product.setter
    def product(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiskRestorePointAttributesArgsDict(TypedDict):
    
    encryption: NotRequired[pulumi.Input[RestorePointEncryptionArgsDict]]
    source_disk_restore_point: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]


@pulumi.input_type
class DiskRestorePointAttributesArgs:
    def __init__(__self__, *, encryption: Optional[pulumi.Input[RestorePointEncryptionArgs]] = ..., source_disk_restore_point: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[RestorePointEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[RestorePointEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskRestorePoint")
    def source_disk_restore_point(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]:
        
        ...
    
    @source_disk_restore_point.setter
    def source_disk_restore_point(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): # -> None:
        ...
    


class DiskSecurityProfileArgsDict(TypedDict):
    
    secure_vm_disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    security_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskSecurityTypes]]]


@pulumi.input_type
class DiskSecurityProfileArgs:
    def __init__(__self__, *, secure_vm_disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ..., security_type: Optional[pulumi.Input[Union[_builtins.str, DiskSecurityTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureVMDiskEncryptionSetId")
    def secure_vm_disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secure_vm_disk_encryption_set_id.setter
    def secure_vm_disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskSecurityTypes]]]:
        
        ...
    
    @security_type.setter
    def security_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskSecurityTypes]]]): # -> None:
        ...
    


class DiskSkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[Union[_builtins.str, DiskStorageAccountTypes]]]


@pulumi.input_type
class DiskSkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[Union[_builtins.str, DiskStorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskStorageAccountTypes]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskStorageAccountTypes]]]): # -> None:
        ...
    


class EncryptionIdentityArgsDict(TypedDict):
    
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(__self__, *, user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionImagesArgsDict(TypedDict):
    
    data_disk_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataDiskImageEncryptionArgsDict]]]]
    os_disk_image: NotRequired[pulumi.Input[OSDiskImageEncryptionArgsDict]]


@pulumi.input_type
class EncryptionImagesArgs:
    def __init__(__self__, *, data_disk_images: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskImageEncryptionArgs]]]] = ..., os_disk_image: Optional[pulumi.Input[OSDiskImageEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskImages")
    def data_disk_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskImageEncryptionArgs]]]]:
        
        ...
    
    @data_disk_images.setter
    def data_disk_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskImageEncryptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskImage")
    def os_disk_image(self) -> Optional[pulumi.Input[OSDiskImageEncryptionArgs]]:
        
        ...
    
    @os_disk_image.setter
    def os_disk_image(self, value: Optional[pulumi.Input[OSDiskImageEncryptionArgs]]): # -> None:
        ...
    


class EncryptionSetIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, DiskEncryptionSetIdentityType]]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EncryptionSetIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, DiskEncryptionSetIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskEncryptionSetIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskEncryptionSetIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EncryptionSettingsCollectionArgsDict(TypedDict):
    
    enabled: pulumi.Input[_builtins.bool]
    encryption_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[EncryptionSettingsElementArgsDict]]]]
    encryption_settings_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionSettingsCollectionArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], encryption_settings: Optional[pulumi.Input[Sequence[pulumi.Input[EncryptionSettingsElementArgs]]]] = ..., encryption_settings_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EncryptionSettingsElementArgs]]]]:
        
        ...
    
    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EncryptionSettingsElementArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettingsVersion")
    def encryption_settings_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_settings_version.setter
    def encryption_settings_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionSettingsElementArgsDict(TypedDict):
    
    disk_encryption_key: NotRequired[pulumi.Input[KeyVaultAndSecretReferenceArgsDict]]
    key_encryption_key: NotRequired[pulumi.Input[KeyVaultAndKeyReferenceArgsDict]]


@pulumi.input_type
class EncryptionSettingsElementArgs:
    def __init__(__self__, *, disk_encryption_key: Optional[pulumi.Input[KeyVaultAndSecretReferenceArgs]] = ..., key_encryption_key: Optional[pulumi.Input[KeyVaultAndKeyReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[pulumi.Input[KeyVaultAndSecretReferenceArgs]]:
        
        ...
    
    @disk_encryption_key.setter
    def disk_encryption_key(self, value: Optional[pulumi.Input[KeyVaultAndSecretReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKey")
    def key_encryption_key(self) -> Optional[pulumi.Input[KeyVaultAndKeyReferenceArgs]]:
        
        ...
    
    @key_encryption_key.setter
    def key_encryption_key(self, value: Optional[pulumi.Input[KeyVaultAndKeyReferenceArgs]]): # -> None:
        ...
    


class EncryptionArgsDict(TypedDict):
    
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionType]]]


@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *, disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]]): # -> None:
        ...
    


class EventGridAndResourceGraphArgsDict(TypedDict):
    
    enable: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class EventGridAndResourceGraphArgs:
    def __init__(__self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]): # -> None:
        ...
    


class ExtensionArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[CloudServiceExtensionPropertiesArgsDict]]


@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[CloudServiceExtensionPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[CloudServiceExtensionPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[CloudServiceExtensionPropertiesArgs]]): # -> None:
        ...
    


class GalleryApplicationCustomActionParameterArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[GalleryApplicationCustomActionParameterType]]


@pulumi.input_type
class GalleryApplicationCustomActionParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], default_value: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., required: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[GalleryApplicationCustomActionParameterType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[GalleryApplicationCustomActionParameterType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[GalleryApplicationCustomActionParameterType]]): # -> None:
        ...
    


class GalleryApplicationCustomActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    script: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionParameterArgsDict]]]]


@pulumi.input_type
class GalleryApplicationCustomActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], script: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @script.setter
    def script(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionParameterArgs]]]]): # -> None:
        ...
    


class GalleryApplicationVersionPublishingProfileArgsDict(TypedDict):
    
    source: pulumi.Input[UserArtifactSourceArgsDict]
    advanced_settings: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    custom_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgsDict]]]]
    enable_health_check: NotRequired[pulumi.Input[_builtins.bool]]
    end_of_life_date: NotRequired[pulumi.Input[_builtins.str]]
    exclude_from_latest: NotRequired[pulumi.Input[_builtins.bool]]
    manage_actions: NotRequired[pulumi.Input[UserArtifactManageArgsDict]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]
    replication_mode: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationMode]]]
    settings: NotRequired[pulumi.Input[UserArtifactSettingsArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountType]]]
    target_extended_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgsDict]]]]
    target_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgsDict]]]]


@pulumi.input_type
class GalleryApplicationVersionPublishingProfileArgs:
    def __init__(__self__, *, source: pulumi.Input[UserArtifactSourceArgs], advanced_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]] = ..., enable_health_check: Optional[pulumi.Input[_builtins.bool]] = ..., end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., manage_actions: Optional[pulumi.Input[UserArtifactManageArgs]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., replication_mode: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]] = ..., settings: Optional[pulumi.Input[UserArtifactSettingsArgs]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]] = ..., target_extended_locations: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]] = ..., target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[UserArtifactSourceArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[UserArtifactSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]]:
        
        ...
    
    @custom_actions.setter
    def custom_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHealthCheck")
    def enable_health_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_health_check.setter
    def enable_health_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageActions")
    def manage_actions(self) -> Optional[pulumi.Input[UserArtifactManageArgs]]:
        ...
    
    @manage_actions.setter
    def manage_actions(self, value: Optional[pulumi.Input[UserArtifactManageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]:
        
        ...
    
    @replication_mode.setter
    def replication_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[UserArtifactSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[UserArtifactSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetExtendedLocations")
    def target_extended_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]:
        
        ...
    
    @target_extended_locations.setter
    def target_extended_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]:
        
        ...
    
    @target_regions.setter
    def target_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]): # -> None:
        ...
    


class GalleryApplicationVersionSafetyProfileArgsDict(TypedDict):
    
    allow_deletion_of_replicated_locations: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class GalleryApplicationVersionSafetyProfileArgs:
    def __init__(__self__, *, allow_deletion_of_replicated_locations: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDeletionOfReplicatedLocations")
    def allow_deletion_of_replicated_locations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_deletion_of_replicated_locations.setter
    def allow_deletion_of_replicated_locations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class GalleryArtifactVersionFullSourceArgsDict(TypedDict):
    
    community_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GalleryArtifactVersionFullSourceArgs:
    def __init__(__self__, *, community_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @community_gallery_image_id.setter
    def community_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GalleryDataDiskImageArgsDict(TypedDict):
    
    lun: pulumi.Input[_builtins.int]
    host_caching: NotRequired[pulumi.Input[HostCaching]]
    source: NotRequired[pulumi.Input[GalleryDiskImageSourceArgsDict]]


@pulumi.input_type
class GalleryDataDiskImageArgs:
    def __init__(__self__, *, lun: pulumi.Input[_builtins.int], host_caching: Optional[pulumi.Input[HostCaching]] = ..., source: Optional[pulumi.Input[GalleryDiskImageSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostCaching")
    def host_caching(self) -> Optional[pulumi.Input[HostCaching]]:
        
        ...
    
    @host_caching.setter
    def host_caching(self, value: Optional[pulumi.Input[HostCaching]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[GalleryDiskImageSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[GalleryDiskImageSourceArgs]]): # -> None:
        ...
    


class GalleryDiskImageSourceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GalleryDiskImageSourceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GalleryExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, GalleryExtendedLocationType]]]


@pulumi.input_type
class GalleryExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, GalleryExtendedLocationType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, GalleryExtendedLocationType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, GalleryExtendedLocationType]]]): # -> None:
        ...
    


class GalleryIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class GalleryIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class GalleryImageFeatureArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    starts_at_version: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GalleryImageFeatureArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., starts_at_version: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startsAtVersion")
    def starts_at_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @starts_at_version.setter
    def starts_at_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GalleryImageIdentifierArgsDict(TypedDict):
    
    offer: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    sku: pulumi.Input[_builtins.str]


@pulumi.input_type
class GalleryImageIdentifierArgs:
    def __init__(__self__, *, offer: pulumi.Input[_builtins.str], publisher: pulumi.Input[_builtins.str], sku: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @offer.setter
    def offer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sku.setter
    def sku(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GalleryImageVersionPublishingProfileArgsDict(TypedDict):
    
    end_of_life_date: NotRequired[pulumi.Input[_builtins.str]]
    exclude_from_latest: NotRequired[pulumi.Input[_builtins.bool]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]
    replication_mode: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationMode]]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountType]]]
    target_extended_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgsDict]]]]
    target_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgsDict]]]]


@pulumi.input_type
class GalleryImageVersionPublishingProfileArgs:
    def __init__(__self__, *, end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., replication_mode: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]] = ..., target_extended_locations: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]] = ..., target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]:
        
        ...
    
    @replication_mode.setter
    def replication_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetExtendedLocations")
    def target_extended_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]:
        
        ...
    
    @target_extended_locations.setter
    def target_extended_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]:
        
        ...
    
    @target_regions.setter
    def target_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]): # -> None:
        ...
    


class GalleryImageVersionSafetyProfileArgsDict(TypedDict):
    
    allow_deletion_of_replicated_locations: NotRequired[pulumi.Input[_builtins.bool]]
    block_deletion_before_end_of_life: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class GalleryImageVersionSafetyProfileArgs:
    def __init__(__self__, *, allow_deletion_of_replicated_locations: Optional[pulumi.Input[_builtins.bool]] = ..., block_deletion_before_end_of_life: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDeletionOfReplicatedLocations")
    def allow_deletion_of_replicated_locations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_deletion_of_replicated_locations.setter
    def allow_deletion_of_replicated_locations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeletionBeforeEndOfLife")
    def block_deletion_before_end_of_life(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_deletion_before_end_of_life.setter
    def block_deletion_before_end_of_life(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class GalleryImageVersionStorageProfileArgsDict(TypedDict):
    
    data_disk_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryDataDiskImageArgsDict]]]]
    os_disk_image: NotRequired[pulumi.Input[GalleryOSDiskImageArgsDict]]
    source: NotRequired[pulumi.Input[GalleryArtifactVersionFullSourceArgsDict]]


@pulumi.input_type
class GalleryImageVersionStorageProfileArgs:
    def __init__(__self__, *, data_disk_images: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryDataDiskImageArgs]]]] = ..., os_disk_image: Optional[pulumi.Input[GalleryOSDiskImageArgs]] = ..., source: Optional[pulumi.Input[GalleryArtifactVersionFullSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskImages")
    def data_disk_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryDataDiskImageArgs]]]]:
        
        ...
    
    @data_disk_images.setter
    def data_disk_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryDataDiskImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskImage")
    def os_disk_image(self) -> Optional[pulumi.Input[GalleryOSDiskImageArgs]]:
        
        ...
    
    @os_disk_image.setter
    def os_disk_image(self, value: Optional[pulumi.Input[GalleryOSDiskImageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[GalleryArtifactVersionFullSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[GalleryArtifactVersionFullSourceArgs]]): # -> None:
        ...
    


class GalleryImageVersionUefiSettingsArgsDict(TypedDict):
    
    additional_signatures: NotRequired[pulumi.Input[UefiKeySignaturesArgsDict]]
    signature_template_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, UefiSignatureTemplateName]]]]]


@pulumi.input_type
class GalleryImageVersionUefiSettingsArgs:
    def __init__(__self__, *, additional_signatures: Optional[pulumi.Input[UefiKeySignaturesArgs]] = ..., signature_template_names: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, UefiSignatureTemplateName]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalSignatures")
    def additional_signatures(self) -> Optional[pulumi.Input[UefiKeySignaturesArgs]]:
        
        ...
    
    @additional_signatures.setter
    def additional_signatures(self, value: Optional[pulumi.Input[UefiKeySignaturesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureTemplateNames")
    def signature_template_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, UefiSignatureTemplateName]]]]]:
        
        ...
    
    @signature_template_names.setter
    def signature_template_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, UefiSignatureTemplateName]]]]]): # -> None:
        ...
    


class GalleryInVMAccessControlProfilePropertiesArgsDict(TypedDict):
    
    applicable_host_endpoint: pulumi.Input[EndpointTypes]
    os_type: pulumi.Input[OperatingSystemTypes]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GalleryInVMAccessControlProfilePropertiesArgs:
    def __init__(__self__, *, applicable_host_endpoint: pulumi.Input[EndpointTypes], os_type: pulumi.Input[OperatingSystemTypes], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicableHostEndpoint")
    def applicable_host_endpoint(self) -> pulumi.Input[EndpointTypes]:
        
        ...
    
    @applicable_host_endpoint.setter
    def applicable_host_endpoint(self, value: pulumi.Input[EndpointTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[OperatingSystemTypes]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: pulumi.Input[OperatingSystemTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GalleryOSDiskImageArgsDict(TypedDict):
    
    host_caching: NotRequired[pulumi.Input[HostCaching]]
    source: NotRequired[pulumi.Input[GalleryDiskImageSourceArgsDict]]


@pulumi.input_type
class GalleryOSDiskImageArgs:
    def __init__(__self__, *, host_caching: Optional[pulumi.Input[HostCaching]] = ..., source: Optional[pulumi.Input[GalleryDiskImageSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostCaching")
    def host_caching(self) -> Optional[pulumi.Input[HostCaching]]:
        
        ...
    
    @host_caching.setter
    def host_caching(self, value: Optional[pulumi.Input[HostCaching]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[GalleryDiskImageSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[GalleryDiskImageSourceArgs]]): # -> None:
        ...
    


class GalleryScriptParameterArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enum_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_value: NotRequired[pulumi.Input[_builtins.str]]
    min_value: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, GalleryScriptParameterType]]]


@pulumi.input_type
class GalleryScriptParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], default_value: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enum_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_value: Optional[pulumi.Input[_builtins.str]] = ..., min_value: Optional[pulumi.Input[_builtins.str]] = ..., required: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, GalleryScriptParameterType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enumValues")
    def enum_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enum_values.setter
    def enum_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, GalleryScriptParameterType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, GalleryScriptParameterType]]]): # -> None:
        ...
    


class GalleryScriptPropertiesArgsDict(TypedDict):
    
    supported_os_type: pulumi.Input[OperatingSystemTypes]
    description: NotRequired[pulumi.Input[_builtins.str]]
    end_of_life_date: NotRequired[pulumi.Input[_builtins.str]]
    eula: NotRequired[pulumi.Input[_builtins.str]]
    privacy_statement_uri: NotRequired[pulumi.Input[_builtins.str]]
    release_note_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GalleryScriptPropertiesArgs:
    def __init__(__self__, *, supported_os_type: pulumi.Input[OperatingSystemTypes], description: Optional[pulumi.Input[_builtins.str]] = ..., end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., eula: Optional[pulumi.Input[_builtins.str]] = ..., privacy_statement_uri: Optional[pulumi.Input[_builtins.str]] = ..., release_note_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> pulumi.Input[OperatingSystemTypes]:
        
        ...
    
    @supported_os_type.setter
    def supported_os_type(self, value: pulumi.Input[OperatingSystemTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def eula(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eula.setter
    def eula(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @privacy_statement_uri.setter
    def privacy_statement_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_note_uri.setter
    def release_note_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GalleryScriptVersionPropertiesArgsDict(TypedDict):
    
    publishing_profile: pulumi.Input[GalleryScriptVersionPublishingProfileArgsDict]
    safety_profile: NotRequired[pulumi.Input[GalleryScriptVersionSafetyProfileArgsDict]]


@pulumi.input_type
class GalleryScriptVersionPropertiesArgs:
    def __init__(__self__, *, publishing_profile: pulumi.Input[GalleryScriptVersionPublishingProfileArgs], safety_profile: Optional[pulumi.Input[GalleryScriptVersionSafetyProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(self) -> pulumi.Input[GalleryScriptVersionPublishingProfileArgs]:
        
        ...
    
    @publishing_profile.setter
    def publishing_profile(self, value: pulumi.Input[GalleryScriptVersionPublishingProfileArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(self) -> Optional[pulumi.Input[GalleryScriptVersionSafetyProfileArgs]]:
        
        ...
    
    @safety_profile.setter
    def safety_profile(self, value: Optional[pulumi.Input[GalleryScriptVersionSafetyProfileArgs]]): # -> None:
        ...
    


class GalleryScriptVersionPublishingProfileArgsDict(TypedDict):
    
    source: pulumi.Input[ScriptSourceArgsDict]
    end_of_life_date: NotRequired[pulumi.Input[_builtins.str]]
    exclude_from_latest: NotRequired[pulumi.Input[_builtins.bool]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]
    replication_mode: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationMode]]]
    storage_account_strategy: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountStrategy]]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountType]]]
    target_extended_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgsDict]]]]
    target_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgsDict]]]]


@pulumi.input_type
class GalleryScriptVersionPublishingProfileArgs:
    def __init__(__self__, *, source: pulumi.Input[ScriptSourceArgs], end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., replication_mode: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]] = ..., storage_account_strategy: Optional[pulumi.Input[Union[_builtins.str, StorageAccountStrategy]]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]] = ..., target_extended_locations: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]] = ..., target_regions: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[ScriptSourceArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[ScriptSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]:
        
        ...
    
    @replication_mode.setter
    def replication_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountStrategy")
    def storage_account_strategy(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountStrategy]]]:
        
        ...
    
    @storage_account_strategy.setter
    def storage_account_strategy(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountStrategy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetExtendedLocations")
    def target_extended_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]:
        
        ...
    
    @target_extended_locations.setter
    def target_extended_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryTargetExtendedLocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRegions")
    def target_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]:
        
        ...
    
    @target_regions.setter
    def target_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TargetRegionArgs]]]]): # -> None:
        ...
    


class GalleryScriptVersionSafetyProfileArgsDict(TypedDict):
    
    allow_deletion_of_replicated_locations: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class GalleryScriptVersionSafetyProfileArgs:
    def __init__(__self__, *, allow_deletion_of_replicated_locations: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDeletionOfReplicatedLocations")
    def allow_deletion_of_replicated_locations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_deletion_of_replicated_locations.setter
    def allow_deletion_of_replicated_locations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class GalleryTargetExtendedLocationArgsDict(TypedDict):
    encryption: NotRequired[pulumi.Input[EncryptionImagesArgsDict]]
    extended_location: NotRequired[pulumi.Input[GalleryExtendedLocationArgsDict]]
    extended_location_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, EdgeZoneStorageAccountType]]]


@pulumi.input_type
class GalleryTargetExtendedLocationArgs:
    def __init__(__self__, *, encryption: Optional[pulumi.Input[EncryptionImagesArgs]] = ..., extended_location: Optional[pulumi.Input[GalleryExtendedLocationArgs]] = ..., extended_location_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, EdgeZoneStorageAccountType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionImagesArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionImagesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[GalleryExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[GalleryExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocationReplicaCount")
    def extended_location_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @extended_location_replica_count.setter
    def extended_location_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EdgeZoneStorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EdgeZoneStorageAccountType]]]): # -> None:
        ...
    


class HardwareProfileArgsDict(TypedDict):
    
    vm_size: NotRequired[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]]
    vm_size_properties: NotRequired[pulumi.Input[VMSizePropertiesArgsDict]]


@pulumi.input_type
class HardwareProfileArgs:
    def __init__(__self__, *, vm_size: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]] = ..., vm_size_properties: Optional[pulumi.Input[VMSizePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]]:
        
        ...
    
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineSizeTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSizeProperties")
    def vm_size_properties(self) -> Optional[pulumi.Input[VMSizePropertiesArgs]]:
        
        ...
    
    @vm_size_properties.setter
    def vm_size_properties(self, value: Optional[pulumi.Input[VMSizePropertiesArgs]]): # -> None:
        ...
    


class HostEndpointSettingsArgsDict(TypedDict):
    
    in_vm_access_control_profile_reference_id: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Modes]]]


@pulumi.input_type
class HostEndpointSettingsArgs:
    def __init__(__self__, *, in_vm_access_control_profile_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, Modes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inVMAccessControlProfileReferenceId")
    def in_vm_access_control_profile_reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_vm_access_control_profile_reference_id.setter
    def in_vm_access_control_profile_reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Modes]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Modes]]]): # -> None:
        ...
    


class ImageDataDiskArgsDict(TypedDict):
    
    lun: pulumi.Input[_builtins.int]
    blob_uri: NotRequired[pulumi.Input[_builtins.str]]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    managed_disk: NotRequired[pulumi.Input[SubResourceArgsDict]]
    snapshot: NotRequired[pulumi.Input[SubResourceArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]


@pulumi.input_type
class ImageDataDiskArgs:
    def __init__(__self__, *, lun: pulumi.Input[_builtins.int], blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., caching: Optional[pulumi.Input[CachingTypes]] = ..., disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., managed_disk: Optional[pulumi.Input[SubResourceArgs]] = ..., snapshot: Optional[pulumi.Input[SubResourceArgs]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobUri")
    def blob_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_uri.setter
    def blob_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]): # -> None:
        ...
    


class ImageDiskReferenceArgsDict(TypedDict):
    
    community_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    lun: NotRequired[pulumi.Input[_builtins.int]]
    shared_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImageDiskReferenceArgs:
    def __init__(__self__, *, community_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., lun: Optional[pulumi.Input[_builtins.int]] = ..., shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @community_gallery_image_id.setter
    def community_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lun.setter
    def lun(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_gallery_image_id.setter
    def shared_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ImageOSDiskArgsDict(TypedDict):
    
    os_state: pulumi.Input[OperatingSystemStateTypes]
    os_type: pulumi.Input[OperatingSystemTypes]
    blob_uri: NotRequired[pulumi.Input[_builtins.str]]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    managed_disk: NotRequired[pulumi.Input[SubResourceArgsDict]]
    snapshot: NotRequired[pulumi.Input[SubResourceArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]


@pulumi.input_type
class ImageOSDiskArgs:
    def __init__(__self__, *, os_state: pulumi.Input[OperatingSystemStateTypes], os_type: pulumi.Input[OperatingSystemTypes], blob_uri: Optional[pulumi.Input[_builtins.str]] = ..., caching: Optional[pulumi.Input[CachingTypes]] = ..., disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., managed_disk: Optional[pulumi.Input[SubResourceArgs]] = ..., snapshot: Optional[pulumi.Input[SubResourceArgs]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osState")
    def os_state(self) -> pulumi.Input[OperatingSystemStateTypes]:
        
        ...
    
    @os_state.setter
    def os_state(self, value: pulumi.Input[OperatingSystemStateTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[OperatingSystemTypes]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: pulumi.Input[OperatingSystemTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobUri")
    def blob_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_uri.setter
    def blob_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]): # -> None:
        ...
    


class ImagePurchasePlanArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImagePurchasePlanArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., product: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


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
    def __init__(__self__, *, community_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., offer: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @community_gallery_image_id.setter
    def community_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_gallery_image_id.setter
    def shared_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ImageStorageProfileArgsDict(TypedDict):
    
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[ImageDataDiskArgsDict]]]]
    os_disk: NotRequired[pulumi.Input[ImageOSDiskArgsDict]]
    zone_resilient: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ImageStorageProfileArgs:
    def __init__(__self__, *, data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[ImageDataDiskArgs]]]] = ..., os_disk: Optional[pulumi.Input[ImageOSDiskArgs]] = ..., zone_resilient: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageDataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageDataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[ImageOSDiskArgs]]:
        
        ...
    
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[ImageOSDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneResilient")
    def zone_resilient(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zone_resilient.setter
    def zone_resilient(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ImageVersionSecurityProfileArgsDict(TypedDict):
    
    uefi_settings: NotRequired[pulumi.Input[GalleryImageVersionUefiSettingsArgsDict]]


@pulumi.input_type
class ImageVersionSecurityProfileArgs:
    def __init__(__self__, *, uefi_settings: Optional[pulumi.Input[GalleryImageVersionUefiSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[pulumi.Input[GalleryImageVersionUefiSettingsArgs]]:
        
        ...
    
    @uefi_settings.setter
    def uefi_settings(self, value: Optional[pulumi.Input[GalleryImageVersionUefiSettingsArgs]]): # -> None:
        ...
    


class InstanceViewStatusArgsDict(TypedDict):
    
    code: NotRequired[pulumi.Input[_builtins.str]]
    display_status: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[StatusLevelTypes]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceViewStatusArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.str]] = ..., display_status: Optional[pulumi.Input[_builtins.str]] = ..., level: Optional[pulumi.Input[StatusLevelTypes]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_status.setter
    def display_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[StatusLevelTypes]]:
        
        ...
    
    @level.setter
    def level(self, value: Optional[pulumi.Input[StatusLevelTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time.setter
    def time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyForDiskEncryptionSetArgsDict(TypedDict):
    
    key_url: pulumi.Input[_builtins.str]
    source_vault: NotRequired[pulumi.Input[SourceVaultArgsDict]]


@pulumi.input_type
class KeyForDiskEncryptionSetArgs:
    def __init__(__self__, *, key_url: pulumi.Input[_builtins.str], source_vault: Optional[pulumi.Input[SourceVaultArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_url.setter
    def key_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[pulumi.Input[SourceVaultArgs]]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: Optional[pulumi.Input[SourceVaultArgs]]): # -> None:
        ...
    


class KeyVaultAndKeyReferenceArgsDict(TypedDict):
    
    key_url: pulumi.Input[_builtins.str]
    source_vault: pulumi.Input[SourceVaultArgsDict]


@pulumi.input_type
class KeyVaultAndKeyReferenceArgs:
    def __init__(__self__, *, key_url: pulumi.Input[_builtins.str], source_vault: pulumi.Input[SourceVaultArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_url.setter
    def key_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SourceVaultArgs]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SourceVaultArgs]): # -> None:
        ...
    


class KeyVaultAndSecretReferenceArgsDict(TypedDict):
    
    secret_url: pulumi.Input[_builtins.str]
    source_vault: pulumi.Input[SourceVaultArgsDict]


@pulumi.input_type
class KeyVaultAndSecretReferenceArgs:
    def __init__(__self__, *, secret_url: pulumi.Input[_builtins.str], source_vault: pulumi.Input[SourceVaultArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_url.setter
    def secret_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SourceVaultArgs]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SourceVaultArgs]): # -> None:
        ...
    


class KeyVaultKeyReferenceArgsDict(TypedDict):
    
    key_url: pulumi.Input[_builtins.str]
    source_vault: pulumi.Input[SubResourceArgsDict]


@pulumi.input_type
class KeyVaultKeyReferenceArgs:
    def __init__(__self__, *, key_url: pulumi.Input[_builtins.str], source_vault: pulumi.Input[SubResourceArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_url.setter
    def key_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SubResourceArgs]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SubResourceArgs]): # -> None:
        ...
    


class KeyVaultSecretReferenceArgsDict(TypedDict):
    
    secret_url: pulumi.Input[_builtins.str]
    source_vault: pulumi.Input[SubResourceArgsDict]


@pulumi.input_type
class KeyVaultSecretReferenceArgs:
    def __init__(__self__, *, secret_url: pulumi.Input[_builtins.str], source_vault: pulumi.Input[SubResourceArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUrl")
    def secret_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_url.setter
    def secret_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SubResourceArgs]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SubResourceArgs]): # -> None:
        ...
    


class LinuxConfigurationArgsDict(TypedDict):
    
    disable_password_authentication: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vm_agent_platform_updates: NotRequired[pulumi.Input[_builtins.bool]]
    patch_settings: NotRequired[pulumi.Input[LinuxPatchSettingsArgsDict]]
    provision_vm_agent: NotRequired[pulumi.Input[_builtins.bool]]
    ssh: NotRequired[pulumi.Input[SshConfigurationArgsDict]]


@pulumi.input_type
class LinuxConfigurationArgs:
    def __init__(__self__, *, disable_password_authentication: Optional[pulumi.Input[_builtins.bool]] = ..., enable_vm_agent_platform_updates: Optional[pulumi.Input[_builtins.bool]] = ..., patch_settings: Optional[pulumi.Input[LinuxPatchSettingsArgs]] = ..., provision_vm_agent: Optional[pulumi.Input[_builtins.bool]] = ..., ssh: Optional[pulumi.Input[SshConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disablePasswordAuthentication")
    def disable_password_authentication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_password_authentication.setter
    def disable_password_authentication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVMAgentPlatformUpdates")
    def enable_vm_agent_platform_updates(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_vm_agent_platform_updates.setter
    def enable_vm_agent_platform_updates(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[pulumi.Input[LinuxPatchSettingsArgs]]:
        
        ...
    
    @patch_settings.setter
    def patch_settings(self, value: Optional[pulumi.Input[LinuxPatchSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @provision_vm_agent.setter
    def provision_vm_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[pulumi.Input[SshConfigurationArgs]]:
        
        ...
    
    @ssh.setter
    def ssh(self, value: Optional[pulumi.Input[SshConfigurationArgs]]): # -> None:
        ...
    


class LinuxPatchSettingsArgsDict(TypedDict):
    
    assessment_mode: NotRequired[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]]
    automatic_by_platform_settings: NotRequired[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgsDict]]
    patch_mode: NotRequired[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]


@pulumi.input_type
class LinuxPatchSettingsArgs:
    def __init__(__self__, *, assessment_mode: Optional[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]] = ..., automatic_by_platform_settings: Optional[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]] = ..., patch_mode: Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]]:
        
        ...
    
    @assessment_mode.setter
    def assessment_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxPatchAssessmentMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(self) -> Optional[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]]:
        
        ...
    
    @automatic_by_platform_settings.setter
    def automatic_by_platform_settings(self, value: Optional[pulumi.Input[LinuxVMGuestPatchAutomaticByPlatformSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]:
        
        ...
    
    @patch_mode.setter
    def patch_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchMode]]]): # -> None:
        ...
    


class LinuxVMGuestPatchAutomaticByPlatformSettingsArgsDict(TypedDict):
    
    bypass_platform_safety_checks_on_user_schedule: NotRequired[pulumi.Input[_builtins.bool]]
    reboot_setting: NotRequired[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]]]


@pulumi.input_type
class LinuxVMGuestPatchAutomaticByPlatformSettingsArgs:
    def __init__(__self__, *, bypass_platform_safety_checks_on_user_schedule: Optional[pulumi.Input[_builtins.bool]] = ..., reboot_setting: Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bypass_platform_safety_checks_on_user_schedule.setter
    def bypass_platform_safety_checks_on_user_schedule(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]]]:
        
        ...
    
    @reboot_setting.setter
    def reboot_setting(self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxVMGuestPatchAutomaticByPlatformRebootSetting]]]): # -> None:
        ...
    


class LoadBalancerConfigurationPropertiesArgsDict(TypedDict):
    
    frontend_ip_configurations: pulumi.Input[Sequence[pulumi.Input[LoadBalancerFrontendIpConfigurationArgsDict]]]


@pulumi.input_type
class LoadBalancerConfigurationPropertiesArgs:
    def __init__(__self__, *, frontend_ip_configurations: pulumi.Input[Sequence[pulumi.Input[LoadBalancerFrontendIpConfigurationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendIpConfigurations")
    def frontend_ip_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[LoadBalancerFrontendIpConfigurationArgs]]]:
        
        ...
    
    @frontend_ip_configurations.setter
    def frontend_ip_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[LoadBalancerFrontendIpConfigurationArgs]]]): # -> None:
        ...
    


class LoadBalancerConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    properties: pulumi.Input[LoadBalancerConfigurationPropertiesArgsDict]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], properties: pulumi.Input[LoadBalancerConfigurationPropertiesArgs], id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[LoadBalancerConfigurationPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[LoadBalancerConfigurationPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerFrontendIpConfigurationPropertiesArgsDict(TypedDict):
    
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_address: NotRequired[pulumi.Input[SubResourceArgsDict]]
    subnet: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class LoadBalancerFrontendIpConfigurationPropertiesArgs:
    def __init__(__self__, *, private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[SubResourceArgs]] = ..., subnet: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class LoadBalancerFrontendIpConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    properties: pulumi.Input[LoadBalancerFrontendIpConfigurationPropertiesArgsDict]


@pulumi.input_type
class LoadBalancerFrontendIpConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], properties: pulumi.Input[LoadBalancerFrontendIpConfigurationPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[LoadBalancerFrontendIpConfigurationPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[LoadBalancerFrontendIpConfigurationPropertiesArgs]): # -> None:
        ...
    


class ManagedDiskParametersArgsDict(TypedDict):
    
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    security_profile: NotRequired[pulumi.Input[VMDiskSecurityProfileArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]


@pulumi.input_type
class ManagedDiskParametersArgs:
    def __init__(__self__, *, disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., security_profile: Optional[pulumi.Input[VMDiskSecurityProfileArgs]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[VMDiskSecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[VMDiskSecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]): # -> None:
        ...
    


class NetworkInterfaceReferenceArgsDict(TypedDict):
    
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class NetworkInterfaceReferenceArgs:
    def __init__(__self__, *, delete_option: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., primary: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class NetworkProfileArgsDict(TypedDict):
    
    network_api_version: NotRequired[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]
    network_interface_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceConfigurationArgsDict]]]]
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceReferenceArgsDict]]]]


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *, network_api_version: Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]] = ..., network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceConfigurationArgs]]]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceReferenceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkApiVersion")
    def network_api_version(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]:
        
        ...
    
    @network_api_version.setter
    def network_api_version(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceConfigurationArgs]]]]:
        
        ...
    
    @network_interface_configurations.setter
    def network_interface_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceReferenceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfaceReferenceArgs]]]]): # -> None:
        ...
    


class OSDiskImageEncryptionArgsDict(TypedDict):
    
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    security_profile: NotRequired[pulumi.Input[OSDiskImageSecurityProfileArgsDict]]


@pulumi.input_type
class OSDiskImageEncryptionArgs:
    def __init__(__self__, *, disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ..., security_profile: Optional[pulumi.Input[OSDiskImageSecurityProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[OSDiskImageSecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[OSDiskImageSecurityProfileArgs]]): # -> None:
        ...
    


class OSDiskImageSecurityProfileArgsDict(TypedDict):
    
    confidential_vm_encryption_type: NotRequired[pulumi.Input[Union[_builtins.str, ConfidentialVMEncryptionType]]]
    secure_vm_disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OSDiskImageSecurityProfileArgs:
    def __init__(__self__, *, confidential_vm_encryption_type: Optional[pulumi.Input[Union[_builtins.str, ConfidentialVMEncryptionType]]] = ..., secure_vm_disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialVMEncryptionType")
    def confidential_vm_encryption_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ConfidentialVMEncryptionType]]]:
        
        ...
    
    @confidential_vm_encryption_type.setter
    def confidential_vm_encryption_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ConfidentialVMEncryptionType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureVMDiskEncryptionSetId")
    def secure_vm_disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secure_vm_disk_encryption_set_id.setter
    def secure_vm_disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OSDiskArgsDict(TypedDict):
    
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    diff_disk_settings: NotRequired[pulumi.Input[DiffDiskSettingsArgsDict]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    encryption_settings: NotRequired[pulumi.Input[DiskEncryptionSettingsArgsDict]]
    image: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    managed_disk: NotRequired[pulumi.Input[ManagedDiskParametersArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[OperatingSystemTypes]]
    vhd: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class OSDiskArgs:
    def __init__(__self__, *, create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]], caching: Optional[pulumi.Input[CachingTypes]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]] = ..., diff_disk_settings: Optional[pulumi.Input[DiffDiskSettingsArgs]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., encryption_settings: Optional[pulumi.Input[DiskEncryptionSettingsArgs]] = ..., image: Optional[pulumi.Input[VirtualHardDiskArgs]] = ..., managed_disk: Optional[pulumi.Input[ManagedDiskParametersArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ..., vhd: Optional[pulumi.Input[VirtualHardDiskArgs]] = ..., write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diffDiskSettings")
    def diff_disk_settings(self) -> Optional[pulumi.Input[DiffDiskSettingsArgs]]:
        
        ...
    
    @diff_disk_settings.setter
    def diff_disk_settings(self, value: Optional[pulumi.Input[DiffDiskSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input[DiskEncryptionSettingsArgs]]:
        
        ...
    
    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input[DiskEncryptionSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[ManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[ManagedDiskParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[OperatingSystemTypes]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[OperatingSystemTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vhd(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]:
        
        ...
    
    @vhd.setter
    def vhd(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class OSImageNotificationProfileArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    not_before_timeout: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OSImageNotificationProfileArgs:
    def __init__(__self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ..., not_before_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_before_timeout.setter
    def not_before_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OSProfileArgsDict(TypedDict):
    
    admin_password: NotRequired[pulumi.Input[_builtins.str]]
    admin_username: NotRequired[pulumi.Input[_builtins.str]]
    allow_extension_operations: NotRequired[pulumi.Input[_builtins.bool]]
    computer_name: NotRequired[pulumi.Input[_builtins.str]]
    custom_data: NotRequired[pulumi.Input[_builtins.str]]
    linux_configuration: NotRequired[pulumi.Input[LinuxConfigurationArgsDict]]
    require_guest_provision_signal: NotRequired[pulumi.Input[_builtins.bool]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgsDict]]]]
    windows_configuration: NotRequired[pulumi.Input[WindowsConfigurationArgsDict]]


@pulumi.input_type
class OSProfileArgs:
    def __init__(__self__, *, admin_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., allow_extension_operations: Optional[pulumi.Input[_builtins.bool]] = ..., computer_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_data: Optional[pulumi.Input[_builtins.str]] = ..., linux_configuration: Optional[pulumi.Input[LinuxConfigurationArgs]] = ..., require_guest_provision_signal: Optional[pulumi.Input[_builtins.bool]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]] = ..., windows_configuration: Optional[pulumi.Input[WindowsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_extension_operations.setter
    def allow_extension_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[pulumi.Input[LinuxConfigurationArgs]]:
        
        ...
    
    @linux_configuration.setter
    def linux_configuration(self, value: Optional[pulumi.Input[LinuxConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireGuestProvisionSignal")
    def require_guest_provision_signal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_guest_provision_signal.setter
    def require_guest_provision_signal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[pulumi.Input[WindowsConfigurationArgs]]:
        
        ...
    
    @windows_configuration.setter
    def windows_configuration(self, value: Optional[pulumi.Input[WindowsConfigurationArgs]]): # -> None:
        ...
    


class PatchSettingsArgsDict(TypedDict):
    
    assessment_mode: NotRequired[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]]
    automatic_by_platform_settings: NotRequired[pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgsDict]]
    enable_hotpatching: NotRequired[pulumi.Input[_builtins.bool]]
    patch_mode: NotRequired[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]]


@pulumi.input_type
class PatchSettingsArgs:
    def __init__(__self__, *, assessment_mode: Optional[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]] = ..., automatic_by_platform_settings: Optional[pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]] = ..., enable_hotpatching: Optional[pulumi.Input[_builtins.bool]] = ..., patch_mode: Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]]:
        
        ...
    
    @assessment_mode.setter
    def assessment_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, WindowsPatchAssessmentMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticByPlatformSettings")
    def automatic_by_platform_settings(self) -> Optional[pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]]:
        
        ...
    
    @automatic_by_platform_settings.setter
    def automatic_by_platform_settings(self, value: Optional[pulumi.Input[WindowsVMGuestPatchAutomaticByPlatformSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_hotpatching.setter
    def enable_hotpatching(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]]:
        
        ...
    
    @patch_mode.setter
    def patch_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchMode]]]): # -> None:
        ...
    


class PlacementArgsDict(TypedDict):
    
    exclude_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zone_placement_policy: NotRequired[pulumi.Input[Union[_builtins.str, ZonePlacementPolicyType]]]


@pulumi.input_type
class PlacementArgs:
    def __init__(__self__, *, exclude_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., include_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zone_placement_policy: Optional[pulumi.Input[Union[_builtins.str, ZonePlacementPolicyType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeZones")
    def exclude_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclude_zones.setter
    def exclude_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeZones")
    def include_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @include_zones.setter
    def include_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonePlacementPolicy")
    def zone_placement_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, ZonePlacementPolicyType]]]:
        
        ...
    
    @zone_placement_policy.setter
    def zone_placement_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, ZonePlacementPolicyType]]]): # -> None:
        ...
    


class PlanArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.str]]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., product: Optional[pulumi.Input[_builtins.str]] = ..., promotion_code: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PriorityMixPolicyArgsDict(TypedDict):
    
    base_regular_priority_count: NotRequired[pulumi.Input[_builtins.int]]
    regular_priority_percentage_above_base: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class PriorityMixPolicyArgs:
    def __init__(__self__, *, base_regular_priority_count: Optional[pulumi.Input[_builtins.int]] = ..., regular_priority_percentage_above_base: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseRegularPriorityCount")
    def base_regular_priority_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @base_regular_priority_count.setter
    def base_regular_priority_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regularPriorityPercentageAboveBase")
    def regular_priority_percentage_above_base(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @regular_priority_percentage_above_base.setter
    def regular_priority_percentage_above_base(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class ProximityPlacementGroupPropertiesIntentArgsDict(TypedDict):
    
    vm_sizes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ProximityPlacementGroupPropertiesIntentArgs:
    def __init__(__self__, *, vm_sizes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSizes")
    def vm_sizes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vm_sizes.setter
    def vm_sizes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ProxyAgentSettingsArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    imds: NotRequired[pulumi.Input[HostEndpointSettingsArgsDict]]
    key_incarnation_id: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, Mode]]]
    wire_server: NotRequired[pulumi.Input[HostEndpointSettingsArgsDict]]


@pulumi.input_type
class ProxyAgentSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., imds: Optional[pulumi.Input[HostEndpointSettingsArgs]] = ..., key_incarnation_id: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ..., wire_server: Optional[pulumi.Input[HostEndpointSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def imds(self) -> Optional[pulumi.Input[HostEndpointSettingsArgs]]:
        
        ...
    
    @imds.setter
    def imds(self, value: Optional[pulumi.Input[HostEndpointSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyIncarnationId")
    def key_incarnation_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_incarnation_id.setter
    def key_incarnation_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, Mode]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, Mode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wireServer")
    def wire_server(self) -> Optional[pulumi.Input[HostEndpointSettingsArgs]]:
        
        ...
    
    @wire_server.setter
    def wire_server(self, value: Optional[pulumi.Input[HostEndpointSettingsArgs]]): # -> None:
        ...
    


class PublicIPAddressSkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]]


@pulumi.input_type
class PublicIPAddressSkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]] = ..., tier: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuName]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressSkuTier]]]): # -> None:
        ...
    


class RecommendedMachineConfigurationArgsDict(TypedDict):
    
    memory: NotRequired[pulumi.Input[ResourceRangeArgsDict]]
    v_cpus: NotRequired[pulumi.Input[ResourceRangeArgsDict]]


@pulumi.input_type
class RecommendedMachineConfigurationArgs:
    def __init__(__self__, *, memory: Optional[pulumi.Input[ResourceRangeArgs]] = ..., v_cpus: Optional[pulumi.Input[ResourceRangeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[ResourceRangeArgs]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[ResourceRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCPUs")
    def v_cpus(self) -> Optional[pulumi.Input[ResourceRangeArgs]]:
        
        ...
    
    @v_cpus.setter
    def v_cpus(self, value: Optional[pulumi.Input[ResourceRangeArgs]]): # -> None:
        ...
    


class ResiliencyPolicyArgsDict(TypedDict):
    
    automatic_zone_rebalancing_policy: NotRequired[pulumi.Input[AutomaticZoneRebalancingPolicyArgsDict]]
    resilient_vm_creation_policy: NotRequired[pulumi.Input[ResilientVMCreationPolicyArgsDict]]
    resilient_vm_deletion_policy: NotRequired[pulumi.Input[ResilientVMDeletionPolicyArgsDict]]


@pulumi.input_type
class ResiliencyPolicyArgs:
    def __init__(__self__, *, automatic_zone_rebalancing_policy: Optional[pulumi.Input[AutomaticZoneRebalancingPolicyArgs]] = ..., resilient_vm_creation_policy: Optional[pulumi.Input[ResilientVMCreationPolicyArgs]] = ..., resilient_vm_deletion_policy: Optional[pulumi.Input[ResilientVMDeletionPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticZoneRebalancingPolicy")
    def automatic_zone_rebalancing_policy(self) -> Optional[pulumi.Input[AutomaticZoneRebalancingPolicyArgs]]:
        
        ...
    
    @automatic_zone_rebalancing_policy.setter
    def automatic_zone_rebalancing_policy(self, value: Optional[pulumi.Input[AutomaticZoneRebalancingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resilientVMCreationPolicy")
    def resilient_vm_creation_policy(self) -> Optional[pulumi.Input[ResilientVMCreationPolicyArgs]]:
        
        ...
    
    @resilient_vm_creation_policy.setter
    def resilient_vm_creation_policy(self, value: Optional[pulumi.Input[ResilientVMCreationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resilientVMDeletionPolicy")
    def resilient_vm_deletion_policy(self) -> Optional[pulumi.Input[ResilientVMDeletionPolicyArgs]]:
        
        ...
    
    @resilient_vm_deletion_policy.setter
    def resilient_vm_deletion_policy(self, value: Optional[pulumi.Input[ResilientVMDeletionPolicyArgs]]): # -> None:
        ...
    


class ResilientVMCreationPolicyArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ResilientVMCreationPolicyArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ResilientVMDeletionPolicyArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ResilientVMDeletionPolicyArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ResourceRangeArgsDict(TypedDict):
    
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ResourceRangeArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.int]] = ..., min: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ResourceSharingProfileArgsDict(TypedDict):
    subscription_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]


@pulumi.input_type
class ResourceSharingProfileArgs:
    def __init__(__self__, *, subscription_ids: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionIds")
    def subscription_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @subscription_ids.setter
    def subscription_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    


class RestorePointCollectionSourcePropertiesArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RestorePointCollectionSourcePropertiesArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RestorePointEncryptionArgsDict(TypedDict):
    
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, RestorePointEncryptionType]]]


@pulumi.input_type
class RestorePointEncryptionArgs:
    def __init__(__self__, *, disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, RestorePointEncryptionType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, RestorePointEncryptionType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, RestorePointEncryptionType]]]): # -> None:
        ...
    


class RestorePointSourceMetadataArgsDict(TypedDict):
    
    storage_profile: NotRequired[pulumi.Input[RestorePointSourceVMStorageProfileArgsDict]]


@pulumi.input_type
class RestorePointSourceMetadataArgs:
    def __init__(__self__, *, storage_profile: Optional[pulumi.Input[RestorePointSourceVMStorageProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[RestorePointSourceVMStorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[RestorePointSourceVMStorageProfileArgs]]): # -> None:
        ...
    


class RestorePointSourceVMDataDiskArgsDict(TypedDict):
    
    disk_restore_point: NotRequired[pulumi.Input[DiskRestorePointAttributesArgsDict]]
    managed_disk: NotRequired[pulumi.Input[ManagedDiskParametersArgsDict]]


@pulumi.input_type
class RestorePointSourceVMDataDiskArgs:
    def __init__(__self__, *, disk_restore_point: Optional[pulumi.Input[DiskRestorePointAttributesArgs]] = ..., managed_disk: Optional[pulumi.Input[ManagedDiskParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRestorePoint")
    def disk_restore_point(self) -> Optional[pulumi.Input[DiskRestorePointAttributesArgs]]:
        
        ...
    
    @disk_restore_point.setter
    def disk_restore_point(self, value: Optional[pulumi.Input[DiskRestorePointAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[ManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[ManagedDiskParametersArgs]]): # -> None:
        ...
    


class RestorePointSourceVMOSDiskArgsDict(TypedDict):
    
    disk_restore_point: NotRequired[pulumi.Input[DiskRestorePointAttributesArgsDict]]
    managed_disk: NotRequired[pulumi.Input[ManagedDiskParametersArgsDict]]


@pulumi.input_type
class RestorePointSourceVMOSDiskArgs:
    def __init__(__self__, *, disk_restore_point: Optional[pulumi.Input[DiskRestorePointAttributesArgs]] = ..., managed_disk: Optional[pulumi.Input[ManagedDiskParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRestorePoint")
    def disk_restore_point(self) -> Optional[pulumi.Input[DiskRestorePointAttributesArgs]]:
        
        ...
    
    @disk_restore_point.setter
    def disk_restore_point(self, value: Optional[pulumi.Input[DiskRestorePointAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[ManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[ManagedDiskParametersArgs]]): # -> None:
        ...
    


class RestorePointSourceVMStorageProfileArgsDict(TypedDict):
    
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[RestorePointSourceVMDataDiskArgsDict]]]]
    os_disk: NotRequired[pulumi.Input[RestorePointSourceVMOSDiskArgsDict]]


@pulumi.input_type
class RestorePointSourceVMStorageProfileArgs:
    def __init__(__self__, *, data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[RestorePointSourceVMDataDiskArgs]]]] = ..., os_disk: Optional[pulumi.Input[RestorePointSourceVMOSDiskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RestorePointSourceVMDataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RestorePointSourceVMDataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[RestorePointSourceVMOSDiskArgs]]:
        
        ...
    
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[RestorePointSourceVMOSDiskArgs]]): # -> None:
        ...
    


class RollingUpgradePolicyArgsDict(TypedDict):
    
    enable_cross_zone_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    max_batch_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_surge: NotRequired[pulumi.Input[_builtins.bool]]
    max_unhealthy_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_upgraded_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    pause_time_between_batches: NotRequired[pulumi.Input[_builtins.str]]
    prioritize_unhealthy_instances: NotRequired[pulumi.Input[_builtins.bool]]
    rollback_failed_instances_on_policy_breach: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RollingUpgradePolicyArgs:
    def __init__(__self__, *, enable_cross_zone_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., max_batch_instance_percent: Optional[pulumi.Input[_builtins.int]] = ..., max_surge: Optional[pulumi.Input[_builtins.bool]] = ..., max_unhealthy_instance_percent: Optional[pulumi.Input[_builtins.int]] = ..., max_unhealthy_upgraded_instance_percent: Optional[pulumi.Input[_builtins.int]] = ..., pause_time_between_batches: Optional[pulumi.Input[_builtins.str]] = ..., prioritize_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., rollback_failed_instances_on_policy_breach: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneUpgrade")
    def enable_cross_zone_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_cross_zone_upgrade.setter
    def enable_cross_zone_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBatchInstancePercent")
    def max_batch_instance_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_batch_instance_percent.setter
    def max_batch_instance_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @max_surge.setter
    def max_surge(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyInstancePercent")
    def max_unhealthy_instance_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_unhealthy_instance_percent.setter
    def max_unhealthy_instance_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyUpgradedInstancePercent")
    def max_unhealthy_upgraded_instance_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_unhealthy_upgraded_instance_percent.setter
    def max_unhealthy_upgraded_instance_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pauseTimeBetweenBatches")
    def pause_time_between_batches(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pause_time_between_batches.setter
    def pause_time_between_batches(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prioritizeUnhealthyInstances")
    def prioritize_unhealthy_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prioritize_unhealthy_instances.setter
    def prioritize_unhealthy_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollbackFailedInstancesOnPolicyBreach")
    def rollback_failed_instances_on_policy_breach(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rollback_failed_instances_on_policy_breach.setter
    def rollback_failed_instances_on_policy_breach(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RunCommandInputParameterArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class RunCommandInputParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RunCommandManagedIdentityArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RunCommandManagedIdentityArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScaleInPolicyArgsDict(TypedDict):
    
    force_deletion: NotRequired[pulumi.Input[_builtins.bool]]
    prioritize_unhealthy_vms: NotRequired[pulumi.Input[_builtins.bool]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VirtualMachineScaleSetScaleInRules]]]]]


@pulumi.input_type
class ScaleInPolicyArgs:
    def __init__(__self__, *, force_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., prioritize_unhealthy_vms: Optional[pulumi.Input[_builtins.bool]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VirtualMachineScaleSetScaleInRules]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDeletion")
    def force_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_deletion.setter
    def force_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prioritizeUnhealthyVMs")
    def prioritize_unhealthy_vms(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prioritize_unhealthy_vms.setter
    def prioritize_unhealthy_vms(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VirtualMachineScaleSetScaleInRules]]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VirtualMachineScaleSetScaleInRules]]]]]): # -> None:
        ...
    


class ScheduledEventsAdditionalPublishingTargetsArgsDict(TypedDict):
    event_grid_and_resource_graph: NotRequired[pulumi.Input[EventGridAndResourceGraphArgsDict]]


@pulumi.input_type
class ScheduledEventsAdditionalPublishingTargetsArgs:
    def __init__(__self__, *, event_grid_and_resource_graph: Optional[pulumi.Input[EventGridAndResourceGraphArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventGridAndResourceGraph")
    def event_grid_and_resource_graph(self) -> Optional[pulumi.Input[EventGridAndResourceGraphArgs]]:
        
        ...
    
    @event_grid_and_resource_graph.setter
    def event_grid_and_resource_graph(self, value: Optional[pulumi.Input[EventGridAndResourceGraphArgs]]): # -> None:
        ...
    


class ScheduledEventsPolicyArgsDict(TypedDict):
    
    scheduled_events_additional_publishing_targets: NotRequired[pulumi.Input[ScheduledEventsAdditionalPublishingTargetsArgsDict]]
    user_initiated_reboot: NotRequired[pulumi.Input[UserInitiatedRebootArgsDict]]
    user_initiated_redeploy: NotRequired[pulumi.Input[UserInitiatedRedeployArgsDict]]


@pulumi.input_type
class ScheduledEventsPolicyArgs:
    def __init__(__self__, *, scheduled_events_additional_publishing_targets: Optional[pulumi.Input[ScheduledEventsAdditionalPublishingTargetsArgs]] = ..., user_initiated_reboot: Optional[pulumi.Input[UserInitiatedRebootArgs]] = ..., user_initiated_redeploy: Optional[pulumi.Input[UserInitiatedRedeployArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsAdditionalPublishingTargets")
    def scheduled_events_additional_publishing_targets(self) -> Optional[pulumi.Input[ScheduledEventsAdditionalPublishingTargetsArgs]]:
        
        ...
    
    @scheduled_events_additional_publishing_targets.setter
    def scheduled_events_additional_publishing_targets(self, value: Optional[pulumi.Input[ScheduledEventsAdditionalPublishingTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInitiatedReboot")
    def user_initiated_reboot(self) -> Optional[pulumi.Input[UserInitiatedRebootArgs]]:
        
        ...
    
    @user_initiated_reboot.setter
    def user_initiated_reboot(self, value: Optional[pulumi.Input[UserInitiatedRebootArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInitiatedRedeploy")
    def user_initiated_redeploy(self) -> Optional[pulumi.Input[UserInitiatedRedeployArgs]]:
        
        ...
    
    @user_initiated_redeploy.setter
    def user_initiated_redeploy(self, value: Optional[pulumi.Input[UserInitiatedRedeployArgs]]): # -> None:
        ...
    


class ScheduledEventsProfileArgsDict(TypedDict):
    os_image_notification_profile: NotRequired[pulumi.Input[OSImageNotificationProfileArgsDict]]
    terminate_notification_profile: NotRequired[pulumi.Input[TerminateNotificationProfileArgsDict]]


@pulumi.input_type
class ScheduledEventsProfileArgs:
    def __init__(__self__, *, os_image_notification_profile: Optional[pulumi.Input[OSImageNotificationProfileArgs]] = ..., terminate_notification_profile: Optional[pulumi.Input[TerminateNotificationProfileArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osImageNotificationProfile")
    def os_image_notification_profile(self) -> Optional[pulumi.Input[OSImageNotificationProfileArgs]]:
        
        ...
    
    @os_image_notification_profile.setter
    def os_image_notification_profile(self, value: Optional[pulumi.Input[OSImageNotificationProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateNotificationProfile")
    def terminate_notification_profile(self) -> Optional[pulumi.Input[TerminateNotificationProfileArgs]]:
        
        ...
    
    @terminate_notification_profile.setter
    def terminate_notification_profile(self, value: Optional[pulumi.Input[TerminateNotificationProfileArgs]]): # -> None:
        ...
    


class ScriptSourceArgsDict(TypedDict):
    
    script_link: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[GalleryScriptParameterArgsDict]]]]


@pulumi.input_type
class ScriptSourceArgs:
    def __init__(__self__, *, script_link: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryScriptParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptLink")
    def script_link(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @script_link.setter
    def script_link(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryScriptParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryScriptParameterArgs]]]]): # -> None:
        ...
    


class SecurityPostureReferenceArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    exclude_extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_overridable: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SecurityPostureReferenceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], exclude_extensions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., is_overridable: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeExtensions")
    def exclude_extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclude_extensions.setter
    def exclude_extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOverridable")
    def is_overridable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_overridable.setter
    def is_overridable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SecurityProfileArgsDict(TypedDict):
    
    encryption_at_host: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_identity: NotRequired[pulumi.Input[EncryptionIdentityArgsDict]]
    proxy_agent_settings: NotRequired[pulumi.Input[ProxyAgentSettingsArgsDict]]
    security_type: NotRequired[pulumi.Input[Union[_builtins.str, SecurityTypes]]]
    uefi_settings: NotRequired[pulumi.Input[UefiSettingsArgsDict]]


@pulumi.input_type
class SecurityProfileArgs:
    def __init__(__self__, *, encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_identity: Optional[pulumi.Input[EncryptionIdentityArgs]] = ..., proxy_agent_settings: Optional[pulumi.Input[ProxyAgentSettingsArgs]] = ..., security_type: Optional[pulumi.Input[Union[_builtins.str, SecurityTypes]]] = ..., uefi_settings: Optional[pulumi.Input[UefiSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[pulumi.Input[EncryptionIdentityArgs]]:
        
        ...
    
    @encryption_identity.setter
    def encryption_identity(self, value: Optional[pulumi.Input[EncryptionIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyAgentSettings")
    def proxy_agent_settings(self) -> Optional[pulumi.Input[ProxyAgentSettingsArgs]]:
        
        ...
    
    @proxy_agent_settings.setter
    def proxy_agent_settings(self, value: Optional[pulumi.Input[ProxyAgentSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SecurityTypes]]]:
        
        ...
    
    @security_type.setter
    def security_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[pulumi.Input[UefiSettingsArgs]]:
        
        ...
    
    @uefi_settings.setter
    def uefi_settings(self, value: Optional[pulumi.Input[UefiSettingsArgs]]): # -> None:
        ...
    


class ServiceArtifactReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceArtifactReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SharingProfileArgsDict(TypedDict):
    
    community_gallery_info: NotRequired[pulumi.Input[CommunityGalleryInfoArgsDict]]
    permissions: NotRequired[pulumi.Input[Union[_builtins.str, GallerySharingPermissionTypes]]]


@pulumi.input_type
class SharingProfileArgs:
    def __init__(__self__, *, community_gallery_info: Optional[pulumi.Input[CommunityGalleryInfoArgs]] = ..., permissions: Optional[pulumi.Input[Union[_builtins.str, GallerySharingPermissionTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityGalleryInfo")
    def community_gallery_info(self) -> Optional[pulumi.Input[CommunityGalleryInfoArgs]]:
        
        ...
    
    @community_gallery_info.setter
    def community_gallery_info(self, value: Optional[pulumi.Input[CommunityGalleryInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Union[_builtins.str, GallerySharingPermissionTypes]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Union[_builtins.str, GallerySharingPermissionTypes]]]): # -> None:
        ...
    


class SkuProfileVMSizeArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    rank: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SkuProfileVMSizeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., rank: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SkuProfileArgsDict(TypedDict):
    
    allocation_strategy: NotRequired[pulumi.Input[Union[_builtins.str, AllocationStrategy]]]
    vm_sizes: NotRequired[pulumi.Input[Sequence[pulumi.Input[SkuProfileVMSizeArgsDict]]]]


@pulumi.input_type
class SkuProfileArgs:
    def __init__(__self__, *, allocation_strategy: Optional[pulumi.Input[Union[_builtins.str, AllocationStrategy]]] = ..., vm_sizes: Optional[pulumi.Input[Sequence[pulumi.Input[SkuProfileVMSizeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationStrategy]]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationStrategy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSizes")
    def vm_sizes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuProfileVMSizeArgs]]]]:
        
        ...
    
    @vm_sizes.setter
    def vm_sizes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuProfileVMSizeArgs]]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.float]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SnapshotSkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[Union[_builtins.str, SnapshotStorageAccountTypes]]]


@pulumi.input_type
class SnapshotSkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[Union[_builtins.str, SnapshotStorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SnapshotStorageAccountTypes]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SnapshotStorageAccountTypes]]]): # -> None:
        ...
    


class SoftDeletePolicyArgsDict(TypedDict):
    
    is_soft_delete_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SoftDeletePolicyArgs:
    def __init__(__self__, *, is_soft_delete_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSoftDeleteEnabled")
    def is_soft_delete_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_soft_delete_enabled.setter
    def is_soft_delete_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SourceVaultArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SourceVaultArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpotRestorePolicyArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    restore_timeout: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpotRestorePolicyArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., restore_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreTimeout")
    def restore_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_timeout.setter
    def restore_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SshConfigurationArgsDict(TypedDict):
    
    public_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgsDict]]]]


@pulumi.input_type
class SshConfigurationArgs:
    def __init__(__self__, *, public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]:
        
        ...
    
    @public_keys.setter
    def public_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]): # -> None:
        ...
    


class SshPublicKeyArgsDict(TypedDict):
    
    key_data: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(__self__, *, key_data: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_data.setter
    def key_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageProfileArgsDict(TypedDict):
    
    align_regional_disks_to_vm_zone: NotRequired[pulumi.Input[_builtins.bool]]
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataDiskArgsDict]]]]
    disk_controller_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]
    image_reference: NotRequired[pulumi.Input[ImageReferenceArgsDict]]
    os_disk: NotRequired[pulumi.Input[OSDiskArgsDict]]


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *, align_regional_disks_to_vm_zone: Optional[pulumi.Input[_builtins.bool]] = ..., data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]] = ..., disk_controller_type: Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]] = ..., image_reference: Optional[pulumi.Input[ImageReferenceArgs]] = ..., os_disk: Optional[pulumi.Input[OSDiskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignRegionalDisksToVMZone")
    def align_regional_disks_to_vm_zone(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @align_regional_disks_to_vm_zone.setter
    def align_regional_disks_to_vm_zone(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskControllerType")
    def disk_controller_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]:
        
        ...
    
    @disk_controller_type.setter
    def disk_controller_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[pulumi.Input[ImageReferenceArgs]]:
        
        ...
    
    @image_reference.setter
    def image_reference(self, value: Optional[pulumi.Input[ImageReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[OSDiskArgs]]:
        
        ...
    
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[OSDiskArgs]]): # -> None:
        ...
    


class SubResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SupportedCapabilitiesArgsDict(TypedDict):
    
    accelerated_network: NotRequired[pulumi.Input[_builtins.bool]]
    architecture: NotRequired[pulumi.Input[Union[_builtins.str, Architecture]]]
    disk_controller_types: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SupportedCapabilitiesArgs:
    def __init__(__self__, *, accelerated_network: Optional[pulumi.Input[_builtins.bool]] = ..., architecture: Optional[pulumi.Input[Union[_builtins.str, Architecture]]] = ..., disk_controller_types: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratedNetwork")
    def accelerated_network(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @accelerated_network.setter
    def accelerated_network(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[Union[_builtins.str, Architecture]]]:
        
        ...
    
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[Union[_builtins.str, Architecture]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskControllerTypes")
    def disk_controller_types(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_controller_types.setter
    def disk_controller_types(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetRegionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    additional_replica_sets: NotRequired[pulumi.Input[Sequence[pulumi.Input[AdditionalReplicaSetArgsDict]]]]
    encryption: NotRequired[pulumi.Input[EncryptionImagesArgsDict]]
    exclude_from_latest: NotRequired[pulumi.Input[_builtins.bool]]
    regional_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountType]]]


@pulumi.input_type
class TargetRegionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], additional_replica_sets: Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalReplicaSetArgs]]]] = ..., encryption: Optional[pulumi.Input[EncryptionImagesArgs]] = ..., exclude_from_latest: Optional[pulumi.Input[_builtins.bool]] = ..., regional_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalReplicaSets")
    def additional_replica_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalReplicaSetArgs]]]]:
        
        ...
    
    @additional_replica_sets.setter
    def additional_replica_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalReplicaSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionImagesArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionImagesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFromLatest")
    def exclude_from_latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_from_latest.setter
    def exclude_from_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionalReplicaCount")
    def regional_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @regional_replica_count.setter
    def regional_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountType]]]): # -> None:
        ...
    


class TerminateNotificationProfileArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    not_before_timeout: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TerminateNotificationProfileArgs:
    def __init__(__self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ..., not_before_timeout: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeTimeout")
    def not_before_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_before_timeout.setter
    def not_before_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UefiKeySignaturesArgsDict(TypedDict):
    
    db: NotRequired[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgsDict]]]]
    dbx: NotRequired[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgsDict]]]]
    kek: NotRequired[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgsDict]]]]
    pk: NotRequired[pulumi.Input[UefiKeyArgsDict]]


@pulumi.input_type
class UefiKeySignaturesArgs:
    def __init__(__self__, *, db: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]] = ..., dbx: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]] = ..., kek: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]] = ..., pk: Optional[pulumi.Input[UefiKeyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def db(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]:
        
        ...
    
    @db.setter
    def db(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dbx(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]:
        
        ...
    
    @dbx.setter
    def dbx(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kek(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]:
        
        ...
    
    @kek.setter
    def kek(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UefiKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pk(self) -> Optional[pulumi.Input[UefiKeyArgs]]:
        
        ...
    
    @pk.setter
    def pk(self, value: Optional[pulumi.Input[UefiKeyArgs]]): # -> None:
        ...
    


class UefiKeyArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, UefiKeyType]]]
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UefiKeyArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, UefiKeyType]]] = ..., value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, UefiKeyType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, UefiKeyType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UefiSettingsArgsDict(TypedDict):
    
    secure_boot_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    v_tpm_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UefiSettingsArgs:
    def __init__(__self__, *, secure_boot_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., v_tpm_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @secure_boot_enabled.setter
    def secure_boot_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vTpmEnabled")
    def v_tpm_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @v_tpm_enabled.setter
    def v_tpm_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UpgradePolicyArgsDict(TypedDict):
    
    automatic_os_upgrade_policy: NotRequired[pulumi.Input[AutomaticOSUpgradePolicyArgsDict]]
    mode: NotRequired[pulumi.Input[UpgradeMode]]
    rolling_upgrade_policy: NotRequired[pulumi.Input[RollingUpgradePolicyArgsDict]]


@pulumi.input_type
class UpgradePolicyArgs:
    def __init__(__self__, *, automatic_os_upgrade_policy: Optional[pulumi.Input[AutomaticOSUpgradePolicyArgs]] = ..., mode: Optional[pulumi.Input[UpgradeMode]] = ..., rolling_upgrade_policy: Optional[pulumi.Input[RollingUpgradePolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticOSUpgradePolicy")
    def automatic_os_upgrade_policy(self) -> Optional[pulumi.Input[AutomaticOSUpgradePolicyArgs]]:
        
        ...
    
    @automatic_os_upgrade_policy.setter
    def automatic_os_upgrade_policy(self, value: Optional[pulumi.Input[AutomaticOSUpgradePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[UpgradeMode]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[UpgradeMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingUpgradePolicy")
    def rolling_upgrade_policy(self) -> Optional[pulumi.Input[RollingUpgradePolicyArgs]]:
        
        ...
    
    @rolling_upgrade_policy.setter
    def rolling_upgrade_policy(self, value: Optional[pulumi.Input[RollingUpgradePolicyArgs]]): # -> None:
        ...
    


class UserArtifactManageArgsDict(TypedDict):
    install: pulumi.Input[_builtins.str]
    remove: pulumi.Input[_builtins.str]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserArtifactManageArgs:
    def __init__(__self__, *, install: pulumi.Input[_builtins.str], remove: pulumi.Input[_builtins.str], update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def install(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @install.setter
    def install(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def remove(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @remove.setter
    def remove(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserArtifactSettingsArgsDict(TypedDict):
    
    config_file_name: NotRequired[pulumi.Input[_builtins.str]]
    package_file_name: NotRequired[pulumi.Input[_builtins.str]]
    script_behavior_after_reboot: NotRequired[pulumi.Input[Union[_builtins.str, GalleryApplicationScriptRebootBehavior]]]


@pulumi.input_type
class UserArtifactSettingsArgs:
    def __init__(__self__, *, config_file_name: Optional[pulumi.Input[_builtins.str]] = ..., package_file_name: Optional[pulumi.Input[_builtins.str]] = ..., script_behavior_after_reboot: Optional[pulumi.Input[Union[_builtins.str, GalleryApplicationScriptRebootBehavior]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configFileName")
    def config_file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_file_name.setter
    def config_file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageFileName")
    def package_file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_file_name.setter
    def package_file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptBehaviorAfterReboot")
    def script_behavior_after_reboot(self) -> Optional[pulumi.Input[Union[_builtins.str, GalleryApplicationScriptRebootBehavior]]]:
        
        ...
    
    @script_behavior_after_reboot.setter
    def script_behavior_after_reboot(self, value: Optional[pulumi.Input[Union[_builtins.str, GalleryApplicationScriptRebootBehavior]]]): # -> None:
        ...
    


class UserArtifactSourceArgsDict(TypedDict):
    
    media_link: pulumi.Input[_builtins.str]
    default_configuration_link: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserArtifactSourceArgs:
    def __init__(__self__, *, media_link: pulumi.Input[_builtins.str], default_configuration_link: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @media_link.setter
    def media_link(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultConfigurationLink")
    def default_configuration_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_configuration_link.setter
    def default_configuration_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserInitiatedRebootArgsDict(TypedDict):
    
    automatically_approve: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UserInitiatedRebootArgs:
    def __init__(__self__, *, automatically_approve: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticallyApprove")
    def automatically_approve(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatically_approve.setter
    def automatically_approve(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UserInitiatedRedeployArgsDict(TypedDict):
    
    automatically_approve: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UserInitiatedRedeployArgs:
    def __init__(__self__, *, automatically_approve: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticallyApprove")
    def automatically_approve(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatically_approve.setter
    def automatically_approve(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VMDiskSecurityProfileArgsDict(TypedDict):
    
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    security_encryption_type: NotRequired[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]]


@pulumi.input_type
class VMDiskSecurityProfileArgs:
    def __init__(__self__, *, disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., security_encryption_type: Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]]:
        
        ...
    
    @security_encryption_type.setter
    def security_encryption_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]]): # -> None:
        ...
    


class VMGalleryApplicationArgsDict(TypedDict):
    
    package_reference_id: pulumi.Input[_builtins.str]
    configuration_reference: NotRequired[pulumi.Input[_builtins.str]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    tags: NotRequired[pulumi.Input[_builtins.str]]
    treat_failure_as_deployment_failure: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VMGalleryApplicationArgs:
    def __init__(__self__, *, package_reference_id: pulumi.Input[_builtins.str], configuration_reference: Optional[pulumi.Input[_builtins.str]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[_builtins.str]] = ..., treat_failure_as_deployment_failure: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageReferenceId")
    def package_reference_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @package_reference_id.setter
    def package_reference_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationReference")
    def configuration_reference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_reference.setter
    def configuration_reference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @treat_failure_as_deployment_failure.setter
    def treat_failure_as_deployment_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VMSizePropertiesArgsDict(TypedDict):
    
    v_cpus_available: NotRequired[pulumi.Input[_builtins.int]]
    v_cpus_per_core: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VMSizePropertiesArgs:
    def __init__(__self__, *, v_cpus_available: Optional[pulumi.Input[_builtins.int]] = ..., v_cpus_per_core: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCPUsAvailable")
    def v_cpus_available(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @v_cpus_available.setter
    def v_cpus_available(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCPUsPerCore")
    def v_cpus_per_core(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @v_cpus_per_core.setter
    def v_cpus_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VaultCertificateArgsDict(TypedDict):
    
    certificate_store: NotRequired[pulumi.Input[_builtins.str]]
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VaultCertificateArgs:
    def __init__(__self__, *, certificate_store: Optional[pulumi.Input[_builtins.str]] = ..., certificate_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_store.setter
    def certificate_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VaultSecretGroupArgsDict(TypedDict):
    
    source_vault: NotRequired[pulumi.Input[SubResourceArgsDict]]
    vault_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgsDict]]]]


@pulumi.input_type
class VaultSecretGroupArgs:
    def __init__(__self__, *, source_vault: Optional[pulumi.Input[SubResourceArgs]] = ..., vault_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @source_vault.setter
    def source_vault(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]]:
        
        ...
    
    @vault_certificates.setter
    def vault_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]]): # -> None:
        ...
    


class VirtualHardDiskArgsDict(TypedDict):
    
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualHardDiskArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineExtensionInstanceViewArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgsDict]]]]
    substatuses: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgsDict]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    type_handler_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineExtensionInstanceViewArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]] = ..., substatuses: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def substatuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]]:
        
        ...
    
    @substatuses.setter
    def substatuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceViewStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VirtualMachineIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VirtualMachineIpTagArgsDict(TypedDict):
    
    ip_tag_type: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineIpTagArgs:
    def __init__(__self__, *, ip_tag_type: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_tag_type.setter
    def ip_tag_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineNetworkInterfaceConfigurationArgsDict(TypedDict):
    
    ip_configurations: pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceIPConfigurationArgsDict]]]
    name: pulumi.Input[_builtins.str]
    auxiliary_mode: NotRequired[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]
    auxiliary_sku: NotRequired[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    disable_tcp_state_tracking: NotRequired[pulumi.Input[_builtins.bool]]
    dns_settings: NotRequired[pulumi.Input[VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgsDict]]
    dscp_configuration: NotRequired[pulumi.Input[SubResourceArgsDict]]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]
    enable_fpga: NotRequired[pulumi.Input[_builtins.bool]]
    enable_ip_forwarding: NotRequired[pulumi.Input[_builtins.bool]]
    network_security_group: NotRequired[pulumi.Input[SubResourceArgsDict]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualMachineNetworkInterfaceConfigurationArgs:
    def __init__(__self__, *, ip_configurations: pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceIPConfigurationArgs]]], name: pulumi.Input[_builtins.str], auxiliary_mode: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]] = ..., auxiliary_sku: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]] = ..., disable_tcp_state_tracking: Optional[pulumi.Input[_builtins.bool]] = ..., dns_settings: Optional[pulumi.Input[VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgs]] = ..., dscp_configuration: Optional[pulumi.Input[SubResourceArgs]] = ..., enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fpga: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ip_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., network_security_group: Optional[pulumi.Input[SubResourceArgs]] = ..., primary: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceIPConfigurationArgs]]]:
        
        ...
    
    @ip_configurations.setter
    def ip_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[VirtualMachineNetworkInterfaceIPConfigurationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]:
        
        ...
    
    @auxiliary_mode.setter
    def auxiliary_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]:
        
        ...
    
    @auxiliary_sku.setter
    def auxiliary_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_tcp_state_tracking.setter
    def disable_tcp_state_tracking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dscpConfiguration")
    def dscp_configuration(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        ...
    
    @dscp_configuration.setter
    def dscp_configuration(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFpga")
    def enable_fpga(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fpga.setter
    def enable_fpga(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ip_forwarding.setter
    def enable_ip_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgsDict(TypedDict):
    
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VirtualMachineNetworkInterfaceDnsSettingsConfigurationArgs:
    def __init__(__self__, *, dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VirtualMachineNetworkInterfaceIPConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    application_gateway_backend_address_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    application_security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    load_balancer_backend_address_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address_version: NotRequired[pulumi.Input[Union[_builtins.str, IPVersions]]]
    public_ip_address_configuration: NotRequired[pulumi.Input[VirtualMachinePublicIPAddressConfigurationArgsDict]]
    subnet: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class VirtualMachineNetworkInterfaceIPConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], application_gateway_backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., application_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., load_balancer_backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., primary: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_address_version: Optional[pulumi.Input[Union[_builtins.str, IPVersions]]] = ..., public_ip_address_configuration: Optional[pulumi.Input[VirtualMachinePublicIPAddressConfigurationArgs]] = ..., subnet: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @application_gateway_backend_address_pools.setter
    def application_gateway_backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @application_security_groups.setter
    def application_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @load_balancer_backend_address_pools.setter
    def load_balancer_backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(self) -> Optional[pulumi.Input[Union[_builtins.str, IPVersions]]]:
        
        ...
    
    @private_ip_address_version.setter
    def private_ip_address_version(self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(self) -> Optional[pulumi.Input[VirtualMachinePublicIPAddressConfigurationArgs]]:
        
        ...
    
    @public_ip_address_configuration.setter
    def public_ip_address_configuration(self, value: Optional[pulumi.Input[VirtualMachinePublicIPAddressConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class VirtualMachinePublicIPAddressConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    dns_settings: NotRequired[pulumi.Input[VirtualMachinePublicIPAddressDnsSettingsConfigurationArgsDict]]
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ip_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineIpTagArgsDict]]]]
    public_ip_address_version: NotRequired[pulumi.Input[Union[_builtins.str, IPVersions]]]
    public_ip_allocation_method: NotRequired[pulumi.Input[Union[_builtins.str, PublicIPAllocationMethod]]]
    public_ip_prefix: NotRequired[pulumi.Input[SubResourceArgsDict]]
    sku: NotRequired[pulumi.Input[PublicIPAddressSkuArgsDict]]


@pulumi.input_type
class VirtualMachinePublicIPAddressConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], delete_option: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]] = ..., dns_settings: Optional[pulumi.Input[VirtualMachinePublicIPAddressDnsSettingsConfigurationArgs]] = ..., idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineIpTagArgs]]]] = ..., public_ip_address_version: Optional[pulumi.Input[Union[_builtins.str, IPVersions]]] = ..., public_ip_allocation_method: Optional[pulumi.Input[Union[_builtins.str, PublicIPAllocationMethod]]] = ..., public_ip_prefix: Optional[pulumi.Input[SubResourceArgs]] = ..., sku: Optional[pulumi.Input[PublicIPAddressSkuArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[VirtualMachinePublicIPAddressDnsSettingsConfigurationArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[VirtualMachinePublicIPAddressDnsSettingsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineIpTagArgs]]]]:
        
        ...
    
    @ip_tags.setter
    def ip_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineIpTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[pulumi.Input[Union[_builtins.str, IPVersions]]]:
        
        ...
    
    @public_ip_address_version.setter
    def public_ip_address_version(self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAllocationMethod]]]:
        
        ...
    
    @public_ip_allocation_method.setter
    def public_ip_allocation_method(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAllocationMethod]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @public_ip_prefix.setter
    def public_ip_prefix(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[PublicIPAddressSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[PublicIPAddressSkuArgs]]): # -> None:
        ...
    


class VirtualMachinePublicIPAddressDnsSettingsConfigurationArgsDict(TypedDict):
    
    domain_name_label: pulumi.Input[_builtins.str]
    domain_name_label_scope: NotRequired[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]


@pulumi.input_type
class VirtualMachinePublicIPAddressDnsSettingsConfigurationArgs:
    def __init__(__self__, *, domain_name_label: pulumi.Input[_builtins.str], domain_name_label_scope: Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name_label.setter
    def domain_name_label(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabelScope")
    def domain_name_label_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]:
        
        ...
    
    @domain_name_label_scope.setter
    def domain_name_label_scope(self, value: Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]): # -> None:
        ...
    


class VirtualMachineRunCommandScriptSourceArgsDict(TypedDict):
    
    command_id: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    script_uri: NotRequired[pulumi.Input[_builtins.str]]
    script_uri_managed_identity: NotRequired[pulumi.Input[RunCommandManagedIdentityArgsDict]]


@pulumi.input_type
class VirtualMachineRunCommandScriptSourceArgs:
    def __init__(__self__, *, command_id: Optional[pulumi.Input[_builtins.str]] = ..., script: Optional[pulumi.Input[_builtins.str]] = ..., script_uri: Optional[pulumi.Input[_builtins.str]] = ..., script_uri_managed_identity: Optional[pulumi.Input[RunCommandManagedIdentityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandId")
    def command_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @command_id.setter
    def command_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @script_uri.setter
    def script_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptUriManagedIdentity")
    def script_uri_managed_identity(self) -> Optional[pulumi.Input[RunCommandManagedIdentityArgs]]:
        
        ...
    
    @script_uri_managed_identity.setter
    def script_uri_managed_identity(self, value: Optional[pulumi.Input[RunCommandManagedIdentityArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetDataDiskArgsDict(TypedDict):
    
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    lun: pulumi.Input[_builtins.int]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    disk_iops_read_write: NotRequired[pulumi.Input[_builtins.float]]
    disk_m_bps_read_write: NotRequired[pulumi.Input[_builtins.float]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    managed_disk: NotRequired[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualMachineScaleSetDataDiskArgs:
    def __init__(__self__, *, create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]], lun: pulumi.Input[_builtins.int], caching: Optional[pulumi.Input[CachingTypes]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]] = ..., disk_iops_read_write: Optional[pulumi.Input[_builtins.float]] = ..., disk_m_bps_read_write: Optional[pulumi.Input[_builtins.float]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., managed_disk: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @disk_iops_read_write.setter
    def disk_iops_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @disk_m_bps_read_write.setter
    def disk_m_bps_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VirtualMachineScaleSetExtensionProfileArgsDict(TypedDict):
    
    extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgsDict]]]]
    extensions_time_budget: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineScaleSetExtensionProfileArgs:
    def __init__(__self__, *, extensions: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]] = ..., extensions_time_budget: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]]:
        
        ...
    
    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetExtensionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extensions_time_budget.setter
    def extensions_time_budget(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineScaleSetExtensionArgsDict(TypedDict):
    
    auto_upgrade_minor_version: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    force_update_tag: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    protected_settings: NotRequired[Any]
    protected_settings_from_key_vault: NotRequired[pulumi.Input[KeyVaultSecretReferenceArgsDict]]
    provision_after_extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[Any]
    suppress_failures: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    type_handler_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineScaleSetExtensionArgs:
    def __init__(__self__, *, auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., force_update_tag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., protected_settings: Optional[Any] = ..., protected_settings_from_key_vault: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]] = ..., provision_after_extensions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[Any] = ..., suppress_failures: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(self) -> Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]:
        
        ...
    
    @protected_settings_from_key_vault.setter
    def protected_settings_from_key_vault(self, value: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @provision_after_extensions.setter
    def provision_after_extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @suppress_failures.setter
    def suppress_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineScaleSetHardwareProfileArgsDict(TypedDict):
    
    vm_size_properties: NotRequired[pulumi.Input[VMSizePropertiesArgsDict]]


@pulumi.input_type
class VirtualMachineScaleSetHardwareProfileArgs:
    def __init__(__self__, *, vm_size_properties: Optional[pulumi.Input[VMSizePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSizeProperties")
    def vm_size_properties(self) -> Optional[pulumi.Input[VMSizePropertiesArgs]]:
        
        ...
    
    @vm_size_properties.setter
    def vm_size_properties(self, value: Optional[pulumi.Input[VMSizePropertiesArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetIPConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    application_gateway_backend_address_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    application_security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    load_balancer_backend_address_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    load_balancer_inbound_nat_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    private_ip_address_version: NotRequired[pulumi.Input[Union[_builtins.str, IPVersion]]]
    public_ip_address_configuration: NotRequired[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgsDict]]
    subnet: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]


@pulumi.input_type
class VirtualMachineScaleSetIPConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], application_gateway_backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., application_security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., load_balancer_backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., load_balancer_inbound_nat_pools: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., primary: Optional[pulumi.Input[_builtins.bool]] = ..., private_ip_address_version: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]] = ..., public_ip_address_configuration: Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]] = ..., subnet: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @application_gateway_backend_address_pools.setter
    def application_gateway_backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @application_security_groups.setter
    def application_security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @load_balancer_backend_address_pools.setter
    def load_balancer_backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPools")
    def load_balancer_inbound_nat_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @load_balancer_inbound_nat_pools.setter
    def load_balancer_inbound_nat_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(self) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]:
        
        ...
    
    @private_ip_address_version.setter
    def private_ip_address_version(self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(self) -> Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]]:
        
        ...
    
    @public_ip_address_configuration.setter
    def public_ip_address_configuration(self, value: Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VirtualMachineScaleSetIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VirtualMachineScaleSetIpTagArgsDict(TypedDict):
    
    ip_tag_type: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineScaleSetIpTagArgs:
    def __init__(__self__, *, ip_tag_type: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_tag_type.setter
    def ip_tag_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineScaleSetManagedDiskParametersArgsDict(TypedDict):
    
    disk_encryption_set: NotRequired[pulumi.Input[DiskEncryptionSetParametersArgsDict]]
    security_profile: NotRequired[pulumi.Input[VMDiskSecurityProfileArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]


@pulumi.input_type
class VirtualMachineScaleSetManagedDiskParametersArgs:
    def __init__(__self__, *, disk_encryption_set: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]] = ..., security_profile: Optional[pulumi.Input[VMDiskSecurityProfileArgs]] = ..., storage_account_type: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSet")
    def disk_encryption_set(self) -> Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]:
        
        ...
    
    @disk_encryption_set.setter
    def disk_encryption_set(self, value: Optional[pulumi.Input[DiskEncryptionSetParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[VMDiskSecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[VMDiskSecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]:
        
        ...
    
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountTypes]]]): # -> None:
        ...
    


class VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgsDict(TypedDict):
    
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs:
    def __init__(__self__, *, dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VirtualMachineScaleSetNetworkConfigurationArgsDict(TypedDict):
    
    ip_configurations: pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgsDict]]]
    name: pulumi.Input[_builtins.str]
    auxiliary_mode: NotRequired[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]
    auxiliary_sku: NotRequired[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    disable_tcp_state_tracking: NotRequired[pulumi.Input[_builtins.bool]]
    dns_settings: NotRequired[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgsDict]]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]
    enable_fpga: NotRequired[pulumi.Input[_builtins.bool]]
    enable_ip_forwarding: NotRequired[pulumi.Input[_builtins.bool]]
    network_security_group: NotRequired[pulumi.Input[SubResourceArgsDict]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualMachineScaleSetNetworkConfigurationArgs:
    def __init__(__self__, *, ip_configurations: pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]], name: pulumi.Input[_builtins.str], auxiliary_mode: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]] = ..., auxiliary_sku: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]] = ..., disable_tcp_state_tracking: Optional[pulumi.Input[_builtins.bool]] = ..., dns_settings: Optional[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]] = ..., enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fpga: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ip_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., network_security_group: Optional[pulumi.Input[SubResourceArgs]] = ..., primary: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]]:
        
        ...
    
    @ip_configurations.setter
    def ip_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIPConfigurationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]:
        
        ...
    
    @auxiliary_mode.setter
    def auxiliary_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliaryMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]:
        
        ...
    
    @auxiliary_sku.setter
    def auxiliary_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkInterfaceAuxiliarySku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_tcp_state_tracking.setter
    def disable_tcp_state_tracking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationDnsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFpga")
    def enable_fpga(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fpga.setter
    def enable_fpga(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ip_forwarding.setter
    def enable_ip_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VirtualMachineScaleSetNetworkProfileArgsDict(TypedDict):
    
    health_probe: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]
    network_api_version: NotRequired[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]
    network_interface_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgsDict]]]]


@pulumi.input_type
class VirtualMachineScaleSetNetworkProfileArgs:
    def __init__(__self__, *, health_probe: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ..., network_api_version: Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]] = ..., network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbe")
    def health_probe(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]:
        
        ...
    
    @health_probe.setter
    def health_probe(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkApiVersion")
    def network_api_version(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]:
        
        ...
    
    @network_api_version.setter
    def network_api_version(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkApiVersion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]]:
        
        ...
    
    @network_interface_configurations.setter
    def network_interface_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]]): # -> None:
        ...
    


class VirtualMachineScaleSetOSDiskArgsDict(TypedDict):
    
    create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]
    caching: NotRequired[pulumi.Input[CachingTypes]]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]
    diff_disk_settings: NotRequired[pulumi.Input[DiffDiskSettingsArgsDict]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    image: NotRequired[pulumi.Input[VirtualHardDiskArgsDict]]
    managed_disk: NotRequired[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[OperatingSystemTypes]]
    vhd_containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualMachineScaleSetOSDiskArgs:
    def __init__(__self__, *, create_option: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]], caching: Optional[pulumi.Input[CachingTypes]] = ..., delete_option: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]] = ..., diff_disk_settings: Optional[pulumi.Input[DiffDiskSettingsArgs]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., image: Optional[pulumi.Input[VirtualHardDiskArgs]] = ..., managed_disk: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ..., vhd_containers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createOption")
    def create_option(self) -> pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]:
        
        ...
    
    @create_option.setter
    def create_option(self, value: pulumi.Input[Union[_builtins.str, DiskCreateOptionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingTypes]]:
        
        ...
    
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskDeleteOptionTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diffDiskSettings")
    def diff_disk_settings(self) -> Optional[pulumi.Input[DiffDiskSettingsArgs]]:
        
        ...
    
    @diff_disk_settings.setter
    def diff_disk_settings(self, value: Optional[pulumi.Input[DiffDiskSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[VirtualHardDiskArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[VirtualHardDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]:
        
        ...
    
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[VirtualMachineScaleSetManagedDiskParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[OperatingSystemTypes]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[OperatingSystemTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdContainers")
    def vhd_containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vhd_containers.setter
    def vhd_containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


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
    def __init__(__self__, *, admin_password: Optional[pulumi.Input[_builtins.str]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., allow_extension_operations: Optional[pulumi.Input[_builtins.bool]] = ..., computer_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., custom_data: Optional[pulumi.Input[_builtins.str]] = ..., linux_configuration: Optional[pulumi.Input[LinuxConfigurationArgs]] = ..., require_guest_provision_signal: Optional[pulumi.Input[_builtins.bool]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]] = ..., windows_configuration: Optional[pulumi.Input[WindowsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_extension_operations.setter
    def allow_extension_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerNamePrefix")
    def computer_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computer_name_prefix.setter
    def computer_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[pulumi.Input[LinuxConfigurationArgs]]:
        
        ...
    
    @linux_configuration.setter
    def linux_configuration(self, value: Optional[pulumi.Input[LinuxConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireGuestProvisionSignal")
    def require_guest_provision_signal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_guest_provision_signal.setter
    def require_guest_provision_signal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VaultSecretGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[pulumi.Input[WindowsConfigurationArgs]]:
        
        ...
    
    @windows_configuration.setter
    def windows_configuration(self, value: Optional[pulumi.Input[WindowsConfigurationArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgsDict(TypedDict):
    
    domain_name_label: pulumi.Input[_builtins.str]
    domain_name_label_scope: NotRequired[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]


@pulumi.input_type
class VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs:
    def __init__(__self__, *, domain_name_label: pulumi.Input[_builtins.str], domain_name_label_scope: Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabel")
    def domain_name_label(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name_label.setter
    def domain_name_label(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameLabelScope")
    def domain_name_label_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]:
        
        ...
    
    @domain_name_label_scope.setter
    def domain_name_label_scope(self, value: Optional[pulumi.Input[Union[_builtins.str, DomainNameLabelScopeTypes]]]): # -> None:
        ...
    


class VirtualMachineScaleSetPublicIPAddressConfigurationArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    delete_option: NotRequired[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    dns_settings: NotRequired[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgsDict]]
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ip_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgsDict]]]]
    public_ip_address_version: NotRequired[pulumi.Input[Union[_builtins.str, IPVersion]]]
    public_ip_prefix: NotRequired[pulumi.Input[SubResourceArgsDict]]
    sku: NotRequired[pulumi.Input[PublicIPAddressSkuArgsDict]]


@pulumi.input_type
class VirtualMachineScaleSetPublicIPAddressConfigurationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], delete_option: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]] = ..., dns_settings: Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs]] = ..., idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]] = ..., public_ip_address_version: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]] = ..., public_ip_prefix: Optional[pulumi.Input[SubResourceArgs]] = ..., sku: Optional[pulumi.Input[PublicIPAddressSkuArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]:
        
        ...
    
    @delete_option.setter
    def delete_option(self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]]:
        
        ...
    
    @ip_tags.setter
    def ip_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetIpTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]:
        
        ...
    
    @public_ip_address_version.setter
    def public_ip_address_version(self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @public_ip_prefix.setter
    def public_ip_prefix(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[PublicIPAddressSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[PublicIPAddressSkuArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetStorageProfileArgsDict(TypedDict):
    
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgsDict]]]]
    disk_controller_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]
    image_reference: NotRequired[pulumi.Input[ImageReferenceArgsDict]]
    os_disk: NotRequired[pulumi.Input[VirtualMachineScaleSetOSDiskArgsDict]]


@pulumi.input_type
class VirtualMachineScaleSetStorageProfileArgs:
    def __init__(__self__, *, data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]] = ..., disk_controller_type: Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]] = ..., image_reference: Optional[pulumi.Input[ImageReferenceArgs]] = ..., os_disk: Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetDataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskControllerType")
    def disk_controller_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]:
        
        ...
    
    @disk_controller_type.setter
    def disk_controller_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DiskControllerTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> Optional[pulumi.Input[ImageReferenceArgs]]:
        
        ...
    
    @image_reference.setter
    def image_reference(self, value: Optional[pulumi.Input[ImageReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]]:
        
        ...
    
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[VirtualMachineScaleSetOSDiskArgs]]): # -> None:
        ...
    


class VirtualMachineScaleSetVMNetworkProfileConfigurationArgsDict(TypedDict):
    
    network_interface_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgsDict]]]]


@pulumi.input_type
class VirtualMachineScaleSetVMNetworkProfileConfigurationArgs:
    def __init__(__self__, *, network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceConfigurations")
    def network_interface_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]]:
        
        ...
    
    @network_interface_configurations.setter
    def network_interface_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineScaleSetNetworkConfigurationArgs]]]]): # -> None:
        ...
    


class VirtualMachineScaleSetVMProfileArgsDict(TypedDict):
    
    application_profile: NotRequired[pulumi.Input[ApplicationProfileArgsDict]]
    billing_profile: NotRequired[pulumi.Input[BillingProfileArgsDict]]
    capacity_reservation: NotRequired[pulumi.Input[CapacityReservationProfileArgsDict]]
    diagnostics_profile: NotRequired[pulumi.Input[DiagnosticsProfileArgsDict]]
    eviction_policy: NotRequired[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]]
    extension_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgsDict]]
    hardware_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgsDict]]
    license_type: NotRequired[pulumi.Input[_builtins.str]]
    network_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgsDict]]
    os_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetOSProfileArgsDict]]
    priority: NotRequired[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]]
    scheduled_events_profile: NotRequired[pulumi.Input[ScheduledEventsProfileArgsDict]]
    security_posture_reference: NotRequired[pulumi.Input[SecurityPostureReferenceArgsDict]]
    security_profile: NotRequired[pulumi.Input[SecurityProfileArgsDict]]
    service_artifact_reference: NotRequired[pulumi.Input[ServiceArtifactReferenceArgsDict]]
    storage_profile: NotRequired[pulumi.Input[VirtualMachineScaleSetStorageProfileArgsDict]]
    user_data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineScaleSetVMProfileArgs:
    def __init__(__self__, *, application_profile: Optional[pulumi.Input[ApplicationProfileArgs]] = ..., billing_profile: Optional[pulumi.Input[BillingProfileArgs]] = ..., capacity_reservation: Optional[pulumi.Input[CapacityReservationProfileArgs]] = ..., diagnostics_profile: Optional[pulumi.Input[DiagnosticsProfileArgs]] = ..., eviction_policy: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]] = ..., extension_profile: Optional[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]] = ..., hardware_profile: Optional[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]] = ..., os_profile: Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]] = ..., priority: Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]] = ..., scheduled_events_profile: Optional[pulumi.Input[ScheduledEventsProfileArgs]] = ..., security_posture_reference: Optional[pulumi.Input[SecurityPostureReferenceArgs]] = ..., security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ..., service_artifact_reference: Optional[pulumi.Input[ServiceArtifactReferenceArgs]] = ..., storage_profile: Optional[pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[pulumi.Input[ApplicationProfileArgs]]:
        
        ...
    
    @application_profile.setter
    def application_profile(self, value: Optional[pulumi.Input[ApplicationProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfile")
    def billing_profile(self) -> Optional[pulumi.Input[BillingProfileArgs]]:
        
        ...
    
    @billing_profile.setter
    def billing_profile(self, value: Optional[pulumi.Input[BillingProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(self) -> Optional[pulumi.Input[CapacityReservationProfileArgs]]:
        
        ...
    
    @capacity_reservation.setter
    def capacity_reservation(self, value: Optional[pulumi.Input[CapacityReservationProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[pulumi.Input[DiagnosticsProfileArgs]]:
        
        ...
    
    @diagnostics_profile.setter
    def diagnostics_profile(self, value: Optional[pulumi.Input[DiagnosticsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]]:
        
        ...
    
    @eviction_policy.setter
    def eviction_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionProfile")
    def extension_profile(self) -> Optional[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]]:
        
        ...
    
    @extension_profile.setter
    def extension_profile(self, value: Optional[pulumi.Input[VirtualMachineScaleSetExtensionProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]]:
        
        ...
    
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[VirtualMachineScaleSetHardwareProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[VirtualMachineScaleSetNetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]]:
        
        ...
    
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[VirtualMachineScaleSetOSProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(self) -> Optional[pulumi.Input[ScheduledEventsProfileArgs]]:
        
        ...
    
    @scheduled_events_profile.setter
    def scheduled_events_profile(self, value: Optional[pulumi.Input[ScheduledEventsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureReference")
    def security_posture_reference(self) -> Optional[pulumi.Input[SecurityPostureReferenceArgs]]:
        
        ...
    
    @security_posture_reference.setter
    def security_posture_reference(self, value: Optional[pulumi.Input[SecurityPostureReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReference")
    def service_artifact_reference(self) -> Optional[pulumi.Input[ServiceArtifactReferenceArgs]]:
        
        ...
    
    @service_artifact_reference.setter
    def service_artifact_reference(self, value: Optional[pulumi.Input[ServiceArtifactReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[VirtualMachineScaleSetStorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineScaleSetVMProtectionPolicyArgsDict(TypedDict):
    
    protect_from_scale_in: NotRequired[pulumi.Input[_builtins.bool]]
    protect_from_scale_set_actions: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VirtualMachineScaleSetVMProtectionPolicyArgs:
    def __init__(__self__, *, protect_from_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., protect_from_scale_set_actions: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectFromScaleIn")
    def protect_from_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @protect_from_scale_in.setter
    def protect_from_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectFromScaleSetActions")
    def protect_from_scale_set_actions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @protect_from_scale_set_actions.setter
    def protect_from_scale_set_actions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WinRMConfigurationArgsDict(TypedDict):
    
    listeners: NotRequired[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgsDict]]]]


@pulumi.input_type
class WinRMConfigurationArgs:
    def __init__(__self__, *, listeners: Optional[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]]:
        
        ...
    
    @listeners.setter
    def listeners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WinRMListenerArgs]]]]): # -> None:
        ...
    


class WinRMListenerArgsDict(TypedDict):
    
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[ProtocolTypes]]


@pulumi.input_type
class WinRMListenerArgs:
    def __init__(__self__, *, certificate_url: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[ProtocolTypes]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[ProtocolTypes]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[ProtocolTypes]]): # -> None:
        ...
    


class WindowsConfigurationArgsDict(TypedDict):
    
    additional_unattend_content: NotRequired[pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgsDict]]]]
    enable_automatic_updates: NotRequired[pulumi.Input[_builtins.bool]]
    patch_settings: NotRequired[pulumi.Input[PatchSettingsArgsDict]]
    provision_vm_agent: NotRequired[pulumi.Input[_builtins.bool]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    win_rm: NotRequired[pulumi.Input[WinRMConfigurationArgsDict]]


@pulumi.input_type
class WindowsConfigurationArgs:
    def __init__(__self__, *, additional_unattend_content: Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]] = ..., enable_automatic_updates: Optional[pulumi.Input[_builtins.bool]] = ..., patch_settings: Optional[pulumi.Input[PatchSettingsArgs]] = ..., provision_vm_agent: Optional[pulumi.Input[_builtins.bool]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., win_rm: Optional[pulumi.Input[WinRMConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalUnattendContent")
    def additional_unattend_content(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]]:
        
        ...
    
    @additional_unattend_content.setter
    def additional_unattend_content(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AdditionalUnattendContentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_updates.setter
    def enable_automatic_updates(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchSettings")
    def patch_settings(self) -> Optional[pulumi.Input[PatchSettingsArgs]]:
        
        ...
    
    @patch_settings.setter
    def patch_settings(self, value: Optional[pulumi.Input[PatchSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionVMAgent")
    def provision_vm_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @provision_vm_agent.setter
    def provision_vm_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="winRM")
    def win_rm(self) -> Optional[pulumi.Input[WinRMConfigurationArgs]]:
        
        ...
    
    @win_rm.setter
    def win_rm(self, value: Optional[pulumi.Input[WinRMConfigurationArgs]]): # -> None:
        ...
    


class WindowsVMGuestPatchAutomaticByPlatformSettingsArgsDict(TypedDict):
    
    bypass_platform_safety_checks_on_user_schedule: NotRequired[pulumi.Input[_builtins.bool]]
    reboot_setting: NotRequired[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]]]


@pulumi.input_type
class WindowsVMGuestPatchAutomaticByPlatformSettingsArgs:
    def __init__(__self__, *, bypass_platform_safety_checks_on_user_schedule: Optional[pulumi.Input[_builtins.bool]] = ..., reboot_setting: Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bypassPlatformSafetyChecksOnUserSchedule")
    def bypass_platform_safety_checks_on_user_schedule(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bypass_platform_safety_checks_on_user_schedule.setter
    def bypass_platform_safety_checks_on_user_schedule(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]]]:
        
        ...
    
    @reboot_setting.setter
    def reboot_setting(self, value: Optional[pulumi.Input[Union[_builtins.str, WindowsVMGuestPatchAutomaticByPlatformRebootSetting]]]): # -> None:
        ...
    


