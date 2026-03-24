

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssociationOutputLocation', 'AssociationTarget', 'ContactsRotationRecurrence', 'ContactsRotationRecurrenceDailySetting', 'ContactsRotationRecurrenceMonthlySetting', ..., 'ContactsRotationRecurrenceShiftCoverage', ..., ..., ..., 'ContactsRotationRecurrenceWeeklySetting', 'ContactsRotationRecurrenceWeeklySettingHandOffTime', 'DocumentAttachmentsSource', 'DocumentParameter', 'MaintenanceWindowTargetTarget', 'MaintenanceWindowTaskTarget', 'MaintenanceWindowTaskTaskInvocationParameters', ..., ..., ..., ..., ..., ..., ..., ..., 'PatchBaselineApprovalRule', 'PatchBaselineApprovalRulePatchFilter', 'PatchBaselineGlobalFilter', 'PatchBaselineSource', ..., 'QuicksetupConfigurationManagerStatusSummary', 'QuicksetupConfigurationManagerTimeouts', 'ResourceDataSyncS3Destination', 'GetContactsRotationRecurrenceResult', 'GetContactsRotationRecurrenceDailySettingResult', 'GetContactsRotationRecurrenceMonthlySettingResult', ..., 'GetContactsRotationRecurrenceShiftCoverageResult', ..., ..., ..., 'GetContactsRotationRecurrenceWeeklySettingResult', ..., 'GetInstancesFilterResult', 'GetMaintenanceWindowsFilterResult', 'GetPatchBaselineApprovalRuleResult', 'GetPatchBaselineApprovalRulePatchFilterResult', 'GetPatchBaselineGlobalFilterResult', 'GetPatchBaselineSourceResult', 'GetPatchBaselinesBaselineIdentityResult', 'GetPatchBaselinesFilterResult']
@pulumi.output_type
class AssociationOutputLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, s3_bucket_name: _builtins.str, s3_key_prefix: Optional[_builtins.str] = ..., s3_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AssociationTarget(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrence(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, number_of_on_calls: _builtins.int, recurrence_multiplier: _builtins.int, daily_settings: Optional[Sequence[outputs.ContactsRotationRecurrenceDailySetting]] = ..., monthly_settings: Optional[Sequence[outputs.ContactsRotationRecurrenceMonthlySetting]] = ..., shift_coverages: Optional[Sequence[outputs.ContactsRotationRecurrenceShiftCoverage]] = ..., weekly_settings: Optional[Sequence[outputs.ContactsRotationRecurrenceWeeklySetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfOnCalls")
    def number_of_on_calls(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceMultiplier")
    def recurrence_multiplier(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySettings")
    def daily_settings(self) -> Optional[Sequence[outputs.ContactsRotationRecurrenceDailySetting]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySettings")
    def monthly_settings(self) -> Optional[Sequence[outputs.ContactsRotationRecurrenceMonthlySetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shiftCoverages")
    def shift_coverages(self) -> Optional[Sequence[outputs.ContactsRotationRecurrenceShiftCoverage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySettings")
    def weekly_settings(self) -> Optional[Sequence[outputs.ContactsRotationRecurrenceWeeklySetting]]:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceDailySetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceMonthlySetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day_of_month: _builtins.int, hand_off_time: Optional[outputs.ContactsRotationRecurrenceMonthlySettingHandOffTime] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="handOffTime")
    def hand_off_time(self) -> Optional[outputs.ContactsRotationRecurrenceMonthlySettingHandOffTime]:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceMonthlySettingHandOffTime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceShiftCoverage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, coverage_times: Sequence[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTime], map_block_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coverageTimes")
    def coverage_times(self) -> Sequence[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTime]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceShiftCoverageCoverageTime(dict):
    def __init__(__self__, *, end: Optional[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTimeEnd] = ..., start: Optional[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTimeStart] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTimeEnd]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[outputs.ContactsRotationRecurrenceShiftCoverageCoverageTimeStart]:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceShiftCoverageCoverageTimeEnd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceShiftCoverageCoverageTimeStart(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceWeeklySetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day_of_week: _builtins.str, hand_off_time: Optional[outputs.ContactsRotationRecurrenceWeeklySettingHandOffTime] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="handOffTime")
    def hand_off_time(self) -> Optional[outputs.ContactsRotationRecurrenceWeeklySettingHandOffTime]:
        
        ...
    


@pulumi.output_type
class ContactsRotationRecurrenceWeeklySettingHandOffTime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class DocumentAttachmentsSource(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DocumentParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTargetTarget(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTarget(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automation_parameters: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParameters] = ..., lambda_parameters: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersLambdaParameters] = ..., run_command_parameters: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters] = ..., step_functions_parameters: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationParameters")
    def automation_parameters(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaParameters")
    def lambda_parameters(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersLambdaParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runCommandParameters")
    def run_command_parameters(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepFunctionsParameters")
    def step_functions_parameters(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, document_version: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersLambdaParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_context: Optional[_builtins.str] = ..., payload: Optional[_builtins.str] = ..., qualifier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientContext")
    def client_context(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_config: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig] = ..., comment: Optional[_builtins.str] = ..., document_hash: Optional[_builtins.str] = ..., document_hash_type: Optional[_builtins.str] = ..., document_version: Optional[_builtins.str] = ..., notification_config: Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig] = ..., output_s3_bucket: Optional[_builtins.str] = ..., output_s3_key_prefix: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]] = ..., service_role_arn: Optional[_builtins.str] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchConfig")
    def cloudwatch_config(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentHash")
    def document_hash(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentHashType")
    def document_hash_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputS3Bucket")
    def output_s3_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputS3KeyPrefix")
    def output_s3_key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_log_group_name: Optional[_builtins.str] = ..., cloudwatch_output_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupName")
    def cloudwatch_log_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchOutputEnabled")
    def cloudwatch_output_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, notification_arn: Optional[_builtins.str] = ..., notification_events: Optional[Sequence[_builtins.str]] = ..., notification_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationArn")
    def notification_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEvents")
    def notification_events(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(dict):
    def __init__(__self__, *, input: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PatchBaselineApprovalRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, patch_filters: Sequence[outputs.PatchBaselineApprovalRulePatchFilter], approve_after_days: Optional[_builtins.int] = ..., approve_until_date: Optional[_builtins.str] = ..., compliance_level: Optional[_builtins.str] = ..., enable_non_security: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchFilters")
    def patch_filters(self) -> Sequence[outputs.PatchBaselineApprovalRulePatchFilter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAfterDays")
    def approve_after_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveUntilDate")
    def approve_until_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceLevel")
    def compliance_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNonSecurity")
    def enable_non_security(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PatchBaselineApprovalRulePatchFilter(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class PatchBaselineGlobalFilter(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class PatchBaselineSource(dict):
    def __init__(__self__, *, configuration: _builtins.str, name: _builtins.str, products: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def products(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QuicksetupConfigurationManagerConfigurationDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parameters: Mapping[str, _builtins.str], type: _builtins.str, id: Optional[_builtins.str] = ..., local_deployment_administration_role_arn: Optional[_builtins.str] = ..., local_deployment_execution_role_name: Optional[_builtins.str] = ..., type_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDeploymentAdministrationRoleArn")
    def local_deployment_administration_role_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDeploymentExecutionRoleName")
    def local_deployment_execution_role_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeVersion")
    def type_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QuicksetupConfigurationManagerStatusSummary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: _builtins.str, status_message: _builtins.str, status_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusType")
    def status_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class QuicksetupConfigurationManagerTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceDataSyncS3Destination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, region: _builtins.str, kms_key_arn: Optional[_builtins.str] = ..., prefix: Optional[_builtins.str] = ..., sync_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncFormat")
    def sync_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceResult(dict):
    def __init__(__self__, *, daily_settings: Sequence[outputs.GetContactsRotationRecurrenceDailySettingResult], monthly_settings: Sequence[outputs.GetContactsRotationRecurrenceMonthlySettingResult], number_of_on_calls: _builtins.int, recurrence_multiplier: _builtins.int, shift_coverages: Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageResult], weekly_settings: Sequence[outputs.GetContactsRotationRecurrenceWeeklySettingResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySettings")
    def daily_settings(self) -> Sequence[outputs.GetContactsRotationRecurrenceDailySettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySettings")
    def monthly_settings(self) -> Sequence[outputs.GetContactsRotationRecurrenceMonthlySettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfOnCalls")
    def number_of_on_calls(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceMultiplier")
    def recurrence_multiplier(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shiftCoverages")
    def shift_coverages(self) -> Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySettings")
    def weekly_settings(self) -> Sequence[outputs.GetContactsRotationRecurrenceWeeklySettingResult]:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceDailySettingResult(dict):
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceMonthlySettingResult(dict):
    def __init__(__self__, *, day_of_month: _builtins.int, hand_off_times: Sequence[outputs.GetContactsRotationRecurrenceMonthlySettingHandOffTimeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="handOffTimes")
    def hand_off_times(self) -> Sequence[outputs.GetContactsRotationRecurrenceMonthlySettingHandOffTimeResult]:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceMonthlySettingHandOffTimeResult(dict):
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceShiftCoverageResult(dict):
    def __init__(__self__, *, coverage_times: Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeResult], map_block_key: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coverageTimes")
    def coverage_times(self) -> Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceShiftCoverageCoverageTimeResult(dict):
    def __init__(__self__, *, ends: Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeEndResult], starts: Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeStartResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ends(self) -> Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeEndResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def starts(self) -> Sequence[outputs.GetContactsRotationRecurrenceShiftCoverageCoverageTimeStartResult]:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceShiftCoverageCoverageTimeEndResult(dict):
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceShiftCoverageCoverageTimeStartResult(dict):
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceWeeklySettingResult(dict):
    def __init__(__self__, *, day_of_week: _builtins.str, hand_off_times: Sequence[outputs.GetContactsRotationRecurrenceWeeklySettingHandOffTimeResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="handOffTimes")
    def hand_off_times(self) -> Sequence[outputs.GetContactsRotationRecurrenceWeeklySettingHandOffTimeResult]:
        ...
    


@pulumi.output_type
class GetContactsRotationRecurrenceWeeklySettingHandOffTimeResult(dict):
    def __init__(__self__, *, hour_of_day: _builtins.int, minute_of_hour: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetInstancesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetMaintenanceWindowsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPatchBaselineApprovalRuleResult(dict):
    def __init__(__self__, *, approve_after_days: _builtins.int, approve_until_date: _builtins.str, compliance_level: _builtins.str, enable_non_security: _builtins.bool, patch_filters: Sequence[outputs.GetPatchBaselineApprovalRulePatchFilterResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAfterDays")
    def approve_after_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveUntilDate")
    def approve_until_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceLevel")
    def compliance_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNonSecurity")
    def enable_non_security(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchFilters")
    def patch_filters(self) -> Sequence[outputs.GetPatchBaselineApprovalRulePatchFilterResult]:
        
        ...
    


@pulumi.output_type
class GetPatchBaselineApprovalRulePatchFilterResult(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPatchBaselineGlobalFilterResult(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPatchBaselineSourceResult(dict):
    def __init__(__self__, *, configuration: _builtins.str, name: _builtins.str, products: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def products(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPatchBaselinesBaselineIdentityResult(dict):
    def __init__(__self__, *, baseline_description: _builtins.str, baseline_id: _builtins.str, baseline_name: _builtins.str, default_baseline: _builtins.bool, operating_system: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineDescription")
    def baseline_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineId")
    def baseline_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineName")
    def baseline_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBaseline")
    def default_baseline(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPatchBaselinesFilterResult(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


