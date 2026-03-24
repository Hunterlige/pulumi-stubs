

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BitbucketServerConfigConnectedRepository', 'BitbucketServerConfigSecrets', 'TriggerApprovalConfig', 'TriggerBitbucketServerTriggerConfig', 'TriggerBitbucketServerTriggerConfigPullRequest', 'TriggerBitbucketServerTriggerConfigPush', 'TriggerBuild', 'TriggerBuildArtifacts', 'TriggerBuildArtifactsMavenArtifact', 'TriggerBuildArtifactsNpmPackage', 'TriggerBuildArtifactsObjects', 'TriggerBuildArtifactsObjectsTiming', 'TriggerBuildArtifactsPythonPackage', 'TriggerBuildAvailableSecrets', 'TriggerBuildAvailableSecretsSecretManager', 'TriggerBuildOptions', 'TriggerBuildOptionsVolume', 'TriggerBuildSecret', 'TriggerBuildSource', 'TriggerBuildSourceRepoSource', 'TriggerBuildSourceStorageSource', 'TriggerBuildStep', 'TriggerBuildStepVolume', 'TriggerDeveloperConnectEventConfig', 'TriggerDeveloperConnectEventConfigPullRequest', 'TriggerDeveloperConnectEventConfigPush', 'TriggerGitFileSource', 'TriggerGithub', 'TriggerGithubPullRequest', 'TriggerGithubPush', 'TriggerPubsubConfig', 'TriggerRepositoryEventConfig', 'TriggerRepositoryEventConfigPullRequest', 'TriggerRepositoryEventConfigPush', 'TriggerSourceToBuild', 'TriggerTriggerTemplate', 'TriggerWebhookConfig', 'WorkerPoolNetworkConfig', 'WorkerPoolPrivateServiceConnect', 'WorkerPoolWorkerConfig', 'GetTriggerApprovalConfigResult', 'GetTriggerBitbucketServerTriggerConfigResult', ..., 'GetTriggerBitbucketServerTriggerConfigPushResult', 'GetTriggerBuildResult', 'GetTriggerBuildArtifactResult', 'GetTriggerBuildArtifactMavenArtifactResult', 'GetTriggerBuildArtifactNpmPackageResult', 'GetTriggerBuildArtifactObjectResult', 'GetTriggerBuildArtifactObjectTimingResult', 'GetTriggerBuildArtifactPythonPackageResult', 'GetTriggerBuildAvailableSecretResult', 'GetTriggerBuildAvailableSecretSecretManagerResult', 'GetTriggerBuildOptionResult', 'GetTriggerBuildOptionVolumeResult', 'GetTriggerBuildSecretResult', 'GetTriggerBuildSourceResult', 'GetTriggerBuildSourceRepoSourceResult', 'GetTriggerBuildSourceStorageSourceResult', 'GetTriggerBuildStepResult', 'GetTriggerBuildStepVolumeResult', 'GetTriggerDeveloperConnectEventConfigResult', ..., 'GetTriggerDeveloperConnectEventConfigPushResult', 'GetTriggerGitFileSourceResult', 'GetTriggerGithubResult', 'GetTriggerGithubPullRequestResult', 'GetTriggerGithubPushResult', 'GetTriggerPubsubConfigResult', 'GetTriggerRepositoryEventConfigResult', 'GetTriggerRepositoryEventConfigPullRequestResult', 'GetTriggerRepositoryEventConfigPushResult', 'GetTriggerSourceToBuildResult', 'GetTriggerTriggerTemplateResult', 'GetTriggerWebhookConfigResult']
@pulumi.output_type
class BitbucketServerConfigConnectedRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_key: _builtins.str, repo_slug: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BitbucketServerConfigSecrets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_access_token_version_name: _builtins.str, read_access_token_version_name: _builtins.str, webhook_secret_version_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminAccessTokenVersionName")
    def admin_access_token_version_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAccessTokenVersionName")
    def read_access_token_version_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretVersionName")
    def webhook_secret_version_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TriggerApprovalConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approval_required: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TriggerBitbucketServerTriggerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bitbucket_server_config_resource: _builtins.str, project_key: _builtins.str, repo_slug: _builtins.str, pull_request: Optional[outputs.TriggerBitbucketServerTriggerConfigPullRequest] = ..., push: Optional[outputs.TriggerBitbucketServerTriggerConfigPush] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfigResource")
    def bitbucket_server_config_resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[outputs.TriggerBitbucketServerTriggerConfigPullRequest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[outputs.TriggerBitbucketServerTriggerConfigPush]:
        
        ...
    


@pulumi.output_type
class TriggerBitbucketServerTriggerConfigPullRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: _builtins.str, comment_control: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TriggerBitbucketServerTriggerConfigPush(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuild(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, steps: Sequence[outputs.TriggerBuildStep], artifacts: Optional[outputs.TriggerBuildArtifacts] = ..., available_secrets: Optional[outputs.TriggerBuildAvailableSecrets] = ..., images: Optional[Sequence[_builtins.str]] = ..., logs_bucket: Optional[_builtins.str] = ..., options: Optional[outputs.TriggerBuildOptions] = ..., queue_ttl: Optional[_builtins.str] = ..., secrets: Optional[Sequence[outputs.TriggerBuildSecret]] = ..., source: Optional[outputs.TriggerBuildSource] = ..., substitutions: Optional[Mapping[str, _builtins.str]] = ..., tags: Optional[Sequence[_builtins.str]] = ..., timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Sequence[outputs.TriggerBuildStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[outputs.TriggerBuildArtifacts]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSecrets")
    def available_secrets(self) -> Optional[outputs.TriggerBuildAvailableSecrets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsBucket")
    def logs_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.TriggerBuildOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueTtl")
    def queue_ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.TriggerBuildSecret]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.TriggerBuildSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def substitutions(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifacts(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, images: Optional[Sequence[_builtins.str]] = ..., maven_artifacts: Optional[Sequence[outputs.TriggerBuildArtifactsMavenArtifact]] = ..., npm_packages: Optional[Sequence[outputs.TriggerBuildArtifactsNpmPackage]] = ..., objects: Optional[outputs.TriggerBuildArtifactsObjects] = ..., python_packages: Optional[Sequence[outputs.TriggerBuildArtifactsPythonPackage]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenArtifacts")
    def maven_artifacts(self) -> Optional[Sequence[outputs.TriggerBuildArtifactsMavenArtifact]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="npmPackages")
    def npm_packages(self) -> Optional[Sequence[outputs.TriggerBuildArtifactsNpmPackage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def objects(self) -> Optional[outputs.TriggerBuildArtifactsObjects]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(self) -> Optional[Sequence[outputs.TriggerBuildArtifactsPythonPackage]]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifactsMavenArtifact(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, artifact_id: Optional[_builtins.str] = ..., group_id: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., repository: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifactsNpmPackage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, package_path: Optional[_builtins.str] = ..., repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifactsObjects(dict):
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., paths: Optional[Sequence[_builtins.str]] = ..., timings: Optional[Sequence[outputs.TriggerBuildArtifactsObjectsTiming]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timings(self) -> Optional[Sequence[outputs.TriggerBuildArtifactsObjectsTiming]]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifactsObjectsTiming(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildArtifactsPythonPackage(dict):
    def __init__(__self__, *, paths: Optional[Sequence[_builtins.str]] = ..., repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildAvailableSecrets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_managers: Sequence[outputs.TriggerBuildAvailableSecretsSecretManager]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagers")
    def secret_managers(self) -> Sequence[outputs.TriggerBuildAvailableSecretsSecretManager]:
        
        ...
    


@pulumi.output_type
class TriggerBuildAvailableSecretsSecretManager(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, env: _builtins.str, version_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TriggerBuildOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: Optional[_builtins.int] = ..., dynamic_substitutions: Optional[_builtins.bool] = ..., envs: Optional[Sequence[_builtins.str]] = ..., log_streaming_option: Optional[_builtins.str] = ..., logging: Optional[_builtins.str] = ..., machine_type: Optional[_builtins.str] = ..., requested_verify_option: Optional[_builtins.str] = ..., secret_envs: Optional[Sequence[_builtins.str]] = ..., source_provenance_hashes: Optional[Sequence[_builtins.str]] = ..., substitution_option: Optional[_builtins.str] = ..., volumes: Optional[Sequence[outputs.TriggerBuildOptionsVolume]] = ..., worker_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicSubstitutions")
    def dynamic_substitutions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamingOption")
    def log_streaming_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedVerifyOption")
    def requested_verify_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProvenanceHashes")
    def source_provenance_hashes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="substitutionOption")
    def substitution_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.TriggerBuildOptionsVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildOptionsVolume(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, secret_env: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnv")
    def secret_env(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class TriggerBuildSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repo_source: Optional[outputs.TriggerBuildSourceRepoSource] = ..., storage_source: Optional[outputs.TriggerBuildSourceStorageSource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSource")
    def repo_source(self) -> Optional[outputs.TriggerBuildSourceRepoSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSource")
    def storage_source(self) -> Optional[outputs.TriggerBuildSourceStorageSource]:
        
        ...
    


@pulumi.output_type
class TriggerBuildSourceRepoSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repo_name: _builtins.str, branch_name: Optional[_builtins.str] = ..., commit_sha: Optional[_builtins.str] = ..., dir: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., project_id: Optional[_builtins.str] = ..., substitutions: Optional[Mapping[str, _builtins.str]] = ..., tag_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> _builtins.str:
        
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
    @pulumi.getter
    def substitutions(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildSourceStorageSource(dict):
    def __init__(__self__, *, bucket: _builtins.str, object: _builtins.str, generation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerBuildStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, allow_exit_codes: Optional[Sequence[_builtins.int]] = ..., allow_failure: Optional[_builtins.bool] = ..., args: Optional[Sequence[_builtins.str]] = ..., dir: Optional[_builtins.str] = ..., entrypoint: Optional[_builtins.str] = ..., envs: Optional[Sequence[_builtins.str]] = ..., id: Optional[_builtins.str] = ..., script: Optional[_builtins.str] = ..., secret_envs: Optional[Sequence[_builtins.str]] = ..., timeout: Optional[_builtins.str] = ..., timing: Optional[_builtins.str] = ..., volumes: Optional[Sequence[outputs.TriggerBuildStepVolume]] = ..., wait_fors: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExitCodes")
    def allow_exit_codes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowFailure")
    def allow_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.TriggerBuildStepVolume]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitFors")
    def wait_fors(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TriggerBuildStepVolume(dict):
    def __init__(__self__, *, name: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TriggerDeveloperConnectEventConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, git_repository_link: _builtins.str, git_repository_link_type: Optional[_builtins.str] = ..., pull_request: Optional[outputs.TriggerDeveloperConnectEventConfigPullRequest] = ..., push: Optional[outputs.TriggerDeveloperConnectEventConfigPush] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLink")
    def git_repository_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLinkType")
    def git_repository_link_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[outputs.TriggerDeveloperConnectEventConfigPullRequest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[outputs.TriggerDeveloperConnectEventConfigPush]:
        
        ...
    


@pulumi.output_type
class TriggerDeveloperConnectEventConfigPullRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., comment_control: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TriggerDeveloperConnectEventConfigPush(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerGitFileSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, repo_type: _builtins.str, bitbucket_server_config: Optional[_builtins.str] = ..., github_enterprise_config: Optional[_builtins.str] = ..., repository: Optional[_builtins.str] = ..., revision: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerGithub(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enterprise_config_resource_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., owner: Optional[_builtins.str] = ..., pull_request: Optional[outputs.TriggerGithubPullRequest] = ..., push: Optional[outputs.TriggerGithubPush] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfigResourceName")
    def enterprise_config_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[outputs.TriggerGithubPullRequest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[outputs.TriggerGithubPush]:
        
        ...
    


@pulumi.output_type
class TriggerGithubPullRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: _builtins.str, comment_control: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TriggerGithubPush(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerPubsubConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, topic: _builtins.str, service_account_email: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., subscription: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerRepositoryEventConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pull_request: Optional[outputs.TriggerRepositoryEventConfigPullRequest] = ..., push: Optional[outputs.TriggerRepositoryEventConfigPush] = ..., repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[outputs.TriggerRepositoryEventConfigPullRequest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[outputs.TriggerRepositoryEventConfigPush]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerRepositoryEventConfigPullRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., comment_control: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TriggerRepositoryEventConfigPush(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., invert_regex: Optional[_builtins.bool] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerSourceToBuild(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ref: _builtins.str, repo_type: _builtins.str, bitbucket_server_config: Optional[_builtins.str] = ..., github_enterprise_config: Optional[_builtins.str] = ..., repository: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TriggerTriggerTemplate(dict):
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
class TriggerWebhookConfig(dict):
    def __init__(__self__, *, secret: _builtins.str, state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, peered_network: _builtins.str, peered_network_ip_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeredNetwork")
    def peered_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeredNetworkIpRange")
    def peered_network_ip_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerPoolPrivateServiceConnect(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_attachment: _builtins.str, route_all_traffic: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeAllTraffic")
    def route_all_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkerPoolWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_size_gb: Optional[_builtins.int] = ..., enable_nested_virtualization: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., no_external_ip: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noExternalIp")
    def no_external_ip(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GetTriggerApprovalConfigResult(dict):
    def __init__(__self__, *, approval_required: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTriggerBitbucketServerTriggerConfigResult(dict):
    def __init__(__self__, *, bitbucket_server_config_resource: _builtins.str, project_key: _builtins.str, pull_requests: Sequence[outputs.GetTriggerBitbucketServerTriggerConfigPullRequestResult], pushes: Sequence[outputs.GetTriggerBitbucketServerTriggerConfigPushResult], repo_slug: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfigResource")
    def bitbucket_server_config_resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(self) -> Sequence[outputs.GetTriggerBitbucketServerTriggerConfigPullRequestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pushes(self) -> Sequence[outputs.GetTriggerBitbucketServerTriggerConfigPushResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBitbucketServerTriggerConfigPullRequestResult(dict):
    def __init__(__self__, *, branch: _builtins.str, comment_control: _builtins.str, invert_regex: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTriggerBitbucketServerTriggerConfigPushResult(dict):
    def __init__(__self__, *, branch: _builtins.str, invert_regex: _builtins.bool, tag: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildResult(dict):
    def __init__(__self__, *, artifacts: Sequence[outputs.GetTriggerBuildArtifactResult], available_secrets: Sequence[outputs.GetTriggerBuildAvailableSecretResult], images: Sequence[_builtins.str], logs_bucket: _builtins.str, options: Sequence[outputs.GetTriggerBuildOptionResult], queue_ttl: _builtins.str, secrets: Sequence[outputs.GetTriggerBuildSecretResult], sources: Sequence[outputs.GetTriggerBuildSourceResult], steps: Sequence[outputs.GetTriggerBuildStepResult], substitutions: Mapping[str, _builtins.str], tags: Sequence[_builtins.str], timeout: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Sequence[outputs.GetTriggerBuildArtifactResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSecrets")
    def available_secrets(self) -> Sequence[outputs.GetTriggerBuildAvailableSecretResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsBucket")
    def logs_bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Sequence[outputs.GetTriggerBuildOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueTtl")
    def queue_ttl(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetTriggerBuildSecretResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetTriggerBuildSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Sequence[outputs.GetTriggerBuildStepResult]:
        
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
    @pulumi.getter
    def timeout(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactResult(dict):
    def __init__(__self__, *, images: Sequence[_builtins.str], maven_artifacts: Sequence[outputs.GetTriggerBuildArtifactMavenArtifactResult], npm_packages: Sequence[outputs.GetTriggerBuildArtifactNpmPackageResult], objects: Sequence[outputs.GetTriggerBuildArtifactObjectResult], python_packages: Sequence[outputs.GetTriggerBuildArtifactPythonPackageResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenArtifacts")
    def maven_artifacts(self) -> Sequence[outputs.GetTriggerBuildArtifactMavenArtifactResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="npmPackages")
    def npm_packages(self) -> Sequence[outputs.GetTriggerBuildArtifactNpmPackageResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def objects(self) -> Sequence[outputs.GetTriggerBuildArtifactObjectResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(self) -> Sequence[outputs.GetTriggerBuildArtifactPythonPackageResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactMavenArtifactResult(dict):
    def __init__(__self__, *, artifact_id: _builtins.str, group_id: _builtins.str, path: _builtins.str, repository: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactNpmPackageResult(dict):
    def __init__(__self__, *, package_path: _builtins.str, repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactObjectResult(dict):
    def __init__(__self__, *, location: _builtins.str, paths: Sequence[_builtins.str], timings: Sequence[outputs.GetTriggerBuildArtifactObjectTimingResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timings(self) -> Sequence[outputs.GetTriggerBuildArtifactObjectTimingResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactObjectTimingResult(dict):
    def __init__(__self__, *, end_time: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildArtifactPythonPackageResult(dict):
    def __init__(__self__, *, paths: Sequence[_builtins.str], repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildAvailableSecretResult(dict):
    def __init__(__self__, *, secret_managers: Sequence[outputs.GetTriggerBuildAvailableSecretSecretManagerResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagers")
    def secret_managers(self) -> Sequence[outputs.GetTriggerBuildAvailableSecretSecretManagerResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildAvailableSecretSecretManagerResult(dict):
    def __init__(__self__, *, env: _builtins.str, version_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildOptionResult(dict):
    def __init__(__self__, *, disk_size_gb: _builtins.int, dynamic_substitutions: _builtins.bool, envs: Sequence[_builtins.str], log_streaming_option: _builtins.str, logging: _builtins.str, machine_type: _builtins.str, requested_verify_option: _builtins.str, secret_envs: Sequence[_builtins.str], source_provenance_hashes: Sequence[_builtins.str], substitution_option: _builtins.str, volumes: Sequence[outputs.GetTriggerBuildOptionVolumeResult], worker_pool: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicSubstitutions")
    def dynamic_substitutions(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamingOption")
    def log_streaming_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedVerifyOption")
    def requested_verify_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProvenanceHashes")
    def source_provenance_hashes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="substitutionOption")
    def substitution_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetTriggerBuildOptionVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildOptionVolumeResult(dict):
    def __init__(__self__, *, name: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildSecretResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str, secret_env: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnv")
    def secret_env(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildSourceResult(dict):
    def __init__(__self__, *, repo_sources: Sequence[outputs.GetTriggerBuildSourceRepoSourceResult], storage_sources: Sequence[outputs.GetTriggerBuildSourceStorageSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoSources")
    def repo_sources(self) -> Sequence[outputs.GetTriggerBuildSourceRepoSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSources")
    def storage_sources(self) -> Sequence[outputs.GetTriggerBuildSourceStorageSourceResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildSourceRepoSourceResult(dict):
    def __init__(__self__, *, branch_name: _builtins.str, commit_sha: _builtins.str, dir: _builtins.str, invert_regex: _builtins.bool, project_id: _builtins.str, repo_name: _builtins.str, substitutions: Mapping[str, _builtins.str], tag_name: _builtins.str) -> None:
        
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
    @pulumi.getter
    def substitutions(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildSourceStorageSourceResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, generation: _builtins.str, object: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildStepResult(dict):
    def __init__(__self__, *, allow_exit_codes: Sequence[_builtins.int], allow_failure: _builtins.bool, args: Sequence[_builtins.str], dir: _builtins.str, entrypoint: _builtins.str, envs: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, script: _builtins.str, secret_envs: Sequence[_builtins.str], timeout: _builtins.str, timing: _builtins.str, volumes: Sequence[outputs.GetTriggerBuildStepVolumeResult], wait_fors: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExitCodes")
    def allow_exit_codes(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowFailure")
    def allow_failure(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dir(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timing(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetTriggerBuildStepVolumeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitFors")
    def wait_fors(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTriggerBuildStepVolumeResult(dict):
    def __init__(__self__, *, name: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerDeveloperConnectEventConfigResult(dict):
    def __init__(__self__, *, git_repository_link: _builtins.str, git_repository_link_type: _builtins.str, pull_requests: Sequence[outputs.GetTriggerDeveloperConnectEventConfigPullRequestResult], pushes: Sequence[outputs.GetTriggerDeveloperConnectEventConfigPushResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLink")
    def git_repository_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLinkType")
    def git_repository_link_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(self) -> Sequence[outputs.GetTriggerDeveloperConnectEventConfigPullRequestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pushes(self) -> Sequence[outputs.GetTriggerDeveloperConnectEventConfigPushResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerDeveloperConnectEventConfigPullRequestResult(dict):
    def __init__(__self__, *, branch: _builtins.str, comment_control: _builtins.str, invert_regex: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTriggerDeveloperConnectEventConfigPushResult(dict):
    def __init__(__self__, *, branch: _builtins.str, invert_regex: _builtins.bool, tag: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerGitFileSourceResult(dict):
    def __init__(__self__, *, bitbucket_server_config: _builtins.str, github_enterprise_config: _builtins.str, path: _builtins.str, repo_type: _builtins.str, repository: _builtins.str, revision: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerGithubResult(dict):
    def __init__(__self__, *, enterprise_config_resource_name: _builtins.str, name: _builtins.str, owner: _builtins.str, pull_requests: Sequence[outputs.GetTriggerGithubPullRequestResult], pushes: Sequence[outputs.GetTriggerGithubPushResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfigResourceName")
    def enterprise_config_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(self) -> Sequence[outputs.GetTriggerGithubPullRequestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pushes(self) -> Sequence[outputs.GetTriggerGithubPushResult]:
        
        ...
    


@pulumi.output_type
class GetTriggerGithubPullRequestResult(dict):
    def __init__(__self__, *, branch: _builtins.str, comment_control: _builtins.str, invert_regex: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTriggerGithubPushResult(dict):
    def __init__(__self__, *, branch: _builtins.str, invert_regex: _builtins.bool, tag: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerPubsubConfigResult(dict):
    def __init__(__self__, *, service_account_email: _builtins.str, state: _builtins.str, subscription: _builtins.str, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerRepositoryEventConfigResult(dict):
    def __init__(__self__, *, pull_requests: Sequence[outputs.GetTriggerRepositoryEventConfigPullRequestResult], pushes: Sequence[outputs.GetTriggerRepositoryEventConfigPushResult], repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullRequests")
    def pull_requests(self) -> Sequence[outputs.GetTriggerRepositoryEventConfigPullRequestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pushes(self) -> Sequence[outputs.GetTriggerRepositoryEventConfigPushResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerRepositoryEventConfigPullRequestResult(dict):
    def __init__(__self__, *, branch: _builtins.str, comment_control: _builtins.str, invert_regex: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTriggerRepositoryEventConfigPushResult(dict):
    def __init__(__self__, *, branch: _builtins.str, invert_regex: _builtins.bool, tag: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerSourceToBuildResult(dict):
    def __init__(__self__, *, bitbucket_server_config: _builtins.str, github_enterprise_config: _builtins.str, ref: _builtins.str, repo_type: _builtins.str, repository: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTriggerTriggerTemplateResult(dict):
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
class GetTriggerWebhookConfigResult(dict):
    def __init__(__self__, *, secret: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


