import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LifecyclePolicyPolicyDetails",
    "LifecyclePolicyPolicyDetailsAction",
    "LifecyclePolicyPolicyDetailsActionCrossRegionCopy",
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsEventSource",
    "LifecyclePolicyPolicyDetailsEventSourceParameters",
    "LifecyclePolicyPolicyDetailsExclusions",
    "LifecyclePolicyPolicyDetailsParameters",
    "LifecyclePolicyPolicyDetailsSchedule",
    "LifecyclePolicyPolicyDetailsScheduleArchiveRule",
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsScheduleCreateRule",
    ...,
    ...,
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsScheduleDeprecateRule",
    ...,
    "LifecyclePolicyPolicyDetailsScheduleRetainRule",
    "LifecyclePolicyPolicyDetailsScheduleShareRule",
]

@pulumi.output_type
class LifecyclePolicyPolicyDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: Optional[outputs.LifecyclePolicyPolicyDetailsAction] = ...,
        copy_tags: Optional[_builtins.bool] = ...,
        create_interval: Optional[_builtins.int] = ...,
        event_source: Optional[outputs.LifecyclePolicyPolicyDetailsEventSource] = ...,
        exclusions: Optional[outputs.LifecyclePolicyPolicyDetailsExclusions] = ...,
        extend_deletion: Optional[_builtins.bool] = ...,
        parameters: Optional[outputs.LifecyclePolicyPolicyDetailsParameters] = ...,
        policy_language: Optional[_builtins.str] = ...,
        policy_type: Optional[_builtins.str] = ...,
        resource_locations: Optional[_builtins.str] = ...,
        resource_type: Optional[_builtins.str] = ...,
        resource_types: Optional[Sequence[_builtins.str]] = ...,
        retain_interval: Optional[_builtins.int] = ...,
        schedules: Optional[
            Sequence[outputs.LifecyclePolicyPolicyDetailsSchedule]
        ] = ...,
        target_tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.LifecyclePolicyPolicyDetailsAction]: ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="createInterval")
    def create_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsEventSource]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsExclusions]: ...
    @_builtins.property
    @pulumi.getter(name="extendDeletion")
    def extend_deletion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsParameters]: ...
    @_builtins.property
    @pulumi.getter(name="policyLanguage")
    def policy_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLocations")
    def resource_locations(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retainInterval")
    def retain_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def schedules(
        self,
    ) -> Optional[Sequence[outputs.LifecyclePolicyPolicyDetailsSchedule]]: ...
    @_builtins.property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_region_copies: Sequence[
            outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopy
        ],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossRegionCopies")
    def cross_region_copies(
        self,
    ) -> Sequence[outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopy]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_configuration: outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration,
        target: _builtins.str,
        retain_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> (
        outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(
        self,
    ) -> Optional[
        outputs.LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule
    ]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cmk_arn: Optional[_builtins.str] = ...,
        encrypted: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cmkArn")
    def cmk_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, interval: _builtins.int, interval_unit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> _builtins.str: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsEventSource(dict):
    def __init__(
        __self__,
        *,
        parameters: outputs.LifecyclePolicyPolicyDetailsEventSourceParameters,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> outputs.LifecyclePolicyPolicyDetailsEventSourceParameters: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsEventSourceParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description_regex: _builtins.str,
        event_type: _builtins.str,
        snapshot_owners: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="descriptionRegex")
    def description_regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotOwners")
    def snapshot_owners(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsExclusions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclude_boot_volumes: Optional[_builtins.bool] = ...,
        exclude_tags: Optional[Mapping[str, _builtins.str]] = ...,
        exclude_volume_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeBootVolumes")
    def exclude_boot_volumes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludeTags")
    def exclude_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeVolumeTypes")
    def exclude_volume_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclude_boot_volume: Optional[_builtins.bool] = ...,
        no_reboot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeBootVolume")
    def exclude_boot_volume(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="noReboot")
    def no_reboot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_rule: outputs.LifecyclePolicyPolicyDetailsScheduleCreateRule,
        name: _builtins.str,
        retain_rule: outputs.LifecyclePolicyPolicyDetailsScheduleRetainRule,
        archive_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRule
        ] = ...,
        copy_tags: Optional[_builtins.bool] = ...,
        cross_region_copy_rules: Optional[
            Sequence[outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]
        ] = ...,
        deprecate_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleDeprecateRule
        ] = ...,
        fast_restore_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleFastRestoreRule
        ] = ...,
        share_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleShareRule
        ] = ...,
        tags_to_add: Optional[Mapping[str, _builtins.str]] = ...,
        variable_tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createRule")
    def create_rule(self) -> outputs.LifecyclePolicyPolicyDetailsScheduleCreateRule: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(self) -> outputs.LifecyclePolicyPolicyDetailsScheduleRetainRule: ...
    @_builtins.property
    @pulumi.getter(name="archiveRule")
    def archive_rule(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRule]: ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crossRegionCopyRules")
    def cross_region_copy_rules(
        self,
    ) -> Optional[
        Sequence[outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsScheduleDeprecateRule]: ...
    @_builtins.property
    @pulumi.getter(name="fastRestoreRule")
    def fast_restore_rule(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsScheduleFastRestoreRule]: ...
    @_builtins.property
    @pulumi.getter(name="shareRule")
    def share_rule(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsScheduleShareRule]: ...
    @_builtins.property
    @pulumi.getter(name="tagsToAdd")
    def tags_to_add(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="variableTags")
    def variable_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_retain_rule: outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRule,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveRetainRule")
    def archive_retain_rule(
        self,
    ) -> outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRule: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        retention_archive_tier: outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTier,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionArchiveTier")
    def retention_archive_tier(
        self,
    ) -> outputs.LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTier: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTier(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.int] = ...,
        interval: Optional[_builtins.int] = ...,
        interval_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCreateRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cron_expression: Optional[_builtins.str] = ...,
        interval: Optional[_builtins.int] = ...,
        interval_unit: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        scripts: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleCreateRuleScripts
        ] = ...,
        times: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scripts(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailsScheduleCreateRuleScripts]: ...
    @_builtins.property
    @pulumi.getter
    def times(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCreateRuleScripts(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_handler: _builtins.str,
        execute_operation_on_script_failure: Optional[_builtins.bool] = ...,
        execution_handler_service: Optional[_builtins.str] = ...,
        execution_timeout: Optional[_builtins.int] = ...,
        maximum_retry_count: Optional[_builtins.int] = ...,
        stages: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionHandler")
    def execution_handler(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="executeOperationOnScriptFailure")
    def execute_operation_on_script_failure(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="executionHandlerService")
    def execution_handler_service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryCount")
    def maximum_retry_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encrypted: _builtins.bool,
        cmk_arn: Optional[_builtins.str] = ...,
        copy_tags: Optional[_builtins.bool] = ...,
        deprecate_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule
        ] = ...,
        retain_rule: Optional[
            outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule
        ] = ...,
        target: Optional[_builtins.str] = ...,
        target_region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="cmkArn")
    def cmk_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> Optional[
        outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(
        self,
    ) -> Optional[
        outputs.LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule
    ]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, interval: _builtins.int, interval_unit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> _builtins.str: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, interval: _builtins.int, interval_unit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> _builtins.str: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleDeprecateRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.int] = ...,
        interval: Optional[_builtins.int] = ...,
        interval_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleFastRestoreRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zones: Sequence[_builtins.str],
        count: Optional[_builtins.int] = ...,
        interval: Optional[_builtins.int] = ...,
        interval_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleRetainRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: Optional[_builtins.int] = ...,
        interval: Optional[_builtins.int] = ...,
        interval_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailsScheduleShareRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_accounts: Sequence[_builtins.str],
        unshare_interval: Optional[_builtins.int] = ...,
        unshare_interval_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetAccounts")
    def target_accounts(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unshareInterval")
    def unshare_interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="unshareIntervalUnit")
    def unshare_interval_unit(self) -> Optional[_builtins.str]: ...
