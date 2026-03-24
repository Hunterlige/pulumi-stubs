

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRepositoryResult', 'AwaitableGetRepositoryResult', 'get_repository', 'get_repository_output']
@pulumi.output_type
class GetRepositoryResult:
    
    def __init__(__self__, cleanup_policies=..., cleanup_policy_dry_run=..., create_time=..., description=..., docker_configs=..., effective_labels=..., format=..., id=..., kms_key_name=..., labels=..., location=..., maven_configs=..., mode=..., name=..., project=..., pulumi_labels=..., registry_uri=..., remote_repository_configs=..., repository_id=..., update_time=..., virtual_repository_configs=..., vulnerability_scanning_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicies")
    def cleanup_policies(self) -> Sequence[outputs.GetRepositoryCleanupPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanupPolicyDryRun")
    def cleanup_policy_dry_run(self) -> _builtins.bool:
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
    @pulumi.getter(name="dockerConfigs")
    def docker_configs(self) -> Sequence[outputs.GetRepositoryDockerConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenConfigs")
    def maven_configs(self) -> Sequence[outputs.GetRepositoryMavenConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUri")
    def registry_uri(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteRepositoryConfigs")
    def remote_repository_configs(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualRepositoryConfigs")
    def virtual_repository_configs(self) -> Sequence[outputs.GetRepositoryVirtualRepositoryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityScanningConfigs")
    def vulnerability_scanning_configs(self) -> Sequence[outputs.GetRepositoryVulnerabilityScanningConfigResult]:
        ...
    


class AwaitableGetRepositoryResult(GetRepositoryResult):
    def __await__(self): # -> Generator[Never, Any, GetRepositoryResult]:
        ...
    


def get_repository(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRepositoryResult:
    
    ...

def get_repository_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRepositoryResult]:
    
    ...

