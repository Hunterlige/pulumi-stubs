import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupEncryptionConfigArgs",
    "BackupEncryptionConfigArgsDict",
    "BackupEncryptionInfoArgs",
    "BackupEncryptionInfoArgsDict",
    "BackupExpiryQuantityArgs",
    "BackupExpiryQuantityArgsDict",
    "ClusterAutomatedBackupPolicyArgs",
    "ClusterAutomatedBackupPolicyArgsDict",
    "ClusterAutomatedBackupPolicyEncryptionConfigArgs",
    ...,
    ...,
    ...,
    "ClusterAutomatedBackupPolicyTimeBasedRetentionArgs",
    ...,
    "ClusterAutomatedBackupPolicyWeeklyScheduleArgs",
    "ClusterAutomatedBackupPolicyWeeklyScheduleArgsDict",
    ...,
    ...,
    "ClusterBackupSourceArgs",
    "ClusterBackupSourceArgsDict",
    "ClusterBackupdrBackupSourceArgs",
    "ClusterBackupdrBackupSourceArgsDict",
    "ClusterContinuousBackupConfigArgs",
    "ClusterContinuousBackupConfigArgsDict",
    "ClusterContinuousBackupConfigEncryptionConfigArgs",
    ...,
    "ClusterContinuousBackupInfoArgs",
    "ClusterContinuousBackupInfoArgsDict",
    "ClusterContinuousBackupInfoEncryptionInfoArgs",
    "ClusterContinuousBackupInfoEncryptionInfoArgsDict",
    "ClusterDataplexConfigArgs",
    "ClusterDataplexConfigArgsDict",
    "ClusterEncryptionConfigArgs",
    "ClusterEncryptionConfigArgsDict",
    "ClusterEncryptionInfoArgs",
    "ClusterEncryptionInfoArgsDict",
    "ClusterInitialUserArgs",
    "ClusterInitialUserArgsDict",
    "ClusterMaintenanceUpdatePolicyArgs",
    "ClusterMaintenanceUpdatePolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterMigrationSourceArgs",
    "ClusterMigrationSourceArgsDict",
    "ClusterNetworkConfigArgs",
    "ClusterNetworkConfigArgsDict",
    "ClusterPscConfigArgs",
    "ClusterPscConfigArgsDict",
    "ClusterRestoreBackupSourceArgs",
    "ClusterRestoreBackupSourceArgsDict",
    "ClusterRestoreBackupdrBackupSourceArgs",
    "ClusterRestoreBackupdrBackupSourceArgsDict",
    "ClusterRestoreBackupdrPitrSourceArgs",
    "ClusterRestoreBackupdrPitrSourceArgsDict",
    "ClusterRestoreContinuousBackupSourceArgs",
    "ClusterRestoreContinuousBackupSourceArgsDict",
    "ClusterSecondaryConfigArgs",
    "ClusterSecondaryConfigArgsDict",
    "ClusterTrialMetadataArgs",
    "ClusterTrialMetadataArgsDict",
    "InstanceClientConnectionConfigArgs",
    "InstanceClientConnectionConfigArgsDict",
    "InstanceClientConnectionConfigSslConfigArgs",
    "InstanceClientConnectionConfigSslConfigArgsDict",
    "InstanceConnectionPoolConfigArgs",
    "InstanceConnectionPoolConfigArgsDict",
    "InstanceMachineConfigArgs",
    "InstanceMachineConfigArgsDict",
    "InstanceNetworkConfigArgs",
    "InstanceNetworkConfigArgsDict",
    "InstanceNetworkConfigAuthorizedExternalNetworkArgs",
    ...,
    "InstanceObservabilityConfigArgs",
    "InstanceObservabilityConfigArgsDict",
    "InstancePscInstanceConfigArgs",
    "InstancePscInstanceConfigArgsDict",
    "InstancePscInstanceConfigPscAutoConnectionArgs",
    "InstancePscInstanceConfigPscAutoConnectionArgsDict",
    "InstancePscInstanceConfigPscInterfaceConfigArgs",
    ...,
    "InstanceQueryInsightsConfigArgs",
    "InstanceQueryInsightsConfigArgsDict",
    "InstanceReadPoolConfigArgs",
    "InstanceReadPoolConfigArgsDict",
]

class BackupEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BackupEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupEncryptionInfoArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class BackupEncryptionInfoArgs:
    def __init__(
        __self__,
        *,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kms_key_versions.setter
    def kms_key_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BackupExpiryQuantityArgsDict(TypedDict):
    retention_count: NotRequired[pulumi.Input[_builtins.int]]
    total_retention_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class BackupExpiryQuantityArgs:
    def __init__(
        __self__,
        *,
        retention_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_retention_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionCount")
    def retention_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_count.setter
    def retention_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="totalRetentionCount")
    def total_retention_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_retention_count.setter
    def total_retention_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterAutomatedBackupPolicyArgsDict(TypedDict):
    backup_window: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_config: NotRequired[
        pulumi.Input[ClusterAutomatedBackupPolicyEncryptionConfigArgsDict]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    quantity_based_retention: NotRequired[
        pulumi.Input[ClusterAutomatedBackupPolicyQuantityBasedRetentionArgsDict]
    ]
    time_based_retention: NotRequired[
        pulumi.Input[ClusterAutomatedBackupPolicyTimeBasedRetentionArgsDict]
    ]
    weekly_schedule: NotRequired[
        pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleArgsDict]
    ]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_config: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyEncryptionConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        quantity_based_retention: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyQuantityBasedRetentionArgs]
        ] = ...,
        time_based_retention: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyTimeBasedRetentionArgs]
        ] = ...,
        weekly_schedule: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_window.setter
    def backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAutomatedBackupPolicyEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self,
        value: Optional[pulumi.Input[ClusterAutomatedBackupPolicyEncryptionConfigArgs]],
    ): ...
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
    @pulumi.getter(name="quantityBasedRetention")
    def quantity_based_retention(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAutomatedBackupPolicyQuantityBasedRetentionArgs]
    ]: ...
    @quantity_based_retention.setter
    def quantity_based_retention(
        self,
        value: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyQuantityBasedRetentionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeBasedRetention")
    def time_based_retention(
        self,
    ) -> Optional[pulumi.Input[ClusterAutomatedBackupPolicyTimeBasedRetentionArgs]]: ...
    @time_based_retention.setter
    def time_based_retention(
        self,
        value: Optional[
            pulumi.Input[ClusterAutomatedBackupPolicyTimeBasedRetentionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(
        self,
    ) -> Optional[pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleArgs]]: ...
    @weekly_schedule.setter
    def weekly_schedule(
        self,
        value: Optional[pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleArgs]],
    ): ...

class ClusterAutomatedBackupPolicyEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterAutomatedBackupPolicyQuantityBasedRetentionArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyQuantityBasedRetentionArgs:
    def __init__(
        __self__, *, count: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterAutomatedBackupPolicyTimeBasedRetentionArgsDict(TypedDict):
    retention_period: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyTimeBasedRetentionArgs:
    def __init__(
        __self__, *, retention_period: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterAutomatedBackupPolicyWeeklyScheduleArgsDict(TypedDict):
    start_times: pulumi.Input[
        Sequence[
            pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgsDict]
        ]
    ]
    days_of_weeks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyWeeklyScheduleArgs:
    def __init__(
        __self__,
        *,
        start_times: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgs]
            ]
        ],
        days_of_weeks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgs]]
    ]: ...
    @start_times.setter
    def start_times(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @days_of_weeks.setter
    def days_of_weeks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterAutomatedBackupPolicyWeeklyScheduleStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterBackupSourceArgsDict(TypedDict):
    backup_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterBackupSourceArgs:
    def __init__(
        __self__, *, backup_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_name.setter
    def backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterBackupdrBackupSourceArgsDict(TypedDict):
    backup: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterBackupdrBackupSourceArgs:
    def __init__(
        __self__, *, backup: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup.setter
    def backup(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterContinuousBackupConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_config: NotRequired[
        pulumi.Input[ClusterContinuousBackupConfigEncryptionConfigArgsDict]
    ]
    recovery_window_days: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterContinuousBackupConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_config: Optional[
            pulumi.Input[ClusterContinuousBackupConfigEncryptionConfigArgs]
        ] = ...,
        recovery_window_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[ClusterContinuousBackupConfigEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self,
        value: Optional[
            pulumi.Input[ClusterContinuousBackupConfigEncryptionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryWindowDays")
    def recovery_window_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @recovery_window_days.setter
    def recovery_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterContinuousBackupConfigEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterContinuousBackupConfigEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterContinuousBackupInfoArgsDict(TypedDict):
    earliest_restorable_time: NotRequired[pulumi.Input[_builtins.str]]
    enabled_time: NotRequired[pulumi.Input[_builtins.str]]
    encryption_infos: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterContinuousBackupInfoEncryptionInfoArgsDict]]
        ]
    ]
    schedules: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterContinuousBackupInfoArgs:
    def __init__(
        __self__,
        *,
        earliest_restorable_time: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_time: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterContinuousBackupInfoEncryptionInfoArgs]]
            ]
        ] = ...,
        schedules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestorableTime")
    def earliest_restorable_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @earliest_restorable_time.setter
    def earliest_restorable_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enabled_time.setter
    def enabled_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionInfos")
    def encryption_infos(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterContinuousBackupInfoEncryptionInfoArgs]]
        ]
    ]: ...
    @encryption_infos.setter
    def encryption_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterContinuousBackupInfoEncryptionInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schedules.setter
    def schedules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterContinuousBackupInfoEncryptionInfoArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterContinuousBackupInfoEncryptionInfoArgs:
    def __init__(
        __self__,
        *,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kms_key_versions.setter
    def kms_key_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterDataplexConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class ClusterDataplexConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterEncryptionInfoArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterEncryptionInfoArgs:
    def __init__(
        __self__,
        *,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersions")
    def kms_key_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kms_key_versions.setter
    def kms_key_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterInitialUserArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_wo: NotRequired[pulumi.Input[_builtins.str]]
    password_wo_version: NotRequired[pulumi.Input[_builtins.str]]
    user: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterInitialUserArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenanceUpdatePolicyArgsDict(TypedDict):
    maintenance_windows: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterMaintenanceUpdatePolicyMaintenanceWindowArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClusterMaintenanceUpdatePolicyArgs:
    def __init__(
        __self__,
        *,
        maintenance_windows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterMaintenanceUpdatePolicyMaintenanceWindowArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMaintenanceUpdatePolicyMaintenanceWindowArgs]]
        ]
    ]: ...
    @maintenance_windows.setter
    def maintenance_windows(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterMaintenanceUpdatePolicyMaintenanceWindowArgs]
                ]
            ]
        ],
    ): ...

class ClusterMaintenanceUpdatePolicyMaintenanceWindowArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[
        ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgsDict
    ]
    ...

@pulumi.input_type
class ClusterMaintenanceUpdatePolicyMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        day: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[
            ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]: ...
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgs]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgs
        ],
    ): ...

class ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMaintenanceUpdatePolicyMaintenanceWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: pulumi.Input[_builtins.int],
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]: ...
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterMigrationSourceArgsDict(TypedDict):
    host_port: NotRequired[pulumi.Input[_builtins.str]]
    reference_id: NotRequired[pulumi.Input[_builtins.str]]
    source_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterMigrationSourceArgs:
    def __init__(
        __self__,
        *,
        host_port: Optional[pulumi.Input[_builtins.str]] = ...,
        reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_port.setter
    def host_port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNetworkConfigArgsDict(TypedDict):
    allocated_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        allocated_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allocated_ip_range.setter
    def allocated_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterPscConfigArgsDict(TypedDict):
    psc_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    service_owned_project_number: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterPscConfigArgs:
    def __init__(
        __self__,
        *,
        psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_owned_project_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @psc_enabled.setter
    def psc_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceOwnedProjectNumber")
    def service_owned_project_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @service_owned_project_number.setter
    def service_owned_project_number(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ClusterRestoreBackupSourceArgsDict(TypedDict):
    backup_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterRestoreBackupSourceArgs:
    def __init__(__self__, *, backup_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> pulumi.Input[_builtins.str]: ...
    @backup_name.setter
    def backup_name(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRestoreBackupdrBackupSourceArgsDict(TypedDict):
    backup: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterRestoreBackupdrBackupSourceArgs:
    def __init__(__self__, *, backup: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> pulumi.Input[_builtins.str]: ...
    @backup.setter
    def backup(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRestoreBackupdrPitrSourceArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    point_in_time: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterRestoreBackupdrPitrSourceArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        point_in_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> pulumi.Input[_builtins.str]: ...
    @point_in_time.setter
    def point_in_time(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRestoreContinuousBackupSourceArgsDict(TypedDict):
    cluster: pulumi.Input[_builtins.str]
    point_in_time: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterRestoreContinuousBackupSourceArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        point_in_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> pulumi.Input[_builtins.str]: ...
    @point_in_time.setter
    def point_in_time(self, value: pulumi.Input[_builtins.str]): ...

class ClusterSecondaryConfigArgsDict(TypedDict):
    primary_cluster_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterSecondaryConfigArgs:
    def __init__(
        __self__, *, primary_cluster_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusterName")
    def primary_cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @primary_cluster_name.setter
    def primary_cluster_name(self, value: pulumi.Input[_builtins.str]): ...

class ClusterTrialMetadataArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    grace_end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    upgrade_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterTrialMetadataArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        grace_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graceEndTime")
    def grace_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grace_end_time.setter
    def grace_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeTime")
    def upgrade_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upgrade_time.setter
    def upgrade_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceClientConnectionConfigArgsDict(TypedDict):
    require_connectors: NotRequired[pulumi.Input[_builtins.bool]]
    ssl_config: NotRequired[
        pulumi.Input[InstanceClientConnectionConfigSslConfigArgsDict]
    ]
    ...

@pulumi.input_type
class InstanceClientConnectionConfigArgs:
    def __init__(
        __self__,
        *,
        require_connectors: Optional[pulumi.Input[_builtins.bool]] = ...,
        ssl_config: Optional[
            pulumi.Input[InstanceClientConnectionConfigSslConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requireConnectors")
    def require_connectors(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_connectors.setter
    def require_connectors(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[pulumi.Input[InstanceClientConnectionConfigSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(
        self, value: Optional[pulumi.Input[InstanceClientConnectionConfigSslConfigArgs]]
    ): ...

class InstanceClientConnectionConfigSslConfigArgsDict(TypedDict):
    ssl_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceClientConnectionConfigSslConfigArgs:
    def __init__(
        __self__, *, ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceConnectionPoolConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    flags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pooler_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceConnectionPoolConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        pooler_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def flags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @flags.setter
    def flags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="poolerCount")
    def pooler_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pooler_count.setter
    def pooler_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceMachineConfigArgsDict(TypedDict):
    cpu_count: NotRequired[pulumi.Input[_builtins.int]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMachineConfigArgs:
    def __init__(
        __self__,
        *,
        cpu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceNetworkConfigArgsDict(TypedDict):
    allocated_ip_range_override: NotRequired[pulumi.Input[_builtins.str]]
    authorized_external_networks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceNetworkConfigAuthorizedExternalNetworkArgsDict]
            ]
        ]
    ]
    enable_outbound_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    enable_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        allocated_ip_range_override: Optional[pulumi.Input[_builtins.str]] = ...,
        authorized_external_networks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceNetworkConfigAuthorizedExternalNetworkArgs]
                ]
            ]
        ] = ...,
        enable_outbound_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedIpRangeOverride")
    def allocated_ip_range_override(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allocated_ip_range_override.setter
    def allocated_ip_range_override(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizedExternalNetworks")
    def authorized_external_networks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceNetworkConfigAuthorizedExternalNetworkArgs]]
        ]
    ]: ...
    @authorized_external_networks.setter
    def authorized_external_networks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceNetworkConfigAuthorizedExternalNetworkArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOutboundPublicIp")
    def enable_outbound_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_outbound_public_ip.setter
    def enable_outbound_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePublicIp")
    def enable_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_public_ip.setter
    def enable_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceNetworkConfigAuthorizedExternalNetworkArgsDict(TypedDict):
    cidr_range: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceNetworkConfigAuthorizedExternalNetworkArgs:
    def __init__(
        __self__, *, cidr_range: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrRange")
    def cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_range.setter
    def cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceObservabilityConfigArgsDict(TypedDict):
    assistive_experiences_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_query_string_length: NotRequired[pulumi.Input[_builtins.int]]
    preserve_comments: NotRequired[pulumi.Input[_builtins.bool]]
    query_plans_per_minute: NotRequired[pulumi.Input[_builtins.int]]
    record_application_tags: NotRequired[pulumi.Input[_builtins.bool]]
    track_active_queries: NotRequired[pulumi.Input[_builtins.bool]]
    track_wait_event_types: NotRequired[pulumi.Input[_builtins.bool]]
    track_wait_events: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceObservabilityConfigArgs:
    def __init__(
        __self__,
        *,
        assistive_experiences_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_query_string_length: Optional[pulumi.Input[_builtins.int]] = ...,
        preserve_comments: Optional[pulumi.Input[_builtins.bool]] = ...,
        query_plans_per_minute: Optional[pulumi.Input[_builtins.int]] = ...,
        record_application_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        track_active_queries: Optional[pulumi.Input[_builtins.bool]] = ...,
        track_wait_event_types: Optional[pulumi.Input[_builtins.bool]] = ...,
        track_wait_events: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assistiveExperiencesEnabled")
    def assistive_experiences_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assistive_experiences_enabled.setter
    def assistive_experiences_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxQueryStringLength")
    def max_query_string_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_query_string_length.setter
    def max_query_string_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preserveComments")
    def preserve_comments(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve_comments.setter
    def preserve_comments(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_plans_per_minute.setter
    def query_plans_per_minute(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @record_application_tags.setter
    def record_application_tags(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trackActiveQueries")
    def track_active_queries(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @track_active_queries.setter
    def track_active_queries(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEventTypes")
    def track_wait_event_types(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @track_wait_event_types.setter
    def track_wait_event_types(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="trackWaitEvents")
    def track_wait_events(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @track_wait_events.setter
    def track_wait_events(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstancePscInstanceConfigArgsDict(TypedDict):
    allowed_consumer_projects: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    psc_auto_connections: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstancePscInstanceConfigPscAutoConnectionArgsDict]]
        ]
    ]
    psc_dns_name: NotRequired[pulumi.Input[_builtins.str]]
    psc_interface_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstancePscInstanceConfigPscInterfaceConfigArgsDict]]
        ]
    ]
    service_attachment_link: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_consumer_projects: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        psc_auto_connections: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstancePscInstanceConfigPscAutoConnectionArgs]]
            ]
        ] = ...,
        psc_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_interface_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstancePscInstanceConfigPscInterfaceConfigArgs]]
            ]
        ] = ...,
        service_attachment_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_consumer_projects.setter
    def allowed_consumer_projects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstancePscInstanceConfigPscAutoConnectionArgs]]
        ]
    ]: ...
    @psc_auto_connections.setter
    def psc_auto_connections(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstancePscInstanceConfigPscAutoConnectionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscDnsName")
    def psc_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_dns_name.setter
    def psc_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscInterfaceConfigs")
    def psc_interface_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstancePscInstanceConfigPscInterfaceConfigArgs]]
        ]
    ]: ...
    @psc_interface_configs.setter
    def psc_interface_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstancePscInstanceConfigPscInterfaceConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachmentLink")
    def service_attachment_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment_link.setter
    def service_attachment_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePscInstanceConfigPscAutoConnectionArgsDict(TypedDict):
    consumer_network: NotRequired[pulumi.Input[_builtins.str]]
    consumer_network_status: NotRequired[pulumi.Input[_builtins.str]]
    consumer_project: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscInstanceConfigPscAutoConnectionArgs:
    def __init__(
        __self__,
        *,
        consumer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        consumer_network_status: Optional[pulumi.Input[_builtins.str]] = ...,
        consumer_project: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_network.setter
    def consumer_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_network_status.setter
    def consumer_network_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_project.setter
    def consumer_project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePscInstanceConfigPscInterfaceConfigArgsDict(TypedDict):
    network_attachment_resource: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscInstanceConfigPscInterfaceConfigArgs:
    def __init__(
        __self__,
        *,
        network_attachment_resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachmentResource")
    def network_attachment_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_attachment_resource.setter
    def network_attachment_resource(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class InstanceQueryInsightsConfigArgsDict(TypedDict):
    query_plans_per_minute: NotRequired[pulumi.Input[_builtins.int]]
    query_string_length: NotRequired[pulumi.Input[_builtins.int]]
    record_application_tags: NotRequired[pulumi.Input[_builtins.bool]]
    record_client_address: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceQueryInsightsConfigArgs:
    def __init__(
        __self__,
        *,
        query_plans_per_minute: Optional[pulumi.Input[_builtins.int]] = ...,
        query_string_length: Optional[pulumi.Input[_builtins.int]] = ...,
        record_application_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        record_client_address: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_plans_per_minute.setter
    def query_plans_per_minute(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_string_length.setter
    def query_string_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @record_application_tags.setter
    def record_application_tags(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @record_client_address.setter
    def record_client_address(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceReadPoolConfigArgsDict(TypedDict):
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceReadPoolConfigArgs:
    def __init__(
        __self__, *, node_count: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
