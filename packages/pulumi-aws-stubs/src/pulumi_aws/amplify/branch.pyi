

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BranchArgs', 'Branch']
@pulumi.input_type
class BranchArgs:
    def __init__(__self__, *, app_id: pulumi.Input[_builtins.str], branch_name: pulumi.Input[_builtins.str], backend_environment_arn: Optional[pulumi.Input[_builtins.str]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_notification: Optional[pulumi.Input[_builtins.bool]] = ..., enable_performance_mode: Optional[pulumi.Input[_builtins.bool]] = ..., enable_pull_request_preview: Optional[pulumi.Input[_builtins.bool]] = ..., enable_skew_protection: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., framework: Optional[pulumi.Input[_builtins.str]] = ..., pull_request_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stage: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @branch_name.setter
    def branch_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendEnvironmentArn")
    def backend_environment_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backend_environment_arn.setter
    def backend_environment_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_auto_build.setter
    def enable_auto_build(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNotification")
    def enable_notification(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_notification.setter
    def enable_notification(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_performance_mode.setter
    def enable_performance_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_pull_request_preview.setter
    def enable_pull_request_preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSkewProtection")
    def enable_skew_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_skew_protection.setter
    def enable_skew_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @framework.setter
    def framework(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BranchState:
    def __init__(__self__, *, app_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associated_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backend_environment_arn: Optional[pulumi.Input[_builtins.str]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., branch_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_branch: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_notification: Optional[pulumi.Input[_builtins.bool]] = ..., enable_performance_mode: Optional[pulumi.Input[_builtins.bool]] = ..., enable_pull_request_preview: Optional[pulumi.Input[_builtins.bool]] = ..., enable_skew_protection: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., framework: Optional[pulumi.Input[_builtins.str]] = ..., pull_request_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_branch: Optional[pulumi.Input[_builtins.str]] = ..., stage: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResources")
    def associated_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @associated_resources.setter
    def associated_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendEnvironmentArn")
    def backend_environment_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backend_environment_arn.setter
    def backend_environment_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationBranch")
    def destination_branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_branch.setter
    def destination_branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_auto_build.setter
    def enable_auto_build(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNotification")
    def enable_notification(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_notification.setter
    def enable_notification(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_performance_mode.setter
    def enable_performance_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_pull_request_preview.setter
    def enable_pull_request_preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSkewProtection")
    def enable_skew_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_skew_protection.setter
    def enable_skew_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @framework.setter
    def framework(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBranch")
    def source_branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_branch.setter
    def source_branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:amplify/branch:Branch")
class Branch(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., backend_environment_arn: Optional[pulumi.Input[_builtins.str]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., branch_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_notification: Optional[pulumi.Input[_builtins.bool]] = ..., enable_performance_mode: Optional[pulumi.Input[_builtins.bool]] = ..., enable_pull_request_preview: Optional[pulumi.Input[_builtins.bool]] = ..., enable_skew_protection: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., framework: Optional[pulumi.Input[_builtins.str]] = ..., pull_request_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stage: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BranchArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associated_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backend_environment_arn: Optional[pulumi.Input[_builtins.str]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., branch_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_branch: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_notification: Optional[pulumi.Input[_builtins.bool]] = ..., enable_performance_mode: Optional[pulumi.Input[_builtins.bool]] = ..., enable_pull_request_preview: Optional[pulumi.Input[_builtins.bool]] = ..., enable_skew_protection: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., framework: Optional[pulumi.Input[_builtins.str]] = ..., pull_request_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_branch: Optional[pulumi.Input[_builtins.str]] = ..., stage: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> Branch:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResources")
    def associated_resources(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendEnvironmentArn")
    def backend_environment_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationBranch")
    def destination_branch(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNotification")
    def enable_notification(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSkewProtection")
    def enable_skew_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBranch")
    def source_branch(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


