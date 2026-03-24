

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupPlanAssociationRulesConfigInfo', ..., 'BackupPlanBackupRule', 'BackupPlanBackupRuleStandardSchedule', 'BackupPlanBackupRuleStandardScheduleBackupWindow', 'BackupPlanBackupRuleStandardScheduleWeekDayOfMonth', 'BackupVaultEncryptionConfig', 'ManagementServerManagementUri', 'ManagementServerNetwork', 'RestoreWorkloadComputeInstanceRestoreProperties', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RestoreWorkloadComputeInstanceTargetEnvironment', 'RestoreWorkloadDiskRestoreProperties', ..., 'RestoreWorkloadDiskRestorePropertiesGuestOsFeature', 'RestoreWorkloadDiskRestorePropertiesLabel', ..., 'RestoreWorkloadDiskTargetEnvironment', 'RestoreWorkloadRegionDiskTargetEnvironment', 'RestoreWorkloadTargetResource', 'RestoreWorkloadTargetResourceGcpResource', 'GetBackupBackupResult', 'GetBackupPlanAssociationRulesConfigInfoResult', ..., 'GetBackupPlanAssociationsAssociationResult', ..., ..., 'GetBackupPlanBackupRuleResult', 'GetBackupPlanBackupRuleStandardScheduleResult', ..., ..., 'GetBackupVaultEncryptionConfigResult', 'GetDataSourceBackupConfigInfoResult', ..., 'GetDataSourceBackupConfigInfoGcpBackupConfigResult', ..., 'GetDataSourceDataSourceGcpResourceResult', ..., 'GetDataSourceReferencesDataSourceReferenceResult', 'GetDataSourcesDataSourceResult', 'GetDataSourcesDataSourceBackupConfigInfoResult', ..., ..., ..., ..., ..., 'GetManagementServerManagementUriResult', 'GetManagementServerNetworkResult']
@pulumi.output_type
class BackupPlanAssociationRulesConfigInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_backup_errors: Optional[Sequence[outputs.BackupPlanAssociationRulesConfigInfoLastBackupError]] = ..., last_backup_state: Optional[_builtins.str] = ..., last_successful_backup_consistency_time: Optional[_builtins.str] = ..., rule_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrors")
    def last_backup_errors(self) -> Optional[Sequence[outputs.BackupPlanAssociationRulesConfigInfoLastBackupError]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupPlanAssociationRulesConfigInfoLastBackupError(dict):
    def __init__(__self__, *, code: Optional[_builtins.float] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_retention_days: _builtins.int, rule_id: _builtins.str, standard_schedule: outputs.BackupPlanBackupRuleStandardSchedule) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardSchedule")
    def standard_schedule(self) -> outputs.BackupPlanBackupRuleStandardSchedule:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupRuleStandardSchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recurrence_type: _builtins.str, time_zone: _builtins.str, backup_window: Optional[outputs.BackupPlanBackupRuleStandardScheduleBackupWindow] = ..., days_of_months: Optional[Sequence[_builtins.int]] = ..., days_of_weeks: Optional[Sequence[_builtins.str]] = ..., hourly_frequency: Optional[_builtins.int] = ..., months: Optional[Sequence[_builtins.str]] = ..., week_day_of_month: Optional[outputs.BackupPlanBackupRuleStandardScheduleWeekDayOfMonth] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[outputs.BackupPlanBackupRuleStandardScheduleBackupWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonths")
    def days_of_months(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlyFrequency")
    def hourly_frequency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def months(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDayOfMonth")
    def week_day_of_month(self) -> Optional[outputs.BackupPlanBackupRuleStandardScheduleWeekDayOfMonth]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupRuleStandardScheduleBackupWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_hour_of_day: _builtins.int, end_hour_of_day: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHourOfDay")
    def start_hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endHourOfDay")
    def end_hour_of_day(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupRuleStandardScheduleWeekDayOfMonth(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day_of_week: _builtins.str, week_of_month: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekOfMonth")
    def week_of_month(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BackupVaultEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagementServerManagementUri(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api: Optional[_builtins.str] = ..., web_ui: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webUi")
    def web_ui(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagementServerNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network: _builtins.str, peering_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringMode")
    def peering_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestoreProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, advanced_machine_features: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeatures] = ..., allocation_affinity: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinity] = ..., can_ip_forward: Optional[_builtins.bool] = ..., confidential_instance_config: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfig] = ..., deletion_protection: Optional[_builtins.bool] = ..., description: Optional[_builtins.str] = ..., disks: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDisk]] = ..., display_device: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDisplayDevice] = ..., guest_accelerators: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesGuestAccelerator]] = ..., hostname: Optional[_builtins.str] = ..., instance_encryption_key: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKey] = ..., key_revocation_action_type: Optional[_builtins.str] = ..., labels: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesLabel]] = ..., machine_type: Optional[_builtins.str] = ..., metadata: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesMetadata] = ..., min_cpu_platform: Optional[_builtins.str] = ..., network_interfaces: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterface]] = ..., network_performance_config: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfig] = ..., params: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesParams] = ..., private_ipv6_google_access: Optional[_builtins.str] = ..., resource_policies: Optional[Sequence[_builtins.str]] = ..., scheduling: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesScheduling] = ..., service_accounts: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesServiceAccount]] = ..., shielded_instance_config: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfig] = ..., tags: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeatures]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationAffinity")
    def allocation_affinity(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDisk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayDevice")
    def display_device(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDisplayDevice]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesGuestAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKey")
    def instance_encryption_key(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesMetadata]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesParams]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesScheduling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesServiceAccount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesTags]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeatures(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_nested_virtualization: Optional[_builtins.bool] = ..., enable_uefi_networking: Optional[_builtins.bool] = ..., threads_per_core: Optional[_builtins.int] = ..., visible_core_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableUefiNetworking")
    def enable_uefi_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibleCoreCount")
    def visible_core_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consume_allocation_type: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumeAllocationType")
    def consume_allocation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_confidential_compute: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesDisk(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_delete: Optional[_builtins.bool] = ..., boot: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., disk_encryption_key: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKey] = ..., disk_interface: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., disk_type: Optional[_builtins.str] = ..., guest_os_features: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeature]] = ..., index: Optional[_builtins.int] = ..., initialize_params: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParams] = ..., kind: Optional[_builtins.str] = ..., licenses: Optional[Sequence[_builtins.str]] = ..., mode: Optional[_builtins.str] = ..., saved_state: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskInterface")
    def disk_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeature]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializeParams")
    def initialize_params(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParams]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savedState")
    def saved_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ..., kms_key_service_account: Optional[_builtins.str] = ..., raw_key: Optional[_builtins.str] = ..., rsa_encrypted_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeature(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParams(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_name: Optional[_builtins.str] = ..., replica_zones: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesDisplayDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_display: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesGuestAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ..., kms_key_service_account: Optional[_builtins.str] = ..., raw_key: Optional[_builtins.str] = ..., rsa_encrypted_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesLabel(dict):
    def __init__(__self__, *, key: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesMetadata(dict):
    def __init__(__self__, *, items: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesMetadataItem]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesMetadataItem]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesMetadataItem(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_configs: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfig]] = ..., alias_ip_ranges: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRange]] = ..., internal_ipv6_prefix_length: Optional[_builtins.int] = ..., ip_address: Optional[_builtins.str] = ..., ipv6_access_configs: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfig]] = ..., ipv6_access_type: Optional[_builtins.str] = ..., ipv6_address: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., network_attachment: Optional[_builtins.str] = ..., nic_type: Optional[_builtins.str] = ..., queue_count: Optional[_builtins.int] = ..., stack_type: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aliasIpRanges")
    def alias_ip_ranges(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRange]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpv6PrefixLength")
    def internal_ipv6_prefix_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessConfigs")
    def ipv6_access_configs(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_ip: Optional[_builtins.str] = ..., external_ipv6: Optional[_builtins.str] = ..., external_ipv6_prefix_length: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ..., network_tier: Optional[_builtins.str] = ..., public_ptr_domain_name: Optional[_builtins.str] = ..., set_public_ptr: Optional[_builtins.bool] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6")
    def external_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="setPublicPtr")
    def set_public_ptr(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_cidr_range: Optional[_builtins.str] = ..., subnetwork_range_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworkRangeName")
    def subnetwork_range_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_ip: Optional[_builtins.str] = ..., external_ipv6: Optional[_builtins.str] = ..., external_ipv6_prefix_length: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ..., network_tier: Optional[_builtins.str] = ..., public_ptr_domain_name: Optional[_builtins.str] = ..., set_public_ptr: Optional[_builtins.bool] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6")
    def external_ipv6(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="setPublicPtr")
    def set_public_ptr(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, total_egress_bandwidth_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesParams(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_manager_tags: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTag]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesScheduling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic_restart: Optional[_builtins.bool] = ..., instance_termination_action: Optional[_builtins.str] = ..., local_ssd_recovery_timeout: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeout] = ..., max_run_duration: Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDuration] = ..., min_node_cpus: Optional[_builtins.int] = ..., node_affinities: Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinity]] = ..., on_host_maintenance: Optional[_builtins.str] = ..., preemptible: Optional[_builtins.bool] = ..., provisioning_model: Optional[_builtins.str] = ..., termination_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticRestart")
    def automatic_restart(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTerminationAction")
    def instance_termination_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdRecoveryTimeout")
    def local_ssd_recovery_timeout(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeout]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDuration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(self) -> Optional[Sequence[outputs.RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onHostMaintenance")
    def on_host_maintenance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningModel")
    def provisioning_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationTime")
    def termination_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeout(dict):
    def __init__(__self__, *, nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDuration(dict):
    def __init__(__self__, *, nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinity(dict):
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., operator: Optional[_builtins.str] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesServiceAccount(dict):
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_integrity_monitoring: Optional[_builtins.bool] = ..., enable_secure_boot: Optional[_builtins.bool] = ..., enable_vtpm: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceRestorePropertiesTags(dict):
    def __init__(__self__, *, items: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadComputeInstanceTargetEnvironment(dict):
    def __init__(__self__, *, project: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskRestoreProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, size_gb: _builtins.int, type: _builtins.str, access_mode: Optional[_builtins.str] = ..., architecture: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., disk_encryption_key: Optional[outputs.RestoreWorkloadDiskRestorePropertiesDiskEncryptionKey] = ..., enable_confidential_compute: Optional[_builtins.bool] = ..., guest_os_features: Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesGuestOsFeature]] = ..., labels: Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesLabel]] = ..., licenses: Optional[Sequence[_builtins.str]] = ..., physical_block_size_bytes: Optional[_builtins.int] = ..., provisioned_iops: Optional[_builtins.int] = ..., provisioned_throughput: Optional[_builtins.int] = ..., resource_manager_tags: Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesResourceManagerTag]] = ..., resource_policies: Optional[Sequence[_builtins.str]] = ..., storage_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[outputs.RestoreWorkloadDiskRestorePropertiesDiskEncryptionKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesGuestOsFeature]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Sequence[outputs.RestoreWorkloadDiskRestorePropertiesResourceManagerTag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskRestorePropertiesDiskEncryptionKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ..., kms_key_service_account: Optional[_builtins.str] = ..., raw_key: Optional[_builtins.str] = ..., rsa_encrypted_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskRestorePropertiesGuestOsFeature(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskRestorePropertiesLabel(dict):
    def __init__(__self__, *, key: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskRestorePropertiesResourceManagerTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadDiskTargetEnvironment(dict):
    def __init__(__self__, *, project: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadRegionDiskTargetEnvironment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project: _builtins.str, region: _builtins.str, replica_zones: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadTargetResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcp_resource: Optional[outputs.RestoreWorkloadTargetResourceGcpResource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpResource")
    def gcp_resource(self) -> Optional[outputs.RestoreWorkloadTargetResourceGcpResource]:
        
        ...
    


@pulumi.output_type
class RestoreWorkloadTargetResourceGcpResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcp_resourcename: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpResourcename")
    def gcp_resourcename(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetBackupBackupResult(dict):
    def __init__(__self__, *, backup_id: _builtins.str, backup_vault_id: _builtins.str, create_time: _builtins.str, data_source_id: _builtins.str, location: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupPlanAssociationRulesConfigInfoResult(dict):
    def __init__(__self__, *, last_backup_errors: Sequence[outputs.GetBackupPlanAssociationRulesConfigInfoLastBackupErrorResult], last_backup_state: _builtins.str, last_successful_backup_consistency_time: _builtins.str, rule_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrors")
    def last_backup_errors(self) -> Sequence[outputs.GetBackupPlanAssociationRulesConfigInfoLastBackupErrorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupPlanAssociationRulesConfigInfoLastBackupErrorResult(dict):
    def __init__(__self__, *, code: _builtins.float, message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupPlanAssociationsAssociationResult(dict):
    def __init__(__self__, *, backup_plan: _builtins.str, create_time: _builtins.str, data_source: _builtins.str, name: _builtins.str, resource: _builtins.str, rules_config_infos: Sequence[outputs.GetBackupPlanAssociationsAssociationRulesConfigInfoResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesConfigInfos")
    def rules_config_infos(self) -> Sequence[outputs.GetBackupPlanAssociationsAssociationRulesConfigInfoResult]:
        
        ...
    


@pulumi.output_type
class GetBackupPlanAssociationsAssociationRulesConfigInfoResult(dict):
    def __init__(__self__, *, last_backup_errors: Sequence[outputs.GetBackupPlanAssociationsAssociationRulesConfigInfoLastBackupErrorResult], last_backup_state: _builtins.str, last_successful_backup_consistency_time: _builtins.str, rule_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupErrors")
    def last_backup_errors(self) -> Sequence[outputs.GetBackupPlanAssociationsAssociationRulesConfigInfoLastBackupErrorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupPlanAssociationsAssociationRulesConfigInfoLastBackupErrorResult(dict):
    def __init__(__self__, *, code: _builtins.int, message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupPlanBackupRuleResult(dict):
    def __init__(__self__, *, backup_retention_days: _builtins.int, rule_id: _builtins.str, standard_schedules: Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardSchedules")
    def standard_schedules(self) -> Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleResult]:
        
        ...
    


@pulumi.output_type
class GetBackupPlanBackupRuleStandardScheduleResult(dict):
    def __init__(__self__, *, backup_windows: Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleBackupWindowResult], days_of_months: Sequence[_builtins.int], days_of_weeks: Sequence[_builtins.str], hourly_frequency: _builtins.int, months: Sequence[_builtins.str], recurrence_type: _builtins.str, time_zone: _builtins.str, week_day_of_months: Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleWeekDayOfMonthResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupWindows")
    def backup_windows(self) -> Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleBackupWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonths")
    def days_of_months(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlyFrequency")
    def hourly_frequency(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def months(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDayOfMonths")
    def week_day_of_months(self) -> Sequence[outputs.GetBackupPlanBackupRuleStandardScheduleWeekDayOfMonthResult]:
        
        ...
    


@pulumi.output_type
class GetBackupPlanBackupRuleStandardScheduleBackupWindowResult(dict):
    def __init__(__self__, *, end_hour_of_day: _builtins.int, start_hour_of_day: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endHourOfDay")
    def end_hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHourOfDay")
    def start_hour_of_day(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetBackupPlanBackupRuleStandardScheduleWeekDayOfMonthResult(dict):
    def __init__(__self__, *, day_of_week: _builtins.str, week_of_month: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekOfMonth")
    def week_of_month(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBackupVaultEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceBackupConfigInfoResult(dict):
    def __init__(__self__, *, backup_appliance_backup_configs: Sequence[outputs.GetDataSourceBackupConfigInfoBackupApplianceBackupConfigResult], gcp_backup_configs: Sequence[outputs.GetDataSourceBackupConfigInfoGcpBackupConfigResult], last_backup_error: Mapping[str, _builtins.str], last_backup_state: _builtins.str, last_successful_backup_consistency_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceBackupConfigs")
    def backup_appliance_backup_configs(self) -> Sequence[outputs.GetDataSourceBackupConfigInfoBackupApplianceBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpBackupConfigs")
    def gcp_backup_configs(self) -> Sequence[outputs.GetDataSourceBackupConfigInfoGcpBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupError")
    def last_backup_error(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceBackupConfigInfoBackupApplianceBackupConfigResult(dict):
    def __init__(__self__, *, application_name: _builtins.str, backup_appliance_id: _builtins.str, backup_appliance_name: _builtins.str, host_name: _builtins.str, sla_id: _builtins.str, slp_name: _builtins.str, slt_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceId")
    def backup_appliance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceName")
    def backup_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slaId")
    def sla_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slpName")
    def slp_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sltName")
    def slt_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceBackupConfigInfoGcpBackupConfigResult(dict):
    def __init__(__self__, *, backup_plan: _builtins.str, backup_plan_association: _builtins.str, backup_plan_description: _builtins.str, backup_plan_rules: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociation")
    def backup_plan_association(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanDescription")
    def backup_plan_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanRules")
    def backup_plan_rules(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetDataSourceDataSourceBackupApplianceApplicationResult(dict):
    def __init__(__self__, *, appliance_id: _builtins.str, application_id: _builtins.str, application_name: _builtins.str, backup_appliance: _builtins.str, host_id: _builtins.str, hostname: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceId")
    def appliance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupAppliance")
    def backup_appliance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceDataSourceGcpResourceResult(dict):
    def __init__(__self__, *, compute_instance_data_source_properties: Sequence[outputs.GetDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult], gcp_resourcename: _builtins.str, location: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceDataSourceProperties")
    def compute_instance_data_source_properties(self) -> Sequence[outputs.GetDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpResourcename")
    def gcp_resourcename(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult(dict):
    def __init__(__self__, *, description: _builtins.str, machine_type: _builtins.str, name: _builtins.str, total_disk_count: _builtins.str, total_disk_size_gb: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDiskCount")
    def total_disk_count(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDiskSizeGb")
    def total_disk_size_gb(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourceReferencesDataSourceReferenceResult(dict):
    def __init__(__self__, *, backup_config_state: _builtins.str, backup_count: _builtins.int, data_source: _builtins.str, gcp_resource_name: _builtins.str, last_backup_state: _builtins.str, last_successful_backup_time: _builtins.str, name: _builtins.str, resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfigState")
    def backup_config_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpResourceName")
    def gcp_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupTime")
    def last_successful_backup_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceResult(dict):
    def __init__(__self__, *, backup_config_infos: Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoResult], backup_count: _builtins.str, config_state: _builtins.str, create_time: _builtins.str, data_source_backup_appliance_applications: Sequence[outputs.GetDataSourcesDataSourceDataSourceBackupApplianceApplicationResult], data_source_gcp_resources: Sequence[outputs.GetDataSourcesDataSourceDataSourceGcpResourceResult], etag: _builtins.str, labels: Mapping[str, _builtins.str], name: _builtins.str, state: _builtins.str, total_stored_bytes: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfigInfos")
    def backup_config_infos(self) -> Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configState")
    def config_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceBackupApplianceApplications")
    def data_source_backup_appliance_applications(self) -> Sequence[outputs.GetDataSourcesDataSourceDataSourceBackupApplianceApplicationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceGcpResources")
    def data_source_gcp_resources(self) -> Sequence[outputs.GetDataSourcesDataSourceDataSourceGcpResourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStoredBytes")
    def total_stored_bytes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceBackupConfigInfoResult(dict):
    def __init__(__self__, *, backup_appliance_backup_configs: Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoBackupApplianceBackupConfigResult], gcp_backup_configs: Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoGcpBackupConfigResult], last_backup_error: Mapping[str, _builtins.str], last_backup_state: _builtins.str, last_successful_backup_consistency_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceBackupConfigs")
    def backup_appliance_backup_configs(self) -> Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoBackupApplianceBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpBackupConfigs")
    def gcp_backup_configs(self) -> Sequence[outputs.GetDataSourcesDataSourceBackupConfigInfoGcpBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupError")
    def last_backup_error(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceBackupConfigInfoBackupApplianceBackupConfigResult(dict):
    def __init__(__self__, *, application_name: _builtins.str, backup_appliance_id: _builtins.str, backup_appliance_name: _builtins.str, host_name: _builtins.str, sla_id: _builtins.str, slp_name: _builtins.str, slt_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceId")
    def backup_appliance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupApplianceName")
    def backup_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slaId")
    def sla_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slpName")
    def slp_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sltName")
    def slt_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceBackupConfigInfoGcpBackupConfigResult(dict):
    def __init__(__self__, *, backup_plan: _builtins.str, backup_plan_association: _builtins.str, backup_plan_description: _builtins.str, backup_plan_rules: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociation")
    def backup_plan_association(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanDescription")
    def backup_plan_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanRules")
    def backup_plan_rules(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceDataSourceBackupApplianceApplicationResult(dict):
    def __init__(__self__, *, appliance_id: _builtins.str, application_id: _builtins.str, application_name: _builtins.str, backup_appliance: _builtins.str, host_id: _builtins.str, hostname: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceId")
    def appliance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupAppliance")
    def backup_appliance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceDataSourceGcpResourceResult(dict):
    def __init__(__self__, *, compute_instance_data_source_properties: Sequence[outputs.GetDataSourcesDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult], gcp_resourcename: _builtins.str, location: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceDataSourceProperties")
    def compute_instance_data_source_properties(self) -> Sequence[outputs.GetDataSourcesDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpResourcename")
    def gcp_resourcename(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataSourcesDataSourceDataSourceGcpResourceComputeInstanceDataSourcePropertyResult(dict):
    def __init__(__self__, *, description: _builtins.str, machine_type: _builtins.str, name: _builtins.str, total_disk_count: _builtins.str, total_disk_size_gb: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDiskCount")
    def total_disk_count(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDiskSizeGb")
    def total_disk_size_gb(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetManagementServerManagementUriResult(dict):
    def __init__(__self__, *, api: _builtins.str, web_ui: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def api(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webUi")
    def web_ui(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetManagementServerNetworkResult(dict):
    def __init__(__self__, *, network: _builtins.str, peering_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringMode")
    def peering_mode(self) -> _builtins.str:
        
        ...
    


