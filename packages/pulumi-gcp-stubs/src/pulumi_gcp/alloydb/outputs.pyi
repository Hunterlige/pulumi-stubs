import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupEncryptionConfig",
    "BackupEncryptionInfo",
    "BackupExpiryQuantity",
    "ClusterAutomatedBackupPolicy",
    "ClusterAutomatedBackupPolicyEncryptionConfig",
    "ClusterAutomatedBackupPolicyQuantityBasedRetention",
    "ClusterAutomatedBackupPolicyTimeBasedRetention",
    "ClusterAutomatedBackupPolicyWeeklySchedule",
    ...,
    "ClusterBackupSource",
    "ClusterBackupdrBackupSource",
    "ClusterContinuousBackupConfig",
    "ClusterContinuousBackupConfigEncryptionConfig",
    "ClusterContinuousBackupInfo",
    "ClusterContinuousBackupInfoEncryptionInfo",
    "ClusterDataplexConfig",
    "ClusterEncryptionConfig",
    "ClusterEncryptionInfo",
    "ClusterInitialUser",
    "ClusterMaintenanceUpdatePolicy",
    "ClusterMaintenanceUpdatePolicyMaintenanceWindow",
    ...,
    "ClusterMigrationSource",
    "ClusterNetworkConfig",
    "ClusterPscConfig",
    "ClusterRestoreBackupSource",
    "ClusterRestoreBackupdrBackupSource",
    "ClusterRestoreBackupdrPitrSource",
    "ClusterRestoreContinuousBackupSource",
    "ClusterSecondaryConfig",
    "ClusterTrialMetadata",
    "InstanceClientConnectionConfig",
    "InstanceClientConnectionConfigSslConfig",
    "InstanceConnectionPoolConfig",
    "InstanceMachineConfig",
    "InstanceNetworkConfig",
    "InstanceNetworkConfigAuthorizedExternalNetwork",
    "InstanceObservabilityConfig",
    "InstancePscInstanceConfig",
    "InstancePscInstanceConfigPscAutoConnection",
    "InstancePscInstanceConfigPscInterfaceConfig",
    "InstanceQueryInsightsConfig",
    "InstanceReadPoolConfig",
    "GetClusterAutomatedBackupPolicyResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterBackupSourceResult",
    "GetClusterBackupdrBackupSourceResult",
    "GetClusterContinuousBackupConfigResult",
    ...,
    "GetClusterContinuousBackupInfoResult",
    "GetClusterContinuousBackupInfoEncryptionInfoResult",
    "GetClusterDataplexConfigResult",
    "GetClusterEncryptionConfigResult",
    "GetClusterEncryptionInfoResult",
    "GetClusterInitialUserResult",
    "GetClusterMaintenanceUpdatePolicyResult",
    ...,
    ...,
    "GetClusterMigrationSourceResult",
    "GetClusterNetworkConfigResult",
    "GetClusterPscConfigResult",
    "GetClusterRestoreBackupSourceResult",
    "GetClusterRestoreBackupdrBackupSourceResult",
    "GetClusterRestoreBackupdrPitrSourceResult",
    "GetClusterRestoreContinuousBackupSourceResult",
    "GetClusterSecondaryConfigResult",
    "GetClusterTrialMetadataResult",
    "GetInstanceClientConnectionConfigResult",
    "GetInstanceClientConnectionConfigSslConfigResult",
    "GetInstanceConnectionPoolConfigResult",
    "GetInstanceMachineConfigResult",
    "GetInstanceNetworkConfigResult",
    ...,
    "GetInstanceObservabilityConfigResult",
    "GetInstancePscInstanceConfigResult",
    ...,
    ...,
    "GetInstanceQueryInsightsConfigResult",
    "GetInstanceReadPoolConfigResult",
    "GetLocationsLocationResult",
    ...,
    ...,
    ...,
]

@pulumi.output_type
class BackupEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BackupEncryptionInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: Optional[_builtins.str] = ...,
        kms_key_versions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class BackupExpiryQuantity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_count: Optional[_builtins.int] = ...,
        total_retention_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionCount")
    def retention_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalRetentionCount")
    def total_retention_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_window: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        encryption_config: Optional[
            outputs.ClusterAutomatedBackupPolicyEncryptionConfig
        ] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        location: Optional[_builtins.str] = ...,
        quantity_based_retention: Optional[
            outputs.ClusterAutomatedBackupPolicyQuantityBasedRetention
        ] = ...,
        time_based_retention: Optional[
            outputs.ClusterAutomatedBackupPolicyTimeBasedRetention
        ] = ...,
        weekly_schedule: Optional[
            outputs.ClusterAutomatedBackupPolicyWeeklySchedule
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[outputs.ClusterAutomatedBackupPolicyEncryptionConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quantityBasedRetention")
    def quantity_based_retention(
        self,
    ) -> Optional[outputs.ClusterAutomatedBackupPolicyQuantityBasedRetention]: ...
    @_builtins.property
    @pulumi.getter(name="timeBasedRetention")
    def time_based_retention(
        self,
    ) -> Optional[outputs.ClusterAutomatedBackupPolicyTimeBasedRetention]: ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(
        self,
    ) -> Optional[outputs.ClusterAutomatedBackupPolicyWeeklySchedule]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicyEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicyQuantityBasedRetention(dict):
    def __init__(__self__, *, count: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicyTimeBasedRetention(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, retention_period: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicyWeeklySchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        start_times: Sequence[
            outputs.ClusterAutomatedBackupPolicyWeeklyScheduleStartTime
        ],
        days_of_weeks: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[outputs.ClusterAutomatedBackupPolicyWeeklyScheduleStartTime]: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterAutomatedBackupPolicyWeeklyScheduleStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterBackupSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, backup_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterBackupdrBackupSource(dict):
    def __init__(__self__, *, backup: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterContinuousBackupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        encryption_config: Optional[
            outputs.ClusterContinuousBackupConfigEncryptionConfig
        ] = ...,
        recovery_window_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[outputs.ClusterContinuousBackupConfigEncryptionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryWindowDays")
    def recovery_window_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterContinuousBackupConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterContinuousBackupInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        earliest_restorable_time: Optional[_builtins.str] = ...,
        enabled_time: Optional[_builtins.str] = ...,
        encryption_infos: Optional[
            Sequence[outputs.ClusterContinuousBackupInfoEncryptionInfo]
        ] = ...,
        schedules: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestorableTime")
    def earliest_restorable_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(
        self,
    ) -> Optional[Sequence[outputs.ClusterContinuousBackupInfoEncryptionInfo]]: ...
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterContinuousBackupInfoEncryptionInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: Optional[_builtins.str] = ...,
        kms_key_versions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterDataplexConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterEncryptionInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: Optional[_builtins.str] = ...,
        kms_key_versions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterInitialUser(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password: Optional[_builtins.str] = ...,
        password_wo: Optional[_builtins.str] = ...,
        password_wo_version: Optional[_builtins.str] = ...,
        user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenanceUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maintenance_windows: Optional[
            Sequence[outputs.ClusterMaintenanceUpdatePolicyMaintenanceWindow]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterMaintenanceUpdatePolicyMaintenanceWindow]
    ]: ...

@pulumi.output_type
class ClusterMaintenanceUpdatePolicyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        start_time: outputs.ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> outputs.ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTime: ...

@pulumi.output_type
class ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMigrationSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_port: Optional[_builtins.str] = ...,
        reference_id: Optional[_builtins.str] = ...,
        source_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocated_ip_range: Optional[_builtins.str] = ...,
        network: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterPscConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        psc_enabled: Optional[_builtins.bool] = ...,
        service_owned_project_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceOwnedProjectNumber")
    def service_owned_project_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterRestoreBackupSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, backup_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterRestoreBackupdrBackupSource(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterRestoreBackupdrPitrSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_source: _builtins.str, point_in_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterRestoreContinuousBackupSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cluster: _builtins.str, point_in_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterSecondaryConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, primary_cluster_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusterName")
    def primary_cluster_name(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterTrialMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        grace_end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        upgrade_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="graceEndTime")
    def grace_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeTime")
    def upgrade_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceClientConnectionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        require_connectors: Optional[_builtins.bool] = ...,
        ssl_config: Optional[outputs.InstanceClientConnectionConfigSslConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requireConnectors")
    def require_connectors(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[outputs.InstanceClientConnectionConfigSslConfig]: ...

@pulumi.output_type
class InstanceClientConnectionConfigSslConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ssl_mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceConnectionPoolConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        flags: Optional[Mapping[str, _builtins.str]] = ...,
        pooler_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="poolerCount")
    def pooler_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceMachineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu_count: Optional[_builtins.int] = ...,
        machine_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocated_ip_range_override: Optional[_builtins.str] = ...,
        authorized_external_networks: Optional[
            Sequence[outputs.InstanceNetworkConfigAuthorizedExternalNetwork]
        ] = ...,
        enable_outbound_public_ip: Optional[_builtins.bool] = ...,
        enable_public_ip: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRangeOverride")
    def allocated_ip_range_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizedExternalNetworks")
    def authorized_external_networks(
        self,
    ) -> Optional[Sequence[outputs.InstanceNetworkConfigAuthorizedExternalNetwork]]: ...
    @_builtins.property
    @pulumi.getter(name="enableOutboundPublicIp")
    def enable_outbound_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePublicIp")
    def enable_public_ip(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InstanceNetworkConfigAuthorizedExternalNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cidr_range: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrRange")
    def cidr_range(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceObservabilityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assistive_experiences_enabled: Optional[_builtins.bool] = ...,
        enabled: Optional[_builtins.bool] = ...,
        max_query_string_length: Optional[_builtins.int] = ...,
        preserve_comments: Optional[_builtins.bool] = ...,
        query_plans_per_minute: Optional[_builtins.int] = ...,
        record_application_tags: Optional[_builtins.bool] = ...,
        track_active_queries: Optional[_builtins.bool] = ...,
        track_wait_event_types: Optional[_builtins.bool] = ...,
        track_wait_events: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assistiveExperiencesEnabled")
    def assistive_experiences_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxQueryStringLength")
    def max_query_string_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="preserveComments")
    def preserve_comments(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trackActiveQueries")
    def track_active_queries(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEventTypes")
    def track_wait_event_types(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEvents")
    def track_wait_events(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InstancePscInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_consumer_projects: Optional[Sequence[_builtins.str]] = ...,
        psc_auto_connections: Optional[
            Sequence[outputs.InstancePscInstanceConfigPscAutoConnection]
        ] = ...,
        psc_dns_name: Optional[_builtins.str] = ...,
        psc_interface_configs: Optional[
            Sequence[outputs.InstancePscInstanceConfigPscInterfaceConfig]
        ] = ...,
        service_attachment_link: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(
        self,
    ) -> Optional[Sequence[outputs.InstancePscInstanceConfigPscAutoConnection]]: ...
    @_builtins.property
    @pulumi.getter(name="pscDnsName")
    def psc_dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscInterfaceConfigs")
    def psc_interface_configs(
        self,
    ) -> Optional[Sequence[outputs.InstancePscInstanceConfigPscInterfaceConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachmentLink")
    def service_attachment_link(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstancePscInstanceConfigPscAutoConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_network: Optional[_builtins.str] = ...,
        consumer_network_status: Optional[_builtins.str] = ...,
        consumer_project: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstancePscInstanceConfigPscInterfaceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, network_attachment_resource: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachmentResource")
    def network_attachment_resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceQueryInsightsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_plans_per_minute: Optional[_builtins.int] = ...,
        query_string_length: Optional[_builtins.int] = ...,
        record_application_tags: Optional[_builtins.bool] = ...,
        record_client_address: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InstanceReadPoolConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, node_count: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyResult(dict):
    def __init__(
        __self__,
        *,
        backup_window: _builtins.str,
        enabled: _builtins.bool,
        encryption_configs: Sequence[
            outputs.GetClusterAutomatedBackupPolicyEncryptionConfigResult
        ],
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
        quantity_based_retentions: Sequence[
            outputs.GetClusterAutomatedBackupPolicyQuantityBasedRetentionResult
        ],
        time_based_retentions: Sequence[
            outputs.GetClusterAutomatedBackupPolicyTimeBasedRetentionResult
        ],
        weekly_schedules: Sequence[
            outputs.GetClusterAutomatedBackupPolicyWeeklyScheduleResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(
        self,
    ) -> Sequence[outputs.GetClusterAutomatedBackupPolicyEncryptionConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quantityBasedRetentions")
    def quantity_based_retentions(
        self,
    ) -> Sequence[
        outputs.GetClusterAutomatedBackupPolicyQuantityBasedRetentionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeBasedRetentions")
    def time_based_retentions(
        self,
    ) -> Sequence[outputs.GetClusterAutomatedBackupPolicyTimeBasedRetentionResult]: ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedules")
    def weekly_schedules(
        self,
    ) -> Sequence[outputs.GetClusterAutomatedBackupPolicyWeeklyScheduleResult]: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyQuantityBasedRetentionResult(dict):
    def __init__(__self__, *, count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyTimeBasedRetentionResult(dict):
    def __init__(__self__, *, retention_period: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyWeeklyScheduleResult(dict):
    def __init__(
        __self__,
        *,
        days_of_weeks: Sequence[_builtins.str],
        start_times: Sequence[
            outputs.GetClusterAutomatedBackupPolicyWeeklyScheduleStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetClusterAutomatedBackupPolicyWeeklyScheduleStartTimeResult
    ]: ...

@pulumi.output_type
class GetClusterAutomatedBackupPolicyWeeklyScheduleStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterBackupSourceResult(dict):
    def __init__(__self__, *, backup_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterBackupdrBackupSourceResult(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterContinuousBackupConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        encryption_configs: Sequence[
            outputs.GetClusterContinuousBackupConfigEncryptionConfigResult
        ],
        recovery_window_days: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(
        self,
    ) -> Sequence[outputs.GetClusterContinuousBackupConfigEncryptionConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryWindowDays")
    def recovery_window_days(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterContinuousBackupConfigEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterContinuousBackupInfoResult(dict):
    def __init__(
        __self__,
        *,
        earliest_restorable_time: _builtins.str,
        enabled_time: _builtins.str,
        encryption_infos: Sequence[
            outputs.GetClusterContinuousBackupInfoEncryptionInfoResult
        ],
        schedules: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestorableTime")
    def earliest_restorable_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(
        self,
    ) -> Sequence[outputs.GetClusterContinuousBackupInfoEncryptionInfoResult]: ...
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterContinuousBackupInfoEncryptionInfoResult(dict):
    def __init__(
        __self__,
        *,
        encryption_type: _builtins.str,
        kms_key_versions: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterDataplexConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterEncryptionInfoResult(dict):
    def __init__(
        __self__,
        *,
        encryption_type: _builtins.str,
        kms_key_versions: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterInitialUserResult(dict):
    def __init__(
        __self__,
        *,
        password: _builtins.str,
        password_wo: _builtins.str,
        password_wo_version: _builtins.str,
        user: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMaintenanceUpdatePolicyResult(dict):
    def __init__(
        __self__,
        *,
        maintenance_windows: Sequence[
            outputs.GetClusterMaintenanceUpdatePolicyMaintenanceWindowResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Sequence[outputs.GetClusterMaintenanceUpdatePolicyMaintenanceWindowResult]: ...

@pulumi.output_type
class GetClusterMaintenanceUpdatePolicyMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        start_times: Sequence[
            outputs.GetClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeResult
    ]: ...

@pulumi.output_type
class GetClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterMigrationSourceResult(dict):
    def __init__(
        __self__,
        *,
        host_port: _builtins.str,
        reference_id: _builtins.str,
        source_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNetworkConfigResult(dict):
    def __init__(
        __self__, *, allocated_ip_range: _builtins.str, network: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPscConfigResult(dict):
    def __init__(
        __self__,
        *,
        psc_enabled: _builtins.bool,
        service_owned_project_number: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="serviceOwnedProjectNumber")
    def service_owned_project_number(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterRestoreBackupSourceResult(dict):
    def __init__(__self__, *, backup_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterRestoreBackupdrBackupSourceResult(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterRestoreBackupdrPitrSourceResult(dict):
    def __init__(
        __self__, *, data_source: _builtins.str, point_in_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterRestoreContinuousBackupSourceResult(dict):
    def __init__(
        __self__, *, cluster: _builtins.str, point_in_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterSecondaryConfigResult(dict):
    def __init__(__self__, *, primary_cluster_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusterName")
    def primary_cluster_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterTrialMetadataResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        grace_end_time: _builtins.str,
        start_time: _builtins.str,
        upgrade_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="graceEndTime")
    def grace_end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeTime")
    def upgrade_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceClientConnectionConfigResult(dict):
    def __init__(
        __self__,
        *,
        require_connectors: _builtins.bool,
        ssl_configs: Sequence[outputs.GetInstanceClientConnectionConfigSslConfigResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requireConnectors")
    def require_connectors(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sslConfigs")
    def ssl_configs(
        self,
    ) -> Sequence[outputs.GetInstanceClientConnectionConfigSslConfigResult]: ...

@pulumi.output_type
class GetInstanceClientConnectionConfigSslConfigResult(dict):
    def __init__(__self__, *, ssl_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceConnectionPoolConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        flags: Mapping[str, _builtins.str],
        pooler_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="poolerCount")
    def pooler_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceMachineConfigResult(dict):
    def __init__(
        __self__, *, cpu_count: _builtins.int, machine_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceNetworkConfigResult(dict):
    def __init__(
        __self__,
        *,
        allocated_ip_range_override: _builtins.str,
        authorized_external_networks: Sequence[
            outputs.GetInstanceNetworkConfigAuthorizedExternalNetworkResult
        ],
        enable_outbound_public_ip: _builtins.bool,
        enable_public_ip: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRangeOverride")
    def allocated_ip_range_override(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authorizedExternalNetworks")
    def authorized_external_networks(
        self,
    ) -> Sequence[outputs.GetInstanceNetworkConfigAuthorizedExternalNetworkResult]: ...
    @_builtins.property
    @pulumi.getter(name="enableOutboundPublicIp")
    def enable_outbound_public_ip(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enablePublicIp")
    def enable_public_ip(self) -> _builtins.bool: ...

@pulumi.output_type
class GetInstanceNetworkConfigAuthorizedExternalNetworkResult(dict):
    def __init__(__self__, *, cidr_range: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrRange")
    def cidr_range(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceObservabilityConfigResult(dict):
    def __init__(
        __self__,
        *,
        assistive_experiences_enabled: _builtins.bool,
        enabled: _builtins.bool,
        max_query_string_length: _builtins.int,
        preserve_comments: _builtins.bool,
        query_plans_per_minute: _builtins.int,
        record_application_tags: _builtins.bool,
        track_active_queries: _builtins.bool,
        track_wait_event_types: _builtins.bool,
        track_wait_events: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assistiveExperiencesEnabled")
    def assistive_experiences_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxQueryStringLength")
    def max_query_string_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="preserveComments")
    def preserve_comments(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="trackActiveQueries")
    def track_active_queries(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEventTypes")
    def track_wait_event_types(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEvents")
    def track_wait_events(self) -> _builtins.bool: ...

@pulumi.output_type
class GetInstancePscInstanceConfigResult(dict):
    def __init__(
        __self__,
        *,
        allowed_consumer_projects: Sequence[_builtins.str],
        psc_auto_connections: Sequence[
            outputs.GetInstancePscInstanceConfigPscAutoConnectionResult
        ],
        psc_dns_name: _builtins.str,
        psc_interface_configs: Sequence[
            outputs.GetInstancePscInstanceConfigPscInterfaceConfigResult
        ],
        service_attachment_link: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(
        self,
    ) -> Sequence[outputs.GetInstancePscInstanceConfigPscAutoConnectionResult]: ...
    @_builtins.property
    @pulumi.getter(name="pscDnsName")
    def psc_dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pscInterfaceConfigs")
    def psc_interface_configs(
        self,
    ) -> Sequence[outputs.GetInstancePscInstanceConfigPscInterfaceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachmentLink")
    def service_attachment_link(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstancePscInstanceConfigPscAutoConnectionResult(dict):
    def __init__(
        __self__,
        *,
        consumer_network: _builtins.str,
        consumer_network_status: _builtins.str,
        consumer_project: _builtins.str,
        ip_address: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstancePscInstanceConfigPscInterfaceConfigResult(dict):
    def __init__(__self__, *, network_attachment_resource: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachmentResource")
    def network_attachment_resource(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceQueryInsightsConfigResult(dict):
    def __init__(
        __self__,
        *,
        query_plans_per_minute: _builtins.int,
        query_string_length: _builtins.int,
        record_application_tags: _builtins.bool,
        record_client_address: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> _builtins.bool: ...

@pulumi.output_type
class GetInstanceReadPoolConfigResult(dict):
    def __init__(__self__, *, node_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetLocationsLocationResult(dict):
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location_id: _builtins.str,
        metadata: Mapping[str, _builtins.str],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetSupportedDatabaseFlagsSupportedDatabaseFlagResult(dict):
    def __init__(
        __self__,
        *,
        accepts_multiple_values: _builtins.bool,
        flag_name: _builtins.str,
        integer_restrictions: outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagIntegerRestrictionsResult,
        name: _builtins.str,
        requires_db_restart: _builtins.bool,
        string_restrictions: outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagStringRestrictionsResult,
        supported_db_versions: Sequence[_builtins.str],
        value_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptsMultipleValues")
    def accepts_multiple_values(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="flagName")
    def flag_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="integerRestrictions")
    def integer_restrictions(
        self,
    ) -> (
        outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagIntegerRestrictionsResult
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiresDbRestart")
    def requires_db_restart(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="stringRestrictions")
    def string_restrictions(
        self,
    ) -> (
        outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagStringRestrictionsResult
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedDbVersions")
    def supported_db_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetSupportedDatabaseFlagsSupportedDatabaseFlagIntegerRestrictionsResult(dict):
    def __init__(
        __self__, *, max_value: _builtins.str, min_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> _builtins.str: ...

@pulumi.output_type
class GetSupportedDatabaseFlagsSupportedDatabaseFlagStringRestrictionsResult(dict):
    def __init__(__self__, *, allowed_values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Sequence[_builtins.str]: ...
