import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssociationOutputLocationArgs",
    "AssociationOutputLocationArgsDict",
    "AssociationTargetArgs",
    "AssociationTargetArgsDict",
    "ContactsRotationRecurrenceArgs",
    "ContactsRotationRecurrenceArgsDict",
    "ContactsRotationRecurrenceDailySettingArgs",
    "ContactsRotationRecurrenceDailySettingArgsDict",
    "ContactsRotationRecurrenceMonthlySettingArgs",
    "ContactsRotationRecurrenceMonthlySettingArgsDict",
    ...,
    ...,
    "ContactsRotationRecurrenceShiftCoverageArgs",
    "ContactsRotationRecurrenceShiftCoverageArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ContactsRotationRecurrenceWeeklySettingArgs",
    "ContactsRotationRecurrenceWeeklySettingArgsDict",
    ...,
    ...,
    "DocumentAttachmentsSourceArgs",
    "DocumentAttachmentsSourceArgsDict",
    "DocumentParameterArgs",
    "DocumentParameterArgsDict",
    "MaintenanceWindowTargetTargetArgs",
    "MaintenanceWindowTargetTargetArgsDict",
    "MaintenanceWindowTaskTargetArgs",
    "MaintenanceWindowTaskTargetArgsDict",
    "MaintenanceWindowTaskTaskInvocationParametersArgs",
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
    "PatchBaselineApprovalRuleArgs",
    "PatchBaselineApprovalRuleArgsDict",
    "PatchBaselineApprovalRulePatchFilterArgs",
    "PatchBaselineApprovalRulePatchFilterArgsDict",
    "PatchBaselineGlobalFilterArgs",
    "PatchBaselineGlobalFilterArgsDict",
    "PatchBaselineSourceArgs",
    "PatchBaselineSourceArgsDict",
    ...,
    ...,
    "QuicksetupConfigurationManagerStatusSummaryArgs",
    ...,
    "QuicksetupConfigurationManagerTimeoutsArgs",
    "QuicksetupConfigurationManagerTimeoutsArgsDict",
    "ResourceDataSyncS3DestinationArgs",
    "ResourceDataSyncS3DestinationArgsDict",
    "GetInstancesFilterArgs",
    "GetInstancesFilterArgsDict",
    "GetMaintenanceWindowsFilterArgs",
    "GetMaintenanceWindowsFilterArgsDict",
    "GetPatchBaselinesFilterArgs",
    "GetPatchBaselinesFilterArgsDict",
]

class AssociationOutputLocationArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    s3_key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    s3_region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AssociationOutputLocationArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_region.setter
    def s3_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssociationTargetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class AssociationTargetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ContactsRotationRecurrenceArgsDict(TypedDict):
    number_of_on_calls: pulumi.Input[_builtins.int]
    recurrence_multiplier: pulumi.Input[_builtins.int]
    daily_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceDailySettingArgsDict]]
        ]
    ]
    monthly_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceMonthlySettingArgsDict]]
        ]
    ]
    shift_coverages: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceShiftCoverageArgsDict]]
        ]
    ]
    weekly_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceWeeklySettingArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceArgs:
    def __init__(
        __self__,
        *,
        number_of_on_calls: pulumi.Input[_builtins.int],
        recurrence_multiplier: pulumi.Input[_builtins.int],
        daily_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceDailySettingArgs]]
            ]
        ] = ...,
        monthly_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceMonthlySettingArgs]]
            ]
        ] = ...,
        shift_coverages: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceShiftCoverageArgs]]
            ]
        ] = ...,
        weekly_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceWeeklySettingArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numberOfOnCalls")
    def number_of_on_calls(self) -> pulumi.Input[_builtins.int]: ...
    @number_of_on_calls.setter
    def number_of_on_calls(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="recurrenceMultiplier")
    def recurrence_multiplier(self) -> pulumi.Input[_builtins.int]: ...
    @recurrence_multiplier.setter
    def recurrence_multiplier(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dailySettings")
    def daily_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContactsRotationRecurrenceDailySettingArgs]]]
    ]: ...
    @daily_settings.setter
    def daily_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceDailySettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="monthlySettings")
    def monthly_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceMonthlySettingArgs]]
        ]
    ]: ...
    @monthly_settings.setter
    def monthly_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceMonthlySettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="shiftCoverages")
    def shift_coverages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceShiftCoverageArgs]]
        ]
    ]: ...
    @shift_coverages.setter
    def shift_coverages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceShiftCoverageArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklySettings")
    def weekly_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ContactsRotationRecurrenceWeeklySettingArgs]]
        ]
    ]: ...
    @weekly_settings.setter
    def weekly_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ContactsRotationRecurrenceWeeklySettingArgs]]
            ]
        ],
    ): ...

class ContactsRotationRecurrenceDailySettingArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    minute_of_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceDailySettingArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        minute_of_hour: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> pulumi.Input[_builtins.int]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: pulumi.Input[_builtins.int]): ...

class ContactsRotationRecurrenceMonthlySettingArgsDict(TypedDict):
    day_of_month: pulumi.Input[_builtins.int]
    hand_off_time: NotRequired[
        pulumi.Input[ContactsRotationRecurrenceMonthlySettingHandOffTimeArgsDict]
    ]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceMonthlySettingArgs:
    def __init__(
        __self__,
        *,
        day_of_month: pulumi.Input[_builtins.int],
        hand_off_time: Optional[
            pulumi.Input[ContactsRotationRecurrenceMonthlySettingHandOffTimeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> pulumi.Input[_builtins.int]: ...
    @day_of_month.setter
    def day_of_month(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="handOffTime")
    def hand_off_time(
        self,
    ) -> Optional[
        pulumi.Input[ContactsRotationRecurrenceMonthlySettingHandOffTimeArgs]
    ]: ...
    @hand_off_time.setter
    def hand_off_time(
        self,
        value: Optional[
            pulumi.Input[ContactsRotationRecurrenceMonthlySettingHandOffTimeArgs]
        ],
    ): ...

class ContactsRotationRecurrenceMonthlySettingHandOffTimeArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    minute_of_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceMonthlySettingHandOffTimeArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        minute_of_hour: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> pulumi.Input[_builtins.int]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: pulumi.Input[_builtins.int]): ...

class ContactsRotationRecurrenceShiftCoverageArgsDict(TypedDict):
    coverage_times: pulumi.Input[
        Sequence[
            pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeArgsDict]
        ]
    ]
    map_block_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceShiftCoverageArgs:
    def __init__(
        __self__,
        *,
        coverage_times: pulumi.Input[
            Sequence[
                pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeArgs]
            ]
        ],
        map_block_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coverageTimes")
    def coverage_times(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeArgs]]
    ]: ...
    @coverage_times.setter
    def coverage_times(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> pulumi.Input[_builtins.str]: ...
    @map_block_key.setter
    def map_block_key(self, value: pulumi.Input[_builtins.str]): ...

class ContactsRotationRecurrenceShiftCoverageCoverageTimeArgsDict(TypedDict):
    end: NotRequired[
        pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgsDict]
    ]
    start: NotRequired[
        pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgsDict]
    ]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceShiftCoverageCoverageTimeArgs:
    def __init__(
        __self__,
        *,
        end: Optional[
            pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgs]
        ] = ...,
        start: Optional[
            pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(
        self,
    ) -> Optional[
        pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgs]
    ]: ...
    @end.setter
    def end(
        self,
        value: Optional[
            pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def start(
        self,
    ) -> Optional[
        pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgs]
    ]: ...
    @start.setter
    def start(
        self,
        value: Optional[
            pulumi.Input[ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgs]
        ],
    ): ...

class ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    minute_of_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceShiftCoverageCoverageTimeEndArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        minute_of_hour: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> pulumi.Input[_builtins.int]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: pulumi.Input[_builtins.int]): ...

class ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    minute_of_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceShiftCoverageCoverageTimeStartArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        minute_of_hour: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> pulumi.Input[_builtins.int]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: pulumi.Input[_builtins.int]): ...

class ContactsRotationRecurrenceWeeklySettingArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    hand_off_time: NotRequired[
        pulumi.Input[ContactsRotationRecurrenceWeeklySettingHandOffTimeArgsDict]
    ]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceWeeklySettingArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        hand_off_time: Optional[
            pulumi.Input[ContactsRotationRecurrenceWeeklySettingHandOffTimeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="handOffTime")
    def hand_off_time(
        self,
    ) -> Optional[
        pulumi.Input[ContactsRotationRecurrenceWeeklySettingHandOffTimeArgs]
    ]: ...
    @hand_off_time.setter
    def hand_off_time(
        self,
        value: Optional[
            pulumi.Input[ContactsRotationRecurrenceWeeklySettingHandOffTimeArgs]
        ],
    ): ...

class ContactsRotationRecurrenceWeeklySettingHandOffTimeArgsDict(TypedDict):
    hour_of_day: pulumi.Input[_builtins.int]
    minute_of_hour: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ContactsRotationRecurrenceWeeklySettingHandOffTimeArgs:
    def __init__(
        __self__,
        *,
        hour_of_day: pulumi.Input[_builtins.int],
        minute_of_hour: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> pulumi.Input[_builtins.int]: ...
    @minute_of_hour.setter
    def minute_of_hour(self, value: pulumi.Input[_builtins.int]): ...

class DocumentAttachmentsSourceArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DocumentAttachmentsSourceArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DocumentParameterArgsDict(TypedDict):
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DocumentParameterArgs:
    def __init__(
        __self__,
        *,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MaintenanceWindowTargetTargetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class MaintenanceWindowTargetTargetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MaintenanceWindowTaskTargetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTargetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MaintenanceWindowTaskTaskInvocationParametersArgsDict(TypedDict):
    automation_parameters: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgsDict
        ]
    ]
    lambda_parameters: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgsDict
        ]
    ]
    run_command_parameters: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgsDict
        ]
    ]
    step_functions_parameters: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgsDict
        ]
    ]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersArgs:
    def __init__(
        __self__,
        *,
        automation_parameters: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs
            ]
        ] = ...,
        lambda_parameters: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs
            ]
        ] = ...,
        run_command_parameters: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs
            ]
        ] = ...,
        step_functions_parameters: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationParameters")
    def automation_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs
        ]
    ]: ...
    @automation_parameters.setter
    def automation_parameters(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaParameters")
    def lambda_parameters(
        self,
    ) -> Optional[
        pulumi.Input[MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs]
    ]: ...
    @lambda_parameters.setter
    def lambda_parameters(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runCommandParameters")
    def run_command_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs
        ]
    ]: ...
    @run_command_parameters.setter
    def run_command_parameters(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stepFunctionsParameters")
    def step_functions_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs
        ]
    ]: ...
    @step_functions_parameters.setter
    def step_functions_parameters(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs
            ]
        ],
    ): ...

class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgsDict(
    TypedDict
):
    document_version: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs:
    def __init__(
        __self__,
        *,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs
                ]
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs
                    ]
                ]
            ]
        ],
    ): ...

class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgsDict(TypedDict):
    client_context: NotRequired[pulumi.Input[_builtins.str]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    qualifier: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs:
    def __init__(
        __self__,
        *,
        client_context: Optional[pulumi.Input[_builtins.str]] = ...,
        payload: Optional[pulumi.Input[_builtins.str]] = ...,
        qualifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientContext")
    def client_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_context.setter
    def client_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgsDict(
    TypedDict
):
    cloudwatch_config: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgsDict
        ]
    ]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    document_hash: NotRequired[pulumi.Input[_builtins.str]]
    document_hash_type: NotRequired[pulumi.Input[_builtins.str]]
    document_version: NotRequired[pulumi.Input[_builtins.str]]
    notification_config: NotRequired[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgsDict
        ]
    ]
    output_s3_bucket: NotRequired[pulumi.Input[_builtins.str]]
    output_s3_key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgsDict
                ]
            ]
        ]
    ]
    service_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_config: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgs
            ]
        ] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        document_hash: Optional[pulumi.Input[_builtins.str]] = ...,
        document_hash_type: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_config: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs
            ]
        ] = ...,
        output_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        output_s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs
                    ]
                ]
            ]
        ] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchConfig")
    def cloudwatch_config(
        self,
    ) -> Optional[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgs
        ]
    ]: ...
    @cloudwatch_config.setter
    def cloudwatch_config(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentHash")
    def document_hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_hash.setter
    def document_hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentHashType")
    def document_hash_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_hash_type.setter
    def document_hash_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(
        self,
    ) -> Optional[
        pulumi.Input[
            MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs
        ]
    ]: ...
    @notification_config.setter
    def notification_config(
        self,
        value: Optional[
            pulumi.Input[
                MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputS3Bucket")
    def output_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_s3_bucket.setter
    def output_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputS3KeyPrefix")
    def output_s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_s3_key_prefix.setter
    def output_s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs
                ]
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgsDict(
    TypedDict
):
    cloudwatch_log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatch_output_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupName")
    def cloudwatch_log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_log_group_name.setter
    def cloudwatch_log_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchOutputEnabled")
    def cloudwatch_output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cloudwatch_output_enabled.setter
    def cloudwatch_output_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgsDict(
    TypedDict
):
    notification_arn: NotRequired[pulumi.Input[_builtins.str]]
    notification_events: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    notification_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs:
    def __init__(
        __self__,
        *,
        notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationArn")
    def notification_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_arn.setter
    def notification_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationEvents")
    def notification_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_events.setter
    def notification_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgsDict(
    TypedDict
):
    input: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs:
    def __init__(
        __self__,
        *,
        input: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input.setter
    def input(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PatchBaselineApprovalRuleArgsDict(TypedDict):
    patch_filters: pulumi.Input[
        Sequence[pulumi.Input[PatchBaselineApprovalRulePatchFilterArgsDict]]
    ]
    approve_after_days: NotRequired[pulumi.Input[_builtins.int]]
    approve_until_date: NotRequired[pulumi.Input[_builtins.str]]
    compliance_level: NotRequired[pulumi.Input[_builtins.str]]
    enable_non_security: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PatchBaselineApprovalRuleArgs:
    def __init__(
        __self__,
        *,
        patch_filters: pulumi.Input[
            Sequence[pulumi.Input[PatchBaselineApprovalRulePatchFilterArgs]]
        ],
        approve_after_days: Optional[pulumi.Input[_builtins.int]] = ...,
        approve_until_date: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_level: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_non_security: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patchFilters")
    def patch_filters(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PatchBaselineApprovalRulePatchFilterArgs]]
    ]: ...
    @patch_filters.setter
    def patch_filters(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PatchBaselineApprovalRulePatchFilterArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approveAfterDays")
    def approve_after_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @approve_after_days.setter
    def approve_after_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="approveUntilDate")
    def approve_until_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approve_until_date.setter
    def approve_until_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="complianceLevel")
    def compliance_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compliance_level.setter
    def compliance_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableNonSecurity")
    def enable_non_security(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_non_security.setter
    def enable_non_security(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PatchBaselineApprovalRulePatchFilterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PatchBaselineApprovalRulePatchFilterArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PatchBaselineGlobalFilterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PatchBaselineGlobalFilterArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PatchBaselineSourceArgsDict(TypedDict):
    configuration: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    products: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PatchBaselineSourceArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        products: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[_builtins.str]: ...
    @configuration.setter
    def configuration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def products(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @products.setter
    def products(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class QuicksetupConfigurationManagerConfigurationDefinitionArgsDict(TypedDict):
    parameters: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    local_deployment_administration_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    local_deployment_execution_role_name: NotRequired[pulumi.Input[_builtins.str]]
    type_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class QuicksetupConfigurationManagerConfigurationDefinitionArgs:
    def __init__(
        __self__,
        *,
        parameters: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_deployment_administration_role_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        local_deployment_execution_role_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        type_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @parameters.setter
    def parameters(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localDeploymentAdministrationRoleArn")
    def local_deployment_administration_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_deployment_administration_role_arn.setter
    def local_deployment_administration_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localDeploymentExecutionRoleName")
    def local_deployment_execution_role_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_deployment_execution_role_name.setter
    def local_deployment_execution_role_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeVersion")
    def type_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_version.setter
    def type_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QuicksetupConfigurationManagerStatusSummaryArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    status_message: pulumi.Input[_builtins.str]
    status_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class QuicksetupConfigurationManagerStatusSummaryArgs:
    def __init__(
        __self__,
        *,
        status: pulumi.Input[_builtins.str],
        status_message: pulumi.Input[_builtins.str],
        status_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusType")
    def status_type(self) -> pulumi.Input[_builtins.str]: ...
    @status_type.setter
    def status_type(self, value: pulumi.Input[_builtins.str]): ...

class QuicksetupConfigurationManagerTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class QuicksetupConfigurationManagerTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceDataSyncS3DestinationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    sync_format: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ResourceDataSyncS3DestinationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncFormat")
    def sync_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sync_format.setter
    def sync_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetInstancesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetInstancesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetMaintenanceWindowsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetMaintenanceWindowsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetPatchBaselinesFilterArgsDict(TypedDict):
    key: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetPatchBaselinesFilterArgs:
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @key.setter
    def key(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
