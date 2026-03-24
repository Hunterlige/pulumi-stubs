

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionBuildConfig', 'FunctionBuildConfigAutomaticUpdatePolicy', 'FunctionBuildConfigOnDeployUpdatePolicy', 'FunctionBuildConfigSource', 'FunctionBuildConfigSourceRepoSource', 'FunctionBuildConfigSourceStorageSource', 'FunctionEventTrigger', 'FunctionEventTriggerEventFilter', 'FunctionIamBindingCondition', 'FunctionIamMemberCondition', 'FunctionServiceConfig', 'FunctionServiceConfigDirectVpcNetworkInterface', 'FunctionServiceConfigSecretEnvironmentVariable', 'FunctionServiceConfigSecretVolume', 'FunctionServiceConfigSecretVolumeVersion', 'GetFunctionBuildConfigResult', 'GetFunctionBuildConfigAutomaticUpdatePolicyResult', 'GetFunctionBuildConfigOnDeployUpdatePolicyResult', 'GetFunctionBuildConfigSourceResult', 'GetFunctionBuildConfigSourceRepoSourceResult', 'GetFunctionBuildConfigSourceStorageSourceResult', 'GetFunctionEventTriggerResult', 'GetFunctionEventTriggerEventFilterResult', 'GetFunctionServiceConfigResult', ..., ..., 'GetFunctionServiceConfigSecretVolumeResult', 'GetFunctionServiceConfigSecretVolumeVersionResult']
@pulumi.output_type
class FunctionBuildConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic_update_policy: Optional[outputs.FunctionBuildConfigAutomaticUpdatePolicy] = ..., build: Optional[_builtins.str] = ..., docker_repository: Optional[_builtins.str] = ..., entry_point: Optional[_builtins.str] = ..., environment_variables: Optional[Mapping[str, _builtins.str]] = ..., on_deploy_update_policy: Optional[outputs.FunctionBuildConfigOnDeployUpdatePolicy] = ..., runtime: Optional[_builtins.str] = ..., service_account: Optional[_builtins.str] = ..., source: Optional[outputs.FunctionBuildConfigSource] = ..., worker_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicy")
    def automatic_update_policy(self) -> Optional[outputs.FunctionBuildConfigAutomaticUpdatePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicy")
    def on_deploy_update_policy(self) -> Optional[outputs.FunctionBuildConfigOnDeployUpdatePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.FunctionBuildConfigSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionBuildConfigAutomaticUpdatePolicy(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class FunctionBuildConfigOnDeployUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionBuildConfigSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repo_source: Optional[outputs.FunctionBuildConfigSourceRepoSource] = ..., storage_source: Optional[outputs.FunctionBuildConfigSourceStorageSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSource")
    def repo_source(self) -> Optional[outputs.FunctionBuildConfigSourceRepoSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSource")
    def storage_source(self) -> Optional[outputs.FunctionBuildConfigSourceStorageSource]:
        
        ...
    


@pulumi.output_type
class FunctionBuildConfigSourceRepoSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch_name: Optional[_builtins.str] = ..., commit_sha: Optional[_builtins.str] = ..., dir: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., project_id: Optional[_builtins.str] = ..., repo_name: Optional[_builtins.str] = ..., tag_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionBuildConfigSourceStorageSource(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., generation: Optional[_builtins.int] = ..., object: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionEventTrigger(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_type: _builtins.str, event_filters: Optional[Sequence[outputs.FunctionEventTriggerEventFilter]] = ..., pubsub_topic: Optional[_builtins.str] = ..., retry_policy: Optional[_builtins.str] = ..., service_account_email: Optional[_builtins.str] = ..., trigger: Optional[_builtins.str] = ..., trigger_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(self) -> Optional[Sequence[outputs.FunctionEventTriggerEventFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerRegion")
    def trigger_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionEventTriggerEventFilter(dict):
    def __init__(__self__, *, attribute: _builtins.str, value: _builtins.str, operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class FunctionIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class FunctionServiceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_traffic_on_latest_revision: Optional[_builtins.bool] = ..., available_cpu: Optional[_builtins.str] = ..., available_memory: Optional[_builtins.str] = ..., binary_authorization_policy: Optional[_builtins.str] = ..., direct_vpc_egress: Optional[_builtins.str] = ..., direct_vpc_network_interfaces: Optional[Sequence[outputs.FunctionServiceConfigDirectVpcNetworkInterface]] = ..., environment_variables: Optional[Mapping[str, _builtins.str]] = ..., gcf_uri: Optional[_builtins.str] = ..., ingress_settings: Optional[_builtins.str] = ..., max_instance_count: Optional[_builtins.int] = ..., max_instance_request_concurrency: Optional[_builtins.int] = ..., min_instance_count: Optional[_builtins.int] = ..., secret_environment_variables: Optional[Sequence[outputs.FunctionServiceConfigSecretEnvironmentVariable]] = ..., secret_volumes: Optional[Sequence[outputs.FunctionServiceConfigSecretVolume]] = ..., service: Optional[_builtins.str] = ..., service_account_email: Optional[_builtins.str] = ..., timeout_seconds: Optional[_builtins.int] = ..., uri: Optional[_builtins.str] = ..., vpc_connector: Optional[_builtins.str] = ..., vpc_connector_egress_settings: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allTrafficOnLatestRevision")
    def all_traffic_on_latest_revision(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableCpu")
    def available_cpu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemory")
    def available_memory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationPolicy")
    def binary_authorization_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directVpcEgress")
    def direct_vpc_egress(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directVpcNetworkInterfaces")
    def direct_vpc_network_interfaces(self) -> Optional[Sequence[outputs.FunctionServiceConfigDirectVpcNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcfUri")
    def gcf_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Optional[Sequence[outputs.FunctionServiceConfigSecretEnvironmentVariable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Optional[Sequence[outputs.FunctionServiceConfigSecretVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionServiceConfigDirectVpcNetworkInterface(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class FunctionServiceConfigSecretEnvironmentVariable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, project_id: _builtins.str, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FunctionServiceConfigSecretVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: _builtins.str, project_id: _builtins.str, secret: _builtins.str, versions: Optional[Sequence[outputs.FunctionServiceConfigSecretVolumeVersion]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Sequence[outputs.FunctionServiceConfigSecretVolumeVersion]]:
        
        ...
    


@pulumi.output_type
class FunctionServiceConfigSecretVolumeVersion(dict):
    def __init__(__self__, *, path: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigResult(dict):
    def __init__(__self__, *, automatic_update_policies: Sequence[outputs.GetFunctionBuildConfigAutomaticUpdatePolicyResult], build: _builtins.str, docker_repository: _builtins.str, entry_point: _builtins.str, environment_variables: Mapping[str, _builtins.str], on_deploy_update_policies: Sequence[outputs.GetFunctionBuildConfigOnDeployUpdatePolicyResult], runtime: _builtins.str, service_account: _builtins.str, sources: Sequence[outputs.GetFunctionBuildConfigSourceResult], worker_pool: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicies")
    def automatic_update_policies(self) -> Sequence[outputs.GetFunctionBuildConfigAutomaticUpdatePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def build(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicies")
    def on_deploy_update_policies(self) -> Sequence[outputs.GetFunctionBuildConfigOnDeployUpdatePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetFunctionBuildConfigSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigAutomaticUpdatePolicyResult(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigOnDeployUpdatePolicyResult(dict):
    def __init__(__self__, *, runtime_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigSourceResult(dict):
    def __init__(__self__, *, repo_sources: Sequence[outputs.GetFunctionBuildConfigSourceRepoSourceResult], storage_sources: Sequence[outputs.GetFunctionBuildConfigSourceStorageSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSources")
    def repo_sources(self) -> Sequence[outputs.GetFunctionBuildConfigSourceRepoSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSources")
    def storage_sources(self) -> Sequence[outputs.GetFunctionBuildConfigSourceStorageSourceResult]:
        
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigSourceRepoSourceResult(dict):
    def __init__(__self__, *, branch_name: _builtins.str, commit_sha: _builtins.str, dir: _builtins.str, invert_regex: _builtins.bool, project_id: _builtins.str, repo_name: _builtins.str, tag_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dir(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionBuildConfigSourceStorageSourceResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, generation: _builtins.int, object: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionEventTriggerResult(dict):
    def __init__(__self__, *, event_filters: Sequence[outputs.GetFunctionEventTriggerEventFilterResult], event_type: _builtins.str, pubsub_topic: _builtins.str, retry_policy: _builtins.str, service_account_email: _builtins.str, trigger: _builtins.str, trigger_region: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(self) -> Sequence[outputs.GetFunctionEventTriggerEventFilterResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerRegion")
    def trigger_region(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionEventTriggerEventFilterResult(dict):
    def __init__(__self__, *, attribute: _builtins.str, operator: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionServiceConfigResult(dict):
    def __init__(__self__, *, all_traffic_on_latest_revision: _builtins.bool, available_cpu: _builtins.str, available_memory: _builtins.str, binary_authorization_policy: _builtins.str, direct_vpc_egress: _builtins.str, direct_vpc_network_interfaces: Sequence[outputs.GetFunctionServiceConfigDirectVpcNetworkInterfaceResult], environment_variables: Mapping[str, _builtins.str], gcf_uri: _builtins.str, ingress_settings: _builtins.str, max_instance_count: _builtins.int, max_instance_request_concurrency: _builtins.int, min_instance_count: _builtins.int, secret_environment_variables: Sequence[outputs.GetFunctionServiceConfigSecretEnvironmentVariableResult], secret_volumes: Sequence[outputs.GetFunctionServiceConfigSecretVolumeResult], service: _builtins.str, service_account_email: _builtins.str, timeout_seconds: _builtins.int, uri: _builtins.str, vpc_connector: _builtins.str, vpc_connector_egress_settings: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allTrafficOnLatestRevision")
    def all_traffic_on_latest_revision(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableCpu")
    def available_cpu(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMemory")
    def available_memory(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationPolicy")
    def binary_authorization_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directVpcEgress")
    def direct_vpc_egress(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directVpcNetworkInterfaces")
    def direct_vpc_network_interfaces(self) -> Sequence[outputs.GetFunctionServiceConfigDirectVpcNetworkInterfaceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcfUri")
    def gcf_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Sequence[outputs.GetFunctionServiceConfigSecretEnvironmentVariableResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(self) -> Sequence[outputs.GetFunctionServiceConfigSecretVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionServiceConfigDirectVpcNetworkInterfaceResult(dict):
    def __init__(__self__, *, network: _builtins.str, subnetwork: _builtins.str, tags: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetFunctionServiceConfigSecretEnvironmentVariableResult(dict):
    def __init__(__self__, *, key: _builtins.str, project_id: _builtins.str, secret: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFunctionServiceConfigSecretVolumeResult(dict):
    def __init__(__self__, *, mount_path: _builtins.str, project_id: _builtins.str, secret: _builtins.str, versions: Sequence[outputs.GetFunctionServiceConfigSecretVolumeVersionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[outputs.GetFunctionServiceConfigSecretVolumeVersionResult]:
        
        ...
    


@pulumi.output_type
class GetFunctionServiceConfigSecretVolumeVersionResult(dict):
    def __init__(__self__, *, path: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


