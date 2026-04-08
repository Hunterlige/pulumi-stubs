import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LifecyclePolicyPolicyDetailsArgs",
    "LifecyclePolicyPolicyDetailsArgsDict",
    "LifecyclePolicyPolicyDetailsActionArgs",
    "LifecyclePolicyPolicyDetailsActionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsEventSourceArgs",
    "LifecyclePolicyPolicyDetailsEventSourceArgsDict",
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsExclusionsArgs",
    "LifecyclePolicyPolicyDetailsExclusionsArgsDict",
    "LifecyclePolicyPolicyDetailsParametersArgs",
    "LifecyclePolicyPolicyDetailsParametersArgsDict",
    "LifecyclePolicyPolicyDetailsScheduleArgs",
    "LifecyclePolicyPolicyDetailsScheduleArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs",
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
    "LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs",
    ...,
    "LifecyclePolicyPolicyDetailsScheduleShareRuleArgs",
    ...,
]

class LifecyclePolicyPolicyDetailsArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[LifecyclePolicyPolicyDetailsActionArgsDict]]
    copy_tags: NotRequired[pulumi.Input[_builtins.bool]]
    create_interval: NotRequired[pulumi.Input[_builtins.int]]
    event_source: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceArgsDict]
    ]
    exclusions: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsExclusionsArgsDict]
    ]
    extend_deletion: NotRequired[pulumi.Input[_builtins.bool]]
    parameters: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsParametersArgsDict]
    ]
    policy_language: NotRequired[pulumi.Input[_builtins.str]]
    policy_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_locations: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    retain_interval: NotRequired[pulumi.Input[_builtins.int]]
    schedules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArgsDict]]
        ]
    ]
    target_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[LifecyclePolicyPolicyDetailsActionArgs]] = ...,
        copy_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        event_source: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceArgs]
        ] = ...,
        exclusions: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsExclusionsArgs]
        ] = ...,
        extend_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsParametersArgs]
        ] = ...,
        policy_language: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_locations: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        retain_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        schedules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArgs]]
            ]
        ] = ...,
        target_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailsActionArgs]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[LifecyclePolicyPolicyDetailsActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags.setter
    def copy_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createInterval")
    def create_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @create_interval.setter
    def create_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceArgs]]: ...
    @event_source.setter
    def event_source(
        self, value: Optional[pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailsExclusionsArgs]]: ...
    @exclusions.setter
    def exclusions(
        self, value: Optional[pulumi.Input[LifecyclePolicyPolicyDetailsExclusionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendDeletion")
    def extend_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @extend_deletion.setter
    def extend_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailsParametersArgs]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[LifecyclePolicyPolicyDetailsParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyLanguage")
    def policy_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_language.setter
    def policy_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLocations")
    def resource_locations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_locations.setter
    def resource_locations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retainInterval")
    def retain_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retain_interval.setter
    def retain_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schedules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArgs]]]
    ]: ...
    @schedules.setter
    def schedules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetTags")
    def target_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @target_tags.setter
    def target_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailsActionArgsDict(TypedDict):
    cross_region_copies: pulumi.Input[
        Sequence[
            pulumi.Input[LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgsDict]
        ]
    ]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsActionArgs:
    def __init__(
        __self__,
        *,
        cross_region_copies: pulumi.Input[
            Sequence[
                pulumi.Input[LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgs]
            ]
        ],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossRegionCopies")
    def cross_region_copies(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgs]]
    ]: ...
    @cross_region_copies.setter
    def cross_region_copies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgsDict(TypedDict):
    encryption_configuration: pulumi.Input[
        LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgsDict
    ]
    target: pulumi.Input[_builtins.str]
    retain_rule: NotRequired[
        pulumi.Input[
            LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgsDict
        ]
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopyArgs:
    def __init__(
        __self__,
        *,
        encryption_configuration: pulumi.Input[
            LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgs
        ],
        target: pulumi.Input[_builtins.str],
        retain_rule: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> pulumi.Input[
        LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgs
    ]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: pulumi.Input[
            LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgs]
    ]: ...
    @retain_rule.setter
    def retain_rule(
        self,
        value: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgs
            ]
        ],
    ): ...

class LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgsDict(
    TypedDict
):
    cmk_arn: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopyEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        cmk_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cmkArn")
    def cmk_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cmk_arn.setter
    def cmk_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgsDict(TypedDict):
    interval: pulumi.Input[_builtins.int]
    interval_unit: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsActionCrossRegionCopyRetainRuleArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.int],
        interval_unit: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> pulumi.Input[_builtins.str]: ...
    @interval_unit.setter
    def interval_unit(self, value: pulumi.Input[_builtins.str]): ...

class LifecyclePolicyPolicyDetailsEventSourceArgsDict(TypedDict):
    parameters: pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceParametersArgsDict]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsEventSourceArgs:
    def __init__(
        __self__,
        *,
        parameters: pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceParametersArgs],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceParametersArgs]: ...
    @parameters.setter
    def parameters(
        self, value: pulumi.Input[LifecyclePolicyPolicyDetailsEventSourceParametersArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class LifecyclePolicyPolicyDetailsEventSourceParametersArgsDict(TypedDict):
    description_regex: pulumi.Input[_builtins.str]
    event_type: pulumi.Input[_builtins.str]
    snapshot_owners: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsEventSourceParametersArgs:
    def __init__(
        __self__,
        *,
        description_regex: pulumi.Input[_builtins.str],
        event_type: pulumi.Input[_builtins.str],
        snapshot_owners: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="descriptionRegex")
    def description_regex(self) -> pulumi.Input[_builtins.str]: ...
    @description_regex.setter
    def description_regex(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]: ...
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotOwners")
    def snapshot_owners(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @snapshot_owners.setter
    def snapshot_owners(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class LifecyclePolicyPolicyDetailsExclusionsArgsDict(TypedDict):
    exclude_boot_volumes: NotRequired[pulumi.Input[_builtins.bool]]
    exclude_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    exclude_volume_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsExclusionsArgs:
    def __init__(
        __self__,
        *,
        exclude_boot_volumes: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclude_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_volume_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeBootVolumes")
    def exclude_boot_volumes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_boot_volumes.setter
    def exclude_boot_volumes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeTags")
    def exclude_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @exclude_tags.setter
    def exclude_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeVolumeTypes")
    def exclude_volume_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_volume_types.setter
    def exclude_volume_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailsParametersArgsDict(TypedDict):
    exclude_boot_volume: NotRequired[pulumi.Input[_builtins.bool]]
    no_reboot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsParametersArgs:
    def __init__(
        __self__,
        *,
        exclude_boot_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_reboot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeBootVolume")
    def exclude_boot_volume(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_boot_volume.setter
    def exclude_boot_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noReboot")
    def no_reboot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_reboot.setter
    def no_reboot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LifecyclePolicyPolicyDetailsScheduleArgsDict(TypedDict):
    create_rule: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleArgsDict]
    name: pulumi.Input[_builtins.str]
    retain_rule: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleRetainRuleArgsDict]
    archive_rule: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgsDict]
    ]
    copy_tags: NotRequired[pulumi.Input[_builtins.bool]]
    cross_region_copy_rules: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgsDict
                ]
            ]
        ]
    ]
    deprecate_rule: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgsDict]
    ]
    fast_restore_rule: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgsDict]
    ]
    share_rule: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleShareRuleArgsDict]
    ]
    tags_to_add: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    variable_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleArgs:
    def __init__(
        __self__,
        *,
        create_rule: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs],
        name: pulumi.Input[_builtins.str],
        retain_rule: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs],
        archive_rule: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgs]
        ] = ...,
        copy_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        cross_region_copy_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgs
                    ]
                ]
            ]
        ] = ...,
        deprecate_rule: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgs]
        ] = ...,
        fast_restore_rule: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgs]
        ] = ...,
        share_rule: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleShareRuleArgs]
        ] = ...,
        tags_to_add: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        variable_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createRule")
    def create_rule(
        self,
    ) -> pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs]: ...
    @create_rule.setter
    def create_rule(
        self, value: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(
        self,
    ) -> pulumi.Input[LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs]: ...
    @retain_rule.setter
    def retain_rule(
        self, value: pulumi.Input[LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="archiveRule")
    def archive_rule(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgs]
    ]: ...
    @archive_rule.setter
    def archive_rule(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags.setter
    def copy_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRegionCopyRules")
    def cross_region_copy_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgs
                ]
            ]
        ]
    ]: ...
    @cross_region_copy_rules.setter
    def cross_region_copy_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgs]
    ]: ...
    @deprecate_rule.setter
    def deprecate_rule(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastRestoreRule")
    def fast_restore_rule(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgs]
    ]: ...
    @fast_restore_rule.setter
    def fast_restore_rule(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="shareRule")
    def share_rule(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailsScheduleShareRuleArgs]]: ...
    @share_rule.setter
    def share_rule(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleShareRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsToAdd")
    def tags_to_add(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_to_add.setter
    def tags_to_add(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="variableTags")
    def variable_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @variable_tags.setter
    def variable_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgsDict(TypedDict):
    archive_retain_rule: pulumi.Input[
        LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgsDict
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArgs:
    def __init__(
        __self__,
        *,
        archive_retain_rule: pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveRetainRule")
    def archive_retain_rule(
        self,
    ) -> pulumi.Input[
        LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgs
    ]: ...
    @archive_retain_rule.setter
    def archive_retain_rule(
        self,
        value: pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgs
        ],
    ): ...

class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgsDict(
    TypedDict
):
    retention_archive_tier: pulumi.Input[
        LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgsDict
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleArgs:
    def __init__(
        __self__,
        *,
        retention_archive_tier: pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionArchiveTier")
    def retention_archive_tier(
        self,
    ) -> pulumi.Input[
        LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgs
    ]: ...
    @retention_archive_tier.setter
    def retention_archive_tier(
        self,
        value: pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgs
        ],
    ): ...

class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgsDict(
    TypedDict
):
    count: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleArchiveRuleArchiveRetainRuleRetentionArchiveTierArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleCreateRuleArgsDict(TypedDict):
    cron_expression: NotRequired[pulumi.Input[_builtins.str]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    scripts: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgsDict]
    ]
    times: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleCreateRuleArgs:
    def __init__(
        __self__,
        *,
        cron_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        scripts: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgs]
        ] = ...,
        times: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_expression.setter
    def cron_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scripts(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgs]
    ]: ...
    @scripts.setter
    def scripts(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def times(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @times.setter
    def times(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgsDict(TypedDict):
    execution_handler: pulumi.Input[_builtins.str]
    execute_operation_on_script_failure: NotRequired[pulumi.Input[_builtins.bool]]
    execution_handler_service: NotRequired[pulumi.Input[_builtins.str]]
    execution_timeout: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_count: NotRequired[pulumi.Input[_builtins.int]]
    stages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleCreateRuleScriptsArgs:
    def __init__(
        __self__,
        *,
        execution_handler: pulumi.Input[_builtins.str],
        execute_operation_on_script_failure: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        execution_handler_service: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_retry_count: Optional[pulumi.Input[_builtins.int]] = ...,
        stages: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionHandler")
    def execution_handler(self) -> pulumi.Input[_builtins.str]: ...
    @execution_handler.setter
    def execution_handler(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executeOperationOnScriptFailure")
    def execute_operation_on_script_failure(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @execute_operation_on_script_failure.setter
    def execute_operation_on_script_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionHandlerService")
    def execution_handler_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_handler_service.setter
    def execution_handler_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryCount")
    def maximum_retry_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_retry_count.setter
    def maximum_retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stages.setter
    def stages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgsDict(TypedDict):
    encrypted: pulumi.Input[_builtins.bool]
    cmk_arn: NotRequired[pulumi.Input[_builtins.str]]
    copy_tags: NotRequired[pulumi.Input[_builtins.bool]]
    deprecate_rule: NotRequired[
        pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgsDict
        ]
    ]
    retain_rule: NotRequired[
        pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgsDict
        ]
    ]
    target: NotRequired[pulumi.Input[_builtins.str]]
    target_region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleArgs:
    def __init__(
        __self__,
        *,
        encrypted: pulumi.Input[_builtins.bool],
        cmk_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        deprecate_rule: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgs
            ]
        ] = ...,
        retain_rule: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgs
            ]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Input[_builtins.bool]: ...
    @encrypted.setter
    def encrypted(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="cmkArn")
    def cmk_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cmk_arn.setter
    def cmk_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @copy_tags.setter
    def copy_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deprecateRule")
    def deprecate_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgs
        ]
    ]: ...
    @deprecate_rule.setter
    def deprecate_rule(
        self,
        value: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retainRule")
    def retain_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgs
        ]
    ]: ...
    @retain_rule.setter
    def retain_rule(
        self,
        value: Optional[
            pulumi.Input[
                LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_region.setter
    def target_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgsDict(
    TypedDict
):
    interval: pulumi.Input[_builtins.int]
    interval_unit: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleDeprecateRuleArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.int],
        interval_unit: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> pulumi.Input[_builtins.str]: ...
    @interval_unit.setter
    def interval_unit(self, value: pulumi.Input[_builtins.str]): ...

class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgsDict(
    TypedDict
):
    interval: pulumi.Input[_builtins.int]
    interval_unit: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleCrossRegionCopyRuleRetainRuleArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.int],
        interval_unit: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> pulumi.Input[_builtins.str]: ...
    @interval_unit.setter
    def interval_unit(self, value: pulumi.Input[_builtins.str]): ...

class LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleDeprecateRuleArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgsDict(TypedDict):
    availability_zones: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    count: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleFastRestoreRuleArgs:
    def __init__(
        __self__,
        *,
        availability_zones: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleRetainRuleArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    interval_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleRetainRuleArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalUnit")
    def interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval_unit.setter
    def interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailsScheduleShareRuleArgsDict(TypedDict):
    target_accounts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    unshare_interval: NotRequired[pulumi.Input[_builtins.int]]
    unshare_interval_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailsScheduleShareRuleArgs:
    def __init__(
        __self__,
        *,
        target_accounts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        unshare_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        unshare_interval_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetAccounts")
    def target_accounts(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_accounts.setter
    def target_accounts(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="unshareInterval")
    def unshare_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @unshare_interval.setter
    def unshare_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="unshareIntervalUnit")
    def unshare_interval_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unshare_interval_unit.setter
    def unshare_interval_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
