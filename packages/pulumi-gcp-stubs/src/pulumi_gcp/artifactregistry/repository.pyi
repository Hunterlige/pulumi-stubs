

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryArgs', 'Repository']
@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *, format: pulumi.Input[_builtins.str], repository_id: pulumi.Input[_builtins.str], cleanup_policies: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]] = ..., cleanup_policy_dry_run: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_config: Optional[pulumi.Input[RepositoryDockerConfigArgs]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maven_config: Optional[pulumi.Input[RepositoryMavenConfigArgs]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_repository_config: Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]] = ..., virtual_repository_config: Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]] = ..., vulnerability_scanning_config: Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_id.setter
    def repository_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]]:
        
        ...
    
    @cleanup_policies.setter
    def cleanup_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cleanup_policy_dry_run.setter
    def cleanup_policy_dry_run(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerConfig")
    def docker_config(self) -> Optional[pulumi.Input[RepositoryDockerConfigArgs]]:
        
        ...
    
    @docker_config.setter
    def docker_config(self, value: Optional[pulumi.Input[RepositoryDockerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> Optional[pulumi.Input[RepositoryMavenConfigArgs]]:
        
        ...
    
    @maven_config.setter
    def maven_config(self, value: Optional[pulumi.Input[RepositoryMavenConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteRepositoryConfig")
    def remote_repository_config(self) -> Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]]:
        
        ...
    
    @remote_repository_config.setter
    def remote_repository_config(self, value: Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRepositoryConfig")
    def virtual_repository_config(self) -> Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]]:
        
        ...
    
    @virtual_repository_config.setter
    def virtual_repository_config(self, value: Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningConfig")
    def vulnerability_scanning_config(self) -> Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]]:
        
        ...
    
    @vulnerability_scanning_config.setter
    def vulnerability_scanning_config(self, value: Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RepositoryState:
    def __init__(__self__, *, cleanup_policies: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]] = ..., cleanup_policy_dry_run: Optional[pulumi.Input[_builtins.bool]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_config: Optional[pulumi.Input[RepositoryDockerConfigArgs]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., format: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maven_config: Optional[pulumi.Input[RepositoryMavenConfigArgs]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., registry_uri: Optional[pulumi.Input[_builtins.str]] = ..., remote_repository_config: Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., virtual_repository_config: Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]] = ..., vulnerability_scanning_config: Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]]:
        
        ...
    
    @cleanup_policies.setter
    def cleanup_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryCleanupPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cleanup_policy_dry_run.setter
    def cleanup_policy_dry_run(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerConfig")
    def docker_config(self) -> Optional[pulumi.Input[RepositoryDockerConfigArgs]]:
        
        ...
    
    @docker_config.setter
    def docker_config(self, value: Optional[pulumi.Input[RepositoryDockerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> Optional[pulumi.Input[RepositoryMavenConfigArgs]]:
        
        ...
    
    @maven_config.setter
    def maven_config(self, value: Optional[pulumi.Input[RepositoryMavenConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUri")
    def registry_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_uri.setter
    def registry_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteRepositoryConfig")
    def remote_repository_config(self) -> Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]]:
        
        ...
    
    @remote_repository_config.setter
    def remote_repository_config(self, value: Optional[pulumi.Input[RepositoryRemoteRepositoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRepositoryConfig")
    def virtual_repository_config(self) -> Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]]:
        
        ...
    
    @virtual_repository_config.setter
    def virtual_repository_config(self, value: Optional[pulumi.Input[RepositoryVirtualRepositoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningConfig")
    def vulnerability_scanning_config(self) -> Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]]:
        
        ...
    
    @vulnerability_scanning_config.setter
    def vulnerability_scanning_config(self, value: Optional[pulumi.Input[RepositoryVulnerabilityScanningConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:artifactregistry/repository:Repository")
class Repository(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cleanup_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RepositoryCleanupPolicyArgs, RepositoryCleanupPolicyArgsDict]]]]] = ..., cleanup_policy_dry_run: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_config: Optional[pulumi.Input[Union[RepositoryDockerConfigArgs, RepositoryDockerConfigArgsDict]]] = ..., format: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maven_config: Optional[pulumi.Input[Union[RepositoryMavenConfigArgs, RepositoryMavenConfigArgsDict]]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_repository_config: Optional[pulumi.Input[Union[RepositoryRemoteRepositoryConfigArgs, RepositoryRemoteRepositoryConfigArgsDict]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., virtual_repository_config: Optional[pulumi.Input[Union[RepositoryVirtualRepositoryConfigArgs, RepositoryVirtualRepositoryConfigArgsDict]]] = ..., vulnerability_scanning_config: Optional[pulumi.Input[Union[RepositoryVulnerabilityScanningConfigArgs, RepositoryVulnerabilityScanningConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RepositoryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cleanup_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RepositoryCleanupPolicyArgs, RepositoryCleanupPolicyArgsDict]]]]] = ..., cleanup_policy_dry_run: Optional[pulumi.Input[_builtins.bool]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., docker_config: Optional[pulumi.Input[Union[RepositoryDockerConfigArgs, RepositoryDockerConfigArgsDict]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., format: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maven_config: Optional[pulumi.Input[Union[RepositoryMavenConfigArgs, RepositoryMavenConfigArgsDict]]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., registry_uri: Optional[pulumi.Input[_builtins.str]] = ..., remote_repository_config: Optional[pulumi.Input[Union[RepositoryRemoteRepositoryConfigArgs, RepositoryRemoteRepositoryConfigArgsDict]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., virtual_repository_config: Optional[pulumi.Input[Union[RepositoryVirtualRepositoryConfigArgs, RepositoryVirtualRepositoryConfigArgsDict]]] = ..., vulnerability_scanning_config: Optional[pulumi.Input[Union[RepositoryVulnerabilityScanningConfigArgs, RepositoryVulnerabilityScanningConfigArgsDict]]] = ...) -> Repository:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> pulumi.Output[Optional[Sequence[outputs.RepositoryCleanupPolicy]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerConfig")
    def docker_config(self) -> pulumi.Output[Optional[outputs.RepositoryDockerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> pulumi.Output[Optional[outputs.RepositoryMavenConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUri")
    def registry_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteRepositoryConfig")
    def remote_repository_config(self) -> pulumi.Output[Optional[outputs.RepositoryRemoteRepositoryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRepositoryConfig")
    def virtual_repository_config(self) -> pulumi.Output[Optional[outputs.RepositoryVirtualRepositoryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningConfig")
    def vulnerability_scanning_config(self) -> pulumi.Output[outputs.RepositoryVulnerabilityScanningConfig]:
        
        ...
    


