import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppSourceControlResult",
    "AwaitableGetWebAppSourceControlResult",
    "get_web_app_source_control",
    "get_web_app_source_control_output",
]

@pulumi.output_type
class GetWebAppSourceControlResult:
    def __init__(
        __self__,
        azure_api_version=...,
        branch=...,
        deployment_rollback_enabled=...,
        git_hub_action_configuration=...,
        id=...,
        is_git_hub_action=...,
        is_manual_integration=...,
        is_mercurial=...,
        kind=...,
        name=...,
        repo_url=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentRollbackEnabled")
    def deployment_rollback_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gitHubActionConfiguration")
    def git_hub_action_configuration(
        self,
    ) -> Optional[outputs.GitHubActionConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isGitHubAction")
    def is_git_hub_action(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isManualIntegration")
    def is_manual_integration(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isMercurial")
    def is_mercurial(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAppSourceControlResult(GetWebAppSourceControlResult):
    def __await__(self): ...

def get_web_app_source_control(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppSourceControlResult: ...
def get_web_app_source_control_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppSourceControlResult]: ...
