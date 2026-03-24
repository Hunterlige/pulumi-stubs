import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyArgs]
        ] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        continuous_backup_config: Optional[
            pulumi.Input[ClusterContinuousBackupConfigArgs]
        ] = ...,
        database_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplex_config: Optional[pulumi.Input[ClusterDataplexConfigArgs]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[pulumi.Input[ClusterEncryptionConfigArgs]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_user: Optional[pulumi.Input[ClusterInitialUserArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        maintenance_update_policy: Optional[
            pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]
        ] = ...,
        network_config: Optional[pulumi.Input[ClusterNetworkConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[pulumi.Input[ClusterPscConfigArgs]] = ...,
        restore_backup_source: Optional[
            pulumi.Input[ClusterRestoreBackupSourceArgs]
        ] = ...,
        restore_backupdr_backup_source: Optional[
            pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]
        ] = ...,
        restore_backupdr_pitr_source: Optional[
            pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]
        ] = ...,
        restore_continuous_backup_source: Optional[
            pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]
        ] = ...,
        secondary_config: Optional[pulumi.Input[ClusterSecondaryConfigArgs]] = ...,
        skip_await_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterAutomatedBackupPolicyArgs]]: ...
    @automated_backup_policy.setter
    def automated_backup_policy(
        self, value: Optional[pulumi.Input[ClusterAutomatedBackupPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="continuousBackupConfig")
    def continuous_backup_config(
        self,
    ) -> Optional[pulumi.Input[ClusterContinuousBackupConfigArgs]]: ...
    @continuous_backup_config.setter
    def continuous_backup_config(
        self, value: Optional[pulumi.Input[ClusterContinuousBackupConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_version.setter
    def database_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataplexConfig")
    def dataplex_config(self) -> Optional[pulumi.Input[ClusterDataplexConfigArgs]]: ...
    @dataplex_config.setter
    def dataplex_config(
        self, value: Optional[pulumi.Input[ClusterDataplexConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[ClusterEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[ClusterEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> Optional[pulumi.Input[ClusterInitialUserArgs]]: ...
    @initial_user.setter
    def initial_user(self, value: Optional[pulumi.Input[ClusterInitialUserArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceUpdatePolicy")
    def maintenance_update_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]]: ...
    @maintenance_update_policy.setter
    def maintenance_update_policy(
        self, value: Optional[pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[ClusterNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[ClusterNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[ClusterPscConfigArgs]]: ...
    @psc_config.setter
    def psc_config(self, value: Optional[pulumi.Input[ClusterPscConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupSource")
    def restore_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupSourceArgs]]: ...
    @restore_backup_source.setter
    def restore_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrBackupSource")
    def restore_backupdr_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]]: ...
    @restore_backupdr_backup_source.setter
    def restore_backupdr_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrPitrSource")
    def restore_backupdr_pitr_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]]: ...
    @restore_backupdr_pitr_source.setter
    def restore_backupdr_pitr_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreContinuousBackupSource")
    def restore_continuous_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]]: ...
    @restore_continuous_backup_source.setter
    def restore_continuous_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryConfig")
    def secondary_config(
        self,
    ) -> Optional[pulumi.Input[ClusterSecondaryConfigArgs]]: ...
    @secondary_config.setter
    def secondary_config(
        self, value: Optional[pulumi.Input[ClusterSecondaryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitMajorVersionUpgrade")
    def skip_await_major_version_upgrade(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_await_major_version_upgrade.setter
    def skip_await_major_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_type.setter
    def subscription_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyArgs]
        ] = ...,
        backup_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBackupSourceArgs]]]
        ] = ...,
        backupdr_backup_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBackupdrBackupSourceArgs]]]
        ] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        continuous_backup_config: Optional[
            pulumi.Input[ClusterContinuousBackupConfigArgs]
        ] = ...,
        continuous_backup_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterContinuousBackupInfoArgs]]]
        ] = ...,
        database_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplex_config: Optional[pulumi.Input[ClusterDataplexConfigArgs]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_config: Optional[pulumi.Input[ClusterEncryptionConfigArgs]] = ...,
        encryption_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionInfoArgs]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_user: Optional[pulumi.Input[ClusterInitialUserArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_update_policy: Optional[
            pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]
        ] = ...,
        migration_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterMigrationSourceArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[ClusterNetworkConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[pulumi.Input[ClusterPscConfigArgs]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        restore_backup_source: Optional[
            pulumi.Input[ClusterRestoreBackupSourceArgs]
        ] = ...,
        restore_backupdr_backup_source: Optional[
            pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]
        ] = ...,
        restore_backupdr_pitr_source: Optional[
            pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]
        ] = ...,
        restore_continuous_backup_source: Optional[
            pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]
        ] = ...,
        secondary_config: Optional[pulumi.Input[ClusterSecondaryConfigArgs]] = ...,
        skip_await_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trial_metadatas: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterTrialMetadataArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterAutomatedBackupPolicyArgs]]: ...
    @automated_backup_policy.setter
    def automated_backup_policy(
        self, value: Optional[pulumi.Input[ClusterAutomatedBackupPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupSources")
    def backup_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterBackupSourceArgs]]]]: ...
    @backup_sources.setter
    def backup_sources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterBackupSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupdrBackupSources")
    def backupdr_backup_sources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterBackupdrBackupSourceArgs]]]
    ]: ...
    @backupdr_backup_sources.setter
    def backupdr_backup_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBackupdrBackupSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="continuousBackupConfig")
    def continuous_backup_config(
        self,
    ) -> Optional[pulumi.Input[ClusterContinuousBackupConfigArgs]]: ...
    @continuous_backup_config.setter
    def continuous_backup_config(
        self, value: Optional[pulumi.Input[ClusterContinuousBackupConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="continuousBackupInfos")
    def continuous_backup_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterContinuousBackupInfoArgs]]]
    ]: ...
    @continuous_backup_infos.setter
    def continuous_backup_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterContinuousBackupInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_version.setter
    def database_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataplexConfig")
    def dataplex_config(self) -> Optional[pulumi.Input[ClusterDataplexConfigArgs]]: ...
    @dataplex_config.setter
    def dataplex_config(
        self, value: Optional[pulumi.Input[ClusterDataplexConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[ClusterEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[ClusterEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionInfoArgs]]]]: ...
    @encryption_infos.setter
    def encryption_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> Optional[pulumi.Input[ClusterInitialUserArgs]]: ...
    @initial_user.setter
    def initial_user(self, value: Optional[pulumi.Input[ClusterInitialUserArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceUpdatePolicy")
    def maintenance_update_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]]: ...
    @maintenance_update_policy.setter
    def maintenance_update_policy(
        self, value: Optional[pulumi.Input[ClusterMaintenanceUpdatePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationSources")
    def migration_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMigrationSourceArgs]]]]: ...
    @migration_sources.setter
    def migration_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterMigrationSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[ClusterNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[ClusterNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[ClusterPscConfigArgs]]: ...
    @psc_config.setter
    def psc_config(self, value: Optional[pulumi.Input[ClusterPscConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupSource")
    def restore_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupSourceArgs]]: ...
    @restore_backup_source.setter
    def restore_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrBackupSource")
    def restore_backupdr_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]]: ...
    @restore_backupdr_backup_source.setter
    def restore_backupdr_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupdrBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrPitrSource")
    def restore_backupdr_pitr_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]]: ...
    @restore_backupdr_pitr_source.setter
    def restore_backupdr_pitr_source(
        self, value: Optional[pulumi.Input[ClusterRestoreBackupdrPitrSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreContinuousBackupSource")
    def restore_continuous_backup_source(
        self,
    ) -> Optional[pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]]: ...
    @restore_continuous_backup_source.setter
    def restore_continuous_backup_source(
        self, value: Optional[pulumi.Input[ClusterRestoreContinuousBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryConfig")
    def secondary_config(
        self,
    ) -> Optional[pulumi.Input[ClusterSecondaryConfigArgs]]: ...
    @secondary_config.setter
    def secondary_config(
        self, value: Optional[pulumi.Input[ClusterSecondaryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitMajorVersionUpgrade")
    def skip_await_major_version_upgrade(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_await_major_version_upgrade.setter
    def skip_await_major_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_type.setter
    def subscription_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trialMetadatas")
    def trial_metadatas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterTrialMetadataArgs]]]]: ...
    @trial_metadatas.setter
    def trial_metadatas(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterTrialMetadataArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:alloydb/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterAutomatedBackupPolicyArgs,
                    ClusterAutomatedBackupPolicyArgsDict,
                ]
            ]
        ] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        continuous_backup_config: Optional[
            pulumi.Input[
                Union[
                    ClusterContinuousBackupConfigArgs,
                    ClusterContinuousBackupConfigArgsDict,
                ]
            ]
        ] = ...,
        database_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplex_config: Optional[
            pulumi.Input[
                Union[ClusterDataplexConfigArgs, ClusterDataplexConfigArgsDict]
            ]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[ClusterEncryptionConfigArgs, ClusterEncryptionConfigArgsDict]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_user: Optional[
            pulumi.Input[Union[ClusterInitialUserArgs, ClusterInitialUserArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_update_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterMaintenanceUpdatePolicyArgs,
                    ClusterMaintenanceUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
        network_config: Optional[
            pulumi.Input[Union[ClusterNetworkConfigArgs, ClusterNetworkConfigArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[
            pulumi.Input[Union[ClusterPscConfigArgs, ClusterPscConfigArgsDict]]
        ] = ...,
        restore_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupSourceArgs, ClusterRestoreBackupSourceArgsDict
                ]
            ]
        ] = ...,
        restore_backupdr_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupdrBackupSourceArgs,
                    ClusterRestoreBackupdrBackupSourceArgsDict,
                ]
            ]
        ] = ...,
        restore_backupdr_pitr_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupdrPitrSourceArgs,
                    ClusterRestoreBackupdrPitrSourceArgsDict,
                ]
            ]
        ] = ...,
        restore_continuous_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreContinuousBackupSourceArgs,
                    ClusterRestoreContinuousBackupSourceArgsDict,
                ]
            ]
        ] = ...,
        secondary_config: Optional[
            pulumi.Input[
                Union[ClusterSecondaryConfigArgs, ClusterSecondaryConfigArgsDict]
            ]
        ] = ...,
        skip_await_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        automated_backup_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterAutomatedBackupPolicyArgs,
                    ClusterAutomatedBackupPolicyArgsDict,
                ]
            ]
        ] = ...,
        backup_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClusterBackupSourceArgs, ClusterBackupSourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        backupdr_backup_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterBackupdrBackupSourceArgs,
                            ClusterBackupdrBackupSourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        continuous_backup_config: Optional[
            pulumi.Input[
                Union[
                    ClusterContinuousBackupConfigArgs,
                    ClusterContinuousBackupConfigArgsDict,
                ]
            ]
        ] = ...,
        continuous_backup_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterContinuousBackupInfoArgs,
                            ClusterContinuousBackupInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        database_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplex_config: Optional[
            pulumi.Input[
                Union[ClusterDataplexConfigArgs, ClusterDataplexConfigArgsDict]
            ]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[ClusterEncryptionConfigArgs, ClusterEncryptionConfigArgsDict]
            ]
        ] = ...,
        encryption_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClusterEncryptionInfoArgs, ClusterEncryptionInfoArgsDict]
                    ]
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_user: Optional[
            pulumi.Input[Union[ClusterInitialUserArgs, ClusterInitialUserArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_update_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterMaintenanceUpdatePolicyArgs,
                    ClusterMaintenanceUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
        migration_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterMigrationSourceArgs, ClusterMigrationSourceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[Union[ClusterNetworkConfigArgs, ClusterNetworkConfigArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_config: Optional[
            pulumi.Input[Union[ClusterPscConfigArgs, ClusterPscConfigArgsDict]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        restore_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupSourceArgs, ClusterRestoreBackupSourceArgsDict
                ]
            ]
        ] = ...,
        restore_backupdr_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupdrBackupSourceArgs,
                    ClusterRestoreBackupdrBackupSourceArgsDict,
                ]
            ]
        ] = ...,
        restore_backupdr_pitr_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreBackupdrPitrSourceArgs,
                    ClusterRestoreBackupdrPitrSourceArgsDict,
                ]
            ]
        ] = ...,
        restore_continuous_backup_source: Optional[
            pulumi.Input[
                Union[
                    ClusterRestoreContinuousBackupSourceArgs,
                    ClusterRestoreContinuousBackupSourceArgsDict,
                ]
            ]
        ] = ...,
        secondary_config: Optional[
            pulumi.Input[
                Union[ClusterSecondaryConfigArgs, ClusterSecondaryConfigArgsDict]
            ]
        ] = ...,
        skip_await_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trial_metadatas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClusterTrialMetadataArgs, ClusterTrialMetadataArgsDict]
                    ]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupPolicy")
    def automated_backup_policy(
        self,
    ) -> pulumi.Output[outputs.ClusterAutomatedBackupPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="backupSources")
    def backup_sources(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="backupdrBackupSources")
    def backupdr_backup_sources(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterBackupdrBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="continuousBackupConfig")
    def continuous_backup_config(
        self,
    ) -> pulumi.Output[outputs.ClusterContinuousBackupConfig]: ...
    @_builtins.property
    @pulumi.getter(name="continuousBackupInfos")
    def continuous_backup_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterContinuousBackupInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataplexConfig")
    def dataplex_config(self) -> pulumi.Output[outputs.ClusterDataplexConfig]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterEncryptionConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterEncryptionInfo]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> pulumi.Output[Optional[outputs.ClusterInitialUser]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceUpdatePolicy")
    def maintenance_update_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterMaintenanceUpdatePolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationSources")
    def migration_sources(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterMigrationSource]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.ClusterNetworkConfig]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> pulumi.Output[Optional[outputs.ClusterPscConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupSource")
    def restore_backup_source(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRestoreBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrBackupSource")
    def restore_backupdr_backup_source(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRestoreBackupdrBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="restoreBackupdrPitrSource")
    def restore_backupdr_pitr_source(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRestoreBackupdrPitrSource]]: ...
    @_builtins.property
    @pulumi.getter(name="restoreContinuousBackupSource")
    def restore_continuous_backup_source(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterRestoreContinuousBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryConfig")
    def secondary_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterSecondaryConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitMajorVersionUpgrade")
    def skip_await_major_version_upgrade(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trialMetadatas")
    def trial_metadatas(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterTrialMetadata]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
