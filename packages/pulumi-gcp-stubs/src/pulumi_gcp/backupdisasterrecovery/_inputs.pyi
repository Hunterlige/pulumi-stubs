import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupPlanAssociationRulesConfigInfoArgs",
    "BackupPlanAssociationRulesConfigInfoArgsDict",
    ...,
    ...,
    "BackupPlanBackupRuleArgs",
    "BackupPlanBackupRuleArgsDict",
    "BackupPlanBackupRuleStandardScheduleArgs",
    "BackupPlanBackupRuleStandardScheduleArgsDict",
    ...,
    ...,
    ...,
    ...,
    "BackupVaultEncryptionConfigArgs",
    "BackupVaultEncryptionConfigArgsDict",
    "ManagementServerManagementUriArgs",
    "ManagementServerManagementUriArgsDict",
    "ManagementServerNetworkArgs",
    "ManagementServerNetworkArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RestoreWorkloadDiskRestorePropertiesArgs",
    "RestoreWorkloadDiskRestorePropertiesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "RestoreWorkloadDiskRestorePropertiesLabelArgs",
    "RestoreWorkloadDiskRestorePropertiesLabelArgsDict",
    ...,
    ...,
    "RestoreWorkloadDiskTargetEnvironmentArgs",
    "RestoreWorkloadDiskTargetEnvironmentArgsDict",
    "RestoreWorkloadRegionDiskTargetEnvironmentArgs",
    "RestoreWorkloadRegionDiskTargetEnvironmentArgsDict",
    "RestoreWorkloadTargetResourceArgs",
    "RestoreWorkloadTargetResourceArgsDict",
    "RestoreWorkloadTargetResourceGcpResourceArgs",
    "RestoreWorkloadTargetResourceGcpResourceArgsDict",
]

class BackupPlanAssociationRulesConfigInfoArgsDict(TypedDict):
    last_backup_errors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    BackupPlanAssociationRulesConfigInfoLastBackupErrorArgsDict
                ]
            ]
        ]
    ]
    last_backup_state: NotRequired[pulumi.Input[_builtins.str]]
    last_successful_backup_consistency_time: NotRequired[pulumi.Input[_builtins.str]]
    rule_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackupPlanAssociationRulesConfigInfoArgs:
    def __init__(
        __self__,
        *,
        last_backup_errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BackupPlanAssociationRulesConfigInfoLastBackupErrorArgs
                    ]
                ]
            ]
        ] = ...,
        last_backup_state: Optional[pulumi.Input[_builtins.str]] = ...,
        last_successful_backup_consistency_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastBackupErrors")
    def last_backup_errors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[BackupPlanAssociationRulesConfigInfoLastBackupErrorArgs]
            ]
        ]
    ]: ...
    @last_backup_errors.setter
    def last_backup_errors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        BackupPlanAssociationRulesConfigInfoLastBackupErrorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_backup_state.setter
    def last_backup_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupConsistencyTime")
    def last_successful_backup_consistency_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_successful_backup_consistency_time.setter
    def last_successful_backup_consistency_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupPlanAssociationRulesConfigInfoLastBackupErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.float]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackupPlanAssociationRulesConfigInfoLastBackupErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.float]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackupPlanBackupRuleArgsDict(TypedDict):
    backup_retention_days: pulumi.Input[_builtins.int]
    rule_id: pulumi.Input[_builtins.str]
    standard_schedule: pulumi.Input[BackupPlanBackupRuleStandardScheduleArgsDict]

@pulumi.input_type
class BackupPlanBackupRuleArgs:
    def __init__(
        __self__,
        *,
        backup_retention_days: pulumi.Input[_builtins.int],
        rule_id: pulumi.Input[_builtins.str],
        standard_schedule: pulumi.Input[BackupPlanBackupRuleStandardScheduleArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> pulumi.Input[_builtins.int]: ...
    @backup_retention_days.setter
    def backup_retention_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]: ...
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="standardSchedule")
    def standard_schedule(
        self,
    ) -> pulumi.Input[BackupPlanBackupRuleStandardScheduleArgs]: ...
    @standard_schedule.setter
    def standard_schedule(
        self, value: pulumi.Input[BackupPlanBackupRuleStandardScheduleArgs]
    ): ...

class BackupPlanBackupRuleStandardScheduleArgsDict(TypedDict):
    recurrence_type: pulumi.Input[_builtins.str]
    time_zone: pulumi.Input[_builtins.str]
    backup_window: NotRequired[
        pulumi.Input[BackupPlanBackupRuleStandardScheduleBackupWindowArgsDict]
    ]
    days_of_months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    days_of_weeks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hourly_frequency: NotRequired[pulumi.Input[_builtins.int]]
    months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    week_day_of_month: NotRequired[
        pulumi.Input[BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgsDict]
    ]

@pulumi.input_type
class BackupPlanBackupRuleStandardScheduleArgs:
    def __init__(
        __self__,
        *,
        recurrence_type: pulumi.Input[_builtins.str],
        time_zone: pulumi.Input[_builtins.str],
        backup_window: Optional[
            pulumi.Input[BackupPlanBackupRuleStandardScheduleBackupWindowArgs]
        ] = ...,
        days_of_months: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        days_of_weeks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        hourly_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        months: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        week_day_of_month: Optional[
            pulumi.Input[BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> pulumi.Input[_builtins.str]: ...
    @recurrence_type.setter
    def recurrence_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupWindow")
    def backup_window(
        self,
    ) -> Optional[
        pulumi.Input[BackupPlanBackupRuleStandardScheduleBackupWindowArgs]
    ]: ...
    @backup_window.setter
    def backup_window(
        self,
        value: Optional[
            pulumi.Input[BackupPlanBackupRuleStandardScheduleBackupWindowArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysOfMonths")
    def days_of_months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @days_of_months.setter
    def days_of_months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
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
    @_builtins.property
    @pulumi.getter(name="hourlyFrequency")
    def hourly_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hourly_frequency.setter
    def hourly_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @months.setter
    def months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weekDayOfMonth")
    def week_day_of_month(
        self,
    ) -> Optional[
        pulumi.Input[BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgs]
    ]: ...
    @week_day_of_month.setter
    def week_day_of_month(
        self,
        value: Optional[
            pulumi.Input[BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgs]
        ],
    ): ...

class BackupPlanBackupRuleStandardScheduleBackupWindowArgsDict(TypedDict):
    start_hour_of_day: pulumi.Input[_builtins.int]
    end_hour_of_day: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackupPlanBackupRuleStandardScheduleBackupWindowArgs:
    def __init__(
        __self__,
        *,
        start_hour_of_day: pulumi.Input[_builtins.int],
        end_hour_of_day: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startHourOfDay")
    def start_hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @start_hour_of_day.setter
    def start_hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="endHourOfDay")
    def end_hour_of_day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @end_hour_of_day.setter
    def end_hour_of_day(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    week_of_month: pulumi.Input[_builtins.str]

@pulumi.input_type
class BackupPlanBackupRuleStandardScheduleWeekDayOfMonthArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        week_of_month: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="weekOfMonth")
    def week_of_month(self) -> pulumi.Input[_builtins.str]: ...
    @week_of_month.setter
    def week_of_month(self, value: pulumi.Input[_builtins.str]): ...

class BackupVaultEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackupVaultEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagementServerManagementUriArgsDict(TypedDict):
    api: NotRequired[pulumi.Input[_builtins.str]]
    web_ui: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementServerManagementUriArgs:
    def __init__(
        __self__,
        *,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        web_ui: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api.setter
    def api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webUi")
    def web_ui(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_ui.setter
    def web_ui(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagementServerNetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    peering_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementServerNetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        peering_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peeringMode")
    def peering_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peering_mode.setter
    def peering_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    advanced_machine_features: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgsDict
        ]
    ]
    allocation_affinity: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgsDict
        ]
    ]
    can_ip_forward: NotRequired[pulumi.Input[_builtins.bool]]
    confidential_instance_config: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgsDict
        ]
    ]
    deletion_protection: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesDiskArgsDict
                ]
            ]
        ]
    ]
    display_device: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgsDict
        ]
    ]
    guest_accelerators: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgsDict
                ]
            ]
        ]
    ]
    hostname: NotRequired[pulumi.Input[_builtins.str]]
    instance_encryption_key: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgsDict
        ]
    ]
    key_revocation_action_type: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesLabelArgsDict
                ]
            ]
        ]
    ]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgsDict]
    ]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    network_interfaces: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgsDict
                ]
            ]
        ]
    ]
    network_performance_config: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgsDict
        ]
    ]
    params: NotRequired[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesParamsArgsDict]
    ]
    private_ipv6_google_access: NotRequired[pulumi.Input[_builtins.str]]
    resource_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    scheduling: NotRequired[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgsDict]
    ]
    service_accounts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgsDict
                ]
            ]
        ]
    ]
    shielded_instance_config: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgsDict
        ]
    ]
    tags: NotRequired[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesTagsArgsDict]
    ]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        advanced_machine_features: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgs
            ]
        ] = ...,
        allocation_affinity: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgs
            ]
        ] = ...,
        can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgs
            ]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesDiskArgs
                    ]
                ]
            ]
        ] = ...,
        display_device: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgs
            ]
        ] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgs
                    ]
                ]
            ]
        ] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_encryption_key: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgs
            ]
        ] = ...,
        key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesLabelArgs
                    ]
                ]
            ]
        ] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgs]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgs
                    ]
                ]
            ]
        ] = ...,
        network_performance_config: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgs
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesParamsArgs]
        ] = ...,
        private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        scheduling: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgs]
        ] = ...,
        service_accounts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgs
                    ]
                ]
            ]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgs
            ]
        ] = ...,
        tags: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesTagsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgs
        ]
    ]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocationAffinity")
    def allocation_affinity(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgs
        ]
    ]: ...
    @allocation_affinity.setter
    def allocation_affinity(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgs
        ]
    ]: ...
    @confidential_instance_config.setter
    def confidential_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesDiskArgs]
            ]
        ]
    ]: ...
    @disks.setter
    def disks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesDiskArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayDevice")
    def display_device(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgs]
    ]: ...
    @display_device.setter
    def display_device(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgs
                ]
            ]
        ]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKey")
    def instance_encryption_key(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgs
        ]
    ]: ...
    @instance_encryption_key.setter
    def instance_encryption_key(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_revocation_action_type.setter
    def key_revocation_action_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesLabelArgs]
            ]
        ]
    ]: ...
    @labels.setter
    def labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesLabelArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgs]
    ]: ...
    @metadata.setter
    def metadata(
        self,
        value: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgs
                ]
            ]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgs
        ]
    ]: ...
    @network_performance_config.setter
    def network_performance_config(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesParamsArgs]
    ]: ...
    @params.setter
    def params(
        self,
        value: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesParamsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_policies.setter
    def resource_policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheduling(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgs]
    ]: ...
    @scheduling.setter
    def scheduling(
        self,
        value: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgs
                ]
            ]
        ]
    ]: ...
    @service_accounts.setter
    def service_accounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgs
        ]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesTagsArgs]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesTagsArgs]
        ],
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgsDict(
    TypedDict
):
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    enable_uefi_networking: NotRequired[pulumi.Input[_builtins.bool]]
    threads_per_core: NotRequired[pulumi.Input[_builtins.int]]
    visible_core_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesAdvancedMachineFeaturesArgs:
    def __init__(
        __self__,
        *,
        enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_uefi_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        threads_per_core: Optional[pulumi.Input[_builtins.int]] = ...,
        visible_core_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableUefiNetworking")
    def enable_uefi_networking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_uefi_networking.setter
    def enable_uefi_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @threads_per_core.setter
    def threads_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="visibleCoreCount")
    def visible_core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @visible_core_count.setter
    def visible_core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgsDict(
    TypedDict
):
    consume_allocation_type: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesAllocationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_allocation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeAllocationType")
    def consume_allocation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consume_allocation_type.setter
    def consume_allocation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgsDict(
    TypedDict
):
    enable_confidential_compute: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesConfidentialInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_confidential_compute: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_compute.setter
    def enable_confidential_compute(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesDiskArgsDict(TypedDict):
    auto_delete: NotRequired[pulumi.Input[_builtins.bool]]
    boot: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    disk_encryption_key: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgsDict
        ]
    ]
    disk_interface: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    guest_os_features: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgsDict
                ]
            ]
        ]
    ]
    index: NotRequired[pulumi.Input[_builtins.int]]
    initialize_params: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgsDict
        ]
    ]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    licenses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    saved_state: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskArgs:
    def __init__(
        __self__,
        *,
        auto_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption_key: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgs
            ]
        ] = ...,
        disk_interface: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_os_features: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgs
                    ]
                ]
            ]
        ] = ...,
        index: Optional[pulumi.Input[_builtins.int]] = ...,
        initialize_params: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgs
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        saved_state: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_delete.setter
    def auto_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boot.setter
    def boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgs
        ]
    ]: ...
    @disk_encryption_key.setter
    def disk_encryption_key(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskInterface")
    def disk_interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_interface.setter
    def disk_interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgs
                ]
            ]
        ]
    ]: ...
    @guest_os_features.setter
    def guest_os_features(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @index.setter
    def index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="initializeParams")
    def initialize_params(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgs
        ]
    ]: ...
    @initialize_params.setter
    def initialize_params(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def licenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @licenses.setter
    def licenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="savedState")
    def saved_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @saved_state.setter
    def saved_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgsDict(
    TypedDict
):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_service_account: NotRequired[pulumi.Input[_builtins.str]]
    raw_key: NotRequired[pulumi.Input[_builtins.str]]
    rsa_encrypted_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskDiskEncryptionKeyArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        raw_key: Optional[pulumi.Input[_builtins.str]] = ...,
        rsa_encrypted_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_service_account.setter
    def kms_key_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @raw_key.setter
    def raw_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rsa_encrypted_key.setter
    def rsa_encrypted_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgsDict(
    TypedDict
):
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskGuestOsFeatureArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgsDict(
    TypedDict
):
    disk_name: NotRequired[pulumi.Input[_builtins.str]]
    replica_zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesDiskInitializeParamsArgs:
    def __init__(
        __self__,
        *,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_zones.setter
    def replica_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgsDict(TypedDict):
    enable_display: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesDisplayDeviceArgs:
    def __init__(
        __self__, *, enable_display: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_display.setter
    def enable_display(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesGuestAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgsDict(
    TypedDict
):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_service_account: NotRequired[pulumi.Input[_builtins.str]]
    raw_key: NotRequired[pulumi.Input[_builtins.str]]
    rsa_encrypted_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesInstanceEncryptionKeyArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        raw_key: Optional[pulumi.Input[_builtins.str]] = ...,
        rsa_encrypted_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_service_account.setter
    def kms_key_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @raw_key.setter
    def raw_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rsa_encrypted_key.setter
    def rsa_encrypted_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesLabelArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesLabelArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgsDict(TypedDict):
    items: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesMetadataArgs:
    def __init__(
        __self__,
        *,
        items: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgs
                ]
            ]
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgs
                    ]
                ]
            ]
        ],
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesMetadataItemArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgsDict(
    TypedDict
):
    access_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgsDict
                ]
            ]
        ]
    ]
    alias_ip_ranges: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgsDict
                ]
            ]
        ]
    ]
    internal_ipv6_prefix_length: NotRequired[pulumi.Input[_builtins.int]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_access_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgsDict
                ]
            ]
        ]
    ]
    ipv6_access_type: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    network_attachment: NotRequired[pulumi.Input[_builtins.str]]
    nic_type: NotRequired[pulumi.Input[_builtins.str]]
    queue_count: NotRequired[pulumi.Input[_builtins.int]]
    stack_type: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgs
                    ]
                ]
            ]
        ] = ...,
        alias_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgs
                    ]
                ]
            ]
        ] = ...,
        internal_ipv6_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_access_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgs
                    ]
                ]
            ]
        ] = ...,
        ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        queue_count: Optional[pulumi.Input[_builtins.int]] = ...,
        stack_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgs
                ]
            ]
        ]
    ]: ...
    @access_configs.setter
    def access_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aliasIpRanges")
    def alias_ip_ranges(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgs
                ]
            ]
        ]
    ]: ...
    @alias_ip_ranges.setter
    def alias_ip_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="internalIpv6PrefixLength")
    def internal_ipv6_prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @internal_ipv6_prefix_length.setter
    def internal_ipv6_prefix_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AccessConfigs")
    def ipv6_access_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgs
                ]
            ]
        ]
    ]: ...
    @ipv6_access_configs.setter
    def ipv6_access_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_attachment.setter
    def network_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nic_type.setter
    def nic_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @queue_count.setter
    def queue_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgsDict(
    TypedDict
):
    external_ip: NotRequired[pulumi.Input[_builtins.str]]
    external_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    external_ipv6_prefix_length: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_tier: NotRequired[pulumi.Input[_builtins.str]]
    public_ptr_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    set_public_ptr: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAccessConfigArgs:
    def __init__(
        __self__,
        *,
        external_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ipv6_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ptr_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        set_public_ptr: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_ip.setter
    def external_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIpv6")
    def external_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_ipv6.setter
    def external_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @external_ipv6_prefix_length.setter
    def external_ipv6_prefix_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_tier.setter
    def network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ptr_domain_name.setter
    def public_ptr_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="setPublicPtr")
    def set_public_ptr(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @set_public_ptr.setter
    def set_public_ptr(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgsDict(
    TypedDict
):
    ip_cidr_range: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork_range_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceAliasIpRangeArgs:
    def __init__(
        __self__,
        *,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork_range_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetworkRangeName")
    def subnetwork_range_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork_range_name.setter
    def subnetwork_range_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgsDict(
    TypedDict
):
    external_ip: NotRequired[pulumi.Input[_builtins.str]]
    external_ipv6: NotRequired[pulumi.Input[_builtins.str]]
    external_ipv6_prefix_length: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_tier: NotRequired[pulumi.Input[_builtins.str]]
    public_ptr_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    set_public_ptr: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkInterfaceIpv6AccessConfigArgs:
    def __init__(
        __self__,
        *,
        external_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ipv6_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ptr_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        set_public_ptr: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_ip.setter
    def external_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIpv6")
    def external_ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_ipv6.setter
    def external_ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIpv6PrefixLength")
    def external_ipv6_prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @external_ipv6_prefix_length.setter
    def external_ipv6_prefix_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_tier.setter
    def network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicPtrDomainName")
    def public_ptr_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ptr_domain_name.setter
    def public_ptr_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="setPublicPtr")
    def set_public_ptr(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @set_public_ptr.setter
    def set_public_ptr(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgsDict(
    TypedDict
):
    total_egress_bandwidth_tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesNetworkPerformanceConfigArgs:
    def __init__(
        __self__,
        *,
        total_egress_bandwidth_tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @total_egress_bandwidth_tier.setter
    def total_egress_bandwidth_tier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesParamsArgsDict(TypedDict):
    resource_manager_tags: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesParamsArgs:
    def __init__(
        __self__,
        *,
        resource_manager_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgs
                ]
            ]
        ]
    ]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgs
                    ]
                ]
            ]
        ],
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesParamsResourceManagerTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgsDict(TypedDict):
    automatic_restart: NotRequired[pulumi.Input[_builtins.bool]]
    instance_termination_action: NotRequired[pulumi.Input[_builtins.str]]
    local_ssd_recovery_timeout: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgsDict
        ]
    ]
    max_run_duration: NotRequired[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgsDict
        ]
    ]
    min_node_cpus: NotRequired[pulumi.Input[_builtins.int]]
    node_affinities: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgsDict
                ]
            ]
        ]
    ]
    on_host_maintenance: NotRequired[pulumi.Input[_builtins.str]]
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    provisioning_model: NotRequired[pulumi.Input[_builtins.str]]
    termination_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingArgs:
    def __init__(
        __self__,
        *,
        automatic_restart: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_termination_action: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ssd_recovery_timeout: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgs
            ]
        ] = ...,
        max_run_duration: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgs
            ]
        ] = ...,
        min_node_cpus: Optional[pulumi.Input[_builtins.int]] = ...,
        node_affinities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgs
                    ]
                ]
            ]
        ] = ...,
        on_host_maintenance: Optional[pulumi.Input[_builtins.str]] = ...,
        preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        provisioning_model: Optional[pulumi.Input[_builtins.str]] = ...,
        termination_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticRestart")
    def automatic_restart(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automatic_restart.setter
    def automatic_restart(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTerminationAction")
    def instance_termination_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_termination_action.setter
    def instance_termination_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localSsdRecoveryTimeout")
    def local_ssd_recovery_timeout(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgs
        ]
    ]: ...
    @local_ssd_recovery_timeout.setter
    def local_ssd_recovery_timeout(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(
        self,
    ) -> Optional[
        pulumi.Input[
            RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgs
        ]
    ]: ...
    @max_run_duration.setter
    def max_run_duration(
        self,
        value: Optional[
            pulumi.Input[
                RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_cpus.setter
    def min_node_cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgs
                ]
            ]
        ]
    ]: ...
    @node_affinities.setter
    def node_affinities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="onHostMaintenance")
    def on_host_maintenance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_host_maintenance.setter
    def on_host_maintenance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningModel")
    def provisioning_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_model.setter
    def provisioning_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="terminationTime")
    def termination_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @termination_time.setter
    def termination_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgsDict(
    TypedDict
):
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingLocalSsdRecoveryTimeoutArgs:
    def __init__(
        __self__,
        *,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
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

class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgsDict(
    TypedDict
):
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingMaxRunDurationArgs:
    def __init__(
        __self__,
        *,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
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

class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgsDict(
    TypedDict
):
    key: NotRequired[pulumi.Input[_builtins.str]]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesSchedulingNodeAffinityArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        operator: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesServiceAccountArgs:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgsDict(
    TypedDict
):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vtpm: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vtpm.setter
    def enable_vtpm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class RestoreWorkloadComputeInstanceRestorePropertiesTagsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestoreWorkloadComputeInstanceRestorePropertiesTagsArgs:
    def __init__(
        __self__,
        *,
        items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @items.setter
    def items(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreWorkloadComputeInstanceTargetEnvironmentArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]

@pulumi.input_type
class RestoreWorkloadComputeInstanceTargetEnvironmentArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...

class RestoreWorkloadDiskRestorePropertiesArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    size_gb: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    access_mode: NotRequired[pulumi.Input[_builtins.str]]
    architecture: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disk_encryption_key: NotRequired[
        pulumi.Input[RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgsDict]
    ]
    enable_confidential_compute: NotRequired[pulumi.Input[_builtins.bool]]
    guest_os_features: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgsDict]
            ]
        ]
    ]
    labels: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RestoreWorkloadDiskRestorePropertiesLabelArgsDict]]
        ]
    ]
    licenses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    physical_block_size_bytes: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_iops: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_throughput: NotRequired[pulumi.Input[_builtins.int]]
    resource_manager_tags: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgsDict
                ]
            ]
        ]
    ]
    resource_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    storage_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadDiskRestorePropertiesArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        size_gb: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption_key: Optional[
            pulumi.Input[RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgs]
        ] = ...,
        enable_confidential_compute: Optional[pulumi.Input[_builtins.bool]] = ...,
        guest_os_features: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgs]
                ]
            ]
        ] = ...,
        labels: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RestoreWorkloadDiskRestorePropertiesLabelArgs]]
            ]
        ] = ...,
        licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        physical_block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgs
                    ]
                ]
            ]
        ] = ...,
        resource_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @size_gb.setter
    def size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> Optional[
        pulumi.Input[RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgs]
    ]: ...
    @disk_encryption_key.setter
    def disk_encryption_key(
        self,
        value: Optional[
            pulumi.Input[RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_compute.setter
    def enable_confidential_compute(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgs]
            ]
        ]
    ]: ...
    @guest_os_features.setter
    def guest_os_features(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RestoreWorkloadDiskRestorePropertiesLabelArgs]]
        ]
    ]: ...
    @labels.setter
    def labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RestoreWorkloadDiskRestorePropertiesLabelArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def licenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @licenses.setter
    def licenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @physical_block_size_bytes.setter
    def physical_block_size_bytes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgs]
            ]
        ]
    ]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_policies.setter
    def resource_policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storagePool")
    def storage_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_pool.setter
    def storage_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_service_account: NotRequired[pulumi.Input[_builtins.str]]
    raw_key: NotRequired[pulumi.Input[_builtins.str]]
    rsa_encrypted_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadDiskRestorePropertiesDiskEncryptionKeyArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        raw_key: Optional[pulumi.Input[_builtins.str]] = ...,
        rsa_encrypted_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_service_account.setter
    def kms_key_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rawKey")
    def raw_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @raw_key.setter
    def raw_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rsaEncryptedKey")
    def rsa_encrypted_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rsa_encrypted_key.setter
    def rsa_encrypted_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadDiskRestorePropertiesGuestOsFeatureArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadDiskRestorePropertiesLabelArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadDiskRestorePropertiesLabelArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadDiskRestorePropertiesResourceManagerTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RestoreWorkloadDiskTargetEnvironmentArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]

@pulumi.input_type
class RestoreWorkloadDiskTargetEnvironmentArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...

class RestoreWorkloadRegionDiskTargetEnvironmentArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    replica_zones: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class RestoreWorkloadRegionDiskTargetEnvironmentArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
        replica_zones: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @replica_zones.setter
    def replica_zones(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class RestoreWorkloadTargetResourceArgsDict(TypedDict):
    gcp_resource: NotRequired[
        pulumi.Input[RestoreWorkloadTargetResourceGcpResourceArgsDict]
    ]

@pulumi.input_type
class RestoreWorkloadTargetResourceArgs:
    def __init__(
        __self__,
        *,
        gcp_resource: Optional[
            pulumi.Input[RestoreWorkloadTargetResourceGcpResourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpResource")
    def gcp_resource(
        self,
    ) -> Optional[pulumi.Input[RestoreWorkloadTargetResourceGcpResourceArgs]]: ...
    @gcp_resource.setter
    def gcp_resource(
        self,
        value: Optional[pulumi.Input[RestoreWorkloadTargetResourceGcpResourceArgs]],
    ): ...

class RestoreWorkloadTargetResourceGcpResourceArgsDict(TypedDict):
    gcp_resourcename: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestoreWorkloadTargetResourceGcpResourceArgs:
    def __init__(
        __self__,
        *,
        gcp_resourcename: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpResourcename")
    def gcp_resourcename(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_resourcename.setter
    def gcp_resourcename(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
