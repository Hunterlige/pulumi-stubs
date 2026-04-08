import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "A2AContainerMappingInputArgs",
    "A2AContainerMappingInputArgsDict",
    "A2ACrossClusterMigrationEnableProtectionInputArgs",
    ...,
    "A2ACrossClusterMigrationPolicyCreationInputArgs",
    ...,
    "A2AEnableProtectionInputArgs",
    "A2AEnableProtectionInputArgsDict",
    "A2APolicyCreationInputArgs",
    "A2APolicyCreationInputArgsDict",
    "A2AProtectedManagedDiskDetailsArgs",
    "A2AProtectedManagedDiskDetailsArgsDict",
    "A2AReplicationProtectionClusterDetailsArgs",
    "A2AReplicationProtectionClusterDetailsArgsDict",
    "A2ASharedDiskReplicationDetailsArgs",
    "A2ASharedDiskReplicationDetailsArgsDict",
    "A2AUnprotectedDiskDetailsArgs",
    "A2AUnprotectedDiskDetailsArgsDict",
    "A2AVmDiskInputDetailsArgs",
    "A2AVmDiskInputDetailsArgsDict",
    "A2AVmManagedDiskInputDetailsArgs",
    "A2AVmManagedDiskInputDetailsArgsDict",
    "AADProperties",
    "AADPropertiesDict",
    "AddRecoveryServicesProviderInputPropertiesArgs",
    "AddRecoveryServicesProviderInputPropertiesArgsDict",
    "AddVCenterRequestPropertiesArgs",
    "AddVCenterRequestPropertiesArgsDict",
    "AzureBackupServerContainerArgs",
    "AzureBackupServerContainerArgsDict",
    "AzureFabricCreationInputArgs",
    "AzureFabricCreationInputArgsDict",
    "AzureFileShareProtectionPolicyArgs",
    "AzureFileShareProtectionPolicyArgsDict",
    "AzureFileshareProtectedItemExtendedInfoArgs",
    "AzureFileshareProtectedItemExtendedInfoArgsDict",
    "AzureFileshareProtectedItemArgs",
    "AzureFileshareProtectedItemArgsDict",
    "AzureIaaSClassicComputeVMContainerArgs",
    "AzureIaaSClassicComputeVMContainerArgsDict",
    "AzureIaaSClassicComputeVMProtectedItemArgs",
    "AzureIaaSClassicComputeVMProtectedItemArgsDict",
    "AzureIaaSComputeVMContainerArgs",
    "AzureIaaSComputeVMContainerArgsDict",
    "AzureIaaSComputeVMProtectedItemArgs",
    "AzureIaaSComputeVMProtectedItemArgsDict",
    "AzureIaaSVMProtectedItemExtendedInfoArgs",
    "AzureIaaSVMProtectedItemExtendedInfoArgsDict",
    "AzureIaaSVMProtectedItemArgs",
    "AzureIaaSVMProtectedItemArgsDict",
    "AzureIaaSVMProtectionPolicyArgs",
    "AzureIaaSVMProtectionPolicyArgsDict",
    "AzureMonitorAlertSettingsArgs",
    "AzureMonitorAlertSettingsArgsDict",
    "AzureRecoveryServiceVaultProtectionIntentArgs",
    "AzureRecoveryServiceVaultProtectionIntentArgsDict",
    "AzureResourceProtectionIntentArgs",
    "AzureResourceProtectionIntentArgsDict",
    "AzureSQLAGWorkloadContainerProtectionContainerArgs",
    ...,
    "AzureSqlContainerArgs",
    "AzureSqlContainerArgsDict",
    "AzureSqlProtectedItemExtendedInfoArgs",
    "AzureSqlProtectedItemExtendedInfoArgsDict",
    "AzureSqlProtectedItemArgs",
    "AzureSqlProtectedItemArgsDict",
    "AzureSqlProtectionPolicyArgs",
    "AzureSqlProtectionPolicyArgsDict",
    "AzureStorageContainerArgs",
    "AzureStorageContainerArgsDict",
    "AzureToAzureCreateNetworkMappingInputArgs",
    "AzureToAzureCreateNetworkMappingInputArgsDict",
    "AzureVMAppContainerProtectionContainerArgs",
    "AzureVMAppContainerProtectionContainerArgsDict",
    "AzureVmWorkloadProtectedItemExtendedInfoArgs",
    "AzureVmWorkloadProtectedItemExtendedInfoArgsDict",
    "AzureVmWorkloadProtectedItemArgs",
    "AzureVmWorkloadProtectedItemArgsDict",
    "AzureVmWorkloadProtectionPolicyArgs",
    "AzureVmWorkloadProtectionPolicyArgsDict",
    "AzureVmWorkloadSAPAseDatabaseProtectedItemArgs",
    "AzureVmWorkloadSAPAseDatabaseProtectedItemArgsDict",
    "AzureVmWorkloadSAPHanaDBInstanceProtectedItemArgs",
    ...,
    "AzureVmWorkloadSAPHanaDatabaseProtectedItemArgs",
    ...,
    "AzureVmWorkloadSQLDatabaseProtectedItemArgs",
    "AzureVmWorkloadSQLDatabaseProtectedItemArgsDict",
    "AzureWorkloadAutoProtectionIntentArgs",
    "AzureWorkloadAutoProtectionIntentArgsDict",
    "AzureWorkloadContainerAutoProtectionIntentArgs",
    "AzureWorkloadContainerAutoProtectionIntentArgsDict",
    "AzureWorkloadContainerExtendedInfoArgs",
    "AzureWorkloadContainerExtendedInfoArgsDict",
    "AzureWorkloadContainerArgs",
    "AzureWorkloadContainerArgsDict",
    "AzureWorkloadSQLAutoProtectionIntentArgs",
    "AzureWorkloadSQLAutoProtectionIntentArgsDict",
    "ClassicAlertSettingsArgs",
    "ClassicAlertSettingsArgsDict",
    "CmkKekIdentityArgs",
    "CmkKekIdentityArgsDict",
    "CmkKeyVaultPropertiesArgs",
    "CmkKeyVaultPropertiesArgsDict",
    "ContainerIdentityInfoArgs",
    "ContainerIdentityInfoArgsDict",
    "CreateNetworkMappingInputPropertiesArgs",
    "CreateNetworkMappingInputPropertiesArgsDict",
    "CreatePolicyInputPropertiesArgs",
    "CreatePolicyInputPropertiesArgsDict",
    ...,
    ...,
    "CreateRecoveryPlanInputPropertiesArgs",
    "CreateRecoveryPlanInputPropertiesArgsDict",
    "CrossSubscriptionRestoreSettingsArgs",
    "CrossSubscriptionRestoreSettingsArgsDict",
    "CurrentScenarioDetailsArgs",
    "CurrentScenarioDetailsArgsDict",
    "DPMContainerExtendedInfoArgs",
    "DPMContainerExtendedInfoArgsDict",
    "DPMProtectedItemExtendedInfoArgs",
    "DPMProtectedItemExtendedInfoArgsDict",
    "DPMProtectedItemArgs",
    "DPMProtectedItemArgsDict",
    "DailyRetentionFormatArgs",
    "DailyRetentionFormatArgsDict",
    "DailyRetentionScheduleArgs",
    "DailyRetentionScheduleArgsDict",
    "DailyScheduleArgs",
    "DailyScheduleArgsDict",
    "DayArgs",
    "DayArgsDict",
    "DiskEncryptionInfoArgs",
    "DiskEncryptionInfoArgsDict",
    "DiskEncryptionKeyInfoArgs",
    "DiskEncryptionKeyInfoArgsDict",
    "DiskExclusionPropertiesArgs",
    "DiskExclusionPropertiesArgsDict",
    "DistributedNodesInfoArgs",
    "DistributedNodesInfoArgsDict",
    "DpmContainerArgs",
    "DpmContainerArgsDict",
    "EnableMigrationInputPropertiesArgs",
    "EnableMigrationInputPropertiesArgsDict",
    "EnableProtectionInputPropertiesArgs",
    "EnableProtectionInputPropertiesArgsDict",
    "ExtendedLocationArgs",
    "ExtendedLocationArgsDict",
    "ExtendedPropertiesArgs",
    "ExtendedPropertiesArgsDict",
    "FabricCreationInputPropertiesArgs",
    "FabricCreationInputPropertiesArgsDict",
    "GenericContainerExtendedInfoArgs",
    "GenericContainerExtendedInfoArgsDict",
    "GenericContainerArgs",
    "GenericContainerArgsDict",
    "GenericProtectedItemArgs",
    "GenericProtectedItemArgsDict",
    "GenericProtectionPolicyArgs",
    "GenericProtectionPolicyArgsDict",
    "HealthErrorArgs",
    "HealthErrorArgsDict",
    "HourlyScheduleArgs",
    "HourlyScheduleArgsDict",
    "HyperVReplicaAzureDiskInputDetailsArgs",
    "HyperVReplicaAzureDiskInputDetailsArgsDict",
    "HyperVReplicaAzureEnableProtectionInputArgs",
    "HyperVReplicaAzureEnableProtectionInputArgsDict",
    "HyperVReplicaAzurePolicyInputArgs",
    "HyperVReplicaAzurePolicyInputArgsDict",
    "HyperVReplicaBluePolicyInputArgs",
    "HyperVReplicaBluePolicyInputArgsDict",
    "HyperVReplicaPolicyInputArgs",
    "HyperVReplicaPolicyInputArgsDict",
    "IaaSVMContainerArgs",
    "IaaSVMContainerArgsDict",
    "IdentityDataArgs",
    "IdentityDataArgsDict",
    "IdentityProviderInputArgs",
    "IdentityProviderInputArgsDict",
    "ImmutabilitySettingsArgs",
    "ImmutabilitySettingsArgsDict",
    "InMageAzureV2DiskInputDetailsArgs",
    "InMageAzureV2DiskInputDetailsArgsDict",
    "InMageAzureV2EnableProtectionInputArgs",
    "InMageAzureV2EnableProtectionInputArgsDict",
    "InMageAzureV2PolicyInputArgs",
    "InMageAzureV2PolicyInputArgsDict",
    "InMageDiskExclusionInputArgs",
    "InMageDiskExclusionInputArgsDict",
    "InMageDiskSignatureExclusionOptionsArgs",
    "InMageDiskSignatureExclusionOptionsArgsDict",
    "InMageEnableProtectionInputArgs",
    "InMageEnableProtectionInputArgsDict",
    "InMagePolicyInputArgs",
    "InMagePolicyInputArgsDict",
    "InMageRcmDiskInputArgs",
    "InMageRcmDiskInputArgsDict",
    "InMageRcmDisksDefaultInputArgs",
    "InMageRcmDisksDefaultInputArgsDict",
    "InMageRcmEnableProtectionInputArgs",
    "InMageRcmEnableProtectionInputArgsDict",
    "InMageRcmFabricCreationInputArgs",
    "InMageRcmFabricCreationInputArgsDict",
    "InMageRcmFailbackPolicyCreationInputArgs",
    "InMageRcmFailbackPolicyCreationInputArgsDict",
    "InMageRcmPolicyCreationInputArgs",
    "InMageRcmPolicyCreationInputArgsDict",
    "InMageVolumeExclusionOptionsArgs",
    "InMageVolumeExclusionOptionsArgsDict",
    "InnerHealthErrorArgs",
    "InnerHealthErrorArgsDict",
    "InquiryInfoArgs",
    "InquiryInfoArgsDict",
    "InquiryValidationArgs",
    "InquiryValidationArgsDict",
    "InstantRPAdditionalDetailsArgs",
    "InstantRPAdditionalDetailsArgsDict",
    "KPIResourceHealthDetailsArgs",
    "KPIResourceHealthDetailsArgsDict",
    "KeyEncryptionKeyInfoArgs",
    "KeyEncryptionKeyInfoArgsDict",
    "LogSchedulePolicyArgs",
    "LogSchedulePolicyArgsDict",
    "LongTermRetentionPolicyArgs",
    "LongTermRetentionPolicyArgsDict",
    "LongTermSchedulePolicyArgs",
    "LongTermSchedulePolicyArgsDict",
    "MABContainerHealthDetailsArgs",
    "MABContainerHealthDetailsArgsDict",
    "MabContainerExtendedInfoArgs",
    "MabContainerExtendedInfoArgsDict",
    "MabContainerArgs",
    "MabContainerArgsDict",
    "MabFileFolderProtectedItemExtendedInfoArgs",
    "MabFileFolderProtectedItemExtendedInfoArgsDict",
    "MabFileFolderProtectedItemArgs",
    "MabFileFolderProtectedItemArgsDict",
    "MabProtectionPolicyArgs",
    "MabProtectionPolicyArgsDict",
    "MonitoringSettingsArgs",
    "MonitoringSettingsArgsDict",
    "MonthlyRetentionScheduleArgs",
    "MonthlyRetentionScheduleArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "RecoveryPlanA2AInputArgs",
    "RecoveryPlanA2AInputArgsDict",
    "RecoveryPlanActionArgs",
    "RecoveryPlanActionArgsDict",
    "RecoveryPlanAutomationRunbookActionDetailsArgs",
    "RecoveryPlanAutomationRunbookActionDetailsArgsDict",
    "RecoveryPlanGroupArgs",
    "RecoveryPlanGroupArgsDict",
    "RecoveryPlanManualActionDetailsArgs",
    "RecoveryPlanManualActionDetailsArgsDict",
    "RecoveryPlanProtectedItemArgs",
    "RecoveryPlanProtectedItemArgsDict",
    "RecoveryPlanScriptActionDetailsArgs",
    "RecoveryPlanScriptActionDetailsArgsDict",
    "RegisteredClusterNodesArgs",
    "RegisteredClusterNodesArgsDict",
    "ReplicationProtectionClusterPropertiesArgs",
    "ReplicationProtectionClusterPropertiesArgsDict",
    "ResourceGuardOperationDetailArgs",
    "ResourceGuardOperationDetailArgsDict",
    "ResourceGuardProxyBaseArgs",
    "ResourceGuardProxyBaseArgsDict",
    "RestoreSettingsArgs",
    "RestoreSettingsArgsDict",
    "RetentionDurationArgs",
    "RetentionDurationArgsDict",
    "SecurityProfilePropertiesArgs",
    "SecurityProfilePropertiesArgsDict",
    "SecuritySettingsArgs",
    "SecuritySettingsArgsDict",
    "SettingsArgs",
    "SettingsArgsDict",
    "SharedDiskReplicationItemPropertiesArgs",
    "SharedDiskReplicationItemPropertiesArgsDict",
    "SimpleRetentionPolicyArgs",
    "SimpleRetentionPolicyArgsDict",
    "SimpleSchedulePolicyV2Args",
    "SimpleSchedulePolicyV2ArgsDict",
    "SimpleSchedulePolicyArgs",
    "SimpleSchedulePolicyArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SnapshotBackupAdditionalDetailsArgs",
    "SnapshotBackupAdditionalDetailsArgsDict",
    "SoftDeleteSettingsArgs",
    "SoftDeleteSettingsArgsDict",
    "StorageMappingInputPropertiesArgs",
    "StorageMappingInputPropertiesArgsDict",
    "SubProtectionPolicyArgs",
    "SubProtectionPolicyArgsDict",
    "TieringPolicyArgs",
    "TieringPolicyArgsDict",
    "UserAssignedIdentityPropertiesArgs",
    "UserAssignedIdentityPropertiesArgsDict",
    "UserAssignedManagedIdentityDetailsArgs",
    "UserAssignedManagedIdentityDetailsArgsDict",
    "UserCreatedResourceTagArgs",
    "UserCreatedResourceTagArgsDict",
    "VMwareCbtContainerMappingInputArgs",
    "VMwareCbtContainerMappingInputArgsDict",
    "VMwareCbtDiskInputArgs",
    "VMwareCbtDiskInputArgsDict",
    "VMwareCbtEnableMigrationInputArgs",
    "VMwareCbtEnableMigrationInputArgsDict",
    "VMwareCbtPolicyCreationInputArgs",
    "VMwareCbtPolicyCreationInputArgsDict",
    "VMwareCbtSecurityProfilePropertiesArgs",
    "VMwareCbtSecurityProfilePropertiesArgsDict",
    "VMwareV2FabricCreationInputArgs",
    "VMwareV2FabricCreationInputArgsDict",
    "VaultPropertiesEncryptionArgs",
    "VaultPropertiesEncryptionArgsDict",
    "VaultPropertiesRedundancySettingsArgs",
    "VaultPropertiesRedundancySettingsArgsDict",
    "VaultPropertiesArgs",
    "VaultPropertiesArgsDict",
    "VaultRetentionPolicyArgs",
    "VaultRetentionPolicyArgsDict",
    "VmmToAzureCreateNetworkMappingInputArgs",
    "VmmToAzureCreateNetworkMappingInputArgsDict",
    "VmmToVmmCreateNetworkMappingInputArgs",
    "VmmToVmmCreateNetworkMappingInputArgsDict",
    "WeeklyRetentionFormatArgs",
    "WeeklyRetentionFormatArgsDict",
    "WeeklyRetentionScheduleArgs",
    "WeeklyRetentionScheduleArgsDict",
    "WeeklyScheduleArgs",
    "WeeklyScheduleArgsDict",
    "WorkloadInquiryDetailsArgs",
    "WorkloadInquiryDetailsArgsDict",
    "YearlyRetentionScheduleArgs",
    "YearlyRetentionScheduleArgsDict",
]

class A2AContainerMappingInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    agent_auto_update_status: NotRequired[
        pulumi.Input[Union[_builtins.str, AgentAutoUpdateStatus]]
    ]
    automation_account_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    automation_account_authentication_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AutomationAccountAuthenticationType]]
    ]

@pulumi.input_type
class A2AContainerMappingInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        agent_auto_update_status: Optional[
            pulumi.Input[Union[_builtins.str, AgentAutoUpdateStatus]]
        ] = ...,
        automation_account_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        automation_account_authentication_type: Optional[
            pulumi.Input[Union[_builtins.str, AutomationAccountAuthenticationType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentAutoUpdateStatus")
    def agent_auto_update_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AgentAutoUpdateStatus]]]: ...
    @agent_auto_update_status.setter
    def agent_auto_update_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AgentAutoUpdateStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automationAccountArmId")
    def automation_account_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @automation_account_arm_id.setter
    def automation_account_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automationAccountAuthenticationType")
    def automation_account_authentication_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AutomationAccountAuthenticationType]]
    ]: ...
    @automation_account_authentication_type.setter
    def automation_account_authentication_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AutomationAccountAuthenticationType]]
        ],
    ): ...

class A2ACrossClusterMigrationEnableProtectionInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    fabric_object_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_container_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class A2ACrossClusterMigrationEnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        fabric_object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fabric_object_id.setter
    def fabric_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryContainerId")
    def recovery_container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_container_id.setter
    def recovery_container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class A2ACrossClusterMigrationPolicyCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class A2ACrossClusterMigrationPolicyCreationInputArgs:
    def __init__(__self__, *, instance_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...

class A2AEnableProtectionInputArgsDict(TypedDict):
    fabric_object_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    auto_protection_of_data_disk: NotRequired[
        pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]
    ]
    disk_encryption_info: NotRequired[pulumi.Input[DiskEncryptionInfoArgsDict]]
    multi_vm_group_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_vm_group_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    recovery_azure_network_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_boot_diag_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_capacity_reservation_group_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_cloud_service_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_container_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_extended_location: NotRequired[pulumi.Input[ExtendedLocationArgsDict]]
    recovery_proximity_placement_group_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    recovery_virtual_machine_scale_set_id: NotRequired[pulumi.Input[_builtins.str]]
    vm_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[A2AVmDiskInputDetailsArgsDict]]]
    ]
    vm_managed_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[A2AVmManagedDiskInputDetailsArgsDict]]]
    ]

@pulumi.input_type
class A2AEnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        fabric_object_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        auto_protection_of_data_disk: Optional[
            pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]
        ] = ...,
        disk_encryption_info: Optional[pulumi.Input[DiskEncryptionInfoArgs]] = ...,
        multi_vm_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_vm_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_azure_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_boot_diag_storage_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        recovery_capacity_reservation_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        recovery_cloud_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        recovery_proximity_placement_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        recovery_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_virtual_machine_scale_set_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        vm_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AVmDiskInputDetailsArgs]]]
        ] = ...,
        vm_managed_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AVmManagedDiskInputDetailsArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_object_id.setter
    def fabric_object_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoProtectionOfDataDisk")
    def auto_protection_of_data_disk(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]]: ...
    @auto_protection_of_data_disk.setter
    def auto_protection_of_data_disk(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionInfo")
    def disk_encryption_info(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionInfoArgs]]: ...
    @disk_encryption_info.setter
    def disk_encryption_info(
        self, value: Optional[pulumi.Input[DiskEncryptionInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_id.setter
    def multi_vm_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_name.setter
    def multi_vm_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionClusterId")
    def protection_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_cluster_id.setter
    def protection_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilitySetId")
    def recovery_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_availability_set_id.setter
    def recovery_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilityZone")
    def recovery_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_availability_zone.setter
    def recovery_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryAzureNetworkId")
    def recovery_azure_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_azure_network_id.setter
    def recovery_azure_network_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryBootDiagStorageAccountId")
    def recovery_boot_diag_storage_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_boot_diag_storage_account_id.setter
    def recovery_boot_diag_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryCapacityReservationGroupId")
    def recovery_capacity_reservation_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_capacity_reservation_group_id.setter
    def recovery_capacity_reservation_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryCloudServiceId")
    def recovery_cloud_service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_cloud_service_id.setter
    def recovery_cloud_service_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryContainerId")
    def recovery_container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_container_id.setter
    def recovery_container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @recovery_extended_location.setter
    def recovery_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryProximityPlacementGroupId")
    def recovery_proximity_placement_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_proximity_placement_group_id.setter
    def recovery_proximity_placement_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryResourceGroupId")
    def recovery_resource_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_resource_group_id.setter
    def recovery_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoverySubnetName")
    def recovery_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_subnet_name.setter
    def recovery_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryVirtualMachineScaleSetId")
    def recovery_virtual_machine_scale_set_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_virtual_machine_scale_set_id.setter
    def recovery_virtual_machine_scale_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmDisks")
    def vm_disks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[A2AVmDiskInputDetailsArgs]]]]: ...
    @vm_disks.setter
    def vm_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AVmDiskInputDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmManagedDisks")
    def vm_managed_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[A2AVmManagedDiskInputDetailsArgs]]]
    ]: ...
    @vm_managed_disks.setter
    def vm_managed_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AVmManagedDiskInputDetailsArgs]]]
        ],
    ): ...

class A2APolicyCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    crash_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_history: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class A2APolicyCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        crash_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        recovery_point_history: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]: ...
    @multi_vm_sync_status.setter
    def multi_vm_sync_status(
        self, value: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history.setter
    def recovery_point_history(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class A2AProtectedManagedDiskDetailsArgsDict(TypedDict):
    allowed_disk_level_operation: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    data_pending_at_source_agent_in_mb: NotRequired[pulumi.Input[_builtins.float]]
    data_pending_in_staging_storage_account_in_mb: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    dek_key_vault_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_capacity_in_bytes: NotRequired[pulumi.Input[_builtins.float]]
    disk_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_name: NotRequired[pulumi.Input[_builtins.str]]
    disk_state: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    failover_disk_name: NotRequired[pulumi.Input[_builtins.str]]
    is_disk_encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    is_disk_key_encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    kek_key_vault_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    key_identifier: NotRequired[pulumi.Input[_builtins.str]]
    monitoring_job_type: NotRequired[pulumi.Input[_builtins.str]]
    monitoring_percentage_completion: NotRequired[pulumi.Input[_builtins.int]]
    primary_disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_staging_azure_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_orignal_target_disk_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_replica_disk_account_type: NotRequired[pulumi.Input[_builtins.str]]
    recovery_replica_disk_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_target_disk_account_type: NotRequired[pulumi.Input[_builtins.str]]
    recovery_target_disk_id: NotRequired[pulumi.Input[_builtins.str]]
    resync_required: NotRequired[pulumi.Input[_builtins.bool]]
    secret_identifier: NotRequired[pulumi.Input[_builtins.str]]
    tfo_disk_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class A2AProtectedManagedDiskDetailsArgs:
    def __init__(
        __self__,
        *,
        allowed_disk_level_operation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_pending_at_source_agent_in_mb: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        data_pending_in_staging_storage_account_in_mb: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        dek_key_vault_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_capacity_in_bytes: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_state: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_disk_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_disk_key_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kek_key_vault_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_percentage_completion: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_staging_azure_storage_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        recovery_disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_orignal_target_disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_replica_disk_account_type: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_replica_disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_target_disk_account_type: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_target_disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resync_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        secret_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tfo_disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDiskLevelOperation")
    def allowed_disk_level_operation(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_disk_level_operation.setter
    def allowed_disk_level_operation(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPendingAtSourceAgentInMB")
    def data_pending_at_source_agent_in_mb(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @data_pending_at_source_agent_in_mb.setter
    def data_pending_at_source_agent_in_mb(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPendingInStagingStorageAccountInMB")
    def data_pending_in_staging_storage_account_in_mb(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @data_pending_in_staging_storage_account_in_mb.setter
    def data_pending_in_staging_storage_account_in_mb(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dekKeyVaultArmId")
    def dek_key_vault_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dek_key_vault_arm_id.setter
    def dek_key_vault_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskCapacityInBytes")
    def disk_capacity_in_bytes(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_capacity_in_bytes.setter
    def disk_capacity_in_bytes(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_state.setter
    def disk_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverDiskName")
    def failover_disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover_disk_name.setter
    def failover_disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDiskEncrypted")
    def is_disk_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_disk_encrypted.setter
    def is_disk_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDiskKeyEncrypted")
    def is_disk_key_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_disk_key_encrypted.setter
    def is_disk_key_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kekKeyVaultArmId")
    def kek_key_vault_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kek_key_vault_arm_id.setter
    def kek_key_vault_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_identifier.setter
    def key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_job_type.setter
    def monitoring_job_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitoring_percentage_completion.setter
    def monitoring_percentage_completion(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryDiskEncryptionSetId")
    def primary_disk_encryption_set_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_disk_encryption_set_id.setter
    def primary_disk_encryption_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryStagingAzureStorageAccountId")
    def primary_staging_azure_storage_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_staging_azure_storage_account_id.setter
    def primary_staging_azure_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryDiskEncryptionSetId")
    def recovery_disk_encryption_set_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_disk_encryption_set_id.setter
    def recovery_disk_encryption_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryOrignalTargetDiskId")
    def recovery_orignal_target_disk_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_orignal_target_disk_id.setter
    def recovery_orignal_target_disk_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryReplicaDiskAccountType")
    def recovery_replica_disk_account_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_replica_disk_account_type.setter
    def recovery_replica_disk_account_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryReplicaDiskId")
    def recovery_replica_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_replica_disk_id.setter
    def recovery_replica_disk_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryResourceGroupId")
    def recovery_resource_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_resource_group_id.setter
    def recovery_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryTargetDiskAccountType")
    def recovery_target_disk_account_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_target_disk_account_type.setter
    def recovery_target_disk_account_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryTargetDiskId")
    def recovery_target_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_target_disk_id.setter
    def recovery_target_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @resync_required.setter
    def resync_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_identifier.setter
    def secret_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tfoDiskName")
    def tfo_disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tfo_disk_name.setter
    def tfo_disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class A2AReplicationProtectionClusterDetailsArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    cluster_management_id: NotRequired[pulumi.Input[_builtins.str]]
    failover_recovery_point_id: NotRequired[pulumi.Input[_builtins.str]]
    initial_primary_extended_location: NotRequired[
        pulumi.Input[ExtendedLocationArgsDict]
    ]
    initial_primary_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    initial_primary_zone: NotRequired[pulumi.Input[_builtins.str]]
    initial_recovery_extended_location: NotRequired[
        pulumi.Input[ExtendedLocationArgsDict]
    ]
    initial_recovery_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    initial_recovery_zone: NotRequired[pulumi.Input[_builtins.str]]
    last_rpo_calculated_time: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_vm_group_create_option: NotRequired[
        pulumi.Input[Union[_builtins.str, MultiVmGroupCreateOption]]
    ]
    multi_vm_group_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_vm_group_name: NotRequired[pulumi.Input[_builtins.str]]
    primary_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    primary_extended_location: NotRequired[pulumi.Input[ExtendedLocationArgsDict]]
    primary_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    recovery_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    recovery_extended_location: NotRequired[pulumi.Input[ExtendedLocationArgsDict]]
    recovery_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    rpo_in_seconds: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class A2AReplicationProtectionClusterDetailsArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        cluster_management_id: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_recovery_point_id: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_primary_extended_location: Optional[
            pulumi.Input[ExtendedLocationArgs]
        ] = ...,
        initial_primary_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_primary_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_recovery_extended_location: Optional[
            pulumi.Input[ExtendedLocationArgs]
        ] = ...,
        initial_recovery_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_recovery_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        last_rpo_calculated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_vm_group_create_option: Optional[
            pulumi.Input[Union[_builtins.str, MultiVmGroupCreateOption]]
        ] = ...,
        multi_vm_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_vm_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        primary_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        recovery_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        rpo_in_seconds: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterManagementId")
    def cluster_management_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_management_id.setter
    def cluster_management_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover_recovery_point_id.setter
    def failover_recovery_point_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialPrimaryExtendedLocation")
    def initial_primary_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @initial_primary_extended_location.setter
    def initial_primary_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialPrimaryFabricLocation")
    def initial_primary_fabric_location(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_primary_fabric_location.setter
    def initial_primary_fabric_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialPrimaryZone")
    def initial_primary_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_primary_zone.setter
    def initial_primary_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialRecoveryExtendedLocation")
    def initial_recovery_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @initial_recovery_extended_location.setter
    def initial_recovery_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialRecoveryFabricLocation")
    def initial_recovery_fabric_location(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_recovery_fabric_location.setter
    def initial_recovery_fabric_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialRecoveryZone")
    def initial_recovery_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_recovery_zone.setter
    def initial_recovery_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_rpo_calculated_time.setter
    def last_rpo_calculated_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleId")
    def lifecycle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_id.setter
    def lifecycle_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupCreateOption")
    def multi_vm_group_create_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MultiVmGroupCreateOption]]]: ...
    @multi_vm_group_create_option.setter
    def multi_vm_group_create_option(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, MultiVmGroupCreateOption]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_id.setter
    def multi_vm_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_name.setter
    def multi_vm_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_availability_zone.setter
    def primary_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @primary_extended_location.setter
    def primary_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_fabric_location.setter
    def primary_fabric_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilityZone")
    def recovery_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_availability_zone.setter
    def recovery_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @recovery_extended_location.setter
    def recovery_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_fabric_location.setter
    def recovery_fabric_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @rpo_in_seconds.setter
    def rpo_in_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class A2ASharedDiskReplicationDetailsArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    failover_recovery_point_id: NotRequired[pulumi.Input[_builtins.str]]
    last_rpo_calculated_time: NotRequired[pulumi.Input[_builtins.str]]
    management_id: NotRequired[pulumi.Input[_builtins.str]]
    monitoring_job_type: NotRequired[pulumi.Input[_builtins.str]]
    monitoring_percentage_completion: NotRequired[pulumi.Input[_builtins.int]]
    primary_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    protected_managed_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[A2AProtectedManagedDiskDetailsArgsDict]]]
    ]
    recovery_fabric_location: NotRequired[pulumi.Input[_builtins.str]]
    rpo_in_seconds: NotRequired[pulumi.Input[_builtins.float]]
    unprotected_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[A2AUnprotectedDiskDetailsArgsDict]]]
    ]

@pulumi.input_type
class A2ASharedDiskReplicationDetailsArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        failover_recovery_point_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_rpo_calculated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        management_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_percentage_completion: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_managed_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AProtectedManagedDiskDetailsArgs]]]
        ] = ...,
        recovery_fabric_location: Optional[pulumi.Input[_builtins.str]] = ...,
        rpo_in_seconds: Optional[pulumi.Input[_builtins.float]] = ...,
        unprotected_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AUnprotectedDiskDetailsArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover_recovery_point_id.setter
    def failover_recovery_point_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_rpo_calculated_time.setter
    def last_rpo_calculated_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managementId")
    def management_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_id.setter
    def management_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_job_type.setter
    def monitoring_job_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitoring_percentage_completion.setter
    def monitoring_percentage_completion(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_fabric_location.setter
    def primary_fabric_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedManagedDisks")
    def protected_managed_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[A2AProtectedManagedDiskDetailsArgs]]]
    ]: ...
    @protected_managed_disks.setter
    def protected_managed_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AProtectedManagedDiskDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_fabric_location.setter
    def recovery_fabric_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @rpo_in_seconds.setter
    def rpo_in_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="unprotectedDisks")
    def unprotected_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[A2AUnprotectedDiskDetailsArgs]]]
    ]: ...
    @unprotected_disks.setter
    def unprotected_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[A2AUnprotectedDiskDetailsArgs]]]
        ],
    ): ...

class A2AUnprotectedDiskDetailsArgsDict(TypedDict):
    disk_auto_protection_status: NotRequired[
        pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]
    ]
    disk_lun_id: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class A2AUnprotectedDiskDetailsArgs:
    def __init__(
        __self__,
        *,
        disk_auto_protection_status: Optional[
            pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]
        ] = ...,
        disk_lun_id: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskAutoProtectionStatus")
    def disk_auto_protection_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]]: ...
    @disk_auto_protection_status.setter
    def disk_auto_protection_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AutoProtectionOfDataDisk]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskLunId")
    def disk_lun_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_lun_id.setter
    def disk_lun_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class A2AVmDiskInputDetailsArgsDict(TypedDict):
    disk_uri: pulumi.Input[_builtins.str]
    primary_staging_azure_storage_account_id: pulumi.Input[_builtins.str]
    recovery_azure_storage_account_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class A2AVmDiskInputDetailsArgs:
    def __init__(
        __self__,
        *,
        disk_uri: pulumi.Input[_builtins.str],
        primary_staging_azure_storage_account_id: pulumi.Input[_builtins.str],
        recovery_azure_storage_account_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskUri")
    def disk_uri(self) -> pulumi.Input[_builtins.str]: ...
    @disk_uri.setter
    def disk_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryStagingAzureStorageAccountId")
    def primary_staging_azure_storage_account_id(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @primary_staging_azure_storage_account_id.setter
    def primary_staging_azure_storage_account_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryAzureStorageAccountId")
    def recovery_azure_storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @recovery_azure_storage_account_id.setter
    def recovery_azure_storage_account_id(self, value: pulumi.Input[_builtins.str]): ...

class A2AVmManagedDiskInputDetailsArgsDict(TypedDict):
    disk_id: pulumi.Input[_builtins.str]
    primary_staging_azure_storage_account_id: pulumi.Input[_builtins.str]
    recovery_resource_group_id: pulumi.Input[_builtins.str]
    disk_encryption_info: NotRequired[pulumi.Input[DiskEncryptionInfoArgsDict]]
    recovery_disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_replica_disk_account_type: NotRequired[pulumi.Input[_builtins.str]]
    recovery_target_disk_account_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class A2AVmManagedDiskInputDetailsArgs:
    def __init__(
        __self__,
        *,
        disk_id: pulumi.Input[_builtins.str],
        primary_staging_azure_storage_account_id: pulumi.Input[_builtins.str],
        recovery_resource_group_id: pulumi.Input[_builtins.str],
        disk_encryption_info: Optional[pulumi.Input[DiskEncryptionInfoArgs]] = ...,
        recovery_disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_replica_disk_account_type: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_target_disk_account_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]: ...
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryStagingAzureStorageAccountId")
    def primary_staging_azure_storage_account_id(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @primary_staging_azure_storage_account_id.setter
    def primary_staging_azure_storage_account_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryResourceGroupId")
    def recovery_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @recovery_resource_group_id.setter
    def recovery_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionInfo")
    def disk_encryption_info(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionInfoArgs]]: ...
    @disk_encryption_info.setter
    def disk_encryption_info(
        self, value: Optional[pulumi.Input[DiskEncryptionInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryDiskEncryptionSetId")
    def recovery_disk_encryption_set_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_disk_encryption_set_id.setter
    def recovery_disk_encryption_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryReplicaDiskAccountType")
    def recovery_replica_disk_account_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_replica_disk_account_type.setter
    def recovery_replica_disk_account_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryTargetDiskAccountType")
    def recovery_target_disk_account_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_target_disk_account_type.setter
    def recovery_target_disk_account_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AADPropertiesDict(TypedDict):
    audience: NotRequired[_builtins.str]
    authority: NotRequired[_builtins.str]
    service_principal_client_id: NotRequired[_builtins.str]
    service_principal_object_id: NotRequired[_builtins.str]
    tenant_id: NotRequired[_builtins.str]

@pulumi.input_type
class AADProperties:
    def __init__(
        __self__,
        *,
        audience: Optional[_builtins.str] = ...,
        authority: Optional[_builtins.str] = ...,
        service_principal_client_id: Optional[_builtins.str] = ...,
        service_principal_object_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]: ...
    @audience.setter
    def audience(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]: ...
    @authority.setter
    def authority(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalClientId")
    def service_principal_client_id(self) -> Optional[_builtins.str]: ...
    @service_principal_client_id.setter
    def service_principal_client_id(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalObjectId")
    def service_principal_object_id(self) -> Optional[_builtins.str]: ...
    @service_principal_object_id.setter
    def service_principal_object_id(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[_builtins.str]): ...

class AddRecoveryServicesProviderInputPropertiesArgsDict(TypedDict):
    authentication_identity_input: pulumi.Input[IdentityProviderInputArgsDict]
    machine_name: pulumi.Input[_builtins.str]
    resource_access_identity_input: pulumi.Input[IdentityProviderInputArgsDict]
    bios_id: NotRequired[pulumi.Input[_builtins.str]]
    data_plane_authentication_identity_input: NotRequired[
        pulumi.Input[IdentityProviderInputArgsDict]
    ]
    machine_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AddRecoveryServicesProviderInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_identity_input: pulumi.Input[IdentityProviderInputArgs],
        machine_name: pulumi.Input[_builtins.str],
        resource_access_identity_input: pulumi.Input[IdentityProviderInputArgs],
        bios_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_plane_authentication_identity_input: Optional[
            pulumi.Input[IdentityProviderInputArgs]
        ] = ...,
        machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationIdentityInput")
    def authentication_identity_input(
        self,
    ) -> pulumi.Input[IdentityProviderInputArgs]: ...
    @authentication_identity_input.setter
    def authentication_identity_input(
        self, value: pulumi.Input[IdentityProviderInputArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[_builtins.str]: ...
    @machine_name.setter
    def machine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentityInput")
    def resource_access_identity_input(
        self,
    ) -> pulumi.Input[IdentityProviderInputArgs]: ...
    @resource_access_identity_input.setter
    def resource_access_identity_input(
        self, value: pulumi.Input[IdentityProviderInputArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bios_id.setter
    def bios_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneAuthenticationIdentityInput")
    def data_plane_authentication_identity_input(
        self,
    ) -> Optional[pulumi.Input[IdentityProviderInputArgs]]: ...
    @data_plane_authentication_identity_input.setter
    def data_plane_authentication_identity_input(
        self, value: Optional[pulumi.Input[IdentityProviderInputArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_id.setter
    def machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AddVCenterRequestPropertiesArgsDict(TypedDict):
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    process_server_id: NotRequired[pulumi.Input[_builtins.str]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AddVCenterRequestPropertiesArgs:
    def __init__(
        __self__,
        *,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        process_server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @process_server_id.setter
    def process_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureBackupServerContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    can_re_register: NotRequired[pulumi.Input[_builtins.bool]]
    container_id: NotRequired[pulumi.Input[_builtins.str]]
    dpm_agent_version: NotRequired[pulumi.Input[_builtins.str]]
    dpm_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    extended_info: NotRequired[pulumi.Input[DPMContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_count: NotRequired[pulumi.Input[_builtins.float]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    upgrade_available: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AzureBackupServerContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        can_re_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dpm_agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dpm_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        extended_info: Optional[pulumi.Input[DPMContainerExtendedInfoArgs]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_count: Optional[pulumi.Input[_builtins.float]] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_available: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_re_register.setter
    def can_re_register(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dpmAgentVersion")
    def dpm_agent_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dpm_agent_version.setter
    def dpm_agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dpmServers")
    def dpm_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dpm_servers.setter
    def dpm_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[pulumi.Input[DPMContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[DPMContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @protected_item_count.setter
    def protected_item_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @upgrade_available.setter
    def upgrade_available(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AzureFabricCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFabricCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureFileShareProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    retention_policy: NotRequired[
        pulumi.Input[
            Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
        ]
    ]
    schedule_policy: NotRequired[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgsDict,
                LongTermSchedulePolicyArgsDict,
                SimpleSchedulePolicyArgsDict,
                SimpleSchedulePolicyV2ArgsDict,
            ]
        ]
    ]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    vault_retention_policy: NotRequired[pulumi.Input[VaultRetentionPolicyArgsDict]]
    work_load_type: NotRequired[pulumi.Input[Union[_builtins.str, WorkloadType]]]

@pulumi.input_type
class AzureFileShareProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        retention_policy: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ] = ...,
        schedule_policy: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_retention_policy: Optional[pulumi.Input[VaultRetentionPolicyArgs]] = ...,
        work_load_type: Optional[
            pulumi.Input[Union[_builtins.str, WorkloadType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
    ]: ...
    @retention_policy.setter
    def retention_policy(
        self,
        value: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgs,
                LongTermSchedulePolicyArgs,
                SimpleSchedulePolicyArgs,
                SimpleSchedulePolicyV2Args,
            ]
        ]
    ]: ...
    @schedule_policy.setter
    def schedule_policy(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vaultRetentionPolicy")
    def vault_retention_policy(
        self,
    ) -> Optional[pulumi.Input[VaultRetentionPolicyArgs]]: ...
    @vault_retention_policy.setter
    def vault_retention_policy(
        self, value: Optional[pulumi.Input[VaultRetentionPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workLoadType")
    def work_load_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]: ...
    @work_load_type.setter
    def work_load_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]
    ): ...

class AzureFileshareProtectedItemExtendedInfoArgsDict(TypedDict):
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_state: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureFileshareProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_state: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureFileshareProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureFileshareProtectedItemExtendedInfoArgsDict]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFileshareProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureFileshareProtectedItemExtendedInfoArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureFileshareProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureFileshareProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSClassicComputeVMContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSClassicComputeVMContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_version.setter
    def virtual_machine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSClassicComputeVMProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgsDict]
    ]
    extended_properties: NotRequired[pulumi.Input[ExtendedPropertiesArgsDict]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSClassicComputeVMProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]
        ] = ...,
        extended_properties: Optional[pulumi.Input[ExtendedPropertiesArgs]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[ExtendedPropertiesArgs]]: ...
    @extended_properties.setter
    def extended_properties(
        self, value: Optional[pulumi.Input[ExtendedPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSComputeVMContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSComputeVMContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_version.setter
    def virtual_machine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSComputeVMProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgsDict]
    ]
    extended_properties: NotRequired[pulumi.Input[ExtendedPropertiesArgsDict]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSComputeVMProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]
        ] = ...,
        extended_properties: Optional[pulumi.Input[ExtendedPropertiesArgs]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[ExtendedPropertiesArgs]]: ...
    @extended_properties.setter
    def extended_properties(
        self, value: Optional[pulumi.Input[ExtendedPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSVMProtectedItemExtendedInfoArgsDict(TypedDict):
    newest_recovery_point_in_archive: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point_in_archive: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point_in_vault: NotRequired[pulumi.Input[_builtins.str]]
    policy_inconsistent: NotRequired[pulumi.Input[_builtins.bool]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureIaaSVMProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        newest_recovery_point_in_archive: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point_in_archive: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point_in_vault: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_inconsistent: Optional[pulumi.Input[_builtins.bool]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newestRecoveryPointInArchive")
    def newest_recovery_point_in_archive(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @newest_recovery_point_in_archive.setter
    def newest_recovery_point_in_archive(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInArchive")
    def oldest_recovery_point_in_archive(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point_in_archive.setter
    def oldest_recovery_point_in_archive(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInVault")
    def oldest_recovery_point_in_vault(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point_in_vault.setter
    def oldest_recovery_point_in_vault(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyInconsistent")
    def policy_inconsistent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @policy_inconsistent.setter
    def policy_inconsistent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureIaaSVMProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgsDict]
    ]
    extended_properties: NotRequired[pulumi.Input[ExtendedPropertiesArgsDict]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSVMProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]
        ] = ...,
        extended_properties: Optional[pulumi.Input[ExtendedPropertiesArgs]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureIaaSVMProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[ExtendedPropertiesArgs]]: ...
    @extended_properties.setter
    def extended_properties(
        self, value: Optional[pulumi.Input[ExtendedPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureIaaSVMProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    instant_rp_details: NotRequired[pulumi.Input[InstantRPAdditionalDetailsArgsDict]]
    instant_rp_retention_range_in_days: NotRequired[pulumi.Input[_builtins.int]]
    policy_type: NotRequired[pulumi.Input[Union[_builtins.str, IAASVMPolicyType]]]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    retention_policy: NotRequired[
        pulumi.Input[
            Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
        ]
    ]
    schedule_policy: NotRequired[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgsDict,
                LongTermSchedulePolicyArgsDict,
                SimpleSchedulePolicyArgsDict,
                SimpleSchedulePolicyV2ArgsDict,
            ]
        ]
    ]
    snapshot_consistency_type: NotRequired[
        pulumi.Input[Union[_builtins.str, IaasVMSnapshotConsistencyType]]
    ]
    tiering_policy: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgsDict]]]
    ]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureIaaSVMProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        instant_rp_details: Optional[
            pulumi.Input[InstantRPAdditionalDetailsArgs]
        ] = ...,
        instant_rp_retention_range_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_type: Optional[
            pulumi.Input[Union[_builtins.str, IAASVMPolicyType]]
        ] = ...,
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        retention_policy: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ] = ...,
        schedule_policy: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ] = ...,
        snapshot_consistency_type: Optional[
            pulumi.Input[Union[_builtins.str, IaasVMSnapshotConsistencyType]]
        ] = ...,
        tiering_policy: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]
        ] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(
        self,
    ) -> Optional[pulumi.Input[InstantRPAdditionalDetailsArgs]]: ...
    @instant_rp_details.setter
    def instant_rp_details(
        self, value: Optional[pulumi.Input[InstantRPAdditionalDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instant_rp_retention_range_in_days.setter
    def instant_rp_retention_range_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IAASVMPolicyType]]]: ...
    @policy_type.setter
    def policy_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IAASVMPolicyType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
    ]: ...
    @retention_policy.setter
    def retention_policy(
        self,
        value: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgs,
                LongTermSchedulePolicyArgs,
                SimpleSchedulePolicyArgs,
                SimpleSchedulePolicyV2Args,
            ]
        ]
    ]: ...
    @schedule_policy.setter
    def schedule_policy(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotConsistencyType")
    def snapshot_consistency_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, IaasVMSnapshotConsistencyType]]
    ]: ...
    @snapshot_consistency_type.setter
    def snapshot_consistency_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, IaasVMSnapshotConsistencyType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]]: ...
    @tiering_policy.setter
    def tiering_policy(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureMonitorAlertSettingsArgsDict(TypedDict):
    alerts_for_all_failover_issues: NotRequired[
        pulumi.Input[Union[_builtins.str, AlertsState]]
    ]
    alerts_for_all_job_failures: NotRequired[
        pulumi.Input[Union[_builtins.str, AlertsState]]
    ]
    alerts_for_all_replication_issues: NotRequired[
        pulumi.Input[Union[_builtins.str, AlertsState]]
    ]

@pulumi.input_type
class AzureMonitorAlertSettingsArgs:
    def __init__(
        __self__,
        *,
        alerts_for_all_failover_issues: Optional[
            pulumi.Input[Union[_builtins.str, AlertsState]]
        ] = ...,
        alerts_for_all_job_failures: Optional[
            pulumi.Input[Union[_builtins.str, AlertsState]]
        ] = ...,
        alerts_for_all_replication_issues: Optional[
            pulumi.Input[Union[_builtins.str, AlertsState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertsForAllFailoverIssues")
    def alerts_for_all_failover_issues(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]: ...
    @alerts_for_all_failover_issues.setter
    def alerts_for_all_failover_issues(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="alertsForAllJobFailures")
    def alerts_for_all_job_failures(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]: ...
    @alerts_for_all_job_failures.setter
    def alerts_for_all_job_failures(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="alertsForAllReplicationIssues")
    def alerts_for_all_replication_issues(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]: ...
    @alerts_for_all_replication_issues.setter
    def alerts_for_all_replication_issues(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]
    ): ...

class AzureRecoveryServiceVaultProtectionIntentArgsDict(TypedDict):
    protection_intent_item_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    item_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureRecoveryServiceVaultProtectionIntentArgs:
    def __init__(
        __self__,
        *,
        protection_intent_item_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionStatus]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureResourceProtectionIntentArgsDict(TypedDict):
    protection_intent_item_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    item_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureResourceProtectionIntentArgs:
    def __init__(
        __self__,
        *,
        protection_intent_item_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionStatus]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureSQLAGWorkloadContainerProtectionContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    extended_info: NotRequired[pulumi.Input[AzureWorkloadContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_time: NotRequired[pulumi.Input[_builtins.str]]
    operation_type: NotRequired[pulumi.Input[Union[_builtins.str, OperationType]]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    workload_type: NotRequired[pulumi.Input[Union[_builtins.str, WorkloadType]]]

@pulumi.input_type
class AzureSQLAGWorkloadContainerProtectionContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        extended_info: Optional[
            pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_type: Optional[
            pulumi.Input[Union[_builtins.str, OperationType]]
        ] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_type: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperationType]]]: ...
    @operation_type.setter
    def operation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]: ...
    @workload_type.setter
    def workload_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]
    ): ...

class AzureSqlContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureSqlContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureSqlProtectedItemExtendedInfoArgsDict(TypedDict):
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_state: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureSqlProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_state: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureSqlProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[pulumi.Input[AzureSqlProtectedItemExtendedInfoArgsDict]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemState]]
    ]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureSqlProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureSqlProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureSqlProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureSqlProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataId")
    def protected_item_data_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_id.setter
    def protected_item_data_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureSqlProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    retention_policy: NotRequired[
        pulumi.Input[
            Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
        ]
    ]

@pulumi.input_type
class AzureSqlProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        retention_policy: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
    ]: ...
    @retention_policy.setter
    def retention_policy(
        self,
        value: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ],
    ): ...

class AzureStorageContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    acquire_storage_account_lock: NotRequired[
        pulumi.Input[Union[_builtins.str, AcquireStorageAccountLock]]
    ]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    operation_type: NotRequired[pulumi.Input[Union[_builtins.str, OperationType]]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_count: NotRequired[pulumi.Input[_builtins.float]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureStorageContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        acquire_storage_account_lock: Optional[
            pulumi.Input[Union[_builtins.str, AcquireStorageAccountLock]]
        ] = ...,
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_type: Optional[
            pulumi.Input[Union[_builtins.str, OperationType]]
        ] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_count: Optional[pulumi.Input[_builtins.float]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="acquireStorageAccountLock")
    def acquire_storage_account_lock(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AcquireStorageAccountLock]]]: ...
    @acquire_storage_account_lock.setter
    def acquire_storage_account_lock(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AcquireStorageAccountLock]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperationType]]]: ...
    @operation_type.setter
    def operation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @protected_item_count.setter
    def protected_item_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountVersion")
    def storage_account_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_version.setter
    def storage_account_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureToAzureCreateNetworkMappingInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    primary_network_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureToAzureCreateNetworkMappingInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        primary_network_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryNetworkId")
    def primary_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @primary_network_id.setter
    def primary_network_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureVMAppContainerProtectionContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    extended_info: NotRequired[pulumi.Input[AzureWorkloadContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_time: NotRequired[pulumi.Input[_builtins.str]]
    operation_type: NotRequired[pulumi.Input[Union[_builtins.str, OperationType]]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    workload_type: NotRequired[pulumi.Input[Union[_builtins.str, WorkloadType]]]

@pulumi.input_type
class AzureVMAppContainerProtectionContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        extended_info: Optional[
            pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_type: Optional[
            pulumi.Input[Union[_builtins.str, OperationType]]
        ] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_type: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperationType]]]: ...
    @operation_type.setter
    def operation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]: ...
    @workload_type.setter
    def workload_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]
    ): ...

class AzureVmWorkloadProtectedItemExtendedInfoArgsDict(TypedDict):
    newest_recovery_point_in_archive: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point_in_archive: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point_in_vault: NotRequired[pulumi.Input[_builtins.str]]
    policy_state: NotRequired[pulumi.Input[_builtins.str]]
    recovery_model: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureVmWorkloadProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        newest_recovery_point_in_archive: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point_in_archive: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point_in_vault: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_state: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_model: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newestRecoveryPointInArchive")
    def newest_recovery_point_in_archive(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @newest_recovery_point_in_archive.setter
    def newest_recovery_point_in_archive(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInArchive")
    def oldest_recovery_point_in_archive(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point_in_archive.setter
    def oldest_recovery_point_in_archive(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInVault")
    def oldest_recovery_point_in_vault(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point_in_vault.setter
    def oldest_recovery_point_in_vault(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryModel")
    def recovery_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_model.setter
    def recovery_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureVmWorkloadProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgsDict]
    ]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[
        pulumi.Input[Union[_builtins.str, LastBackupStatus]]
    ]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]
    parent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_type: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_source_id: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
    ]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureVmWorkloadProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[
            pulumi.Input[Union[_builtins.str, LastBackupStatus]]
        ] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
        parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
        ] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self,
        value: Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]: ...
    @last_backup_status.setter
    def last_backup_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_type.setter
    def parent_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_source_id.setter
    def protected_item_data_source_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]]: ...
    @protected_item_health_status.setter
    def protected_item_health_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureVmWorkloadProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    make_policy_consistent: NotRequired[pulumi.Input[_builtins.bool]]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    settings: NotRequired[pulumi.Input[SettingsArgsDict]]
    sub_protection_policy: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgsDict]]]
    ]
    work_load_type: NotRequired[pulumi.Input[Union[_builtins.str, WorkloadType]]]

@pulumi.input_type
class AzureVmWorkloadProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        make_policy_consistent: Optional[pulumi.Input[_builtins.bool]] = ...,
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        settings: Optional[pulumi.Input[SettingsArgs]] = ...,
        sub_protection_policy: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]
        ] = ...,
        work_load_type: Optional[
            pulumi.Input[Union[_builtins.str, WorkloadType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="makePolicyConsistent")
    def make_policy_consistent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @make_policy_consistent.setter
    def make_policy_consistent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[SettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[SettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="subProtectionPolicy")
    def sub_protection_policy(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]]: ...
    @sub_protection_policy.setter
    def sub_protection_policy(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workLoadType")
    def work_load_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]: ...
    @work_load_type.setter
    def work_load_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]
    ): ...

class AzureVmWorkloadSAPAseDatabaseProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgsDict]
    ]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[
        pulumi.Input[Union[_builtins.str, LastBackupStatus]]
    ]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]
    parent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_type: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_source_id: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
    ]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureVmWorkloadSAPAseDatabaseProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[
            pulumi.Input[Union[_builtins.str, LastBackupStatus]]
        ] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
        parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
        ] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self,
        value: Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]: ...
    @last_backup_status.setter
    def last_backup_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_type.setter
    def parent_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_source_id.setter
    def protected_item_data_source_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]]: ...
    @protected_item_health_status.setter
    def protected_item_health_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureVmWorkloadSAPHanaDBInstanceProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgsDict]
    ]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[
        pulumi.Input[Union[_builtins.str, LastBackupStatus]]
    ]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]
    parent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_type: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_source_id: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
    ]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureVmWorkloadSAPHanaDBInstanceProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[
            pulumi.Input[Union[_builtins.str, LastBackupStatus]]
        ] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
        parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
        ] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self,
        value: Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]: ...
    @last_backup_status.setter
    def last_backup_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_type.setter
    def parent_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_source_id.setter
    def protected_item_data_source_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]]: ...
    @protected_item_health_status.setter
    def protected_item_health_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureVmWorkloadSAPHanaDatabaseProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgsDict]
    ]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[
        pulumi.Input[Union[_builtins.str, LastBackupStatus]]
    ]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]
    parent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_type: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_source_id: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
    ]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureVmWorkloadSAPHanaDatabaseProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[
            pulumi.Input[Union[_builtins.str, LastBackupStatus]]
        ] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
        parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
        ] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self,
        value: Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]: ...
    @last_backup_status.setter
    def last_backup_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_type.setter
    def parent_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_source_id.setter
    def protected_item_data_source_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]]: ...
    @protected_item_health_status.setter
    def protected_item_health_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureVmWorkloadSQLDatabaseProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgsDict]
    ]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    kpis_healths: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgsDict]]]
    ]
    last_backup_status: NotRequired[
        pulumi.Input[Union[_builtins.str, LastBackupStatus]]
    ]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]
    parent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_type: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_data_source_id: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
    ]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureVmWorkloadSQLDatabaseProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]
        ] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        kpis_healths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ] = ...,
        last_backup_status: Optional[
            pulumi.Input[Union[_builtins.str, LastBackupStatus]]
        ] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
        parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]
        ] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self,
        value: Optional[pulumi.Input[AzureVmWorkloadProtectedItemExtendedInfoArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
    ]: ...
    @kpis_healths.setter
    def kpis_healths(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[KPIResourceHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]: ...
    @last_backup_status.setter
    def last_backup_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LastBackupStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_name.setter
    def parent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_type.setter
    def parent_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_item_data_source_id.setter
    def protected_item_data_source_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]]: ...
    @protected_item_health_status.setter
    def protected_item_health_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemHealthStatus]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureWorkloadAutoProtectionIntentArgsDict(TypedDict):
    protection_intent_item_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    item_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureWorkloadAutoProtectionIntentArgs:
    def __init__(
        __self__,
        *,
        protection_intent_item_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionStatus]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureWorkloadContainerAutoProtectionIntentArgsDict(TypedDict):
    protection_intent_item_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    item_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureWorkloadContainerAutoProtectionIntentArgs:
    def __init__(
        __self__,
        *,
        protection_intent_item_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionStatus]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureWorkloadContainerExtendedInfoArgsDict(TypedDict):
    host_server_name: NotRequired[pulumi.Input[_builtins.str]]
    inquiry_info: NotRequired[pulumi.Input[InquiryInfoArgsDict]]
    nodes_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgsDict]]]
    ]

@pulumi.input_type
class AzureWorkloadContainerExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        host_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inquiry_info: Optional[pulumi.Input[InquiryInfoArgs]] = ...,
        nodes_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostServerName")
    def host_server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_server_name.setter
    def host_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inquiryInfo")
    def inquiry_info(self) -> Optional[pulumi.Input[InquiryInfoArgs]]: ...
    @inquiry_info.setter
    def inquiry_info(self, value: Optional[pulumi.Input[InquiryInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]]: ...
    @nodes_list.setter
    def nodes_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributedNodesInfoArgs]]]],
    ): ...

class AzureWorkloadContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    extended_info: NotRequired[pulumi.Input[AzureWorkloadContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_time: NotRequired[pulumi.Input[_builtins.str]]
    operation_type: NotRequired[pulumi.Input[Union[_builtins.str, OperationType]]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    workload_type: NotRequired[pulumi.Input[Union[_builtins.str, WorkloadType]]]

@pulumi.input_type
class AzureWorkloadContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        extended_info: Optional[
            pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_type: Optional[
            pulumi.Input[Union[_builtins.str, OperationType]]
        ] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_type: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[AzureWorkloadContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperationType]]]: ...
    @operation_type.setter
    def operation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]: ...
    @workload_type.setter
    def workload_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadType]]]
    ): ...

class AzureWorkloadSQLAutoProtectionIntentArgsDict(TypedDict):
    protection_intent_item_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    item_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    workload_item_type: NotRequired[
        pulumi.Input[Union[_builtins.str, WorkloadItemType]]
    ]

@pulumi.input_type
class AzureWorkloadSQLAutoProtectionIntentArgs:
    def __init__(
        __self__,
        *,
        protection_intent_item_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionStatus]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_item_type: Optional[
            pulumi.Input[Union[_builtins.str, WorkloadItemType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadItemType")
    def workload_item_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadItemType]]]: ...
    @workload_item_type.setter
    def workload_item_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadItemType]]]
    ): ...

class ClassicAlertSettingsArgsDict(TypedDict):
    alerts_for_critical_operations: NotRequired[
        pulumi.Input[Union[_builtins.str, AlertsState]]
    ]
    email_notifications_for_site_recovery: NotRequired[
        pulumi.Input[Union[_builtins.str, AlertsState]]
    ]

@pulumi.input_type
class ClassicAlertSettingsArgs:
    def __init__(
        __self__,
        *,
        alerts_for_critical_operations: Optional[
            pulumi.Input[Union[_builtins.str, AlertsState]]
        ] = ...,
        email_notifications_for_site_recovery: Optional[
            pulumi.Input[Union[_builtins.str, AlertsState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertsForCriticalOperations")
    def alerts_for_critical_operations(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]: ...
    @alerts_for_critical_operations.setter
    def alerts_for_critical_operations(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailNotificationsForSiteRecovery")
    def email_notifications_for_site_recovery(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]: ...
    @email_notifications_for_site_recovery.setter
    def email_notifications_for_site_recovery(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlertsState]]]
    ): ...

class CmkKekIdentityArgsDict(TypedDict):
    use_system_assigned_identity: NotRequired[pulumi.Input[_builtins.bool]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CmkKekIdentityArgs:
    def __init__(
        __self__,
        *,
        use_system_assigned_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
        user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_system_assigned_identity.setter
    def use_system_assigned_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CmkKeyVaultPropertiesArgsDict(TypedDict):
    key_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CmkKeyVaultPropertiesArgs:
    def __init__(
        __self__, *, key_uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_uri.setter
    def key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerIdentityInfoArgsDict(TypedDict):
    aad_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    service_principal_client_id: NotRequired[pulumi.Input[_builtins.str]]
    unique_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerIdentityInfoArgs:
    def __init__(
        __self__,
        *,
        aad_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        service_principal_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aad_tenant_id.setter
    def aad_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalClientId")
    def service_principal_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_principal_client_id.setter
    def service_principal_client_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unique_name.setter
    def unique_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CreateNetworkMappingInputPropertiesArgsDict(TypedDict):
    recovery_network_id: pulumi.Input[_builtins.str]
    fabric_specific_details: NotRequired[
        pulumi.Input[
            Union[
                AzureToAzureCreateNetworkMappingInputArgsDict,
                VmmToAzureCreateNetworkMappingInputArgsDict,
                VmmToVmmCreateNetworkMappingInputArgsDict,
            ]
        ]
    ]
    recovery_fabric_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CreateNetworkMappingInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        recovery_network_id: pulumi.Input[_builtins.str],
        fabric_specific_details: Optional[
            pulumi.Input[
                Union[
                    AzureToAzureCreateNetworkMappingInputArgs,
                    VmmToAzureCreateNetworkMappingInputArgs,
                    VmmToVmmCreateNetworkMappingInputArgs,
                ]
            ]
        ] = ...,
        recovery_fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recoveryNetworkId")
    def recovery_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @recovery_network_id.setter
    def recovery_network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fabricSpecificDetails")
    def fabric_specific_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureToAzureCreateNetworkMappingInputArgs,
                VmmToAzureCreateNetworkMappingInputArgs,
                VmmToVmmCreateNetworkMappingInputArgs,
            ]
        ]
    ]: ...
    @fabric_specific_details.setter
    def fabric_specific_details(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureToAzureCreateNetworkMappingInputArgs,
                    VmmToAzureCreateNetworkMappingInputArgs,
                    VmmToVmmCreateNetworkMappingInputArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricName")
    def recovery_fabric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_fabric_name.setter
    def recovery_fabric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CreatePolicyInputPropertiesArgsDict(TypedDict):
    provider_specific_input: NotRequired[
        pulumi.Input[
            Union[
                A2ACrossClusterMigrationPolicyCreationInputArgsDict,
                A2APolicyCreationInputArgsDict,
                HyperVReplicaAzurePolicyInputArgsDict,
                HyperVReplicaBluePolicyInputArgsDict,
                HyperVReplicaPolicyInputArgsDict,
                InMageAzureV2PolicyInputArgsDict,
                InMagePolicyInputArgsDict,
                InMageRcmFailbackPolicyCreationInputArgsDict,
                InMageRcmPolicyCreationInputArgsDict,
                VMwareCbtPolicyCreationInputArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class CreatePolicyInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        provider_specific_input: Optional[
            pulumi.Input[
                Union[
                    A2ACrossClusterMigrationPolicyCreationInputArgs,
                    A2APolicyCreationInputArgs,
                    HyperVReplicaAzurePolicyInputArgs,
                    HyperVReplicaBluePolicyInputArgs,
                    HyperVReplicaPolicyInputArgs,
                    InMageAzureV2PolicyInputArgs,
                    InMagePolicyInputArgs,
                    InMageRcmFailbackPolicyCreationInputArgs,
                    InMageRcmPolicyCreationInputArgs,
                    VMwareCbtPolicyCreationInputArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificInput")
    def provider_specific_input(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                A2ACrossClusterMigrationPolicyCreationInputArgs,
                A2APolicyCreationInputArgs,
                HyperVReplicaAzurePolicyInputArgs,
                HyperVReplicaBluePolicyInputArgs,
                HyperVReplicaPolicyInputArgs,
                InMageAzureV2PolicyInputArgs,
                InMagePolicyInputArgs,
                InMageRcmFailbackPolicyCreationInputArgs,
                InMageRcmPolicyCreationInputArgs,
                VMwareCbtPolicyCreationInputArgs,
            ]
        ]
    ]: ...
    @provider_specific_input.setter
    def provider_specific_input(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    A2ACrossClusterMigrationPolicyCreationInputArgs,
                    A2APolicyCreationInputArgs,
                    HyperVReplicaAzurePolicyInputArgs,
                    HyperVReplicaBluePolicyInputArgs,
                    HyperVReplicaPolicyInputArgs,
                    InMageAzureV2PolicyInputArgs,
                    InMagePolicyInputArgs,
                    InMageRcmFailbackPolicyCreationInputArgs,
                    InMageRcmPolicyCreationInputArgs,
                    VMwareCbtPolicyCreationInputArgs,
                ]
            ]
        ],
    ): ...

class CreateProtectionContainerMappingInputPropertiesArgsDict(TypedDict):
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    provider_specific_input: NotRequired[
        pulumi.Input[
            Union[
                A2AContainerMappingInputArgsDict, VMwareCbtContainerMappingInputArgsDict
            ]
        ]
    ]
    target_protection_container_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CreateProtectionContainerMappingInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_specific_input: Optional[
            pulumi.Input[
                Union[A2AContainerMappingInputArgs, VMwareCbtContainerMappingInputArgs]
            ]
        ] = ...,
        target_protection_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificInput")
    def provider_specific_input(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[A2AContainerMappingInputArgs, VMwareCbtContainerMappingInputArgs]
        ]
    ]: ...
    @provider_specific_input.setter
    def provider_specific_input(
        self,
        value: Optional[
            pulumi.Input[
                Union[A2AContainerMappingInputArgs, VMwareCbtContainerMappingInputArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProtectionContainerId")
    def target_protection_container_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_protection_container_id.setter
    def target_protection_container_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class CreateRecoveryPlanInputPropertiesArgsDict(TypedDict):
    groups: pulumi.Input[Sequence[pulumi.Input[RecoveryPlanGroupArgsDict]]]
    primary_fabric_id: pulumi.Input[_builtins.str]
    recovery_fabric_id: pulumi.Input[_builtins.str]
    failover_deployment_model: NotRequired[
        pulumi.Input[Union[_builtins.str, FailoverDeploymentModel]]
    ]
    provider_specific_input: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RecoveryPlanA2AInputArgsDict]]]
    ]

@pulumi.input_type
class CreateRecoveryPlanInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        groups: pulumi.Input[Sequence[pulumi.Input[RecoveryPlanGroupArgs]]],
        primary_fabric_id: pulumi.Input[_builtins.str],
        recovery_fabric_id: pulumi.Input[_builtins.str],
        failover_deployment_model: Optional[
            pulumi.Input[Union[_builtins.str, FailoverDeploymentModel]]
        ] = ...,
        provider_specific_input: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecoveryPlanA2AInputArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input[RecoveryPlanGroupArgs]]]: ...
    @groups.setter
    def groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[RecoveryPlanGroupArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryFabricId")
    def primary_fabric_id(self) -> pulumi.Input[_builtins.str]: ...
    @primary_fabric_id.setter
    def primary_fabric_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricId")
    def recovery_fabric_id(self) -> pulumi.Input[_builtins.str]: ...
    @recovery_fabric_id.setter
    def recovery_fabric_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failoverDeploymentModel")
    def failover_deployment_model(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FailoverDeploymentModel]]]: ...
    @failover_deployment_model.setter
    def failover_deployment_model(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, FailoverDeploymentModel]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificInput")
    def provider_specific_input(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanA2AInputArgs]]]]: ...
    @provider_specific_input.setter
    def provider_specific_input(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanA2AInputArgs]]]],
    ): ...

class CrossSubscriptionRestoreSettingsArgsDict(TypedDict):
    cross_subscription_restore_state: NotRequired[
        pulumi.Input[Union[_builtins.str, CrossSubscriptionRestoreState]]
    ]

@pulumi.input_type
class CrossSubscriptionRestoreSettingsArgs:
    def __init__(
        __self__,
        *,
        cross_subscription_restore_state: Optional[
            pulumi.Input[Union[_builtins.str, CrossSubscriptionRestoreState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionRestoreState")
    def cross_subscription_restore_state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, CrossSubscriptionRestoreState]]
    ]: ...
    @cross_subscription_restore_state.setter
    def cross_subscription_restore_state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, CrossSubscriptionRestoreState]]
        ],
    ): ...

class CurrentScenarioDetailsArgsDict(TypedDict):
    job_id: NotRequired[pulumi.Input[_builtins.str]]
    scenario_name: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CurrentScenarioDetailsArgs:
    def __init__(
        __self__,
        *,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scenario_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scenario_name.setter
    def scenario_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DPMContainerExtendedInfoArgsDict(TypedDict):
    last_refreshed_at: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DPMContainerExtendedInfoArgs:
    def __init__(
        __self__, *, last_refreshed_at: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_refreshed_at.setter
    def last_refreshed_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DPMProtectedItemExtendedInfoArgsDict(TypedDict):
    disk_storage_used_in_bytes: NotRequired[pulumi.Input[_builtins.str]]
    is_collocated: NotRequired[pulumi.Input[_builtins.bool]]
    is_present_on_cloud: NotRequired[pulumi.Input[_builtins.bool]]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_refreshed_at: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    on_premise_latest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    on_premise_oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    on_premise_recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]
    protectable_object_load_path: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    protected: NotRequired[pulumi.Input[_builtins.bool]]
    protection_group_name: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]
    total_disk_storage_size_in_bytes: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DPMProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        disk_storage_used_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
        is_collocated: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_present_on_cloud: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_refreshed_at: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        on_premise_latest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        on_premise_oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        on_premise_recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
        protectable_object_load_path: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        protected: Optional[pulumi.Input[_builtins.bool]] = ...,
        protection_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_disk_storage_size_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskStorageUsedInBytes")
    def disk_storage_used_in_bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_storage_used_in_bytes.setter
    def disk_storage_used_in_bytes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isCollocated")
    def is_collocated(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_collocated.setter
    def is_collocated(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isPresentOnCloud")
    def is_present_on_cloud(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_present_on_cloud.setter
    def is_present_on_cloud(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_refreshed_at.setter
    def last_refreshed_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="onPremiseLatestRecoveryPoint")
    def on_premise_latest_recovery_point(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_premise_latest_recovery_point.setter
    def on_premise_latest_recovery_point(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremiseOldestRecoveryPoint")
    def on_premise_oldest_recovery_point(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_premise_oldest_recovery_point.setter
    def on_premise_oldest_recovery_point(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremiseRecoveryPointCount")
    def on_premise_recovery_point_count(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @on_premise_recovery_point_count.setter
    def on_premise_recovery_point_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectLoadPath")
    def protectable_object_load_path(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @protectable_object_load_path.setter
    def protectable_object_load_path(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protected(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @protected.setter
    def protected(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionGroupName")
    def protection_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_group_name.setter
    def protection_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="totalDiskStorageSizeInBytes")
    def total_disk_storage_size_in_bytes(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @total_disk_storage_size_in_bytes.setter
    def total_disk_storage_size_in_bytes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DPMProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_engine_name: NotRequired[pulumi.Input[_builtins.str]]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[pulumi.Input[DPMProtectedItemExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProtectedItemState]]
    ]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DPMProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[pulumi.Input[DPMProtectedItemExtendedInfoArgs]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectedItemState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupEngineName")
    def backup_engine_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_engine_name.setter
    def backup_engine_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[DPMProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[DPMProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectedItemState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectedItemState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DailyRetentionFormatArgsDict(TypedDict):
    days_of_the_month: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayArgsDict]]]]

@pulumi.input_type
class DailyRetentionFormatArgs:
    def __init__(
        __self__,
        *,
        days_of_the_month: Optional[
            pulumi.Input[Sequence[pulumi.Input[DayArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheMonth")
    def days_of_the_month(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayArgs]]]]: ...
    @days_of_the_month.setter
    def days_of_the_month(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayArgs]]]]
    ): ...

class DailyRetentionScheduleArgsDict(TypedDict):
    retention_duration: NotRequired[pulumi.Input[RetentionDurationArgsDict]]
    retention_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DailyRetentionScheduleArgs:
    def __init__(
        __self__,
        *,
        retention_duration: Optional[pulumi.Input[RetentionDurationArgs]] = ...,
        retention_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[RetentionDurationArgs]]: ...
    @retention_duration.setter
    def retention_duration(
        self, value: Optional[pulumi.Input[RetentionDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retention_times.setter
    def retention_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DailyScheduleArgsDict(TypedDict):
    schedule_run_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DailyScheduleArgs:
    def __init__(
        __self__,
        *,
        schedule_run_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schedule_run_times.setter
    def schedule_run_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DayArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.int]]
    is_last: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DayArgs:
    def __init__(
        __self__,
        *,
        date: Optional[pulumi.Input[_builtins.int]] = ...,
        is_last: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="isLast")
    def is_last(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_last.setter
    def is_last(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DiskEncryptionInfoArgsDict(TypedDict):
    disk_encryption_key_info: NotRequired[pulumi.Input[DiskEncryptionKeyInfoArgsDict]]
    key_encryption_key_info: NotRequired[pulumi.Input[KeyEncryptionKeyInfoArgsDict]]

@pulumi.input_type
class DiskEncryptionInfoArgs:
    def __init__(
        __self__,
        *,
        disk_encryption_key_info: Optional[
            pulumi.Input[DiskEncryptionKeyInfoArgs]
        ] = ...,
        key_encryption_key_info: Optional[pulumi.Input[KeyEncryptionKeyInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKeyInfo")
    def disk_encryption_key_info(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionKeyInfoArgs]]: ...
    @disk_encryption_key_info.setter
    def disk_encryption_key_info(
        self, value: Optional[pulumi.Input[DiskEncryptionKeyInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyInfo")
    def key_encryption_key_info(
        self,
    ) -> Optional[pulumi.Input[KeyEncryptionKeyInfoArgs]]: ...
    @key_encryption_key_info.setter
    def key_encryption_key_info(
        self, value: Optional[pulumi.Input[KeyEncryptionKeyInfoArgs]]
    ): ...

class DiskEncryptionKeyInfoArgsDict(TypedDict):
    key_vault_resource_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiskEncryptionKeyInfoArgs:
    def __init__(
        __self__,
        *,
        key_vault_resource_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceArmId")
    def key_vault_resource_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_resource_arm_id.setter
    def key_vault_resource_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_identifier.setter
    def secret_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DiskExclusionPropertiesArgsDict(TypedDict):
    disk_lun_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    is_inclusion_list: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DiskExclusionPropertiesArgs:
    def __init__(
        __self__,
        *,
        disk_lun_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        is_inclusion_list: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskLunList")
    def disk_lun_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @disk_lun_list.setter
    def disk_lun_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isInclusionList")
    def is_inclusion_list(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_inclusion_list.setter
    def is_inclusion_list(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DistributedNodesInfoArgsDict(TypedDict):
    node_name: NotRequired[pulumi.Input[_builtins.str]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributedNodesInfoArgs:
    def __init__(
        __self__,
        *,
        node_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DpmContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    can_re_register: NotRequired[pulumi.Input[_builtins.bool]]
    container_id: NotRequired[pulumi.Input[_builtins.str]]
    dpm_agent_version: NotRequired[pulumi.Input[_builtins.str]]
    dpm_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    extended_info: NotRequired[pulumi.Input[DPMContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_count: NotRequired[pulumi.Input[_builtins.float]]
    protection_status: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    upgrade_available: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DpmContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        can_re_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dpm_agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dpm_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        extended_info: Optional[pulumi.Input[DPMContainerExtendedInfoArgs]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_count: Optional[pulumi.Input[_builtins.float]] = ...,
        protection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_available: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_re_register.setter
    def can_re_register(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dpmAgentVersion")
    def dpm_agent_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dpm_agent_version.setter
    def dpm_agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dpmServers")
    def dpm_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dpm_servers.setter
    def dpm_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[pulumi.Input[DPMContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[DPMContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @protected_item_count.setter
    def protected_item_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_status.setter
    def protection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @upgrade_available.setter
    def upgrade_available(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EnableMigrationInputPropertiesArgsDict(TypedDict):
    policy_id: pulumi.Input[_builtins.str]
    provider_specific_details: pulumi.Input[VMwareCbtEnableMigrationInputArgsDict]

@pulumi.input_type
class EnableMigrationInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        policy_id: pulumi.Input[_builtins.str],
        provider_specific_details: pulumi.Input[VMwareCbtEnableMigrationInputArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(
        self,
    ) -> pulumi.Input[VMwareCbtEnableMigrationInputArgs]: ...
    @provider_specific_details.setter
    def provider_specific_details(
        self, value: pulumi.Input[VMwareCbtEnableMigrationInputArgs]
    ): ...

class EnableProtectionInputPropertiesArgsDict(TypedDict):
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    protectable_item_id: NotRequired[pulumi.Input[_builtins.str]]
    provider_specific_details: NotRequired[
        pulumi.Input[
            Union[
                A2ACrossClusterMigrationEnableProtectionInputArgsDict,
                A2AEnableProtectionInputArgsDict,
                HyperVReplicaAzureEnableProtectionInputArgsDict,
                InMageAzureV2EnableProtectionInputArgsDict,
                InMageEnableProtectionInputArgsDict,
                InMageRcmEnableProtectionInputArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class EnableProtectionInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_specific_details: Optional[
            pulumi.Input[
                Union[
                    A2ACrossClusterMigrationEnableProtectionInputArgs,
                    A2AEnableProtectionInputArgs,
                    HyperVReplicaAzureEnableProtectionInputArgs,
                    InMageAzureV2EnableProtectionInputArgs,
                    InMageEnableProtectionInputArgs,
                    InMageRcmEnableProtectionInputArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableItemId")
    def protectable_item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_item_id.setter
    def protectable_item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                A2ACrossClusterMigrationEnableProtectionInputArgs,
                A2AEnableProtectionInputArgs,
                HyperVReplicaAzureEnableProtectionInputArgs,
                InMageAzureV2EnableProtectionInputArgs,
                InMageEnableProtectionInputArgs,
                InMageRcmEnableProtectionInputArgs,
            ]
        ]
    ]: ...
    @provider_specific_details.setter
    def provider_specific_details(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    A2ACrossClusterMigrationEnableProtectionInputArgs,
                    A2AEnableProtectionInputArgs,
                    HyperVReplicaAzureEnableProtectionInputArgs,
                    InMageAzureV2EnableProtectionInputArgs,
                    InMageEnableProtectionInputArgs,
                    InMageRcmEnableProtectionInputArgs,
                ]
            ]
        ],
    ): ...

class ExtendedLocationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ExtendedLocationType]]

@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ExtendedLocationType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ExtendedLocationType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ExtendedLocationType]]): ...

class ExtendedPropertiesArgsDict(TypedDict):
    disk_exclusion_properties: NotRequired[
        pulumi.Input[DiskExclusionPropertiesArgsDict]
    ]
    linux_vm_application_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExtendedPropertiesArgs:
    def __init__(
        __self__,
        *,
        disk_exclusion_properties: Optional[
            pulumi.Input[DiskExclusionPropertiesArgs]
        ] = ...,
        linux_vm_application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskExclusionProperties")
    def disk_exclusion_properties(
        self,
    ) -> Optional[pulumi.Input[DiskExclusionPropertiesArgs]]: ...
    @disk_exclusion_properties.setter
    def disk_exclusion_properties(
        self, value: Optional[pulumi.Input[DiskExclusionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxVmApplicationName")
    def linux_vm_application_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linux_vm_application_name.setter
    def linux_vm_application_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FabricCreationInputPropertiesArgsDict(TypedDict):
    custom_details: NotRequired[
        pulumi.Input[
            Union[
                AzureFabricCreationInputArgsDict,
                InMageRcmFabricCreationInputArgsDict,
                VMwareV2FabricCreationInputArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class FabricCreationInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        custom_details: Optional[
            pulumi.Input[
                Union[
                    AzureFabricCreationInputArgs,
                    InMageRcmFabricCreationInputArgs,
                    VMwareV2FabricCreationInputArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureFabricCreationInputArgs,
                InMageRcmFabricCreationInputArgs,
                VMwareV2FabricCreationInputArgs,
            ]
        ]
    ]: ...
    @custom_details.setter
    def custom_details(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureFabricCreationInputArgs,
                    InMageRcmFabricCreationInputArgs,
                    VMwareV2FabricCreationInputArgs,
                ]
            ]
        ],
    ): ...

class GenericContainerExtendedInfoArgsDict(TypedDict):
    container_identity_info: NotRequired[pulumi.Input[ContainerIdentityInfoArgsDict]]
    raw_cert_data: NotRequired[pulumi.Input[_builtins.str]]
    service_endpoints: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class GenericContainerExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        container_identity_info: Optional[
            pulumi.Input[ContainerIdentityInfoArgs]
        ] = ...,
        raw_cert_data: Optional[pulumi.Input[_builtins.str]] = ...,
        service_endpoints: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerIdentityInfo")
    def container_identity_info(
        self,
    ) -> Optional[pulumi.Input[ContainerIdentityInfoArgs]]: ...
    @container_identity_info.setter
    def container_identity_info(
        self, value: Optional[pulumi.Input[ContainerIdentityInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rawCertData")
    def raw_cert_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @raw_cert_data.setter
    def raw_cert_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @service_endpoints.setter
    def service_endpoints(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class GenericContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    extended_information: NotRequired[
        pulumi.Input[GenericContainerExtendedInfoArgsDict]
    ]
    fabric_name: NotRequired[pulumi.Input[_builtins.str]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GenericContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        extended_information: Optional[
            pulumi.Input[GenericContainerExtendedInfoArgs]
        ] = ...,
        fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInformation")
    def extended_information(
        self,
    ) -> Optional[pulumi.Input[GenericContainerExtendedInfoArgs]]: ...
    @extended_information.setter
    def extended_information(
        self, value: Optional[pulumi.Input[GenericContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fabric_name.setter
    def fabric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GenericProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    fabric_name: NotRequired[pulumi.Input[_builtins.str]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    policy_state: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_id: NotRequired[pulumi.Input[_builtins.float]]
    protection_state: NotRequired[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_associations: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GenericProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_state: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_id: Optional[pulumi.Input[_builtins.float]] = ...,
        protection_state: Optional[
            pulumi.Input[Union[_builtins.str, ProtectionState]]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_associations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fabric_name.setter
    def fabric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemId")
    def protected_item_id(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @protected_item_id.setter
    def protected_item_id(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]: ...
    @protection_state.setter
    def protection_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProtectionState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceAssociations")
    def source_associations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @source_associations.setter
    def source_associations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GenericProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    fabric_name: NotRequired[pulumi.Input[_builtins.str]]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    sub_protection_policy: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgsDict]]]
    ]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GenericProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        sub_protection_policy: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]
        ] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fabric_name.setter
    def fabric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subProtectionPolicy")
    def sub_protection_policy(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]]: ...
    @sub_protection_policy.setter
    def sub_protection_policy(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SubProtectionPolicyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HealthErrorArgsDict(TypedDict):
    creation_time_utc: NotRequired[pulumi.Input[_builtins.str]]
    customer_resolvability: NotRequired[
        pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
    ]
    entity_id: NotRequired[pulumi.Input[_builtins.str]]
    error_category: NotRequired[pulumi.Input[_builtins.str]]
    error_code: NotRequired[pulumi.Input[_builtins.str]]
    error_id: NotRequired[pulumi.Input[_builtins.str]]
    error_level: NotRequired[pulumi.Input[_builtins.str]]
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    error_source: NotRequired[pulumi.Input[_builtins.str]]
    error_type: NotRequired[pulumi.Input[_builtins.str]]
    inner_health_errors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InnerHealthErrorArgsDict]]]
    ]
    possible_causes: NotRequired[pulumi.Input[_builtins.str]]
    recommended_action: NotRequired[pulumi.Input[_builtins.str]]
    recovery_provider_error_message: NotRequired[pulumi.Input[_builtins.str]]
    summary_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HealthErrorArgs:
    def __init__(
        __self__,
        *,
        creation_time_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_resolvability: Optional[
            pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
        ] = ...,
        entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        error_category: Optional[pulumi.Input[_builtins.str]] = ...,
        error_code: Optional[pulumi.Input[_builtins.str]] = ...,
        error_id: Optional[pulumi.Input[_builtins.str]] = ...,
        error_level: Optional[pulumi.Input[_builtins.str]] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        error_source: Optional[pulumi.Input[_builtins.str]] = ...,
        error_type: Optional[pulumi.Input[_builtins.str]] = ...,
        inner_health_errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[InnerHealthErrorArgs]]]
        ] = ...,
        possible_causes: Optional[pulumi.Input[_builtins.str]] = ...,
        recommended_action: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_provider_error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        summary_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTimeUtc")
    def creation_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time_utc.setter
    def creation_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerResolvability")
    def customer_resolvability(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
    ]: ...
    @customer_resolvability.setter
    def customer_resolvability(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_id.setter
    def entity_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorCategory")
    def error_category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_category.setter
    def error_category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorId")
    def error_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_id.setter
    def error_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorLevel")
    def error_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_level.setter
    def error_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorSource")
    def error_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_source.setter
    def error_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_type.setter
    def error_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="innerHealthErrors")
    def inner_health_errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InnerHealthErrorArgs]]]]: ...
    @inner_health_errors.setter
    def inner_health_errors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InnerHealthErrorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @possible_causes.setter
    def possible_causes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recommended_action.setter
    def recommended_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryProviderErrorMessage")
    def recovery_provider_error_message(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_provider_error_message.setter
    def recovery_provider_error_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @summary_message.setter
    def summary_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HourlyScheduleArgsDict(TypedDict):
    interval: NotRequired[pulumi.Input[_builtins.int]]
    schedule_window_duration: NotRequired[pulumi.Input[_builtins.int]]
    schedule_window_start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HourlyScheduleArgs:
    def __init__(
        __self__,
        *,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_window_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule_window_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleWindowDuration")
    def schedule_window_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schedule_window_duration.setter
    def schedule_window_duration(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleWindowStartTime")
    def schedule_window_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_window_start_time.setter
    def schedule_window_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class HyperVReplicaAzureDiskInputDetailsArgsDict(TypedDict):
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    log_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    sector_size_in_bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class HyperVReplicaAzureDiskInputDetailsArgs:
    def __init__(
        __self__,
        *,
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]] = ...,
        log_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sector_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sector_size_in_bytes.setter
    def sector_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HyperVReplicaAzureEnableProtectionInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    disks_to_include: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    disks_to_include_for_managed_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HyperVReplicaAzureDiskInputDetailsArgsDict]]]
    ]
    enable_rdp_on_target_option: NotRequired[pulumi.Input[_builtins.str]]
    hv_host_vm_id: NotRequired[pulumi.Input[_builtins.str]]
    license_type: NotRequired[pulumi.Input[Union[_builtins.str, LicenseType]]]
    linux_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
    ]
    log_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[_builtins.str]]
    seed_managed_disk_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    sql_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
    ]
    target_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_network_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_v1_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_v2_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    target_managed_disk_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_nic_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_proximity_placement_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_security_profile: NotRequired[
        pulumi.Input[SecurityProfilePropertiesArgsDict]
    ]
    target_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    use_managed_disks: NotRequired[pulumi.Input[_builtins.str]]
    use_managed_disks_for_replication: NotRequired[pulumi.Input[_builtins.str]]
    user_selected_os_name: NotRequired[pulumi.Input[_builtins.str]]
    vhd_id: NotRequired[pulumi.Input[_builtins.str]]
    vm_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HyperVReplicaAzureEnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]] = ...,
        disks_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disks_to_include_for_managed_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[HyperVReplicaAzureDiskInputDetailsArgs]]]
        ] = ...,
        enable_rdp_on_target_option: Optional[pulumi.Input[_builtins.str]] = ...,
        hv_host_vm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_type: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]] = ...,
        linux_license_type: Optional[
            pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
        ] = ...,
        log_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        os_type: Optional[pulumi.Input[_builtins.str]] = ...,
        seed_managed_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sql_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
        ] = ...,
        target_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_v1_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_v2_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_managed_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_nic_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_proximity_placement_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_security_profile: Optional[
            pulumi.Input[SecurityProfilePropertiesArgs]
        ] = ...,
        target_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        use_managed_disks: Optional[pulumi.Input[_builtins.str]] = ...,
        use_managed_disks_for_replication: Optional[pulumi.Input[_builtins.str]] = ...,
        user_selected_os_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vhd_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disksToIncludeForManagedDisks")
    def disks_to_include_for_managed_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HyperVReplicaAzureDiskInputDetailsArgs]]]
    ]: ...
    @disks_to_include_for_managed_disks.setter
    def disks_to_include_for_managed_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HyperVReplicaAzureDiskInputDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRdpOnTargetOption")
    def enable_rdp_on_target_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable_rdp_on_target_option.setter
    def enable_rdp_on_target_option(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hvHostVmId")
    def hv_host_vm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hv_host_vm_id.setter
    def hv_host_vm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]: ...
    @license_type.setter
    def license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]: ...
    @linux_license_type.setter
    def linux_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @seed_managed_disk_tags.setter
    def seed_managed_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]: ...
    @sql_server_license_type.setter
    def sql_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_set_id.setter
    def target_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_zone.setter
    def target_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureNetworkId")
    def target_azure_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_network_id.setter
    def target_azure_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureSubnetId")
    def target_azure_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_subnet_id.setter
    def target_azure_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureV1ResourceGroupId")
    def target_azure_v1_resource_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_v1_resource_group_id.setter
    def target_azure_v1_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureV2ResourceGroupId")
    def target_azure_v2_resource_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_v2_resource_group_id.setter
    def target_azure_v2_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureVmName")
    def target_azure_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_vm_name.setter
    def target_azure_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_managed_disk_tags.setter
    def target_managed_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_nic_tags.setter
    def target_nic_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_proximity_placement_group_id.setter
    def target_proximity_placement_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetStorageAccountId")
    def target_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_storage_account_id.setter
    def target_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(
        self,
    ) -> Optional[pulumi.Input[SecurityProfilePropertiesArgs]]: ...
    @target_vm_security_profile.setter
    def target_vm_security_profile(
        self, value: Optional[pulumi.Input[SecurityProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_size.setter
    def target_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_vm_tags.setter
    def target_vm_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useManagedDisks")
    def use_managed_disks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @use_managed_disks.setter
    def use_managed_disks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useManagedDisksForReplication")
    def use_managed_disks_for_replication(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @use_managed_disks_for_replication.setter
    def use_managed_disks_for_replication(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userSelectedOSName")
    def user_selected_os_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_selected_os_name.setter
    def user_selected_os_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vhdId")
    def vhd_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vhd_id.setter
    def vhd_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_name.setter
    def vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HyperVReplicaAzurePolicyInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    application_consistent_snapshot_frequency_in_hours: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    online_replication_start_time: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_history_duration: NotRequired[pulumi.Input[_builtins.int]]
    replication_interval: NotRequired[pulumi.Input[_builtins.int]]
    storage_accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class HyperVReplicaAzurePolicyInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        application_consistent_snapshot_frequency_in_hours: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        online_replication_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_history_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @application_consistent_snapshot_frequency_in_hours.setter
    def application_consistent_snapshot_frequency_in_hours(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @online_replication_start_time.setter
    def online_replication_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryDuration")
    def recovery_point_history_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history_duration.setter
    def recovery_point_history_duration(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationInterval")
    def replication_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_interval.setter
    def replication_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_accounts.setter
    def storage_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HyperVReplicaBluePolicyInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    allowed_authentication_type: NotRequired[pulumi.Input[_builtins.int]]
    application_consistent_snapshot_frequency_in_hours: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    initial_replication_method: NotRequired[pulumi.Input[_builtins.str]]
    offline_replication_export_path: NotRequired[pulumi.Input[_builtins.str]]
    offline_replication_import_path: NotRequired[pulumi.Input[_builtins.str]]
    online_replication_start_time: NotRequired[pulumi.Input[_builtins.str]]
    recovery_points: NotRequired[pulumi.Input[_builtins.int]]
    replica_deletion: NotRequired[pulumi.Input[_builtins.str]]
    replication_frequency_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    replication_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class HyperVReplicaBluePolicyInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        allowed_authentication_type: Optional[pulumi.Input[_builtins.int]] = ...,
        application_consistent_snapshot_frequency_in_hours: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_replication_method: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_replication_export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_replication_import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        online_replication_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_points: Optional[pulumi.Input[_builtins.int]] = ...,
        replica_deletion: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_frequency_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationType")
    def allowed_authentication_type(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allowed_authentication_type.setter
    def allowed_authentication_type(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @application_consistent_snapshot_frequency_in_hours.setter
    def application_consistent_snapshot_frequency_in_hours(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialReplicationMethod")
    def initial_replication_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_replication_method.setter
    def initial_replication_method(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="offlineReplicationExportPath")
    def offline_replication_export_path(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_replication_export_path.setter
    def offline_replication_export_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="offlineReplicationImportPath")
    def offline_replication_import_path(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_replication_import_path.setter
    def offline_replication_import_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @online_replication_start_time.setter
    def online_replication_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPoints")
    def recovery_points(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_points.setter
    def recovery_points(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaDeletion")
    def replica_deletion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_deletion.setter
    def replica_deletion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationFrequencyInSeconds")
    def replication_frequency_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_frequency_in_seconds.setter
    def replication_frequency_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationPort")
    def replication_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_port.setter
    def replication_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HyperVReplicaPolicyInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    allowed_authentication_type: NotRequired[pulumi.Input[_builtins.int]]
    application_consistent_snapshot_frequency_in_hours: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    initial_replication_method: NotRequired[pulumi.Input[_builtins.str]]
    offline_replication_export_path: NotRequired[pulumi.Input[_builtins.str]]
    offline_replication_import_path: NotRequired[pulumi.Input[_builtins.str]]
    online_replication_start_time: NotRequired[pulumi.Input[_builtins.str]]
    recovery_points: NotRequired[pulumi.Input[_builtins.int]]
    replica_deletion: NotRequired[pulumi.Input[_builtins.str]]
    replication_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class HyperVReplicaPolicyInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        allowed_authentication_type: Optional[pulumi.Input[_builtins.int]] = ...,
        application_consistent_snapshot_frequency_in_hours: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_replication_method: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_replication_export_path: Optional[pulumi.Input[_builtins.str]] = ...,
        offline_replication_import_path: Optional[pulumi.Input[_builtins.str]] = ...,
        online_replication_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_points: Optional[pulumi.Input[_builtins.int]] = ...,
        replica_deletion: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationType")
    def allowed_authentication_type(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allowed_authentication_type.setter
    def allowed_authentication_type(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @application_consistent_snapshot_frequency_in_hours.setter
    def application_consistent_snapshot_frequency_in_hours(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialReplicationMethod")
    def initial_replication_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_replication_method.setter
    def initial_replication_method(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="offlineReplicationExportPath")
    def offline_replication_export_path(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_replication_export_path.setter
    def offline_replication_export_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="offlineReplicationImportPath")
    def offline_replication_import_path(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_replication_import_path.setter
    def offline_replication_import_path(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @online_replication_start_time.setter
    def online_replication_start_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPoints")
    def recovery_points(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_points.setter
    def recovery_points(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaDeletion")
    def replica_deletion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_deletion.setter
    def replica_deletion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationPort")
    def replication_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_port.setter
    def replication_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IaaSVMContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IaaSVMContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_version.setter
    def virtual_machine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityDataArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityDataArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ResourceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class IdentityProviderInputArgsDict(TypedDict):
    aad_authority: pulumi.Input[_builtins.str]
    application_id: pulumi.Input[_builtins.str]
    audience: pulumi.Input[_builtins.str]
    object_id: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class IdentityProviderInputArgs:
    def __init__(
        __self__,
        *,
        aad_authority: pulumi.Input[_builtins.str],
        application_id: pulumi.Input[_builtins.str],
        audience: pulumi.Input[_builtins.str],
        object_id: pulumi.Input[_builtins.str],
        tenant_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> pulumi.Input[_builtins.str]: ...
    @aad_authority.setter
    def aad_authority(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> pulumi.Input[_builtins.str]: ...
    @audience.setter
    def audience(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]: ...
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...

class ImmutabilitySettingsArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[Union[_builtins.str, ImmutabilityState]]]

@pulumi.input_type
class ImmutabilitySettingsArgs:
    def __init__(
        __self__,
        *,
        state: Optional[pulumi.Input[Union[_builtins.str, ImmutabilityState]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ImmutabilityState]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ImmutabilityState]]]
    ): ...

class InMageAzureV2DiskInputDetailsArgsDict(TypedDict):
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    log_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InMageAzureV2DiskInputDetailsArgs:
    def __init__(
        __self__,
        *,
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]] = ...,
        log_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InMageAzureV2EnableProtectionInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    disks_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InMageAzureV2DiskInputDetailsArgsDict]]]
    ]
    enable_rdp_on_target_option: NotRequired[pulumi.Input[_builtins.str]]
    license_type: NotRequired[pulumi.Input[Union[_builtins.str, LicenseType]]]
    log_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    master_target_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_vm_group_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_vm_group_name: NotRequired[pulumi.Input[_builtins.str]]
    process_server_id: NotRequired[pulumi.Input[_builtins.str]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]
    seed_managed_disk_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    sql_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
    ]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_network_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_v1_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_v2_resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_azure_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    target_managed_disk_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_nic_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_proximity_placement_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class InMageAzureV2EnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]] = ...,
        disks_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[InMageAzureV2DiskInputDetailsArgs]]]
        ] = ...,
        enable_rdp_on_target_option: Optional[pulumi.Input[_builtins.str]] = ...,
        license_type: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]] = ...,
        log_storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_vm_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_vm_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        process_server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        seed_managed_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sql_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
        ] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_v1_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_v2_resource_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_azure_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_managed_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_nic_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_proximity_placement_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InMageAzureV2DiskInputDetailsArgs]]]
    ]: ...
    @disks_to_include.setter
    def disks_to_include(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InMageAzureV2DiskInputDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRdpOnTargetOption")
    def enable_rdp_on_target_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable_rdp_on_target_option.setter
    def enable_rdp_on_target_option(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]: ...
    @license_type.setter
    def license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterTargetId")
    def master_target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_target_id.setter
    def master_target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_id.setter
    def multi_vm_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_name.setter
    def multi_vm_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @process_server_id.setter
    def process_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @seed_managed_disk_tags.setter
    def seed_managed_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]: ...
    @sql_server_license_type.setter
    def sql_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_set_id.setter
    def target_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_zone.setter
    def target_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureNetworkId")
    def target_azure_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_network_id.setter
    def target_azure_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureSubnetId")
    def target_azure_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_subnet_id.setter
    def target_azure_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureV1ResourceGroupId")
    def target_azure_v1_resource_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_v1_resource_group_id.setter
    def target_azure_v1_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureV2ResourceGroupId")
    def target_azure_v2_resource_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_v2_resource_group_id.setter
    def target_azure_v2_resource_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAzureVmName")
    def target_azure_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_azure_vm_name.setter
    def target_azure_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_managed_disk_tags.setter
    def target_managed_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_nic_tags.setter
    def target_nic_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_proximity_placement_group_id.setter
    def target_proximity_placement_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_size.setter
    def target_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_vm_tags.setter
    def target_vm_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class InMageAzureV2PolicyInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    crash_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_history: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_threshold_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMageAzureV2PolicyInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        crash_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        recovery_point_history: Optional[pulumi.Input[_builtins.int]] = ...,
        recovery_point_threshold_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]: ...
    @multi_vm_sync_status.setter
    def multi_vm_sync_status(
        self, value: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history.setter
    def recovery_point_history(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_threshold_in_minutes.setter
    def recovery_point_threshold_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InMageDiskExclusionInputArgsDict(TypedDict):
    disk_signature_options: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InMageDiskSignatureExclusionOptionsArgsDict]]
        ]
    ]
    volume_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InMageVolumeExclusionOptionsArgsDict]]]
    ]

@pulumi.input_type
class InMageDiskExclusionInputArgs:
    def __init__(
        __self__,
        *,
        disk_signature_options: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InMageDiskSignatureExclusionOptionsArgs]]
            ]
        ] = ...,
        volume_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[InMageVolumeExclusionOptionsArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSignatureOptions")
    def disk_signature_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InMageDiskSignatureExclusionOptionsArgs]]]
    ]: ...
    @disk_signature_options.setter
    def disk_signature_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InMageDiskSignatureExclusionOptionsArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeOptions")
    def volume_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InMageVolumeExclusionOptionsArgs]]]
    ]: ...
    @volume_options.setter
    def volume_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InMageVolumeExclusionOptionsArgs]]]
        ],
    ): ...

class InMageDiskSignatureExclusionOptionsArgsDict(TypedDict):
    disk_signature: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InMageDiskSignatureExclusionOptionsArgs:
    def __init__(
        __self__, *, disk_signature: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSignature")
    def disk_signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_signature.setter
    def disk_signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InMageEnableProtectionInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    master_target_id: pulumi.Input[_builtins.str]
    multi_vm_group_id: pulumi.Input[_builtins.str]
    multi_vm_group_name: pulumi.Input[_builtins.str]
    process_server_id: pulumi.Input[_builtins.str]
    retention_drive: pulumi.Input[_builtins.str]
    datastore_name: NotRequired[pulumi.Input[_builtins.str]]
    disk_exclusion_input: NotRequired[pulumi.Input[InMageDiskExclusionInputArgsDict]]
    disks_to_include: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]
    vm_friendly_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InMageEnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        master_target_id: pulumi.Input[_builtins.str],
        multi_vm_group_id: pulumi.Input[_builtins.str],
        multi_vm_group_name: pulumi.Input[_builtins.str],
        process_server_id: pulumi.Input[_builtins.str],
        retention_drive: pulumi.Input[_builtins.str],
        datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_exclusion_input: Optional[
            pulumi.Input[InMageDiskExclusionInputArgs]
        ] = ...,
        disks_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="masterTargetId")
    def master_target_id(self) -> pulumi.Input[_builtins.str]: ...
    @master_target_id.setter
    def master_target_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @multi_vm_group_id.setter
    def multi_vm_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @multi_vm_group_name.setter
    def multi_vm_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> pulumi.Input[_builtins.str]: ...
    @process_server_id.setter
    def process_server_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDrive")
    def retention_drive(self) -> pulumi.Input[_builtins.str]: ...
    @retention_drive.setter
    def retention_drive(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskExclusionInput")
    def disk_exclusion_input(
        self,
    ) -> Optional[pulumi.Input[InMageDiskExclusionInputArgs]]: ...
    @disk_exclusion_input.setter
    def disk_exclusion_input(
        self, value: Optional[pulumi.Input[InMageDiskExclusionInputArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmFriendlyName")
    def vm_friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_friendly_name.setter
    def vm_friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InMagePolicyInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_history: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_threshold_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMagePolicyInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        multi_vm_sync_status: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        recovery_point_history: Optional[pulumi.Input[_builtins.int]] = ...,
        recovery_point_threshold_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]: ...
    @multi_vm_sync_status.setter
    def multi_vm_sync_status(
        self, value: pulumi.Input[Union[_builtins.str, SetMultiVmSyncStatus]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history.setter
    def recovery_point_history(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_threshold_in_minutes.setter
    def recovery_point_threshold_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InMageRcmDiskInputArgsDict(TypedDict):
    disk_id: pulumi.Input[_builtins.str]
    disk_type: pulumi.Input[Union[_builtins.str, DiskAccountType]]
    log_storage_account_id: pulumi.Input[_builtins.str]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    sector_size_in_bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMageRcmDiskInputArgs:
    def __init__(
        __self__,
        *,
        disk_id: pulumi.Input[_builtins.str],
        disk_type: pulumi.Input[Union[_builtins.str, DiskAccountType]],
        log_storage_account_id: pulumi.Input[_builtins.str],
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sector_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]: ...
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> pulumi.Input[Union[_builtins.str, DiskAccountType]]: ...
    @disk_type.setter
    def disk_type(self, value: pulumi.Input[Union[_builtins.str, DiskAccountType]]): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sector_size_in_bytes.setter
    def sector_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InMageRcmDisksDefaultInputArgsDict(TypedDict):
    disk_type: pulumi.Input[Union[_builtins.str, DiskAccountType]]
    log_storage_account_id: pulumi.Input[_builtins.str]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    sector_size_in_bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMageRcmDisksDefaultInputArgs:
    def __init__(
        __self__,
        *,
        disk_type: pulumi.Input[Union[_builtins.str, DiskAccountType]],
        log_storage_account_id: pulumi.Input[_builtins.str],
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sector_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> pulumi.Input[Union[_builtins.str, DiskAccountType]]: ...
    @disk_type.setter
    def disk_type(self, value: pulumi.Input[Union[_builtins.str, DiskAccountType]]): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sector_size_in_bytes.setter
    def sector_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InMageRcmEnableProtectionInputArgsDict(TypedDict):
    fabric_discovery_machine_id: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    process_server_id: pulumi.Input[_builtins.str]
    target_resource_group_id: pulumi.Input[_builtins.str]
    disks_default: NotRequired[pulumi.Input[InMageRcmDisksDefaultInputArgsDict]]
    disks_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InMageRcmDiskInputArgsDict]]]
    ]
    license_type: NotRequired[pulumi.Input[Union[_builtins.str, LicenseType]]]
    linux_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
    ]
    multi_vm_group_name: NotRequired[pulumi.Input[_builtins.str]]
    run_as_account_id: NotRequired[pulumi.Input[_builtins.str]]
    seed_managed_disk_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgsDict]]]
    ]
    sql_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
    ]
    target_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    target_boot_diagnostics_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    target_managed_disk_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgsDict]]]
    ]
    target_network_id: NotRequired[pulumi.Input[_builtins.str]]
    target_nic_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgsDict]]]
    ]
    target_proximity_placement_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_security_profile: NotRequired[
        pulumi.Input[SecurityProfilePropertiesArgsDict]
    ]
    target_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgsDict]]]
    ]
    test_network_id: NotRequired[pulumi.Input[_builtins.str]]
    test_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    user_selected_os_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InMageRcmEnableProtectionInputArgs:
    def __init__(
        __self__,
        *,
        fabric_discovery_machine_id: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        process_server_id: pulumi.Input[_builtins.str],
        target_resource_group_id: pulumi.Input[_builtins.str],
        disks_default: Optional[pulumi.Input[InMageRcmDisksDefaultInputArgs]] = ...,
        disks_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[InMageRcmDiskInputArgs]]]
        ] = ...,
        license_type: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]] = ...,
        linux_license_type: Optional[
            pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
        ] = ...,
        multi_vm_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        run_as_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        seed_managed_disk_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ] = ...,
        sql_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
        ] = ...,
        target_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        target_boot_diagnostics_storage_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_managed_disk_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ] = ...,
        target_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_nic_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ] = ...,
        target_proximity_placement_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_security_profile: Optional[
            pulumi.Input[SecurityProfilePropertiesArgs]
        ] = ...,
        target_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ] = ...,
        test_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        test_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_selected_os_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_discovery_machine_id.setter
    def fabric_discovery_machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> pulumi.Input[_builtins.str]: ...
    @process_server_id.setter
    def process_server_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_resource_group_id.setter
    def target_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disksDefault")
    def disks_default(
        self,
    ) -> Optional[pulumi.Input[InMageRcmDisksDefaultInputArgs]]: ...
    @disks_default.setter
    def disks_default(
        self, value: Optional[pulumi.Input[InMageRcmDisksDefaultInputArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InMageRcmDiskInputArgs]]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InMageRcmDiskInputArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]: ...
    @license_type.setter
    def license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]: ...
    @linux_license_type.setter
    def linux_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_vm_group_name.setter
    def multi_vm_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]]: ...
    @seed_managed_disk_tags.setter
    def seed_managed_disk_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]: ...
    @sql_server_license_type.setter
    def sql_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_set_id.setter
    def target_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_zone.setter
    def target_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetBootDiagnosticsStorageAccountId")
    def target_boot_diagnostics_storage_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_boot_diagnostics_storage_account_id.setter
    def target_boot_diagnostics_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]]: ...
    @target_managed_disk_tags.setter
    def target_managed_disk_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_network_id.setter
    def target_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]]: ...
    @target_nic_tags.setter
    def target_nic_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_proximity_placement_group_id.setter
    def target_proximity_placement_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSubnetName")
    def target_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_subnet_name.setter
    def target_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_name.setter
    def target_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(
        self,
    ) -> Optional[pulumi.Input[SecurityProfilePropertiesArgs]]: ...
    @target_vm_security_profile.setter
    def target_vm_security_profile(
        self, value: Optional[pulumi.Input[SecurityProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_size.setter
    def target_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]]: ...
    @target_vm_tags.setter
    def target_vm_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserCreatedResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_network_id.setter
    def test_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testSubnetName")
    def test_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_subnet_name.setter
    def test_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSelectedOSName")
    def user_selected_os_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_selected_os_name.setter
    def user_selected_os_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InMageRcmFabricCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    physical_site_id: pulumi.Input[_builtins.str]
    source_agent_identity: pulumi.Input[IdentityProviderInputArgsDict]
    vmware_site_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class InMageRcmFabricCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        physical_site_id: pulumi.Input[_builtins.str],
        source_agent_identity: pulumi.Input[IdentityProviderInputArgs],
        vmware_site_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="physicalSiteId")
    def physical_site_id(self) -> pulumi.Input[_builtins.str]: ...
    @physical_site_id.setter
    def physical_site_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAgentIdentity")
    def source_agent_identity(self) -> pulumi.Input[IdentityProviderInputArgs]: ...
    @source_agent_identity.setter
    def source_agent_identity(self, value: pulumi.Input[IdentityProviderInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_site_id.setter
    def vmware_site_id(self, value: pulumi.Input[_builtins.str]): ...

class InMageRcmFailbackPolicyCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    crash_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMageRcmFailbackPolicyCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        crash_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InMageRcmPolicyCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    crash_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    enable_multi_vm_sync: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_history_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InMageRcmPolicyCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        crash_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        enable_multi_vm_sync: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_history_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableMultiVmSync")
    def enable_multi_vm_sync(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable_multi_vm_sync.setter
    def enable_multi_vm_sync(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history_in_minutes.setter
    def recovery_point_history_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InMageVolumeExclusionOptionsArgsDict(TypedDict):
    only_exclude_if_single_volume: NotRequired[pulumi.Input[_builtins.str]]
    volume_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InMageVolumeExclusionOptionsArgs:
    def __init__(
        __self__,
        *,
        only_exclude_if_single_volume: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onlyExcludeIfSingleVolume")
    def only_exclude_if_single_volume(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @only_exclude_if_single_volume.setter
    def only_exclude_if_single_volume(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeLabel")
    def volume_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_label.setter
    def volume_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InnerHealthErrorArgsDict(TypedDict):
    creation_time_utc: NotRequired[pulumi.Input[_builtins.str]]
    customer_resolvability: NotRequired[
        pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
    ]
    entity_id: NotRequired[pulumi.Input[_builtins.str]]
    error_category: NotRequired[pulumi.Input[_builtins.str]]
    error_code: NotRequired[pulumi.Input[_builtins.str]]
    error_id: NotRequired[pulumi.Input[_builtins.str]]
    error_level: NotRequired[pulumi.Input[_builtins.str]]
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    error_source: NotRequired[pulumi.Input[_builtins.str]]
    error_type: NotRequired[pulumi.Input[_builtins.str]]
    possible_causes: NotRequired[pulumi.Input[_builtins.str]]
    recommended_action: NotRequired[pulumi.Input[_builtins.str]]
    recovery_provider_error_message: NotRequired[pulumi.Input[_builtins.str]]
    summary_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InnerHealthErrorArgs:
    def __init__(
        __self__,
        *,
        creation_time_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_resolvability: Optional[
            pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
        ] = ...,
        entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        error_category: Optional[pulumi.Input[_builtins.str]] = ...,
        error_code: Optional[pulumi.Input[_builtins.str]] = ...,
        error_id: Optional[pulumi.Input[_builtins.str]] = ...,
        error_level: Optional[pulumi.Input[_builtins.str]] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        error_source: Optional[pulumi.Input[_builtins.str]] = ...,
        error_type: Optional[pulumi.Input[_builtins.str]] = ...,
        possible_causes: Optional[pulumi.Input[_builtins.str]] = ...,
        recommended_action: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_provider_error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        summary_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTimeUtc")
    def creation_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time_utc.setter
    def creation_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerResolvability")
    def customer_resolvability(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
    ]: ...
    @customer_resolvability.setter
    def customer_resolvability(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, HealthErrorCustomerResolvability]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_id.setter
    def entity_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorCategory")
    def error_category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_category.setter
    def error_category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorId")
    def error_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_id.setter
    def error_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorLevel")
    def error_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_level.setter
    def error_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorSource")
    def error_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_source.setter
    def error_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_type.setter
    def error_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @possible_causes.setter
    def possible_causes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recommended_action.setter
    def recommended_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryProviderErrorMessage")
    def recovery_provider_error_message(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_provider_error_message.setter
    def recovery_provider_error_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @summary_message.setter
    def summary_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InquiryInfoArgsDict(TypedDict):
    inquiry_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkloadInquiryDetailsArgsDict]]]
    ]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InquiryInfoArgs:
    def __init__(
        __self__,
        *,
        inquiry_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadInquiryDetailsArgs]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inquiryDetails")
    def inquiry_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadInquiryDetailsArgs]]]]: ...
    @inquiry_details.setter
    def inquiry_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadInquiryDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InquiryValidationArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InquiryValidationArgs:
    def __init__(
        __self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstantRPAdditionalDetailsArgsDict(TypedDict):
    azure_backup_rg_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    azure_backup_rg_name_suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstantRPAdditionalDetailsArgs:
    def __init__(
        __self__,
        *,
        azure_backup_rg_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_backup_rg_name_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNamePrefix")
    def azure_backup_rg_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_backup_rg_name_prefix.setter
    def azure_backup_rg_name_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNameSuffix")
    def azure_backup_rg_name_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_backup_rg_name_suffix.setter
    def azure_backup_rg_name_suffix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class KPIResourceHealthDetailsArgsDict(TypedDict):
    resource_health_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceHealthStatus]]
    ]

@pulumi.input_type
class KPIResourceHealthDetailsArgs:
    def __init__(
        __self__,
        *,
        resource_health_status: Optional[
            pulumi.Input[Union[_builtins.str, ResourceHealthStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceHealthStatus")
    def resource_health_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceHealthStatus]]]: ...
    @resource_health_status.setter
    def resource_health_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceHealthStatus]]]
    ): ...

class KeyEncryptionKeyInfoArgsDict(TypedDict):
    key_identifier: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_resource_arm_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyEncryptionKeyInfoArgs:
    def __init__(
        __self__,
        *,
        key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_resource_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_identifier.setter
    def key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceArmId")
    def key_vault_resource_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_resource_arm_id.setter
    def key_vault_resource_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class LogSchedulePolicyArgsDict(TypedDict):
    schedule_policy_type: pulumi.Input[_builtins.str]
    schedule_frequency_in_mins: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LogSchedulePolicyArgs:
    def __init__(
        __self__,
        *,
        schedule_policy_type: pulumi.Input[_builtins.str],
        schedule_frequency_in_mins: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_policy_type.setter
    def schedule_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequencyInMins")
    def schedule_frequency_in_mins(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schedule_frequency_in_mins.setter
    def schedule_frequency_in_mins(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class LongTermRetentionPolicyArgsDict(TypedDict):
    retention_policy_type: pulumi.Input[_builtins.str]
    daily_schedule: NotRequired[pulumi.Input[DailyRetentionScheduleArgsDict]]
    monthly_schedule: NotRequired[pulumi.Input[MonthlyRetentionScheduleArgsDict]]
    weekly_schedule: NotRequired[pulumi.Input[WeeklyRetentionScheduleArgsDict]]
    yearly_schedule: NotRequired[pulumi.Input[YearlyRetentionScheduleArgsDict]]

@pulumi.input_type
class LongTermRetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        retention_policy_type: pulumi.Input[_builtins.str],
        daily_schedule: Optional[pulumi.Input[DailyRetentionScheduleArgs]] = ...,
        monthly_schedule: Optional[pulumi.Input[MonthlyRetentionScheduleArgs]] = ...,
        weekly_schedule: Optional[pulumi.Input[WeeklyRetentionScheduleArgs]] = ...,
        yearly_schedule: Optional[pulumi.Input[YearlyRetentionScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @retention_policy_type.setter
    def retention_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input[DailyRetentionScheduleArgs]]: ...
    @daily_schedule.setter
    def daily_schedule(
        self, value: Optional[pulumi.Input[DailyRetentionScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(
        self,
    ) -> Optional[pulumi.Input[MonthlyRetentionScheduleArgs]]: ...
    @monthly_schedule.setter
    def monthly_schedule(
        self, value: Optional[pulumi.Input[MonthlyRetentionScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(
        self,
    ) -> Optional[pulumi.Input[WeeklyRetentionScheduleArgs]]: ...
    @weekly_schedule.setter
    def weekly_schedule(
        self, value: Optional[pulumi.Input[WeeklyRetentionScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="yearlySchedule")
    def yearly_schedule(
        self,
    ) -> Optional[pulumi.Input[YearlyRetentionScheduleArgs]]: ...
    @yearly_schedule.setter
    def yearly_schedule(
        self, value: Optional[pulumi.Input[YearlyRetentionScheduleArgs]]
    ): ...

class LongTermSchedulePolicyArgsDict(TypedDict):
    schedule_policy_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class LongTermSchedulePolicyArgs:
    def __init__(
        __self__, *, schedule_policy_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_policy_type.setter
    def schedule_policy_type(self, value: pulumi.Input[_builtins.str]): ...

class MABContainerHealthDetailsArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    recommendations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MABContainerHealthDetailsArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        recommendations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def recommendations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @recommendations.setter
    def recommendations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MabContainerExtendedInfoArgsDict(TypedDict):
    backup_item_type: NotRequired[pulumi.Input[Union[_builtins.str, BackupItemType]]]
    backup_items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_refreshed_at: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MabContainerExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        backup_item_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupItemType]]
        ] = ...,
        backup_items: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_refreshed_at: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupItemType")
    def backup_item_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupItemType]]]: ...
    @backup_item_type.setter
    def backup_item_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupItemType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupItems")
    def backup_items(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @backup_items.setter
    def backup_items(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_refreshed_at.setter
    def last_refreshed_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MabContainerArgsDict(TypedDict):
    container_type: pulumi.Input[_builtins.str]
    agent_version: NotRequired[pulumi.Input[_builtins.str]]
    backup_management_type: NotRequired[
        pulumi.Input[Union[_builtins.str, BackupManagementType]]
    ]
    can_re_register: NotRequired[pulumi.Input[_builtins.bool]]
    container_health_state: NotRequired[pulumi.Input[_builtins.str]]
    container_id: NotRequired[pulumi.Input[_builtins.float]]
    extended_info: NotRequired[pulumi.Input[MabContainerExtendedInfoArgsDict]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    health_status: NotRequired[pulumi.Input[_builtins.str]]
    mab_container_health_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MABContainerHealthDetailsArgsDict]]]
    ]
    protectable_object_type: NotRequired[pulumi.Input[_builtins.str]]
    protected_item_count: NotRequired[pulumi.Input[_builtins.float]]
    registration_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MabContainerArgs:
    def __init__(
        __self__,
        *,
        container_type: pulumi.Input[_builtins.str],
        agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_management_type: Optional[
            pulumi.Input[Union[_builtins.str, BackupManagementType]]
        ] = ...,
        can_re_register: Optional[pulumi.Input[_builtins.bool]] = ...,
        container_health_state: Optional[pulumi.Input[_builtins.str]] = ...,
        container_id: Optional[pulumi.Input[_builtins.float]] = ...,
        extended_info: Optional[pulumi.Input[MabContainerExtendedInfoArgs]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_status: Optional[pulumi.Input[_builtins.str]] = ...,
        mab_container_health_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[MABContainerHealthDetailsArgs]]]
        ] = ...,
        protectable_object_type: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_item_count: Optional[pulumi.Input[_builtins.float]] = ...,
        registration_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]: ...
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]: ...
    @backup_management_type.setter
    def backup_management_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupManagementType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_re_register.setter
    def can_re_register(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="containerHealthState")
    def container_health_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_health_state.setter
    def container_health_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[pulumi.Input[MabContainerExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[MabContainerExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_status.setter
    def health_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mabContainerHealthDetails")
    def mab_container_health_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MABContainerHealthDetailsArgs]]]
    ]: ...
    @mab_container_health_details.setter
    def mab_container_health_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MABContainerHealthDetailsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protectable_object_type.setter
    def protectable_object_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @protected_item_count.setter
    def protected_item_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_status.setter
    def registration_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MabFileFolderProtectedItemExtendedInfoArgsDict(TypedDict):
    last_refreshed_at: NotRequired[pulumi.Input[_builtins.str]]
    oldest_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    recovery_point_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MabFileFolderProtectedItemExtendedInfoArgs:
    def __init__(
        __self__,
        *,
        last_refreshed_at: Optional[pulumi.Input[_builtins.str]] = ...,
        oldest_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_refreshed_at.setter
    def last_refreshed_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oldest_recovery_point.setter
    def oldest_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_count.setter
    def recovery_point_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MabFileFolderProtectedItemArgsDict(TypedDict):
    protected_item_type: pulumi.Input[_builtins.str]
    backup_set_name: NotRequired[pulumi.Input[_builtins.str]]
    computer_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    create_mode: NotRequired[pulumi.Input[Union[_builtins.str, CreateMode]]]
    deferred_delete_sync_time_in_utc: NotRequired[pulumi.Input[_builtins.float]]
    deferred_delete_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    deferred_delete_time_remaining: NotRequired[pulumi.Input[_builtins.str]]
    extended_info: NotRequired[
        pulumi.Input[MabFileFolderProtectedItemExtendedInfoArgsDict]
    ]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    is_archive_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_deferred_delete_schedule_upcoming: NotRequired[pulumi.Input[_builtins.bool]]
    is_rehydrate: NotRequired[pulumi.Input[_builtins.bool]]
    is_scheduled_for_deferred_delete: NotRequired[pulumi.Input[_builtins.bool]]
    last_backup_status: NotRequired[pulumi.Input[_builtins.str]]
    last_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    last_recovery_point: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    source_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MabFileFolderProtectedItemArgs:
    def __init__(
        __self__,
        *,
        protected_item_type: pulumi.Input[_builtins.str],
        backup_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        computer_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]] = ...,
        deferred_delete_sync_time_in_utc: Optional[pulumi.Input[_builtins.float]] = ...,
        deferred_delete_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        deferred_delete_time_remaining: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_info: Optional[
            pulumi.Input[MabFileFolderProtectedItemExtendedInfoArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archive_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_deferred_delete_schedule_upcoming: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_rehydrate: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_scheduled_for_deferred_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_backup_status: Optional[pulumi.Input[_builtins.str]] = ...,
        last_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_recovery_point: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_item_type.setter
    def protected_item_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_set_name.setter
    def backup_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]: ...
    @create_mode.setter
    def create_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreateMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteSyncTimeInUTC")
    def deferred_delete_sync_time_in_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @deferred_delete_sync_time_in_utc.setter
    def deferred_delete_sync_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_in_utc.setter
    def deferred_delete_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deferred_delete_time_remaining.setter
    def deferred_delete_time_remaining(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(
        self,
    ) -> Optional[pulumi.Input[MabFileFolderProtectedItemExtendedInfoArgs]]: ...
    @extended_info.setter
    def extended_info(
        self, value: Optional[pulumi.Input[MabFileFolderProtectedItemExtendedInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archive_enabled.setter
    def is_archive_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_deferred_delete_schedule_upcoming.setter
    def is_deferred_delete_schedule_upcoming(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_rehydrate.setter
    def is_rehydrate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_scheduled_for_deferred_delete.setter
    def is_scheduled_for_deferred_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_status.setter
    def last_backup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_time.setter
    def last_backup_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_recovery_point.setter
    def last_recovery_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MabProtectionPolicyArgsDict(TypedDict):
    backup_management_type: pulumi.Input[_builtins.str]
    protected_items_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    retention_policy: NotRequired[
        pulumi.Input[
            Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
        ]
    ]
    schedule_policy: NotRequired[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgsDict,
                LongTermSchedulePolicyArgsDict,
                SimpleSchedulePolicyArgsDict,
                SimpleSchedulePolicyV2ArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class MabProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_management_type: pulumi.Input[_builtins.str],
        protected_items_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        retention_policy: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ] = ...,
        schedule_policy: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> pulumi.Input[_builtins.str]: ...
    @backup_management_type.setter
    def backup_management_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @protected_items_count.setter
    def protected_items_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
    ]: ...
    @retention_policy.setter
    def retention_policy(
        self,
        value: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgs,
                LongTermSchedulePolicyArgs,
                SimpleSchedulePolicyArgs,
                SimpleSchedulePolicyV2Args,
            ]
        ]
    ]: ...
    @schedule_policy.setter
    def schedule_policy(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ],
    ): ...

class MonitoringSettingsArgsDict(TypedDict):
    azure_monitor_alert_settings: NotRequired[
        pulumi.Input[AzureMonitorAlertSettingsArgsDict]
    ]
    classic_alert_settings: NotRequired[pulumi.Input[ClassicAlertSettingsArgsDict]]

@pulumi.input_type
class MonitoringSettingsArgs:
    def __init__(
        __self__,
        *,
        azure_monitor_alert_settings: Optional[
            pulumi.Input[AzureMonitorAlertSettingsArgs]
        ] = ...,
        classic_alert_settings: Optional[pulumi.Input[ClassicAlertSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorAlertSettings")
    def azure_monitor_alert_settings(
        self,
    ) -> Optional[pulumi.Input[AzureMonitorAlertSettingsArgs]]: ...
    @azure_monitor_alert_settings.setter
    def azure_monitor_alert_settings(
        self, value: Optional[pulumi.Input[AzureMonitorAlertSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="classicAlertSettings")
    def classic_alert_settings(
        self,
    ) -> Optional[pulumi.Input[ClassicAlertSettingsArgs]]: ...
    @classic_alert_settings.setter
    def classic_alert_settings(
        self, value: Optional[pulumi.Input[ClassicAlertSettingsArgs]]
    ): ...

class MonthlyRetentionScheduleArgsDict(TypedDict):
    retention_duration: NotRequired[pulumi.Input[RetentionDurationArgsDict]]
    retention_schedule_daily: NotRequired[pulumi.Input[DailyRetentionFormatArgsDict]]
    retention_schedule_format_type: NotRequired[
        pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]
    ]
    retention_schedule_weekly: NotRequired[pulumi.Input[WeeklyRetentionFormatArgsDict]]
    retention_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class MonthlyRetentionScheduleArgs:
    def __init__(
        __self__,
        *,
        retention_duration: Optional[pulumi.Input[RetentionDurationArgs]] = ...,
        retention_schedule_daily: Optional[
            pulumi.Input[DailyRetentionFormatArgs]
        ] = ...,
        retention_schedule_format_type: Optional[
            pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]
        ] = ...,
        retention_schedule_weekly: Optional[
            pulumi.Input[WeeklyRetentionFormatArgs]
        ] = ...,
        retention_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[RetentionDurationArgs]]: ...
    @retention_duration.setter
    def retention_duration(
        self, value: Optional[pulumi.Input[RetentionDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(
        self,
    ) -> Optional[pulumi.Input[DailyRetentionFormatArgs]]: ...
    @retention_schedule_daily.setter
    def retention_schedule_daily(
        self, value: Optional[pulumi.Input[DailyRetentionFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]]: ...
    @retention_schedule_format_type.setter
    def retention_schedule_format_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(
        self,
    ) -> Optional[pulumi.Input[WeeklyRetentionFormatArgs]]: ...
    @retention_schedule_weekly.setter
    def retention_schedule_weekly(
        self, value: Optional[pulumi.Input[WeeklyRetentionFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retention_times.setter
    def retention_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    group_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VaultSubResourceType]]]]
    ]
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ProvisioningState]]
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        group_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, VaultSubResourceType]]]
            ]
        ] = ...,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ProvisioningState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, VaultSubResourceType]]]]
    ]: ...
    @group_ids.setter
    def group_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, VaultSubResourceType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
    ): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionStatus]]
        ],
    ): ...

class RecoveryPlanA2AInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    primary_extended_location: NotRequired[pulumi.Input[ExtendedLocationArgsDict]]
    primary_zone: NotRequired[pulumi.Input[_builtins.str]]
    recovery_extended_location: NotRequired[pulumi.Input[ExtendedLocationArgsDict]]
    recovery_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecoveryPlanA2AInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        primary_extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        primary_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        recovery_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @primary_extended_location.setter
    def primary_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryZone")
    def primary_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_zone.setter
    def primary_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(
        self,
    ) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @recovery_extended_location.setter
    def recovery_extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryZone")
    def recovery_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_zone.setter
    def recovery_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecoveryPlanActionArgsDict(TypedDict):
    action_name: pulumi.Input[_builtins.str]
    custom_details: pulumi.Input[
        Union[
            RecoveryPlanAutomationRunbookActionDetailsArgsDict,
            RecoveryPlanManualActionDetailsArgsDict,
            RecoveryPlanScriptActionDetailsArgsDict,
        ]
    ]
    failover_directions: pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, PossibleOperationsDirections]]]
    ]
    failover_types: pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, ReplicationProtectedItemOperation]]]
    ]

@pulumi.input_type
class RecoveryPlanActionArgs:
    def __init__(
        __self__,
        *,
        action_name: pulumi.Input[_builtins.str],
        custom_details: pulumi.Input[
            Union[
                RecoveryPlanAutomationRunbookActionDetailsArgs,
                RecoveryPlanManualActionDetailsArgs,
                RecoveryPlanScriptActionDetailsArgs,
            ]
        ],
        failover_directions: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, PossibleOperationsDirections]]]
        ],
        failover_types: pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, ReplicationProtectedItemOperation]]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Input[_builtins.str]: ...
    @action_name.setter
    def action_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(
        self,
    ) -> pulumi.Input[
        Union[
            RecoveryPlanAutomationRunbookActionDetailsArgs,
            RecoveryPlanManualActionDetailsArgs,
            RecoveryPlanScriptActionDetailsArgs,
        ]
    ]: ...
    @custom_details.setter
    def custom_details(
        self,
        value: pulumi.Input[
            Union[
                RecoveryPlanAutomationRunbookActionDetailsArgs,
                RecoveryPlanManualActionDetailsArgs,
                RecoveryPlanScriptActionDetailsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverDirections")
    def failover_directions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, PossibleOperationsDirections]]]
    ]: ...
    @failover_directions.setter
    def failover_directions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, PossibleOperationsDirections]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverTypes")
    def failover_types(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[Union[_builtins.str, ReplicationProtectedItemOperation]]]
    ]: ...
    @failover_types.setter
    def failover_types(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, ReplicationProtectedItemOperation]]
            ]
        ],
    ): ...

class RecoveryPlanAutomationRunbookActionDetailsArgsDict(TypedDict):
    fabric_location: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]
    instance_type: pulumi.Input[_builtins.str]
    runbook_id: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecoveryPlanAutomationRunbookActionDetailsArgs:
    def __init__(
        __self__,
        *,
        fabric_location: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]],
        instance_type: pulumi.Input[_builtins.str],
        runbook_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricLocation")
    def fabric_location(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]: ...
    @fabric_location.setter
    def fabric_location(
        self, value: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="runbookId")
    def runbook_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runbook_id.setter
    def runbook_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecoveryPlanGroupArgsDict(TypedDict):
    group_type: pulumi.Input[Union[_builtins.str, RecoveryPlanGroupType]]
    end_group_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgsDict]]]
    ]
    replication_protected_items: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RecoveryPlanProtectedItemArgsDict]]]
    ]
    start_group_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgsDict]]]
    ]

@pulumi.input_type
class RecoveryPlanGroupArgs:
    def __init__(
        __self__,
        *,
        group_type: pulumi.Input[Union[_builtins.str, RecoveryPlanGroupType]],
        end_group_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]
        ] = ...,
        replication_protected_items: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecoveryPlanProtectedItemArgs]]]
        ] = ...,
        start_group_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RecoveryPlanGroupType]]: ...
    @group_type.setter
    def group_type(
        self, value: pulumi.Input[Union[_builtins.str, RecoveryPlanGroupType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endGroupActions")
    def end_group_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]]: ...
    @end_group_actions.setter
    def end_group_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationProtectedItems")
    def replication_protected_items(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecoveryPlanProtectedItemArgs]]]
    ]: ...
    @replication_protected_items.setter
    def replication_protected_items(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecoveryPlanProtectedItemArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startGroupActions")
    def start_group_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]]: ...
    @start_group_actions.setter
    def start_group_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RecoveryPlanActionArgs]]]],
    ): ...

class RecoveryPlanManualActionDetailsArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecoveryPlanManualActionDetailsArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecoveryPlanProtectedItemArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecoveryPlanProtectedItemArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecoveryPlanScriptActionDetailsArgsDict(TypedDict):
    fabric_location: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]
    instance_type: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecoveryPlanScriptActionDetailsArgs:
    def __init__(
        __self__,
        *,
        fabric_location: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]],
        instance_type: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricLocation")
    def fabric_location(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]: ...
    @fabric_location.setter
    def fabric_location(
        self, value: pulumi.Input[Union[_builtins.str, RecoveryPlanActionLocation]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RegisteredClusterNodesArgsDict(TypedDict):
    bios_id: NotRequired[pulumi.Input[_builtins.str]]
    cluster_node_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_disk_virtual_node: NotRequired[pulumi.Input[_builtins.bool]]
    machine_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RegisteredClusterNodesArgs:
    def __init__(
        __self__,
        *,
        bios_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_node_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_disk_virtual_node: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bios_id.setter
    def bios_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterNodeFqdn")
    def cluster_node_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_node_fqdn.setter
    def cluster_node_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedDiskVirtualNode")
    def is_shared_disk_virtual_node(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_disk_virtual_node.setter
    def is_shared_disk_virtual_node(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_id.setter
    def machine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReplicationProtectionClusterPropertiesArgsDict(TypedDict):
    active_location: NotRequired[pulumi.Input[_builtins.str]]
    agent_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    allowed_operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    are_all_cluster_nodes_registered: NotRequired[pulumi.Input[_builtins.bool]]
    cluster_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    cluster_node_fqdns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cluster_protected_item_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    cluster_registered_nodes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RegisteredClusterNodesArgsDict]]]
    ]
    current_scenario: NotRequired[pulumi.Input[CurrentScenarioDetailsArgsDict]]
    health_errors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HealthErrorArgsDict]]]
    ]
    last_successful_failover_time: NotRequired[pulumi.Input[_builtins.str]]
    last_successful_test_failover_time: NotRequired[pulumi.Input[_builtins.str]]
    policy_friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_fabric_friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    primary_fabric_provider: NotRequired[pulumi.Input[_builtins.str]]
    primary_protection_container_friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    protection_cluster_type: NotRequired[pulumi.Input[_builtins.str]]
    protection_state: NotRequired[pulumi.Input[_builtins.str]]
    protection_state_description: NotRequired[pulumi.Input[_builtins.str]]
    provider_specific_details: NotRequired[
        pulumi.Input[A2AReplicationProtectionClusterDetailsArgsDict]
    ]
    recovery_container_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_fabric_friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    recovery_fabric_id: NotRequired[pulumi.Input[_builtins.str]]
    recovery_protection_container_friendly_name: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    replication_health: NotRequired[pulumi.Input[_builtins.str]]
    shared_disk_properties: NotRequired[
        pulumi.Input[SharedDiskReplicationItemPropertiesArgsDict]
    ]
    test_failover_state: NotRequired[pulumi.Input[_builtins.str]]
    test_failover_state_description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReplicationProtectionClusterPropertiesArgs:
    def __init__(
        __self__,
        *,
        active_location: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_operations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        are_all_cluster_nodes_registered: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_node_fqdns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_protected_item_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cluster_registered_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegisteredClusterNodesArgs]]]
        ] = ...,
        current_scenario: Optional[pulumi.Input[CurrentScenarioDetailsArgs]] = ...,
        health_errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]
        ] = ...,
        last_successful_failover_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_successful_test_failover_time: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_fabric_friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_fabric_provider: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_protection_container_friendly_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        protection_cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state: Optional[pulumi.Input[_builtins.str]] = ...,
        protection_state_description: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_specific_details: Optional[
            pulumi.Input[A2AReplicationProtectionClusterDetailsArgs]
        ] = ...,
        recovery_container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_fabric_friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_fabric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_protection_container_friendly_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        replication_health: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_disk_properties: Optional[
            pulumi.Input[SharedDiskReplicationItemPropertiesArgs]
        ] = ...,
        test_failover_state: Optional[pulumi.Input[_builtins.str]] = ...,
        test_failover_state_description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_location.setter
    def active_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="agentClusterId")
    def agent_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_cluster_id.setter
    def agent_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_operations.setter
    def allowed_operations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="areAllClusterNodesRegistered")
    def are_all_cluster_nodes_registered(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @are_all_cluster_nodes_registered.setter
    def are_all_cluster_nodes_registered(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterFqdn")
    def cluster_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_fqdn.setter
    def cluster_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterNodeFqdns")
    def cluster_node_fqdns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_node_fqdns.setter
    def cluster_node_fqdns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterProtectedItemIds")
    def cluster_protected_item_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_protected_item_ids.setter
    def cluster_protected_item_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterRegisteredNodes")
    def cluster_registered_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegisteredClusterNodesArgs]]]]: ...
    @cluster_registered_nodes.setter
    def cluster_registered_nodes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegisteredClusterNodesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(
        self,
    ) -> Optional[pulumi.Input[CurrentScenarioDetailsArgs]]: ...
    @current_scenario.setter
    def current_scenario(
        self, value: Optional[pulumi.Input[CurrentScenarioDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]]: ...
    @health_errors.setter
    def health_errors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulFailoverTime")
    def last_successful_failover_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_successful_failover_time.setter
    def last_successful_failover_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulTestFailoverTime")
    def last_successful_test_failover_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_successful_test_failover_time.setter
    def last_successful_test_failover_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyFriendlyName")
    def policy_friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_friendly_name.setter
    def policy_friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryFabricFriendlyName")
    def primary_fabric_friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_fabric_friendly_name.setter
    def primary_fabric_friendly_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryFabricProvider")
    def primary_fabric_provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_fabric_provider.setter
    def primary_fabric_provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryProtectionContainerFriendlyName")
    def primary_protection_container_friendly_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_protection_container_friendly_name.setter
    def primary_protection_container_friendly_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionClusterType")
    def protection_cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_cluster_type.setter
    def protection_cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectionStateDescription")
    def protection_state_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_state_description.setter
    def protection_state_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(
        self,
    ) -> Optional[pulumi.Input[A2AReplicationProtectionClusterDetailsArgs]]: ...
    @provider_specific_details.setter
    def provider_specific_details(
        self, value: Optional[pulumi.Input[A2AReplicationProtectionClusterDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryContainerId")
    def recovery_container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_container_id.setter
    def recovery_container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricFriendlyName")
    def recovery_fabric_friendly_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_fabric_friendly_name.setter
    def recovery_fabric_friendly_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryFabricId")
    def recovery_fabric_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_fabric_id.setter
    def recovery_fabric_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryProtectionContainerFriendlyName")
    def recovery_protection_container_friendly_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recovery_protection_container_friendly_name.setter
    def recovery_protection_container_friendly_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_health.setter
    def replication_health(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedDiskProperties")
    def shared_disk_properties(
        self,
    ) -> Optional[pulumi.Input[SharedDiskReplicationItemPropertiesArgs]]: ...
    @shared_disk_properties.setter
    def shared_disk_properties(
        self, value: Optional[pulumi.Input[SharedDiskReplicationItemPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_failover_state.setter
    def test_failover_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testFailoverStateDescription")
    def test_failover_state_description(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_failover_state_description.setter
    def test_failover_state_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ResourceGuardOperationDetailArgsDict(TypedDict):
    default_resource_request: NotRequired[pulumi.Input[_builtins.str]]
    vault_critical_operation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceGuardOperationDetailArgs:
    def __init__(
        __self__,
        *,
        default_resource_request: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_critical_operation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceRequest")
    def default_resource_request(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_resource_request.setter
    def default_resource_request(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vaultCriticalOperation")
    def vault_critical_operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vault_critical_operation.setter
    def vault_critical_operation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ResourceGuardProxyBaseArgsDict(TypedDict):
    resource_guard_resource_id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_time: NotRequired[pulumi.Input[_builtins.str]]
    resource_guard_operation_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceGuardOperationDetailArgsDict]]]
    ]

@pulumi.input_type
class ResourceGuardProxyBaseArgs:
    def __init__(
        __self__,
        *,
        resource_guard_resource_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_guard_operation_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceGuardOperationDetailArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardResourceId")
    def resource_guard_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_guard_resource_id.setter
    def resource_guard_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationDetails")
    def resource_guard_operation_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceGuardOperationDetailArgs]]]
    ]: ...
    @resource_guard_operation_details.setter
    def resource_guard_operation_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceGuardOperationDetailArgs]]]
        ],
    ): ...

class RestoreSettingsArgsDict(TypedDict):
    cross_subscription_restore_settings: NotRequired[
        pulumi.Input[CrossSubscriptionRestoreSettingsArgsDict]
    ]

@pulumi.input_type
class RestoreSettingsArgs:
    def __init__(
        __self__,
        *,
        cross_subscription_restore_settings: Optional[
            pulumi.Input[CrossSubscriptionRestoreSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionRestoreSettings")
    def cross_subscription_restore_settings(
        self,
    ) -> Optional[pulumi.Input[CrossSubscriptionRestoreSettingsArgs]]: ...
    @cross_subscription_restore_settings.setter
    def cross_subscription_restore_settings(
        self, value: Optional[pulumi.Input[CrossSubscriptionRestoreSettingsArgs]]
    ): ...

class RetentionDurationArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    duration_type: NotRequired[
        pulumi.Input[Union[_builtins.str, RetentionDurationType]]
    ]

@pulumi.input_type
class RetentionDurationArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        duration_type: Optional[
            pulumi.Input[Union[_builtins.str, RetentionDurationType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RetentionDurationType]]]: ...
    @duration_type.setter
    def duration_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RetentionDurationType]]]
    ): ...

class SecurityProfilePropertiesArgsDict(TypedDict):
    target_vm_confidential_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
    ]
    target_vm_monitoring: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
    ]
    target_vm_secure_boot: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
    ]
    target_vm_security_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityType]]
    ]
    target_vm_tpm: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
    ]

@pulumi.input_type
class SecurityProfilePropertiesArgs:
    def __init__(
        __self__,
        *,
        target_vm_confidential_encryption: Optional[
            pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
        ] = ...,
        target_vm_monitoring: Optional[
            pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
        ] = ...,
        target_vm_secure_boot: Optional[
            pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
        ] = ...,
        target_vm_security_type: Optional[
            pulumi.Input[Union[_builtins.str, SecurityType]]
        ] = ...,
        target_vm_tpm: Optional[
            pulumi.Input[Union[_builtins.str, SecurityConfiguration]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetVmConfidentialEncryption")
    def target_vm_confidential_encryption(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]: ...
    @target_vm_confidential_encryption.setter
    def target_vm_confidential_encryption(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmMonitoring")
    def target_vm_monitoring(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]: ...
    @target_vm_monitoring.setter
    def target_vm_monitoring(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecureBoot")
    def target_vm_secure_boot(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]: ...
    @target_vm_secure_boot.setter
    def target_vm_secure_boot(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityType")
    def target_vm_security_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]: ...
    @target_vm_security_type.setter
    def target_vm_security_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmTpm")
    def target_vm_tpm(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]: ...
    @target_vm_tpm.setter
    def target_vm_tpm(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityConfiguration]]]
    ): ...

class SecuritySettingsArgsDict(TypedDict):
    immutability_settings: NotRequired[pulumi.Input[ImmutabilitySettingsArgsDict]]
    soft_delete_settings: NotRequired[pulumi.Input[SoftDeleteSettingsArgsDict]]

@pulumi.input_type
class SecuritySettingsArgs:
    def __init__(
        __self__,
        *,
        immutability_settings: Optional[pulumi.Input[ImmutabilitySettingsArgs]] = ...,
        soft_delete_settings: Optional[pulumi.Input[SoftDeleteSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="immutabilitySettings")
    def immutability_settings(
        self,
    ) -> Optional[pulumi.Input[ImmutabilitySettingsArgs]]: ...
    @immutability_settings.setter
    def immutability_settings(
        self, value: Optional[pulumi.Input[ImmutabilitySettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteSettings")
    def soft_delete_settings(
        self,
    ) -> Optional[pulumi.Input[SoftDeleteSettingsArgs]]: ...
    @soft_delete_settings.setter
    def soft_delete_settings(
        self, value: Optional[pulumi.Input[SoftDeleteSettingsArgs]]
    ): ...

class SettingsArgsDict(TypedDict):
    is_compression: NotRequired[pulumi.Input[_builtins.bool]]
    issqlcompression: NotRequired[pulumi.Input[_builtins.bool]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SettingsArgs:
    def __init__(
        __self__,
        *,
        is_compression: Optional[pulumi.Input[_builtins.bool]] = ...,
        issqlcompression: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCompression")
    def is_compression(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_compression.setter
    def is_compression(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def issqlcompression(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @issqlcompression.setter
    def issqlcompression(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SharedDiskReplicationItemPropertiesArgsDict(TypedDict):
    active_location: NotRequired[pulumi.Input[_builtins.str]]
    allowed_operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    current_scenario: NotRequired[pulumi.Input[CurrentScenarioDetailsArgsDict]]
    health_errors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HealthErrorArgsDict]]]
    ]
    protection_state: NotRequired[pulumi.Input[_builtins.str]]
    replication_health: NotRequired[pulumi.Input[_builtins.str]]
    shared_disk_provider_specific_details: NotRequired[
        pulumi.Input[A2ASharedDiskReplicationDetailsArgsDict]
    ]
    test_failover_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SharedDiskReplicationItemPropertiesArgs:
    def __init__(
        __self__,
        *,
        active_location: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_operations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        current_scenario: Optional[pulumi.Input[CurrentScenarioDetailsArgs]] = ...,
        health_errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]
        ] = ...,
        protection_state: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_health: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_disk_provider_specific_details: Optional[
            pulumi.Input[A2ASharedDiskReplicationDetailsArgs]
        ] = ...,
        test_failover_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_location.setter
    def active_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_operations.setter
    def allowed_operations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(
        self,
    ) -> Optional[pulumi.Input[CurrentScenarioDetailsArgs]]: ...
    @current_scenario.setter
    def current_scenario(
        self, value: Optional[pulumi.Input[CurrentScenarioDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]]: ...
    @health_errors.setter
    def health_errors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HealthErrorArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_health.setter
    def replication_health(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedDiskProviderSpecificDetails")
    def shared_disk_provider_specific_details(
        self,
    ) -> Optional[pulumi.Input[A2ASharedDiskReplicationDetailsArgs]]: ...
    @shared_disk_provider_specific_details.setter
    def shared_disk_provider_specific_details(
        self, value: Optional[pulumi.Input[A2ASharedDiskReplicationDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_failover_state.setter
    def test_failover_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SimpleRetentionPolicyArgsDict(TypedDict):
    retention_policy_type: pulumi.Input[_builtins.str]
    retention_duration: NotRequired[pulumi.Input[RetentionDurationArgsDict]]

@pulumi.input_type
class SimpleRetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        retention_policy_type: pulumi.Input[_builtins.str],
        retention_duration: Optional[pulumi.Input[RetentionDurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @retention_policy_type.setter
    def retention_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[RetentionDurationArgs]]: ...
    @retention_duration.setter
    def retention_duration(
        self, value: Optional[pulumi.Input[RetentionDurationArgs]]
    ): ...

class SimpleSchedulePolicyV2ArgsDict(TypedDict):
    schedule_policy_type: pulumi.Input[_builtins.str]
    daily_schedule: NotRequired[pulumi.Input[DailyScheduleArgsDict]]
    hourly_schedule: NotRequired[pulumi.Input[HourlyScheduleArgsDict]]
    schedule_run_frequency: NotRequired[
        pulumi.Input[Union[_builtins.str, ScheduleRunType]]
    ]
    weekly_schedule: NotRequired[pulumi.Input[WeeklyScheduleArgsDict]]

@pulumi.input_type
class SimpleSchedulePolicyV2Args:
    def __init__(
        __self__,
        *,
        schedule_policy_type: pulumi.Input[_builtins.str],
        daily_schedule: Optional[pulumi.Input[DailyScheduleArgs]] = ...,
        hourly_schedule: Optional[pulumi.Input[HourlyScheduleArgs]] = ...,
        schedule_run_frequency: Optional[
            pulumi.Input[Union[_builtins.str, ScheduleRunType]]
        ] = ...,
        weekly_schedule: Optional[pulumi.Input[WeeklyScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_policy_type.setter
    def schedule_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input[DailyScheduleArgs]]: ...
    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input[DailyScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input[HourlyScheduleArgs]]: ...
    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input[HourlyScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleRunType]]]: ...
    @schedule_run_frequency.setter
    def schedule_run_frequency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleRunType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input[WeeklyScheduleArgs]]: ...
    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input[WeeklyScheduleArgs]]): ...

class SimpleSchedulePolicyArgsDict(TypedDict):
    schedule_policy_type: pulumi.Input[_builtins.str]
    hourly_schedule: NotRequired[pulumi.Input[HourlyScheduleArgsDict]]
    schedule_run_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    schedule_run_frequency: NotRequired[
        pulumi.Input[Union[_builtins.str, ScheduleRunType]]
    ]
    schedule_run_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    schedule_weekly_frequency: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SimpleSchedulePolicyArgs:
    def __init__(
        __self__,
        *,
        schedule_policy_type: pulumi.Input[_builtins.str],
        hourly_schedule: Optional[pulumi.Input[HourlyScheduleArgs]] = ...,
        schedule_run_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]
        ] = ...,
        schedule_run_frequency: Optional[
            pulumi.Input[Union[_builtins.str, ScheduleRunType]]
        ] = ...,
        schedule_run_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        schedule_weekly_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_policy_type.setter
    def schedule_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input[HourlyScheduleArgs]]: ...
    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input[HourlyScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]: ...
    @schedule_run_days.setter
    def schedule_run_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleRunType]]]: ...
    @schedule_run_frequency.setter
    def schedule_run_frequency(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleRunType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schedule_run_times.setter
    def schedule_run_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleWeeklyFrequency")
    def schedule_weekly_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schedule_weekly_frequency.setter
    def schedule_weekly_frequency(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    capacity: NotRequired[pulumi.Input[_builtins.str]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, SkuName]],
        capacity: Optional[pulumi.Input[_builtins.str]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SnapshotBackupAdditionalDetailsArgsDict(TypedDict):
    instant_rp_details: NotRequired[pulumi.Input[_builtins.str]]
    instant_rp_retention_range_in_days: NotRequired[pulumi.Input[_builtins.int]]
    user_assigned_managed_identity_details: NotRequired[
        pulumi.Input[UserAssignedManagedIdentityDetailsArgsDict]
    ]

@pulumi.input_type
class SnapshotBackupAdditionalDetailsArgs:
    def __init__(
        __self__,
        *,
        instant_rp_details: Optional[pulumi.Input[_builtins.str]] = ...,
        instant_rp_retention_range_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        user_assigned_managed_identity_details: Optional[
            pulumi.Input[UserAssignedManagedIdentityDetailsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instant_rp_details.setter
    def instant_rp_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instant_rp_retention_range_in_days.setter
    def instant_rp_retention_range_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedManagedIdentityDetails")
    def user_assigned_managed_identity_details(
        self,
    ) -> Optional[pulumi.Input[UserAssignedManagedIdentityDetailsArgs]]: ...
    @user_assigned_managed_identity_details.setter
    def user_assigned_managed_identity_details(
        self, value: Optional[pulumi.Input[UserAssignedManagedIdentityDetailsArgs]]
    ): ...

class SoftDeleteSettingsArgsDict(TypedDict):
    enhanced_security_state: NotRequired[
        pulumi.Input[Union[_builtins.str, EnhancedSecurityState]]
    ]
    soft_delete_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    soft_delete_state: NotRequired[pulumi.Input[Union[_builtins.str, SoftDeleteState]]]

@pulumi.input_type
class SoftDeleteSettingsArgs:
    def __init__(
        __self__,
        *,
        enhanced_security_state: Optional[
            pulumi.Input[Union[_builtins.str, EnhancedSecurityState]]
        ] = ...,
        soft_delete_retention_period_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        soft_delete_state: Optional[
            pulumi.Input[Union[_builtins.str, SoftDeleteState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityState")
    def enhanced_security_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnhancedSecurityState]]]: ...
    @enhanced_security_state.setter
    def enhanced_security_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnhancedSecurityState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_period_in_days.setter
    def soft_delete_retention_period_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softDeleteState")
    def soft_delete_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SoftDeleteState]]]: ...
    @soft_delete_state.setter
    def soft_delete_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SoftDeleteState]]]
    ): ...

class StorageMappingInputPropertiesArgsDict(TypedDict):
    target_storage_classification_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageMappingInputPropertiesArgs:
    def __init__(
        __self__,
        *,
        target_storage_classification_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetStorageClassificationId")
    def target_storage_classification_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_storage_classification_id.setter
    def target_storage_classification_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SubProtectionPolicyArgsDict(TypedDict):
    policy_type: NotRequired[pulumi.Input[Union[_builtins.str, PolicyType]]]
    retention_policy: NotRequired[
        pulumi.Input[
            Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
        ]
    ]
    schedule_policy: NotRequired[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgsDict,
                LongTermSchedulePolicyArgsDict,
                SimpleSchedulePolicyArgsDict,
                SimpleSchedulePolicyV2ArgsDict,
            ]
        ]
    ]
    snapshot_backup_additional_details: NotRequired[
        pulumi.Input[SnapshotBackupAdditionalDetailsArgsDict]
    ]
    tiering_policy: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgsDict]]]
    ]

@pulumi.input_type
class SubProtectionPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_type: Optional[pulumi.Input[Union[_builtins.str, PolicyType]]] = ...,
        retention_policy: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ] = ...,
        schedule_policy: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ] = ...,
        snapshot_backup_additional_details: Optional[
            pulumi.Input[SnapshotBackupAdditionalDetailsArgs]
        ] = ...,
        tiering_policy: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyType]]]: ...
    @policy_type.setter
    def policy_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
    ]: ...
    @retention_policy.setter
    def retention_policy(
        self,
        value: Optional[
            pulumi.Input[Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                LogSchedulePolicyArgs,
                LongTermSchedulePolicyArgs,
                SimpleSchedulePolicyArgs,
                SimpleSchedulePolicyV2Args,
            ]
        ]
    ]: ...
    @schedule_policy.setter
    def schedule_policy(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    LogSchedulePolicyArgs,
                    LongTermSchedulePolicyArgs,
                    SimpleSchedulePolicyArgs,
                    SimpleSchedulePolicyV2Args,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotBackupAdditionalDetails")
    def snapshot_backup_additional_details(
        self,
    ) -> Optional[pulumi.Input[SnapshotBackupAdditionalDetailsArgs]]: ...
    @snapshot_backup_additional_details.setter
    def snapshot_backup_additional_details(
        self, value: Optional[pulumi.Input[SnapshotBackupAdditionalDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]]: ...
    @tiering_policy.setter
    def tiering_policy(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[TieringPolicyArgs]]]],
    ): ...

class TieringPolicyArgsDict(TypedDict):
    duration: NotRequired[pulumi.Input[_builtins.int]]
    duration_type: NotRequired[
        pulumi.Input[Union[_builtins.str, RetentionDurationType]]
    ]
    tiering_mode: NotRequired[pulumi.Input[Union[_builtins.str, TieringMode]]]

@pulumi.input_type
class TieringPolicyArgs:
    def __init__(
        __self__,
        *,
        duration: Optional[pulumi.Input[_builtins.int]] = ...,
        duration_type: Optional[
            pulumi.Input[Union[_builtins.str, RetentionDurationType]]
        ] = ...,
        tiering_mode: Optional[pulumi.Input[Union[_builtins.str, TieringMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RetentionDurationType]]]: ...
    @duration_type.setter
    def duration_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RetentionDurationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tieringMode")
    def tiering_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TieringMode]]]: ...
    @tiering_mode.setter
    def tiering_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TieringMode]]]
    ): ...

class UserAssignedIdentityPropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAssignedManagedIdentityDetailsArgsDict(TypedDict):
    identity_arm_id: NotRequired[pulumi.Input[_builtins.str]]
    identity_name: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identity_properties: NotRequired[
        pulumi.Input[UserAssignedIdentityPropertiesArgsDict]
    ]

@pulumi.input_type
class UserAssignedManagedIdentityDetailsArgs:
    def __init__(
        __self__,
        *,
        identity_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assigned_identity_properties: Optional[
            pulumi.Input[UserAssignedIdentityPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityArmId")
    def identity_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_arm_id.setter
    def identity_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_name.setter
    def identity_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityProperties")
    def user_assigned_identity_properties(
        self,
    ) -> Optional[pulumi.Input[UserAssignedIdentityPropertiesArgs]]: ...
    @user_assigned_identity_properties.setter
    def user_assigned_identity_properties(
        self, value: Optional[pulumi.Input[UserAssignedIdentityPropertiesArgs]]
    ): ...

class UserCreatedResourceTagArgsDict(TypedDict):
    tag_name: NotRequired[pulumi.Input[_builtins.str]]
    tag_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserCreatedResourceTagArgs:
    def __init__(
        __self__,
        *,
        tag_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_name.setter
    def tag_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_value.setter
    def tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareCbtContainerMappingInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    storage_account_id: pulumi.Input[_builtins.str]
    target_location: pulumi.Input[_builtins.str]
    key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    service_bus_connection_string_secret_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_sas_secret_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareCbtContainerMappingInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        storage_account_id: pulumi.Input[_builtins.str],
        target_location: pulumi.Input[_builtins.str],
        key_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_bus_connection_string_secret_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        storage_account_sas_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> pulumi.Input[_builtins.str]: ...
    @target_location.setter
    def target_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceBusConnectionStringSecretName")
    def service_bus_connection_string_secret_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_bus_connection_string_secret_name.setter
    def service_bus_connection_string_secret_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_sas_secret_name.setter
    def storage_account_sas_secret_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class VMwareCbtDiskInputArgsDict(TypedDict):
    disk_id: pulumi.Input[_builtins.str]
    is_os_disk: pulumi.Input[_builtins.str]
    log_storage_account_id: pulumi.Input[_builtins.str]
    log_storage_account_sas_secret_name: pulumi.Input[_builtins.str]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    sector_size_in_bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VMwareCbtDiskInputArgs:
    def __init__(
        __self__,
        *,
        disk_id: pulumi.Input[_builtins.str],
        is_os_disk: pulumi.Input[_builtins.str],
        log_storage_account_id: pulumi.Input[_builtins.str],
        log_storage_account_sas_secret_name: pulumi.Input[_builtins.str],
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]] = ...,
        sector_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Input[_builtins.str]: ...
    @disk_id.setter
    def disk_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isOSDisk")
    def is_os_disk(self) -> pulumi.Input[_builtins.str]: ...
    @is_os_disk.setter
    def is_os_disk(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @log_storage_account_id.setter
    def log_storage_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logStorageAccountSasSecretName")
    def log_storage_account_sas_secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_storage_account_sas_secret_name.setter
    def log_storage_account_sas_secret_name(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskAccountType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sector_size_in_bytes.setter
    def sector_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VMwareCbtEnableMigrationInputArgsDict(TypedDict):
    data_mover_run_as_account_id: pulumi.Input[_builtins.str]
    disks_to_include: pulumi.Input[Sequence[pulumi.Input[VMwareCbtDiskInputArgsDict]]]
    instance_type: pulumi.Input[_builtins.str]
    snapshot_run_as_account_id: pulumi.Input[_builtins.str]
    target_network_id: pulumi.Input[_builtins.str]
    target_resource_group_id: pulumi.Input[_builtins.str]
    vmware_machine_id: pulumi.Input[_builtins.str]
    confidential_vm_key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    license_type: NotRequired[pulumi.Input[Union[_builtins.str, LicenseType]]]
    linux_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
    ]
    perform_auto_resync: NotRequired[pulumi.Input[_builtins.str]]
    perform_sql_bulk_registration: NotRequired[pulumi.Input[_builtins.str]]
    seed_disk_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    sql_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
    ]
    target_availability_set_id: NotRequired[pulumi.Input[_builtins.str]]
    target_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    target_boot_diagnostics_storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    target_disk_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_nic_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    target_proximity_placement_group_id: NotRequired[pulumi.Input[_builtins.str]]
    target_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_security_profile: NotRequired[
        pulumi.Input[VMwareCbtSecurityProfilePropertiesArgsDict]
    ]
    target_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    test_network_id: NotRequired[pulumi.Input[_builtins.str]]
    test_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    user_selected_os_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareCbtEnableMigrationInputArgs:
    def __init__(
        __self__,
        *,
        data_mover_run_as_account_id: pulumi.Input[_builtins.str],
        disks_to_include: pulumi.Input[Sequence[pulumi.Input[VMwareCbtDiskInputArgs]]],
        instance_type: pulumi.Input[_builtins.str],
        snapshot_run_as_account_id: pulumi.Input[_builtins.str],
        target_network_id: pulumi.Input[_builtins.str],
        target_resource_group_id: pulumi.Input[_builtins.str],
        vmware_machine_id: pulumi.Input[_builtins.str],
        confidential_vm_key_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
        license_type: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]] = ...,
        linux_license_type: Optional[
            pulumi.Input[Union[_builtins.str, LinuxLicenseType]]
        ] = ...,
        perform_auto_resync: Optional[pulumi.Input[_builtins.str]] = ...,
        perform_sql_bulk_registration: Optional[pulumi.Input[_builtins.str]] = ...,
        seed_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sql_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]
        ] = ...,
        target_availability_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        target_boot_diagnostics_storage_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_disk_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_nic_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_proximity_placement_group_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_security_profile: Optional[
            pulumi.Input[VMwareCbtSecurityProfilePropertiesArgs]
        ] = ...,
        target_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        test_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        test_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_selected_os_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataMoverRunAsAccountId")
    def data_mover_run_as_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_mover_run_as_account_id.setter
    def data_mover_run_as_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VMwareCbtDiskInputArgs]]]: ...
    @disks_to_include.setter
    def disks_to_include(
        self, value: pulumi.Input[Sequence[pulumi.Input[VMwareCbtDiskInputArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotRunAsAccountId")
    def snapshot_run_as_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @snapshot_run_as_account_id.setter
    def snapshot_run_as_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_network_id.setter
    def target_network_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_resource_group_id.setter
    def target_resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareMachineId")
    def vmware_machine_id(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_machine_id.setter
    def vmware_machine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialVmKeyVaultId")
    def confidential_vm_key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_vm_key_vault_id.setter
    def confidential_vm_key_vault_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]: ...
    @license_type.setter
    def license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]: ...
    @linux_license_type.setter
    def linux_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performAutoResync")
    def perform_auto_resync(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perform_auto_resync.setter
    def perform_auto_resync(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="performSqlBulkRegistration")
    def perform_sql_bulk_registration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perform_sql_bulk_registration.setter
    def perform_sql_bulk_registration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="seedDiskTags")
    def seed_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @seed_disk_tags.setter
    def seed_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]: ...
    @sql_server_license_type.setter
    def sql_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_set_id.setter
    def target_availability_set_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_availability_zone.setter
    def target_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetBootDiagnosticsStorageAccountId")
    def target_boot_diagnostics_storage_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_boot_diagnostics_storage_account_id.setter
    def target_boot_diagnostics_storage_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDiskTags")
    def target_disk_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_disk_tags.setter
    def target_disk_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_nic_tags.setter
    def target_nic_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_proximity_placement_group_id.setter
    def target_proximity_placement_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSubnetName")
    def target_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_subnet_name.setter
    def target_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_name.setter
    def target_vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(
        self,
    ) -> Optional[pulumi.Input[VMwareCbtSecurityProfilePropertiesArgs]]: ...
    @target_vm_security_profile.setter
    def target_vm_security_profile(
        self, value: Optional[pulumi.Input[VMwareCbtSecurityProfilePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_vm_size.setter
    def target_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_vm_tags.setter
    def target_vm_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_network_id.setter
    def test_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testSubnetName")
    def test_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_subnet_name.setter
    def test_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSelectedOSName")
    def user_selected_os_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_selected_os_name.setter
    def user_selected_os_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMwareCbtPolicyCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    app_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    crash_consistent_frequency_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    recovery_point_history_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VMwareCbtPolicyCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        app_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        crash_consistent_frequency_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        recovery_point_history_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_consistent_frequency_in_minutes.setter
    def app_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @crash_consistent_frequency_in_minutes.setter
    def crash_consistent_frequency_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_point_history_in_minutes.setter
    def recovery_point_history_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class VMwareCbtSecurityProfilePropertiesArgsDict(TypedDict):
    is_target_vm_confidential_encryption_enabled: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    is_target_vm_integrity_monitoring_enabled: NotRequired[pulumi.Input[_builtins.str]]
    is_target_vm_secure_boot_enabled: NotRequired[pulumi.Input[_builtins.str]]
    is_target_vm_tpm_enabled: NotRequired[pulumi.Input[_builtins.str]]
    target_vm_security_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityType]]
    ]

@pulumi.input_type
class VMwareCbtSecurityProfilePropertiesArgs:
    def __init__(
        __self__,
        *,
        is_target_vm_confidential_encryption_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        is_target_vm_integrity_monitoring_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        is_target_vm_secure_boot_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        is_target_vm_tpm_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        target_vm_security_type: Optional[
            pulumi.Input[Union[_builtins.str, SecurityType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isTargetVmConfidentialEncryptionEnabled")
    def is_target_vm_confidential_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @is_target_vm_confidential_encryption_enabled.setter
    def is_target_vm_confidential_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isTargetVmIntegrityMonitoringEnabled")
    def is_target_vm_integrity_monitoring_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @is_target_vm_integrity_monitoring_enabled.setter
    def is_target_vm_integrity_monitoring_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isTargetVmSecureBootEnabled")
    def is_target_vm_secure_boot_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @is_target_vm_secure_boot_enabled.setter
    def is_target_vm_secure_boot_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isTargetVmTpmEnabled")
    def is_target_vm_tpm_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @is_target_vm_tpm_enabled.setter
    def is_target_vm_tpm_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityType")
    def target_vm_security_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]: ...
    @target_vm_security_type.setter
    def target_vm_security_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityType]]]
    ): ...

class VMwareV2FabricCreationInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    migration_solution_id: pulumi.Input[_builtins.str]
    physical_site_id: NotRequired[pulumi.Input[_builtins.str]]
    vmware_site_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMwareV2FabricCreationInputArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        migration_solution_id: pulumi.Input[_builtins.str],
        physical_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_site_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> pulumi.Input[_builtins.str]: ...
    @migration_solution_id.setter
    def migration_solution_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="physicalSiteId")
    def physical_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @physical_site_id.setter
    def physical_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_site_id.setter
    def vmware_site_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VaultPropertiesEncryptionArgsDict(TypedDict):
    infrastructure_encryption: NotRequired[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryptionState]]
    ]
    kek_identity: NotRequired[pulumi.Input[CmkKekIdentityArgsDict]]
    key_vault_properties: NotRequired[pulumi.Input[CmkKeyVaultPropertiesArgsDict]]

@pulumi.input_type
class VaultPropertiesEncryptionArgs:
    def __init__(
        __self__,
        *,
        infrastructure_encryption: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryptionState]]
        ] = ...,
        kek_identity: Optional[pulumi.Input[CmkKekIdentityArgs]] = ...,
        key_vault_properties: Optional[pulumi.Input[CmkKeyVaultPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, InfrastructureEncryptionState]]
    ]: ...
    @infrastructure_encryption.setter
    def infrastructure_encryption(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, InfrastructureEncryptionState]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kekIdentity")
    def kek_identity(self) -> Optional[pulumi.Input[CmkKekIdentityArgs]]: ...
    @kek_identity.setter
    def kek_identity(self, value: Optional[pulumi.Input[CmkKekIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[CmkKeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[CmkKeyVaultPropertiesArgs]]
    ): ...

class VaultPropertiesRedundancySettingsArgsDict(TypedDict):
    cross_region_restore: NotRequired[
        pulumi.Input[Union[_builtins.str, CrossRegionRestore]]
    ]
    standard_tier_storage_redundancy: NotRequired[
        pulumi.Input[Union[_builtins.str, StandardTierStorageRedundancy]]
    ]

@pulumi.input_type
class VaultPropertiesRedundancySettingsArgs:
    def __init__(
        __self__,
        *,
        cross_region_restore: Optional[
            pulumi.Input[Union[_builtins.str, CrossRegionRestore]]
        ] = ...,
        standard_tier_storage_redundancy: Optional[
            pulumi.Input[Union[_builtins.str, StandardTierStorageRedundancy]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossRegionRestore")
    def cross_region_restore(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CrossRegionRestore]]]: ...
    @cross_region_restore.setter
    def cross_region_restore(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CrossRegionRestore]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standardTierStorageRedundancy")
    def standard_tier_storage_redundancy(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, StandardTierStorageRedundancy]]
    ]: ...
    @standard_tier_storage_redundancy.setter
    def standard_tier_storage_redundancy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, StandardTierStorageRedundancy]]
        ],
    ): ...

class VaultPropertiesArgsDict(TypedDict):
    encryption: NotRequired[pulumi.Input[VaultPropertiesEncryptionArgsDict]]
    monitoring_settings: NotRequired[pulumi.Input[MonitoringSettingsArgsDict]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]
    redundancy_settings: NotRequired[
        pulumi.Input[VaultPropertiesRedundancySettingsArgsDict]
    ]
    resource_guard_operation_requests: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    restore_settings: NotRequired[pulumi.Input[RestoreSettingsArgsDict]]
    security_settings: NotRequired[pulumi.Input[SecuritySettingsArgsDict]]

@pulumi.input_type
class VaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        encryption: Optional[pulumi.Input[VaultPropertiesEncryptionArgs]] = ...,
        monitoring_settings: Optional[pulumi.Input[MonitoringSettingsArgs]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        redundancy_settings: Optional[
            pulumi.Input[VaultPropertiesRedundancySettingsArgs]
        ] = ...,
        resource_guard_operation_requests: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        restore_settings: Optional[pulumi.Input[RestoreSettingsArgs]] = ...,
        security_settings: Optional[pulumi.Input[SecuritySettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[VaultPropertiesEncryptionArgs]]: ...
    @encryption.setter
    def encryption(
        self, value: Optional[pulumi.Input[VaultPropertiesEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringSettings")
    def monitoring_settings(self) -> Optional[pulumi.Input[MonitoringSettingsArgs]]: ...
    @monitoring_settings.setter
    def monitoring_settings(
        self, value: Optional[pulumi.Input[MonitoringSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redundancySettings")
    def redundancy_settings(
        self,
    ) -> Optional[pulumi.Input[VaultPropertiesRedundancySettingsArgs]]: ...
    @redundancy_settings.setter
    def redundancy_settings(
        self, value: Optional[pulumi.Input[VaultPropertiesRedundancySettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_guard_operation_requests.setter
    def resource_guard_operation_requests(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreSettings")
    def restore_settings(self) -> Optional[pulumi.Input[RestoreSettingsArgs]]: ...
    @restore_settings.setter
    def restore_settings(self, value: Optional[pulumi.Input[RestoreSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[SecuritySettingsArgs]]: ...
    @security_settings.setter
    def security_settings(
        self, value: Optional[pulumi.Input[SecuritySettingsArgs]]
    ): ...

class VaultRetentionPolicyArgsDict(TypedDict):
    snapshot_retention_in_days: pulumi.Input[_builtins.int]
    vault_retention: pulumi.Input[
        Union[LongTermRetentionPolicyArgsDict, SimpleRetentionPolicyArgsDict]
    ]

@pulumi.input_type
class VaultRetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        snapshot_retention_in_days: pulumi.Input[_builtins.int],
        vault_retention: pulumi.Input[
            Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionInDays")
    def snapshot_retention_in_days(self) -> pulumi.Input[_builtins.int]: ...
    @snapshot_retention_in_days.setter
    def snapshot_retention_in_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="vaultRetention")
    def vault_retention(
        self,
    ) -> pulumi.Input[
        Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]
    ]: ...
    @vault_retention.setter
    def vault_retention(
        self,
        value: pulumi.Input[
            Union[LongTermRetentionPolicyArgs, SimpleRetentionPolicyArgs]
        ],
    ): ...

class VmmToAzureCreateNetworkMappingInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class VmmToAzureCreateNetworkMappingInputArgs:
    def __init__(__self__, *, instance_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...

class VmmToVmmCreateNetworkMappingInputArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class VmmToVmmCreateNetworkMappingInputArgs:
    def __init__(__self__, *, instance_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...

class WeeklyRetentionFormatArgsDict(TypedDict):
    days_of_the_week: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    weeks_of_the_month: NotRequired[pulumi.Input[Sequence[pulumi.Input[WeekOfMonth]]]]

@pulumi.input_type
class WeeklyRetentionFormatArgs:
    def __init__(
        __self__,
        *,
        days_of_the_week: Optional[
            pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]
        ] = ...,
        weeks_of_the_month: Optional[
            pulumi.Input[Sequence[pulumi.Input[WeekOfMonth]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]: ...
    @days_of_the_week.setter
    def days_of_the_week(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeksOfTheMonth")
    def weeks_of_the_month(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WeekOfMonth]]]]: ...
    @weeks_of_the_month.setter
    def weeks_of_the_month(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WeekOfMonth]]]]
    ): ...

class WeeklyRetentionScheduleArgsDict(TypedDict):
    days_of_the_week: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    retention_duration: NotRequired[pulumi.Input[RetentionDurationArgsDict]]
    retention_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WeeklyRetentionScheduleArgs:
    def __init__(
        __self__,
        *,
        days_of_the_week: Optional[
            pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]
        ] = ...,
        retention_duration: Optional[pulumi.Input[RetentionDurationArgs]] = ...,
        retention_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]: ...
    @days_of_the_week.setter
    def days_of_the_week(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[RetentionDurationArgs]]: ...
    @retention_duration.setter
    def retention_duration(
        self, value: Optional[pulumi.Input[RetentionDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retention_times.setter
    def retention_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WeeklyScheduleArgsDict(TypedDict):
    schedule_run_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    schedule_run_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WeeklyScheduleArgs:
    def __init__(
        __self__,
        *,
        schedule_run_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]
        ] = ...,
        schedule_run_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]: ...
    @schedule_run_days.setter
    def schedule_run_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schedule_run_times.setter
    def schedule_run_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkloadInquiryDetailsArgsDict(TypedDict):
    inquiry_validation: NotRequired[pulumi.Input[InquiryValidationArgsDict]]
    item_count: NotRequired[pulumi.Input[_builtins.float]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadInquiryDetailsArgs:
    def __init__(
        __self__,
        *,
        inquiry_validation: Optional[pulumi.Input[InquiryValidationArgs]] = ...,
        item_count: Optional[pulumi.Input[_builtins.float]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inquiryValidation")
    def inquiry_validation(self) -> Optional[pulumi.Input[InquiryValidationArgs]]: ...
    @inquiry_validation.setter
    def inquiry_validation(
        self, value: Optional[pulumi.Input[InquiryValidationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @item_count.setter
    def item_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class YearlyRetentionScheduleArgsDict(TypedDict):
    months_of_year: NotRequired[pulumi.Input[Sequence[pulumi.Input[MonthOfYear]]]]
    retention_duration: NotRequired[pulumi.Input[RetentionDurationArgsDict]]
    retention_schedule_daily: NotRequired[pulumi.Input[DailyRetentionFormatArgsDict]]
    retention_schedule_format_type: NotRequired[
        pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]
    ]
    retention_schedule_weekly: NotRequired[pulumi.Input[WeeklyRetentionFormatArgsDict]]
    retention_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class YearlyRetentionScheduleArgs:
    def __init__(
        __self__,
        *,
        months_of_year: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonthOfYear]]]
        ] = ...,
        retention_duration: Optional[pulumi.Input[RetentionDurationArgs]] = ...,
        retention_schedule_daily: Optional[
            pulumi.Input[DailyRetentionFormatArgs]
        ] = ...,
        retention_schedule_format_type: Optional[
            pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]
        ] = ...,
        retention_schedule_weekly: Optional[
            pulumi.Input[WeeklyRetentionFormatArgs]
        ] = ...,
        retention_times: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monthsOfYear")
    def months_of_year(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonthOfYear]]]]: ...
    @months_of_year.setter
    def months_of_year(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonthOfYear]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[RetentionDurationArgs]]: ...
    @retention_duration.setter
    def retention_duration(
        self, value: Optional[pulumi.Input[RetentionDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(
        self,
    ) -> Optional[pulumi.Input[DailyRetentionFormatArgs]]: ...
    @retention_schedule_daily.setter
    def retention_schedule_daily(
        self, value: Optional[pulumi.Input[DailyRetentionFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]]: ...
    @retention_schedule_format_type.setter
    def retention_schedule_format_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, RetentionScheduleFormat]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(
        self,
    ) -> Optional[pulumi.Input[WeeklyRetentionFormatArgs]]: ...
    @retention_schedule_weekly.setter
    def retention_schedule_weekly(
        self, value: Optional[pulumi.Input[WeeklyRetentionFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retention_times.setter
    def retention_times(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
