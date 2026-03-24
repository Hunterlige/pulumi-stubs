

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, annotations=..., automated_backup_policies=..., backup_sources=..., backupdr_backup_sources=..., cluster_id=..., cluster_type=..., continuous_backup_configs=..., continuous_backup_infos=..., database_version=..., dataplex_configs=..., deletion_policy=..., deletion_protection=..., display_name=..., effective_annotations=..., effective_labels=..., encryption_configs=..., encryption_infos=..., etag=..., id=..., initial_users=..., labels=..., location=..., maintenance_update_policies=..., migration_sources=..., name=..., network_configs=..., project=..., psc_configs=..., pulumi_labels=..., reconciling=..., restore_backup_sources=..., restore_backupdr_backup_sources=..., restore_backupdr_pitr_sources=..., restore_continuous_backup_sources=..., secondary_configs=..., skip_await_major_version_upgrade=..., state=..., subscription_type=..., trial_metadatas=..., uid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicies")
    def automated_backup_policies(self) -> Sequence[outputs.GetClusterAutomatedBackupPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSources")
    def backup_sources(self) -> Sequence[outputs.GetClusterBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupdrBackupSources")
    def backupdr_backup_sources(self) -> Sequence[outputs.GetClusterBackupdrBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousBackupConfigs")
    def continuous_backup_configs(self) -> Sequence[outputs.GetClusterContinuousBackupConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousBackupInfos")
    def continuous_backup_infos(self) -> Sequence[outputs.GetClusterContinuousBackupInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexConfigs")
    def dataplex_configs(self) -> Sequence[outputs.GetClusterDataplexConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
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
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(self) -> Sequence[outputs.GetClusterEncryptionConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(self) -> Sequence[outputs.GetClusterEncryptionInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialUsers")
    def initial_users(self) -> Sequence[outputs.GetClusterInitialUserResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceUpdatePolicies")
    def maintenance_update_policies(self) -> Sequence[outputs.GetClusterMaintenanceUpdatePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSources")
    def migration_sources(self) -> Sequence[outputs.GetClusterMigrationSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> Sequence[outputs.GetClusterNetworkConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Sequence[outputs.GetClusterPscConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupSources")
    def restore_backup_sources(self) -> Sequence[outputs.GetClusterRestoreBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrBackupSources")
    def restore_backupdr_backup_sources(self) -> Sequence[outputs.GetClusterRestoreBackupdrBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrPitrSources")
    def restore_backupdr_pitr_sources(self) -> Sequence[outputs.GetClusterRestoreBackupdrPitrSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreContinuousBackupSources")
    def restore_continuous_backup_sources(self) -> Sequence[outputs.GetClusterRestoreContinuousBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryConfigs")
    def secondary_configs(self) -> Sequence[outputs.GetClusterSecondaryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipAwaitMajorVersionUpgrade")
    def skip_await_major_version_upgrade(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trialMetadatas")
    def trial_metadatas(self) -> Sequence[outputs.GetClusterTrialMetadataResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(cluster_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

