import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomActionTypeConfigurationPropertyArgs",
    "CustomActionTypeConfigurationPropertyArgsDict",
    "CustomActionTypeInputArtifactDetailsArgs",
    "CustomActionTypeInputArtifactDetailsArgsDict",
    "CustomActionTypeOutputArtifactDetailsArgs",
    "CustomActionTypeOutputArtifactDetailsArgsDict",
    "CustomActionTypeSettingsArgs",
    "CustomActionTypeSettingsArgsDict",
    "PipelineArtifactStoreArgs",
    "PipelineArtifactStoreArgsDict",
    "PipelineArtifactStoreEncryptionKeyArgs",
    "PipelineArtifactStoreEncryptionKeyArgsDict",
    "PipelineStageArgs",
    "PipelineStageArgsDict",
    "PipelineStageActionArgs",
    "PipelineStageActionArgsDict",
    "PipelineStageBeforeEntryArgs",
    "PipelineStageBeforeEntryArgsDict",
    "PipelineStageBeforeEntryConditionArgs",
    "PipelineStageBeforeEntryConditionArgsDict",
    "PipelineStageBeforeEntryConditionRuleArgs",
    "PipelineStageBeforeEntryConditionRuleArgsDict",
    ...,
    ...,
    "PipelineStageOnFailureArgs",
    "PipelineStageOnFailureArgsDict",
    "PipelineStageOnFailureConditionArgs",
    "PipelineStageOnFailureConditionArgsDict",
    "PipelineStageOnFailureConditionRuleArgs",
    "PipelineStageOnFailureConditionRuleArgsDict",
    "PipelineStageOnFailureConditionRuleRuleTypeIdArgs",
    ...,
    "PipelineStageOnFailureRetryConfigurationArgs",
    "PipelineStageOnFailureRetryConfigurationArgsDict",
    "PipelineStageOnSuccessArgs",
    "PipelineStageOnSuccessArgsDict",
    "PipelineStageOnSuccessConditionArgs",
    "PipelineStageOnSuccessConditionArgsDict",
    "PipelineStageOnSuccessConditionRuleArgs",
    "PipelineStageOnSuccessConditionRuleArgsDict",
    "PipelineStageOnSuccessConditionRuleRuleTypeIdArgs",
    ...,
    "PipelineTriggerArgs",
    "PipelineTriggerArgsDict",
    "PipelineTriggerAllArgs",
    "PipelineTriggerAllArgsDict",
    "PipelineTriggerAllGitConfigurationArgs",
    "PipelineTriggerAllGitConfigurationArgsDict",
    "PipelineTriggerAllGitConfigurationPullRequestArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "PipelineTriggerAllGitConfigurationPushArgs",
    "PipelineTriggerAllGitConfigurationPushArgsDict",
    "PipelineTriggerAllGitConfigurationPushBranchArgs",
    ...,
    "PipelineTriggerAllGitConfigurationPushFilePathArgs",
    ...,
    "PipelineTriggerAllGitConfigurationPushTagArgs",
    "PipelineTriggerAllGitConfigurationPushTagArgsDict",
    "PipelineTriggerGitConfigurationArgs",
    "PipelineTriggerGitConfigurationArgsDict",
    "PipelineTriggerGitConfigurationPullRequestArgs",
    "PipelineTriggerGitConfigurationPullRequestArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PipelineTriggerGitConfigurationPushArgs",
    "PipelineTriggerGitConfigurationPushArgsDict",
    "PipelineTriggerGitConfigurationPushBranchesArgs",
    ...,
    "PipelineTriggerGitConfigurationPushFilePathsArgs",
    ...,
    "PipelineTriggerGitConfigurationPushTagsArgs",
    "PipelineTriggerGitConfigurationPushTagsArgsDict",
    "PipelineVariableArgs",
    "PipelineVariableArgsDict",
    "WebhookAuthenticationConfigurationArgs",
    "WebhookAuthenticationConfigurationArgsDict",
    "WebhookFilterArgs",
    "WebhookFilterArgsDict",
]

class CustomActionTypeConfigurationPropertyArgsDict(TypedDict):
    key: pulumi.Input[_builtins.bool]
    name: pulumi.Input[_builtins.str]
    required: pulumi.Input[_builtins.bool]
    secret: pulumi.Input[_builtins.bool]
    description: NotRequired[pulumi.Input[_builtins.str]]
    queryable: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomActionTypeConfigurationPropertyArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.bool],
        name: pulumi.Input[_builtins.str],
        required: pulumi.Input[_builtins.bool],
        secret: pulumi.Input[_builtins.bool],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        queryable: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.bool]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> pulumi.Input[_builtins.bool]: ...
    @required.setter
    def required(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.bool]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def queryable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @queryable.setter
    def queryable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomActionTypeInputArtifactDetailsArgsDict(TypedDict):
    maximum_count: pulumi.Input[_builtins.int]
    minimum_count: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class CustomActionTypeInputArtifactDetailsArgs:
    def __init__(
        __self__,
        *,
        maximum_count: pulumi.Input[_builtins.int],
        minimum_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> pulumi.Input[_builtins.int]: ...
    @maximum_count.setter
    def maximum_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_count.setter
    def minimum_count(self, value: pulumi.Input[_builtins.int]): ...

class CustomActionTypeOutputArtifactDetailsArgsDict(TypedDict):
    maximum_count: pulumi.Input[_builtins.int]
    minimum_count: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class CustomActionTypeOutputArtifactDetailsArgs:
    def __init__(
        __self__,
        *,
        maximum_count: pulumi.Input[_builtins.int],
        minimum_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> pulumi.Input[_builtins.int]: ...
    @maximum_count.setter
    def maximum_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_count.setter
    def minimum_count(self, value: pulumi.Input[_builtins.int]): ...

class CustomActionTypeSettingsArgsDict(TypedDict):
    entity_url_template: NotRequired[pulumi.Input[_builtins.str]]
    execution_url_template: NotRequired[pulumi.Input[_builtins.str]]
    revision_url_template: NotRequired[pulumi.Input[_builtins.str]]
    third_party_configuration_url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomActionTypeSettingsArgs:
    def __init__(
        __self__,
        *,
        entity_url_template: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_url_template: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_url_template: Optional[pulumi.Input[_builtins.str]] = ...,
        third_party_configuration_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityUrlTemplate")
    def entity_url_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_url_template.setter
    def entity_url_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionUrlTemplate")
    def execution_url_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_url_template.setter
    def execution_url_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionUrlTemplate")
    def revision_url_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_url_template.setter
    def revision_url_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyConfigurationUrl")
    def third_party_configuration_url(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @third_party_configuration_url.setter
    def third_party_configuration_url(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PipelineArtifactStoreArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    encryption_key: NotRequired[
        pulumi.Input[PipelineArtifactStoreEncryptionKeyArgsDict]
    ]
    region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineArtifactStoreArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        encryption_key: Optional[
            pulumi.Input[PipelineArtifactStoreEncryptionKeyArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> Optional[pulumi.Input[PipelineArtifactStoreEncryptionKeyArgs]]: ...
    @encryption_key.setter
    def encryption_key(
        self, value: Optional[pulumi.Input[PipelineArtifactStoreEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineArtifactStoreEncryptionKeyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipelineArtifactStoreEncryptionKeyArgs:
    def __init__(
        __self__, *, id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class PipelineStageArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[PipelineStageActionArgsDict]]]
    name: pulumi.Input[_builtins.str]
    before_entry: NotRequired[pulumi.Input[PipelineStageBeforeEntryArgsDict]]
    on_failure: NotRequired[pulumi.Input[PipelineStageOnFailureArgsDict]]
    on_success: NotRequired[pulumi.Input[PipelineStageOnSuccessArgsDict]]
    ...

@pulumi.input_type
class PipelineStageArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[PipelineStageActionArgs]]],
        name: pulumi.Input[_builtins.str],
        before_entry: Optional[pulumi.Input[PipelineStageBeforeEntryArgs]] = ...,
        on_failure: Optional[pulumi.Input[PipelineStageOnFailureArgs]] = ...,
        on_success: Optional[pulumi.Input[PipelineStageOnSuccessArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PipelineStageActionArgs]]]: ...
    @actions.setter
    def actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[PipelineStageActionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="beforeEntry")
    def before_entry(self) -> Optional[pulumi.Input[PipelineStageBeforeEntryArgs]]: ...
    @before_entry.setter
    def before_entry(
        self, value: Optional[pulumi.Input[PipelineStageBeforeEntryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[pulumi.Input[PipelineStageOnFailureArgs]]: ...
    @on_failure.setter
    def on_failure(self, value: Optional[pulumi.Input[PipelineStageOnFailureArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="onSuccess")
    def on_success(self) -> Optional[pulumi.Input[PipelineStageOnSuccessArgs]]: ...
    @on_success.setter
    def on_success(self, value: Optional[pulumi.Input[PipelineStageOnSuccessArgs]]): ...

class PipelineStageActionArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    owner: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    configuration: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input_artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    output_artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    run_order: NotRequired[pulumi.Input[_builtins.int]]
    timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipelineStageActionArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        owner: pulumi.Input[_builtins.str],
        provider: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        input_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        output_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        run_order: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]: ...
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_artifacts.setter
    def input_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputArtifacts")
    def output_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @output_artifacts.setter
    def output_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runOrder")
    def run_order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @run_order.setter
    def run_order(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipelineStageBeforeEntryArgsDict(TypedDict):
    condition: pulumi.Input[PipelineStageBeforeEntryConditionArgsDict]
    ...

@pulumi.input_type
class PipelineStageBeforeEntryArgs:
    def __init__(
        __self__, *, condition: pulumi.Input[PipelineStageBeforeEntryConditionArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[PipelineStageBeforeEntryConditionArgs]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[PipelineStageBeforeEntryConditionArgs]): ...

class PipelineStageBeforeEntryConditionArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[pulumi.Input[PipelineStageBeforeEntryConditionRuleArgsDict]]
    ]
    result: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageBeforeEntryConditionArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageBeforeEntryConditionRuleArgs]]
        ],
        result: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PipelineStageBeforeEntryConditionRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageBeforeEntryConditionRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result.setter
    def result(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageBeforeEntryConditionRuleArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    rule_type_id: pulumi.Input[PipelineStageBeforeEntryConditionRuleRuleTypeIdArgsDict]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    configuration: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input_artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipelineStageBeforeEntryConditionRuleArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        rule_type_id: pulumi.Input[PipelineStageBeforeEntryConditionRuleRuleTypeIdArgs],
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        input_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(
        self,
    ) -> pulumi.Input[PipelineStageBeforeEntryConditionRuleRuleTypeIdArgs]: ...
    @rule_type_id.setter
    def rule_type_id(
        self, value: pulumi.Input[PipelineStageBeforeEntryConditionRuleRuleTypeIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_artifacts.setter
    def input_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipelineStageBeforeEntryConditionRuleRuleTypeIdArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageBeforeEntryConditionRuleRuleTypeIdArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        provider: pulumi.Input[_builtins.str],
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageOnFailureArgsDict(TypedDict):
    condition: NotRequired[pulumi.Input[PipelineStageOnFailureConditionArgsDict]]
    result: NotRequired[pulumi.Input[_builtins.str]]
    retry_configuration: NotRequired[
        pulumi.Input[PipelineStageOnFailureRetryConfigurationArgsDict]
    ]
    ...

@pulumi.input_type
class PipelineStageOnFailureArgs:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[PipelineStageOnFailureConditionArgs]] = ...,
        result: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_configuration: Optional[
            pulumi.Input[PipelineStageOnFailureRetryConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[PipelineStageOnFailureConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[PipelineStageOnFailureConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result.setter
    def result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConfiguration")
    def retry_configuration(
        self,
    ) -> Optional[pulumi.Input[PipelineStageOnFailureRetryConfigurationArgs]]: ...
    @retry_configuration.setter
    def retry_configuration(
        self,
        value: Optional[pulumi.Input[PipelineStageOnFailureRetryConfigurationArgs]],
    ): ...

class PipelineStageOnFailureConditionArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[pulumi.Input[PipelineStageOnFailureConditionRuleArgsDict]]
    ]
    result: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageOnFailureConditionArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageOnFailureConditionRuleArgs]]
        ],
        result: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PipelineStageOnFailureConditionRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageOnFailureConditionRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result.setter
    def result(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageOnFailureConditionRuleArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    rule_type_id: pulumi.Input[PipelineStageOnFailureConditionRuleRuleTypeIdArgsDict]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    configuration: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input_artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipelineStageOnFailureConditionRuleArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        rule_type_id: pulumi.Input[PipelineStageOnFailureConditionRuleRuleTypeIdArgs],
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        input_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(
        self,
    ) -> pulumi.Input[PipelineStageOnFailureConditionRuleRuleTypeIdArgs]: ...
    @rule_type_id.setter
    def rule_type_id(
        self, value: pulumi.Input[PipelineStageOnFailureConditionRuleRuleTypeIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_artifacts.setter
    def input_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipelineStageOnFailureConditionRuleRuleTypeIdArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageOnFailureConditionRuleRuleTypeIdArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        provider: pulumi.Input[_builtins.str],
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageOnFailureRetryConfigurationArgsDict(TypedDict):
    retry_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageOnFailureRetryConfigurationArgs:
    def __init__(
        __self__, *, retry_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retryMode")
    def retry_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retry_mode.setter
    def retry_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageOnSuccessArgsDict(TypedDict):
    condition: pulumi.Input[PipelineStageOnSuccessConditionArgsDict]
    ...

@pulumi.input_type
class PipelineStageOnSuccessArgs:
    def __init__(
        __self__, *, condition: pulumi.Input[PipelineStageOnSuccessConditionArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[PipelineStageOnSuccessConditionArgs]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[PipelineStageOnSuccessConditionArgs]): ...

class PipelineStageOnSuccessConditionArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[pulumi.Input[PipelineStageOnSuccessConditionRuleArgsDict]]
    ]
    result: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageOnSuccessConditionArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageOnSuccessConditionRuleArgs]]
        ],
        result: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PipelineStageOnSuccessConditionRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PipelineStageOnSuccessConditionRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result.setter
    def result(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineStageOnSuccessConditionRuleArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    rule_type_id: pulumi.Input[PipelineStageOnSuccessConditionRuleRuleTypeIdArgsDict]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    configuration: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    input_artifacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PipelineStageOnSuccessConditionRuleArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        rule_type_id: pulumi.Input[PipelineStageOnSuccessConditionRuleRuleTypeIdArgs],
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        input_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleTypeId")
    def rule_type_id(
        self,
    ) -> pulumi.Input[PipelineStageOnSuccessConditionRuleRuleTypeIdArgs]: ...
    @rule_type_id.setter
    def rule_type_id(
        self, value: pulumi.Input[PipelineStageOnSuccessConditionRuleRuleTypeIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_artifacts.setter
    def input_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMinutes")
    def timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipelineStageOnSuccessConditionRuleRuleTypeIdArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineStageOnSuccessConditionRuleRuleTypeIdArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        provider: pulumi.Input[_builtins.str],
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineTriggerArgsDict(TypedDict):
    git_configuration: pulumi.Input[PipelineTriggerGitConfigurationArgsDict]
    provider_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PipelineTriggerArgs:
    def __init__(
        __self__,
        *,
        git_configuration: pulumi.Input[PipelineTriggerGitConfigurationArgs],
        provider_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitConfiguration")
    def git_configuration(
        self,
    ) -> pulumi.Input[PipelineTriggerGitConfigurationArgs]: ...
    @git_configuration.setter
    def git_configuration(
        self, value: pulumi.Input[PipelineTriggerGitConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Input[_builtins.str]: ...
    @provider_type.setter
    def provider_type(self, value: pulumi.Input[_builtins.str]): ...

class PipelineTriggerAllArgsDict(TypedDict):
    git_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationArgsDict]]]
    ]
    provider_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineTriggerAllArgs:
    def __init__(
        __self__,
        *,
        git_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationArgs]]]
        ] = ...,
        provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitConfigurations")
    def git_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationArgs]]]
    ]: ...
    @git_configurations.setter
    def git_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_type.setter
    def provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineTriggerAllGitConfigurationArgsDict(TypedDict):
    pull_requests: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestArgsDict]
            ]
        ]
    ]
    pushes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushArgsDict]]
        ]
    ]
    source_action_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationArgs:
    def __init__(
        __self__,
        *,
        pull_requests: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestArgs]
                ]
            ]
        ] = ...,
        pushes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushArgs]]
            ]
        ] = ...,
        source_action_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestArgs]]
        ]
    ]: ...
    @pull_requests.setter
    def pull_requests(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pushes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushArgs]]]
    ]: ...
    @pushes.setter
    def pushes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceActionName")
    def source_action_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_action_name.setter
    def source_action_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineTriggerAllGitConfigurationPullRequestArgsDict(TypedDict):
    branches: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipelineTriggerAllGitConfigurationPullRequestBranchArgsDict
                ]
            ]
        ]
    ]
    events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_paths: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PipelineTriggerAllGitConfigurationPullRequestFilePathArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPullRequestArgs:
    def __init__(
        __self__,
        *,
        branches: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipelineTriggerAllGitConfigurationPullRequestBranchArgs
                    ]
                ]
            ]
        ] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_paths: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipelineTriggerAllGitConfigurationPullRequestFilePathArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestBranchArgs]
            ]
        ]
    ]: ...
    @branches.setter
    def branches(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipelineTriggerAllGitConfigurationPullRequestBranchArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipelineTriggerAllGitConfigurationPullRequestFilePathArgs]
            ]
        ]
    ]: ...
    @file_paths.setter
    def file_paths(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PipelineTriggerAllGitConfigurationPullRequestFilePathArgs
                    ]
                ]
            ]
        ],
    ): ...

class PipelineTriggerAllGitConfigurationPullRequestBranchArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPullRequestBranchArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerAllGitConfigurationPullRequestFilePathArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPullRequestFilePathArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerAllGitConfigurationPushArgsDict(TypedDict):
    branches: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushBranchArgsDict]]
        ]
    ]
    file_paths: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PipelineTriggerAllGitConfigurationPushFilePathArgsDict]
            ]
        ]
    ]
    tags: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushTagArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPushArgs:
    def __init__(
        __self__,
        *,
        branches: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushBranchArgs]]
            ]
        ] = ...,
        file_paths: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipelineTriggerAllGitConfigurationPushFilePathArgs]
                ]
            ]
        ] = ...,
        tags: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushTagArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushBranchArgs]]
        ]
    ]: ...
    @branches.setter
    def branches(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushBranchArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushFilePathArgs]]
        ]
    ]: ...
    @file_paths.setter
    def file_paths(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PipelineTriggerAllGitConfigurationPushFilePathArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushTagArgs]]
        ]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerAllGitConfigurationPushTagArgs]]
            ]
        ],
    ): ...

class PipelineTriggerAllGitConfigurationPushBranchArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPushBranchArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerAllGitConfigurationPushFilePathArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPushFilePathArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerAllGitConfigurationPushTagArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerAllGitConfigurationPushTagArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerGitConfigurationArgsDict(TypedDict):
    source_action_name: pulumi.Input[_builtins.str]
    pull_requests: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerGitConfigurationPullRequestArgsDict]]
        ]
    ]
    pushes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerGitConfigurationPushArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationArgs:
    def __init__(
        __self__,
        *,
        source_action_name: pulumi.Input[_builtins.str],
        pull_requests: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerGitConfigurationPullRequestArgs]]
            ]
        ] = ...,
        pushes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerGitConfigurationPushArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceActionName")
    def source_action_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_action_name.setter
    def source_action_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineTriggerGitConfigurationPullRequestArgs]]
        ]
    ]: ...
    @pull_requests.setter
    def pull_requests(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerGitConfigurationPullRequestArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def pushes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineTriggerGitConfigurationPushArgs]]]
    ]: ...
    @pushes.setter
    def pushes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineTriggerGitConfigurationPushArgs]]
            ]
        ],
    ): ...

class PipelineTriggerGitConfigurationPullRequestArgsDict(TypedDict):
    branches: NotRequired[
        pulumi.Input[PipelineTriggerGitConfigurationPullRequestBranchesArgsDict]
    ]
    events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_paths: NotRequired[
        pulumi.Input[PipelineTriggerGitConfigurationPullRequestFilePathsArgsDict]
    ]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPullRequestArgs:
    def __init__(
        __self__,
        *,
        branches: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPullRequestBranchesArgs]
        ] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_paths: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPullRequestFilePathsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[
        pulumi.Input[PipelineTriggerGitConfigurationPullRequestBranchesArgs]
    ]: ...
    @branches.setter
    def branches(
        self,
        value: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPullRequestBranchesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[
        pulumi.Input[PipelineTriggerGitConfigurationPullRequestFilePathsArgs]
    ]: ...
    @file_paths.setter
    def file_paths(
        self,
        value: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPullRequestFilePathsArgs]
        ],
    ): ...

class PipelineTriggerGitConfigurationPullRequestBranchesArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPullRequestBranchesArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerGitConfigurationPullRequestFilePathsArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPullRequestFilePathsArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerGitConfigurationPushArgsDict(TypedDict):
    branches: NotRequired[
        pulumi.Input[PipelineTriggerGitConfigurationPushBranchesArgsDict]
    ]
    file_paths: NotRequired[
        pulumi.Input[PipelineTriggerGitConfigurationPushFilePathsArgsDict]
    ]
    tags: NotRequired[pulumi.Input[PipelineTriggerGitConfigurationPushTagsArgsDict]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPushArgs:
    def __init__(
        __self__,
        *,
        branches: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPushBranchesArgs]
        ] = ...,
        file_paths: Optional[
            pulumi.Input[PipelineTriggerGitConfigurationPushFilePathsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[PipelineTriggerGitConfigurationPushTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[pulumi.Input[PipelineTriggerGitConfigurationPushBranchesArgs]]: ...
    @branches.setter
    def branches(
        self,
        value: Optional[pulumi.Input[PipelineTriggerGitConfigurationPushBranchesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filePaths")
    def file_paths(
        self,
    ) -> Optional[pulumi.Input[PipelineTriggerGitConfigurationPushFilePathsArgs]]: ...
    @file_paths.setter
    def file_paths(
        self,
        value: Optional[pulumi.Input[PipelineTriggerGitConfigurationPushFilePathsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[PipelineTriggerGitConfigurationPushTagsArgs]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[PipelineTriggerGitConfigurationPushTagsArgs]]
    ): ...

class PipelineTriggerGitConfigurationPushBranchesArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPushBranchesArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerGitConfigurationPushFilePathsArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPushFilePathsArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineTriggerGitConfigurationPushTagsArgsDict(TypedDict):
    excludes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PipelineTriggerGitConfigurationPushTagsArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excludes.setter
    def excludes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PipelineVariableArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PipelineVariableArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
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

class WebhookAuthenticationConfigurationArgsDict(TypedDict):
    allowed_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    secret_token: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WebhookAuthenticationConfigurationArgs:
    def __init__(
        __self__,
        *,
        allowed_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIpRange")
    def allowed_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allowed_ip_range.setter
    def allowed_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_token.setter
    def secret_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebhookFilterArgsDict(TypedDict):
    json_path: pulumi.Input[_builtins.str]
    match_equals: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class WebhookFilterArgs:
    def __init__(
        __self__,
        *,
        json_path: pulumi.Input[_builtins.str],
        match_equals: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> pulumi.Input[_builtins.str]: ...
    @json_path.setter
    def json_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="matchEquals")
    def match_equals(self) -> pulumi.Input[_builtins.str]: ...
    @match_equals.setter
    def match_equals(self, value: pulumi.Input[_builtins.str]): ...
