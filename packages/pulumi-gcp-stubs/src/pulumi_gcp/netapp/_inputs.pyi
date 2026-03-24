

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupVaultBackupRetentionPolicyArgs', 'BackupVaultBackupRetentionPolicyArgsDict', 'VolumeBackupConfigArgs', 'VolumeBackupConfigArgsDict', 'VolumeBlockDeviceArgs', 'VolumeBlockDeviceArgsDict', 'VolumeCacheParametersArgs', 'VolumeCacheParametersArgsDict', 'VolumeCacheParametersCacheConfigArgs', 'VolumeCacheParametersCacheConfigArgsDict', 'VolumeExportPolicyArgs', 'VolumeExportPolicyArgsDict', 'VolumeExportPolicyRuleArgs', 'VolumeExportPolicyRuleArgsDict', 'VolumeHybridReplicationParametersArgs', 'VolumeHybridReplicationParametersArgsDict', 'VolumeLargeCapacityConfigArgs', 'VolumeLargeCapacityConfigArgsDict', 'VolumeMountOptionArgs', 'VolumeMountOptionArgsDict', 'VolumeReplicationDestinationVolumeParametersArgs', ..., ..., ..., 'VolumeReplicationHybridPeeringDetailArgs', 'VolumeReplicationHybridPeeringDetailArgsDict', 'VolumeReplicationHybridReplicationUserCommandArgs', ..., 'VolumeReplicationTransferStatArgs', 'VolumeReplicationTransferStatArgsDict', 'VolumeRestoreParametersArgs', 'VolumeRestoreParametersArgsDict', 'VolumeSnapshotPolicyArgs', 'VolumeSnapshotPolicyArgsDict', 'VolumeSnapshotPolicyDailyScheduleArgs', 'VolumeSnapshotPolicyDailyScheduleArgsDict', 'VolumeSnapshotPolicyHourlyScheduleArgs', 'VolumeSnapshotPolicyHourlyScheduleArgsDict', 'VolumeSnapshotPolicyMonthlyScheduleArgs', 'VolumeSnapshotPolicyMonthlyScheduleArgsDict', 'VolumeSnapshotPolicyWeeklyScheduleArgs', 'VolumeSnapshotPolicyWeeklyScheduleArgsDict', 'VolumeTieringPolicyArgs', 'VolumeTieringPolicyArgsDict']
class BackupVaultBackupRetentionPolicyArgsDict(TypedDict):
    backup_minimum_enforced_retention_days: pulumi.Input[_builtins.int]
    daily_backup_immutable: NotRequired[pulumi.Input[_builtins.bool]]
    manual_backup_immutable: NotRequired[pulumi.Input[_builtins.bool]]
    monthly_backup_immutable: NotRequired[pulumi.Input[_builtins.bool]]
    weekly_backup_immutable: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BackupVaultBackupRetentionPolicyArgs:
    def __init__(__self__, *, backup_minimum_enforced_retention_days: pulumi.Input[_builtins.int], daily_backup_immutable: Optional[pulumi.Input[_builtins.bool]] = ..., manual_backup_immutable: Optional[pulumi.Input[_builtins.bool]] = ..., monthly_backup_immutable: Optional[pulumi.Input[_builtins.bool]] = ..., weekly_backup_immutable: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupMinimumEnforcedRetentionDays")
    def backup_minimum_enforced_retention_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @backup_minimum_enforced_retention_days.setter
    def backup_minimum_enforced_retention_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyBackupImmutable")
    def daily_backup_immutable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @daily_backup_immutable.setter
    def daily_backup_immutable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualBackupImmutable")
    def manual_backup_immutable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @manual_backup_immutable.setter
    def manual_backup_immutable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBackupImmutable")
    def monthly_backup_immutable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @monthly_backup_immutable.setter
    def monthly_backup_immutable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyBackupImmutable")
    def weekly_backup_immutable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @weekly_backup_immutable.setter
    def weekly_backup_immutable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VolumeBackupConfigArgsDict(TypedDict):
    backup_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    backup_vault: NotRequired[pulumi.Input[_builtins.str]]
    scheduled_backup_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VolumeBackupConfigArgs:
    def __init__(__self__, *, backup_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_vault: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicies")
    def backup_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backup_policies.setter
    def backup_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault.setter
    def backup_vault(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackupEnabled")
    def scheduled_backup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @scheduled_backup_enabled.setter
    def scheduled_backup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VolumeBlockDeviceArgsDict(TypedDict):
    os_type: pulumi.Input[_builtins.str]
    host_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identifier: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    size_gib: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeBlockDeviceArgs:
    def __init__(__self__, *, os_type: pulumi.Input[_builtins.str], host_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., size_gib: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroups")
    def host_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @host_groups.setter
    def host_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeCacheParametersArgsDict(TypedDict):
    cache_config: NotRequired[pulumi.Input[VolumeCacheParametersCacheConfigArgsDict]]
    cache_state: NotRequired[pulumi.Input[_builtins.str]]
    command: NotRequired[pulumi.Input[_builtins.str]]
    enable_global_file_lock: NotRequired[pulumi.Input[_builtins.bool]]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    peer_cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    peer_svm_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_volume_name: NotRequired[pulumi.Input[_builtins.str]]
    peering_command_expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    state_details: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeCacheParametersArgs:
    def __init__(__self__, *, cache_config: Optional[pulumi.Input[VolumeCacheParametersCacheConfigArgs]] = ..., cache_state: Optional[pulumi.Input[_builtins.str]] = ..., command: Optional[pulumi.Input[_builtins.str]] = ..., enable_global_file_lock: Optional[pulumi.Input[_builtins.bool]] = ..., passphrase: Optional[pulumi.Input[_builtins.str]] = ..., peer_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., peer_svm_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_volume_name: Optional[pulumi.Input[_builtins.str]] = ..., peering_command_expiry_time: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfig")
    def cache_config(self) -> Optional[pulumi.Input[VolumeCacheParametersCacheConfigArgs]]:
        
        ...
    
    @cache_config.setter
    def cache_config(self, value: Optional[pulumi.Input[VolumeCacheParametersCacheConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheState")
    def cache_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_state.setter
    def cache_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @command.setter
    def command(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGlobalFileLock")
    def enable_global_file_lock(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_global_file_lock.setter
    def enable_global_file_lock(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_cluster_name.setter
    def peer_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddresses")
    def peer_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @peer_ip_addresses.setter
    def peer_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_svm_name.setter
    def peer_svm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_volume_name.setter
    def peer_volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringCommandExpiryTime")
    def peering_command_expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_command_expiry_time.setter
    def peering_command_expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_details.setter
    def state_details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeCacheParametersCacheConfigArgsDict(TypedDict):
    cifs_change_notify_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VolumeCacheParametersCacheConfigArgs:
    def __init__(__self__, *, cifs_change_notify_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cifsChangeNotifyEnabled")
    def cifs_change_notify_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cifs_change_notify_enabled.setter
    def cifs_change_notify_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VolumeExportPolicyArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[VolumeExportPolicyRuleArgsDict]]]


@pulumi.input_type
class VolumeExportPolicyArgs:
    def __init__(__self__, *, rules: pulumi.Input[Sequence[pulumi.Input[VolumeExportPolicyRuleArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[VolumeExportPolicyRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[VolumeExportPolicyRuleArgs]]]): # -> None:
        ...
    


class VolumeExportPolicyRuleArgsDict(TypedDict):
    access_type: NotRequired[pulumi.Input[_builtins.str]]
    allowed_clients: NotRequired[pulumi.Input[_builtins.str]]
    anon_uid: NotRequired[pulumi.Input[_builtins.int]]
    has_root_access: NotRequired[pulumi.Input[_builtins.str]]
    kerberos5_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5i_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5i_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5p_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5p_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    nfsv3: NotRequired[pulumi.Input[_builtins.bool]]
    nfsv4: NotRequired[pulumi.Input[_builtins.bool]]
    squash_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeExportPolicyRuleArgs:
    def __init__(__self__, *, access_type: Optional[pulumi.Input[_builtins.str]] = ..., allowed_clients: Optional[pulumi.Input[_builtins.str]] = ..., anon_uid: Optional[pulumi.Input[_builtins.int]] = ..., has_root_access: Optional[pulumi.Input[_builtins.str]] = ..., kerberos5_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5i_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5i_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5p_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5p_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., nfsv3: Optional[pulumi.Input[_builtins.bool]] = ..., nfsv4: Optional[pulumi.Input[_builtins.bool]] = ..., squash_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allowed_clients.setter
    def allowed_clients(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonUid")
    def anon_uid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @anon_uid.setter
    def anon_uid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasRootAccess")
    def has_root_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @has_root_access.setter
    def has_root_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadOnly")
    def kerberos5_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_read_only.setter
    def kerberos5_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadWrite")
    def kerberos5_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_read_write.setter
    def kerberos5_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadOnly")
    def kerberos5i_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5i_read_only.setter
    def kerberos5i_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadWrite")
    def kerberos5i_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5i_read_write.setter
    def kerberos5i_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadOnly")
    def kerberos5p_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5p_read_only.setter
    def kerberos5p_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadWrite")
    def kerberos5p_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5p_read_write.setter
    def kerberos5p_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv3(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @nfsv3.setter
    def nfsv3(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv4(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @nfsv4.setter
    def nfsv4(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @squash_mode.setter
    def squash_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeHybridReplicationParametersArgsDict(TypedDict):
    cluster_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    hybrid_replication_type: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    large_volume_constituent_count: NotRequired[pulumi.Input[_builtins.int]]
    peer_cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    peer_svm_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_volume_name: NotRequired[pulumi.Input[_builtins.str]]
    replication: NotRequired[pulumi.Input[_builtins.str]]
    replication_schedule: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeHybridReplicationParametersArgs:
    def __init__(__self__, *, cluster_location: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_replication_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., large_volume_constituent_count: Optional[pulumi.Input[_builtins.int]] = ..., peer_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., peer_svm_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_volume_name: Optional[pulumi.Input[_builtins.str]] = ..., replication: Optional[pulumi.Input[_builtins.str]] = ..., replication_schedule: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_location.setter
    def cluster_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationType")
    def hybrid_replication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hybrid_replication_type.setter
    def hybrid_replication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeVolumeConstituentCount")
    def large_volume_constituent_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @large_volume_constituent_count.setter
    def large_volume_constituent_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_cluster_name.setter
    def peer_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddresses")
    def peer_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @peer_ip_addresses.setter
    def peer_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_svm_name.setter
    def peer_svm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_volume_name.setter
    def peer_volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replication(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication.setter
    def replication(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_schedule.setter
    def replication_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeLargeCapacityConfigArgsDict(TypedDict):
    constituent_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeLargeCapacityConfigArgs:
    def __init__(__self__, *, constituent_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="constituentCount")
    def constituent_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @constituent_count.setter
    def constituent_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeMountOptionArgsDict(TypedDict):
    export: NotRequired[pulumi.Input[_builtins.str]]
    export_full: NotRequired[pulumi.Input[_builtins.str]]
    instructions: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeMountOptionArgs:
    def __init__(__self__, *, export: Optional[pulumi.Input[_builtins.str]] = ..., export_full: Optional[pulumi.Input[_builtins.str]] = ..., instructions: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export.setter
    def export(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFull")
    def export_full(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_full.setter
    def export_full(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instructions.setter
    def instructions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeReplicationDestinationVolumeParametersArgsDict(TypedDict):
    storage_pool: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    share_name: NotRequired[pulumi.Input[_builtins.str]]
    tiering_policy: NotRequired[pulumi.Input[VolumeReplicationDestinationVolumeParametersTieringPolicyArgsDict]]
    volume_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeReplicationDestinationVolumeParametersArgs:
    def __init__(__self__, *, storage_pool: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., tiering_policy: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersTieringPolicyArgs]] = ..., volume_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_pool.setter
    def storage_pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersTieringPolicyArgs]]:
        
        ...
    
    @tiering_policy.setter
    def tiering_policy(self, value: Optional[pulumi.Input[VolumeReplicationDestinationVolumeParametersTieringPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeReplicationDestinationVolumeParametersTieringPolicyArgsDict(TypedDict):
    cooling_threshold_days: NotRequired[pulumi.Input[_builtins.int]]
    tier_action: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeReplicationDestinationVolumeParametersTieringPolicyArgs:
    def __init__(__self__, *, cooling_threshold_days: Optional[pulumi.Input[_builtins.int]] = ..., tier_action: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolingThresholdDays")
    def cooling_threshold_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooling_threshold_days.setter
    def cooling_threshold_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tierAction")
    def tier_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier_action.setter
    def tier_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeReplicationHybridPeeringDetailArgsDict(TypedDict):
    command: NotRequired[pulumi.Input[_builtins.str]]
    command_expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    peer_cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_svm_name: NotRequired[pulumi.Input[_builtins.str]]
    peer_volume_name: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ip: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeReplicationHybridPeeringDetailArgs:
    def __init__(__self__, *, command: Optional[pulumi.Input[_builtins.str]] = ..., command_expiry_time: Optional[pulumi.Input[_builtins.str]] = ..., passphrase: Optional[pulumi.Input[_builtins.str]] = ..., peer_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_svm_name: Optional[pulumi.Input[_builtins.str]] = ..., peer_volume_name: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @command.setter
    def command(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandExpiryTime")
    def command_expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @command_expiry_time.setter
    def command_expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_cluster_name.setter
    def peer_cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSvmName")
    def peer_svm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_svm_name.setter
    def peer_svm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_volume_name.setter
    def peer_volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIp")
    def subnet_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_ip.setter
    def subnet_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeReplicationHybridReplicationUserCommandArgsDict(TypedDict):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VolumeReplicationHybridReplicationUserCommandArgs:
    def __init__(__self__, *, commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VolumeReplicationTransferStatArgsDict(TypedDict):
    lag_duration: NotRequired[pulumi.Input[_builtins.str]]
    last_transfer_bytes: NotRequired[pulumi.Input[_builtins.str]]
    last_transfer_duration: NotRequired[pulumi.Input[_builtins.str]]
    last_transfer_end_time: NotRequired[pulumi.Input[_builtins.str]]
    last_transfer_error: NotRequired[pulumi.Input[_builtins.str]]
    total_transfer_duration: NotRequired[pulumi.Input[_builtins.str]]
    transfer_bytes: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeReplicationTransferStatArgs:
    def __init__(__self__, *, lag_duration: Optional[pulumi.Input[_builtins.str]] = ..., last_transfer_bytes: Optional[pulumi.Input[_builtins.str]] = ..., last_transfer_duration: Optional[pulumi.Input[_builtins.str]] = ..., last_transfer_end_time: Optional[pulumi.Input[_builtins.str]] = ..., last_transfer_error: Optional[pulumi.Input[_builtins.str]] = ..., total_transfer_duration: Optional[pulumi.Input[_builtins.str]] = ..., transfer_bytes: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lagDuration")
    def lag_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lag_duration.setter
    def lag_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferBytes")
    def last_transfer_bytes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_transfer_bytes.setter
    def last_transfer_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferDuration")
    def last_transfer_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_transfer_duration.setter
    def last_transfer_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferEndTime")
    def last_transfer_end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_transfer_end_time.setter
    def last_transfer_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransferError")
    def last_transfer_error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_transfer_error.setter
    def last_transfer_error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalTransferDuration")
    def total_transfer_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_transfer_duration.setter
    def total_transfer_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferBytes")
    def transfer_bytes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transfer_bytes.setter
    def transfer_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeRestoreParametersArgsDict(TypedDict):
    source_backup: NotRequired[pulumi.Input[_builtins.str]]
    source_snapshot: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeRestoreParametersArgs:
    def __init__(__self__, *, source_backup: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBackup")
    def source_backup(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_backup.setter
    def source_backup(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot.setter
    def source_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeSnapshotPolicyArgsDict(TypedDict):
    daily_schedule: NotRequired[pulumi.Input[VolumeSnapshotPolicyDailyScheduleArgsDict]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    hourly_schedule: NotRequired[pulumi.Input[VolumeSnapshotPolicyHourlyScheduleArgsDict]]
    monthly_schedule: NotRequired[pulumi.Input[VolumeSnapshotPolicyMonthlyScheduleArgsDict]]
    weekly_schedule: NotRequired[pulumi.Input[VolumeSnapshotPolicyWeeklyScheduleArgsDict]]


@pulumi.input_type
class VolumeSnapshotPolicyArgs:
    def __init__(__self__, *, daily_schedule: Optional[pulumi.Input[VolumeSnapshotPolicyDailyScheduleArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., hourly_schedule: Optional[pulumi.Input[VolumeSnapshotPolicyHourlyScheduleArgs]] = ..., monthly_schedule: Optional[pulumi.Input[VolumeSnapshotPolicyMonthlyScheduleArgs]] = ..., weekly_schedule: Optional[pulumi.Input[VolumeSnapshotPolicyWeeklyScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyDailyScheduleArgs]]:
        
        ...
    
    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyDailyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyHourlyScheduleArgs]]:
        
        ...
    
    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyHourlyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyMonthlyScheduleArgs]]:
        
        ...
    
    @monthly_schedule.setter
    def monthly_schedule(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyMonthlyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyWeeklyScheduleArgs]]:
        
        ...
    
    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyWeeklyScheduleArgs]]): # -> None:
        ...
    


class VolumeSnapshotPolicyDailyScheduleArgsDict(TypedDict):
    snapshots_to_keep: pulumi.Input[_builtins.int]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeSnapshotPolicyDailyScheduleArgs:
    def __init__(__self__, *, snapshots_to_keep: pulumi.Input[_builtins.int], hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeSnapshotPolicyHourlyScheduleArgsDict(TypedDict):
    snapshots_to_keep: pulumi.Input[_builtins.int]
    minute: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeSnapshotPolicyHourlyScheduleArgs:
    def __init__(__self__, *, snapshots_to_keep: pulumi.Input[_builtins.int], minute: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeSnapshotPolicyMonthlyScheduleArgsDict(TypedDict):
    snapshots_to_keep: pulumi.Input[_builtins.int]
    days_of_month: NotRequired[pulumi.Input[_builtins.str]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeSnapshotPolicyMonthlyScheduleArgs:
    def __init__(__self__, *, snapshots_to_keep: pulumi.Input[_builtins.int], days_of_month: Optional[pulumi.Input[_builtins.str]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @days_of_month.setter
    def days_of_month(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeSnapshotPolicyWeeklyScheduleArgsDict(TypedDict):
    snapshots_to_keep: pulumi.Input[_builtins.int]
    day: NotRequired[pulumi.Input[_builtins.str]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VolumeSnapshotPolicyWeeklyScheduleArgs:
    def __init__(__self__, *, snapshots_to_keep: pulumi.Input[_builtins.int], day: Optional[pulumi.Input[_builtins.str]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VolumeTieringPolicyArgsDict(TypedDict):
    cooling_threshold_days: NotRequired[pulumi.Input[_builtins.int]]
    hot_tier_bypass_mode_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    tier_action: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeTieringPolicyArgs:
    def __init__(__self__, *, cooling_threshold_days: Optional[pulumi.Input[_builtins.int]] = ..., hot_tier_bypass_mode_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., tier_action: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolingThresholdDays")
    def cooling_threshold_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooling_threshold_days.setter
    def cooling_threshold_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierBypassModeEnabled")
    def hot_tier_bypass_mode_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hot_tier_bypass_mode_enabled.setter
    def hot_tier_bypass_mode_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tierAction")
    def tier_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier_action.setter
    def tier_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


