

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
__all__ = ['A2ACrossClusterMigrationReplicationDetailsResponse', 'A2AExtendedLocationDetailsResponse', 'A2AFabricSpecificLocationDetailsResponse', 'A2APolicyDetailsResponse', 'A2AProtectedDiskDetailsResponse', 'A2AProtectedManagedDiskDetailsResponse', 'A2AProtectionContainerMappingDetailsResponse', 'A2AReplicationDetailsResponse', 'A2AReplicationProtectionClusterDetailsResponse', 'A2ASharedDiskIRErrorDetailsResponse', 'A2ASharedDiskReplicationDetailsResponse', 'A2AUnprotectedDiskDetailsResponse', 'A2AZoneDetailsResponse', 'AgentDetailsResponse', 'AgentDiskDetailsResponse', 'ApplianceMonitoringDetailsResponse', 'ApplianceResourceDetailsResponse', 'AzureBackupServerContainerResponse', 'AzureFabricSpecificDetailsResponse', 'AzureFileShareProtectionPolicyResponse', 'AzureFileshareProtectedItemExtendedInfoResponse', 'AzureFileshareProtectedItemResponse', 'AzureIaaSClassicComputeVMContainerResponse', 'AzureIaaSClassicComputeVMProtectedItemResponse', 'AzureIaaSComputeVMContainerResponse', 'AzureIaaSComputeVMProtectedItemResponse', 'AzureIaaSVMHealthDetailsResponse', 'AzureIaaSVMProtectedItemExtendedInfoResponse', 'AzureIaaSVMProtectedItemResponse', 'AzureIaaSVMProtectionPolicyResponse', 'AzureMonitorAlertSettingsResponse', 'AzureRecoveryServiceVaultProtectionIntentResponse', 'AzureResourceProtectionIntentResponse', ..., 'AzureSqlContainerResponse', 'AzureSqlProtectedItemExtendedInfoResponse', 'AzureSqlProtectedItemResponse', 'AzureSqlProtectionPolicyResponse', 'AzureStorageContainerResponse', 'AzureToAzureNetworkMappingSettingsResponse', 'AzureToAzureVmSyncedConfigDetailsResponse', 'AzureVMAppContainerProtectionContainerResponse', 'AzureVmDiskDetailsResponse', 'AzureVmWorkloadProtectedItemExtendedInfoResponse', 'AzureVmWorkloadProtectedItemResponse', 'AzureVmWorkloadProtectionPolicyResponse', 'AzureVmWorkloadSAPAseDatabaseProtectedItemResponse', ..., ..., 'AzureVmWorkloadSQLDatabaseProtectedItemResponse', 'AzureWorkloadAutoProtectionIntentResponse', 'AzureWorkloadContainerAutoProtectionIntentResponse', 'AzureWorkloadContainerExtendedInfoResponse', 'AzureWorkloadContainerResponse', 'AzureWorkloadSQLAutoProtectionIntentResponse', 'ClassicAlertSettingsResponse', 'CmkKekIdentityResponse', 'CmkKeyVaultPropertiesResponse', 'ContainerIdentityInfoResponse', 'CriticalJobHistoryDetailsResponse', 'CrossSubscriptionRestoreSettingsResponse', 'CurrentJobDetailsResponse', 'CurrentScenarioDetailsResponse', 'DPMContainerExtendedInfoResponse', 'DPMProtectedItemExtendedInfoResponse', 'DPMProtectedItemResponse', 'DailyRetentionFormatResponse', 'DailyRetentionScheduleResponse', 'DailyScheduleResponse', 'DataStoreResponse', 'DataStoreUtilizationDetailsResponse', 'DayResponse', 'DiskDetailsResponse', 'DiskExclusionPropertiesResponse', 'DistributedNodesInfoResponse', 'DpmContainerResponse', 'DraDetailsResponse', 'EncryptionDetailsResponse', 'ErrorDetailResponse', 'ExtendedLocationResponse', 'ExtendedPropertiesResponse', 'FabricPropertiesResponse', 'GatewayOperationDetailsResponse', 'GenericContainerExtendedInfoResponse', 'GenericContainerResponse', 'GenericProtectedItemResponse', 'GenericProtectionPolicyResponse', 'HealthErrorResponse', 'HourlyScheduleResponse', 'HyperVHostDetailsResponse', 'HyperVReplicaAzureManagedDiskDetailsResponse', 'HyperVReplicaAzurePolicyDetailsResponse', 'HyperVReplicaAzureReplicationDetailsResponse', 'HyperVReplicaBasePolicyDetailsResponse', 'HyperVReplicaBaseReplicationDetailsResponse', 'HyperVReplicaBluePolicyDetailsResponse', 'HyperVReplicaBlueReplicationDetailsResponse', 'HyperVReplicaPolicyDetailsResponse', 'HyperVReplicaReplicationDetailsResponse', 'HyperVSiteDetailsResponse', 'IPConfigDetailsResponse', 'IaaSVMContainerResponse', 'IdentityDataResponse', 'IdentityProviderDetailsResponse', 'ImmutabilitySettingsResponse', 'InMageAgentDetailsResponse', 'InMageAzureV2ManagedDiskDetailsResponse', 'InMageAzureV2PolicyDetailsResponse', 'InMageAzureV2ProtectedDiskDetailsResponse', 'InMageAzureV2ReplicationDetailsResponse', ..., 'InMageAzureV2SwitchProviderDetailsResponse', 'InMageBasePolicyDetailsResponse', ..., 'InMagePolicyDetailsResponse', 'InMageProtectedDiskDetailsResponse', 'InMageRcmAgentUpgradeBlockingErrorDetailsResponse', 'InMageRcmDiscoveredProtectedVmDetailsResponse', 'InMageRcmFabricSpecificDetailsResponse', ..., 'InMageRcmFailbackMobilityAgentDetailsResponse', 'InMageRcmFailbackNicDetailsResponse', 'InMageRcmFailbackPolicyDetailsResponse', 'InMageRcmFailbackProtectedDiskDetailsResponse', 'InMageRcmFailbackReplicationDetailsResponse', 'InMageRcmFailbackSyncDetailsResponse', 'InMageRcmLastAgentUpgradeErrorDetailsResponse', 'InMageRcmMobilityAgentDetailsResponse', 'InMageRcmNicDetailsResponse', 'InMageRcmPolicyDetailsResponse', 'InMageRcmProtectedDiskDetailsResponse', 'InMageRcmProtectionContainerMappingDetailsResponse', 'InMageRcmReplicationDetailsResponse', 'InMageRcmSyncDetailsResponse', 'InMageRcmUnProtectedDiskDetailsResponse', 'InMageReplicationDetailsResponse', 'InitialReplicationDetailsResponse', 'InnerHealthErrorResponse', 'InputEndpointResponse', 'InquiryInfoResponse', 'InquiryValidationResponse', 'InstantRPAdditionalDetailsResponse', 'KPIResourceHealthDetailsResponse', 'LogSchedulePolicyResponse', 'LongTermRetentionPolicyResponse', 'LongTermSchedulePolicyResponse', 'MABContainerHealthDetailsResponse', 'MabContainerExtendedInfoResponse', 'MabContainerResponse', 'MabFileFolderProtectedItemExtendedInfoResponse', 'MabFileFolderProtectedItemResponse', 'MabProtectionPolicyResponse', 'MarsAgentDetailsResponse', 'MasterTargetServerResponse', 'MigrationItemPropertiesResponse', 'MobilityServiceUpdateResponse', 'MonitoringSettingsResponse', 'MonthlyRetentionScheduleResponse', 'NetworkMappingPropertiesResponse', 'OSDetailsResponse', 'OSDiskDetailsResponse', 'OSUpgradeSupportedVersionsResponse', 'PolicyPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointConnectionVaultPropertiesResponse', 'PrivateEndpointResponse', 'PrivateEndpointResponseV1', 'PrivateLinkServiceConnectionStateResponse', 'ProcessServerDetailsResponse', 'ProcessServerResponse', 'ProtectionContainerMappingPropertiesResponse', 'PushInstallerDetailsResponse', 'RcmProxyDetailsResponse', 'RecoveryPlanA2ADetailsResponse', 'RecoveryPlanActionResponse', 'RecoveryPlanAutomationRunbookActionDetailsResponse', 'RecoveryPlanGroupResponse', 'RecoveryPlanManualActionDetailsResponse', 'RecoveryPlanPropertiesResponse', 'RecoveryPlanProtectedItemResponse', 'RecoveryPlanScriptActionDetailsResponse', 'RecoveryServicesProviderPropertiesResponse', 'RegisteredClusterNodesResponse', 'ReplicationAgentDetailsResponse', 'ReplicationProtectedItemPropertiesResponse', 'ReplicationProtectionClusterPropertiesResponse', 'ReprotectAgentDetailsResponse', 'ResourceGuardOperationDetailResponse', 'ResourceGuardProxyBaseResponse', 'ResourceHealthDetailsResponse', 'RestoreSettingsResponse', 'RetentionDurationResponse', 'RetentionVolumeResponse', 'RunAsAccountResponse', 'SecurityProfilePropertiesResponse', 'SecuritySettingsResponse', 'SettingsResponse', 'SharedDiskReplicationItemPropertiesResponse', 'SimpleRetentionPolicyResponse', 'SimpleSchedulePolicyResponse', 'SimpleSchedulePolicyV2Response', 'SkuResponse', 'SnapshotBackupAdditionalDetailsResponse', 'SoftDeleteSettingsResponse', 'StorageClassificationMappingPropertiesResponse', 'SubProtectionPolicyResponse', 'SystemDataResponse', 'TieringPolicyResponse', 'UpgradeDetailsResponse', 'UserAssignedIdentityPropertiesResponse', 'UserAssignedManagedIdentityDetailsResponse', 'UserCreatedResourceTagResponse', 'UserIdentityResponse', 'VCenterPropertiesResponse', 'VMNicDetailsResponse', 'VMwareCbtMigrationDetailsResponse', 'VMwareCbtNicDetailsResponse', 'VMwareCbtProtectedDiskDetailsResponse', 'VMwareCbtProtectionContainerMappingDetailsResponse', 'VMwareCbtSecurityProfilePropertiesResponse', 'VMwareDetailsResponse', 'VMwareV2FabricSpecificDetailsResponse', 'VaultPrivateEndpointConnectionResponse', 'VaultPrivateLinkServiceConnectionStateResponse', 'VaultPropertiesResponse', 'VaultPropertiesResponseEncryption', 'VaultPropertiesResponseMoveDetails', 'VaultPropertiesResponseRedundancySettings', 'VaultRetentionPolicyResponse', 'VersionDetailsResponse', 'VmmDetailsResponse', 'VmmToAzureNetworkMappingSettingsResponse', 'VmmToVmmNetworkMappingSettingsResponse', 'VmwareCbtPolicyDetailsResponse', 'WeeklyRetentionFormatResponse', 'WeeklyRetentionScheduleResponse', 'WeeklyScheduleResponse', 'WorkloadCrrAccessTokenResponse', 'WorkloadInquiryDetailsResponse', 'YearlyRetentionScheduleResponse']
@pulumi.output_type
class A2ACrossClusterMigrationReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, fabric_object_id: Optional[_builtins.str] = ..., lifecycle_id: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., primary_fabric_location: Optional[_builtins.str] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleId")
    def lifecycle_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class A2AExtendedLocationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    


@pulumi.output_type
class A2AFabricSpecificLocationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., initial_primary_fabric_location: Optional[_builtins.str] = ..., initial_primary_zone: Optional[_builtins.str] = ..., initial_recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., initial_recovery_fabric_location: Optional[_builtins.str] = ..., initial_recovery_zone: Optional[_builtins.str] = ..., primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., primary_fabric_location: Optional[_builtins.str] = ..., primary_zone: Optional[_builtins.str] = ..., recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., recovery_fabric_location: Optional[_builtins.str] = ..., recovery_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryExtendedLocation")
    def initial_primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryFabricLocation")
    def initial_primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryZone")
    def initial_primary_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryExtendedLocation")
    def initial_recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryFabricLocation")
    def initial_recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryZone")
    def initial_recovery_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryZone")
    def primary_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryZone")
    def recovery_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class A2APolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., crash_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., recovery_point_history: Optional[_builtins.int] = ..., recovery_point_threshold_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class A2AProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_disk_level_operation: Optional[Sequence[_builtins.str]] = ..., data_pending_at_source_agent_in_mb: Optional[_builtins.float] = ..., data_pending_in_staging_storage_account_in_mb: Optional[_builtins.float] = ..., dek_key_vault_arm_id: Optional[_builtins.str] = ..., disk_capacity_in_bytes: Optional[_builtins.float] = ..., disk_name: Optional[_builtins.str] = ..., disk_state: Optional[_builtins.str] = ..., disk_type: Optional[_builtins.str] = ..., disk_uri: Optional[_builtins.str] = ..., failover_disk_name: Optional[_builtins.str] = ..., is_disk_encrypted: Optional[_builtins.bool] = ..., is_disk_key_encrypted: Optional[_builtins.bool] = ..., kek_key_vault_arm_id: Optional[_builtins.str] = ..., key_identifier: Optional[_builtins.str] = ..., monitoring_job_type: Optional[_builtins.str] = ..., monitoring_percentage_completion: Optional[_builtins.int] = ..., primary_disk_azure_storage_account_id: Optional[_builtins.str] = ..., primary_staging_azure_storage_account_id: Optional[_builtins.str] = ..., recovery_azure_storage_account_id: Optional[_builtins.str] = ..., recovery_disk_uri: Optional[_builtins.str] = ..., resync_required: Optional[_builtins.bool] = ..., secret_identifier: Optional[_builtins.str] = ..., tfo_disk_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDiskLevelOperation")
    def allowed_disk_level_operation(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingAtSourceAgentInMB")
    def data_pending_at_source_agent_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingInStagingStorageAccountInMB")
    def data_pending_in_staging_storage_account_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dekKeyVaultArmId")
    def dek_key_vault_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacityInBytes")
    def disk_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskUri")
    def disk_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDiskName")
    def failover_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDiskEncrypted")
    def is_disk_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDiskKeyEncrypted")
    def is_disk_key_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekKeyVaultArmId")
    def kek_key_vault_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryDiskAzureStorageAccountId")
    def primary_disk_azure_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryStagingAzureStorageAccountId")
    def primary_staging_azure_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureStorageAccountId")
    def recovery_azure_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryDiskUri")
    def recovery_disk_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoDiskName")
    def tfo_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class A2AProtectedManagedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_disk_level_operation: Optional[Sequence[_builtins.str]] = ..., data_pending_at_source_agent_in_mb: Optional[_builtins.float] = ..., data_pending_in_staging_storage_account_in_mb: Optional[_builtins.float] = ..., dek_key_vault_arm_id: Optional[_builtins.str] = ..., disk_capacity_in_bytes: Optional[_builtins.float] = ..., disk_id: Optional[_builtins.str] = ..., disk_name: Optional[_builtins.str] = ..., disk_state: Optional[_builtins.str] = ..., disk_type: Optional[_builtins.str] = ..., failover_disk_name: Optional[_builtins.str] = ..., is_disk_encrypted: Optional[_builtins.bool] = ..., is_disk_key_encrypted: Optional[_builtins.bool] = ..., kek_key_vault_arm_id: Optional[_builtins.str] = ..., key_identifier: Optional[_builtins.str] = ..., monitoring_job_type: Optional[_builtins.str] = ..., monitoring_percentage_completion: Optional[_builtins.int] = ..., primary_disk_encryption_set_id: Optional[_builtins.str] = ..., primary_staging_azure_storage_account_id: Optional[_builtins.str] = ..., recovery_disk_encryption_set_id: Optional[_builtins.str] = ..., recovery_orignal_target_disk_id: Optional[_builtins.str] = ..., recovery_replica_disk_account_type: Optional[_builtins.str] = ..., recovery_replica_disk_id: Optional[_builtins.str] = ..., recovery_resource_group_id: Optional[_builtins.str] = ..., recovery_target_disk_account_type: Optional[_builtins.str] = ..., recovery_target_disk_id: Optional[_builtins.str] = ..., resync_required: Optional[_builtins.bool] = ..., secret_identifier: Optional[_builtins.str] = ..., tfo_disk_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDiskLevelOperation")
    def allowed_disk_level_operation(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingAtSourceAgentInMB")
    def data_pending_at_source_agent_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingInStagingStorageAccountInMB")
    def data_pending_in_staging_storage_account_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dekKeyVaultArmId")
    def dek_key_vault_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacityInBytes")
    def disk_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDiskName")
    def failover_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDiskEncrypted")
    def is_disk_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDiskKeyEncrypted")
    def is_disk_key_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekKeyVaultArmId")
    def kek_key_vault_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryDiskEncryptionSetId")
    def primary_disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryStagingAzureStorageAccountId")
    def primary_staging_azure_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryDiskEncryptionSetId")
    def recovery_disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryOrignalTargetDiskId")
    def recovery_orignal_target_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryReplicaDiskAccountType")
    def recovery_replica_disk_account_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryReplicaDiskId")
    def recovery_replica_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryResourceGroupId")
    def recovery_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryTargetDiskAccountType")
    def recovery_target_disk_account_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryTargetDiskId")
    def recovery_target_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoDiskName")
    def tfo_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class A2AProtectionContainerMappingDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, agent_auto_update_status: Optional[_builtins.str] = ..., automation_account_arm_id: Optional[_builtins.str] = ..., automation_account_authentication_type: Optional[_builtins.str] = ..., job_schedule_name: Optional[_builtins.str] = ..., schedule_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentAutoUpdateStatus")
    def agent_auto_update_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationAccountArmId")
    def automation_account_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationAccountAuthenticationType")
    def automation_account_authentication_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobScheduleName")
    def job_schedule_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleName")
    def schedule_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class A2AReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_certificate_expiry_date: _builtins.str, churn_option_selected: _builtins.str, initial_primary_fabric_location: _builtins.str, initial_primary_zone: _builtins.str, initial_recovery_fabric_location: _builtins.str, initial_recovery_zone: _builtins.str, instance_type: _builtins.str, recovery_azure_generation: _builtins.str, vm_encryption_type: _builtins.str, agent_expiry_date: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., auto_protection_of_data_disk: Optional[_builtins.str] = ..., fabric_object_id: Optional[_builtins.str] = ..., initial_primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., initial_recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., is_cluster_infra_ready: Optional[_builtins.bool] = ..., is_replication_agent_certificate_update_required: Optional[_builtins.bool] = ..., is_replication_agent_update_required: Optional[_builtins.bool] = ..., last_heartbeat: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., lifecycle_id: Optional[_builtins.str] = ..., management_id: Optional[_builtins.str] = ..., monitoring_job_type: Optional[_builtins.str] = ..., monitoring_percentage_completion: Optional[_builtins.int] = ..., multi_vm_group_create_option: Optional[_builtins.str] = ..., multi_vm_group_id: Optional[_builtins.str] = ..., multi_vm_group_name: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., primary_availability_zone: Optional[_builtins.str] = ..., primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., primary_fabric_location: Optional[_builtins.str] = ..., protected_disks: Optional[Sequence[outputs.A2AProtectedDiskDetailsResponse]] = ..., protected_managed_disks: Optional[Sequence[outputs.A2AProtectedManagedDiskDetailsResponse]] = ..., protection_cluster_id: Optional[_builtins.str] = ..., recovery_availability_set: Optional[_builtins.str] = ..., recovery_availability_zone: Optional[_builtins.str] = ..., recovery_azure_resource_group_id: Optional[_builtins.str] = ..., recovery_azure_vm_name: Optional[_builtins.str] = ..., recovery_azure_vm_size: Optional[_builtins.str] = ..., recovery_boot_diag_storage_account_id: Optional[_builtins.str] = ..., recovery_capacity_reservation_group_id: Optional[_builtins.str] = ..., recovery_cloud_service: Optional[_builtins.str] = ..., recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., recovery_fabric_location: Optional[_builtins.str] = ..., recovery_fabric_object_id: Optional[_builtins.str] = ..., recovery_proximity_placement_group_id: Optional[_builtins.str] = ..., recovery_virtual_machine_scale_set_id: Optional[_builtins.str] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., selected_recovery_azure_network_id: Optional[_builtins.str] = ..., selected_tfo_azure_network_id: Optional[_builtins.str] = ..., test_failover_recovery_fabric_object_id: Optional[_builtins.str] = ..., tfo_azure_vm_name: Optional[_builtins.str] = ..., unprotected_disks: Optional[Sequence[outputs.A2AUnprotectedDiskDetailsResponse]] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ..., vm_synced_config_details: Optional[outputs.AzureToAzureVmSyncedConfigDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentCertificateExpiryDate")
    def agent_certificate_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="churnOptionSelected")
    def churn_option_selected(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryFabricLocation")
    def initial_primary_fabric_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryZone")
    def initial_primary_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryFabricLocation")
    def initial_recovery_fabric_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryZone")
    def initial_recovery_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureGeneration")
    def recovery_azure_generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmEncryptionType")
    def vm_encryption_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoProtectionOfDataDisk")
    def auto_protection_of_data_disk(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryExtendedLocation")
    def initial_primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryExtendedLocation")
    def initial_recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isClusterInfraReady")
    def is_cluster_infra_ready(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isReplicationAgentCertificateUpdateRequired")
    def is_replication_agent_certificate_update_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isReplicationAgentUpdateRequired")
    def is_replication_agent_update_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleId")
    def lifecycle_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementId")
    def management_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupCreateOption")
    def multi_vm_group_create_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.A2AProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedManagedDisks")
    def protected_managed_disks(self) -> Optional[Sequence[outputs.A2AProtectedManagedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionClusterId")
    def protection_cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilitySet")
    def recovery_availability_set(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilityZone")
    def recovery_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureResourceGroupId")
    def recovery_azure_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVMName")
    def recovery_azure_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVMSize")
    def recovery_azure_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryBootDiagStorageAccountId")
    def recovery_boot_diag_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryCapacityReservationGroupId")
    def recovery_capacity_reservation_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryCloudService")
    def recovery_cloud_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricObjectId")
    def recovery_fabric_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryProximityPlacementGroupId")
    def recovery_proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryVirtualMachineScaleSetId")
    def recovery_virtual_machine_scale_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedRecoveryAzureNetworkId")
    def selected_recovery_azure_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTfoAzureNetworkId")
    def selected_tfo_azure_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverRecoveryFabricObjectId")
    def test_failover_recovery_fabric_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoAzureVMName")
    def tfo_azure_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unprotectedDisks")
    def unprotected_disks(self) -> Optional[Sequence[outputs.A2AUnprotectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSyncedConfigDetails")
    def vm_synced_config_details(self) -> Optional[outputs.AzureToAzureVmSyncedConfigDetailsResponse]:
        
        ...
    


@pulumi.output_type
class A2AReplicationProtectionClusterDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, cluster_management_id: Optional[_builtins.str] = ..., failover_recovery_point_id: Optional[_builtins.str] = ..., initial_primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., initial_primary_fabric_location: Optional[_builtins.str] = ..., initial_primary_zone: Optional[_builtins.str] = ..., initial_recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., initial_recovery_fabric_location: Optional[_builtins.str] = ..., initial_recovery_zone: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., lifecycle_id: Optional[_builtins.str] = ..., multi_vm_group_create_option: Optional[_builtins.str] = ..., multi_vm_group_id: Optional[_builtins.str] = ..., multi_vm_group_name: Optional[_builtins.str] = ..., primary_availability_zone: Optional[_builtins.str] = ..., primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., primary_fabric_location: Optional[_builtins.str] = ..., recovery_availability_zone: Optional[_builtins.str] = ..., recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., recovery_fabric_location: Optional[_builtins.str] = ..., rpo_in_seconds: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterManagementId")
    def cluster_management_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryExtendedLocation")
    def initial_primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryFabricLocation")
    def initial_primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPrimaryZone")
    def initial_primary_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryExtendedLocation")
    def initial_recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryFabricLocation")
    def initial_recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialRecoveryZone")
    def initial_recovery_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleId")
    def lifecycle_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupCreateOption")
    def multi_vm_group_create_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilityZone")
    def recovery_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class A2ASharedDiskIRErrorDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.str, error_code_enum: _builtins.str, error_message: _builtins.str, possible_causes: _builtins.str, recommended_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCodeEnum")
    def error_code_enum(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class A2ASharedDiskReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, failover_recovery_point_id: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., management_id: Optional[_builtins.str] = ..., monitoring_job_type: Optional[_builtins.str] = ..., monitoring_percentage_completion: Optional[_builtins.int] = ..., primary_fabric_location: Optional[_builtins.str] = ..., protected_managed_disks: Optional[Sequence[outputs.A2AProtectedManagedDiskDetailsResponse]] = ..., recovery_fabric_location: Optional[_builtins.str] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., shared_disk_ir_errors: Optional[Sequence[outputs.A2ASharedDiskIRErrorDetailsResponse]] = ..., unprotected_disks: Optional[Sequence[outputs.A2AUnprotectedDiskDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementId")
    def management_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobType")
    def monitoring_job_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringPercentageCompletion")
    def monitoring_percentage_completion(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedManagedDisks")
    def protected_managed_disks(self) -> Optional[Sequence[outputs.A2AProtectedManagedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedDiskIRErrors")
    def shared_disk_ir_errors(self) -> Optional[Sequence[outputs.A2ASharedDiskIRErrorDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unprotectedDisks")
    def unprotected_disks(self) -> Optional[Sequence[outputs.A2AUnprotectedDiskDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class A2AUnprotectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_auto_protection_status: Optional[_builtins.str] = ..., disk_lun_id: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoProtectionStatus")
    def disk_auto_protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskLunId")
    def disk_lun_id(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class A2AZoneDetailsResponse(dict):
    
    def __init__(__self__, *, source: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_id: _builtins.str, bios_id: _builtins.str, disks: Sequence[outputs.AgentDiskDetailsResponse], fqdn: _builtins.str, machine_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Sequence[outputs.AgentDiskDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AgentDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, disk_id: _builtins.str, disk_name: _builtins.str, is_os_disk: _builtins.str, lun_id: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOSDisk")
    def is_os_disk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lunId")
    def lun_id(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ApplianceMonitoringDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_details: outputs.ApplianceResourceDetailsResponse, datastore_snapshot: Sequence[outputs.DataStoreUtilizationDetailsResponse], disks_replication_details: outputs.ApplianceResourceDetailsResponse, esxi_nfc_buffer: outputs.ApplianceResourceDetailsResponse, network_bandwidth: outputs.ApplianceResourceDetailsResponse, ram_details: outputs.ApplianceResourceDetailsResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuDetails")
    def cpu_details(self) -> outputs.ApplianceResourceDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreSnapshot")
    def datastore_snapshot(self) -> Sequence[outputs.DataStoreUtilizationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disksReplicationDetails")
    def disks_replication_details(self) -> outputs.ApplianceResourceDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esxiNfcBuffer")
    def esxi_nfc_buffer(self) -> outputs.ApplianceResourceDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidth")
    def network_bandwidth(self) -> outputs.ApplianceResourceDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramDetails")
    def ram_details(self) -> outputs.ApplianceResourceDetailsResponse:
        
        ...
    


@pulumi.output_type
class ApplianceResourceDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity: _builtins.float, process_utilization: _builtins.float, status: _builtins.str, total_utilization: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processUtilization")
    def process_utilization(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalUtilization")
    def total_utilization(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class AzureBackupServerContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., can_re_register: Optional[_builtins.bool] = ..., container_id: Optional[_builtins.str] = ..., dpm_agent_version: Optional[_builtins.str] = ..., dpm_servers: Optional[Sequence[_builtins.str]] = ..., extended_info: Optional[outputs.DPMContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., protected_item_count: Optional[_builtins.float] = ..., protection_status: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., upgrade_available: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpmAgentVersion")
    def dpm_agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpmServers")
    def dpm_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.DPMContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AzureFabricSpecificDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, container_ids: Optional[Sequence[_builtins.str]] = ..., extended_locations: Optional[Sequence[outputs.A2AExtendedLocationDetailsResponse]] = ..., location: Optional[_builtins.str] = ..., location_details: Optional[Sequence[outputs.A2AFabricSpecificLocationDetailsResponse]] = ..., zones: Optional[Sequence[outputs.A2AZoneDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerIds")
    def container_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(self) -> Optional[Sequence[outputs.A2AExtendedLocationDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationDetails")
    def location_details(self) -> Optional[Sequence[outputs.A2AFabricSpecificLocationDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[outputs.A2AZoneDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class AzureFileShareProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., retention_policy: Optional[Any] = ..., schedule_policy: Optional[Any] = ..., time_zone: Optional[_builtins.str] = ..., vault_retention_policy: Optional[outputs.VaultRetentionPolicyResponse] = ..., work_load_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultRetentionPolicy")
    def vault_retention_policy(self) -> Optional[outputs.VaultRetentionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workLoadType")
    def work_load_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureFileshareProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_state: _builtins.str, resource_state_sync_time: _builtins.str, oldest_recovery_point: Optional[_builtins.str] = ..., policy_state: Optional[_builtins.str] = ..., recovery_point_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStateSyncTime")
    def resource_state_sync_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AzureFileshareProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureFileshareProtectedItemExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_status: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureFileshareProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSClassicComputeVMContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., virtual_machine_id: Optional[_builtins.str] = ..., virtual_machine_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSClassicComputeVMProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, health_status: _builtins.str, last_backup_time: _builtins.str, protected_item_data_id: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, virtual_machine_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse] = ..., extended_properties: Optional[outputs.ExtendedPropertiesResponse] = ..., health_details: Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_status: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_status: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataId")
    def protected_item_data_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[outputs.ExtendedPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthDetails")
    def health_details(self) -> Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSComputeVMContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., virtual_machine_id: Optional[_builtins.str] = ..., virtual_machine_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSComputeVMProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, health_status: _builtins.str, last_backup_time: _builtins.str, protected_item_data_id: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, virtual_machine_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse] = ..., extended_properties: Optional[outputs.ExtendedPropertiesResponse] = ..., health_details: Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_status: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_status: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataId")
    def protected_item_data_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[outputs.ExtendedPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthDetails")
    def health_details(self) -> Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSVMHealthDetailsResponse(dict):
    
    def __init__(__self__, *, code: _builtins.int, message: _builtins.str, recommendations: Sequence[_builtins.str], title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AzureIaaSVMProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, newest_recovery_point_in_archive: Optional[_builtins.str] = ..., oldest_recovery_point: Optional[_builtins.str] = ..., oldest_recovery_point_in_archive: Optional[_builtins.str] = ..., oldest_recovery_point_in_vault: Optional[_builtins.str] = ..., policy_inconsistent: Optional[_builtins.bool] = ..., recovery_point_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newestRecoveryPointInArchive")
    def newest_recovery_point_in_archive(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInArchive")
    def oldest_recovery_point_in_archive(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInVault")
    def oldest_recovery_point_in_vault(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInconsistent")
    def policy_inconsistent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AzureIaaSVMProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, health_status: _builtins.str, last_backup_time: _builtins.str, protected_item_data_id: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, virtual_machine_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse] = ..., extended_properties: Optional[outputs.ExtendedPropertiesResponse] = ..., health_details: Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_status: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_status: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataId")
    def protected_item_data_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureIaaSVMProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[outputs.ExtendedPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthDetails")
    def health_details(self) -> Optional[Sequence[outputs.AzureIaaSVMHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureIaaSVMProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, instant_rp_details: Optional[outputs.InstantRPAdditionalDetailsResponse] = ..., instant_rp_retention_range_in_days: Optional[_builtins.int] = ..., policy_type: Optional[_builtins.str] = ..., protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., retention_policy: Optional[Any] = ..., schedule_policy: Optional[Any] = ..., snapshot_consistency_type: Optional[_builtins.str] = ..., tiering_policy: Optional[Mapping[str, outputs.TieringPolicyResponse]] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(self) -> Optional[outputs.InstantRPAdditionalDetailsResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotConsistencyType")
    def snapshot_consistency_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[Mapping[str, outputs.TieringPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureMonitorAlertSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alerts_for_all_failover_issues: Optional[_builtins.str] = ..., alerts_for_all_job_failures: Optional[_builtins.str] = ..., alerts_for_all_replication_issues: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertsForAllFailoverIssues")
    def alerts_for_all_failover_issues(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertsForAllJobFailures")
    def alerts_for_all_job_failures(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertsForAllReplicationIssues")
    def alerts_for_all_replication_issues(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AzureRecoveryServiceVaultProtectionIntentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, protection_intent_item_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., item_id: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureResourceProtectionIntentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, protection_intent_item_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., item_id: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureSQLAGWorkloadContainerProtectionContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureWorkloadContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., last_updated_time: Optional[_builtins.str] = ..., operation_type: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., workload_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureWorkloadContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureSqlContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureSqlProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oldest_recovery_point: Optional[_builtins.str] = ..., policy_state: Optional[_builtins.str] = ..., recovery_point_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AzureSqlProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureSqlProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureSqlProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataId")
    def protected_item_data_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureSqlProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., retention_policy: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class AzureStorageContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, acquire_storage_account_lock: Optional[_builtins.str] = ..., backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., operation_type: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., protected_item_count: Optional[_builtins.float] = ..., registration_status: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., storage_account_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acquireStorageAccountLock")
    def acquire_storage_account_lock(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountVersion")
    def storage_account_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureToAzureNetworkMappingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, primary_fabric_location: Optional[_builtins.str] = ..., recovery_fabric_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricLocation")
    def primary_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricLocation")
    def recovery_fabric_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureToAzureVmSyncedConfigDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_endpoints: Optional[Sequence[outputs.InputEndpointResponse]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputEndpoints")
    def input_endpoints(self) -> Optional[Sequence[outputs.InputEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class AzureVMAppContainerProtectionContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureWorkloadContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., last_updated_time: Optional[_builtins.str] = ..., operation_type: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., workload_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureWorkloadContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_target_disk_name: Optional[_builtins.str] = ..., disk_encryption_set_id: Optional[_builtins.str] = ..., disk_id: Optional[_builtins.str] = ..., lun_id: Optional[_builtins.str] = ..., max_size_mb: Optional[_builtins.str] = ..., target_disk_location: Optional[_builtins.str] = ..., target_disk_name: Optional[_builtins.str] = ..., vhd_id: Optional[_builtins.str] = ..., vhd_name: Optional[_builtins.str] = ..., vhd_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTargetDiskName")
    def custom_target_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lunId")
    def lun_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeMB")
    def max_size_mb(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskLocation")
    def target_disk_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskName")
    def target_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdId")
    def vhd_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdName")
    def vhd_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdType")
    def vhd_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, newest_recovery_point_in_archive: Optional[_builtins.str] = ..., oldest_recovery_point: Optional[_builtins.str] = ..., oldest_recovery_point_in_archive: Optional[_builtins.str] = ..., oldest_recovery_point_in_vault: Optional[_builtins.str] = ..., policy_state: Optional[_builtins.str] = ..., recovery_model: Optional[_builtins.str] = ..., recovery_point_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newestRecoveryPointInArchive")
    def newest_recovery_point_in_archive(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInArchive")
    def oldest_recovery_point_in_archive(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPointInVault")
    def oldest_recovery_point_in_vault(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryModel")
    def recovery_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, protected_item_type: _builtins.str, protection_status: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_error_detail: Optional[outputs.ErrorDetailResponse] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ..., parent_name: Optional[_builtins.str] = ..., parent_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_source_id: Optional[_builtins.str] = ..., protected_item_health_status: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., server_name: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrorDetail")
    def last_backup_error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, make_policy_consistent: Optional[_builtins.bool] = ..., protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., settings: Optional[outputs.SettingsResponse] = ..., sub_protection_policy: Optional[Sequence[outputs.SubProtectionPolicyResponse]] = ..., work_load_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="makePolicyConsistent")
    def make_policy_consistent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.SettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subProtectionPolicy")
    def sub_protection_policy(self) -> Optional[Sequence[outputs.SubProtectionPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workLoadType")
    def work_load_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadSAPAseDatabaseProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, protected_item_type: _builtins.str, protection_status: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_error_detail: Optional[outputs.ErrorDetailResponse] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ..., parent_name: Optional[_builtins.str] = ..., parent_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_source_id: Optional[_builtins.str] = ..., protected_item_health_status: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., server_name: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrorDetail")
    def last_backup_error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadSAPHanaDBInstanceProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, protected_item_type: _builtins.str, protection_status: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_error_detail: Optional[outputs.ErrorDetailResponse] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ..., parent_name: Optional[_builtins.str] = ..., parent_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_source_id: Optional[_builtins.str] = ..., protected_item_health_status: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., server_name: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrorDetail")
    def last_backup_error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadSAPHanaDatabaseProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, protected_item_type: _builtins.str, protection_status: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_error_detail: Optional[outputs.ErrorDetailResponse] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ..., parent_name: Optional[_builtins.str] = ..., parent_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_source_id: Optional[_builtins.str] = ..., protected_item_health_status: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., server_name: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrorDetail")
    def last_backup_error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureVmWorkloadSQLDatabaseProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, friendly_name: _builtins.str, protected_item_type: _builtins.str, protection_status: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., kpis_healths: Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]] = ..., last_backup_error_detail: Optional[outputs.ErrorDetailResponse] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ..., parent_name: Optional[_builtins.str] = ..., parent_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protected_item_data_source_id: Optional[_builtins.str] = ..., protected_item_health_status: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., server_name: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureVmWorkloadProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kpisHealths")
    def kpis_healths(self) -> Optional[Mapping[str, outputs.KPIResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrorDetail")
    def last_backup_error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentName")
    def parent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemDataSourceId")
    def protected_item_data_source_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemHealthStatus")
    def protected_item_health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureWorkloadAutoProtectionIntentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, protection_intent_item_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., item_id: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureWorkloadContainerAutoProtectionIntentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, protection_intent_item_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., item_id: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureWorkloadContainerExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_server_name: Optional[_builtins.str] = ..., inquiry_info: Optional[outputs.InquiryInfoResponse] = ..., nodes_list: Optional[Sequence[outputs.DistributedNodesInfoResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostServerName")
    def host_server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inquiryInfo")
    def inquiry_info(self) -> Optional[outputs.InquiryInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodesList")
    def nodes_list(self) -> Optional[Sequence[outputs.DistributedNodesInfoResponse]]:
        
        ...
    


@pulumi.output_type
class AzureWorkloadContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., extended_info: Optional[outputs.AzureWorkloadContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., last_updated_time: Optional[_builtins.str] = ..., operation_type: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., workload_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.AzureWorkloadContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureWorkloadSQLAutoProtectionIntentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, protection_intent_item_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., item_id: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., workload_item_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadItemType")
    def workload_item_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClassicAlertSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alerts_for_critical_operations: Optional[_builtins.str] = ..., email_notifications_for_site_recovery: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertsForCriticalOperations")
    def alerts_for_critical_operations(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailNotificationsForSiteRecovery")
    def email_notifications_for_site_recovery(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CmkKekIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_system_assigned_identity: Optional[_builtins.bool] = ..., user_assigned_identity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CmkKeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUri")
    def key_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerIdentityInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aad_tenant_id: Optional[_builtins.str] = ..., audience: Optional[_builtins.str] = ..., service_principal_client_id: Optional[_builtins.str] = ..., unique_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipalClientId")
    def service_principal_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CriticalJobHistoryDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_id: _builtins.str, job_name: _builtins.str, job_status: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CrossSubscriptionRestoreSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cross_subscription_restore_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionRestoreState")
    def cross_subscription_restore_state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CurrentJobDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_id: _builtins.str, job_name: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CurrentScenarioDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_id: Optional[_builtins.str] = ..., scenario_name: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DPMContainerExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_refreshed_at: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DPMProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_storage_used_in_bytes: Optional[_builtins.str] = ..., is_collocated: Optional[_builtins.bool] = ..., is_present_on_cloud: Optional[_builtins.bool] = ..., last_backup_status: Optional[_builtins.str] = ..., last_refreshed_at: Optional[_builtins.str] = ..., oldest_recovery_point: Optional[_builtins.str] = ..., on_premise_latest_recovery_point: Optional[_builtins.str] = ..., on_premise_oldest_recovery_point: Optional[_builtins.str] = ..., on_premise_recovery_point_count: Optional[_builtins.int] = ..., protectable_object_load_path: Optional[Mapping[str, _builtins.str]] = ..., protected: Optional[_builtins.bool] = ..., protection_group_name: Optional[_builtins.str] = ..., recovery_point_count: Optional[_builtins.int] = ..., total_disk_storage_size_in_bytes: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskStorageUsedInBytes")
    def disk_storage_used_in_bytes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCollocated")
    def is_collocated(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPresentOnCloud")
    def is_present_on_cloud(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremiseLatestRecoveryPoint")
    def on_premise_latest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremiseOldestRecoveryPoint")
    def on_premise_oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremiseRecoveryPointCount")
    def on_premise_recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectLoadPath")
    def protectable_object_load_path(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protected(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionGroupName")
    def protection_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDiskStorageSizeInBytes")
    def total_disk_storage_size_in_bytes(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DPMProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_engine_name: Optional[_builtins.str] = ..., backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.DPMProtectedItemExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupEngineName")
    def backup_engine_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.DPMProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DailyRetentionFormatResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_of_the_month: Optional[Sequence[outputs.DayResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfTheMonth")
    def days_of_the_month(self) -> Optional[Sequence[outputs.DayResponse]]:
        
        ...
    


@pulumi.output_type
class DailyRetentionScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_duration: Optional[outputs.RetentionDurationResponse] = ..., retention_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DailyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_run_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DataStoreResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity: Optional[_builtins.str] = ..., free_space: Optional[_builtins.str] = ..., symbolic_name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., uuid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeSpace")
    def free_space(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="symbolicName")
    def symbolic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataStoreUtilizationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_store_name: _builtins.str, total_snapshots_created: _builtins.float, total_snapshots_supported: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreName")
    def data_store_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSnapshotsCreated")
    def total_snapshots_created(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSnapshotsSupported")
    def total_snapshots_supported(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class DayResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date: Optional[_builtins.int] = ..., is_last: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLast")
    def is_last(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_size_mb: Optional[_builtins.float] = ..., vhd_id: Optional[_builtins.str] = ..., vhd_name: Optional[_builtins.str] = ..., vhd_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeMB")
    def max_size_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdId")
    def vhd_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdName")
    def vhd_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdType")
    def vhd_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskExclusionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_lun_list: Optional[Sequence[_builtins.int]] = ..., is_inclusion_list: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskLunList")
    def disk_lun_list(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInclusionList")
    def is_inclusion_list(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DistributedNodesInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_detail: Optional[outputs.ErrorDetailResponse] = ..., node_name: Optional[_builtins.str] = ..., source_resource_id: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetail")
    def error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DpmContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., can_re_register: Optional[_builtins.bool] = ..., container_id: Optional[_builtins.str] = ..., dpm_agent_version: Optional[_builtins.str] = ..., dpm_servers: Optional[Sequence[_builtins.str]] = ..., extended_info: Optional[outputs.DPMContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., protected_item_count: Optional[_builtins.float] = ..., protection_status: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., upgrade_available: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpmAgentVersion")
    def dpm_agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpmServers")
    def dpm_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.DPMContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStatus")
    def protection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DraDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, forward_protected_item_count: _builtins.int, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, reverse_protected_item_count: _builtins.int, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProtectedItemCount")
    def forward_protected_item_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseProtectedItemCount")
    def reverse_protected_item_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kek_cert_expiry_date: Optional[_builtins.str] = ..., kek_cert_thumbprint: Optional[_builtins.str] = ..., kek_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekCertExpiryDate")
    def kek_cert_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekCertThumbprint")
    def kek_cert_thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekState")
    def kek_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, recommendations: Sequence[_builtins.str]) -> None:
        
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
    def recommendations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtendedLocationResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExtendedPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_exclusion_properties: Optional[outputs.DiskExclusionPropertiesResponse] = ..., linux_vm_application_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskExclusionProperties")
    def disk_exclusion_properties(self) -> Optional[outputs.DiskExclusionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxVmApplicationName")
    def linux_vm_application_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FabricPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bcdr_state: Optional[_builtins.str] = ..., custom_details: Optional[Any] = ..., encryption_details: Optional[outputs.EncryptionDetailsResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health: Optional[_builtins.str] = ..., health_error_details: Optional[Sequence[outputs.HealthErrorResponse]] = ..., internal_identifier: Optional[_builtins.str] = ..., rollover_encryption_details: Optional[outputs.EncryptionDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bcdrState")
    def bcdr_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionDetails")
    def encryption_details(self) -> Optional[outputs.EncryptionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrorDetails")
    def health_error_details(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIdentifier")
    def internal_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverEncryptionDetails")
    def rollover_encryption_details(self) -> Optional[outputs.EncryptionDetailsResponse]:
        
        ...
    


@pulumi.output_type
class GatewayOperationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_stores: Sequence[_builtins.str], host_name: _builtins.str, progress_percentage: _builtins.int, state: _builtins.str, time_elapsed: _builtins.float, time_remaining: _builtins.float, upload_speed: _builtins.float, vmware_read_throughput: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeElapsed")
    def time_elapsed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRemaining")
    def time_remaining(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareReadThroughput")
    def vmware_read_throughput(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GenericContainerExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_identity_info: Optional[outputs.ContainerIdentityInfoResponse] = ..., raw_cert_data: Optional[_builtins.str] = ..., service_endpoints: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerIdentityInfo")
    def container_identity_info(self) -> Optional[outputs.ContainerIdentityInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawCertData")
    def raw_cert_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class GenericContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., extended_information: Optional[outputs.GenericContainerExtendedInfoResponse] = ..., fabric_name: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInformation")
    def extended_information(self) -> Optional[outputs.GenericContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GenericProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., fabric_name: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., policy_state: Optional[_builtins.str] = ..., protected_item_id: Optional[_builtins.float] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_associations: Optional[Mapping[str, _builtins.str]] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemId")
    def protected_item_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAssociations")
    def source_associations(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GenericProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, fabric_name: Optional[_builtins.str] = ..., protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., sub_protection_policy: Optional[Sequence[outputs.SubProtectionPolicyResponse]] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subProtectionPolicy")
    def sub_protection_policy(self) -> Optional[Sequence[outputs.SubProtectionPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HealthErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time_utc: Optional[_builtins.str] = ..., customer_resolvability: Optional[_builtins.str] = ..., entity_id: Optional[_builtins.str] = ..., error_category: Optional[_builtins.str] = ..., error_code: Optional[_builtins.str] = ..., error_id: Optional[_builtins.str] = ..., error_level: Optional[_builtins.str] = ..., error_message: Optional[_builtins.str] = ..., error_source: Optional[_builtins.str] = ..., error_type: Optional[_builtins.str] = ..., inner_health_errors: Optional[Sequence[outputs.InnerHealthErrorResponse]] = ..., possible_causes: Optional[_builtins.str] = ..., recommended_action: Optional[_builtins.str] = ..., recovery_provider_error_message: Optional[_builtins.str] = ..., summary_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimeUtc")
    def creation_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerResolvability")
    def customer_resolvability(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCategory")
    def error_category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorId")
    def error_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorLevel")
    def error_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorSource")
    def error_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerHealthErrors")
    def inner_health_errors(self) -> Optional[Sequence[outputs.InnerHealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryProviderErrorMessage")
    def recovery_provider_error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HourlyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interval: Optional[_builtins.int] = ..., schedule_window_duration: Optional[_builtins.int] = ..., schedule_window_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleWindowDuration")
    def schedule_window_duration(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleWindowStartTime")
    def schedule_window_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVHostDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, mars_agent_version: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAgentVersion")
    def mars_agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HyperVReplicaAzureManagedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_set_id: Optional[_builtins.str] = ..., disk_id: Optional[_builtins.str] = ..., replica_disk_type: Optional[_builtins.str] = ..., sector_size_in_bytes: Optional[_builtins.int] = ..., seed_managed_disk_id: Optional[_builtins.str] = ..., target_disk_account_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaDiskType")
    def replica_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskId")
    def seed_managed_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskAccountType")
    def target_disk_account_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaAzurePolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, active_storage_account_id: Optional[_builtins.str] = ..., application_consistent_snapshot_frequency_in_hours: Optional[_builtins.int] = ..., encryption: Optional[_builtins.str] = ..., online_replication_start_time: Optional[_builtins.str] = ..., recovery_point_history_duration_in_hours: Optional[_builtins.int] = ..., replication_interval: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeStorageAccountId")
    def active_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryDurationInHours")
    def recovery_point_history_duration_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInterval")
    def replication_interval(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaAzureReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, last_recovery_point_received: _builtins.str, all_available_os_upgrade_configurations: Optional[Sequence[outputs.OSUpgradeSupportedVersionsResponse]] = ..., azure_vm_disk_details: Optional[Sequence[outputs.AzureVmDiskDetailsResponse]] = ..., enable_rdp_on_target_option: Optional[_builtins.str] = ..., encryption: Optional[_builtins.str] = ..., initial_replication_details: Optional[outputs.InitialReplicationDetailsResponse] = ..., last_replicated_time: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., license_type: Optional[_builtins.str] = ..., linux_license_type: Optional[_builtins.str] = ..., o_s_details: Optional[outputs.OSDetailsResponse] = ..., protected_managed_disks: Optional[Sequence[outputs.HyperVReplicaAzureManagedDiskDetailsResponse]] = ..., recovery_availability_set_id: Optional[_builtins.str] = ..., recovery_azure_log_storage_account_id: Optional[_builtins.str] = ..., recovery_azure_resource_group_id: Optional[_builtins.str] = ..., recovery_azure_storage_account: Optional[_builtins.str] = ..., recovery_azure_vm_size: Optional[_builtins.str] = ..., recovery_azure_vm_name: Optional[_builtins.str] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., seed_managed_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., selected_recovery_azure_network_id: Optional[_builtins.str] = ..., selected_source_nic_id: Optional[_builtins.str] = ..., source_vm_cpu_count: Optional[_builtins.int] = ..., source_vm_ram_size_in_mb: Optional[_builtins.int] = ..., sql_server_license_type: Optional[_builtins.str] = ..., target_availability_zone: Optional[_builtins.str] = ..., target_managed_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., target_nic_tags: Optional[Mapping[str, _builtins.str]] = ..., target_proximity_placement_group_id: Optional[_builtins.str] = ..., target_vm_security_profile: Optional[outputs.SecurityProfilePropertiesResponse] = ..., target_vm_tags: Optional[Mapping[str, _builtins.str]] = ..., use_managed_disks: Optional[_builtins.str] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allAvailableOSUpgradeConfigurations")
    def all_available_os_upgrade_configurations(self) -> Optional[Sequence[outputs.OSUpgradeSupportedVersionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmDiskDetails")
    def azure_vm_disk_details(self) -> Optional[Sequence[outputs.AzureVmDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRdpOnTargetOption")
    def enable_rdp_on_target_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationDetails")
    def initial_replication_details(self) -> Optional[outputs.InitialReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicatedTime")
    def last_replicated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oSDetails")
    def o_s_details(self) -> Optional[outputs.OSDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedManagedDisks")
    def protected_managed_disks(self) -> Optional[Sequence[outputs.HyperVReplicaAzureManagedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilitySetId")
    def recovery_availability_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureLogStorageAccountId")
    def recovery_azure_log_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureResourceGroupId")
    def recovery_azure_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureStorageAccount")
    def recovery_azure_storage_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVMSize")
    def recovery_azure_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVmName")
    def recovery_azure_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedRecoveryAzureNetworkId")
    def selected_recovery_azure_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSourceNicId")
    def selected_source_nic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmCpuCount")
    def source_vm_cpu_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmRamSizeInMB")
    def source_vm_ram_size_in_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(self) -> Optional[outputs.SecurityProfilePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useManagedDisks")
    def use_managed_disks(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaBasePolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, allowed_authentication_type: Optional[_builtins.int] = ..., application_consistent_snapshot_frequency_in_hours: Optional[_builtins.int] = ..., compression: Optional[_builtins.str] = ..., initial_replication_method: Optional[_builtins.str] = ..., offline_replication_export_path: Optional[_builtins.str] = ..., offline_replication_import_path: Optional[_builtins.str] = ..., online_replication_start_time: Optional[_builtins.str] = ..., recovery_points: Optional[_builtins.int] = ..., replica_deletion_option: Optional[_builtins.str] = ..., replication_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationType")
    def allowed_authentication_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationMethod")
    def initial_replication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationExportPath")
    def offline_replication_export_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationImportPath")
    def offline_replication_import_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPoints")
    def recovery_points(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaDeletionOption")
    def replica_deletion_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPort")
    def replication_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaBaseReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, initial_replication_details: Optional[outputs.InitialReplicationDetailsResponse] = ..., last_replicated_time: Optional[_builtins.str] = ..., v_m_disk_details: Optional[Sequence[outputs.DiskDetailsResponse]] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationDetails")
    def initial_replication_details(self) -> Optional[outputs.InitialReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicatedTime")
    def last_replicated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vMDiskDetails")
    def v_m_disk_details(self) -> Optional[Sequence[outputs.DiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaBluePolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, allowed_authentication_type: Optional[_builtins.int] = ..., application_consistent_snapshot_frequency_in_hours: Optional[_builtins.int] = ..., compression: Optional[_builtins.str] = ..., initial_replication_method: Optional[_builtins.str] = ..., offline_replication_export_path: Optional[_builtins.str] = ..., offline_replication_import_path: Optional[_builtins.str] = ..., online_replication_start_time: Optional[_builtins.str] = ..., recovery_points: Optional[_builtins.int] = ..., replica_deletion_option: Optional[_builtins.str] = ..., replication_frequency_in_seconds: Optional[_builtins.int] = ..., replication_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationType")
    def allowed_authentication_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationMethod")
    def initial_replication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationExportPath")
    def offline_replication_export_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationImportPath")
    def offline_replication_import_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPoints")
    def recovery_points(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaDeletionOption")
    def replica_deletion_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFrequencyInSeconds")
    def replication_frequency_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPort")
    def replication_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaBlueReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, initial_replication_details: Optional[outputs.InitialReplicationDetailsResponse] = ..., last_replicated_time: Optional[_builtins.str] = ..., v_m_disk_details: Optional[Sequence[outputs.DiskDetailsResponse]] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationDetails")
    def initial_replication_details(self) -> Optional[outputs.InitialReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicatedTime")
    def last_replicated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vMDiskDetails")
    def v_m_disk_details(self) -> Optional[Sequence[outputs.DiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaPolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, allowed_authentication_type: Optional[_builtins.int] = ..., application_consistent_snapshot_frequency_in_hours: Optional[_builtins.int] = ..., compression: Optional[_builtins.str] = ..., initial_replication_method: Optional[_builtins.str] = ..., offline_replication_export_path: Optional[_builtins.str] = ..., offline_replication_import_path: Optional[_builtins.str] = ..., online_replication_start_time: Optional[_builtins.str] = ..., recovery_points: Optional[_builtins.int] = ..., replica_deletion_option: Optional[_builtins.str] = ..., replication_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAuthenticationType")
    def allowed_authentication_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationConsistentSnapshotFrequencyInHours")
    def application_consistent_snapshot_frequency_in_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationMethod")
    def initial_replication_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationExportPath")
    def offline_replication_export_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineReplicationImportPath")
    def offline_replication_import_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlineReplicationStartTime")
    def online_replication_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPoints")
    def recovery_points(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaDeletionOption")
    def replica_deletion_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPort")
    def replication_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HyperVReplicaReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, initial_replication_details: Optional[outputs.InitialReplicationDetailsResponse] = ..., last_replicated_time: Optional[_builtins.str] = ..., v_m_disk_details: Optional[Sequence[outputs.DiskDetailsResponse]] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationDetails")
    def initial_replication_details(self) -> Optional[outputs.InitialReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicatedTime")
    def last_replicated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vMDiskDetails")
    def v_m_disk_details(self) -> Optional[Sequence[outputs.DiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVSiteDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, hyper_v_hosts: Optional[Sequence[outputs.HyperVHostDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVHosts")
    def hyper_v_hosts(self) -> Optional[Sequence[outputs.HyperVHostDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class IPConfigDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address_type: Optional[_builtins.str] = ..., is_primary: Optional[_builtins.bool] = ..., is_seleted_for_failover: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., recovery_ip_address_type: Optional[_builtins.str] = ..., recovery_lb_backend_address_pool_ids: Optional[Sequence[_builtins.str]] = ..., recovery_public_ip_address_id: Optional[_builtins.str] = ..., recovery_static_ip_address: Optional[_builtins.str] = ..., recovery_subnet_name: Optional[_builtins.str] = ..., static_ip_address: Optional[_builtins.str] = ..., subnet_name: Optional[_builtins.str] = ..., tfo_lb_backend_address_pool_ids: Optional[Sequence[_builtins.str]] = ..., tfo_public_ip_address_id: Optional[_builtins.str] = ..., tfo_static_ip_address: Optional[_builtins.str] = ..., tfo_subnet_name: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSeletedForFailover")
    def is_seleted_for_failover(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryIPAddressType")
    def recovery_ip_address_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryLBBackendAddressPoolIds")
    def recovery_lb_backend_address_pool_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPublicIPAddressId")
    def recovery_public_ip_address_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryStaticIPAddress")
    def recovery_static_ip_address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoverySubnetName")
    def recovery_subnet_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIPAddress")
    def static_ip_address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetName")
    def subnet_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoLBBackendAddressPoolIds")
    def tfo_lb_backend_address_pool_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoPublicIPAddressId")
    def tfo_public_ip_address_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoStaticIPAddress")
    def tfo_static_ip_address(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoSubnetName")
    def tfo_subnet_name(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IaaSVMContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, backup_management_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., protectable_object_type: Optional[_builtins.str] = ..., registration_status: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., virtual_machine_id: Optional[_builtins.str] = ..., virtual_machine_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineVersion")
    def virtual_machine_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserIdentityResponse]] = ...) -> None:
        
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
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class IdentityProviderDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aad_authority: Optional[_builtins.str] = ..., application_id: Optional[_builtins.str] = ..., audience: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ImmutabilitySettingsResponse(dict):
    
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class InMageAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_expiry_date: Optional[_builtins.str] = ..., agent_update_status: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., post_update_reboot_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpdateStatus")
    def agent_update_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postUpdateRebootStatus")
    def post_update_reboot_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InMageAzureV2ManagedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_set_id: Optional[_builtins.str] = ..., disk_id: Optional[_builtins.str] = ..., replica_disk_type: Optional[_builtins.str] = ..., seed_managed_disk_id: Optional[_builtins.str] = ..., target_disk_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaDiskType")
    def replica_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskId")
    def seed_managed_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskName")
    def target_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InMageAzureV2PolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., crash_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., recovery_point_history: Optional[_builtins.int] = ..., recovery_point_threshold_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageAzureV2ProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_capacity_in_bytes: Optional[_builtins.float] = ..., disk_id: Optional[_builtins.str] = ..., disk_name: Optional[_builtins.str] = ..., disk_resized: Optional[_builtins.str] = ..., file_system_capacity_in_bytes: Optional[_builtins.float] = ..., health_error_code: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., progress_health: Optional[_builtins.str] = ..., progress_status: Optional[_builtins.str] = ..., protection_stage: Optional[_builtins.str] = ..., ps_data_in_mega_bytes: Optional[_builtins.float] = ..., resync_duration_in_seconds: Optional[_builtins.float] = ..., resync_last15_minutes_transferred_bytes: Optional[_builtins.float] = ..., resync_last_data_transfer_time_utc: Optional[_builtins.str] = ..., resync_processed_bytes: Optional[_builtins.float] = ..., resync_progress_percentage: Optional[_builtins.int] = ..., resync_required: Optional[_builtins.str] = ..., resync_start_time: Optional[_builtins.str] = ..., resync_total_transferred_bytes: Optional[_builtins.float] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., seconds_to_take_switch_provider: Optional[_builtins.float] = ..., source_data_in_mega_bytes: Optional[_builtins.float] = ..., target_data_in_mega_bytes: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacityInBytes")
    def disk_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskResized")
    def disk_resized(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemCapacityInBytes")
    def file_system_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrorCode")
    def health_error_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressHealth")
    def progress_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressStatus")
    def progress_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStage")
    def protection_stage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psDataInMegaBytes")
    def ps_data_in_mega_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncDurationInSeconds")
    def resync_duration_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncLast15MinutesTransferredBytes")
    def resync_last15_minutes_transferred_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncLastDataTransferTimeUTC")
    def resync_last_data_transfer_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProcessedBytes")
    def resync_processed_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncStartTime")
    def resync_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncTotalTransferredBytes")
    def resync_total_transferred_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondsToTakeSwitchProvider")
    def seconds_to_take_switch_provider(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDataInMegaBytes")
    def source_data_in_mega_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDataInMegaBytes")
    def target_data_in_mega_bytes(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class InMageAzureV2ReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, last_recovery_point_received: _builtins.str, os_name: _builtins.str, agent_expiry_date: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., all_available_os_upgrade_configurations: Optional[Sequence[outputs.OSUpgradeSupportedVersionsResponse]] = ..., azure_vm_disk_details: Optional[Sequence[outputs.AzureVmDiskDetailsResponse]] = ..., azure_vm_generation: Optional[_builtins.str] = ..., compressed_data_rate_in_mb: Optional[_builtins.float] = ..., datastores: Optional[Sequence[_builtins.str]] = ..., discovery_type: Optional[_builtins.str] = ..., disk_resized: Optional[_builtins.str] = ..., enable_rdp_on_target_option: Optional[_builtins.str] = ..., firmware_type: Optional[_builtins.str] = ..., infrastructure_vm_id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., is_additional_stats_available: Optional[_builtins.bool] = ..., is_agent_update_required: Optional[_builtins.str] = ..., is_reboot_after_update_required: Optional[_builtins.str] = ..., last_heartbeat: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., last_update_received_time: Optional[_builtins.str] = ..., license_type: Optional[_builtins.str] = ..., master_target_id: Optional[_builtins.str] = ..., multi_vm_group_id: Optional[_builtins.str] = ..., multi_vm_group_name: Optional[_builtins.str] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., os_disk_id: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., os_version: Optional[_builtins.str] = ..., process_server_id: Optional[_builtins.str] = ..., process_server_name: Optional[_builtins.str] = ..., protected_disks: Optional[Sequence[outputs.InMageAzureV2ProtectedDiskDetailsResponse]] = ..., protected_managed_disks: Optional[Sequence[outputs.InMageAzureV2ManagedDiskDetailsResponse]] = ..., protection_stage: Optional[_builtins.str] = ..., recovery_availability_set_id: Optional[_builtins.str] = ..., recovery_azure_log_storage_account_id: Optional[_builtins.str] = ..., recovery_azure_resource_group_id: Optional[_builtins.str] = ..., recovery_azure_storage_account: Optional[_builtins.str] = ..., recovery_azure_vm_name: Optional[_builtins.str] = ..., recovery_azure_vm_size: Optional[_builtins.str] = ..., replica_id: Optional[_builtins.str] = ..., resync_progress_percentage: Optional[_builtins.int] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., seed_managed_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., selected_recovery_azure_network_id: Optional[_builtins.str] = ..., selected_source_nic_id: Optional[_builtins.str] = ..., selected_tfo_azure_network_id: Optional[_builtins.str] = ..., source_vm_cpu_count: Optional[_builtins.int] = ..., source_vm_ram_size_in_mb: Optional[_builtins.int] = ..., sql_server_license_type: Optional[_builtins.str] = ..., supported_os_versions: Optional[Sequence[_builtins.str]] = ..., switch_provider_blocking_error_details: Optional[Sequence[outputs.InMageAzureV2SwitchProviderBlockingErrorDetailsResponse]] = ..., switch_provider_details: Optional[outputs.InMageAzureV2SwitchProviderDetailsResponse] = ..., target_availability_zone: Optional[_builtins.str] = ..., target_managed_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., target_nic_tags: Optional[Mapping[str, _builtins.str]] = ..., target_proximity_placement_group_id: Optional[_builtins.str] = ..., target_vm_id: Optional[_builtins.str] = ..., target_vm_tags: Optional[Mapping[str, _builtins.str]] = ..., total_data_transferred: Optional[_builtins.float] = ..., total_progress_health: Optional[_builtins.str] = ..., uncompressed_data_rate_in_mb: Optional[_builtins.float] = ..., use_managed_disks: Optional[_builtins.str] = ..., v_center_infrastructure_id: Optional[_builtins.str] = ..., validation_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., vhd_name: Optional[_builtins.str] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allAvailableOSUpgradeConfigurations")
    def all_available_os_upgrade_configurations(self) -> Optional[Sequence[outputs.OSUpgradeSupportedVersionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVMDiskDetails")
    def azure_vm_disk_details(self) -> Optional[Sequence[outputs.AzureVmDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVmGeneration")
    def azure_vm_generation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressedDataRateInMB")
    def compressed_data_rate_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastores(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskResized")
    def disk_resized(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRdpOnTargetOption")
    def enable_rdp_on_target_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureVmId")
    def infrastructure_vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAdditionalStatsAvailable")
    def is_additional_stats_available(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAgentUpdateRequired")
    def is_agent_update_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRebootAfterUpdateRequired")
    def is_reboot_after_update_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateReceivedTime")
    def last_update_received_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterTargetId")
    def master_target_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskId")
    def os_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerName")
    def process_server_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.InMageAzureV2ProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedManagedDisks")
    def protected_managed_disks(self) -> Optional[Sequence[outputs.InMageAzureV2ManagedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStage")
    def protection_stage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAvailabilitySetId")
    def recovery_availability_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureLogStorageAccountId")
    def recovery_azure_log_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureResourceGroupId")
    def recovery_azure_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureStorageAccount")
    def recovery_azure_storage_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVMName")
    def recovery_azure_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryAzureVMSize")
    def recovery_azure_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaId")
    def replica_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedRecoveryAzureNetworkId")
    def selected_recovery_azure_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedSourceNicId")
    def selected_source_nic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedTfoAzureNetworkId")
    def selected_tfo_azure_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmCpuCount")
    def source_vm_cpu_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmRamSizeInMB")
    def source_vm_ram_size_in_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSVersions")
    def supported_os_versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchProviderBlockingErrorDetails")
    def switch_provider_blocking_error_details(self) -> Optional[Sequence[outputs.InMageAzureV2SwitchProviderBlockingErrorDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchProviderDetails")
    def switch_provider_details(self) -> Optional[outputs.InMageAzureV2SwitchProviderDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmId")
    def target_vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDataTransferred")
    def total_data_transferred(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalProgressHealth")
    def total_progress_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uncompressedDataRateInMB")
    def uncompressed_data_rate_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useManagedDisks")
    def use_managed_disks(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterInfrastructureId")
    def v_center_infrastructure_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdName")
    def vhd_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InMageAzureV2SwitchProviderBlockingErrorDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.str, error_message: _builtins.str, error_message_parameters: Mapping[str, _builtins.str], error_tags: Mapping[str, _builtins.str], possible_causes: _builtins.str, recommended_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessageParameters")
    def error_message_parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorTags")
    def error_tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageAzureV2SwitchProviderDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_appliance_id: _builtins.str, target_fabric_id: _builtins.str, target_resource_id: _builtins.str, target_vault_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetApplianceId")
    def target_appliance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFabricId")
    def target_fabric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVaultId")
    def target_vault_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageBasePolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., recovery_point_history: Optional[_builtins.int] = ..., recovery_point_threshold_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageFabricSwitchProviderBlockingErrorDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.str, error_message: _builtins.str, error_message_parameters: Mapping[str, _builtins.str], error_tags: Mapping[str, _builtins.str], possible_causes: _builtins.str, recommended_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessageParameters")
    def error_message_parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorTags")
    def error_tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMagePolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., recovery_point_history: Optional[_builtins.int] = ..., recovery_point_threshold_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistory")
    def recovery_point_history(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointThresholdInMinutes")
    def recovery_point_threshold_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_capacity_in_bytes: Optional[_builtins.float] = ..., disk_id: Optional[_builtins.str] = ..., disk_name: Optional[_builtins.str] = ..., disk_resized: Optional[_builtins.str] = ..., file_system_capacity_in_bytes: Optional[_builtins.float] = ..., health_error_code: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., progress_health: Optional[_builtins.str] = ..., progress_status: Optional[_builtins.str] = ..., protection_stage: Optional[_builtins.str] = ..., ps_data_in_mb: Optional[_builtins.float] = ..., resync_duration_in_seconds: Optional[_builtins.float] = ..., resync_last15_minutes_transferred_bytes: Optional[_builtins.float] = ..., resync_last_data_transfer_time_utc: Optional[_builtins.str] = ..., resync_processed_bytes: Optional[_builtins.float] = ..., resync_progress_percentage: Optional[_builtins.int] = ..., resync_required: Optional[_builtins.str] = ..., resync_start_time: Optional[_builtins.str] = ..., resync_total_transferred_bytes: Optional[_builtins.float] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., source_data_in_mb: Optional[_builtins.float] = ..., target_data_in_mb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCapacityInBytes")
    def disk_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskResized")
    def disk_resized(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemCapacityInBytes")
    def file_system_capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrorCode")
    def health_error_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressHealth")
    def progress_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressStatus")
    def progress_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStage")
    def protection_stage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psDataInMB")
    def ps_data_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncDurationInSeconds")
    def resync_duration_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncLast15MinutesTransferredBytes")
    def resync_last15_minutes_transferred_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncLastDataTransferTimeUTC")
    def resync_last_data_transfer_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProcessedBytes")
    def resync_processed_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncStartTime")
    def resync_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncTotalTransferredBytes")
    def resync_total_transferred_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDataInMB")
    def source_data_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDataInMB")
    def target_data_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class InMageRcmAgentUpgradeBlockingErrorDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.str, error_message: _builtins.str, error_message_parameters: Mapping[str, _builtins.str], error_tags: Mapping[str, _builtins.str], possible_causes: _builtins.str, recommended_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessageParameters")
    def error_message_parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorTags")
    def error_tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmDiscoveredProtectedVmDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, datastores: Sequence[_builtins.str], ip_addresses: Sequence[_builtins.str], is_deleted: _builtins.bool, last_discovery_time_in_utc: _builtins.str, os_name: _builtins.str, power_status: _builtins.str, updated_timestamp: _builtins.str, v_center_fqdn: _builtins.str, v_center_id: _builtins.str, vm_fqdn: _builtins.str, vmware_tools_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastores(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDiscoveryTimeInUtc")
    def last_discovery_time_in_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterFqdn")
    def v_center_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmFqdn")
    def vm_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareToolsStatus")
    def vmware_tools_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmFabricSpecificDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_details: Sequence[outputs.AgentDetailsResponse], control_plane_uri: _builtins.str, data_plane_uri: _builtins.str, dras: Sequence[outputs.DraDetailsResponse], instance_type: _builtins.str, mars_agents: Sequence[outputs.MarsAgentDetailsResponse], physical_site_id: _builtins.str, process_servers: Sequence[outputs.ProcessServerDetailsResponse], push_installers: Sequence[outputs.PushInstallerDetailsResponse], rcm_proxies: Sequence[outputs.RcmProxyDetailsResponse], replication_agents: Sequence[outputs.ReplicationAgentDetailsResponse], reprotect_agents: Sequence[outputs.ReprotectAgentDetailsResponse], service_container_id: _builtins.str, service_endpoint: _builtins.str, service_resource_id: _builtins.str, vmware_site_id: _builtins.str, source_agent_identity_details: Optional[outputs.IdentityProviderDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Sequence[outputs.AgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneUri")
    def control_plane_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPlaneUri")
    def data_plane_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dras(self) -> Sequence[outputs.DraDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAgents")
    def mars_agents(self) -> Sequence[outputs.MarsAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalSiteId")
    def physical_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServers")
    def process_servers(self) -> Sequence[outputs.ProcessServerDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pushInstallers")
    def push_installers(self) -> Sequence[outputs.PushInstallerDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rcmProxies")
    def rcm_proxies(self) -> Sequence[outputs.RcmProxyDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationAgents")
    def replication_agents(self) -> Sequence[outputs.ReplicationAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reprotectAgents")
    def reprotect_agents(self) -> Sequence[outputs.ReprotectAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceContainerId")
    def service_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAgentIdentityDetails")
    def source_agent_identity_details(self) -> Optional[outputs.IdentityProviderDetailsResponse]:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackDiscoveredProtectedVmDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_timestamp: _builtins.str, datastores: Sequence[_builtins.str], ip_addresses: Sequence[_builtins.str], is_deleted: _builtins.bool, last_discovery_time_in_utc: _builtins.str, os_name: _builtins.str, power_status: _builtins.str, updated_timestamp: _builtins.str, v_center_fqdn: _builtins.str, v_center_id: _builtins.str, vm_fqdn: _builtins.str, vmware_tools_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastores(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDiscoveryTimeInUtc")
    def last_discovery_time_in_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterFqdn")
    def v_center_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmFqdn")
    def vm_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareToolsStatus")
    def vmware_tools_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackMobilityAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_version_expiry_date: _builtins.str, driver_version: _builtins.str, driver_version_expiry_date: _builtins.str, is_upgradeable: _builtins.str, last_heartbeat_utc: _builtins.str, latest_upgradable_version_without_reboot: _builtins.str, latest_version: _builtins.str, reasons_blocking_upgrade: Sequence[_builtins.str], version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersionExpiryDate")
    def agent_version_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverVersion")
    def driver_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverVersionExpiryDate")
    def driver_version_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUpgradeable")
    def is_upgradeable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestUpgradableVersionWithoutReboot")
    def latest_upgradable_version_without_reboot(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reasonsBlockingUpgrade")
    def reasons_blocking_upgrade(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackNicDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, adapter_type: _builtins.str, mac_address: _builtins.str, network_name: _builtins.str, source_ip_address: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adapterType")
    def adapter_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpAddress")
    def source_ip_address(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackPolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., crash_consistent_frequency_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, data_pending_at_source_agent_in_mb: _builtins.float, data_pending_in_log_data_store_in_mb: _builtins.float, disk_id: _builtins.str, disk_name: _builtins.str, disk_uuid: _builtins.str, is_initial_replication_complete: _builtins.str, is_os_disk: _builtins.str, last_sync_time: _builtins.str, ir_details: Optional[outputs.InMageRcmFailbackSyncDetailsResponse] = ..., resync_details: Optional[outputs.InMageRcmFailbackSyncDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingAtSourceAgentInMB")
    def data_pending_at_source_agent_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingInLogDataStoreInMB")
    def data_pending_in_log_data_store_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskUuid")
    def disk_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInitialReplicationComplete")
    def is_initial_replication_complete(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOSDisk")
    def is_os_disk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="irDetails")
    def ir_details(self) -> Optional[outputs.InMageRcmFailbackSyncDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncDetails")
    def resync_details(self) -> Optional[outputs.InMageRcmFailbackSyncDetailsResponse]:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_virtual_machine_id: _builtins.str, initial_replication_processed_bytes: _builtins.float, initial_replication_progress_health: _builtins.str, initial_replication_progress_percentage: _builtins.int, initial_replication_transferred_bytes: _builtins.float, instance_type: _builtins.str, internal_identifier: _builtins.str, is_agent_registration_successful_after_failover: _builtins.bool, last_planned_failover_start_time: _builtins.str, last_planned_failover_status: _builtins.str, last_used_policy_friendly_name: _builtins.str, last_used_policy_id: _builtins.str, log_storage_account_id: _builtins.str, multi_vm_group_name: _builtins.str, os_type: _builtins.str, reprotect_agent_id: _builtins.str, reprotect_agent_name: _builtins.str, resync_processed_bytes: _builtins.float, resync_progress_health: _builtins.str, resync_progress_percentage: _builtins.int, resync_required: _builtins.str, resync_state: _builtins.str, resync_transferred_bytes: _builtins.float, target_data_store_name: _builtins.str, target_vm_name: _builtins.str, targetv_center_id: _builtins.str, discovered_vm_details: Optional[outputs.InMageRcmFailbackDiscoveredProtectedVmDetailsResponse] = ..., mobility_agent_details: Optional[outputs.InMageRcmFailbackMobilityAgentDetailsResponse] = ..., protected_disks: Optional[Sequence[outputs.InMageRcmFailbackProtectedDiskDetailsResponse]] = ..., vm_nics: Optional[Sequence[outputs.InMageRcmFailbackNicDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureVirtualMachineId")
    def azure_virtual_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProcessedBytes")
    def initial_replication_processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressHealth")
    def initial_replication_progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressPercentage")
    def initial_replication_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationTransferredBytes")
    def initial_replication_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIdentifier")
    def internal_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAgentRegistrationSuccessfulAfterFailover")
    def is_agent_registration_successful_after_failover(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPlannedFailoverStartTime")
    def last_planned_failover_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPlannedFailoverStatus")
    def last_planned_failover_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUsedPolicyFriendlyName")
    def last_used_policy_friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUsedPolicyId")
    def last_used_policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reprotectAgentId")
    def reprotect_agent_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reprotectAgentName")
    def reprotect_agent_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProcessedBytes")
    def resync_processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressHealth")
    def resync_progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncState")
    def resync_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncTransferredBytes")
    def resync_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDataStoreName")
    def target_data_store_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetvCenterId")
    def targetv_center_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredVmDetails")
    def discovered_vm_details(self) -> Optional[outputs.InMageRcmFailbackDiscoveredProtectedVmDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mobilityAgentDetails")
    def mobility_agent_details(self) -> Optional[outputs.InMageRcmFailbackMobilityAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.InMageRcmFailbackProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.InMageRcmFailbackNicDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class InMageRcmFailbackSyncDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last15_minutes_transferred_bytes: _builtins.float, last_data_transfer_time_utc: _builtins.str, last_refresh_time: _builtins.str, processed_bytes: _builtins.float, progress_health: _builtins.str, progress_percentage: _builtins.int, start_time: _builtins.str, transferred_bytes: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="last15MinutesTransferredBytes")
    def last15_minutes_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDataTransferTimeUtc")
    def last_data_transfer_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshTime")
    def last_refresh_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processedBytes")
    def processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressHealth")
    def progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferredBytes")
    def transferred_bytes(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class InMageRcmLastAgentUpgradeErrorDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.str, error_message: _builtins.str, error_message_parameters: Mapping[str, _builtins.str], error_tags: Mapping[str, _builtins.str], possible_causes: _builtins.str, recommended_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessageParameters")
    def error_message_parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorTags")
    def error_tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmMobilityAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_version_expiry_date: _builtins.str, driver_version: _builtins.str, driver_version_expiry_date: _builtins.str, is_upgradeable: _builtins.str, last_heartbeat_utc: _builtins.str, latest_agent_release_date: _builtins.str, latest_upgradable_version_without_reboot: _builtins.str, latest_version: _builtins.str, reasons_blocking_upgrade: Sequence[_builtins.str], version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersionExpiryDate")
    def agent_version_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverVersion")
    def driver_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverVersionExpiryDate")
    def driver_version_expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUpgradeable")
    def is_upgradeable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestAgentReleaseDate")
    def latest_agent_release_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestUpgradableVersionWithoutReboot")
    def latest_upgradable_version_without_reboot(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reasonsBlockingUpgrade")
    def reasons_blocking_upgrade(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmNicDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, nic_id: _builtins.str, source_ip_address: _builtins.str, source_ip_address_type: _builtins.str, source_network_id: _builtins.str, source_subnet_name: _builtins.str, is_primary_nic: Optional[_builtins.str] = ..., is_selected_for_failover: Optional[_builtins.str] = ..., target_ip_address: Optional[_builtins.str] = ..., target_ip_address_type: Optional[_builtins.str] = ..., target_nic_name: Optional[_builtins.str] = ..., target_subnet_name: Optional[_builtins.str] = ..., test_ip_address: Optional[_builtins.str] = ..., test_ip_address_type: Optional[_builtins.str] = ..., test_subnet_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIPAddress")
    def source_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIPAddressType")
    def source_ip_address_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceNetworkId")
    def source_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetName")
    def source_subnet_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimaryNic")
    def is_primary_nic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSelectedForFailover")
    def is_selected_for_failover(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIPAddress")
    def target_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIPAddressType")
    def target_ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicName")
    def target_nic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSubnetName")
    def target_subnet_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testIPAddress")
    def test_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testIPAddressType")
    def test_ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testSubnetName")
    def test_subnet_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InMageRcmPolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., crash_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., enable_multi_vm_sync: Optional[_builtins.str] = ..., recovery_point_history_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiVmSync")
    def enable_multi_vm_sync(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageRcmProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, data_pending_at_source_agent_in_mb: _builtins.float, data_pending_in_log_data_store_in_mb: _builtins.float, disk_encryption_set_id: _builtins.str, disk_id: _builtins.str, disk_name: _builtins.str, disk_state: _builtins.str, is_initial_replication_complete: _builtins.str, is_os_disk: _builtins.str, log_storage_account_id: _builtins.str, seed_blob_uri: _builtins.str, seed_managed_disk_id: _builtins.str, target_managed_disk_id: _builtins.str, custom_target_disk_name: Optional[_builtins.str] = ..., disk_type: Optional[_builtins.str] = ..., ir_details: Optional[outputs.InMageRcmSyncDetailsResponse] = ..., resync_details: Optional[outputs.InMageRcmSyncDetailsResponse] = ..., sector_size_in_bytes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingAtSourceAgentInMB")
    def data_pending_at_source_agent_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPendingInLogDataStoreInMB")
    def data_pending_in_log_data_store_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInitialReplicationComplete")
    def is_initial_replication_complete(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOSDisk")
    def is_os_disk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedBlobUri")
    def seed_blob_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskId")
    def seed_managed_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskId")
    def target_managed_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTargetDiskName")
    def custom_target_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="irDetails")
    def ir_details(self) -> Optional[outputs.InMageRcmSyncDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncDetails")
    def resync_details(self) -> Optional[outputs.InMageRcmSyncDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InMageRcmProtectionContainerMappingDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_agent_auto_upgrade: _builtins.str, instance_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAgentAutoUpgrade")
    def enable_agent_auto_upgrade(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageRcmReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_upgrade_attempt_to_version: _builtins.str, agent_upgrade_job_id: _builtins.str, agent_upgrade_state: _builtins.str, allocated_memory_in_mb: _builtins.float, discovery_type: _builtins.str, fabric_discovery_machine_id: _builtins.str, failover_recovery_point_id: _builtins.str, firmware_type: _builtins.str, initial_replication_processed_bytes: _builtins.float, initial_replication_progress_health: _builtins.str, initial_replication_progress_percentage: _builtins.int, initial_replication_transferred_bytes: _builtins.float, instance_type: _builtins.str, internal_identifier: _builtins.str, is_agent_registration_successful_after_failover: _builtins.bool, is_last_upgrade_successful: _builtins.str, last_agent_upgrade_type: _builtins.str, last_recovery_point_id: _builtins.str, last_recovery_point_received: _builtins.str, last_rpo_calculated_time: _builtins.str, last_rpo_in_seconds: _builtins.float, multi_vm_group_name: _builtins.str, os_type: _builtins.str, primary_nic_ip_address: _builtins.str, process_server_id: _builtins.str, process_server_name: _builtins.str, processor_core_count: _builtins.int, resync_processed_bytes: _builtins.float, resync_progress_health: _builtins.str, resync_progress_percentage: _builtins.int, resync_required: _builtins.str, resync_state: _builtins.str, resync_transferred_bytes: _builtins.float, run_as_account_id: _builtins.str, storage_account_id: _builtins.str, target_generation: _builtins.str, agent_upgrade_blocking_error_details: Optional[Sequence[outputs.InMageRcmAgentUpgradeBlockingErrorDetailsResponse]] = ..., discovered_vm_details: Optional[outputs.InMageRcmDiscoveredProtectedVmDetailsResponse] = ..., last_agent_upgrade_error_details: Optional[Sequence[outputs.InMageRcmLastAgentUpgradeErrorDetailsResponse]] = ..., license_type: Optional[_builtins.str] = ..., linux_license_type: Optional[_builtins.str] = ..., mobility_agent_details: Optional[outputs.InMageRcmMobilityAgentDetailsResponse] = ..., os_name: Optional[_builtins.str] = ..., protected_disks: Optional[Sequence[outputs.InMageRcmProtectedDiskDetailsResponse]] = ..., seed_managed_disk_tags: Optional[Sequence[outputs.UserCreatedResourceTagResponse]] = ..., sql_server_license_type: Optional[_builtins.str] = ..., supported_os_versions: Optional[Sequence[_builtins.str]] = ..., target_availability_set_id: Optional[_builtins.str] = ..., target_availability_zone: Optional[_builtins.str] = ..., target_boot_diagnostics_storage_account_id: Optional[_builtins.str] = ..., target_location: Optional[_builtins.str] = ..., target_managed_disk_tags: Optional[Sequence[outputs.UserCreatedResourceTagResponse]] = ..., target_network_id: Optional[_builtins.str] = ..., target_nic_tags: Optional[Sequence[outputs.UserCreatedResourceTagResponse]] = ..., target_proximity_placement_group_id: Optional[_builtins.str] = ..., target_resource_group_id: Optional[_builtins.str] = ..., target_vm_name: Optional[_builtins.str] = ..., target_vm_security_profile: Optional[outputs.SecurityProfilePropertiesResponse] = ..., target_vm_size: Optional[_builtins.str] = ..., target_vm_tags: Optional[Sequence[outputs.UserCreatedResourceTagResponse]] = ..., test_network_id: Optional[_builtins.str] = ..., unprotected_disks: Optional[Sequence[outputs.InMageRcmUnProtectedDiskDetailsResponse]] = ..., vm_nics: Optional[Sequence[outputs.InMageRcmNicDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpgradeAttemptToVersion")
    def agent_upgrade_attempt_to_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpgradeJobId")
    def agent_upgrade_job_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpgradeState")
    def agent_upgrade_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedMemoryInMB")
    def allocated_memory_in_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProcessedBytes")
    def initial_replication_processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressHealth")
    def initial_replication_progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressPercentage")
    def initial_replication_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationTransferredBytes")
    def initial_replication_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIdentifier")
    def internal_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAgentRegistrationSuccessfulAfterFailover")
    def is_agent_registration_successful_after_failover(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLastUpgradeSuccessful")
    def is_last_upgrade_successful(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAgentUpgradeType")
    def last_agent_upgrade_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointId")
    def last_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoInSeconds")
    def last_rpo_in_seconds(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNicIpAddress")
    def primary_nic_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerName")
    def process_server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processorCoreCount")
    def processor_core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProcessedBytes")
    def resync_processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressHealth")
    def resync_progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncState")
    def resync_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncTransferredBytes")
    def resync_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGeneration")
    def target_generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentUpgradeBlockingErrorDetails")
    def agent_upgrade_blocking_error_details(self) -> Optional[Sequence[outputs.InMageRcmAgentUpgradeBlockingErrorDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredVmDetails")
    def discovered_vm_details(self) -> Optional[outputs.InMageRcmDiscoveredProtectedVmDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAgentUpgradeErrorDetails")
    def last_agent_upgrade_error_details(self) -> Optional[Sequence[outputs.InMageRcmLastAgentUpgradeErrorDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mobilityAgentDetails")
    def mobility_agent_details(self) -> Optional[outputs.InMageRcmMobilityAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.InMageRcmProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskTags")
    def seed_managed_disk_tags(self) -> Optional[Sequence[outputs.UserCreatedResourceTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSVersions")
    def supported_os_versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBootDiagnosticsStorageAccountId")
    def target_boot_diagnostics_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskTags")
    def target_managed_disk_tags(self) -> Optional[Sequence[outputs.UserCreatedResourceTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(self) -> Optional[Sequence[outputs.UserCreatedResourceTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(self) -> Optional[outputs.SecurityProfilePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(self) -> Optional[Sequence[outputs.UserCreatedResourceTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unprotectedDisks")
    def unprotected_disks(self) -> Optional[Sequence[outputs.InMageRcmUnProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.InMageRcmNicDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class InMageRcmSyncDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last15_minutes_transferred_bytes: _builtins.float, last_data_transfer_time_utc: _builtins.str, last_refresh_time: _builtins.str, processed_bytes: _builtins.float, progress_health: _builtins.str, progress_percentage: _builtins.int, start_time: _builtins.str, transferred_bytes: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="last15MinutesTransferredBytes")
    def last15_minutes_transferred_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDataTransferTimeUtc")
    def last_data_transfer_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshTime")
    def last_refresh_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processedBytes")
    def processed_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressHealth")
    def progress_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferredBytes")
    def transferred_bytes(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class InMageRcmUnProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, disk_id: _builtins.str, disk_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InMageReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, active_site_type: Optional[_builtins.str] = ..., agent_details: Optional[outputs.InMageAgentDetailsResponse] = ..., azure_storage_account_id: Optional[_builtins.str] = ..., compressed_data_rate_in_mb: Optional[_builtins.float] = ..., consistency_points: Optional[Mapping[str, _builtins.str]] = ..., datastores: Optional[Sequence[_builtins.str]] = ..., discovery_type: Optional[_builtins.str] = ..., disk_resized: Optional[_builtins.str] = ..., infrastructure_vm_id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., is_additional_stats_available: Optional[_builtins.bool] = ..., last_heartbeat: Optional[_builtins.str] = ..., last_rpo_calculated_time: Optional[_builtins.str] = ..., last_update_received_time: Optional[_builtins.str] = ..., master_target_id: Optional[_builtins.str] = ..., multi_vm_group_id: Optional[_builtins.str] = ..., multi_vm_group_name: Optional[_builtins.str] = ..., multi_vm_sync_status: Optional[_builtins.str] = ..., os_details: Optional[outputs.OSDiskDetailsResponse] = ..., os_version: Optional[_builtins.str] = ..., process_server_id: Optional[_builtins.str] = ..., protected_disks: Optional[Sequence[outputs.InMageProtectedDiskDetailsResponse]] = ..., protection_stage: Optional[_builtins.str] = ..., reboot_after_update_status: Optional[_builtins.str] = ..., replica_id: Optional[_builtins.str] = ..., resync_details: Optional[outputs.InitialReplicationDetailsResponse] = ..., retention_window_end: Optional[_builtins.str] = ..., retention_window_start: Optional[_builtins.str] = ..., rpo_in_seconds: Optional[_builtins.float] = ..., source_vm_cpu_count: Optional[_builtins.int] = ..., source_vm_ram_size_in_mb: Optional[_builtins.int] = ..., total_data_transferred: Optional[_builtins.float] = ..., total_progress_health: Optional[_builtins.str] = ..., uncompressed_data_rate_in_mb: Optional[_builtins.float] = ..., v_center_infrastructure_id: Optional[_builtins.str] = ..., validation_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., vm_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMNicDetailsResponse]] = ..., vm_protection_state: Optional[_builtins.str] = ..., vm_protection_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeSiteType")
    def active_site_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[outputs.InMageAgentDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageAccountId")
    def azure_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressedDataRateInMB")
    def compressed_data_rate_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consistencyPoints")
    def consistency_points(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastores(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskResized")
    def disk_resized(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureVmId")
    def infrastructure_vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAdditionalStatsAvailable")
    def is_additional_stats_available(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRpoCalculatedTime")
    def last_rpo_calculated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateReceivedTime")
    def last_update_received_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterTargetId")
    def master_target_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupId")
    def multi_vm_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmGroupName")
    def multi_vm_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiVmSyncStatus")
    def multi_vm_sync_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDetails")
    def os_details(self) -> Optional[outputs.OSDiskDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.InMageProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStage")
    def protection_stage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootAfterUpdateStatus")
    def reboot_after_update_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaId")
    def replica_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncDetails")
    def resync_details(self) -> Optional[outputs.InitialReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionWindowEnd")
    def retention_window_end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionWindowStart")
    def retention_window_start(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoInSeconds")
    def rpo_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmCpuCount")
    def source_vm_cpu_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmRamSizeInMB")
    def source_vm_ram_size_in_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDataTransferred")
    def total_data_transferred(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalProgressHealth")
    def total_progress_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uncompressedDataRateInMB")
    def uncompressed_data_rate_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterInfrastructureId")
    def v_center_infrastructure_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMNicDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionState")
    def vm_protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmProtectionStateDescription")
    def vm_protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InitialReplicationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_replication_progress_percentage: Optional[_builtins.str] = ..., initial_replication_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressPercentage")
    def initial_replication_progress_percentage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationType")
    def initial_replication_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InnerHealthErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_time_utc: Optional[_builtins.str] = ..., customer_resolvability: Optional[_builtins.str] = ..., entity_id: Optional[_builtins.str] = ..., error_category: Optional[_builtins.str] = ..., error_code: Optional[_builtins.str] = ..., error_id: Optional[_builtins.str] = ..., error_level: Optional[_builtins.str] = ..., error_message: Optional[_builtins.str] = ..., error_source: Optional[_builtins.str] = ..., error_type: Optional[_builtins.str] = ..., possible_causes: Optional[_builtins.str] = ..., recommended_action: Optional[_builtins.str] = ..., recovery_provider_error_message: Optional[_builtins.str] = ..., summary_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimeUtc")
    def creation_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerResolvability")
    def customer_resolvability(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCategory")
    def error_category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorId")
    def error_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorLevel")
    def error_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorSource")
    def error_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorType")
    def error_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryProviderErrorMessage")
    def recovery_provider_error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InputEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint_name: Optional[_builtins.str] = ..., private_port: Optional[_builtins.int] = ..., protocol: Optional[_builtins.str] = ..., public_port: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privatePort")
    def private_port(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class InquiryInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_detail: Optional[outputs.ErrorDetailResponse] = ..., inquiry_details: Optional[Sequence[outputs.WorkloadInquiryDetailsResponse]] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetail")
    def error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inquiryDetails")
    def inquiry_details(self) -> Optional[Sequence[outputs.WorkloadInquiryDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InquiryValidationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_detail: _builtins.str, protectable_item_count: Any, error_detail: Optional[outputs.ErrorDetailResponse] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalDetail")
    def additional_detail(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableItemCount")
    def protectable_item_count(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetail")
    def error_detail(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstantRPAdditionalDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_backup_rg_name_prefix: Optional[_builtins.str] = ..., azure_backup_rg_name_suffix: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNamePrefix")
    def azure_backup_rg_name_prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBackupRGNameSuffix")
    def azure_backup_rg_name_suffix(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class KPIResourceHealthDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_health_details: Optional[Sequence[outputs.ResourceHealthDetailsResponse]] = ..., resource_health_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceHealthDetails")
    def resource_health_details(self) -> Optional[Sequence[outputs.ResourceHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceHealthStatus")
    def resource_health_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogSchedulePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_policy_type: _builtins.str, schedule_frequency_in_mins: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleFrequencyInMins")
    def schedule_frequency_in_mins(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LongTermRetentionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_policy_type: _builtins.str, daily_schedule: Optional[outputs.DailyRetentionScheduleResponse] = ..., monthly_schedule: Optional[outputs.MonthlyRetentionScheduleResponse] = ..., weekly_schedule: Optional[outputs.WeeklyRetentionScheduleResponse] = ..., yearly_schedule: Optional[outputs.YearlyRetentionScheduleResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[outputs.DailyRetentionScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[outputs.MonthlyRetentionScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[outputs.WeeklyRetentionScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yearlySchedule")
    def yearly_schedule(self) -> Optional[outputs.YearlyRetentionScheduleResponse]:
        
        ...
    


@pulumi.output_type
class LongTermSchedulePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_policy_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MABContainerHealthDetailsResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ..., recommendations: Optional[Sequence[_builtins.str]] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MabContainerExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_item_type: Optional[_builtins.str] = ..., backup_items: Optional[Sequence[_builtins.str]] = ..., last_backup_status: Optional[_builtins.str] = ..., last_refreshed_at: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupItemType")
    def backup_item_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupItems")
    def backup_items(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MabContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_type: _builtins.str, agent_version: Optional[_builtins.str] = ..., backup_management_type: Optional[_builtins.str] = ..., can_re_register: Optional[_builtins.bool] = ..., container_health_state: Optional[_builtins.str] = ..., container_id: Optional[_builtins.float] = ..., extended_info: Optional[outputs.MabContainerExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., health_status: Optional[_builtins.str] = ..., mab_container_health_details: Optional[Sequence[outputs.MABContainerHealthDetailsResponse]] = ..., protectable_object_type: Optional[_builtins.str] = ..., protected_item_count: Optional[_builtins.float] = ..., registration_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canReRegister")
    def can_re_register(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerHealthState")
    def container_health_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.MabContainerExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mabContainerHealthDetails")
    def mab_container_health_details(self) -> Optional[Sequence[outputs.MABContainerHealthDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectType")
    def protectable_object_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationStatus")
    def registration_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MabFileFolderProtectedItemExtendedInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_refreshed_at: Optional[_builtins.str] = ..., oldest_recovery_point: Optional[_builtins.str] = ..., recovery_point_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshedAt")
    def last_refreshed_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oldestRecoveryPoint")
    def oldest_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointCount")
    def recovery_point_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MabFileFolderProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_item_type: _builtins.str, vault_id: _builtins.str, workload_type: _builtins.str, backup_set_name: Optional[_builtins.str] = ..., computer_name: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., create_mode: Optional[_builtins.str] = ..., deferred_delete_sync_time_in_utc: Optional[_builtins.float] = ..., deferred_delete_time_in_utc: Optional[_builtins.str] = ..., deferred_delete_time_remaining: Optional[_builtins.str] = ..., extended_info: Optional[outputs.MabFileFolderProtectedItemExtendedInfoResponse] = ..., friendly_name: Optional[_builtins.str] = ..., is_archive_enabled: Optional[_builtins.bool] = ..., is_deferred_delete_schedule_upcoming: Optional[_builtins.bool] = ..., is_rehydrate: Optional[_builtins.bool] = ..., is_scheduled_for_deferred_delete: Optional[_builtins.bool] = ..., last_backup_status: Optional[_builtins.str] = ..., last_backup_time: Optional[_builtins.str] = ..., last_recovery_point: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., source_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSetName")
    def backup_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteSyncTimeInUTC")
    def deferred_delete_sync_time_in_utc(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeInUTC")
    def deferred_delete_time_in_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deferredDeleteTimeRemaining")
    def deferred_delete_time_remaining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedInfo")
    def extended_info(self) -> Optional[outputs.MabFileFolderProtectedItemExtendedInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArchiveEnabled")
    def is_archive_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeferredDeleteScheduleUpcoming")
    def is_deferred_delete_schedule_upcoming(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRehydrate")
    def is_rehydrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isScheduledForDeferredDelete")
    def is_scheduled_for_deferred_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupStatus")
    def last_backup_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupTime")
    def last_backup_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPoint")
    def last_recovery_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MabProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_management_type: _builtins.str, protected_items_count: Optional[_builtins.int] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., retention_policy: Optional[Any] = ..., schedule_policy: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemsCount")
    def protected_items_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class MarsAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MasterTargetServerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_expiry_date: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., agent_version_details: Optional[outputs.VersionDetailsResponse] = ..., data_stores: Optional[Sequence[outputs.DataStoreResponse]] = ..., disk_count: Optional[_builtins.int] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., last_heartbeat: Optional[_builtins.str] = ..., mars_agent_expiry_date: Optional[_builtins.str] = ..., mars_agent_version: Optional[_builtins.str] = ..., mars_agent_version_details: Optional[outputs.VersionDetailsResponse] = ..., name: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., os_version: Optional[_builtins.str] = ..., retention_volumes: Optional[Sequence[outputs.RetentionVolumeResponse]] = ..., validation_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., version_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersionDetails")
    def agent_version_details(self) -> Optional[outputs.VersionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> Optional[Sequence[outputs.DataStoreResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskCount")
    def disk_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAgentExpiryDate")
    def mars_agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAgentVersion")
    def mars_agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAgentVersionDetails")
    def mars_agent_version_details(self) -> Optional[outputs.VersionDetailsResponse]:
        
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
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionVolumes")
    def retention_volumes(self) -> Optional[Sequence[outputs.RetentionVolumeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationItemPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_operations: Sequence[_builtins.str], critical_job_history: Sequence[outputs.CriticalJobHistoryDetailsResponse], current_job: outputs.CurrentJobDetailsResponse, event_correlation_id: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], last_migration_status: _builtins.str, last_migration_time: _builtins.str, last_test_migration_status: _builtins.str, last_test_migration_time: _builtins.str, machine_name: _builtins.str, migration_state: _builtins.str, migration_state_description: _builtins.str, policy_friendly_name: _builtins.str, policy_id: _builtins.str, recovery_services_provider_id: _builtins.str, replication_status: _builtins.str, test_migrate_state: _builtins.str, test_migrate_state_description: _builtins.str, provider_specific_details: Optional[outputs.VMwareCbtMigrationDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="criticalJobHistory")
    def critical_job_history(self) -> Sequence[outputs.CriticalJobHistoryDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentJob")
    def current_job(self) -> outputs.CurrentJobDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventCorrelationId")
    def event_correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastMigrationStatus")
    def last_migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastMigrationTime")
    def last_migration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestMigrationStatus")
    def last_test_migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestMigrationTime")
    def last_test_migration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStateDescription")
    def migration_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFriendlyName")
    def policy_friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryServicesProviderId")
    def recovery_services_provider_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrateState")
    def test_migrate_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrateStateDescription")
    def test_migrate_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[outputs.VMwareCbtMigrationDetailsResponse]:
        
        ...
    


@pulumi.output_type
class MobilityServiceUpdateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_type: Optional[_builtins.str] = ..., reboot_status: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootStatus")
    def reboot_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitoringSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_monitor_alert_settings: Optional[outputs.AzureMonitorAlertSettingsResponse] = ..., classic_alert_settings: Optional[outputs.ClassicAlertSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureMonitorAlertSettings")
    def azure_monitor_alert_settings(self) -> Optional[outputs.AzureMonitorAlertSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classicAlertSettings")
    def classic_alert_settings(self) -> Optional[outputs.ClassicAlertSettingsResponse]:
        
        ...
    


@pulumi.output_type
class MonthlyRetentionScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_duration: Optional[outputs.RetentionDurationResponse] = ..., retention_schedule_daily: Optional[outputs.DailyRetentionFormatResponse] = ..., retention_schedule_format_type: Optional[_builtins.str] = ..., retention_schedule_weekly: Optional[outputs.WeeklyRetentionFormatResponse] = ..., retention_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(self) -> Optional[outputs.DailyRetentionFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(self) -> Optional[outputs.WeeklyRetentionFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class NetworkMappingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fabric_specific_settings: Optional[Any] = ..., primary_fabric_friendly_name: Optional[_builtins.str] = ..., primary_network_friendly_name: Optional[_builtins.str] = ..., primary_network_id: Optional[_builtins.str] = ..., recovery_fabric_arm_id: Optional[_builtins.str] = ..., recovery_fabric_friendly_name: Optional[_builtins.str] = ..., recovery_network_friendly_name: Optional[_builtins.str] = ..., recovery_network_id: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricSpecificSettings")
    def fabric_specific_settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricFriendlyName")
    def primary_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkFriendlyName")
    def primary_network_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkId")
    def primary_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricArmId")
    def recovery_fabric_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricFriendlyName")
    def recovery_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryNetworkFriendlyName")
    def recovery_network_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryNetworkId")
    def recovery_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, o_s_major_version: Optional[_builtins.str] = ..., o_s_minor_version: Optional[_builtins.str] = ..., o_s_version: Optional[_builtins.str] = ..., os_edition: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., product_type: Optional[_builtins.str] = ..., user_selected_os_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oSMajorVersion")
    def o_s_major_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oSMinorVersion")
    def o_s_minor_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oSVersion")
    def o_s_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osEdition")
    def os_edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSelectedOSName")
    def user_selected_os_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_type: Optional[_builtins.str] = ..., os_vhd_id: Optional[_builtins.str] = ..., vhd_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVhdId")
    def os_vhd_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdName")
    def vhd_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSUpgradeSupportedVersionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, supported_source_os_version: _builtins.str, supported_target_os_versions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedSourceOsVersion")
    def supported_source_os_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedTargetOsVersions")
    def supported_target_os_versions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, friendly_name: Optional[_builtins.str] = ..., provider_specific_details: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ..., provisioning_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionVaultPropertiesResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, location: _builtins.str, name: _builtins.str, properties: outputs.VaultPrivateEndpointConnectionResponse, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.VaultPrivateEndpointConnectionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponseV1(dict):
    
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
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProcessServerDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, available_memory_in_bytes: _builtins.float, available_space_in_bytes: _builtins.float, bios_id: _builtins.str, disk_usage_status: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, free_space_percentage: _builtins.float, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], historic_health: _builtins.str, id: _builtins.str, ip_addresses: Sequence[_builtins.str], last_heartbeat_utc: _builtins.str, memory_usage_percentage: _builtins.float, memory_usage_status: _builtins.str, name: _builtins.str, processor_usage_percentage: _builtins.float, processor_usage_status: _builtins.str, protected_item_count: _builtins.int, system_load: _builtins.float, system_load_status: _builtins.str, throughput_in_bytes: _builtins.float, throughput_status: _builtins.str, throughput_upload_pending_data_in_bytes: _builtins.float, total_memory_in_bytes: _builtins.float, total_space_in_bytes: _builtins.float, used_memory_in_bytes: _builtins.float, used_space_in_bytes: _builtins.float, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryInBytes")
    def available_memory_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSpaceInBytes")
    def available_space_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskUsageStatus")
    def disk_usage_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeSpacePercentage")
    def free_space_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="historicHealth")
    def historic_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryUsagePercentage")
    def memory_usage_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryUsageStatus")
    def memory_usage_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processorUsagePercentage")
    def processor_usage_percentage(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processorUsageStatus")
    def processor_usage_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoad")
    def system_load(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoadStatus")
    def system_load_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputInBytes")
    def throughput_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputStatus")
    def throughput_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputUploadPendingDataInBytes")
    def throughput_upload_pending_data_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMemoryInBytes")
    def total_memory_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSpaceInBytes")
    def total_space_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedMemoryInBytes")
    def used_memory_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedSpaceInBytes")
    def used_space_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProcessServerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, health: _builtins.str, mars_communication_status: _builtins.str, mars_registration_status: _builtins.str, ps_stats_refresh_time: _builtins.str, throughput_in_bytes: _builtins.float, throughput_in_m_bps: _builtins.float, throughput_status: _builtins.str, throughput_upload_pending_data_in_bytes: _builtins.float, agent_expiry_date: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., agent_version_details: Optional[outputs.VersionDetailsResponse] = ..., available_memory_in_bytes: Optional[_builtins.float] = ..., available_space_in_bytes: Optional[_builtins.float] = ..., cpu_load: Optional[_builtins.str] = ..., cpu_load_status: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., host_id: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., last_heartbeat: Optional[_builtins.str] = ..., machine_count: Optional[_builtins.str] = ..., memory_usage_status: Optional[_builtins.str] = ..., mobility_service_updates: Optional[Sequence[outputs.MobilityServiceUpdateResponse]] = ..., os_type: Optional[_builtins.str] = ..., os_version: Optional[_builtins.str] = ..., ps_service_status: Optional[_builtins.str] = ..., replication_pair_count: Optional[_builtins.str] = ..., space_usage_status: Optional[_builtins.str] = ..., ssl_cert_expiry_date: Optional[_builtins.str] = ..., ssl_cert_expiry_remaining_days: Optional[_builtins.int] = ..., system_load: Optional[_builtins.str] = ..., system_load_status: Optional[_builtins.str] = ..., total_memory_in_bytes: Optional[_builtins.float] = ..., total_space_in_bytes: Optional[_builtins.float] = ..., version_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsCommunicationStatus")
    def mars_communication_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsRegistrationStatus")
    def mars_registration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psStatsRefreshTime")
    def ps_stats_refresh_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputInBytes")
    def throughput_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputInMBps")
    def throughput_in_m_bps(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputStatus")
    def throughput_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputUploadPendingDataInBytes")
    def throughput_upload_pending_data_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersionDetails")
    def agent_version_details(self) -> Optional[outputs.VersionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryInBytes")
    def available_memory_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSpaceInBytes")
    def available_space_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLoad")
    def cpu_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLoadStatus")
    def cpu_load_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineCount")
    def machine_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryUsageStatus")
    def memory_usage_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mobilityServiceUpdates")
    def mobility_service_updates(self) -> Optional[Sequence[outputs.MobilityServiceUpdateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psServiceStatus")
    def ps_service_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPairCount")
    def replication_pair_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceUsageStatus")
    def space_usage_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertExpiryDate")
    def ssl_cert_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertExpiryRemainingDays")
    def ssl_cert_expiry_remaining_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoad")
    def system_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoadStatus")
    def system_load_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMemoryInBytes")
    def total_memory_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSpaceInBytes")
    def total_space_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProtectionContainerMappingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, health: Optional[_builtins.str] = ..., health_error_details: Optional[Sequence[outputs.HealthErrorResponse]] = ..., policy_friendly_name: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., provider_specific_details: Optional[Any] = ..., source_fabric_friendly_name: Optional[_builtins.str] = ..., source_protection_container_friendly_name: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., target_fabric_friendly_name: Optional[_builtins.str] = ..., target_protection_container_friendly_name: Optional[_builtins.str] = ..., target_protection_container_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrorDetails")
    def health_error_details(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFriendlyName")
    def policy_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFabricFriendlyName")
    def source_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProtectionContainerFriendlyName")
    def source_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFabricFriendlyName")
    def target_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProtectionContainerFriendlyName")
    def target_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProtectionContainerId")
    def target_protection_container_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PushInstallerDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RcmProxyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, client_authentication_type: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthenticationType")
    def client_authentication_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RecoveryPlanA2ADetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, primary_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., primary_zone: Optional[_builtins.str] = ..., recovery_extended_location: Optional[outputs.ExtendedLocationResponse] = ..., recovery_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryExtendedLocation")
    def primary_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryZone")
    def primary_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryExtendedLocation")
    def recovery_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryZone")
    def recovery_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanActionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_name: _builtins.str, custom_details: Any, failover_directions: Sequence[_builtins.str], failover_types: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDetails")
    def custom_details(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDirections")
    def failover_directions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverTypes")
    def failover_types(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanAutomationRunbookActionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fabric_location: _builtins.str, instance_type: _builtins.str, runbook_id: Optional[_builtins.str] = ..., timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricLocation")
    def fabric_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runbookId")
    def runbook_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanGroupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_type: _builtins.str, end_group_actions: Optional[Sequence[outputs.RecoveryPlanActionResponse]] = ..., replication_protected_items: Optional[Sequence[outputs.RecoveryPlanProtectedItemResponse]] = ..., start_group_actions: Optional[Sequence[outputs.RecoveryPlanActionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endGroupActions")
    def end_group_actions(self) -> Optional[Sequence[outputs.RecoveryPlanActionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationProtectedItems")
    def replication_protected_items(self) -> Optional[Sequence[outputs.RecoveryPlanProtectedItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startGroupActions")
    def start_group_actions(self) -> Optional[Sequence[outputs.RecoveryPlanActionResponse]]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanManualActionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_operations: Optional[Sequence[_builtins.str]] = ..., current_scenario: Optional[outputs.CurrentScenarioDetailsResponse] = ..., current_scenario_status: Optional[_builtins.str] = ..., current_scenario_status_description: Optional[_builtins.str] = ..., failover_deployment_model: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., groups: Optional[Sequence[outputs.RecoveryPlanGroupResponse]] = ..., last_planned_failover_time: Optional[_builtins.str] = ..., last_test_failover_time: Optional[_builtins.str] = ..., last_unplanned_failover_time: Optional[_builtins.str] = ..., primary_fabric_friendly_name: Optional[_builtins.str] = ..., primary_fabric_id: Optional[_builtins.str] = ..., provider_specific_details: Optional[Sequence[outputs.RecoveryPlanA2ADetailsResponse]] = ..., recovery_fabric_friendly_name: Optional[_builtins.str] = ..., recovery_fabric_id: Optional[_builtins.str] = ..., replication_providers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(self) -> Optional[outputs.CurrentScenarioDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenarioStatus")
    def current_scenario_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenarioStatusDescription")
    def current_scenario_status_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDeploymentModel")
    def failover_deployment_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[outputs.RecoveryPlanGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPlannedFailoverTime")
    def last_planned_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestFailoverTime")
    def last_test_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUnplannedFailoverTime")
    def last_unplanned_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricFriendlyName")
    def primary_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricId")
    def primary_fabric_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[Sequence[outputs.RecoveryPlanA2ADetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricFriendlyName")
    def recovery_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricId")
    def recovery_fabric_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationProviders")
    def replication_providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanProtectedItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., virtual_machine_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryPlanScriptActionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fabric_location: _builtins.str, instance_type: _builtins.str, path: _builtins.str, timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricLocation")
    def fabric_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecoveryServicesProviderPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_scenarios: Optional[Sequence[_builtins.str]] = ..., authentication_identity_details: Optional[outputs.IdentityProviderDetailsResponse] = ..., bios_id: Optional[_builtins.str] = ..., connection_status: Optional[_builtins.str] = ..., data_plane_authentication_identity_details: Optional[outputs.IdentityProviderDetailsResponse] = ..., dra_identifier: Optional[_builtins.str] = ..., fabric_friendly_name: Optional[_builtins.str] = ..., fabric_type: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_error_details: Optional[Sequence[outputs.HealthErrorResponse]] = ..., last_heart_beat: Optional[_builtins.str] = ..., machine_id: Optional[_builtins.str] = ..., machine_name: Optional[_builtins.str] = ..., protected_item_count: Optional[_builtins.int] = ..., provider_version: Optional[_builtins.str] = ..., provider_version_details: Optional[outputs.VersionDetailsResponse] = ..., provider_version_expiry_date: Optional[_builtins.str] = ..., provider_version_state: Optional[_builtins.str] = ..., resource_access_identity_details: Optional[outputs.IdentityProviderDetailsResponse] = ..., server_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedScenarios")
    def allowed_scenarios(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationIdentityDetails")
    def authentication_identity_details(self) -> Optional[outputs.IdentityProviderDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPlaneAuthenticationIdentityDetails")
    def data_plane_authentication_identity_details(self) -> Optional[outputs.IdentityProviderDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="draIdentifier")
    def dra_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricFriendlyName")
    def fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricType")
    def fabric_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrorDetails")
    def health_error_details(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartBeat")
    def last_heart_beat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerVersion")
    def provider_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerVersionDetails")
    def provider_version_details(self) -> Optional[outputs.VersionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerVersionExpiryDate")
    def provider_version_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerVersionState")
    def provider_version_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentityDetails")
    def resource_access_identity_details(self) -> Optional[outputs.IdentityProviderDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegisteredClusterNodesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: Optional[_builtins.str] = ..., cluster_node_fqdn: Optional[_builtins.str] = ..., is_shared_disk_virtual_node: Optional[_builtins.bool] = ..., machine_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNodeFqdn")
    def cluster_node_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedDiskVirtualNode")
    def is_shared_disk_virtual_node(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReplicationAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ReplicationProtectedItemPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_location: Optional[_builtins.str] = ..., allowed_operations: Optional[Sequence[_builtins.str]] = ..., current_scenario: Optional[outputs.CurrentScenarioDetailsResponse] = ..., event_correlation_id: Optional[_builtins.str] = ..., failover_health: Optional[_builtins.str] = ..., failover_recovery_point_id: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., last_successful_failover_time: Optional[_builtins.str] = ..., last_successful_test_failover_time: Optional[_builtins.str] = ..., policy_friendly_name: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., primary_fabric_friendly_name: Optional[_builtins.str] = ..., primary_fabric_provider: Optional[_builtins.str] = ..., primary_protection_container_friendly_name: Optional[_builtins.str] = ..., protectable_item_id: Optional[_builtins.str] = ..., protected_item_type: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_state_description: Optional[_builtins.str] = ..., provider_specific_details: Optional[Any] = ..., recovery_container_id: Optional[_builtins.str] = ..., recovery_fabric_friendly_name: Optional[_builtins.str] = ..., recovery_fabric_id: Optional[_builtins.str] = ..., recovery_protection_container_friendly_name: Optional[_builtins.str] = ..., recovery_services_provider_id: Optional[_builtins.str] = ..., replication_health: Optional[_builtins.str] = ..., switch_provider_state: Optional[_builtins.str] = ..., switch_provider_state_description: Optional[_builtins.str] = ..., test_failover_state: Optional[_builtins.str] = ..., test_failover_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(self) -> Optional[outputs.CurrentScenarioDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventCorrelationId")
    def event_correlation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverHealth")
    def failover_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulFailoverTime")
    def last_successful_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulTestFailoverTime")
    def last_successful_test_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFriendlyName")
    def policy_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricFriendlyName")
    def primary_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricProvider")
    def primary_fabric_provider(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryProtectionContainerFriendlyName")
    def primary_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableItemId")
    def protectable_item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemType")
    def protected_item_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStateDescription")
    def protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryContainerId")
    def recovery_container_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricFriendlyName")
    def recovery_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricId")
    def recovery_fabric_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryProtectionContainerFriendlyName")
    def recovery_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryServicesProviderId")
    def recovery_services_provider_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchProviderState")
    def switch_provider_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchProviderStateDescription")
    def switch_provider_state_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverStateDescription")
    def test_failover_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReplicationProtectionClusterPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, active_location: Optional[_builtins.str] = ..., agent_cluster_id: Optional[_builtins.str] = ..., allowed_operations: Optional[Sequence[_builtins.str]] = ..., are_all_cluster_nodes_registered: Optional[_builtins.bool] = ..., cluster_fqdn: Optional[_builtins.str] = ..., cluster_node_fqdns: Optional[Sequence[_builtins.str]] = ..., cluster_protected_item_ids: Optional[Sequence[_builtins.str]] = ..., cluster_registered_nodes: Optional[Sequence[outputs.RegisteredClusterNodesResponse]] = ..., current_scenario: Optional[outputs.CurrentScenarioDetailsResponse] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., last_successful_failover_time: Optional[_builtins.str] = ..., last_successful_test_failover_time: Optional[_builtins.str] = ..., policy_friendly_name: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., primary_fabric_friendly_name: Optional[_builtins.str] = ..., primary_fabric_provider: Optional[_builtins.str] = ..., primary_protection_container_friendly_name: Optional[_builtins.str] = ..., protection_cluster_type: Optional[_builtins.str] = ..., protection_state: Optional[_builtins.str] = ..., protection_state_description: Optional[_builtins.str] = ..., provider_specific_details: Optional[outputs.A2AReplicationProtectionClusterDetailsResponse] = ..., recovery_container_id: Optional[_builtins.str] = ..., recovery_fabric_friendly_name: Optional[_builtins.str] = ..., recovery_fabric_id: Optional[_builtins.str] = ..., recovery_protection_container_friendly_name: Optional[_builtins.str] = ..., replication_health: Optional[_builtins.str] = ..., shared_disk_properties: Optional[outputs.SharedDiskReplicationItemPropertiesResponse] = ..., test_failover_state: Optional[_builtins.str] = ..., test_failover_state_description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentClusterId")
    def agent_cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="areAllClusterNodesRegistered")
    def are_all_cluster_nodes_registered(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterFqdn")
    def cluster_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNodeFqdns")
    def cluster_node_fqdns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterProtectedItemIds")
    def cluster_protected_item_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterRegisteredNodes")
    def cluster_registered_nodes(self) -> Optional[Sequence[outputs.RegisteredClusterNodesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(self) -> Optional[outputs.CurrentScenarioDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulFailoverTime")
    def last_successful_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulTestFailoverTime")
    def last_successful_test_failover_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyFriendlyName")
    def policy_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricFriendlyName")
    def primary_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryFabricProvider")
    def primary_fabric_provider(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryProtectionContainerFriendlyName")
    def primary_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionClusterType")
    def protection_cluster_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStateDescription")
    def protection_state_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSpecificDetails")
    def provider_specific_details(self) -> Optional[outputs.A2AReplicationProtectionClusterDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryContainerId")
    def recovery_container_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricFriendlyName")
    def recovery_fabric_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryFabricId")
    def recovery_fabric_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryProtectionContainerFriendlyName")
    def recovery_protection_container_friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedDiskProperties")
    def shared_disk_properties(self) -> Optional[outputs.SharedDiskReplicationItemPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverStateDescription")
    def test_failover_state_description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReprotectAgentDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accessible_datastores: Sequence[_builtins.str], bios_id: _builtins.str, fabric_object_id: _builtins.str, fqdn: _builtins.str, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorResponse], id: _builtins.str, last_discovery_in_utc: _builtins.str, last_heartbeat_utc: _builtins.str, name: _builtins.str, protected_item_count: _builtins.int, vcenter_id: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessibleDatastores")
    def accessible_datastores(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDiscoveryInUtc")
    def last_discovery_in_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedItemCount")
    def protected_item_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterId")
    def vcenter_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResourceGuardOperationDetailResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_resource_request: Optional[_builtins.str] = ..., vault_critical_operation: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceRequest")
    def default_resource_request(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultCriticalOperation")
    def vault_critical_operation(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ResourceGuardProxyBaseResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_guard_resource_id: _builtins.str, description: Optional[_builtins.str] = ..., last_updated_time: Optional[_builtins.str] = ..., resource_guard_operation_details: Optional[Sequence[outputs.ResourceGuardOperationDetailResponse]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardResourceId")
    def resource_guard_resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationDetails")
    def resource_guard_operation_details(self) -> Optional[Sequence[outputs.ResourceGuardOperationDetailResponse]]:
        ...
    


@pulumi.output_type
class ResourceHealthDetailsResponse(dict):
    
    def __init__(__self__, *, code: _builtins.int, message: _builtins.str, recommendations: Sequence[_builtins.str], title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RestoreSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cross_subscription_restore_settings: Optional[outputs.CrossSubscriptionRestoreSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionRestoreSettings")
    def cross_subscription_restore_settings(self) -> Optional[outputs.CrossSubscriptionRestoreSettingsResponse]:
        
        ...
    


@pulumi.output_type
class RetentionDurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., duration_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RetentionVolumeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: Optional[_builtins.float] = ..., free_space_in_bytes: Optional[_builtins.float] = ..., threshold_percentage: Optional[_builtins.int] = ..., volume_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeSpaceInBytes")
    def free_space_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdPercentage")
    def threshold_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RunAsAccountResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_id: Optional[_builtins.str] = ..., account_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityProfilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_vm_confidential_encryption: Optional[_builtins.str] = ..., target_vm_monitoring: Optional[_builtins.str] = ..., target_vm_secure_boot: Optional[_builtins.str] = ..., target_vm_security_type: Optional[_builtins.str] = ..., target_vm_tpm: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmConfidentialEncryption")
    def target_vm_confidential_encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmMonitoring")
    def target_vm_monitoring(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecureBoot")
    def target_vm_secure_boot(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityType")
    def target_vm_security_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmTpm")
    def target_vm_tpm(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecuritySettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, multi_user_authorization: _builtins.str, immutability_settings: Optional[outputs.ImmutabilitySettingsResponse] = ..., soft_delete_settings: Optional[outputs.SoftDeleteSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiUserAuthorization")
    def multi_user_authorization(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutabilitySettings")
    def immutability_settings(self) -> Optional[outputs.ImmutabilitySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteSettings")
    def soft_delete_settings(self) -> Optional[outputs.SoftDeleteSettingsResponse]:
        
        ...
    


@pulumi.output_type
class SettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_compression: Optional[_builtins.bool] = ..., issqlcompression: Optional[_builtins.bool] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCompression")
    def is_compression(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issqlcompression(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SharedDiskReplicationItemPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_location: Optional[_builtins.str] = ..., allowed_operations: Optional[Sequence[_builtins.str]] = ..., current_scenario: Optional[outputs.CurrentScenarioDetailsResponse] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., protection_state: Optional[_builtins.str] = ..., replication_health: Optional[_builtins.str] = ..., shared_disk_provider_specific_details: Optional[outputs.A2ASharedDiskReplicationDetailsResponse] = ..., test_failover_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOperations")
    def allowed_operations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentScenario")
    def current_scenario(self) -> Optional[outputs.CurrentScenarioDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedDiskProviderSpecificDetails")
    def shared_disk_provider_specific_details(self) -> Optional[outputs.A2ASharedDiskReplicationDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SimpleRetentionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_policy_type: _builtins.str, retention_duration: Optional[outputs.RetentionDurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicyType")
    def retention_policy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]:
        
        ...
    


@pulumi.output_type
class SimpleSchedulePolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_policy_type: _builtins.str, hourly_schedule: Optional[outputs.HourlyScheduleResponse] = ..., schedule_run_days: Optional[Sequence[_builtins.str]] = ..., schedule_run_frequency: Optional[_builtins.str] = ..., schedule_run_times: Optional[Sequence[_builtins.str]] = ..., schedule_weekly_frequency: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[outputs.HourlyScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleWeeklyFrequency")
    def schedule_weekly_frequency(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SimpleSchedulePolicyV2Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_policy_type: _builtins.str, daily_schedule: Optional[outputs.DailyScheduleResponse] = ..., hourly_schedule: Optional[outputs.HourlyScheduleResponse] = ..., schedule_run_frequency: Optional[_builtins.str] = ..., weekly_schedule: Optional[outputs.WeeklyScheduleResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicyType")
    def schedule_policy_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[outputs.DailyScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[outputs.HourlyScheduleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunFrequency")
    def schedule_run_frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[outputs.WeeklyScheduleResponse]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.str] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SnapshotBackupAdditionalDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instant_rp_details: Optional[_builtins.str] = ..., instant_rp_retention_range_in_days: Optional[_builtins.int] = ..., user_assigned_managed_identity_details: Optional[outputs.UserAssignedManagedIdentityDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instantRPDetails")
    def instant_rp_details(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedManagedIdentityDetails")
    def user_assigned_managed_identity_details(self) -> Optional[outputs.UserAssignedManagedIdentityDetailsResponse]:
        
        ...
    


@pulumi.output_type
class SoftDeleteSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enhanced_security_state: Optional[_builtins.str] = ..., soft_delete_retention_period_in_days: Optional[_builtins.int] = ..., soft_delete_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityState")
    def enhanced_security_state(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionPeriodInDays")
    def soft_delete_retention_period_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteState")
    def soft_delete_state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class StorageClassificationMappingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_storage_classification_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStorageClassificationId")
    def target_storage_classification_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubProtectionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_type: Optional[_builtins.str] = ..., retention_policy: Optional[Any] = ..., schedule_policy: Optional[Any] = ..., snapshot_backup_additional_details: Optional[outputs.SnapshotBackupAdditionalDetailsResponse] = ..., tiering_policy: Optional[Mapping[str, outputs.TieringPolicyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotBackupAdditionalDetails")
    def snapshot_backup_additional_details(self) -> Optional[outputs.SnapshotBackupAdditionalDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[Mapping[str, outputs.TieringPolicyResponse]]:
        
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
class TieringPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration: Optional[_builtins.int] = ..., duration_type: Optional[_builtins.str] = ..., tiering_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationType")
    def duration_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringMode")
    def tiering_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UpgradeDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time_utc: _builtins.str, last_updated_time_utc: _builtins.str, message: _builtins.str, operation_id: _builtins.str, previous_resource_id: _builtins.str, start_time_utc: _builtins.str, status: _builtins.str, trigger_type: _builtins.str, upgraded_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previousResourceId")
    def previous_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradedResourceId")
    def upgraded_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAssignedManagedIdentityDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_arm_id: Optional[_builtins.str] = ..., identity_name: Optional[_builtins.str] = ..., user_assigned_identity_properties: Optional[outputs.UserAssignedIdentityPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityArmId")
    def identity_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityName")
    def identity_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityProperties")
    def user_assigned_identity_properties(self) -> Optional[outputs.UserAssignedIdentityPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class UserCreatedResourceTagResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tag_name: Optional[_builtins.str] = ..., tag_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserIdentityResponse(dict):
    
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
class VCenterPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, discovery_status: Optional[_builtins.str] = ..., fabric_arm_resource_name: Optional[_builtins.str] = ..., friendly_name: Optional[_builtins.str] = ..., health_errors: Optional[Sequence[outputs.HealthErrorResponse]] = ..., infrastructure_id: Optional[_builtins.str] = ..., internal_id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., last_heartbeat: Optional[_builtins.str] = ..., port: Optional[_builtins.str] = ..., process_server_id: Optional[_builtins.str] = ..., run_as_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryStatus")
    def discovery_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricArmResourceName")
    def fabric_arm_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Optional[Sequence[outputs.HealthErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureId")
    def infrastructure_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerId")
    def process_server_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMNicDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_accelerated_networking_on_recovery: Optional[_builtins.bool] = ..., enable_accelerated_networking_on_tfo: Optional[_builtins.bool] = ..., ip_configs: Optional[Sequence[outputs.IPConfigDetailsResponse]] = ..., nic_id: Optional[_builtins.str] = ..., recovery_network_security_group_id: Optional[_builtins.str] = ..., recovery_nic_name: Optional[_builtins.str] = ..., recovery_nic_resource_group_name: Optional[_builtins.str] = ..., recovery_vm_network_id: Optional[_builtins.str] = ..., replica_nic_id: Optional[_builtins.str] = ..., reuse_existing_nic: Optional[_builtins.bool] = ..., selection_type: Optional[_builtins.str] = ..., source_nic_arm_id: Optional[_builtins.str] = ..., target_nic_name: Optional[_builtins.str] = ..., tfo_network_security_group_id: Optional[_builtins.str] = ..., tfo_recovery_nic_name: Optional[_builtins.str] = ..., tfo_recovery_nic_resource_group_name: Optional[_builtins.str] = ..., tfo_reuse_existing_nic: Optional[_builtins.bool] = ..., tfo_vm_network_id: Optional[_builtins.str] = ..., v_m_network_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworkingOnRecovery")
    def enable_accelerated_networking_on_recovery(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworkingOnTfo")
    def enable_accelerated_networking_on_tfo(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(self) -> Optional[Sequence[outputs.IPConfigDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryNetworkSecurityGroupId")
    def recovery_network_security_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryNicName")
    def recovery_nic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryNicResourceGroupName")
    def recovery_nic_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryVMNetworkId")
    def recovery_vm_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNicId")
    def replica_nic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseExistingNic")
    def reuse_existing_nic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionType")
    def selection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceNicArmId")
    def source_nic_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicName")
    def target_nic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoNetworkSecurityGroupId")
    def tfo_network_security_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoRecoveryNicName")
    def tfo_recovery_nic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoRecoveryNicResourceGroupName")
    def tfo_recovery_nic_resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoReuseExistingNic")
    def tfo_reuse_existing_nic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tfoVMNetworkId")
    def tfo_vm_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vMNetworkName")
    def v_m_network_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareCbtMigrationDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, appliance_monitoring_details: outputs.ApplianceMonitoringDetailsResponse, data_mover_run_as_account_id: _builtins.str, delta_sync_progress_percentage: _builtins.int, delta_sync_retry_count: _builtins.float, firmware_type: _builtins.str, gateway_operation_details: outputs.GatewayOperationDetailsResponse, initial_seeding_progress_percentage: _builtins.int, initial_seeding_retry_count: _builtins.float, instance_type: _builtins.str, is_check_sum_resync_cycle: _builtins.str, last_recovery_point_id: _builtins.str, last_recovery_point_received: _builtins.str, migration_progress_percentage: _builtins.int, migration_recovery_point_id: _builtins.str, operation_name: _builtins.str, os_name: _builtins.str, os_type: _builtins.str, resume_progress_percentage: _builtins.int, resume_retry_count: _builtins.float, resync_progress_percentage: _builtins.int, resync_required: _builtins.str, resync_retry_count: _builtins.float, resync_state: _builtins.str, snapshot_run_as_account_id: _builtins.str, storage_account_id: _builtins.str, target_generation: _builtins.str, target_location: _builtins.str, vmware_machine_id: _builtins.str, confidential_vm_key_vault_id: Optional[_builtins.str] = ..., license_type: Optional[_builtins.str] = ..., linux_license_type: Optional[_builtins.str] = ..., perform_auto_resync: Optional[_builtins.str] = ..., protected_disks: Optional[Sequence[outputs.VMwareCbtProtectedDiskDetailsResponse]] = ..., seed_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., sql_server_license_type: Optional[_builtins.str] = ..., supported_os_versions: Optional[Sequence[_builtins.str]] = ..., target_availability_set_id: Optional[_builtins.str] = ..., target_availability_zone: Optional[_builtins.str] = ..., target_boot_diagnostics_storage_account_id: Optional[_builtins.str] = ..., target_disk_tags: Optional[Mapping[str, _builtins.str]] = ..., target_network_id: Optional[_builtins.str] = ..., target_nic_tags: Optional[Mapping[str, _builtins.str]] = ..., target_proximity_placement_group_id: Optional[_builtins.str] = ..., target_resource_group_id: Optional[_builtins.str] = ..., target_vm_name: Optional[_builtins.str] = ..., target_vm_security_profile: Optional[outputs.VMwareCbtSecurityProfilePropertiesResponse] = ..., target_vm_size: Optional[_builtins.str] = ..., target_vm_tags: Optional[Mapping[str, _builtins.str]] = ..., test_network_id: Optional[_builtins.str] = ..., vm_nics: Optional[Sequence[outputs.VMwareCbtNicDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceMonitoringDetails")
    def appliance_monitoring_details(self) -> outputs.ApplianceMonitoringDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataMoverRunAsAccountId")
    def data_mover_run_as_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaSyncProgressPercentage")
    def delta_sync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaSyncRetryCount")
    def delta_sync_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayOperationDetails")
    def gateway_operation_details(self) -> outputs.GatewayOperationDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialSeedingProgressPercentage")
    def initial_seeding_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialSeedingRetryCount")
    def initial_seeding_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCheckSumResyncCycle")
    def is_check_sum_resync_cycle(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointId")
    def last_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationProgressPercentage")
    def migration_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationRecoveryPointId")
    def migration_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resumeProgressPercentage")
    def resume_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resumeRetryCount")
    def resume_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRetryCount")
    def resync_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncState")
    def resync_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRunAsAccountId")
    def snapshot_run_as_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGeneration")
    def target_generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareMachineId")
    def vmware_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialVmKeyVaultId")
    def confidential_vm_key_vault_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxLicenseType")
    def linux_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performAutoResync")
    def perform_auto_resync(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Optional[Sequence[outputs.VMwareCbtProtectedDiskDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedDiskTags")
    def seed_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSVersions")
    def supported_os_versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAvailabilityZone")
    def target_availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBootDiagnosticsStorageAccountId")
    def target_boot_diagnostics_storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskTags")
    def target_disk_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicTags")
    def target_nic_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetProximityPlacementGroupId")
    def target_proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityProfile")
    def target_vm_security_profile(self) -> Optional[outputs.VMwareCbtSecurityProfilePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSize")
    def target_vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmTags")
    def target_vm_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmNics")
    def vm_nics(self) -> Optional[Sequence[outputs.VMwareCbtNicDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class VMwareCbtNicDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, nic_id: _builtins.str, source_ip_address: _builtins.str, source_ip_address_type: _builtins.str, source_network_id: _builtins.str, is_primary_nic: Optional[_builtins.str] = ..., is_selected_for_migration: Optional[_builtins.str] = ..., target_ip_address: Optional[_builtins.str] = ..., target_ip_address_type: Optional[_builtins.str] = ..., target_nic_name: Optional[_builtins.str] = ..., target_subnet_name: Optional[_builtins.str] = ..., test_ip_address: Optional[_builtins.str] = ..., test_ip_address_type: Optional[_builtins.str] = ..., test_network_id: Optional[_builtins.str] = ..., test_subnet_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIPAddress")
    def source_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIPAddressType")
    def source_ip_address_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceNetworkId")
    def source_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimaryNic")
    def is_primary_nic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSelectedForMigration")
    def is_selected_for_migration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIPAddress")
    def target_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIPAddressType")
    def target_ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNicName")
    def target_nic_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSubnetName")
    def target_subnet_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testIPAddress")
    def test_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testIPAddressType")
    def test_ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testSubnetName")
    def test_subnet_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareCbtProtectedDiskDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, disk_encryption_set_id: _builtins.str, disk_id: _builtins.str, disk_name: _builtins.str, disk_path: _builtins.str, gateway_operation_details: outputs.GatewayOperationDetailsResponse, is_os_disk: _builtins.str, log_storage_account_id: _builtins.str, log_storage_account_sas_secret_name: _builtins.str, seed_blob_uri: _builtins.str, seed_managed_disk_id: _builtins.str, target_blob_uri: _builtins.str, target_managed_disk_id: _builtins.str, disk_type: Optional[_builtins.str] = ..., sector_size_in_bytes: Optional[_builtins.int] = ..., target_disk_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayOperationDetails")
    def gateway_operation_details(self) -> outputs.GatewayOperationDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOSDisk")
    def is_os_disk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStorageAccountId")
    def log_storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStorageAccountSasSecretName")
    def log_storage_account_sas_secret_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedBlobUri")
    def seed_blob_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedManagedDiskId")
    def seed_managed_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBlobUri")
    def target_blob_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetManagedDiskId")
    def target_managed_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sectorSizeInBytes")
    def sector_size_in_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDiskName")
    def target_disk_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareCbtProtectionContainerMappingDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, key_vault_id: _builtins.str, key_vault_uri: _builtins.str, role_size_to_nic_count_map: Mapping[str, _builtins.int], service_bus_connection_string_secret_name: _builtins.str, storage_account_id: _builtins.str, storage_account_sas_secret_name: _builtins.str, target_location: _builtins.str, excluded_skus: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleSizeToNicCountMap")
    def role_size_to_nic_count_map(self) -> Mapping[str, _builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusConnectionStringSecretName")
    def service_bus_connection_string_secret_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedSkus")
    def excluded_skus(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VMwareCbtSecurityProfilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_target_vm_confidential_encryption_enabled: Optional[_builtins.str] = ..., is_target_vm_integrity_monitoring_enabled: Optional[_builtins.str] = ..., is_target_vm_secure_boot_enabled: Optional[_builtins.str] = ..., is_target_vm_tpm_enabled: Optional[_builtins.str] = ..., target_vm_security_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTargetVmConfidentialEncryptionEnabled")
    def is_target_vm_confidential_encryption_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTargetVmIntegrityMonitoringEnabled")
    def is_target_vm_integrity_monitoring_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTargetVmSecureBootEnabled")
    def is_target_vm_secure_boot_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTargetVmTpmEnabled")
    def is_target_vm_tpm_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmSecurityType")
    def target_vm_security_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, agent_count: Optional[_builtins.str] = ..., agent_expiry_date: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ..., agent_version_details: Optional[outputs.VersionDetailsResponse] = ..., available_memory_in_bytes: Optional[_builtins.float] = ..., available_space_in_bytes: Optional[_builtins.float] = ..., cpu_load: Optional[_builtins.str] = ..., cpu_load_status: Optional[_builtins.str] = ..., cs_service_status: Optional[_builtins.str] = ..., database_server_load: Optional[_builtins.str] = ..., database_server_load_status: Optional[_builtins.str] = ..., host_name: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., last_heartbeat: Optional[_builtins.str] = ..., master_target_servers: Optional[Sequence[outputs.MasterTargetServerResponse]] = ..., memory_usage_status: Optional[_builtins.str] = ..., process_server_count: Optional[_builtins.str] = ..., process_servers: Optional[Sequence[outputs.ProcessServerResponse]] = ..., protected_servers: Optional[_builtins.str] = ..., ps_template_version: Optional[_builtins.str] = ..., replication_pair_count: Optional[_builtins.str] = ..., run_as_accounts: Optional[Sequence[outputs.RunAsAccountResponse]] = ..., space_usage_status: Optional[_builtins.str] = ..., ssl_cert_expiry_date: Optional[_builtins.str] = ..., ssl_cert_expiry_remaining_days: Optional[_builtins.int] = ..., switch_provider_blocking_error_details: Optional[Sequence[outputs.InMageFabricSwitchProviderBlockingErrorDetailsResponse]] = ..., system_load: Optional[_builtins.str] = ..., system_load_status: Optional[_builtins.str] = ..., total_memory_in_bytes: Optional[_builtins.float] = ..., total_space_in_bytes: Optional[_builtins.float] = ..., version_status: Optional[_builtins.str] = ..., web_load: Optional[_builtins.str] = ..., web_load_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentCount")
    def agent_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentExpiryDate")
    def agent_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersionDetails")
    def agent_version_details(self) -> Optional[outputs.VersionDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemoryInBytes")
    def available_memory_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSpaceInBytes")
    def available_space_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLoad")
    def cpu_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLoadStatus")
    def cpu_load_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csServiceStatus")
    def cs_service_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerLoad")
    def database_server_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerLoadStatus")
    def database_server_load_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterTargetServers")
    def master_target_servers(self) -> Optional[Sequence[outputs.MasterTargetServerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryUsageStatus")
    def memory_usage_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServerCount")
    def process_server_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServers")
    def process_servers(self) -> Optional[Sequence[outputs.ProcessServerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedServers")
    def protected_servers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psTemplateVersion")
    def ps_template_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPairCount")
    def replication_pair_count(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccounts")
    def run_as_accounts(self) -> Optional[Sequence[outputs.RunAsAccountResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceUsageStatus")
    def space_usage_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertExpiryDate")
    def ssl_cert_expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertExpiryRemainingDays")
    def ssl_cert_expiry_remaining_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchProviderBlockingErrorDetails")
    def switch_provider_blocking_error_details(self) -> Optional[Sequence[outputs.InMageFabricSwitchProviderBlockingErrorDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoad")
    def system_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemLoadStatus")
    def system_load_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalMemoryInBytes")
    def total_memory_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSpaceInBytes")
    def total_space_in_bytes(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webLoad")
    def web_load(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webLoadStatus")
    def web_load_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareV2FabricSpecificDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, migration_solution_id: _builtins.str, physical_site_id: _builtins.str, process_servers: Sequence[outputs.ProcessServerDetailsResponse], service_container_id: _builtins.str, service_endpoint: _builtins.str, service_resource_id: _builtins.str, vmware_site_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalSiteId")
    def physical_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processServers")
    def process_servers(self) -> Sequence[outputs.ProcessServerDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceContainerId")
    def service_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VaultPrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_endpoint: outputs.PrivateEndpointResponseV1, private_link_service_connection_state: outputs.VaultPrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponseV1:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.VaultPrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VaultPrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_storage_version: _builtins.str, bcdr_security_level: _builtins.str, move_state: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionVaultPropertiesResponse], private_endpoint_state_for_backup: _builtins.str, private_endpoint_state_for_site_recovery: _builtins.str, provisioning_state: _builtins.str, secure_score: _builtins.str, encryption: Optional[outputs.VaultPropertiesResponseEncryption] = ..., monitoring_settings: Optional[outputs.MonitoringSettingsResponse] = ..., move_details: Optional[outputs.VaultPropertiesResponseMoveDetails] = ..., public_network_access: Optional[_builtins.str] = ..., redundancy_settings: Optional[outputs.VaultPropertiesResponseRedundancySettings] = ..., resource_guard_operation_requests: Optional[Sequence[_builtins.str]] = ..., restore_settings: Optional[outputs.RestoreSettingsResponse] = ..., security_settings: Optional[outputs.SecuritySettingsResponse] = ..., upgrade_details: Optional[outputs.UpgradeDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupStorageVersion")
    def backup_storage_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bcdrSecurityLevel")
    def bcdr_security_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveState")
    def move_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointStateForBackup")
    def private_endpoint_state_for_backup(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointStateForSiteRecovery")
    def private_endpoint_state_for_site_recovery(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureScore")
    def secure_score(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.VaultPropertiesResponseEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringSettings")
    def monitoring_settings(self) -> Optional[outputs.MonitoringSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moveDetails")
    def move_details(self) -> Optional[outputs.VaultPropertiesResponseMoveDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redundancySettings")
    def redundancy_settings(self) -> Optional[outputs.VaultPropertiesResponseRedundancySettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuardOperationRequests")
    def resource_guard_operation_requests(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSettings")
    def restore_settings(self) -> Optional[outputs.RestoreSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[outputs.SecuritySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeDetails")
    def upgrade_details(self) -> Optional[outputs.UpgradeDetailsResponse]:
        
        ...
    


@pulumi.output_type
class VaultPropertiesResponseEncryption(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, infrastructure_encryption: Optional[_builtins.str] = ..., kek_identity: Optional[outputs.CmkKekIdentityResponse] = ..., key_vault_properties: Optional[outputs.CmkKeyVaultPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekIdentity")
    def kek_identity(self) -> Optional[outputs.CmkKekIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.CmkKeyVaultPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class VaultPropertiesResponseMoveDetails(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, completion_time_utc: _builtins.str, operation_id: _builtins.str, source_resource_id: _builtins.str, start_time_utc: _builtins.str, target_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionTimeUtc")
    def completion_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VaultPropertiesResponseRedundancySettings(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cross_region_restore: Optional[_builtins.str] = ..., standard_tier_storage_redundancy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRegionRestore")
    def cross_region_restore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardTierStorageRedundancy")
    def standard_tier_storage_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VaultRetentionPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshot_retention_in_days: _builtins.int, vault_retention: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionInDays")
    def snapshot_retention_in_days(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultRetention")
    def vault_retention(self) -> Any:
        
        ...
    


@pulumi.output_type
class VersionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expiry_date: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmmDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmmToAzureNetworkMappingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmmToVmmNetworkMappingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmwareCbtPolicyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, app_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., crash_consistent_frequency_in_minutes: Optional[_builtins.int] = ..., recovery_point_history_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WeeklyRetentionFormatResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_of_the_week: Optional[Sequence[_builtins.str]] = ..., weeks_of_the_month: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeksOfTheMonth")
    def weeks_of_the_month(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WeeklyRetentionScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_of_the_week: Optional[Sequence[_builtins.str]] = ..., retention_duration: Optional[outputs.RetentionDurationResponse] = ..., retention_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfTheWeek")
    def days_of_the_week(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WeeklyScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_run_days: Optional[Sequence[_builtins.str]] = ..., schedule_run_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunDays")
    def schedule_run_days(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleRunTimes")
    def schedule_run_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkloadCrrAccessTokenResponse(dict):
    def __init__(__self__, *, object_type: _builtins.str, access_token_string: Optional[_builtins.str] = ..., b_ms_active_region: Optional[_builtins.str] = ..., backup_management_type: Optional[_builtins.str] = ..., container_id: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., container_type: Optional[_builtins.str] = ..., coordinator_service_stamp_id: Optional[_builtins.str] = ..., coordinator_service_stamp_uri: Optional[_builtins.str] = ..., datasource_container_name: Optional[_builtins.str] = ..., datasource_id: Optional[_builtins.str] = ..., datasource_name: Optional[_builtins.str] = ..., datasource_type: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., protectable_object_container_host_os_name: Optional[_builtins.str] = ..., protectable_object_friendly_name: Optional[_builtins.str] = ..., protectable_object_parent_logical_container_name: Optional[_builtins.str] = ..., protectable_object_protection_state: Optional[_builtins.str] = ..., protectable_object_unique_name: Optional[_builtins.str] = ..., protectable_object_workload_type: Optional[_builtins.str] = ..., protection_container_id: Optional[_builtins.float] = ..., protection_service_stamp_id: Optional[_builtins.str] = ..., protection_service_stamp_uri: Optional[_builtins.str] = ..., recovery_point_id: Optional[_builtins.str] = ..., recovery_point_time: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., rp_is_managed_virtual_machine: Optional[_builtins.bool] = ..., rp_original_sa_option: Optional[_builtins.bool] = ..., rp_tier_information: Optional[Mapping[str, _builtins.str]] = ..., rp_vm_size_description: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., token_extended_information: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenString")
    def access_token_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bMSActiveRegion")
    def b_ms_active_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coordinatorServiceStampId")
    def coordinator_service_stamp_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coordinatorServiceStampUri")
    def coordinator_service_stamp_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasourceContainerName")
    def datasource_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasourceId")
    def datasource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasourceName")
    def datasource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasourceType")
    def datasource_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectContainerHostOsName")
    def protectable_object_container_host_os_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectFriendlyName")
    def protectable_object_friendly_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectParentLogicalContainerName")
    def protectable_object_parent_logical_container_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectProtectionState")
    def protectable_object_protection_state(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectUniqueName")
    def protectable_object_unique_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectableObjectWorkloadType")
    def protectable_object_workload_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionContainerId")
    def protection_container_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionServiceStampId")
    def protection_service_stamp_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionServiceStampUri")
    def protection_service_stamp_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointId")
    def recovery_point_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointTime")
    def recovery_point_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpIsManagedVirtualMachine")
    def rp_is_managed_virtual_machine(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpOriginalSAOption")
    def rp_original_sa_option(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpTierInformation")
    def rp_tier_information(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpVMSizeDescription")
    def rp_vm_size_description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenExtendedInformation")
    def token_extended_information(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkloadInquiryDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inquiry_validation: Optional[outputs.InquiryValidationResponse] = ..., item_count: Optional[_builtins.float] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inquiryValidation")
    def inquiry_validation(self) -> Optional[outputs.InquiryValidationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class YearlyRetentionScheduleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, months_of_year: Optional[Sequence[_builtins.str]] = ..., retention_duration: Optional[outputs.RetentionDurationResponse] = ..., retention_schedule_daily: Optional[outputs.DailyRetentionFormatResponse] = ..., retention_schedule_format_type: Optional[_builtins.str] = ..., retention_schedule_weekly: Optional[outputs.WeeklyRetentionFormatResponse] = ..., retention_times: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthsOfYear")
    def months_of_year(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[outputs.RetentionDurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleDaily")
    def retention_schedule_daily(self) -> Optional[outputs.DailyRetentionFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleFormatType")
    def retention_schedule_format_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionScheduleWeekly")
    def retention_schedule_weekly(self) -> Optional[outputs.WeeklyRetentionFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionTimes")
    def retention_times(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


