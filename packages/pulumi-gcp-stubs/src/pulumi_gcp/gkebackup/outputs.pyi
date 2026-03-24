

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupPlanBackupConfig', 'BackupPlanBackupConfigEncryptionKey', 'BackupPlanBackupConfigSelectedApplications', ..., 'BackupPlanBackupConfigSelectedNamespaceLabels', ..., 'BackupPlanBackupConfigSelectedNamespaces', 'BackupPlanBackupSchedule', 'BackupPlanBackupScheduleRpoConfig', 'BackupPlanBackupScheduleRpoConfigExclusionWindow', ..., ..., ..., 'BackupPlanIamBindingCondition', 'BackupPlanIamMemberCondition', 'BackupPlanRetentionPolicy', 'RestorePlanIamBindingCondition', 'RestorePlanIamMemberCondition', 'RestorePlanRestoreConfig', ..., ..., ..., 'RestorePlanRestoreConfigExcludedNamespaces', 'RestorePlanRestoreConfigRestoreOrder', ..., ..., ..., 'RestorePlanRestoreConfigSelectedApplications', ..., 'RestorePlanRestoreConfigSelectedNamespaces', 'RestorePlanRestoreConfigTransformationRule', ..., ..., ..., ...]
@pulumi.output_type
class BackupPlanBackupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_namespaces: Optional[_builtins.bool] = ..., encryption_key: Optional[outputs.BackupPlanBackupConfigEncryptionKey] = ..., include_secrets: Optional[_builtins.bool] = ..., include_volume_data: Optional[_builtins.bool] = ..., permissive_mode: Optional[_builtins.bool] = ..., selected_applications: Optional[outputs.BackupPlanBackupConfigSelectedApplications] = ..., selected_namespace_labels: Optional[outputs.BackupPlanBackupConfigSelectedNamespaceLabels] = ..., selected_namespaces: Optional[outputs.BackupPlanBackupConfigSelectedNamespaces] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allNamespaces")
    def all_namespaces(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[outputs.BackupPlanBackupConfigEncryptionKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSecrets")
    def include_secrets(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeVolumeData")
    def include_volume_data(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissiveMode")
    def permissive_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedApplications")
    def selected_applications(self) -> Optional[outputs.BackupPlanBackupConfigSelectedApplications]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedNamespaceLabels")
    def selected_namespace_labels(self) -> Optional[outputs.BackupPlanBackupConfigSelectedNamespaceLabels]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedNamespaces")
    def selected_namespaces(self) -> Optional[outputs.BackupPlanBackupConfigSelectedNamespaces]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigEncryptionKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcp_kms_encryption_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpKmsEncryptionKey")
    def gcp_kms_encryption_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigSelectedApplications(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespaced_names: Sequence[outputs.BackupPlanBackupConfigSelectedApplicationsNamespacedName]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedNames")
    def namespaced_names(self) -> Sequence[outputs.BackupPlanBackupConfigSelectedApplicationsNamespacedName]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigSelectedApplicationsNamespacedName(dict):
    def __init__(__self__, *, name: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigSelectedNamespaceLabels(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_labels: Sequence[outputs.BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabel]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Sequence[outputs.BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabel]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabel(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupConfigSelectedNamespaces(dict):
    def __init__(__self__, *, namespaces: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupSchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cron_schedule: Optional[_builtins.str] = ..., paused: Optional[_builtins.bool] = ..., rpo_config: Optional[outputs.BackupPlanBackupScheduleRpoConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paused(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpoConfig")
    def rpo_config(self) -> Optional[outputs.BackupPlanBackupScheduleRpoConfig]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupScheduleRpoConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_rpo_minutes: _builtins.int, exclusion_windows: Optional[Sequence[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindow]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRpoMinutes")
    def target_rpo_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionWindows")
    def exclusion_windows(self) -> Optional[Sequence[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindow]]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupScheduleRpoConfigExclusionWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration: _builtins.str, start_time: outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowStartTime, daily: Optional[_builtins.bool] = ..., days_of_week: Optional[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeek] = ..., single_occurrence_date: Optional[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDate] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowStartTime:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeek]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleOccurrenceDate")
    def single_occurrence_date(self) -> Optional[outputs.BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDate]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeek(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, days_of_weeks: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDate(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowStartTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
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
class BackupPlanIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class BackupPlanIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class BackupPlanRetentionPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_delete_lock_days: Optional[_builtins.int] = ..., backup_retain_days: Optional[_builtins.int] = ..., locked: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupDeleteLockDays")
    def backup_delete_lock_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetainDays")
    def backup_retain_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestorePlanIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RestorePlanIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_namespaces: Optional[_builtins.bool] = ..., cluster_resource_conflict_policy: Optional[_builtins.str] = ..., cluster_resource_restore_scope: Optional[outputs.RestorePlanRestoreConfigClusterResourceRestoreScope] = ..., excluded_namespaces: Optional[outputs.RestorePlanRestoreConfigExcludedNamespaces] = ..., namespaced_resource_restore_mode: Optional[_builtins.str] = ..., no_namespaces: Optional[_builtins.bool] = ..., restore_order: Optional[outputs.RestorePlanRestoreConfigRestoreOrder] = ..., selected_applications: Optional[outputs.RestorePlanRestoreConfigSelectedApplications] = ..., selected_namespaces: Optional[outputs.RestorePlanRestoreConfigSelectedNamespaces] = ..., transformation_rules: Optional[Sequence[outputs.RestorePlanRestoreConfigTransformationRule]] = ..., volume_data_restore_policy: Optional[_builtins.str] = ..., volume_data_restore_policy_bindings: Optional[Sequence[outputs.RestorePlanRestoreConfigVolumeDataRestorePolicyBinding]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allNamespaces")
    def all_namespaces(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceConflictPolicy")
    def cluster_resource_conflict_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceRestoreScope")
    def cluster_resource_restore_scope(self) -> Optional[outputs.RestorePlanRestoreConfigClusterResourceRestoreScope]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedNamespaces")
    def excluded_namespaces(self) -> Optional[outputs.RestorePlanRestoreConfigExcludedNamespaces]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedResourceRestoreMode")
    def namespaced_resource_restore_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noNamespaces")
    def no_namespaces(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreOrder")
    def restore_order(self) -> Optional[outputs.RestorePlanRestoreConfigRestoreOrder]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedApplications")
    def selected_applications(self) -> Optional[outputs.RestorePlanRestoreConfigSelectedApplications]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedNamespaces")
    def selected_namespaces(self) -> Optional[outputs.RestorePlanRestoreConfigSelectedNamespaces]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformationRules")
    def transformation_rules(self) -> Optional[Sequence[outputs.RestorePlanRestoreConfigTransformationRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeDataRestorePolicy")
    def volume_data_restore_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeDataRestorePolicyBindings")
    def volume_data_restore_policy_bindings(self) -> Optional[Sequence[outputs.RestorePlanRestoreConfigVolumeDataRestorePolicyBinding]]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigClusterResourceRestoreScope(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_group_kinds: Optional[_builtins.bool] = ..., excluded_group_kinds: Optional[Sequence[outputs.RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKind]] = ..., no_group_kinds: Optional[_builtins.bool] = ..., selected_group_kinds: Optional[Sequence[outputs.RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKind]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allGroupKinds")
    def all_group_kinds(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedGroupKinds")
    def excluded_group_kinds(self) -> Optional[Sequence[outputs.RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKind]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noGroupKinds")
    def no_group_kinds(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedGroupKinds")
    def selected_group_kinds(self) -> Optional[Sequence[outputs.RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKind]]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKind(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: Optional[_builtins.str] = ..., resource_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKind(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: Optional[_builtins.str] = ..., resource_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigExcludedNamespaces(dict):
    def __init__(__self__, *, namespaces: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigRestoreOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_kind_dependencies: Sequence[outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependency]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKindDependencies")
    def group_kind_dependencies(self) -> Sequence[outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependency]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependency(dict):
    def __init__(__self__, *, requiring: outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiring, satisfying: outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfying) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requiring(self) -> outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiring:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def satisfying(self) -> outputs.RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfying:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiring(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: Optional[_builtins.str] = ..., resource_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfying(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: Optional[_builtins.str] = ..., resource_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigSelectedApplications(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespaced_names: Sequence[outputs.RestorePlanRestoreConfigSelectedApplicationsNamespacedName]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedNames")
    def namespaced_names(self) -> Sequence[outputs.RestorePlanRestoreConfigSelectedApplicationsNamespacedName]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigSelectedApplicationsNamespacedName(dict):
    def __init__(__self__, *, name: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigSelectedNamespaces(dict):
    def __init__(__self__, *, namespaces: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigTransformationRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_actions: Sequence[outputs.RestorePlanRestoreConfigTransformationRuleFieldAction], description: Optional[_builtins.str] = ..., resource_filter: Optional[outputs.RestorePlanRestoreConfigTransformationRuleResourceFilter] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldActions")
    def field_actions(self) -> Sequence[outputs.RestorePlanRestoreConfigTransformationRuleFieldAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceFilter")
    def resource_filter(self) -> Optional[outputs.RestorePlanRestoreConfigTransformationRuleResourceFilter]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigTransformationRuleFieldAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, op: _builtins.str, from_path: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def op(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPath")
    def from_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigTransformationRuleResourceFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_kinds: Optional[Sequence[outputs.RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKind]] = ..., json_path: Optional[_builtins.str] = ..., namespaces: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKinds")
    def group_kinds(self) -> Optional[Sequence[outputs.RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKind]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKind(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_group: Optional[_builtins.str] = ..., resource_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestorePlanRestoreConfigVolumeDataRestorePolicyBinding(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy: _builtins.str, volume_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    


