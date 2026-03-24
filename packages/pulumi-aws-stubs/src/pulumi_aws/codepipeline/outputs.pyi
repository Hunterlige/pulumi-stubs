import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomActionTypeConfigurationProperty",
    "CustomActionTypeInputArtifactDetails",
    "CustomActionTypeOutputArtifactDetails",
    "CustomActionTypeSettings",
    "PipelineArtifactStore",
    "PipelineArtifactStoreEncryptionKey",
    "PipelineStage",
    "PipelineStageAction",
    "PipelineStageBeforeEntry",
    "PipelineStageBeforeEntryCondition",
    "PipelineStageBeforeEntryConditionRule",
    "PipelineStageBeforeEntryConditionRuleRuleTypeId",
    "PipelineStageOnFailure",
    "PipelineStageOnFailureCondition",
    "PipelineStageOnFailureConditionRule",
    "PipelineStageOnFailureConditionRuleRuleTypeId",
    "PipelineStageOnFailureRetryConfiguration",
    "PipelineStageOnSuccess",
    "PipelineStageOnSuccessCondition",
    "PipelineStageOnSuccessConditionRule",
    "PipelineStageOnSuccessConditionRuleRuleTypeId",
    "PipelineTrigger",
    "PipelineTriggerAll",
    "PipelineTriggerAllGitConfiguration",
    "PipelineTriggerAllGitConfigurationPullRequest",
    ...,
    ...,
    "PipelineTriggerAllGitConfigurationPush",
    "PipelineTriggerAllGitConfigurationPushBranch",
    "PipelineTriggerAllGitConfigurationPushFilePath",
    "PipelineTriggerAllGitConfigurationPushTag",
    "PipelineTriggerGitConfiguration",
    "PipelineTriggerGitConfigurationPullRequest",
    "PipelineTriggerGitConfigurationPullRequestBranches",
    ...,
    "PipelineTriggerGitConfigurationPush",
    "PipelineTriggerGitConfigurationPushBranches",
    "PipelineTriggerGitConfigurationPushFilePaths",
    "PipelineTriggerGitConfigurationPushTags",
    "PipelineVariable",
    "WebhookAuthenticationConfiguration",
    "WebhookFilter",
]

@pulumi.output_type
class CustomActionTypeConfigurationProperty(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.bool,
        name: _builtins.str,
        required: _builtins.bool,
        secret: _builtins.bool,
        description: Optional[_builtins.str] = ...,
        queryable: Optional[_builtins.bool] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def queryable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomActionTypeInputArtifactDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, maximum_count: _builtins.int, minimum_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> _builtins.int: ...

@pulumi.output_type
class CustomActionTypeOutputArtifactDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, maximum_count: _builtins.int, minimum_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> _builtins.int: ...

@pulumi.output_type
class CustomActionTypeSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_url_template: Optional[_builtins.str] = ...,
        execution_url_template: Optional[_builtins.str] = ...,
        revision_url_template: Optional[_builtins.str] = ...,
        third_party_configuration_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityUrlTemplate")
    def entity_url_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionUrlTemplate")
    def execution_url_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revisionUrlTemplate")
    def revision_url_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyConfigurationUrl")
    def third_party_configuration_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineArtifactStore(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        type: _builtins.str,
        encryption_key: Optional[outputs.PipelineArtifactStoreEncryptionKey] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> Optional[outputs.PipelineArtifactStoreEncryptionKey]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineArtifactStoreEncryptionKey(dict):
    def __init__(__self__, *, id: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineStage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.PipelineStageAction],
        name: _builtins.str,
        before_entry: Optional[outputs.PipelineStageBeforeEntry] = ...,
        on_failure: Optional[outputs.PipelineStageOnFailure] = ...,
        on_success: Optional[outputs.PipelineStageOnSuccess] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.PipelineStageAction]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="beforeEntry")
    def before_entry(self) -> Optional[outputs.PipelineStageBeforeEntry]: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[outputs.PipelineStageOnFailure]: ...
    @_builtins.property
    @pulumi.getter(name="onSuccess")
    def on_success(self) -> Optional[outputs.PipelineStageOnSuccess]: ...

@pulumi.output_type
class PipelineStageAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        category: _builtins.str,
        name: _builtins.str,
        owner: _builtins.str,
        provider: _builtins.str,
        version: _builtins.str,
        configuration: Optional[Mapping[str, _builtins.str]] = ...,
        input_artifacts: Optional[Sequence[_builtins.str]] = ...,
        namespace: Optional[_builtins.str] = ...,
        output_artifacts: Optional[Sequence[_builtins.str]] = ...,
        region: Optional[_builtins.str] = ...,
        role_arn: Optional[_builtins.str] = ...,
        run_order: Optional[_builtins.int] = ...,
        timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputArtifacts")
    def output_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runOrder")
    def run_order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PipelineStageBeforeEntry(dict):
    def __init__(
        __self__, *, condition: outputs.PipelineStageBeforeEntryCondition
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> outputs.PipelineStageBeforeEntryCondition: ...

@pulumi.output_type
class PipelineStageBeforeEntryCondition(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.PipelineStageBeforeEntryConditionRule],
        result: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PipelineStageBeforeEntryConditionRule]: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageBeforeEntryConditionRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        rule_type_id: outputs.PipelineStageBeforeEntryConditionRuleRuleTypeId,
        commands: Optional[Sequence[_builtins.str]] = ...,
        configuration: Optional[Mapping[str, _builtins.str]] = ...,
        input_artifacts: Optional[Sequence[_builtins.str]] = ...,
        region: Optional[_builtins.str] = ...,
        role_arn: Optional[_builtins.str] = ...,
        timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(
        self,
    ) -> outputs.PipelineStageBeforeEntryConditionRuleRuleTypeId: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PipelineStageBeforeEntryConditionRuleRuleTypeId(dict):
    def __init__(
        __self__,
        *,
        category: _builtins.str,
        provider: _builtins.str,
        owner: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageOnFailure(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition: Optional[outputs.PipelineStageOnFailureCondition] = ...,
        result: Optional[_builtins.str] = ...,
        retry_configuration: Optional[
            outputs.PipelineStageOnFailureRetryConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PipelineStageOnFailureCondition]: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retryConfiguration")
    def retry_configuration(
        self,
    ) -> Optional[outputs.PipelineStageOnFailureRetryConfiguration]: ...

@pulumi.output_type
class PipelineStageOnFailureCondition(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.PipelineStageOnFailureConditionRule],
        result: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PipelineStageOnFailureConditionRule]: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageOnFailureConditionRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        rule_type_id: outputs.PipelineStageOnFailureConditionRuleRuleTypeId,
        commands: Optional[Sequence[_builtins.str]] = ...,
        configuration: Optional[Mapping[str, _builtins.str]] = ...,
        input_artifacts: Optional[Sequence[_builtins.str]] = ...,
        region: Optional[_builtins.str] = ...,
        role_arn: Optional[_builtins.str] = ...,
        timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(self) -> outputs.PipelineStageOnFailureConditionRuleRuleTypeId: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PipelineStageOnFailureConditionRuleRuleTypeId(dict):
    def __init__(
        __self__,
        *,
        category: _builtins.str,
        provider: _builtins.str,
        owner: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageOnFailureRetryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, retry_mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retryMode")
    def retry_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageOnSuccess(dict):
    def __init__(
        __self__, *, condition: outputs.PipelineStageOnSuccessCondition
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> outputs.PipelineStageOnSuccessCondition: ...

@pulumi.output_type
class PipelineStageOnSuccessCondition(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.PipelineStageOnSuccessConditionRule],
        result: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PipelineStageOnSuccessConditionRule]: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineStageOnSuccessConditionRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        rule_type_id: outputs.PipelineStageOnSuccessConditionRuleRuleTypeId,
        commands: Optional[Sequence[_builtins.str]] = ...,
        configuration: Optional[Mapping[str, _builtins.str]] = ...,
        input_artifacts: Optional[Sequence[_builtins.str]] = ...,
        region: Optional[_builtins.str] = ...,
        role_arn: Optional[_builtins.str] = ...,
        timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(self) -> outputs.PipelineStageOnSuccessConditionRuleRuleTypeId: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PipelineStageOnSuccessConditionRuleRuleTypeId(dict):
    def __init__(
        __self__,
        *,
        category: _builtins.str,
        provider: _builtins.str,
        owner: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineTrigger(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        git_configuration: outputs.PipelineTriggerGitConfiguration,
        provider_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitConfiguration")
    def git_configuration(self) -> outputs.PipelineTriggerGitConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineTriggerAll(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        git_configurations: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfiguration]
        ] = ...,
        provider_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitConfigurations")
    def git_configurations(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pull_requests: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequest]
        ] = ...,
        pushes: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPush]
        ] = ...,
        source_action_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequest]]: ...
    @_builtins.property
    @pulumi.getter
    def pushes(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfigurationPush]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceActionName")
    def source_action_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPullRequest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branches: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequestBranch]
        ] = ...,
        events: Optional[Sequence[_builtins.str]] = ...,
        file_paths: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequestFilePath]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[
        Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequestBranch]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[
        Sequence[outputs.PipelineTriggerAllGitConfigurationPullRequestFilePath]
    ]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPullRequestBranch(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPullRequestFilePath(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPush(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branches: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPushBranch]
        ] = ...,
        file_paths: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPushFilePath]
        ] = ...,
        tags: Optional[
            Sequence[outputs.PipelineTriggerAllGitConfigurationPushTag]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfigurationPushBranch]]: ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfigurationPushFilePath]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerAllGitConfigurationPushTag]]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPushBranch(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPushFilePath(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerAllGitConfigurationPushTag(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerGitConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_action_name: _builtins.str,
        pull_requests: Optional[
            Sequence[outputs.PipelineTriggerGitConfigurationPullRequest]
        ] = ...,
        pushes: Optional[Sequence[outputs.PipelineTriggerGitConfigurationPush]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceActionName")
    def source_action_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerGitConfigurationPullRequest]]: ...
    @_builtins.property
    @pulumi.getter
    def pushes(
        self,
    ) -> Optional[Sequence[outputs.PipelineTriggerGitConfigurationPush]]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPullRequest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branches: Optional[
            outputs.PipelineTriggerGitConfigurationPullRequestBranches
        ] = ...,
        events: Optional[Sequence[_builtins.str]] = ...,
        file_paths: Optional[
            outputs.PipelineTriggerGitConfigurationPullRequestFilePaths
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[outputs.PipelineTriggerGitConfigurationPullRequestBranches]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[outputs.PipelineTriggerGitConfigurationPullRequestFilePaths]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPullRequestBranches(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPullRequestFilePaths(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPush(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branches: Optional[outputs.PipelineTriggerGitConfigurationPushBranches] = ...,
        file_paths: Optional[
            outputs.PipelineTriggerGitConfigurationPushFilePaths
        ] = ...,
        tags: Optional[outputs.PipelineTriggerGitConfigurationPushTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[outputs.PipelineTriggerGitConfigurationPushBranches]: ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[outputs.PipelineTriggerGitConfigurationPushFilePaths]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.PipelineTriggerGitConfigurationPushTags]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPushBranches(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPushFilePaths(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineTriggerGitConfigurationPushTags(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[Sequence[_builtins.str]] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PipelineVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        default_value: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebhookAuthenticationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_ip_range: Optional[_builtins.str] = ...,
        secret_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIpRange")
    def allowed_ip_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebhookFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, json_path: _builtins.str, match_equals: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchEquals")
    def match_equals(self) -> _builtins.str: ...
