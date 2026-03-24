import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutomationRule",
    "AutomationRuleAdvanceRolloutRule",
    "AutomationRulePromoteReleaseRule",
    "AutomationRuleRepairRolloutRule",
    "AutomationRuleRepairRolloutRuleRepairPhase",
    "AutomationRuleRepairRolloutRuleRepairPhaseRetry",
    "AutomationRuleRepairRolloutRuleRepairPhaseRollback",
    "AutomationRuleTimedPromoteReleaseRule",
    "AutomationSelector",
    "AutomationSelectorTarget",
    "CustomTargetTypeCustomActions",
    "CustomTargetTypeCustomActionsIncludeSkaffoldModule",
    ...,
    ...,
    ...,
    "CustomTargetTypeIamBindingCondition",
    "CustomTargetTypeIamMemberCondition",
    "DeliveryPipelineCondition",
    "DeliveryPipelineConditionPipelineReadyCondition",
    "DeliveryPipelineConditionTargetsPresentCondition",
    "DeliveryPipelineConditionTargetsTypeCondition",
    "DeliveryPipelineIamBindingCondition",
    "DeliveryPipelineIamMemberCondition",
    "DeliveryPipelineSerialPipeline",
    "DeliveryPipelineSerialPipelineStage",
    "DeliveryPipelineSerialPipelineStageDeployParameter",
    "DeliveryPipelineSerialPipelineStageStrategy",
    "DeliveryPipelineSerialPipelineStageStrategyCanary",
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
    "DeployPolicyRule",
    "DeployPolicyRuleRolloutRestriction",
    "DeployPolicyRuleRolloutRestrictionTimeWindows",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DeployPolicySelector",
    "DeployPolicySelectorDeliveryPipeline",
    "DeployPolicySelectorTarget",
    "TargetAnthosCluster",
    "TargetAssociatedEntity",
    "TargetAssociatedEntityAnthosCluster",
    "TargetAssociatedEntityGkeCluster",
    "TargetCustomTarget",
    "TargetExecutionConfig",
    "TargetGke",
    "TargetIamBindingCondition",
    "TargetIamMemberCondition",
    "TargetMultiTarget",
    "TargetRun",
]

@pulumi.output_type
class AutomationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advance_rollout_rule: Optional[outputs.AutomationRuleAdvanceRolloutRule] = ...,
        promote_release_rule: Optional[outputs.AutomationRulePromoteReleaseRule] = ...,
        repair_rollout_rule: Optional[outputs.AutomationRuleRepairRolloutRule] = ...,
        timed_promote_release_rule: Optional[
            outputs.AutomationRuleTimedPromoteReleaseRule
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advanceRolloutRule")
    def advance_rollout_rule(
        self,
    ) -> Optional[outputs.AutomationRuleAdvanceRolloutRule]: ...
    @_builtins.property
    @pulumi.getter(name="promoteReleaseRule")
    def promote_release_rule(
        self,
    ) -> Optional[outputs.AutomationRulePromoteReleaseRule]: ...
    @_builtins.property
    @pulumi.getter(name="repairRolloutRule")
    def repair_rollout_rule(
        self,
    ) -> Optional[outputs.AutomationRuleRepairRolloutRule]: ...
    @_builtins.property
    @pulumi.getter(name="timedPromoteReleaseRule")
    def timed_promote_release_rule(
        self,
    ) -> Optional[outputs.AutomationRuleTimedPromoteReleaseRule]: ...

@pulumi.output_type
class AutomationRuleAdvanceRolloutRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        source_phases: Optional[Sequence[_builtins.str]] = ...,
        wait: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourcePhases")
    def source_phases(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationRulePromoteReleaseRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        destination_phase: Optional[_builtins.str] = ...,
        destination_target_id: Optional[_builtins.str] = ...,
        wait: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationTargetId")
    def destination_target_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationRuleRepairRolloutRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        jobs: Optional[Sequence[_builtins.str]] = ...,
        phases: Optional[Sequence[_builtins.str]] = ...,
        repair_phases: Optional[
            Sequence[outputs.AutomationRuleRepairRolloutRuleRepairPhase]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def phases(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="repairPhases")
    def repair_phases(
        self,
    ) -> Optional[Sequence[outputs.AutomationRuleRepairRolloutRuleRepairPhase]]: ...

@pulumi.output_type
class AutomationRuleRepairRolloutRuleRepairPhase(dict):
    def __init__(
        __self__,
        *,
        retry: Optional[outputs.AutomationRuleRepairRolloutRuleRepairPhaseRetry] = ...,
        rollback: Optional[
            outputs.AutomationRuleRepairRolloutRuleRepairPhaseRollback
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def retry(
        self,
    ) -> Optional[outputs.AutomationRuleRepairRolloutRuleRepairPhaseRetry]: ...
    @_builtins.property
    @pulumi.getter
    def rollback(
        self,
    ) -> Optional[outputs.AutomationRuleRepairRolloutRuleRepairPhaseRollback]: ...

@pulumi.output_type
class AutomationRuleRepairRolloutRuleRepairPhaseRetry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attempts: _builtins.str,
        backoff_mode: Optional[_builtins.str] = ...,
        wait: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backoffMode")
    def backoff_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationRuleRepairRolloutRuleRepairPhaseRollback(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_phase: Optional[_builtins.str] = ...,
        disable_rollback_if_rollout_pending: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableRollbackIfRolloutPending")
    def disable_rollback_if_rollout_pending(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AutomationRuleTimedPromoteReleaseRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        schedule: _builtins.str,
        time_zone: _builtins.str,
        destination_phase: Optional[_builtins.str] = ...,
        destination_target_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationPhase")
    def destination_phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationTargetId")
    def destination_target_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutomationSelector(dict):
    def __init__(
        __self__, *, targets: Sequence[outputs.AutomationSelectorTarget]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Sequence[outputs.AutomationSelectorTarget]: ...

@pulumi.output_type
class AutomationSelectorTarget(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class CustomTargetTypeCustomActions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deploy_action: _builtins.str,
        include_skaffold_modules: Optional[
            Sequence[outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModule]
        ] = ...,
        render_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployAction")
    def deploy_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeSkaffoldModules")
    def include_skaffold_modules(
        self,
    ) -> Optional[
        Sequence[outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModule]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="renderAction")
    def render_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configs: Optional[Sequence[_builtins.str]] = ...,
        git: Optional[
            outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGit
        ] = ...,
        google_cloud_build_repo: Optional[
            outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepo
        ] = ...,
        google_cloud_storage: Optional[
            outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorage
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def git(
        self,
    ) -> Optional[outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGit]: ...
    @_builtins.property
    @pulumi.getter(name="googleCloudBuildRepo")
    def google_cloud_build_repo(
        self,
    ) -> Optional[
        outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepo
    ]: ...
    @_builtins.property
    @pulumi.getter(name="googleCloudStorage")
    def google_cloud_storage(
        self,
    ) -> Optional[
        outputs.CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorage
    ]: ...

@pulumi.output_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGit(dict):
    def __init__(
        __self__,
        *,
        repo: _builtins.str,
        path: Optional[_builtins.str] = ...,
        ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repo(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudBuildRepo(dict):
    def __init__(
        __self__,
        *,
        repository: _builtins.str,
        path: Optional[_builtins.str] = ...,
        ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomTargetTypeCustomActionsIncludeSkaffoldModuleGoogleCloudStorage(dict):
    def __init__(
        __self__, *, source: _builtins.str, path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomTargetTypeIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomTargetTypeIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pipeline_ready_conditions: Optional[
            Sequence[outputs.DeliveryPipelineConditionPipelineReadyCondition]
        ] = ...,
        targets_present_conditions: Optional[
            Sequence[outputs.DeliveryPipelineConditionTargetsPresentCondition]
        ] = ...,
        targets_type_conditions: Optional[
            Sequence[outputs.DeliveryPipelineConditionTargetsTypeCondition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineReadyConditions")
    def pipeline_ready_conditions(
        self,
    ) -> Optional[
        Sequence[outputs.DeliveryPipelineConditionPipelineReadyCondition]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetsPresentConditions")
    def targets_present_conditions(
        self,
    ) -> Optional[
        Sequence[outputs.DeliveryPipelineConditionTargetsPresentCondition]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetsTypeConditions")
    def targets_type_conditions(
        self,
    ) -> Optional[Sequence[outputs.DeliveryPipelineConditionTargetsTypeCondition]]: ...

@pulumi.output_type
class DeliveryPipelineConditionPipelineReadyCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status: Optional[_builtins.bool] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineConditionTargetsPresentCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        missing_targets: Optional[Sequence[_builtins.str]] = ...,
        status: Optional[_builtins.bool] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="missingTargets")
    def missing_targets(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineConditionTargetsTypeCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_details: Optional[_builtins.str] = ...,
        status: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeliveryPipelineIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipeline(dict):
    def __init__(
        __self__,
        *,
        stages: Optional[Sequence[outputs.DeliveryPipelineSerialPipelineStage]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def stages(
        self,
    ) -> Optional[Sequence[outputs.DeliveryPipelineSerialPipelineStage]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deploy_parameters: Optional[
            Sequence[outputs.DeliveryPipelineSerialPipelineStageDeployParameter]
        ] = ...,
        profiles: Optional[Sequence[_builtins.str]] = ...,
        strategy: Optional[outputs.DeliveryPipelineSerialPipelineStageStrategy] = ...,
        target_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployParameters")
    def deploy_parameters(
        self,
    ) -> Optional[
        Sequence[outputs.DeliveryPipelineSerialPipelineStageDeployParameter]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def strategy(
        self,
    ) -> Optional[outputs.DeliveryPipelineSerialPipelineStageStrategy]: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageDeployParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        values: Mapping[str, _builtins.str],
        match_target_labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchTargetLabels")
    def match_target_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategy(dict):
    def __init__(
        __self__,
        *,
        canary: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanary
        ] = ...,
        standard: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyStandard
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def canary(
        self,
    ) -> Optional[outputs.DeliveryPipelineSerialPipelineStageStrategyCanary]: ...
    @_builtins.property
    @pulumi.getter
    def standard(
        self,
    ) -> Optional[outputs.DeliveryPipelineSerialPipelineStageStrategyStandard]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        canary_deployment: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeployment
        ] = ...,
        custom_canary_deployment: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeployment
        ] = ...,
        runtime_config: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canaryDeployment")
    def canary_deployment(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeployment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customCanaryDeployment")
    def custom_canary_deployment(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeployment
    ]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfig
    ]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeployment(dict):
    def __init__(
        __self__,
        *,
        percentages: Sequence[_builtins.int],
        postdeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeploy
        ] = ...,
        predeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeploy
        ] = ...,
        verify: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentages(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPostdeploy(dict):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCanaryDeploymentPredeploy(dict):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeployment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        phase_configs: Sequence[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfig
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phaseConfigs")
    def phase_configs(
        self,
    ) -> Sequence[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfig
    ]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        percentage: _builtins.int,
        phase_id: _builtins.str,
        postdeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeploy
        ] = ...,
        predeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeploy
        ] = ...,
        profiles: Optional[Sequence[_builtins.str]] = ...,
        verify: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="phaseId")
    def phase_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPostdeploy(
    dict
):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryCustomCanaryDeploymentPhaseConfigPredeploy(
    dict
):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_run: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRun
        ] = ...,
        kubernetes: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetes
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRun")
    def cloud_run(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRun
    ]: ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetes
    ]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigCloudRun(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        automatic_traffic_control: Optional[_builtins.bool] = ...,
        canary_revision_tags: Optional[Sequence[_builtins.str]] = ...,
        prior_revision_tags: Optional[Sequence[_builtins.str]] = ...,
        stable_revision_tags: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticTrafficControl")
    def automatic_traffic_control(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="canaryRevisionTags")
    def canary_revision_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="priorRevisionTags")
    def prior_revision_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stableRevisionTags")
    def stable_revision_tags(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gateway_service_mesh: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMesh
        ] = ...,
        service_networking: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworking
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gatewayServiceMesh")
    def gateway_service_mesh(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMesh
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworking")
    def service_networking(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworking
    ]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMesh(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployment: _builtins.str,
        http_route: _builtins.str,
        service: _builtins.str,
        pod_selector_label: Optional[_builtins.str] = ...,
        route_destinations: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinations
        ] = ...,
        route_update_wait_time: Optional[_builtins.str] = ...,
        stable_cutback_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podSelectorLabel")
    def pod_selector_label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeDestinations")
    def route_destinations(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinations
    ]: ...
    @_builtins.property
    @pulumi.getter(name="routeUpdateWaitTime")
    def route_update_wait_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stableCutbackDuration")
    def stable_cutback_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesGatewayServiceMeshRouteDestinations(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_ids: Sequence[_builtins.str],
        propagate_service: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationIds")
    def destination_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagateService")
    def propagate_service(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyCanaryRuntimeConfigKubernetesServiceNetworking(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployment: _builtins.str,
        service: _builtins.str,
        disable_pod_overprovisioning: Optional[_builtins.bool] = ...,
        pod_selector_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disablePodOverprovisioning")
    def disable_pod_overprovisioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="podSelectorLabel")
    def pod_selector_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyStandard(dict):
    def __init__(
        __self__,
        *,
        postdeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyStandardPostdeploy
        ] = ...,
        predeploy: Optional[
            outputs.DeliveryPipelineSerialPipelineStageStrategyStandardPredeploy
        ] = ...,
        verify: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def postdeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyStandardPostdeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def predeploy(
        self,
    ) -> Optional[
        outputs.DeliveryPipelineSerialPipelineStageStrategyStandardPredeploy
    ]: ...
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyStandardPostdeploy(dict):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeliveryPipelineSerialPipelineStageStrategyStandardPredeploy(dict):
    def __init__(
        __self__, *, actions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DeployPolicyRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rollout_restriction: Optional[outputs.DeployPolicyRuleRolloutRestriction] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rolloutRestriction")
    def rollout_restriction(
        self,
    ) -> Optional[outputs.DeployPolicyRuleRolloutRestriction]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestriction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        actions: Optional[Sequence[_builtins.str]] = ...,
        invokers: Optional[Sequence[_builtins.str]] = ...,
        time_windows: Optional[
            outputs.DeployPolicyRuleRolloutRestrictionTimeWindows
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def invokers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeWindows")
    def time_windows(
        self,
    ) -> Optional[outputs.DeployPolicyRuleRolloutRestrictionTimeWindows]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindows(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        time_zone: _builtins.str,
        one_time_windows: Optional[
            Sequence[outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindow]
        ] = ...,
        weekly_windows: Optional[
            Sequence[outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindow]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oneTimeWindows")
    def one_time_windows(
        self,
    ) -> Optional[
        Sequence[outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindow]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyWindows")
    def weekly_windows(
        self,
    ) -> Optional[
        Sequence[outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindow]
    ]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_date: outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDate,
        end_time: outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTime,
        start_date: outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDate,
        start_time: outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(
        self,
    ) -> outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDate: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(
        self,
    ) -> outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTime: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(
        self,
    ) -> (
        outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDate
    ): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> (
        outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTime
    ): ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndDate(dict):
    def __init__(
        __self__,
        *,
        day: Optional[_builtins.int] = ...,
        month: Optional[_builtins.int] = ...,
        year: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowEndTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartDate(dict):
    def __init__(
        __self__,
        *,
        day: Optional[_builtins.int] = ...,
        month: Optional[_builtins.int] = ...,
        year: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsOneTimeWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_weeks: Optional[Sequence[_builtins.str]] = ...,
        end_time: Optional[
            outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTime
        ] = ...,
        start_time: Optional[
            outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTime
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(
        self,
    ) -> Optional[
        outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTime
    ]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> Optional[
        outputs.DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTime
    ]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowEndTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicyRuleRolloutRestrictionTimeWindowsWeeklyWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeployPolicySelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delivery_pipeline: Optional[outputs.DeployPolicySelectorDeliveryPipeline] = ...,
        target: Optional[outputs.DeployPolicySelectorTarget] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryPipeline")
    def delivery_pipeline(
        self,
    ) -> Optional[outputs.DeployPolicySelectorDeliveryPipeline]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.DeployPolicySelectorTarget]: ...

@pulumi.output_type
class DeployPolicySelectorDeliveryPipeline(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class DeployPolicySelectorTarget(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class TargetAnthosCluster(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetAssociatedEntity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_id: _builtins.str,
        anthos_clusters: Optional[
            Sequence[outputs.TargetAssociatedEntityAnthosCluster]
        ] = ...,
        gke_clusters: Optional[
            Sequence[outputs.TargetAssociatedEntityGkeCluster]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="anthosClusters")
    def anthos_clusters(
        self,
    ) -> Optional[Sequence[outputs.TargetAssociatedEntityAnthosCluster]]: ...
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(
        self,
    ) -> Optional[Sequence[outputs.TargetAssociatedEntityGkeCluster]]: ...

@pulumi.output_type
class TargetAssociatedEntityAnthosCluster(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetAssociatedEntityGkeCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        internal_ip: Optional[_builtins.bool] = ...,
        proxy_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetCustomTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, custom_target_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customTargetType")
    def custom_target_type(self) -> _builtins.str: ...

@pulumi.output_type
class TargetExecutionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        usages: Sequence[_builtins.str],
        artifact_storage: Optional[_builtins.str] = ...,
        execution_timeout: Optional[_builtins.str] = ...,
        service_account: Optional[_builtins.str] = ...,
        verbose: Optional[_builtins.bool] = ...,
        worker_pool: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def usages(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactStorage")
    def artifact_storage(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def verbose(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetGke(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        dns_endpoint: Optional[_builtins.bool] = ...,
        internal_ip: Optional[_builtins.bool] = ...,
        proxy_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpoint")
    def dns_endpoint(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetMultiTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, target_ids: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetIds")
    def target_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class TargetRun(dict):
    def __init__(__self__, *, location: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
