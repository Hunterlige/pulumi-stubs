import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutomationRuleArgs",
    "AutomationRuleArgsDict",
    "AutomationRuleAdvanceRolloutRuleArgs",
    "AutomationRuleAdvanceRolloutRuleArgsDict",
    "AutomationRulePromoteReleaseRuleArgs",
    "AutomationRulePromoteReleaseRuleArgsDict",
    "AutomationRuleRepairRolloutRuleArgs",
    "AutomationRuleRepairRolloutRuleArgsDict",
    "AutomationRuleRepairRolloutRuleRepairPhaseArgs",
    "AutomationRuleRepairRolloutRuleRepairPhaseArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AutomationRuleTimedPromoteReleaseRuleArgs",
    "AutomationRuleTimedPromoteReleaseRuleArgsDict",
    "AutomationSelectorArgs",
    "AutomationSelectorArgsDict",
    "AutomationSelectorTargetArgs",
    "AutomationSelectorTargetArgsDict",
    "CustomTargetTypeCustomActionsArgs",
    "CustomTargetTypeCustomActionsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CustomTargetTypeIamBindingConditionArgs",
    "CustomTargetTypeIamBindingConditionArgsDict",
    "CustomTargetTypeIamMemberConditionArgs",
    "CustomTargetTypeIamMemberConditionArgsDict",
    "DeliveryPipelineConditionArgs",
    "DeliveryPipelineConditionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DeliveryPipelineConditionTargetsTypeConditionArgs",
    ...,
    "DeliveryPipelineIamBindingConditionArgs",
    "DeliveryPipelineIamBindingConditionArgsDict",
    "DeliveryPipelineIamMemberConditionArgs",
    "DeliveryPipelineIamMemberConditionArgsDict",
    "DeliveryPipelineSerialPipelineArgs",
    "DeliveryPipelineSerialPipelineArgsDict",
    "DeliveryPipelineSerialPipelineStageArgs",
    "DeliveryPipelineSerialPipelineStageArgsDict",
    ...,
    ...,
    "DeliveryPipelineSerialPipelineStageStrategyArgs",
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
    "DeployPolicyRuleArgs",
    "DeployPolicyRuleArgsDict",
    "DeployPolicyRuleRolloutRestrictionArgs",
    "DeployPolicyRuleRolloutRestrictionArgsDict",
    "DeployPolicyRuleRolloutRestrictionTimeWindowsArgs",
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
    "DeployPolicySelectorArgs",
    "DeployPolicySelectorArgsDict",
    "DeployPolicySelectorDeliveryPipelineArgs",
    "DeployPolicySelectorDeliveryPipelineArgsDict",
    "DeployPolicySelectorTargetArgs",
    "DeployPolicySelectorTargetArgsDict",
    "TargetAnthosClusterArgs",
    "TargetAnthosClusterArgsDict",
    "TargetAssociatedEntityArgs",
    "TargetAssociatedEntityArgsDict",
    "TargetAssociatedEntityAnthosClusterArgs",
    "TargetAssociatedEntityAnthosClusterArgsDict",
    "TargetAssociatedEntityGkeClusterArgs",
    "TargetAssociatedEntityGkeClusterArgsDict",
    "TargetCustomTargetArgs",
    "TargetCustomTargetArgsDict",
    "TargetExecutionConfigArgs",
    "TargetExecutionConfigArgsDict",
    "TargetGkeArgs",
    "TargetGkeArgsDict",
    "TargetIamBindingConditionArgs",
    "TargetIamBindingConditionArgsDict",
    "TargetIamMemberConditionArgs",
    "TargetIamMemberConditionArgsDict",
    "TargetMultiTargetArgs",
    "TargetMultiTargetArgsDict",
    "TargetRunArgs",
    "TargetRunArgsDict",
]

class AutomationRuleArgsDict(TypedDict):
    advance_rollout_rule: NotRequired[
        pulumi.Input[AutomationRuleAdvanceRolloutRuleArgsDict]
    ]
    promote_release_rule: NotRequired[
        pulumi.Input[AutomationRulePromoteReleaseRuleArgsDict]
    ]
    repair_rollout_rule: NotRequired[
        pulumi.Input[AutomationRuleRepairRolloutRuleArgsDict]
    ]
    timed_promote_release_rule: NotRequired[
        pulumi.Input[AutomationRuleTimedPromoteReleaseRuleArgsDict]
    ]

@pulumi.input_type
class AutomationRuleArgs:
    def __init__(
        __self__,
        *,
        advance_rollout_rule: Optional[
            pulumi.Input[AutomationRuleAdvanceRolloutRuleArgs]
        ] = ...,
        promote_release_rule: Optional[
            pulumi.Input[AutomationRulePromoteReleaseRuleArgs]
        ] = ...,
        repair_rollout_rule: Optional[
            pulumi.Input[AutomationRuleRepairRolloutRuleArgs]
        ] = ...,
        timed_promote_release_rule: Optional[
            pulumi.Input[AutomationRuleTimedPromoteReleaseRuleArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advanceRolloutRule")
    def advance_rollout_rule(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleAdvanceRolloutRuleArgs]]: ...
    @advance_rollout_rule.setter
    def advance_rollout_rule(
        self, value: Optional[pulumi.Input[AutomationRuleAdvanceRolloutRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="promoteReleaseRule")
    def promote_release_rule(
        self,
    ) -> Optional[pulumi.Input[AutomationRulePromoteReleaseRuleArgs]]: ...
    @promote_release_rule.setter
    def promote_release_rule(
        self, value: Optional[pulumi.Input[AutomationRulePromoteReleaseRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repairRolloutRule")
    def repair_rollout_rule(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleRepairRolloutRuleArgs]]: ...
    @repair_rollout_rule.setter
    def repair_rollout_rule(
        self, value: Optional[pulumi.Input[AutomationRuleRepairRolloutRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timedPromoteReleaseRule")
    def timed_promote_release_rule(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleTimedPromoteReleaseRuleArgs]]: ...
    @timed_promote_release_rule.setter
    def timed_promote_release_rule(
        self, value: Optional[pulumi.Input[AutomationRuleTimedPromoteReleaseRuleArgs]]
    ): ...

class AutomationRuleAdvanceRolloutRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    source_phases: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleAdvanceRolloutRuleArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        source_phases: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        wait: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePhases")
    def source_phases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_phases.setter
    def source_phases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait.setter
    def wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRulePromoteReleaseRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    destination_phase: NotRequired[pulumi.Input[_builtins.str]]
    destination_target_id: NotRequired[pulumi.Input[_builtins.str]]
    wait: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRulePromoteReleaseRuleArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        destination_phase: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
        wait: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_phase.setter
    def destination_phase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationTargetId")
    def destination_target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_target_id.setter
    def destination_target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait.setter
    def wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleRepairRolloutRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    jobs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    phases: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    repair_phases: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseArgsDict]]
        ]
    ]

@pulumi.input_type
class AutomationRuleRepairRolloutRuleArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        jobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        phases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        repair_phases: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jobs.setter
    def jobs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def phases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @phases.setter
    def phases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repairPhases")
    def repair_phases(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseArgs]]
        ]
    ]: ...
    @repair_phases.setter
    def repair_phases(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseArgs]]
            ]
        ],
    ): ...

class AutomationRuleRepairRolloutRuleRepairPhaseArgsDict(TypedDict):
    retry: NotRequired[
        pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRetryArgsDict]
    ]
    rollback: NotRequired[
        pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgsDict]
    ]

@pulumi.input_type
class AutomationRuleRepairRolloutRuleRepairPhaseArgs:
    def __init__(
        __self__,
        *,
        retry: Optional[
            pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRetryArgs]
        ] = ...,
        rollback: Optional[
            pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def retry(
        self,
    ) -> Optional[
        pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRetryArgs]
    ]: ...
    @retry.setter
    def retry(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRetryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollback(
        self,
    ) -> Optional[
        pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgs]
    ]: ...
    @rollback.setter
    def rollback(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgs]
        ],
    ): ...

class AutomationRuleRepairRolloutRuleRepairPhaseRetryArgsDict(TypedDict):
    attempts: pulumi.Input[_builtins.str]
    backoff_mode: NotRequired[pulumi.Input[_builtins.str]]
    wait: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleRepairRolloutRuleRepairPhaseRetryArgs:
    def __init__(
        __self__,
        *,
        attempts: pulumi.Input[_builtins.str],
        backoff_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        wait: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> pulumi.Input[_builtins.str]: ...
    @attempts.setter
    def attempts(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backoffMode")
    def backoff_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backoff_mode.setter
    def backoff_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait.setter
    def wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgsDict(TypedDict):
    destination_phase: NotRequired[pulumi.Input[_builtins.str]]
    disable_rollback_if_rollout_pending: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AutomationRuleRepairRolloutRuleRepairPhaseRollbackArgs:
    def __init__(
        __self__,
        *,
        destination_phase: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_rollback_if_rollout_pending: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_phase.setter
    def destination_phase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableRollbackIfRolloutPending")
    def disable_rollback_if_rollout_pending(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_rollback_if_rollout_pending.setter
    def disable_rollback_if_rollout_pending(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AutomationRuleTimedPromoteReleaseRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    schedule: pulumi.Input[_builtins.str]
    time_zone: pulumi.Input[_builtins.str]
    destination_phase: NotRequired[pulumi.Input[_builtins.str]]
    destination_target_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleTimedPromoteReleaseRuleArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        schedule: pulumi.Input[_builtins.str],
        time_zone: pulumi.Input[_builtins.str],
        destination_phase: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[_builtins.str]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_phase.setter
    def destination_phase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationTargetId")
    def destination_target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_target_id.setter
    def destination_target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationSelectorArgsDict(TypedDict):
    targets: pulumi.Input[Sequence[pulumi.Input[AutomationSelectorTargetArgsDict]]]

@pulumi.input_type
class AutomationSelectorArgs:
    def __init__(
        __self__,
        *,
        targets: pulumi.Input[Sequence[pulumi.Input[AutomationSelectorTargetArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AutomationSelectorTargetArgs]]]: ...
    @targets.setter
    def targets(
        self, value: pulumi.Input[Sequence[pulumi.Input[AutomationSelectorTargetArgs]]]
    ): ...

class AutomationSelectorTargetArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AutomationSelectorTargetArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class CustomTargetTypeCustomActionsArgsDict(TypedDict):
    deploy_action: pulumi.Input[_builtins.str]
    include_skaffold_modules: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgsDict]
            ]
        ]
    ]
    render_action: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeCustomActionsArgs:
    def __init__(
        __self__,
        *,
        deploy_action: pulumi.Input[_builtins.str],
        include_skaffold_modules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgs]
                ]
            ]
        ] = ...,
        render_action: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployAction")
    def deploy_action(self) -> pulumi.Input[_builtins.str]: ...
    @deploy_action.setter
    def deploy_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeSkaffoldModules")
    def include_skaffold_modules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgs]
            ]
        ]
    ]: ...
    @include_skaffold_modules.setter
    def include_skaffold_modules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="renderAction")
    def render_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @render_action.setter
    def render_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgsDict(TypedDict):
    configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    git: NotRequired[
        pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgsDict]
    ]
    google_cloud_build_repo: NotRequired[
        pulumi.Input[
            CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgsDict
        ]
    ]
    google_cloud_storage: NotRequired[
        pulumi.Input[
            CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgsDict
        ]
    ]

@pulumi.input_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleArgs:
    def __init__(
        __self__,
        *,
        configs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        git: Optional[
            pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgs]
        ] = ...,
        google_cloud_build_repo: Optional[
            pulumi.Input[
                CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgs
            ]
        ] = ...,
        google_cloud_storage: Optional[
            pulumi.Input[
                CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @configs.setter
    def configs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def git(
        self,
    ) -> Optional[
        pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgs]
    ]: ...
    @git.setter
    def git(
        self,
        value: Optional[
            pulumi.Input[CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleCloudBuildRepo")
    def google_cloud_build_repo(
        self,
    ) -> Optional[
        pulumi.Input[
            CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgs
        ]
    ]: ...
    @google_cloud_build_repo.setter
    def google_cloud_build_repo(
        self,
        value: Optional[
            pulumi.Input[
                CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleCloudStorage")
    def google_cloud_storage(
        self,
    ) -> Optional[
        pulumi.Input[
            CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgs
        ]
    ]: ...
    @google_cloud_storage.setter
    def google_cloud_storage(
        self,
        value: Optional[
            pulumi.Input[
                CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgs
            ]
        ],
    ): ...

class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgsDict(TypedDict):
    repo: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGitArgs:
    def __init__(
        __self__,
        *,
        repo: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repo(self) -> pulumi.Input[_builtins.str]: ...
    @repo.setter
    def repo(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgsDict(
    TypedDict
):
    repository: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepoArgs:
    def __init__(
        __self__,
        *,
        repository: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgsDict(
    TypedDict
):
    source: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorageArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomTargetTypeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeIamBindingConditionArgs:
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

class CustomTargetTypeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomTargetTypeIamMemberConditionArgs:
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

class DeliveryPipelineConditionArgsDict(TypedDict):
    pipeline_ready_conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeliveryPipelineConditionPipelineReadyConditionArgsDict]
            ]
        ]
    ]
    targets_present_conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeliveryPipelineConditionTargetsPresentConditionArgsDict]
            ]
        ]
    ]
    targets_type_conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeliveryPipelineConditionTargetsTypeConditionArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class DeliveryPipelineConditionArgs:
    def __init__(
        __self__,
        *,
        pipeline_ready_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionPipelineReadyConditionArgs]
                ]
            ]
        ] = ...,
        targets_present_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionTargetsPresentConditionArgs]
                ]
            ]
        ] = ...,
        targets_type_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionTargetsTypeConditionArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineReadyConditions")
    def pipeline_ready_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[DeliveryPipelineConditionPipelineReadyConditionArgs]]
        ]
    ]: ...
    @pipeline_ready_conditions.setter
    def pipeline_ready_conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionPipelineReadyConditionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetsPresentConditions")
    def targets_present_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[DeliveryPipelineConditionTargetsPresentConditionArgs]]
        ]
    ]: ...
    @targets_present_conditions.setter
    def targets_present_conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionTargetsPresentConditionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetsTypeConditions")
    def targets_type_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[DeliveryPipelineConditionTargetsTypeConditionArgs]]
        ]
    ]: ...
    @targets_type_conditions.setter
    def targets_type_conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineConditionTargetsTypeConditionArgs]
                ]
            ]
        ],
    ): ...

class DeliveryPipelineConditionPipelineReadyConditionArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.bool]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineConditionPipelineReadyConditionArgs:
    def __init__(
        __self__,
        *,
        status: Optional[pulumi.Input[_builtins.bool]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeliveryPipelineConditionTargetsPresentConditionArgsDict(TypedDict):
    missing_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    status: NotRequired[pulumi.Input[_builtins.bool]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineConditionTargetsPresentConditionArgs:
    def __init__(
        __self__,
        *,
        missing_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.bool]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="missingTargets")
    def missing_targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @missing_targets.setter
    def missing_targets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeliveryPipelineConditionTargetsTypeConditionArgsDict(TypedDict):
    error_details: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeliveryPipelineConditionTargetsTypeConditionArgs:
    def __init__(
        __self__,
        *,
        error_details: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_details.setter
    def error_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DeliveryPipelineIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineIamBindingConditionArgs:
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

class DeliveryPipelineIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineIamMemberConditionArgs:
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

class DeliveryPipelineSerialPipelineArgsDict(TypedDict):
    stages: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DeliveryPipelineSerialPipelineStageArgsDict]]
        ]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineArgs:
    def __init__(
        __self__,
        *,
        stages: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeliveryPipelineSerialPipelineStageArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def stages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DeliveryPipelineSerialPipelineStageArgs]]]
    ]: ...
    @stages.setter
    def stages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DeliveryPipelineSerialPipelineStageArgs]]
            ]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageArgsDict(TypedDict):
    deploy_parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeliveryPipelineSerialPipelineStageDeployParameterArgsDict]
            ]
        ]
    ]
    profiles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    strategy: NotRequired[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyArgsDict]
    ]
    target_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageArgs:
    def __init__(
        __self__,
        *,
        deploy_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineSerialPipelineStageDeployParameterArgs]
                ]
            ]
        ] = ...,
        profiles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        strategy: Optional[
            pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyArgs]
        ] = ...,
        target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[DeliveryPipelineSerialPipelineStageDeployParameterArgs]
            ]
        ]
    ]: ...
    @deploy_parameters.setter
    def deploy_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[DeliveryPipelineSerialPipelineStageDeployParameterArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @profiles.setter
    def profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def strategy(
        self,
    ) -> Optional[pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyArgs]]: ...
    @strategy.setter
    def strategy(
        self,
        value: Optional[pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeliveryPipelineSerialPipelineStageDeployParameterArgsDict(TypedDict):
    values: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    match_target_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageDeployParameterArgs:
    def __init__(
        __self__,
        *,
        values: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        match_target_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchTargetLabels")
    def match_target_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @match_target_labels.setter
    def match_target_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyArgsDict(TypedDict):
    canary: NotRequired[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyCanaryArgsDict]
    ]
    standard: NotRequired[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardArgsDict]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyArgs:
    def __init__(
        __self__,
        *,
        canary: Optional[
            pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyCanaryArgs]
        ] = ...,
        standard: Optional[
            pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def canary(
        self,
    ) -> Optional[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyCanaryArgs]
    ]: ...
    @canary.setter
    def canary(
        self,
        value: Optional[
            pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyCanaryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def standard(
        self,
    ) -> Optional[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardArgs]
    ]: ...
    @standard.setter
    def standard(
        self,
        value: Optional[
            pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardArgs]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryArgsDict(TypedDict):
    canary_deployment: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgsDict
        ]
    ]
    custom_canary_deployment: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgsDict
        ]
    ]
    runtime_config: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgsDict
        ]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryArgs:
    def __init__(
        __self__,
        *,
        canary_deployment: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgs
            ]
        ] = ...,
        custom_canary_deployment: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgs
            ]
        ] = ...,
        runtime_config: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canaryDeployment")
    def canary_deployment(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgs
        ]
    ]: ...
    @canary_deployment.setter
    def canary_deployment(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customCanaryDeployment")
    def custom_canary_deployment(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgs
        ]
    ]: ...
    @custom_canary_deployment.setter
    def custom_canary_deployment(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(
        self,
    ) -> Optional[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgs]
    ]: ...
    @runtime_config.setter
    def runtime_config(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgs
            ]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgsDict(
    TypedDict
):
    percentages: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    postdeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgsDict
        ]
    ]
    predeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgsDict
        ]
    ]
    verify: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentArgs:
    def __init__(
        __self__,
        *,
        percentages: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        postdeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgs
            ]
        ] = ...,
        predeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgs
            ]
        ] = ...,
        verify: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentages(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @percentages.setter
    def percentages(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgs
        ]
    ]: ...
    @postdeploy.setter
    def postdeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgs
        ]
    ]: ...
    @predeploy.setter
    def predeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @verify.setter
    def verify(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgsDict(
    TypedDict
):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgsDict(
    TypedDict
):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgsDict(
    TypedDict
):
    phase_configs: pulumi.Input[
        Sequence[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgsDict
            ]
        ]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentArgs:
    def __init__(
        __self__,
        *,
        phase_configs: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phaseConfigs")
    def phase_configs(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgs
            ]
        ]
    ]: ...
    @phase_configs.setter
    def phase_configs(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgs
                ]
            ]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgsDict(
    TypedDict
):
    percentage: pulumi.Input[_builtins.int]
    phase_id: pulumi.Input[_builtins.str]
    postdeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgsDict
        ]
    ]
    predeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgsDict
        ]
    ]
    profiles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    verify: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigArgs:
    def __init__(
        __self__,
        *,
        percentage: pulumi.Input[_builtins.int],
        phase_id: pulumi.Input[_builtins.str],
        postdeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgs
            ]
        ] = ...,
        predeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgs
            ]
        ] = ...,
        profiles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        verify: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> pulumi.Input[_builtins.int]: ...
    @percentage.setter
    def percentage(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="phaseId")
    def phase_id(self) -> pulumi.Input[_builtins.str]: ...
    @phase_id.setter
    def phase_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgs
        ]
    ]: ...
    @postdeploy.setter
    def postdeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgs
        ]
    ]: ...
    @predeploy.setter
    def predeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @profiles.setter
    def profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @verify.setter
    def verify(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgsDict(
    TypedDict
):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgsDict(
    TypedDict
):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgsDict(TypedDict):
    cloud_run: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgsDict
        ]
    ]
    kubernetes: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgsDict
        ]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigArgs:
    def __init__(
        __self__,
        *,
        cloud_run: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgs
            ]
        ] = ...,
        kubernetes: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRun")
    def cloud_run(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgs
        ]
    ]: ...
    @cloud_run.setter
    def cloud_run(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgs
        ]
    ]: ...
    @kubernetes.setter
    def kubernetes(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgs
            ]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgsDict(
    TypedDict
):
    automatic_traffic_control: NotRequired[pulumi.Input[_builtins.bool]]
    canary_revision_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    prior_revision_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    stable_revision_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRunArgs:
    def __init__(
        __self__,
        *,
        automatic_traffic_control: Optional[pulumi.Input[_builtins.bool]] = ...,
        canary_revision_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prior_revision_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        stable_revision_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticTrafficControl")
    def automatic_traffic_control(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automatic_traffic_control.setter
    def automatic_traffic_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canaryRevisionTags")
    def canary_revision_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @canary_revision_tags.setter
    def canary_revision_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="priorRevisionTags")
    def prior_revision_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prior_revision_tags.setter
    def prior_revision_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stableRevisionTags")
    def stable_revision_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stable_revision_tags.setter
    def stable_revision_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgsDict(
    TypedDict
):
    gateway_service_mesh: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgsDict
        ]
    ]
    service_networking: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgsDict
        ]
    ]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesArgs:
    def __init__(
        __self__,
        *,
        gateway_service_mesh: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgs
            ]
        ] = ...,
        service_networking: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayServiceMesh")
    def gateway_service_mesh(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgs
        ]
    ]: ...
    @gateway_service_mesh.setter
    def gateway_service_mesh(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworking")
    def service_networking(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgs
        ]
    ]: ...
    @service_networking.setter
    def service_networking(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgs
            ]
        ],
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgsDict(
    TypedDict
):
    deployment: pulumi.Input[_builtins.str]
    http_route: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    pod_selector_label: NotRequired[pulumi.Input[_builtins.str]]
    route_destinations: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgsDict
        ]
    ]
    route_update_wait_time: NotRequired[pulumi.Input[_builtins.str]]
    stable_cutback_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshArgs:
    def __init__(
        __self__,
        *,
        deployment: pulumi.Input[_builtins.str],
        http_route: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        pod_selector_label: Optional[pulumi.Input[_builtins.str]] = ...,
        route_destinations: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgs
            ]
        ] = ...,
        route_update_wait_time: Optional[pulumi.Input[_builtins.str]] = ...,
        stable_cutback_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Input[_builtins.str]: ...
    @deployment.setter
    def deployment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> pulumi.Input[_builtins.str]: ...
    @http_route.setter
    def http_route(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="podSelectorLabel")
    def pod_selector_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_selector_label.setter
    def pod_selector_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeDestinations")
    def route_destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgs
        ]
    ]: ...
    @route_destinations.setter
    def route_destinations(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeUpdateWaitTime")
    def route_update_wait_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_update_wait_time.setter
    def route_update_wait_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stableCutbackDuration")
    def stable_cutback_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stable_cutback_duration.setter
    def stable_cutback_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgsDict(
    TypedDict
):
    destination_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    propagate_service: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinationsArgs:
    def __init__(
        __self__,
        *,
        destination_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        propagate_service: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationIds")
    def destination_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @destination_ids.setter
    def destination_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="propagateService")
    def propagate_service(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @propagate_service.setter
    def propagate_service(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgsDict(
    TypedDict
):
    deployment: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    disable_pod_overprovisioning: NotRequired[pulumi.Input[_builtins.bool]]
    pod_selector_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworkingArgs:
    def __init__(
        __self__,
        *,
        deployment: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        disable_pod_overprovisioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        pod_selector_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> pulumi.Input[_builtins.str]: ...
    @deployment.setter
    def deployment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disablePodOverprovisioning")
    def disable_pod_overprovisioning(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_pod_overprovisioning.setter
    def disable_pod_overprovisioning(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="podSelectorLabel")
    def pod_selector_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_selector_label.setter
    def pod_selector_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeliveryPipelineSerialPipelineStageStrategyStandardArgsDict(TypedDict):
    postdeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgsDict
        ]
    ]
    predeploy: NotRequired[
        pulumi.Input[
            DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgsDict
        ]
    ]
    verify: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyStandardArgs:
    def __init__(
        __self__,
        *,
        postdeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgs
            ]
        ] = ...,
        predeploy: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgs
            ]
        ] = ...,
        verify: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgs]
    ]: ...
    @postdeploy.setter
    def postdeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        pulumi.Input[DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgs]
    ]: ...
    @predeploy.setter
    def predeploy(
        self,
        value: Optional[
            pulumi.Input[
                DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @verify.setter
    def verify(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyStandardPostdeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeliveryPipelineSerialPipelineStageStrategyStandardPredeployArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DeployPolicyRuleArgsDict(TypedDict):
    rollout_restriction: NotRequired[
        pulumi.Input[DeployPolicyRuleRolloutRestrictionArgsDict]
    ]

@pulumi.input_type
class DeployPolicyRuleArgs:
    def __init__(
        __self__,
        *,
        rollout_restriction: Optional[
            pulumi.Input[DeployPolicyRuleRolloutRestrictionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rolloutRestriction")
    def rollout_restriction(
        self,
    ) -> Optional[pulumi.Input[DeployPolicyRuleRolloutRestrictionArgs]]: ...
    @rollout_restriction.setter
    def rollout_restriction(
        self, value: Optional[pulumi.Input[DeployPolicyRuleRolloutRestrictionArgs]]
    ): ...

class DeployPolicyRuleRolloutRestrictionArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    invokers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    time_windows: NotRequired[
        pulumi.Input[DeployPolicyRuleRolloutRestrictionTimeWindowsArgsDict]
    ]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        invokers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        time_windows: Optional[
            pulumi.Input[DeployPolicyRuleRolloutRestrictionTimeWindowsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def invokers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @invokers.setter
    def invokers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeWindows")
    def time_windows(
        self,
    ) -> Optional[pulumi.Input[DeployPolicyRuleRolloutRestrictionTimeWindowsArgs]]: ...
    @time_windows.setter
    def time_windows(
        self,
        value: Optional[
            pulumi.Input[DeployPolicyRuleRolloutRestrictionTimeWindowsArgs]
        ],
    ): ...

class DeployPolicyRuleRolloutRestrictionTimeWindowsArgsDict(TypedDict):
    time_zone: pulumi.Input[_builtins.str]
    one_time_windows: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgsDict
                ]
            ]
        ]
    ]
    weekly_windows: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsArgs:
    def __init__(
        __self__,
        *,
        time_zone: pulumi.Input[_builtins.str],
        one_time_windows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgs
                    ]
                ]
            ]
        ] = ...,
        weekly_windows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oneTimeWindows")
    def one_time_windows(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgs
                ]
            ]
        ]
    ]: ...
    @one_time_windows.setter
    def one_time_windows(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeklyWindows")
    def weekly_windows(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgs
                ]
            ]
        ]
    ]: ...
    @weekly_windows.setter
    def weekly_windows(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgs
                    ]
                ]
            ]
        ],
    ): ...

class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgsDict(TypedDict):
    end_date: pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgsDict
    ]
    end_time: pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgsDict
    ]
    start_date: pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgsDict
    ]
    start_time: pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgsDict
    ]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowArgs:
    def __init__(
        __self__,
        *,
        end_date: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgs
        ],
        end_time: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgs
        ],
        start_date: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgs
        ],
        start_time: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(
        self,
    ) -> pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgs
    ]: ...
    @end_date.setter
    def end_date(
        self,
        value: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(
        self,
    ) -> pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgs
    ]: ...
    @end_time.setter
    def end_time(
        self,
        value: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(
        self,
    ) -> pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgs
    ]: ...
    @start_date.setter
    def start_date(
        self,
        value: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[
        DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgs
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgs
        ],
    ): ...

class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDateArgs:
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

class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTimeArgs:
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

class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDateArgs:
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

class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTimeArgs:
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

class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgsDict(TypedDict):
    days_of_weeks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    end_time: NotRequired[
        pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgsDict
        ]
    ]
    start_time: NotRequired[
        pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgsDict
        ]
    ]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowArgs:
    def __init__(
        __self__,
        *,
        days_of_weeks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        end_time: Optional[
            pulumi.Input[
                DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgs
            ]
        ] = ...,
        start_time: Optional[
            pulumi.Input[
                DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgs
            ]
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
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(
        self,
    ) -> Optional[
        pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgs
        ]
    ]: ...
    @end_time.setter
    def end_time(
        self,
        value: Optional[
            pulumi.Input[
                DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> Optional[
        pulumi.Input[
            DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgs
        ]
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: Optional[
            pulumi.Input[
                DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgs
            ]
        ],
    ): ...

class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTimeArgs:
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

class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTimeArgs:
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

class DeployPolicySelectorArgsDict(TypedDict):
    delivery_pipeline: NotRequired[
        pulumi.Input[DeployPolicySelectorDeliveryPipelineArgsDict]
    ]
    target: NotRequired[pulumi.Input[DeployPolicySelectorTargetArgsDict]]

@pulumi.input_type
class DeployPolicySelectorArgs:
    def __init__(
        __self__,
        *,
        delivery_pipeline: Optional[
            pulumi.Input[DeployPolicySelectorDeliveryPipelineArgs]
        ] = ...,
        target: Optional[pulumi.Input[DeployPolicySelectorTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPipeline")
    def delivery_pipeline(
        self,
    ) -> Optional[pulumi.Input[DeployPolicySelectorDeliveryPipelineArgs]]: ...
    @delivery_pipeline.setter
    def delivery_pipeline(
        self, value: Optional[pulumi.Input[DeployPolicySelectorDeliveryPipelineArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[DeployPolicySelectorTargetArgs]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[DeployPolicySelectorTargetArgs]]): ...

class DeployPolicySelectorDeliveryPipelineArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeployPolicySelectorDeliveryPipelineArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DeployPolicySelectorTargetArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeployPolicySelectorTargetArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class TargetAnthosClusterArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetAnthosClusterArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetAssociatedEntityArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    anthos_clusters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[TargetAssociatedEntityAnthosClusterArgsDict]]
        ]
    ]
    gke_clusters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityGkeClusterArgsDict]]]
    ]

@pulumi.input_type
class TargetAssociatedEntityArgs:
    def __init__(
        __self__,
        *,
        entity_id: pulumi.Input[_builtins.str],
        anthos_clusters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TargetAssociatedEntityAnthosClusterArgs]]
            ]
        ] = ...,
        gke_clusters: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityGkeClusterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]: ...
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="anthosClusters")
    def anthos_clusters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityAnthosClusterArgs]]]
    ]: ...
    @anthos_clusters.setter
    def anthos_clusters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TargetAssociatedEntityAnthosClusterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityGkeClusterArgs]]]
    ]: ...
    @gke_clusters.setter
    def gke_clusters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TargetAssociatedEntityGkeClusterArgs]]]
        ],
    ): ...

class TargetAssociatedEntityAnthosClusterArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetAssociatedEntityAnthosClusterArgs:
    def __init__(
        __self__, *, membership: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetAssociatedEntityGkeClusterArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    internal_ip: NotRequired[pulumi.Input[_builtins.bool]]
    proxy_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetAssociatedEntityGkeClusterArgs:
    def __init__(
        __self__,
        *,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        internal_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        proxy_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_ip.setter
    def internal_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proxy_url.setter
    def proxy_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetCustomTargetArgsDict(TypedDict):
    custom_target_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TargetCustomTargetArgs:
    def __init__(
        __self__, *, custom_target_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customTargetType")
    def custom_target_type(self) -> pulumi.Input[_builtins.str]: ...
    @custom_target_type.setter
    def custom_target_type(self, value: pulumi.Input[_builtins.str]): ...

class TargetExecutionConfigArgsDict(TypedDict):
    usages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    artifact_storage: NotRequired[pulumi.Input[_builtins.str]]
    execution_timeout: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    verbose: NotRequired[pulumi.Input[_builtins.bool]]
    worker_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetExecutionConfigArgs:
    def __init__(
        __self__,
        *,
        usages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        artifact_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        verbose: Optional[pulumi.Input[_builtins.bool]] = ...,
        worker_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def usages(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @usages.setter
    def usages(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactStorage")
    def artifact_storage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_storage.setter
    def artifact_storage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def verbose(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @verbose.setter
    def verbose(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_pool.setter
    def worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetGkeArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    dns_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    internal_ip: NotRequired[pulumi.Input[_builtins.bool]]
    proxy_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetGkeArgs:
    def __init__(
        __self__,
        *,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        internal_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        proxy_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpoint")
    def dns_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dns_endpoint.setter
    def dns_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_ip.setter
    def internal_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proxy_url.setter
    def proxy_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetIamBindingConditionArgs:
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

class TargetIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetIamMemberConditionArgs:
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

class TargetMultiTargetArgsDict(TypedDict):
    target_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class TargetMultiTargetArgs:
    def __init__(
        __self__, *, target_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_ids.setter
    def target_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class TargetRunArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]

@pulumi.input_type
class TargetRunArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
