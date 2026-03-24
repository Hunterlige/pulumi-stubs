

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTriggerResult', 'AwaitableGetTriggerResult', 'get_trigger', 'get_trigger_output']
@pulumi.output_type
class GetTriggerResult:
    
    def __init__(__self__, approval_configs=..., bitbucket_server_trigger_configs=..., builds=..., create_time=..., description=..., developer_connect_event_configs=..., disabled=..., filename=..., filter=..., git_file_sources=..., githubs=..., id=..., ignored_files=..., include_build_logs=..., included_files=..., location=..., name=..., project=..., pubsub_configs=..., repository_event_configs=..., service_account=..., source_to_builds=..., substitutions=..., tags=..., trigger_id=..., trigger_templates=..., webhook_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalConfigs")
    def approval_configs(self) -> Sequence[outputs.GetTriggerApprovalConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerTriggerConfigs")
    def bitbucket_server_trigger_configs(self) -> Sequence[outputs.GetTriggerBitbucketServerTriggerConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def builds(self) -> Sequence[outputs.GetTriggerBuildResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerConnectEventConfigs")
    def developer_connect_event_configs(self) -> Sequence[outputs.GetTriggerDeveloperConnectEventConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filename(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitFileSources")
    def git_file_sources(self) -> Sequence[outputs.GetTriggerGitFileSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def githubs(self) -> Sequence[outputs.GetTriggerGithubResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoredFiles")
    def ignored_files(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeBuildLogs")
    def include_build_logs(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedFiles")
    def included_files(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Sequence[outputs.GetTriggerPubsubConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryEventConfigs")
    def repository_event_configs(self) -> Sequence[outputs.GetTriggerRepositoryEventConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceToBuilds")
    def source_to_builds(self) -> Sequence[outputs.GetTriggerSourceToBuildResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def substitutions(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerTemplates")
    def trigger_templates(self) -> Sequence[outputs.GetTriggerTriggerTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookConfigs")
    def webhook_configs(self) -> Sequence[outputs.GetTriggerWebhookConfigResult]:
        ...
    


class AwaitableGetTriggerResult(GetTriggerResult):
    def __await__(self): # -> Generator[Never, Any, GetTriggerResult]:
        ...
    


def get_trigger(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., trigger_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTriggerResult:
    
    ...

def get_trigger_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., trigger_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTriggerResult]:
    
    ...

