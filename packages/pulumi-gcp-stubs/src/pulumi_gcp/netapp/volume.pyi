

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VolumeArgs', 'Volume']
@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *, capacity_gib: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], storage_pool: pulumi.Input[_builtins.str], backup_config: Optional[pulumi.Input[VolumeBackupConfigArgs]] = ..., block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]] = ..., cache_parameters: Optional[pulumi.Input[VolumeCacheParametersArgs]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., export_policy: Optional[pulumi.Input[VolumeExportPolicyArgs]] = ..., hybrid_replication_parameters: Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]] = ..., kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., large_capacity: Optional[pulumi.Input[_builtins.bool]] = ..., large_capacity_config: Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]] = ..., multiple_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., restore_parameters: Optional[pulumi.Input[VolumeRestoreParametersArgs]] = ..., restricted_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_style: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., smb_settings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_directory: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_policy: Optional[pulumi.Input[VolumeSnapshotPolicyArgs]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., tiering_policy: Optional[pulumi.Input[VolumeTieringPolicyArgs]] = ..., unix_permissions: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @capacity_gib.setter
    def capacity_gib(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @protocols.setter
    def protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_pool.setter
    def storage_pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> Optional[pulumi.Input[VolumeBackupConfigArgs]]:
        
        ...
    
    @backup_config.setter
    def backup_config(self, value: Optional[pulumi.Input[VolumeBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDevices")
    def block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]]:
        
        ...
    
    @block_devices.setter
    def block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheParameters")
    def cache_parameters(self) -> Optional[pulumi.Input[VolumeCacheParametersArgs]]:
        
        ...
    
    @cache_parameters.setter
    def cache_parameters(self, value: Optional[pulumi.Input[VolumeCacheParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[VolumeExportPolicyArgs]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[VolumeExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationParameters")
    def hybrid_replication_parameters(self) -> Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]]:
        
        ...
    
    @hybrid_replication_parameters.setter
    def hybrid_replication_parameters(self, value: Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos_enabled.setter
    def kerberos_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacity")
    def large_capacity(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @large_capacity.setter
    def large_capacity(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacityConfig")
    def large_capacity_config(self) -> Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]]:
        
        ...
    
    @large_capacity_config.setter
    def large_capacity_config(self, value: Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleEndpoints")
    def multiple_endpoints(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multiple_endpoints.setter
    def multiple_endpoints(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[VolumeRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[VolumeRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedActions")
    def restricted_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @restricted_actions.setter
    def restricted_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSettings")
    def smb_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @smb_settings.setter
    def smb_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDirectory")
    def snapshot_directory(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @snapshot_directory.setter
    def snapshot_directory(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyArgs]]:
        
        ...
    
    @snapshot_policy.setter
    def snapshot_policy(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[pulumi.Input[VolumeTieringPolicyArgs]]:
        
        ...
    
    @tiering_policy.setter
    def tiering_policy(self, value: Optional[pulumi.Input[VolumeTieringPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unix_permissions.setter
    def unix_permissions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *, active_directory: Optional[pulumi.Input[_builtins.str]] = ..., backup_config: Optional[pulumi.Input[VolumeBackupConfigArgs]] = ..., block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]] = ..., cache_parameters: Optional[pulumi.Input[VolumeCacheParametersArgs]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., cold_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., export_policy: Optional[pulumi.Input[VolumeExportPolicyArgs]] = ..., has_replication: Optional[pulumi.Input[_builtins.bool]] = ..., hot_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_replication_parameters: Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]] = ..., kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., large_capacity: Optional[pulumi.Input[_builtins.bool]] = ..., large_capacity_config: Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mount_options: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountOptionArgs]]]] = ..., multiple_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., psa_range: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., restore_parameters: Optional[pulumi.Input[VolumeRestoreParametersArgs]] = ..., restricted_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_style: Optional[pulumi.Input[_builtins.str]] = ..., service_level: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., smb_settings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_directory: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_policy: Optional[pulumi.Input[VolumeSnapshotPolicyArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., storage_pool: Optional[pulumi.Input[_builtins.str]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., tiering_policy: Optional[pulumi.Input[VolumeTieringPolicyArgs]] = ..., unix_permissions: Optional[pulumi.Input[_builtins.str]] = ..., used_gib: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory.setter
    def active_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> Optional[pulumi.Input[VolumeBackupConfigArgs]]:
        
        ...
    
    @backup_config.setter
    def backup_config(self, value: Optional[pulumi.Input[VolumeBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDevices")
    def block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]]:
        
        ...
    
    @block_devices.setter
    def block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheParameters")
    def cache_parameters(self) -> Optional[pulumi.Input[VolumeCacheParametersArgs]]:
        
        ...
    
    @cache_parameters.setter
    def cache_parameters(self, value: Optional[pulumi.Input[VolumeCacheParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_gib.setter
    def capacity_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coldTierSizeGib")
    def cold_tier_size_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cold_tier_size_gib.setter
    def cold_tier_size_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[VolumeExportPolicyArgs]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[VolumeExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasReplication")
    def has_replication(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_replication.setter
    def has_replication(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeUsedGib")
    def hot_tier_size_used_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hot_tier_size_used_gib.setter
    def hot_tier_size_used_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationParameters")
    def hybrid_replication_parameters(self) -> Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]]:
        
        ...
    
    @hybrid_replication_parameters.setter
    def hybrid_replication_parameters(self, value: Optional[pulumi.Input[VolumeHybridReplicationParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos_enabled.setter
    def kerberos_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfig")
    def kms_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_config.setter
    def kms_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacity")
    def large_capacity(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @large_capacity.setter
    def large_capacity(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacityConfig")
    def large_capacity_config(self) -> Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]]:
        
        ...
    
    @large_capacity_config.setter
    def large_capacity_config(self, value: Optional[pulumi.Input[VolumeLargeCapacityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_enabled.setter
    def ldap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountOptionArgs]]]]:
        
        ...
    
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountOptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleEndpoints")
    def multiple_endpoints(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multiple_endpoints.setter
    def multiple_endpoints(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @protocols.setter
    def protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaRange")
    def psa_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @psa_range.setter
    def psa_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZone")
    def replica_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_zone.setter
    def replica_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input[VolumeRestoreParametersArgs]]:
        
        ...
    
    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input[VolumeRestoreParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedActions")
    def restricted_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @restricted_actions.setter
    def restricted_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_level.setter
    def service_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSettings")
    def smb_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @smb_settings.setter
    def smb_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDirectory")
    def snapshot_directory(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @snapshot_directory.setter
    def snapshot_directory(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> Optional[pulumi.Input[VolumeSnapshotPolicyArgs]]:
        
        ...
    
    @snapshot_policy.setter
    def snapshot_policy(self, value: Optional[pulumi.Input[VolumeSnapshotPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_details.setter
    def state_details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_pool.setter
    def storage_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> Optional[pulumi.Input[VolumeTieringPolicyArgs]]:
        
        ...
    
    @tiering_policy.setter
    def tiering_policy(self, value: Optional[pulumi.Input[VolumeTieringPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unix_permissions.setter
    def unix_permissions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedGib")
    def used_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @used_gib.setter
    def used_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:netapp/volume:Volume")
class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_config: Optional[pulumi.Input[Union[VolumeBackupConfigArgs, VolumeBackupConfigArgsDict]]] = ..., block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeBlockDeviceArgs, VolumeBlockDeviceArgsDict]]]]] = ..., cache_parameters: Optional[pulumi.Input[Union[VolumeCacheParametersArgs, VolumeCacheParametersArgsDict]]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., export_policy: Optional[pulumi.Input[Union[VolumeExportPolicyArgs, VolumeExportPolicyArgsDict]]] = ..., hybrid_replication_parameters: Optional[pulumi.Input[Union[VolumeHybridReplicationParametersArgs, VolumeHybridReplicationParametersArgsDict]]] = ..., kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., large_capacity: Optional[pulumi.Input[_builtins.bool]] = ..., large_capacity_config: Optional[pulumi.Input[Union[VolumeLargeCapacityConfigArgs, VolumeLargeCapacityConfigArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multiple_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., restore_parameters: Optional[pulumi.Input[Union[VolumeRestoreParametersArgs, VolumeRestoreParametersArgsDict]]] = ..., restricted_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_style: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., smb_settings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_directory: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_policy: Optional[pulumi.Input[Union[VolumeSnapshotPolicyArgs, VolumeSnapshotPolicyArgsDict]]] = ..., storage_pool: Optional[pulumi.Input[_builtins.str]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., tiering_policy: Optional[pulumi.Input[Union[VolumeTieringPolicyArgs, VolumeTieringPolicyArgsDict]]] = ..., unix_permissions: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VolumeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., active_directory: Optional[pulumi.Input[_builtins.str]] = ..., backup_config: Optional[pulumi.Input[Union[VolumeBackupConfigArgs, VolumeBackupConfigArgsDict]]] = ..., block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeBlockDeviceArgs, VolumeBlockDeviceArgsDict]]]]] = ..., cache_parameters: Optional[pulumi.Input[Union[VolumeCacheParametersArgs, VolumeCacheParametersArgsDict]]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., cold_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., export_policy: Optional[pulumi.Input[Union[VolumeExportPolicyArgs, VolumeExportPolicyArgsDict]]] = ..., has_replication: Optional[pulumi.Input[_builtins.bool]] = ..., hot_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_replication_parameters: Optional[pulumi.Input[Union[VolumeHybridReplicationParametersArgs, VolumeHybridReplicationParametersArgsDict]]] = ..., kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., large_capacity: Optional[pulumi.Input[_builtins.bool]] = ..., large_capacity_config: Optional[pulumi.Input[Union[VolumeLargeCapacityConfigArgs, VolumeLargeCapacityConfigArgsDict]]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mount_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeMountOptionArgs, VolumeMountOptionArgsDict]]]]] = ..., multiple_endpoints: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., psa_range: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., restore_parameters: Optional[pulumi.Input[Union[VolumeRestoreParametersArgs, VolumeRestoreParametersArgsDict]]] = ..., restricted_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_style: Optional[pulumi.Input[_builtins.str]] = ..., service_level: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., smb_settings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_directory: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_policy: Optional[pulumi.Input[Union[VolumeSnapshotPolicyArgs, VolumeSnapshotPolicyArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_details: Optional[pulumi.Input[_builtins.str]] = ..., storage_pool: Optional[pulumi.Input[_builtins.str]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., tiering_policy: Optional[pulumi.Input[Union[VolumeTieringPolicyArgs, VolumeTieringPolicyArgsDict]]] = ..., unix_permissions: Optional[pulumi.Input[_builtins.str]] = ..., used_gib: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Volume:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfig")
    def backup_config(self) -> pulumi.Output[Optional[outputs.VolumeBackupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDevices")
    def block_devices(self) -> pulumi.Output[Optional[Sequence[outputs.VolumeBlockDevice]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheParameters")
    def cache_parameters(self) -> pulumi.Output[Optional[outputs.VolumeCacheParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coldTierSizeGib")
    def cold_tier_size_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> pulumi.Output[Optional[outputs.VolumeExportPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasReplication")
    def has_replication(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeUsedGib")
    def hot_tier_size_used_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridReplicationParameters")
    def hybrid_replication_parameters(self) -> pulumi.Output[Optional[outputs.VolumeHybridReplicationParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfig")
    def kms_config(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacity")
    def large_capacity(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="largeCapacityConfig")
    def large_capacity_config(self) -> pulumi.Output[Optional[outputs.VolumeLargeCapacityConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> pulumi.Output[Sequence[outputs.VolumeMountOption]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleEndpoints")
    def multiple_endpoints(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaRange")
    def psa_range(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZone")
    def replica_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> pulumi.Output[Optional[outputs.VolumeRestoreParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedActions")
    def restricted_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSettings")
    def smb_settings(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDirectory")
    def snapshot_directory(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotPolicy")
    def snapshot_policy(self) -> pulumi.Output[Optional[outputs.VolumeSnapshotPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieringPolicy")
    def tiering_policy(self) -> pulumi.Output[Optional[outputs.VolumeTieringPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedGib")
    def used_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


