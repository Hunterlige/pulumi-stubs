import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAppSourceControlSlotArgs", "WebAppSourceControlSlot"]

@pulumi.input_type
class WebAppSourceControlSlotArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        slot: pulumi.Input[_builtins.str],
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_rollback_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        git_hub_action_configuration: Optional[
            pulumi.Input[GitHubActionConfigurationArgs]
        ] = ...,
        is_git_hub_action: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_manual_integration: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_mercurial: Optional[pulumi.Input[_builtins.bool]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        repo_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def slot(self) -> pulumi.Input[_builtins.str]: ...
    @slot.setter
    def slot(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentRollbackEnabled")
    def deployment_rollback_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deployment_rollback_enabled.setter
    def deployment_rollback_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gitHubActionConfiguration")
    def git_hub_action_configuration(
        self,
    ) -> Optional[pulumi.Input[GitHubActionConfigurationArgs]]: ...
    @git_hub_action_configuration.setter
    def git_hub_action_configuration(
        self, value: Optional[pulumi.Input[GitHubActionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isGitHubAction")
    def is_git_hub_action(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_git_hub_action.setter
    def is_git_hub_action(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isManualIntegration")
    def is_manual_integration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_manual_integration.setter
    def is_manual_integration(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isMercurial")
    def is_mercurial(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_mercurial.setter
    def is_mercurial(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repo_url.setter
    def repo_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:web:WebAppSourceControlSlot")
class WebAppSourceControlSlot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_rollback_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        git_hub_action_configuration: Optional[
            pulumi.Input[
                Union[GitHubActionConfigurationArgs, GitHubActionConfigurationArgsDict]
            ]
        ] = ...,
        is_git_hub_action: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_manual_integration: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_mercurial: Optional[pulumi.Input[_builtins.bool]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        repo_url: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        slot: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAppSourceControlSlotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebAppSourceControlSlot: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentRollbackEnabled")
    def deployment_rollback_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubActionConfiguration")
    def git_hub_action_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.GitHubActionConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="isGitHubAction")
    def is_git_hub_action(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isManualIntegration")
    def is_manual_integration(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isMercurial")
    def is_mercurial(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
