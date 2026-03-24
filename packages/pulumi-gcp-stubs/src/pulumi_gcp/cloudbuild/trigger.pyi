import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TriggerArgs", "Trigger"]

@pulumi.input_type
class TriggerArgs:
    def __init__(
        __self__,
        *,
        approval_config: Optional[pulumi.Input[TriggerApprovalConfigArgs]] = ...,
        bitbucket_server_trigger_config: Optional[
            pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]
        ] = ...,
        build: Optional[pulumi.Input[TriggerBuildArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_connect_event_config: Optional[
            pulumi.Input[TriggerDeveloperConnectEventConfigArgs]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        git_file_source: Optional[pulumi.Input[TriggerGitFileSourceArgs]] = ...,
        github: Optional[pulumi.Input[TriggerGithubArgs]] = ...,
        ignored_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_build_logs: Optional[pulumi.Input[_builtins.str]] = ...,
        included_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_config: Optional[pulumi.Input[TriggerPubsubConfigArgs]] = ...,
        repository_event_config: Optional[
            pulumi.Input[TriggerRepositoryEventConfigArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_to_build: Optional[pulumi.Input[TriggerSourceToBuildArgs]] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        trigger_template: Optional[pulumi.Input[TriggerTriggerTemplateArgs]] = ...,
        webhook_config: Optional[pulumi.Input[TriggerWebhookConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalConfig")
    def approval_config(self) -> Optional[pulumi.Input[TriggerApprovalConfigArgs]]: ...
    @approval_config.setter
    def approval_config(
        self, value: Optional[pulumi.Input[TriggerApprovalConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerTriggerConfig")
    def bitbucket_server_trigger_config(
        self,
    ) -> Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]]: ...
    @bitbucket_server_trigger_config.setter
    def bitbucket_server_trigger_config(
        self, value: Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input[TriggerBuildArgs]]: ...
    @build.setter
    def build(self, value: Optional[pulumi.Input[TriggerBuildArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="developerConnectEventConfig")
    def developer_connect_event_config(
        self,
    ) -> Optional[pulumi.Input[TriggerDeveloperConnectEventConfigArgs]]: ...
    @developer_connect_event_config.setter
    def developer_connect_event_config(
        self, value: Optional[pulumi.Input[TriggerDeveloperConnectEventConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename.setter
    def filename(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitFileSource")
    def git_file_source(self) -> Optional[pulumi.Input[TriggerGitFileSourceArgs]]: ...
    @git_file_source.setter
    def git_file_source(
        self, value: Optional[pulumi.Input[TriggerGitFileSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def github(self) -> Optional[pulumi.Input[TriggerGithubArgs]]: ...
    @github.setter
    def github(self, value: Optional[pulumi.Input[TriggerGithubArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoredFiles")
    def ignored_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ignored_files.setter
    def ignored_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeBuildLogs")
    def include_build_logs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_build_logs.setter
    def include_build_logs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includedFiles")
    def included_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_files.setter
    def included_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pubsubConfig")
    def pubsub_config(self) -> Optional[pulumi.Input[TriggerPubsubConfigArgs]]: ...
    @pubsub_config.setter
    def pubsub_config(self, value: Optional[pulumi.Input[TriggerPubsubConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryEventConfig")
    def repository_event_config(
        self,
    ) -> Optional[pulumi.Input[TriggerRepositoryEventConfigArgs]]: ...
    @repository_event_config.setter
    def repository_event_config(
        self, value: Optional[pulumi.Input[TriggerRepositoryEventConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceToBuild")
    def source_to_build(self) -> Optional[pulumi.Input[TriggerSourceToBuildArgs]]: ...
    @source_to_build.setter
    def source_to_build(
        self, value: Optional[pulumi.Input[TriggerSourceToBuildArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def substitutions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @substitutions.setter
    def substitutions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerTemplate")
    def trigger_template(
        self,
    ) -> Optional[pulumi.Input[TriggerTriggerTemplateArgs]]: ...
    @trigger_template.setter
    def trigger_template(
        self, value: Optional[pulumi.Input[TriggerTriggerTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookConfig")
    def webhook_config(self) -> Optional[pulumi.Input[TriggerWebhookConfigArgs]]: ...
    @webhook_config.setter
    def webhook_config(
        self, value: Optional[pulumi.Input[TriggerWebhookConfigArgs]]
    ): ...

@pulumi.input_type
class _TriggerState:
    def __init__(
        __self__,
        *,
        approval_config: Optional[pulumi.Input[TriggerApprovalConfigArgs]] = ...,
        bitbucket_server_trigger_config: Optional[
            pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]
        ] = ...,
        build: Optional[pulumi.Input[TriggerBuildArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_connect_event_config: Optional[
            pulumi.Input[TriggerDeveloperConnectEventConfigArgs]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        git_file_source: Optional[pulumi.Input[TriggerGitFileSourceArgs]] = ...,
        github: Optional[pulumi.Input[TriggerGithubArgs]] = ...,
        ignored_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_build_logs: Optional[pulumi.Input[_builtins.str]] = ...,
        included_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_config: Optional[pulumi.Input[TriggerPubsubConfigArgs]] = ...,
        repository_event_config: Optional[
            pulumi.Input[TriggerRepositoryEventConfigArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_to_build: Optional[pulumi.Input[TriggerSourceToBuildArgs]] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_template: Optional[pulumi.Input[TriggerTriggerTemplateArgs]] = ...,
        webhook_config: Optional[pulumi.Input[TriggerWebhookConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalConfig")
    def approval_config(self) -> Optional[pulumi.Input[TriggerApprovalConfigArgs]]: ...
    @approval_config.setter
    def approval_config(
        self, value: Optional[pulumi.Input[TriggerApprovalConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerTriggerConfig")
    def bitbucket_server_trigger_config(
        self,
    ) -> Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]]: ...
    @bitbucket_server_trigger_config.setter
    def bitbucket_server_trigger_config(
        self, value: Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input[TriggerBuildArgs]]: ...
    @build.setter
    def build(self, value: Optional[pulumi.Input[TriggerBuildArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="developerConnectEventConfig")
    def developer_connect_event_config(
        self,
    ) -> Optional[pulumi.Input[TriggerDeveloperConnectEventConfigArgs]]: ...
    @developer_connect_event_config.setter
    def developer_connect_event_config(
        self, value: Optional[pulumi.Input[TriggerDeveloperConnectEventConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename.setter
    def filename(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitFileSource")
    def git_file_source(self) -> Optional[pulumi.Input[TriggerGitFileSourceArgs]]: ...
    @git_file_source.setter
    def git_file_source(
        self, value: Optional[pulumi.Input[TriggerGitFileSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def github(self) -> Optional[pulumi.Input[TriggerGithubArgs]]: ...
    @github.setter
    def github(self, value: Optional[pulumi.Input[TriggerGithubArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoredFiles")
    def ignored_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ignored_files.setter
    def ignored_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeBuildLogs")
    def include_build_logs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_build_logs.setter
    def include_build_logs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includedFiles")
    def included_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_files.setter
    def included_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pubsubConfig")
    def pubsub_config(self) -> Optional[pulumi.Input[TriggerPubsubConfigArgs]]: ...
    @pubsub_config.setter
    def pubsub_config(self, value: Optional[pulumi.Input[TriggerPubsubConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryEventConfig")
    def repository_event_config(
        self,
    ) -> Optional[pulumi.Input[TriggerRepositoryEventConfigArgs]]: ...
    @repository_event_config.setter
    def repository_event_config(
        self, value: Optional[pulumi.Input[TriggerRepositoryEventConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceToBuild")
    def source_to_build(self) -> Optional[pulumi.Input[TriggerSourceToBuildArgs]]: ...
    @source_to_build.setter
    def source_to_build(
        self, value: Optional[pulumi.Input[TriggerSourceToBuildArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def substitutions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @substitutions.setter
    def substitutions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_id.setter
    def trigger_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTemplate")
    def trigger_template(
        self,
    ) -> Optional[pulumi.Input[TriggerTriggerTemplateArgs]]: ...
    @trigger_template.setter
    def trigger_template(
        self, value: Optional[pulumi.Input[TriggerTriggerTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookConfig")
    def webhook_config(self) -> Optional[pulumi.Input[TriggerWebhookConfigArgs]]: ...
    @webhook_config.setter
    def webhook_config(
        self, value: Optional[pulumi.Input[TriggerWebhookConfigArgs]]
    ): ...

@pulumi.type_token("gcp:cloudbuild/trigger:Trigger")
class Trigger(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        approval_config: Optional[
            pulumi.Input[
                Union[TriggerApprovalConfigArgs, TriggerApprovalConfigArgsDict]
            ]
        ] = ...,
        bitbucket_server_trigger_config: Optional[
            pulumi.Input[
                Union[
                    TriggerBitbucketServerTriggerConfigArgs,
                    TriggerBitbucketServerTriggerConfigArgsDict,
                ]
            ]
        ] = ...,
        build: Optional[
            pulumi.Input[Union[TriggerBuildArgs, TriggerBuildArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_connect_event_config: Optional[
            pulumi.Input[
                Union[
                    TriggerDeveloperConnectEventConfigArgs,
                    TriggerDeveloperConnectEventConfigArgsDict,
                ]
            ]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        git_file_source: Optional[
            pulumi.Input[Union[TriggerGitFileSourceArgs, TriggerGitFileSourceArgsDict]]
        ] = ...,
        github: Optional[
            pulumi.Input[Union[TriggerGithubArgs, TriggerGithubArgsDict]]
        ] = ...,
        ignored_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_build_logs: Optional[pulumi.Input[_builtins.str]] = ...,
        included_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_config: Optional[
            pulumi.Input[Union[TriggerPubsubConfigArgs, TriggerPubsubConfigArgsDict]]
        ] = ...,
        repository_event_config: Optional[
            pulumi.Input[
                Union[
                    TriggerRepositoryEventConfigArgs,
                    TriggerRepositoryEventConfigArgsDict,
                ]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_to_build: Optional[
            pulumi.Input[Union[TriggerSourceToBuildArgs, TriggerSourceToBuildArgsDict]]
        ] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        trigger_template: Optional[
            pulumi.Input[
                Union[TriggerTriggerTemplateArgs, TriggerTriggerTemplateArgsDict]
            ]
        ] = ...,
        webhook_config: Optional[
            pulumi.Input[Union[TriggerWebhookConfigArgs, TriggerWebhookConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[TriggerArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        approval_config: Optional[
            pulumi.Input[
                Union[TriggerApprovalConfigArgs, TriggerApprovalConfigArgsDict]
            ]
        ] = ...,
        bitbucket_server_trigger_config: Optional[
            pulumi.Input[
                Union[
                    TriggerBitbucketServerTriggerConfigArgs,
                    TriggerBitbucketServerTriggerConfigArgsDict,
                ]
            ]
        ] = ...,
        build: Optional[
            pulumi.Input[Union[TriggerBuildArgs, TriggerBuildArgsDict]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_connect_event_config: Optional[
            pulumi.Input[
                Union[
                    TriggerDeveloperConnectEventConfigArgs,
                    TriggerDeveloperConnectEventConfigArgsDict,
                ]
            ]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        git_file_source: Optional[
            pulumi.Input[Union[TriggerGitFileSourceArgs, TriggerGitFileSourceArgsDict]]
        ] = ...,
        github: Optional[
            pulumi.Input[Union[TriggerGithubArgs, TriggerGithubArgsDict]]
        ] = ...,
        ignored_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_build_logs: Optional[pulumi.Input[_builtins.str]] = ...,
        included_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_config: Optional[
            pulumi.Input[Union[TriggerPubsubConfigArgs, TriggerPubsubConfigArgsDict]]
        ] = ...,
        repository_event_config: Optional[
            pulumi.Input[
                Union[
                    TriggerRepositoryEventConfigArgs,
                    TriggerRepositoryEventConfigArgsDict,
                ]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_to_build: Optional[
            pulumi.Input[Union[TriggerSourceToBuildArgs, TriggerSourceToBuildArgsDict]]
        ] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_template: Optional[
            pulumi.Input[
                Union[TriggerTriggerTemplateArgs, TriggerTriggerTemplateArgsDict]
            ]
        ] = ...,
        webhook_config: Optional[
            pulumi.Input[Union[TriggerWebhookConfigArgs, TriggerWebhookConfigArgsDict]]
        ] = ...,
    ) -> Trigger: ...
    @_builtins.property
    @pulumi.getter(name="approvalConfig")
    def approval_config(self) -> pulumi.Output[outputs.TriggerApprovalConfig]: ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerTriggerConfig")
    def bitbucket_server_trigger_config(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerBitbucketServerTriggerConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> pulumi.Output[Optional[outputs.TriggerBuild]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="developerConnectEventConfig")
    def developer_connect_event_config(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerDeveloperConnectEventConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gitFileSource")
    def git_file_source(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerGitFileSource]]: ...
    @_builtins.property
    @pulumi.getter
    def github(self) -> pulumi.Output[Optional[outputs.TriggerGithub]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoredFiles")
    def ignored_files(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="includeBuildLogs")
    def include_build_logs(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedFiles")
    def included_files(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pubsubConfig")
    def pubsub_config(self) -> pulumi.Output[Optional[outputs.TriggerPubsubConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEventConfig")
    def repository_event_config(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerRepositoryEventConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceToBuild")
    def source_to_build(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerSourceToBuild]]: ...
    @_builtins.property
    @pulumi.getter
    def substitutions(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerTemplate")
    def trigger_template(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerTriggerTemplate]]: ...
    @_builtins.property
    @pulumi.getter(name="webhookConfig")
    def webhook_config(
        self,
    ) -> pulumi.Output[Optional[outputs.TriggerWebhookConfig]]: ...
