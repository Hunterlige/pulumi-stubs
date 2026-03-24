

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupVaultBackupRetentionPolicy', 'VolumeBackupConfig', 'VolumeBlockDevice', 'VolumeCacheParameters', 'VolumeCacheParametersCacheConfig', 'VolumeExportPolicy', 'VolumeExportPolicyRule', 'VolumeHybridReplicationParameters', 'VolumeLargeCapacityConfig', 'VolumeMountOption', 'VolumeReplicationDestinationVolumeParameters', ..., 'VolumeReplicationHybridPeeringDetail', 'VolumeReplicationHybridReplicationUserCommand', 'VolumeReplicationTransferStat', 'VolumeRestoreParameters', 'VolumeSnapshotPolicy', 'VolumeSnapshotPolicyDailySchedule', 'VolumeSnapshotPolicyHourlySchedule', 'VolumeSnapshotPolicyMonthlySchedule', 'VolumeSnapshotPolicyWeeklySchedule', 'VolumeTieringPolicy']
@pulumi.output_type
class BackupVaultBackupRetentionPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_minimum_enforced_retention_days: _builtins.int, daily_backup_immutable: Optional[_builtins.bool] = ..., manual_backup_immutable: Optional[_builtins.bool] = ..., monthly_backup_immutable: Optional[_builtins.bool] = ..., weekly_backup_immutable: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDays")
    def backup_minimum_enforced_retention_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyBackupImmutable")
    def daily_backup_immutable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualBackupImmutable")
    def manual_backup_immutable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBackupImmutable")
    def monthly_backup_immutable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyBackupImmutable")
    def weekly_backup_immutable(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VolumeBackupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_policies: Optional[Sequence[_builtins.str]] = ..., backup_vault: Optional[_builtins.str] = ..., scheduled_backup_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicies")
    def backup_policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackupEnabled")
    def scheduled_backup_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VolumeBlockDevice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_type: _builtins.str, host_groups: Optional[Sequence[_builtins.str]] = ..., identifier: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., size_gib: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroups")
    def host_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeCacheParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_config: Optional[outputs.VolumeCacheParametersCacheConfig] = ..., cache_state: Optional[_builtins.str] = ..., command: Optional[_builtins.str] = ..., enable_global_file_lock: Optional[_builtins.bool] = ..., passphrase: Optional[_builtins.str] = ..., peer_cluster_name: Optional[_builtins.str] = ..., peer_ip_addresses: Optional[Sequence[_builtins.str]] = ..., peer_svm_name: Optional[_builtins.str] = ..., peer_volume_name: Optional[_builtins.str] = ..., peering_command_expiry_time: Optional[_builtins.str] = ..., state_details: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfig")
    def cache_config(self) -> Optional[outputs.VolumeCacheParametersCacheConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheState")
    def cache_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGlobalFileLock")
    def enable_global_file_lock(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddresses")
    def peer_ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringCommandExpiryTime")
    def peering_command_expiry_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeCacheParametersCacheConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cifs_change_notify_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cifsChangeNotifyEnabled")
    def cifs_change_notify_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VolumeExportPolicy(dict):
    def __init__(__self__, *, rules: Sequence[outputs.VolumeExportPolicyRule]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.VolumeExportPolicyRule]:
        
        ...
    


@pulumi.output_type
class VolumeExportPolicyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_type: Optional[_builtins.str] = ..., allowed_clients: Optional[_builtins.str] = ..., anon_uid: Optional[_builtins.int] = ..., has_root_access: Optional[_builtins.str] = ..., kerberos5_read_only: Optional[_builtins.bool] = ..., kerberos5_read_write: Optional[_builtins.bool] = ..., kerberos5i_read_only: Optional[_builtins.bool] = ..., kerberos5i_read_write: Optional[_builtins.bool] = ..., kerberos5p_read_only: Optional[_builtins.bool] = ..., kerberos5p_read_write: Optional[_builtins.bool] = ..., nfsv3: Optional[_builtins.bool] = ..., nfsv4: Optional[_builtins.bool] = ..., squash_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonUid")
    def anon_uid(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasRootAccess")
    def has_root_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadOnly")
    def kerberos5_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadWrite")
    def kerberos5_read_write(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadOnly")
    def kerberos5i_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadWrite")
    def kerberos5i_read_write(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadOnly")
    def kerberos5p_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadWrite")
    def kerberos5p_read_write(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv3(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv4(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeHybridReplicationParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_location: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., hybrid_replication_type: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., large_volume_constituent_count: Optional[_builtins.int] = ..., peer_cluster_name: Optional[_builtins.str] = ..., peer_ip_addresses: Optional[Sequence[_builtins.str]] = ..., peer_svm_name: Optional[_builtins.str] = ..., peer_volume_name: Optional[_builtins.str] = ..., replication: Optional[_builtins.str] = ..., replication_schedule: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationType")
    def hybrid_replication_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeVolumeConstituentCount")
    def large_volume_constituent_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddresses")
    def peer_ip_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replication(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeLargeCapacityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, constituent_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="constituentCount")
    def constituent_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeMountOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, export: Optional[_builtins.str] = ..., export_full: Optional[_builtins.str] = ..., instructions: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFull")
    def export_full(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeReplicationDestinationVolumeParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_pool: _builtins.str, description: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ..., tiering_policy: Optional[outputs.VolumeReplicationDestinationVolumeParametersTieringPolicy] = ..., volume_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[outputs.VolumeReplicationDestinationVolumeParametersTieringPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeReplicationDestinationVolumeParametersTieringPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cooling_threshold_days: Optional[_builtins.int] = ..., tier_action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolingThresholdDays")
    def cooling_threshold_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tierAction")
    def tier_action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeReplicationHybridPeeringDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, command: Optional[_builtins.str] = ..., command_expiry_time: Optional[_builtins.str] = ..., passphrase: Optional[_builtins.str] = ..., peer_cluster_name: Optional[_builtins.str] = ..., peer_svm_name: Optional[_builtins.str] = ..., peer_volume_name: Optional[_builtins.str] = ..., subnet_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandExpiryTime")
    def command_expiry_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIp")
    def subnet_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeReplicationHybridReplicationUserCommand(dict):
    def __init__(__self__, *, commands: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VolumeReplicationTransferStat(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lag_duration: Optional[_builtins.str] = ..., last_transfer_bytes: Optional[_builtins.str] = ..., last_transfer_duration: Optional[_builtins.str] = ..., last_transfer_end_time: Optional[_builtins.str] = ..., last_transfer_error: Optional[_builtins.str] = ..., total_transfer_duration: Optional[_builtins.str] = ..., transfer_bytes: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lagDuration")
    def lag_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferBytes")
    def last_transfer_bytes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferDuration")
    def last_transfer_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferEndTime")
    def last_transfer_end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferError")
    def last_transfer_error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalTransferDuration")
    def total_transfer_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferBytes")
    def transfer_bytes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeRestoreParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_backup: Optional[_builtins.str] = ..., source_snapshot: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBackup")
    def source_backup(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeSnapshotPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, daily_schedule: Optional[outputs.VolumeSnapshotPolicyDailySchedule] = ..., enabled: Optional[_builtins.bool] = ..., hourly_schedule: Optional[outputs.VolumeSnapshotPolicyHourlySchedule] = ..., monthly_schedule: Optional[outputs.VolumeSnapshotPolicyMonthlySchedule] = ..., weekly_schedule: Optional[outputs.VolumeSnapshotPolicyWeeklySchedule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[outputs.VolumeSnapshotPolicyDailySchedule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[outputs.VolumeSnapshotPolicyHourlySchedule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[outputs.VolumeSnapshotPolicyMonthlySchedule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[outputs.VolumeSnapshotPolicyWeeklySchedule]:
        
        ...
    


@pulumi.output_type
class VolumeSnapshotPolicyDailySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshots_to_keep: _builtins.int, hour: Optional[_builtins.int] = ..., minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeSnapshotPolicyHourlySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshots_to_keep: _builtins.int, minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeSnapshotPolicyMonthlySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshots_to_keep: _builtins.int, days_of_month: Optional[_builtins.str] = ..., hour: Optional[_builtins.int] = ..., minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeSnapshotPolicyWeeklySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshots_to_keep: _builtins.int, day: Optional[_builtins.str] = ..., hour: Optional[_builtins.int] = ..., minute: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VolumeTieringPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cooling_threshold_days: Optional[_builtins.int] = ..., hot_tier_bypass_mode_enabled: Optional[_builtins.bool] = ..., tier_action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolingThresholdDays")
    def cooling_threshold_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierBypassModeEnabled")
    def hot_tier_bypass_mode_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tierAction")
    def tier_action(self) -> Optional[_builtins.str]:
        
        ...
    


