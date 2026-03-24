

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryCleanupPolicy', 'RepositoryCleanupPolicyCondition', 'RepositoryCleanupPolicyMostRecentVersions', 'RepositoryDockerConfig', 'RepositoryIamBindingCondition', 'RepositoryIamMemberCondition', 'RepositoryMavenConfig', 'RepositoryRemoteRepositoryConfig', 'RepositoryRemoteRepositoryConfigAptRepository', ..., 'RepositoryRemoteRepositoryConfigCommonRepository', 'RepositoryRemoteRepositoryConfigDockerRepository', ..., 'RepositoryRemoteRepositoryConfigMavenRepository', ..., 'RepositoryRemoteRepositoryConfigNpmRepository', ..., 'RepositoryRemoteRepositoryConfigPythonRepository', ..., ..., ..., 'RepositoryRemoteRepositoryConfigYumRepository', ..., 'RepositoryVirtualRepositoryConfig', 'RepositoryVirtualRepositoryConfigUpstreamPolicy', 'RepositoryVulnerabilityScanningConfig', 'GetDockerImagesDockerImageResult', 'GetMavenArtifactsMavenArtifactResult', 'GetNpmPackagesNpmPackageResult', 'GetPackagesPackageResult', 'GetPythonPackagesPythonPackageResult', 'GetRepositoriesRepositoryResult', 'GetRepositoryCleanupPolicyResult', 'GetRepositoryCleanupPolicyConditionResult', 'GetRepositoryCleanupPolicyMostRecentVersionResult', 'GetRepositoryDockerConfigResult', 'GetRepositoryMavenConfigResult', 'GetRepositoryRemoteRepositoryConfigResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetRepositoryVirtualRepositoryConfigResult', ..., 'GetRepositoryVulnerabilityScanningConfigResult', 'GetTagsTagResult', 'GetVersionRelatedTagResult', 'GetVersionsVersionResult', 'GetVersionsVersionRelatedTagResult']
@pulumi.output_type
class RepositoryCleanupPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, action: Optional[_builtins.str] = ..., condition: Optional[outputs.RepositoryCleanupPolicyCondition] = ..., most_recent_versions: Optional[outputs.RepositoryCleanupPolicyMostRecentVersions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.RepositoryCleanupPolicyCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecentVersions")
    def most_recent_versions(self) -> Optional[outputs.RepositoryCleanupPolicyMostRecentVersions]:
        
        ...
    


@pulumi.output_type
class RepositoryCleanupPolicyCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, newer_than: Optional[_builtins.str] = ..., older_than: Optional[_builtins.str] = ..., package_name_prefixes: Optional[Sequence[_builtins.str]] = ..., tag_prefixes: Optional[Sequence[_builtins.str]] = ..., tag_state: Optional[_builtins.str] = ..., version_name_prefixes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerThan")
    def newer_than(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="olderThan")
    def older_than(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagPrefixes")
    def tag_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagState")
    def tag_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNamePrefixes")
    def version_name_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RepositoryCleanupPolicyMostRecentVersions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, keep_count: Optional[_builtins.int] = ..., package_name_prefixes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keepCount")
    def keep_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RepositoryDockerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immutable_tags: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableTags")
    def immutable_tags(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RepositoryIamBindingCondition(dict):
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
class RepositoryIamMemberCondition(dict):
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
class RepositoryMavenConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_snapshot_overwrites: Optional[_builtins.bool] = ..., version_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSnapshotOverwrites")
    def allow_snapshot_overwrites(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionPolicy")
    def version_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apt_repository: Optional[outputs.RepositoryRemoteRepositoryConfigAptRepository] = ..., common_repository: Optional[outputs.RepositoryRemoteRepositoryConfigCommonRepository] = ..., description: Optional[_builtins.str] = ..., disable_upstream_validation: Optional[_builtins.bool] = ..., docker_repository: Optional[outputs.RepositoryRemoteRepositoryConfigDockerRepository] = ..., maven_repository: Optional[outputs.RepositoryRemoteRepositoryConfigMavenRepository] = ..., npm_repository: Optional[outputs.RepositoryRemoteRepositoryConfigNpmRepository] = ..., python_repository: Optional[outputs.RepositoryRemoteRepositoryConfigPythonRepository] = ..., upstream_credentials: Optional[outputs.RepositoryRemoteRepositoryConfigUpstreamCredentials] = ..., yum_repository: Optional[outputs.RepositoryRemoteRepositoryConfigYumRepository] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aptRepository")
    def apt_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigAptRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonRepository")
    def common_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigCommonRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableUpstreamValidation")
    def disable_upstream_validation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigDockerRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenRepository")
    def maven_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigMavenRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="npmRepository")
    def npm_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigNpmRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonRepository")
    def python_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigPythonRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upstreamCredentials")
    def upstream_credentials(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigUpstreamCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yumRepository")
    def yum_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigYumRepository]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigAptRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, public_repository: Optional[outputs.RepositoryRemoteRepositoryConfigAptRepositoryPublicRepository] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigAptRepositoryPublicRepository]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigAptRepositoryPublicRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repository_base: _builtins.str, repository_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigCommonRepository(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigDockerRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_repository: Optional[outputs.RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepository] = ..., public_repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepository(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigMavenRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_repository: Optional[outputs.RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepository] = ..., public_repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepository(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigNpmRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_repository: Optional[outputs.RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepository] = ..., public_repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepository(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigPythonRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_repository: Optional[outputs.RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepository] = ..., public_repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepository(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigUpstreamCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, username_password_credentials: Optional[outputs.RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentials] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentials]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password_secret_version: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretVersion")
    def password_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigYumRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, public_repository: Optional[outputs.RepositoryRemoteRepositoryConfigYumRepositoryPublicRepository] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[outputs.RepositoryRemoteRepositoryConfigYumRepositoryPublicRepository]:
        
        ...
    


@pulumi.output_type
class RepositoryRemoteRepositoryConfigYumRepositoryPublicRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repository_base: _builtins.str, repository_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RepositoryVirtualRepositoryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, upstream_policies: Optional[Sequence[outputs.RepositoryVirtualRepositoryConfigUpstreamPolicy]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upstreamPolicies")
    def upstream_policies(self) -> Optional[Sequence[outputs.RepositoryVirtualRepositoryConfigUpstreamPolicy]]:
        
        ...
    


@pulumi.output_type
class RepositoryVirtualRepositoryConfigUpstreamPolicy(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., priority: Optional[_builtins.int] = ..., repository: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryVulnerabilityScanningConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enablement_config: Optional[_builtins.str] = ..., enablement_state: Optional[_builtins.str] = ..., enablement_state_reason: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementConfig")
    def enablement_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementStateReason")
    def enablement_state_reason(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetDockerImagesDockerImageResult(dict):
    def __init__(__self__, *, build_time: _builtins.str, image_name: _builtins.str, image_size_bytes: _builtins.str, media_type: _builtins.str, name: _builtins.str, self_link: _builtins.str, tags: Sequence[_builtins.str], update_time: _builtins.str, upload_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildTime")
    def build_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageSizeBytes")
    def image_size_bytes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadTime")
    def upload_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMavenArtifactsMavenArtifactResult(dict):
    def __init__(__self__, *, artifact_id: _builtins.str, create_time: _builtins.str, group_id: _builtins.str, name: _builtins.str, pom_uri: _builtins.str, update_time: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pomUri")
    def pom_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNpmPackagesNpmPackageResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, name: _builtins.str, package_name: _builtins.str, tags: Sequence[_builtins.str], update_time: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPackagesPackageResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], create_time: _builtins.str, display_name: _builtins.str, name: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPythonPackagesPythonPackageResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, name: _builtins.str, package_name: _builtins.str, update_time: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoriesRepositoryResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, description: _builtins.str, format: _builtins.str, id: _builtins.str, repository_id: _builtins.str, update_time: _builtins.str) -> None:
        
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
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryCleanupPolicyResult(dict):
    def __init__(__self__, *, action: _builtins.str, conditions: Sequence[outputs.GetRepositoryCleanupPolicyConditionResult], id: _builtins.str, most_recent_versions: Sequence[outputs.GetRepositoryCleanupPolicyMostRecentVersionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetRepositoryCleanupPolicyConditionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecentVersions")
    def most_recent_versions(self) -> Sequence[outputs.GetRepositoryCleanupPolicyMostRecentVersionResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryCleanupPolicyConditionResult(dict):
    def __init__(__self__, *, newer_than: _builtins.str, older_than: _builtins.str, package_name_prefixes: Sequence[_builtins.str], tag_prefixes: Sequence[_builtins.str], tag_state: _builtins.str, version_name_prefixes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerThan")
    def newer_than(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="olderThan")
    def older_than(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagPrefixes")
    def tag_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagState")
    def tag_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNamePrefixes")
    def version_name_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRepositoryCleanupPolicyMostRecentVersionResult(dict):
    def __init__(__self__, *, keep_count: _builtins.int, package_name_prefixes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keepCount")
    def keep_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRepositoryDockerConfigResult(dict):
    def __init__(__self__, *, immutable_tags: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableTags")
    def immutable_tags(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetRepositoryMavenConfigResult(dict):
    def __init__(__self__, *, allow_snapshot_overwrites: _builtins.bool, version_policy: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSnapshotOverwrites")
    def allow_snapshot_overwrites(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionPolicy")
    def version_policy(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigResult(dict):
    def __init__(__self__, *, apt_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigAptRepositoryResult], common_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigCommonRepositoryResult], description: _builtins.str, disable_upstream_validation: _builtins.bool, docker_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigDockerRepositoryResult], maven_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigMavenRepositoryResult], npm_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigNpmRepositoryResult], python_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigPythonRepositoryResult], upstream_credentials: Sequence[outputs.GetRepositoryRemoteRepositoryConfigUpstreamCredentialResult], yum_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigYumRepositoryResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aptRepositories")
    def apt_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigAptRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonRepositories")
    def common_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigCommonRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableUpstreamValidation")
    def disable_upstream_validation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerRepositories")
    def docker_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigDockerRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mavenRepositories")
    def maven_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigMavenRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="npmRepositories")
    def npm_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigNpmRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonRepositories")
    def python_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigPythonRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upstreamCredentials")
    def upstream_credentials(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigUpstreamCredentialResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yumRepositories")
    def yum_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigYumRepositoryResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigAptRepositoryResult(dict):
    def __init__(__self__, *, public_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepositories")
    def public_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryResult(dict):
    def __init__(__self__, *, repository_base: _builtins.str, repository_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigCommonRepositoryResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigDockerRepositoryResult(dict):
    def __init__(__self__, *, custom_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryResult], public_repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepositories")
    def custom_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigMavenRepositoryResult(dict):
    def __init__(__self__, *, custom_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryResult], public_repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepositories")
    def custom_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigNpmRepositoryResult(dict):
    def __init__(__self__, *, custom_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryResult], public_repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepositories")
    def custom_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigPythonRepositoryResult(dict):
    def __init__(__self__, *, custom_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryResult], public_repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRepositories")
    def custom_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigUpstreamCredentialResult(dict):
    def __init__(__self__, *, username_password_credentials: Sequence[outputs.GetRepositoryRemoteRepositoryConfigUpstreamCredentialUsernamePasswordCredentialResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigUpstreamCredentialUsernamePasswordCredentialResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigUpstreamCredentialUsernamePasswordCredentialResult(dict):
    def __init__(__self__, *, password_secret_version: _builtins.str, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretVersion")
    def password_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigYumRepositoryResult(dict):
    def __init__(__self__, *, public_repositories: Sequence[outputs.GetRepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicRepositories")
    def public_repositories(self) -> Sequence[outputs.GetRepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryResult(dict):
    def __init__(__self__, *, repository_base: _builtins.str, repository_path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryVirtualRepositoryConfigResult(dict):
    def __init__(__self__, *, upstream_policies: Sequence[outputs.GetRepositoryVirtualRepositoryConfigUpstreamPolicyResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upstreamPolicies")
    def upstream_policies(self) -> Sequence[outputs.GetRepositoryVirtualRepositoryConfigUpstreamPolicyResult]:
        
        ...
    


@pulumi.output_type
class GetRepositoryVirtualRepositoryConfigUpstreamPolicyResult(dict):
    def __init__(__self__, *, id: _builtins.str, priority: _builtins.int, repository: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRepositoryVulnerabilityScanningConfigResult(dict):
    def __init__(__self__, *, enablement_config: _builtins.str, enablement_state: _builtins.str, enablement_state_reason: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementConfig")
    def enablement_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablementStateReason")
    def enablement_state_reason(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTagsTagResult(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVersionRelatedTagResult(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetVersionsVersionResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], create_time: _builtins.str, description: _builtins.str, name: _builtins.str, related_tags: Sequence[outputs.GetVersionsVersionRelatedTagResult], update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedTags")
    def related_tags(self) -> Sequence[outputs.GetVersionsVersionRelatedTagResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetVersionsVersionRelatedTagResult(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        ...
    


