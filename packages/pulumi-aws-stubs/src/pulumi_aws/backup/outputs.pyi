import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FrameworkControl",
    "FrameworkControlInputParameter",
    "FrameworkControlScope",
    "LogicallyAirGappedVaultTimeouts",
    "PlanAdvancedBackupSetting",
    "PlanRule",
    "PlanRuleCopyAction",
    "PlanRuleCopyActionLifecycle",
    "PlanRuleLifecycle",
    "PlanRuleScanAction",
    "PlanScanSetting",
    "ReportPlanReportDeliveryChannel",
    "ReportPlanReportSetting",
    "RestoreTestingPlanRecoveryPointSelection",
    "RestoreTestingSelectionProtectedResourceConditions",
    ...,
    ...,
    "SelectionCondition",
    "SelectionConditionStringEqual",
    "SelectionConditionStringLike",
    "SelectionConditionStringNotEqual",
    "SelectionConditionStringNotLike",
    "SelectionSelectionTag",
    "GetFrameworkControlResult",
    "GetFrameworkControlInputParameterResult",
    "GetFrameworkControlScopeResult",
    "GetPlanRuleResult",
    "GetPlanRuleCopyActionResult",
    "GetPlanRuleCopyActionLifecycleResult",
    "GetPlanRuleLifecycleResult",
    "GetPlanRuleScanActionResult",
    "GetPlanScanSettingResult",
    "GetReportPlanReportDeliveryChannelResult",
    "GetReportPlanReportSettingResult",
]

@pulumi.output_type
class FrameworkControl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        input_parameters: Optional[
            Sequence[outputs.FrameworkControlInputParameter]
        ] = ...,
        scope: Optional[outputs.FrameworkControlScope] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> Optional[Sequence[outputs.FrameworkControlInputParameter]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.FrameworkControlScope]: ...

@pulumi.output_type
class FrameworkControlInputParameter(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FrameworkControlScope(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_resource_ids: Optional[Sequence[_builtins.str]] = ...,
        compliance_resource_types: Optional[Sequence[_builtins.str]] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceIds")
    def compliance_resource_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LogicallyAirGappedVaultTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanAdvancedBackupSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_options: Mapping[str, _builtins.str],
        resource_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupOptions")
    def backup_options(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...

@pulumi.output_type
class PlanRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_name: _builtins.str,
        target_vault_name: _builtins.str,
        completion_window: Optional[_builtins.int] = ...,
        copy_actions: Optional[Sequence[outputs.PlanRuleCopyAction]] = ...,
        enable_continuous_backup: Optional[_builtins.bool] = ...,
        lifecycle: Optional[outputs.PlanRuleLifecycle] = ...,
        recovery_point_tags: Optional[Mapping[str, _builtins.str]] = ...,
        scan_actions: Optional[Sequence[outputs.PlanRuleScanAction]] = ...,
        schedule: Optional[_builtins.str] = ...,
        schedule_expression_timezone: Optional[_builtins.str] = ...,
        start_window: Optional[_builtins.int] = ...,
        target_logically_air_gapped_backup_vault_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetVaultName")
    def target_vault_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="completionWindow")
    def completion_window(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="copyActions")
    def copy_actions(self) -> Optional[Sequence[outputs.PlanRuleCopyAction]]: ...
    @_builtins.property
    @pulumi.getter(name="enableContinuousBackup")
    def enable_continuous_backup(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[outputs.PlanRuleLifecycle]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scanActions")
    def scan_actions(self) -> Optional[Sequence[outputs.PlanRuleScanAction]]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startWindow")
    def start_window(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetLogicallyAirGappedBackupVaultArn")
    def target_logically_air_gapped_backup_vault_arn(
        self,
    ) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PlanRuleCopyAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_vault_arn: _builtins.str,
        lifecycle: Optional[outputs.PlanRuleCopyActionLifecycle] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationVaultArn")
    def destination_vault_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[outputs.PlanRuleCopyActionLifecycle]: ...

@pulumi.output_type
class PlanRuleCopyActionLifecycle(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cold_storage_after: Optional[_builtins.int] = ...,
        delete_after: Optional[_builtins.int] = ...,
        opt_in_to_archive_for_supported_resources: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PlanRuleLifecycle(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cold_storage_after: Optional[_builtins.int] = ...,
        delete_after: Optional[_builtins.int] = ...,
        opt_in_to_archive_for_supported_resources: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PlanRuleScanAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, malware_scanner: _builtins.str, scan_mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanMode")
    def scan_mode(self) -> _builtins.str: ...

@pulumi.output_type
class PlanScanSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        malware_scanner: _builtins.str,
        resource_types: Sequence[_builtins.str],
        scanner_role_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scannerRoleArn")
    def scanner_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ReportPlanReportDeliveryChannel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_name: _builtins.str,
        formats: Optional[Sequence[_builtins.str]] = ...,
        s3_key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def formats(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReportPlanReportSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        report_template: _builtins.str,
        accounts: Optional[Sequence[_builtins.str]] = ...,
        framework_arns: Optional[Sequence[_builtins.str]] = ...,
        number_of_frameworks: Optional[_builtins.int] = ...,
        organization_units: Optional[Sequence[_builtins.str]] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reportTemplate")
    def report_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="frameworkArns")
    def framework_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfFrameworks")
    def number_of_frameworks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="organizationUnits")
    def organization_units(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RestoreTestingPlanRecoveryPointSelection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: _builtins.str,
        include_vaults: Sequence[_builtins.str],
        recovery_point_types: Sequence[_builtins.str],
        exclude_vaults: Optional[Sequence[_builtins.str]] = ...,
        selection_window_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeVaults")
    def include_vaults(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointTypes")
    def recovery_point_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeVaults")
    def exclude_vaults(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selectionWindowDays")
    def selection_window_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RestoreTestingSelectionProtectedResourceConditions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        string_equals: Optional[
            Sequence[
                outputs.RestoreTestingSelectionProtectedResourceConditionsStringEqual
            ]
        ] = ...,
        string_not_equals: Optional[
            Sequence[
                outputs.RestoreTestingSelectionProtectedResourceConditionsStringNotEqual
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringEquals")
    def string_equals(
        self,
    ) -> Optional[
        Sequence[outputs.RestoreTestingSelectionProtectedResourceConditionsStringEqual]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stringNotEquals")
    def string_not_equals(
        self,
    ) -> Optional[
        Sequence[
            outputs.RestoreTestingSelectionProtectedResourceConditionsStringNotEqual
        ]
    ]: ...

@pulumi.output_type
class RestoreTestingSelectionProtectedResourceConditionsStringEqual(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class RestoreTestingSelectionProtectedResourceConditionsStringNotEqual(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SelectionCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        string_equals: Optional[Sequence[outputs.SelectionConditionStringEqual]] = ...,
        string_likes: Optional[Sequence[outputs.SelectionConditionStringLike]] = ...,
        string_not_equals: Optional[
            Sequence[outputs.SelectionConditionStringNotEqual]
        ] = ...,
        string_not_likes: Optional[
            Sequence[outputs.SelectionConditionStringNotLike]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringEquals")
    def string_equals(
        self,
    ) -> Optional[Sequence[outputs.SelectionConditionStringEqual]]: ...
    @_builtins.property
    @pulumi.getter(name="stringLikes")
    def string_likes(
        self,
    ) -> Optional[Sequence[outputs.SelectionConditionStringLike]]: ...
    @_builtins.property
    @pulumi.getter(name="stringNotEquals")
    def string_not_equals(
        self,
    ) -> Optional[Sequence[outputs.SelectionConditionStringNotEqual]]: ...
    @_builtins.property
    @pulumi.getter(name="stringNotLikes")
    def string_not_likes(
        self,
    ) -> Optional[Sequence[outputs.SelectionConditionStringNotLike]]: ...

@pulumi.output_type
class SelectionConditionStringEqual(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SelectionConditionStringLike(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SelectionConditionStringNotEqual(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SelectionConditionStringNotLike(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SelectionSelectionTag(dict):
    def __init__(
        __self__, *, key: _builtins.str, type: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetFrameworkControlResult(dict):
    def __init__(
        __self__,
        *,
        input_parameters: Sequence[outputs.GetFrameworkControlInputParameterResult],
        name: _builtins.str,
        scopes: Sequence[outputs.GetFrameworkControlScopeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> Sequence[outputs.GetFrameworkControlInputParameterResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[outputs.GetFrameworkControlScopeResult]: ...

@pulumi.output_type
class GetFrameworkControlInputParameterResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetFrameworkControlScopeResult(dict):
    def __init__(
        __self__,
        *,
        compliance_resource_ids: Sequence[_builtins.str],
        compliance_resource_types: Sequence[_builtins.str],
        tags: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceIds")
    def compliance_resource_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetPlanRuleResult(dict):
    def __init__(
        __self__,
        *,
        completion_window: _builtins.int,
        copy_actions: Sequence[outputs.GetPlanRuleCopyActionResult],
        enable_continuous_backup: _builtins.bool,
        lifecycles: Sequence[outputs.GetPlanRuleLifecycleResult],
        rule_name: _builtins.str,
        scan_actions: Sequence[outputs.GetPlanRuleScanActionResult],
        schedule: _builtins.str,
        schedule_expression_timezone: _builtins.str,
        start_window: _builtins.int,
        target_logically_air_gapped_backup_vault_arn: _builtins.str,
        target_vault_name: _builtins.str,
        recovery_point_tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completionWindow")
    def completion_window(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="copyActions")
    def copy_actions(self) -> Sequence[outputs.GetPlanRuleCopyActionResult]: ...
    @_builtins.property
    @pulumi.getter(name="enableContinuousBackup")
    def enable_continuous_backup(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def lifecycles(self) -> Sequence[outputs.GetPlanRuleLifecycleResult]: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanActions")
    def scan_actions(self) -> Sequence[outputs.GetPlanRuleScanActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startWindow")
    def start_window(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetLogicallyAirGappedBackupVaultArn")
    def target_logically_air_gapped_backup_vault_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetVaultName")
    def target_vault_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class GetPlanRuleCopyActionResult(dict):
    def __init__(
        __self__,
        *,
        destination_vault_arn: _builtins.str,
        lifecycles: Sequence[outputs.GetPlanRuleCopyActionLifecycleResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationVaultArn")
    def destination_vault_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lifecycles(self) -> Sequence[outputs.GetPlanRuleCopyActionLifecycleResult]: ...

@pulumi.output_type
class GetPlanRuleCopyActionLifecycleResult(dict):
    def __init__(
        __self__,
        *,
        cold_storage_after: _builtins.int,
        delete_after: _builtins.int,
        opt_in_to_archive_for_supported_resources: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(self) -> _builtins.bool: ...

@pulumi.output_type
class GetPlanRuleLifecycleResult(dict):
    def __init__(
        __self__,
        *,
        cold_storage_after: _builtins.int,
        delete_after: _builtins.int,
        opt_in_to_archive_for_supported_resources: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(self) -> _builtins.bool: ...

@pulumi.output_type
class GetPlanRuleScanActionResult(dict):
    def __init__(
        __self__, *, malware_scanner: _builtins.str, scan_mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanMode")
    def scan_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetPlanScanSettingResult(dict):
    def __init__(
        __self__,
        *,
        malware_scanner: _builtins.str,
        resource_types: Sequence[_builtins.str],
        scanner_role_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scannerRoleArn")
    def scanner_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetReportPlanReportDeliveryChannelResult(dict):
    def __init__(
        __self__,
        *,
        formats: Sequence[_builtins.str],
        s3_bucket_name: _builtins.str,
        s3_key_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def formats(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetReportPlanReportSettingResult(dict):
    def __init__(
        __self__,
        *,
        accounts: Sequence[_builtins.str],
        framework_arns: Sequence[_builtins.str],
        number_of_frameworks: _builtins.int,
        organization_units: Sequence[_builtins.str],
        regions: Sequence[_builtins.str],
        report_template: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frameworkArns")
    def framework_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfFrameworks")
    def number_of_frameworks(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="organizationUnits")
    def organization_units(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportTemplate")
    def report_template(self) -> _builtins.str: ...
