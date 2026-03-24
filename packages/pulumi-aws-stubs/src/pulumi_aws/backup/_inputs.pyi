import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FrameworkControlArgs",
    "FrameworkControlArgsDict",
    "FrameworkControlInputParameterArgs",
    "FrameworkControlInputParameterArgsDict",
    "FrameworkControlScopeArgs",
    "FrameworkControlScopeArgsDict",
    "LogicallyAirGappedVaultTimeoutsArgs",
    "LogicallyAirGappedVaultTimeoutsArgsDict",
    "PlanAdvancedBackupSettingArgs",
    "PlanAdvancedBackupSettingArgsDict",
    "PlanRuleArgs",
    "PlanRuleArgsDict",
    "PlanRuleCopyActionArgs",
    "PlanRuleCopyActionArgsDict",
    "PlanRuleCopyActionLifecycleArgs",
    "PlanRuleCopyActionLifecycleArgsDict",
    "PlanRuleLifecycleArgs",
    "PlanRuleLifecycleArgsDict",
    "PlanRuleScanActionArgs",
    "PlanRuleScanActionArgsDict",
    "PlanScanSettingArgs",
    "PlanScanSettingArgsDict",
    "ReportPlanReportDeliveryChannelArgs",
    "ReportPlanReportDeliveryChannelArgsDict",
    "ReportPlanReportSettingArgs",
    "ReportPlanReportSettingArgsDict",
    "RestoreTestingPlanRecoveryPointSelectionArgs",
    "RestoreTestingPlanRecoveryPointSelectionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "SelectionConditionArgs",
    "SelectionConditionArgsDict",
    "SelectionConditionStringEqualArgs",
    "SelectionConditionStringEqualArgsDict",
    "SelectionConditionStringLikeArgs",
    "SelectionConditionStringLikeArgsDict",
    "SelectionConditionStringNotEqualArgs",
    "SelectionConditionStringNotEqualArgsDict",
    "SelectionConditionStringNotLikeArgs",
    "SelectionConditionStringNotLikeArgsDict",
    "SelectionSelectionTagArgs",
    "SelectionSelectionTagArgsDict",
]

class FrameworkControlArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    input_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FrameworkControlInputParameterArgsDict]]]
    ]
    scope: NotRequired[pulumi.Input[FrameworkControlScopeArgsDict]]
    ...

@pulumi.input_type
class FrameworkControlArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        input_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrameworkControlInputParameterArgs]]]
        ] = ...,
        scope: Optional[pulumi.Input[FrameworkControlScopeArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputParameters")
    def input_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FrameworkControlInputParameterArgs]]]
    ]: ...
    @input_parameters.setter
    def input_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrameworkControlInputParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[FrameworkControlScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[FrameworkControlScopeArgs]]): ...

class FrameworkControlInputParameterArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FrameworkControlInputParameterArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkControlScopeArgsDict(TypedDict):
    compliance_resource_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    compliance_resource_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class FrameworkControlScopeArgs:
    def __init__(
        __self__,
        *,
        compliance_resource_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compliance_resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceIds")
    def compliance_resource_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @compliance_resource_ids.setter
    def compliance_resource_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @compliance_resource_types.setter
    def compliance_resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LogicallyAirGappedVaultTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LogicallyAirGappedVaultTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PlanAdvancedBackupSettingArgsDict(TypedDict):
    backup_options: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    resource_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanAdvancedBackupSettingArgs:
    def __init__(
        __self__,
        *,
        backup_options: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        resource_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupOptions")
    def backup_options(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @backup_options.setter
    def backup_options(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...

class PlanRuleArgsDict(TypedDict):
    rule_name: pulumi.Input[_builtins.str]
    target_vault_name: pulumi.Input[_builtins.str]
    completion_window: NotRequired[pulumi.Input[_builtins.int]]
    copy_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanRuleCopyActionArgsDict]]]
    ]
    enable_continuous_backup: NotRequired[pulumi.Input[_builtins.bool]]
    lifecycle: NotRequired[pulumi.Input[PlanRuleLifecycleArgsDict]]
    recovery_point_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    scan_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlanRuleScanActionArgsDict]]]
    ]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    schedule_expression_timezone: NotRequired[pulumi.Input[_builtins.str]]
    start_window: NotRequired[pulumi.Input[_builtins.int]]
    target_logically_air_gapped_backup_vault_arn: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    ...

@pulumi.input_type
class PlanRuleArgs:
    def __init__(
        __self__,
        *,
        rule_name: pulumi.Input[_builtins.str],
        target_vault_name: pulumi.Input[_builtins.str],
        completion_window: Optional[pulumi.Input[_builtins.int]] = ...,
        copy_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanRuleCopyActionArgs]]]
        ] = ...,
        enable_continuous_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        lifecycle: Optional[pulumi.Input[PlanRuleLifecycleArgs]] = ...,
        recovery_point_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        scan_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanRuleScanActionArgs]]]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        start_window: Optional[pulumi.Input[_builtins.int]] = ...,
        target_logically_air_gapped_backup_vault_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetVaultName")
    def target_vault_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_vault_name.setter
    def target_vault_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="completionWindow")
    def completion_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @completion_window.setter
    def completion_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="copyActions")
    def copy_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleCopyActionArgs]]]]: ...
    @copy_actions.setter
    def copy_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleCopyActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableContinuousBackup")
    def enable_continuous_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_continuous_backup.setter
    def enable_continuous_backup(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input[PlanRuleLifecycleArgs]]: ...
    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input[PlanRuleLifecycleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @recovery_point_tags.setter
    def recovery_point_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanActions")
    def scan_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleScanActionArgs]]]]: ...
    @scan_actions.setter
    def scan_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleScanActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startWindow")
    def start_window(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_window.setter
    def start_window(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetLogicallyAirGappedBackupVaultArn")
    def target_logically_air_gapped_backup_vault_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_logically_air_gapped_backup_vault_arn.setter
    def target_logically_air_gapped_backup_vault_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PlanRuleCopyActionArgsDict(TypedDict):
    destination_vault_arn: pulumi.Input[_builtins.str]
    lifecycle: NotRequired[pulumi.Input[PlanRuleCopyActionLifecycleArgsDict]]
    ...

@pulumi.input_type
class PlanRuleCopyActionArgs:
    def __init__(
        __self__,
        *,
        destination_vault_arn: pulumi.Input[_builtins.str],
        lifecycle: Optional[pulumi.Input[PlanRuleCopyActionLifecycleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationVaultArn")
    def destination_vault_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_vault_arn.setter
    def destination_vault_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input[PlanRuleCopyActionLifecycleArgs]]: ...
    @lifecycle.setter
    def lifecycle(
        self, value: Optional[pulumi.Input[PlanRuleCopyActionLifecycleArgs]]
    ): ...

class PlanRuleCopyActionLifecycleArgsDict(TypedDict):
    cold_storage_after: NotRequired[pulumi.Input[_builtins.int]]
    delete_after: NotRequired[pulumi.Input[_builtins.int]]
    opt_in_to_archive_for_supported_resources: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PlanRuleCopyActionLifecycleArgs:
    def __init__(
        __self__,
        *,
        cold_storage_after: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_after: Optional[pulumi.Input[_builtins.int]] = ...,
        opt_in_to_archive_for_supported_resources: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cold_storage_after.setter
    def cold_storage_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delete_after.setter
    def delete_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @opt_in_to_archive_for_supported_resources.setter
    def opt_in_to_archive_for_supported_resources(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PlanRuleLifecycleArgsDict(TypedDict):
    cold_storage_after: NotRequired[pulumi.Input[_builtins.int]]
    delete_after: NotRequired[pulumi.Input[_builtins.int]]
    opt_in_to_archive_for_supported_resources: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PlanRuleLifecycleArgs:
    def __init__(
        __self__,
        *,
        cold_storage_after: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_after: Optional[pulumi.Input[_builtins.int]] = ...,
        opt_in_to_archive_for_supported_resources: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cold_storage_after.setter
    def cold_storage_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delete_after.setter
    def delete_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="optInToArchiveForSupportedResources")
    def opt_in_to_archive_for_supported_resources(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @opt_in_to_archive_for_supported_resources.setter
    def opt_in_to_archive_for_supported_resources(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PlanRuleScanActionArgsDict(TypedDict):
    malware_scanner: pulumi.Input[_builtins.str]
    scan_mode: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanRuleScanActionArgs:
    def __init__(
        __self__,
        *,
        malware_scanner: pulumi.Input[_builtins.str],
        scan_mode: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> pulumi.Input[_builtins.str]: ...
    @malware_scanner.setter
    def malware_scanner(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scanMode")
    def scan_mode(self) -> pulumi.Input[_builtins.str]: ...
    @scan_mode.setter
    def scan_mode(self, value: pulumi.Input[_builtins.str]): ...

class PlanScanSettingArgsDict(TypedDict):
    malware_scanner: pulumi.Input[_builtins.str]
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    scanner_role_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PlanScanSettingArgs:
    def __init__(
        __self__,
        *,
        malware_scanner: pulumi.Input[_builtins.str],
        resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        scanner_role_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="malwareScanner")
    def malware_scanner(self) -> pulumi.Input[_builtins.str]: ...
    @malware_scanner.setter
    def malware_scanner(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scannerRoleArn")
    def scanner_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @scanner_role_arn.setter
    def scanner_role_arn(self, value: pulumi.Input[_builtins.str]): ...

class ReportPlanReportDeliveryChannelArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    formats: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    s3_key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ReportPlanReportDeliveryChannelArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        formats: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def formats(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @formats.setter
    def formats(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReportPlanReportSettingArgsDict(TypedDict):
    report_template: pulumi.Input[_builtins.str]
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    framework_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    number_of_frameworks: NotRequired[pulumi.Input[_builtins.int]]
    organization_units: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ReportPlanReportSettingArgs:
    def __init__(
        __self__,
        *,
        report_template: pulumi.Input[_builtins.str],
        accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        framework_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        number_of_frameworks: Optional[pulumi.Input[_builtins.int]] = ...,
        organization_units: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reportTemplate")
    def report_template(self) -> pulumi.Input[_builtins.str]: ...
    @report_template.setter
    def report_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accounts.setter
    def accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="frameworkArns")
    def framework_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @framework_arns.setter
    def framework_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfFrameworks")
    def number_of_frameworks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_frameworks.setter
    def number_of_frameworks(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationUnits")
    def organization_units(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organization_units.setter
    def organization_units(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestoreTestingPlanRecoveryPointSelectionArgsDict(TypedDict):
    algorithm: pulumi.Input[_builtins.str]
    include_vaults: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    recovery_point_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    exclude_vaults: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    selection_window_days: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class RestoreTestingPlanRecoveryPointSelectionArgs:
    def __init__(
        __self__,
        *,
        algorithm: pulumi.Input[_builtins.str],
        include_vaults: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        recovery_point_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        exclude_vaults: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        selection_window_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @algorithm.setter
    def algorithm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeVaults")
    def include_vaults(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @include_vaults.setter
    def include_vaults(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointTypes")
    def recovery_point_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @recovery_point_types.setter
    def recovery_point_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeVaults")
    def exclude_vaults(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_vaults.setter
    def exclude_vaults(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectionWindowDays")
    def selection_window_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @selection_window_days.setter
    def selection_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RestoreTestingSelectionProtectedResourceConditionsArgsDict(TypedDict):
    string_equals: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreTestingSelectionProtectedResourceConditionsStringEqualArgsDict
                ]
            ]
        ]
    ]
    string_not_equals: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RestoreTestingSelectionProtectedResourceConditionsArgs:
    def __init__(
        __self__,
        *,
        string_equals: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreTestingSelectionProtectedResourceConditionsStringEqualArgs
                    ]
                ]
            ]
        ] = ...,
        string_not_equals: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringEquals")
    def string_equals(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreTestingSelectionProtectedResourceConditionsStringEqualArgs
                ]
            ]
        ]
    ]: ...
    @string_equals.setter
    def string_equals(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreTestingSelectionProtectedResourceConditionsStringEqualArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringNotEquals")
    def string_not_equals(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgs
                ]
            ]
        ]
    ]: ...
    @string_not_equals.setter
    def string_not_equals(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgs
                    ]
                ]
            ]
        ],
    ): ...

class RestoreTestingSelectionProtectedResourceConditionsStringEqualArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RestoreTestingSelectionProtectedResourceConditionsStringEqualArgs:
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

class RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RestoreTestingSelectionProtectedResourceConditionsStringNotEqualArgs:
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

class SelectionConditionArgsDict(TypedDict):
    string_equals: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringEqualArgsDict]]]
    ]
    string_likes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringLikeArgsDict]]]
    ]
    string_not_equals: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotEqualArgsDict]]]
    ]
    string_not_likes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotLikeArgsDict]]]
    ]
    ...

@pulumi.input_type
class SelectionConditionArgs:
    def __init__(
        __self__,
        *,
        string_equals: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringEqualArgs]]]
        ] = ...,
        string_likes: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringLikeArgs]]]
        ] = ...,
        string_not_equals: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotEqualArgs]]]
        ] = ...,
        string_not_likes: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotLikeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringEquals")
    def string_equals(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringEqualArgs]]]
    ]: ...
    @string_equals.setter
    def string_equals(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringEqualArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringLikes")
    def string_likes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringLikeArgs]]]
    ]: ...
    @string_likes.setter
    def string_likes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringLikeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringNotEquals")
    def string_not_equals(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotEqualArgs]]]
    ]: ...
    @string_not_equals.setter
    def string_not_equals(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotEqualArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringNotLikes")
    def string_not_likes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotLikeArgs]]]
    ]: ...
    @string_not_likes.setter
    def string_not_likes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionStringNotLikeArgs]]]
        ],
    ): ...

class SelectionConditionStringEqualArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SelectionConditionStringEqualArgs:
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

class SelectionConditionStringLikeArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SelectionConditionStringLikeArgs:
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

class SelectionConditionStringNotEqualArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SelectionConditionStringNotEqualArgs:
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

class SelectionConditionStringNotLikeArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SelectionConditionStringNotLikeArgs:
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

class SelectionSelectionTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SelectionSelectionTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
