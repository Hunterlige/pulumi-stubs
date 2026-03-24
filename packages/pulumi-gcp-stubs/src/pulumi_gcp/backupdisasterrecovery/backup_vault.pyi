

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupVaultArgs', 'BackupVault']
@pulumi.input_type
class BackupVaultArgs:
    def __init__(__self__, *, backup_minimum_enforced_retention_duration: pulumi.Input[_builtins.str], backup_vault_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], access_restriction: Optional[pulumi.Input[_builtins.str]] = ..., allow_missing: Optional[pulumi.Input[_builtins.bool]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., backup_retention_inheritance: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_update: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_backup_plan_references: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_inactive_datasources: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDuration")
    def backup_minimum_enforced_retention_duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_minimum_enforced_retention_duration.setter
    def backup_minimum_enforced_retention_duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_vault_id.setter
    def backup_vault_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRestriction")
    def access_restriction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_restriction.setter
    def access_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMissing")
    def allow_missing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_missing.setter
    def allow_missing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionInheritance")
    def backup_retention_inheritance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_retention_inheritance.setter
    def backup_retention_inheritance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    @_utilities.deprecated(...)
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreBackupPlanReferences")
    def ignore_backup_plan_references(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_backup_plan_references.setter
    def ignore_backup_plan_references(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreInactiveDatasources")
    def ignore_inactive_datasources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_inactive_datasources.setter
    def ignore_inactive_datasources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BackupVaultState:
    def __init__(__self__, *, access_restriction: Optional[pulumi.Input[_builtins.str]] = ..., allow_missing: Optional[pulumi.Input[_builtins.bool]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., backup_count: Optional[pulumi.Input[_builtins.str]] = ..., backup_minimum_enforced_retention_duration: Optional[pulumi.Input[_builtins.str]] = ..., backup_retention_inheritance: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletable: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_update: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_backup_plan_references: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_inactive_datasources: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., total_stored_bytes: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRestriction")
    def access_restriction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_restriction.setter
    def access_restriction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMissing")
    def allow_missing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_missing.setter
    def allow_missing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_count.setter
    def backup_count(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDuration")
    def backup_minimum_enforced_retention_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_minimum_enforced_retention_duration.setter
    def backup_minimum_enforced_retention_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionInheritance")
    def backup_retention_inheritance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_retention_inheritance.setter
    def backup_retention_inheritance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault_id.setter
    def backup_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def deletable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletable.setter
    def deletable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[BackupVaultEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    @_utilities.deprecated(...)
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreBackupPlanReferences")
    def ignore_backup_plan_references(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_backup_plan_references.setter
    def ignore_backup_plan_references(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreInactiveDatasources")
    def ignore_inactive_datasources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_inactive_datasources.setter
    def ignore_inactive_datasources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStoredBytes")
    def total_stored_bytes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_stored_bytes.setter
    def total_stored_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:backupdisasterrecovery/backupVault:BackupVault")
class BackupVault(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_restriction: Optional[pulumi.Input[_builtins.str]] = ..., allow_missing: Optional[pulumi.Input[_builtins.bool]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., backup_minimum_enforced_retention_duration: Optional[pulumi.Input[_builtins.str]] = ..., backup_retention_inheritance: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[Union[BackupVaultEncryptionConfigArgs, BackupVaultEncryptionConfigArgsDict]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_update: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_backup_plan_references: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_inactive_datasources: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BackupVaultArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_restriction: Optional[pulumi.Input[_builtins.str]] = ..., allow_missing: Optional[pulumi.Input[_builtins.bool]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., backup_count: Optional[pulumi.Input[_builtins.str]] = ..., backup_minimum_enforced_retention_duration: Optional[pulumi.Input[_builtins.str]] = ..., backup_retention_inheritance: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletable: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_time: Optional[pulumi.Input[_builtins.str]] = ..., encryption_config: Optional[pulumi.Input[Union[BackupVaultEncryptionConfigArgs, BackupVaultEncryptionConfigArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_update: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_backup_plan_references: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_inactive_datasources: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., total_stored_bytes: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> BackupVault:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRestriction")
    def access_restriction(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMissing")
    def allow_missing(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDuration")
    def backup_minimum_enforced_retention_duration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionInheritance")
    def backup_retention_inheritance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deletable(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[Optional[outputs.BackupVaultEncryptionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    @_utilities.deprecated(...)
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreBackupPlanReferences")
    def ignore_backup_plan_references(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreInactiveDatasources")
    def ignore_inactive_datasources(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStoredBytes")
    def total_stored_bytes(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


