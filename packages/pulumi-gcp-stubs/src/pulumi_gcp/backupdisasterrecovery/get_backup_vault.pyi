

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackupVaultResult', 'AwaitableGetBackupVaultResult', 'get_backup_vault', 'get_backup_vault_output']
@pulumi.output_type
class GetBackupVaultResult:
    
    def __init__(__self__, access_restriction=..., allow_missing=..., annotations=..., backup_count=..., backup_minimum_enforced_retention_duration=..., backup_retention_inheritance=..., backup_vault_id=..., create_time=..., deletable=..., description=..., effective_annotations=..., effective_labels=..., effective_time=..., encryption_configs=..., etag=..., force_delete=..., force_update=..., id=..., ignore_backup_plan_references=..., ignore_inactive_datasources=..., labels=..., location=..., name=..., project=..., pulumi_labels=..., service_account=..., state=..., total_stored_bytes=..., uid=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRestriction")
    def access_restriction(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMissing")
    def allow_missing(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDuration")
    def backup_minimum_enforced_retention_duration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionInheritance")
    def backup_retention_inheritance(self) -> _builtins.str:
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
    @pulumi.getter
    def deletable(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(self) -> Sequence[outputs.GetBackupVaultEncryptionConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreBackupPlanReferences")
    def ignore_backup_plan_references(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreInactiveDatasources")
    def ignore_inactive_datasources(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
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
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
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
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetBackupVaultResult(GetBackupVaultResult):
    def __await__(self): # -> Generator[Never, Any, GetBackupVaultResult]:
        ...
    


def get_backup_vault(backup_vault_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackupVaultResult:
    
    ...

def get_backup_vault_output(backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackupVaultResult]:
    
    ...

