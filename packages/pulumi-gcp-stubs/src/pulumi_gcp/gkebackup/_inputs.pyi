import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupPlanBackupConfigArgs",
    "BackupPlanBackupConfigArgsDict",
    "BackupPlanBackupConfigEncryptionKeyArgs",
    "BackupPlanBackupConfigEncryptionKeyArgsDict",
    "BackupPlanBackupConfigSelectedApplicationsArgs",
    "BackupPlanBackupConfigSelectedApplicationsArgsDict",
    ...,
    ...,
    "BackupPlanBackupConfigSelectedNamespaceLabelsArgs",
    ...,
    ...,
    ...,
    "BackupPlanBackupConfigSelectedNamespacesArgs",
    "BackupPlanBackupConfigSelectedNamespacesArgsDict",
    "BackupPlanBackupScheduleArgs",
    "BackupPlanBackupScheduleArgsDict",
    "BackupPlanBackupScheduleRpoConfigArgs",
    "BackupPlanBackupScheduleRpoConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BackupPlanIamBindingConditionArgs",
    "BackupPlanIamBindingConditionArgsDict",
    "BackupPlanIamMemberConditionArgs",
    "BackupPlanIamMemberConditionArgsDict",
    "BackupPlanRetentionPolicyArgs",
    "BackupPlanRetentionPolicyArgsDict",
    "RestorePlanIamBindingConditionArgs",
    "RestorePlanIamBindingConditionArgsDict",
    "RestorePlanIamMemberConditionArgs",
    "RestorePlanIamMemberConditionArgsDict",
    "RestorePlanRestoreConfigArgs",
    "RestorePlanRestoreConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RestorePlanRestoreConfigExcludedNamespacesArgs",
    "RestorePlanRestoreConfigExcludedNamespacesArgsDict",
    "RestorePlanRestoreConfigRestoreOrderArgs",
    "RestorePlanRestoreConfigRestoreOrderArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RestorePlanRestoreConfigSelectedApplicationsArgs",
    ...,
    ...,
    ...,
    "RestorePlanRestoreConfigSelectedNamespacesArgs",
    "RestorePlanRestoreConfigSelectedNamespacesArgsDict",
    "RestorePlanRestoreConfigTransformationRuleArgs",
    "RestorePlanRestoreConfigTransformationRuleArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class BackupPlanBackupConfigArgsDict(TypedDict):
    all_namespaces: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key: NotRequired[
        pulumi.Input[BackupPlanBackupConfigEncryptionKeyArgsDict]
    ]
    include_secrets: NotRequired[pulumi.Input[_builtins.bool]]
    include_volume_data: NotRequired[pulumi.Input[_builtins.bool]]
    permissive_mode: NotRequired[pulumi.Input[_builtins.bool]]
    selected_applications: NotRequired[
        pulumi.Input[BackupPlanBackupConfigSelectedApplicationsArgsDict]
    ]
    selected_namespace_labels: NotRequired[
        pulumi.Input[BackupPlanBackupConfigSelectedNamespaceLabelsArgsDict]
    ]
    selected_namespaces: NotRequired[
        pulumi.Input[BackupPlanBackupConfigSelectedNamespacesArgsDict]
    ]

@pulumi.input_type
class BackupPlanBackupConfigArgs:
    def __init__(
        __self__,
        *,
        all_namespaces: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key: Optional[
            pulumi.Input[BackupPlanBackupConfigEncryptionKeyArgs]
        ] = ...,
        include_secrets: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_volume_data: Optional[pulumi.Input[_builtins.bool]] = ...,
        permissive_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        selected_applications: Optional[
            pulumi.Input[BackupPlanBackupConfigSelectedApplicationsArgs]
        ] = ...,
        selected_namespace_labels: Optional[
            pulumi.Input[BackupPlanBackupConfigSelectedNamespaceLabelsArgs]
        ] = ...,
        selected_namespaces: Optional[
            pulumi.Input[BackupPlanBackupConfigSelectedNamespacesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allNamespaces")
    def all_namespaces(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_namespaces.setter
    def all_namespaces(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> Optional[pulumi.Input[BackupPlanBackupConfigEncryptionKeyArgs]]: ...
    @encryption_key.setter
    def encryption_key(
        self, value: Optional[pulumi.Input[BackupPlanBackupConfigEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeSecrets")
    def include_secrets(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_secrets.setter
    def include_secrets(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeVolumeData")
    def include_volume_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_volume_data.setter
    def include_volume_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="permissiveMode")
    def permissive_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @permissive_mode.setter
    def permissive_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="selectedApplications")
    def selected_applications(
        self,
    ) -> Optional[pulumi.Input[BackupPlanBackupConfigSelectedApplicationsArgs]]: ...
    @selected_applications.setter
    def selected_applications(
        self,
        value: Optional[pulumi.Input[BackupPlanBackupConfigSelectedApplicationsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedNamespaceLabels")
    def selected_namespace_labels(
        self,
    ) -> Optional[pulumi.Input[BackupPlanBackupConfigSelectedNamespaceLabelsArgs]]: ...
    @selected_namespace_labels.setter
    def selected_namespace_labels(
        self,
        value: Optional[
            pulumi.Input[BackupPlanBackupConfigSelectedNamespaceLabelsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedNamespaces")
    def selected_namespaces(
        self,
    ) -> Optional[pulumi.Input[BackupPlanBackupConfigSelectedNamespacesArgs]]: ...
    @selected_namespaces.setter
    def selected_namespaces(
        self,
        value: Optional[pulumi.Input[BackupPlanBackupConfigSelectedNamespacesArgs]],
    ): ...

class BackupPlanBackupConfigEncryptionKeyArgsDict(TypedDict):
    gcp_kms_encryption_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class BackupPlanBackupConfigEncryptionKeyArgs:
    def __init__(
        __self__, *, gcp_kms_encryption_key: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpKmsEncryptionKey")
    def gcp_kms_encryption_key(self) -> pulumi.Input[_builtins.str]: ...
    @gcp_kms_encryption_key.setter
    def gcp_kms_encryption_key(self, value: pulumi.Input[_builtins.str]): ...

class BackupPlanBackupConfigSelectedApplicationsArgsDict(TypedDict):
    namespaced_names: pulumi.Input[
        Sequence[
            pulumi.Input[
                BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgsDict
            ]
        ]
    ]

@pulumi.input_type
class BackupPlanBackupConfigSelectedApplicationsArgs:
    def __init__(
        __self__,
        *,
        namespaced_names: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespacedNames")
    def namespaced_names(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgs]
        ]
    ]: ...
    @namespaced_names.setter
    def namespaced_names(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgs
                ]
            ]
        ],
    ): ...

class BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]

@pulumi.input_type
class BackupPlanBackupConfigSelectedApplicationsNamespacedNameArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...

class BackupPlanBackupConfigSelectedNamespaceLabelsArgsDict(TypedDict):
    resource_labels: pulumi.Input[
        Sequence[
            pulumi.Input[
                BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgsDict
            ]
        ]
    ]

@pulumi.input_type
class BackupPlanBackupConfigSelectedNamespaceLabelsArgs:
    def __init__(
        __self__,
        *,
        resource_labels: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgs]
        ]
    ]: ...
    @resource_labels.setter
    def resource_labels(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgs
                ]
            ]
        ],
    ): ...

class BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class BackupPlanBackupConfigSelectedNamespaceLabelsResourceLabelArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class BackupPlanBackupConfigSelectedNamespacesArgsDict(TypedDict):
    namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BackupPlanBackupConfigSelectedNamespacesArgs:
    def __init__(
        __self__, *, namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class BackupPlanBackupScheduleArgsDict(TypedDict):
    cron_schedule: NotRequired[pulumi.Input[_builtins.str]]
    paused: NotRequired[pulumi.Input[_builtins.bool]]
    rpo_config: NotRequired[pulumi.Input[BackupPlanBackupScheduleRpoConfigArgsDict]]

@pulumi.input_type
class BackupPlanBackupScheduleArgs:
    def __init__(
        __self__,
        *,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        paused: Optional[pulumi.Input[_builtins.bool]] = ...,
        rpo_config: Optional[pulumi.Input[BackupPlanBackupScheduleRpoConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @paused.setter
    def paused(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rpoConfig")
    def rpo_config(
        self,
    ) -> Optional[pulumi.Input[BackupPlanBackupScheduleRpoConfigArgs]]: ...
    @rpo_config.setter
    def rpo_config(
        self, value: Optional[pulumi.Input[BackupPlanBackupScheduleRpoConfigArgs]]
    ): ...

class BackupPlanBackupScheduleRpoConfigArgsDict(TypedDict):
    target_rpo_minutes: pulumi.Input[_builtins.int]
    exclusion_windows: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class BackupPlanBackupScheduleRpoConfigArgs:
    def __init__(
        __self__,
        *,
        target_rpo_minutes: pulumi.Input[_builtins.int],
        exclusion_windows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetRpoMinutes")
    def target_rpo_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @target_rpo_minutes.setter
    def target_rpo_minutes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionWindows")
    def exclusion_windows(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowArgs]]
        ]
    ]: ...
    @exclusion_windows.setter
    def exclusion_windows(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowArgs]
                ]
            ]
        ],
    ): ...

class BackupPlanBackupScheduleRpoConfigExclusionWindowArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[
        BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgsDict
    ]
    daily: NotRequired[pulumi.Input[_builtins.bool]]
    days_of_week: NotRequired[
        pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgsDict]
    ]
    single_occurrence_date: NotRequired[
        pulumi.Input[
            BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgsDict
        ]
    ]

@pulumi.input_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowArgs:
    def __init__(
        __self__,
        *,
        duration: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[
            BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgs
        ],
        daily: Optional[pulumi.Input[_builtins.bool]] = ...,
        days_of_week: Optional[
            pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgs]
        ] = ...,
        single_occurrence_date: Optional[
            pulumi.Input[
                BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]: ...
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[
        BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgs
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @daily.setter
    def daily(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(
        self,
    ) -> Optional[
        pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgs]
    ]: ...
    @days_of_week.setter
    def days_of_week(
        self,
        value: Optional[
            pulumi.Input[BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleOccurrenceDate")
    def single_occurrence_date(
        self,
    ) -> Optional[
        pulumi.Input[
            BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgs
        ]
    ]: ...
    @single_occurrence_date.setter
    def single_occurrence_date(
        self,
        value: Optional[
            pulumi.Input[
                BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgs
            ]
        ],
    ): ...

class BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgsDict(TypedDict):
    days_of_weeks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowDaysOfWeekArgs:
    def __init__(
        __self__,
        *,
        days_of_weeks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @days_of_weeks.setter
    def days_of_weeks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowSingleOccurrenceDateArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackupPlanBackupScheduleRpoConfigExclusionWindowStartTimeArgs:
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

class BackupPlanIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackupPlanIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupPlanIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackupPlanIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupPlanRetentionPolicyArgsDict(TypedDict):
    backup_delete_lock_days: NotRequired[pulumi.Input[_builtins.int]]
    backup_retain_days: NotRequired[pulumi.Input[_builtins.int]]
    locked: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BackupPlanRetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        backup_delete_lock_days: Optional[pulumi.Input[_builtins.int]] = ...,
        backup_retain_days: Optional[pulumi.Input[_builtins.int]] = ...,
        locked: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupDeleteLockDays")
    def backup_delete_lock_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_delete_lock_days.setter
    def backup_delete_lock_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRetainDays")
    def backup_retain_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retain_days.setter
    def backup_retain_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class RestorePlanIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigArgsDict(TypedDict):
    all_namespaces: NotRequired[pulumi.Input[_builtins.bool]]
    cluster_resource_conflict_policy: NotRequired[pulumi.Input[_builtins.str]]
    cluster_resource_restore_scope: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigClusterResourceRestoreScopeArgsDict]
    ]
    excluded_namespaces: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigExcludedNamespacesArgsDict]
    ]
    namespaced_resource_restore_mode: NotRequired[pulumi.Input[_builtins.str]]
    no_namespaces: NotRequired[pulumi.Input[_builtins.bool]]
    restore_order: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigRestoreOrderArgsDict]
    ]
    selected_applications: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigSelectedApplicationsArgsDict]
    ]
    selected_namespaces: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigSelectedNamespacesArgsDict]
    ]
    transformation_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RestorePlanRestoreConfigTransformationRuleArgsDict]]
        ]
    ]
    volume_data_restore_policy: NotRequired[pulumi.Input[_builtins.str]]
    volume_data_restore_policy_bindings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class RestorePlanRestoreConfigArgs:
    def __init__(
        __self__,
        *,
        all_namespaces: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_resource_conflict_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_resource_restore_scope: Optional[
            pulumi.Input[RestorePlanRestoreConfigClusterResourceRestoreScopeArgs]
        ] = ...,
        excluded_namespaces: Optional[
            pulumi.Input[RestorePlanRestoreConfigExcludedNamespacesArgs]
        ] = ...,
        namespaced_resource_restore_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        no_namespaces: Optional[pulumi.Input[_builtins.bool]] = ...,
        restore_order: Optional[
            pulumi.Input[RestorePlanRestoreConfigRestoreOrderArgs]
        ] = ...,
        selected_applications: Optional[
            pulumi.Input[RestorePlanRestoreConfigSelectedApplicationsArgs]
        ] = ...,
        selected_namespaces: Optional[
            pulumi.Input[RestorePlanRestoreConfigSelectedNamespacesArgs]
        ] = ...,
        transformation_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RestorePlanRestoreConfigTransformationRuleArgs]]
            ]
        ] = ...,
        volume_data_restore_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_data_restore_policy_bindings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allNamespaces")
    def all_namespaces(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_namespaces.setter
    def all_namespaces(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceConflictPolicy")
    def cluster_resource_conflict_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_resource_conflict_policy.setter
    def cluster_resource_conflict_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceRestoreScope")
    def cluster_resource_restore_scope(
        self,
    ) -> Optional[
        pulumi.Input[RestorePlanRestoreConfigClusterResourceRestoreScopeArgs]
    ]: ...
    @cluster_resource_restore_scope.setter
    def cluster_resource_restore_scope(
        self,
        value: Optional[
            pulumi.Input[RestorePlanRestoreConfigClusterResourceRestoreScopeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedNamespaces")
    def excluded_namespaces(
        self,
    ) -> Optional[pulumi.Input[RestorePlanRestoreConfigExcludedNamespacesArgs]]: ...
    @excluded_namespaces.setter
    def excluded_namespaces(
        self,
        value: Optional[pulumi.Input[RestorePlanRestoreConfigExcludedNamespacesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="namespacedResourceRestoreMode")
    def namespaced_resource_restore_mode(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespaced_resource_restore_mode.setter
    def namespaced_resource_restore_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="noNamespaces")
    def no_namespaces(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_namespaces.setter
    def no_namespaces(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreOrder")
    def restore_order(
        self,
    ) -> Optional[pulumi.Input[RestorePlanRestoreConfigRestoreOrderArgs]]: ...
    @restore_order.setter
    def restore_order(
        self, value: Optional[pulumi.Input[RestorePlanRestoreConfigRestoreOrderArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedApplications")
    def selected_applications(
        self,
    ) -> Optional[pulumi.Input[RestorePlanRestoreConfigSelectedApplicationsArgs]]: ...
    @selected_applications.setter
    def selected_applications(
        self,
        value: Optional[pulumi.Input[RestorePlanRestoreConfigSelectedApplicationsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedNamespaces")
    def selected_namespaces(
        self,
    ) -> Optional[pulumi.Input[RestorePlanRestoreConfigSelectedNamespacesArgs]]: ...
    @selected_namespaces.setter
    def selected_namespaces(
        self,
        value: Optional[pulumi.Input[RestorePlanRestoreConfigSelectedNamespacesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformationRules")
    def transformation_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RestorePlanRestoreConfigTransformationRuleArgs]]
        ]
    ]: ...
    @transformation_rules.setter
    def transformation_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RestorePlanRestoreConfigTransformationRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeDataRestorePolicy")
    def volume_data_restore_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_data_restore_policy.setter
    def volume_data_restore_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeDataRestorePolicyBindings")
    def volume_data_restore_policy_bindings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgs]
            ]
        ]
    ]: ...
    @volume_data_restore_policy_bindings.setter
    def volume_data_restore_policy_bindings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgs
                    ]
                ]
            ]
        ],
    ): ...

class RestorePlanRestoreConfigClusterResourceRestoreScopeArgsDict(TypedDict):
    all_group_kinds: NotRequired[pulumi.Input[_builtins.bool]]
    excluded_group_kinds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgsDict
                ]
            ]
        ]
    ]
    no_group_kinds: NotRequired[pulumi.Input[_builtins.bool]]
    selected_group_kinds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class RestorePlanRestoreConfigClusterResourceRestoreScopeArgs:
    def __init__(
        __self__,
        *,
        all_group_kinds: Optional[pulumi.Input[_builtins.bool]] = ...,
        excluded_group_kinds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgs
                    ]
                ]
            ]
        ] = ...,
        no_group_kinds: Optional[pulumi.Input[_builtins.bool]] = ...,
        selected_group_kinds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allGroupKinds")
    def all_group_kinds(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_group_kinds.setter
    def all_group_kinds(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedGroupKinds")
    def excluded_group_kinds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgs
                ]
            ]
        ]
    ]: ...
    @excluded_group_kinds.setter
    def excluded_group_kinds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noGroupKinds")
    def no_group_kinds(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_group_kinds.setter
    def no_group_kinds(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="selectedGroupKinds")
    def selected_group_kinds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgs
                ]
            ]
        ]
    ]: ...
    @selected_group_kinds.setter
    def selected_group_kinds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgs
                    ]
                ]
            ]
        ],
    ): ...

class RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgsDict(
    TypedDict
):
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    resource_kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigClusterResourceRestoreScopeExcludedGroupKindArgs:
    def __init__(
        __self__,
        *,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgsDict(
    TypedDict
):
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    resource_kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigClusterResourceRestoreScopeSelectedGroupKindArgs:
    def __init__(
        __self__,
        *,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigExcludedNamespacesArgsDict(TypedDict):
    namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class RestorePlanRestoreConfigExcludedNamespacesArgs:
    def __init__(
        __self__, *, namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class RestorePlanRestoreConfigRestoreOrderArgsDict(TypedDict):
    group_kind_dependencies: pulumi.Input[
        Sequence[
            pulumi.Input[
                RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgsDict
            ]
        ]
    ]

@pulumi.input_type
class RestorePlanRestoreConfigRestoreOrderArgs:
    def __init__(
        __self__,
        *,
        group_kind_dependencies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupKindDependencies")
    def group_kind_dependencies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgs]
        ]
    ]: ...
    @group_kind_dependencies.setter
    def group_kind_dependencies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgs
                ]
            ]
        ],
    ): ...

class RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgsDict(TypedDict):
    requiring: pulumi.Input[
        RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgsDict
    ]
    satisfying: pulumi.Input[
        RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgsDict
    ]

@pulumi.input_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependencyArgs:
    def __init__(
        __self__,
        *,
        requiring: pulumi.Input[
            RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgs
        ],
        satisfying: pulumi.Input[
            RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def requiring(
        self,
    ) -> pulumi.Input[
        RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgs
    ]: ...
    @requiring.setter
    def requiring(
        self,
        value: pulumi.Input[
            RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def satisfying(
        self,
    ) -> pulumi.Input[
        RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgs
    ]: ...
    @satisfying.setter
    def satisfying(
        self,
        value: pulumi.Input[
            RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgs
        ],
    ): ...

class RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgsDict(
    TypedDict
):
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    resource_kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependencyRequiringArgs:
    def __init__(
        __self__,
        *,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgsDict(
    TypedDict
):
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    resource_kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigRestoreOrderGroupKindDependencySatisfyingArgs:
    def __init__(
        __self__,
        *,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigSelectedApplicationsArgsDict(TypedDict):
    namespaced_names: pulumi.Input[
        Sequence[
            pulumi.Input[
                RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgsDict
            ]
        ]
    ]

@pulumi.input_type
class RestorePlanRestoreConfigSelectedApplicationsArgs:
    def __init__(
        __self__,
        *,
        namespaced_names: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespacedNames")
    def namespaced_names(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgs]
        ]
    ]: ...
    @namespaced_names.setter
    def namespaced_names(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgs
                ]
            ]
        ],
    ): ...

class RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]

@pulumi.input_type
class RestorePlanRestoreConfigSelectedApplicationsNamespacedNameArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...

class RestorePlanRestoreConfigSelectedNamespacesArgsDict(TypedDict):
    namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class RestorePlanRestoreConfigSelectedNamespacesArgs:
    def __init__(
        __self__, *, namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class RestorePlanRestoreConfigTransformationRuleArgsDict(TypedDict):
    field_actions: pulumi.Input[
        Sequence[
            pulumi.Input[RestorePlanRestoreConfigTransformationRuleFieldActionArgsDict]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    resource_filter: NotRequired[
        pulumi.Input[RestorePlanRestoreConfigTransformationRuleResourceFilterArgsDict]
    ]

@pulumi.input_type
class RestorePlanRestoreConfigTransformationRuleArgs:
    def __init__(
        __self__,
        *,
        field_actions: pulumi.Input[
            Sequence[
                pulumi.Input[RestorePlanRestoreConfigTransformationRuleFieldActionArgs]
            ]
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_filter: Optional[
            pulumi.Input[RestorePlanRestoreConfigTransformationRuleResourceFilterArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldActions")
    def field_actions(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[RestorePlanRestoreConfigTransformationRuleFieldActionArgs]
        ]
    ]: ...
    @field_actions.setter
    def field_actions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[RestorePlanRestoreConfigTransformationRuleFieldActionArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceFilter")
    def resource_filter(
        self,
    ) -> Optional[
        pulumi.Input[RestorePlanRestoreConfigTransformationRuleResourceFilterArgs]
    ]: ...
    @resource_filter.setter
    def resource_filter(
        self,
        value: Optional[
            pulumi.Input[RestorePlanRestoreConfigTransformationRuleResourceFilterArgs]
        ],
    ): ...

class RestorePlanRestoreConfigTransformationRuleFieldActionArgsDict(TypedDict):
    op: pulumi.Input[_builtins.str]
    from_path: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigTransformationRuleFieldActionArgs:
    def __init__(
        __self__,
        *,
        op: pulumi.Input[_builtins.str],
        from_path: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def op(self) -> pulumi.Input[_builtins.str]: ...
    @op.setter
    def op(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fromPath")
    def from_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @from_path.setter
    def from_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigTransformationRuleResourceFilterArgsDict(TypedDict):
    group_kinds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgsDict
                ]
            ]
        ]
    ]
    json_path: NotRequired[pulumi.Input[_builtins.str]]
    namespaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestorePlanRestoreConfigTransformationRuleResourceFilterArgs:
    def __init__(
        __self__,
        *,
        group_kinds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgs
                    ]
                ]
            ]
        ] = ...,
        json_path: Optional[pulumi.Input[_builtins.str]] = ...,
        namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupKinds")
    def group_kinds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgs
                ]
            ]
        ]
    ]: ...
    @group_kinds.setter
    def group_kinds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json_path.setter
    def json_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespaces(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgsDict(
    TypedDict
):
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    resource_kind: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestorePlanRestoreConfigTransformationRuleResourceFilterGroupKindArgs:
    def __init__(
        __self__,
        *,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgsDict(TypedDict):
    policy: pulumi.Input[_builtins.str]
    volume_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class RestorePlanRestoreConfigVolumeDataRestorePolicyBindingArgs:
    def __init__(
        __self__,
        *,
        policy: pulumi.Input[_builtins.str],
        volume_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Input[_builtins.str]: ...
    @volume_type.setter
    def volume_type(self, value: pulumi.Input[_builtins.str]): ...
