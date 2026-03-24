import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BitbucketServerConfigConnectedRepositoryArgs",
    "BitbucketServerConfigConnectedRepositoryArgsDict",
    "BitbucketServerConfigSecretsArgs",
    "BitbucketServerConfigSecretsArgsDict",
    "TriggerApprovalConfigArgs",
    "TriggerApprovalConfigArgsDict",
    "TriggerBitbucketServerTriggerConfigArgs",
    "TriggerBitbucketServerTriggerConfigArgsDict",
    "TriggerBitbucketServerTriggerConfigPullRequestArgs",
    ...,
    "TriggerBitbucketServerTriggerConfigPushArgs",
    "TriggerBitbucketServerTriggerConfigPushArgsDict",
    "TriggerBuildArgs",
    "TriggerBuildArgsDict",
    "TriggerBuildArtifactsArgs",
    "TriggerBuildArtifactsArgsDict",
    "TriggerBuildArtifactsMavenArtifactArgs",
    "TriggerBuildArtifactsMavenArtifactArgsDict",
    "TriggerBuildArtifactsNpmPackageArgs",
    "TriggerBuildArtifactsNpmPackageArgsDict",
    "TriggerBuildArtifactsObjectsArgs",
    "TriggerBuildArtifactsObjectsArgsDict",
    "TriggerBuildArtifactsObjectsTimingArgs",
    "TriggerBuildArtifactsObjectsTimingArgsDict",
    "TriggerBuildArtifactsPythonPackageArgs",
    "TriggerBuildArtifactsPythonPackageArgsDict",
    "TriggerBuildAvailableSecretsArgs",
    "TriggerBuildAvailableSecretsArgsDict",
    "TriggerBuildAvailableSecretsSecretManagerArgs",
    "TriggerBuildAvailableSecretsSecretManagerArgsDict",
    "TriggerBuildOptionsArgs",
    "TriggerBuildOptionsArgsDict",
    "TriggerBuildOptionsVolumeArgs",
    "TriggerBuildOptionsVolumeArgsDict",
    "TriggerBuildSecretArgs",
    "TriggerBuildSecretArgsDict",
    "TriggerBuildSourceArgs",
    "TriggerBuildSourceArgsDict",
    "TriggerBuildSourceRepoSourceArgs",
    "TriggerBuildSourceRepoSourceArgsDict",
    "TriggerBuildSourceStorageSourceArgs",
    "TriggerBuildSourceStorageSourceArgsDict",
    "TriggerBuildStepArgs",
    "TriggerBuildStepArgsDict",
    "TriggerBuildStepVolumeArgs",
    "TriggerBuildStepVolumeArgsDict",
    "TriggerDeveloperConnectEventConfigArgs",
    "TriggerDeveloperConnectEventConfigArgsDict",
    "TriggerDeveloperConnectEventConfigPullRequestArgs",
    ...,
    "TriggerDeveloperConnectEventConfigPushArgs",
    "TriggerDeveloperConnectEventConfigPushArgsDict",
    "TriggerGitFileSourceArgs",
    "TriggerGitFileSourceArgsDict",
    "TriggerGithubArgs",
    "TriggerGithubArgsDict",
    "TriggerGithubPullRequestArgs",
    "TriggerGithubPullRequestArgsDict",
    "TriggerGithubPushArgs",
    "TriggerGithubPushArgsDict",
    "TriggerPubsubConfigArgs",
    "TriggerPubsubConfigArgsDict",
    "TriggerRepositoryEventConfigArgs",
    "TriggerRepositoryEventConfigArgsDict",
    "TriggerRepositoryEventConfigPullRequestArgs",
    "TriggerRepositoryEventConfigPullRequestArgsDict",
    "TriggerRepositoryEventConfigPushArgs",
    "TriggerRepositoryEventConfigPushArgsDict",
    "TriggerSourceToBuildArgs",
    "TriggerSourceToBuildArgsDict",
    "TriggerTriggerTemplateArgs",
    "TriggerTriggerTemplateArgsDict",
    "TriggerWebhookConfigArgs",
    "TriggerWebhookConfigArgsDict",
    "WorkerPoolNetworkConfigArgs",
    "WorkerPoolNetworkConfigArgsDict",
    "WorkerPoolPrivateServiceConnectArgs",
    "WorkerPoolPrivateServiceConnectArgsDict",
    "WorkerPoolWorkerConfigArgs",
    "WorkerPoolWorkerConfigArgsDict",
]

class BitbucketServerConfigConnectedRepositoryArgsDict(TypedDict):
    project_key: pulumi.Input[_builtins.str]
    repo_slug: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class BitbucketServerConfigConnectedRepositoryArgs:
    def __init__(
        __self__,
        *,
        project_key: pulumi.Input[_builtins.str],
        repo_slug: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> pulumi.Input[_builtins.str]: ...
    @project_key.setter
    def project_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> pulumi.Input[_builtins.str]: ...
    @repo_slug.setter
    def repo_slug(self, value: pulumi.Input[_builtins.str]): ...

class BitbucketServerConfigSecretsArgsDict(TypedDict):
    admin_access_token_version_name: pulumi.Input[_builtins.str]
    read_access_token_version_name: pulumi.Input[_builtins.str]
    webhook_secret_version_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class BitbucketServerConfigSecretsArgs:
    def __init__(
        __self__,
        *,
        admin_access_token_version_name: pulumi.Input[_builtins.str],
        read_access_token_version_name: pulumi.Input[_builtins.str],
        webhook_secret_version_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminAccessTokenVersionName")
    def admin_access_token_version_name(self) -> pulumi.Input[_builtins.str]: ...
    @admin_access_token_version_name.setter
    def admin_access_token_version_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readAccessTokenVersionName")
    def read_access_token_version_name(self) -> pulumi.Input[_builtins.str]: ...
    @read_access_token_version_name.setter
    def read_access_token_version_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretVersionName")
    def webhook_secret_version_name(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_secret_version_name.setter
    def webhook_secret_version_name(self, value: pulumi.Input[_builtins.str]): ...

class TriggerApprovalConfigArgsDict(TypedDict):
    approval_required: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TriggerApprovalConfigArgs:
    def __init__(
        __self__, *, approval_required: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @approval_required.setter
    def approval_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TriggerBitbucketServerTriggerConfigArgsDict(TypedDict):
    bitbucket_server_config_resource: pulumi.Input[_builtins.str]
    project_key: pulumi.Input[_builtins.str]
    repo_slug: pulumi.Input[_builtins.str]
    pull_request: NotRequired[
        pulumi.Input[TriggerBitbucketServerTriggerConfigPullRequestArgsDict]
    ]
    push: NotRequired[pulumi.Input[TriggerBitbucketServerTriggerConfigPushArgsDict]]
    ...

@pulumi.input_type
class TriggerBitbucketServerTriggerConfigArgs:
    def __init__(
        __self__,
        *,
        bitbucket_server_config_resource: pulumi.Input[_builtins.str],
        project_key: pulumi.Input[_builtins.str],
        repo_slug: pulumi.Input[_builtins.str],
        pull_request: Optional[
            pulumi.Input[TriggerBitbucketServerTriggerConfigPullRequestArgs]
        ] = ...,
        push: Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigPushArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfigResource")
    def bitbucket_server_config_resource(self) -> pulumi.Input[_builtins.str]: ...
    @bitbucket_server_config_resource.setter
    def bitbucket_server_config_resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectKey")
    def project_key(self) -> pulumi.Input[_builtins.str]: ...
    @project_key.setter
    def project_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> pulumi.Input[_builtins.str]: ...
    @repo_slug.setter
    def repo_slug(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(
        self,
    ) -> Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigPullRequestArgs]]: ...
    @pull_request.setter
    def pull_request(
        self,
        value: Optional[
            pulumi.Input[TriggerBitbucketServerTriggerConfigPullRequestArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def push(
        self,
    ) -> Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigPushArgs]]: ...
    @push.setter
    def push(
        self, value: Optional[pulumi.Input[TriggerBitbucketServerTriggerConfigPushArgs]]
    ): ...

class TriggerBitbucketServerTriggerConfigPullRequestArgsDict(TypedDict):
    branch: pulumi.Input[_builtins.str]
    comment_control: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TriggerBitbucketServerTriggerConfigPullRequestArgs:
    def __init__(
        __self__,
        *,
        branch: pulumi.Input[_builtins.str],
        comment_control: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> pulumi.Input[_builtins.str]: ...
    @branch.setter
    def branch(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment_control.setter
    def comment_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TriggerBitbucketServerTriggerConfigPushArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBitbucketServerTriggerConfigPushArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildArgsDict(TypedDict):
    steps: pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepArgsDict]]]
    artifacts: NotRequired[pulumi.Input[TriggerBuildArtifactsArgsDict]]
    available_secrets: NotRequired[pulumi.Input[TriggerBuildAvailableSecretsArgsDict]]
    images: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logs_bucket: NotRequired[pulumi.Input[_builtins.str]]
    options: NotRequired[pulumi.Input[TriggerBuildOptionsArgsDict]]
    queue_ttl: NotRequired[pulumi.Input[_builtins.str]]
    secrets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildSecretArgsDict]]]
    ]
    source: NotRequired[pulumi.Input[TriggerBuildSourceArgsDict]]
    substitutions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildArgs:
    def __init__(
        __self__,
        *,
        steps: pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepArgs]]],
        artifacts: Optional[pulumi.Input[TriggerBuildArtifactsArgs]] = ...,
        available_secrets: Optional[
            pulumi.Input[TriggerBuildAvailableSecretsArgs]
        ] = ...,
        images: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        logs_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[pulumi.Input[TriggerBuildOptionsArgs]] = ...,
        queue_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildSecretArgs]]]
        ] = ...,
        source: Optional[pulumi.Input[TriggerBuildSourceArgs]] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepArgs]]]: ...
    @steps.setter
    def steps(
        self, value: pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[pulumi.Input[TriggerBuildArtifactsArgs]]: ...
    @artifacts.setter
    def artifacts(self, value: Optional[pulumi.Input[TriggerBuildArtifactsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="availableSecrets")
    def available_secrets(
        self,
    ) -> Optional[pulumi.Input[TriggerBuildAvailableSecretsArgs]]: ...
    @available_secrets.setter
    def available_secrets(
        self, value: Optional[pulumi.Input[TriggerBuildAvailableSecretsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def images(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @images.setter
    def images(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logsBucket")
    def logs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logs_bucket.setter
    def logs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[TriggerBuildOptionsArgs]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[TriggerBuildOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="queueTtl")
    def queue_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @queue_ttl.setter
    def queue_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerBuildSecretArgs]]]]: ...
    @secrets.setter
    def secrets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TriggerBuildSecretArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[TriggerBuildSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[TriggerBuildSourceArgs]]): ...
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
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildArtifactsArgsDict(TypedDict):
    images: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    maven_artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsMavenArtifactArgsDict]]]
    ]
    npm_packages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsNpmPackageArgsDict]]]
    ]
    objects: NotRequired[pulumi.Input[TriggerBuildArtifactsObjectsArgsDict]]
    python_packages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsPythonPackageArgsDict]]]
    ]
    ...

@pulumi.input_type
class TriggerBuildArtifactsArgs:
    def __init__(
        __self__,
        *,
        images: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        maven_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsMavenArtifactArgs]]]
        ] = ...,
        npm_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsNpmPackageArgs]]]
        ] = ...,
        objects: Optional[pulumi.Input[TriggerBuildArtifactsObjectsArgs]] = ...,
        python_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsPythonPackageArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def images(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @images.setter
    def images(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mavenArtifacts")
    def maven_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsMavenArtifactArgs]]]
    ]: ...
    @maven_artifacts.setter
    def maven_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsMavenArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="npmPackages")
    def npm_packages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsNpmPackageArgs]]]
    ]: ...
    @npm_packages.setter
    def npm_packages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsNpmPackageArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[TriggerBuildArtifactsObjectsArgs]]: ...
    @objects.setter
    def objects(
        self, value: Optional[pulumi.Input[TriggerBuildArtifactsObjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsPythonPackageArgs]]]
    ]: ...
    @python_packages.setter
    def python_packages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsPythonPackageArgs]]]
        ],
    ): ...

class TriggerBuildArtifactsMavenArtifactArgsDict(TypedDict):
    artifact_id: NotRequired[pulumi.Input[_builtins.str]]
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildArtifactsMavenArtifactArgs:
    def __init__(
        __self__,
        *,
        artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_id.setter
    def artifact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildArtifactsNpmPackageArgsDict(TypedDict):
    package_path: NotRequired[pulumi.Input[_builtins.str]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildArtifactsNpmPackageArgs:
    def __init__(
        __self__,
        *,
        package_path: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_path.setter
    def package_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildArtifactsObjectsArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    timings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsObjectsTimingArgsDict]]]
    ]
    ...

@pulumi.input_type
class TriggerBuildArtifactsObjectsArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        timings: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsObjectsTimingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @paths.setter
    def paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsObjectsTimingArgs]]]
    ]: ...
    @timings.setter
    def timings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildArtifactsObjectsTimingArgs]]]
        ],
    ): ...

class TriggerBuildArtifactsObjectsTimingArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildArtifactsObjectsTimingArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildArtifactsPythonPackageArgsDict(TypedDict):
    paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildArtifactsPythonPackageArgs:
    def __init__(
        __self__,
        *,
        paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @paths.setter
    def paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildAvailableSecretsArgsDict(TypedDict):
    secret_managers: pulumi.Input[
        Sequence[pulumi.Input[TriggerBuildAvailableSecretsSecretManagerArgsDict]]
    ]
    ...

@pulumi.input_type
class TriggerBuildAvailableSecretsArgs:
    def __init__(
        __self__,
        *,
        secret_managers: pulumi.Input[
            Sequence[pulumi.Input[TriggerBuildAvailableSecretsSecretManagerArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretManagers")
    def secret_managers(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TriggerBuildAvailableSecretsSecretManagerArgs]]
    ]: ...
    @secret_managers.setter
    def secret_managers(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TriggerBuildAvailableSecretsSecretManagerArgs]]
        ],
    ): ...

class TriggerBuildAvailableSecretsSecretManagerArgsDict(TypedDict):
    env: pulumi.Input[_builtins.str]
    version_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TriggerBuildAvailableSecretsSecretManagerArgs:
    def __init__(
        __self__,
        *,
        env: pulumi.Input[_builtins.str],
        version_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def env(self) -> pulumi.Input[_builtins.str]: ...
    @env.setter
    def env(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Input[_builtins.str]: ...
    @version_name.setter
    def version_name(self, value: pulumi.Input[_builtins.str]): ...

class TriggerBuildOptionsArgsDict(TypedDict):
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    dynamic_substitutions: NotRequired[pulumi.Input[_builtins.bool]]
    envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    log_streaming_option: NotRequired[pulumi.Input[_builtins.str]]
    logging: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    requested_verify_option: NotRequired[pulumi.Input[_builtins.str]]
    secret_envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_provenance_hashes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    substitution_option: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildOptionsVolumeArgsDict]]]
    ]
    worker_pool: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildOptionsArgs:
    def __init__(
        __self__,
        *,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        dynamic_substitutions: Optional[pulumi.Input[_builtins.bool]] = ...,
        envs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        log_streaming_option: Optional[pulumi.Input[_builtins.str]] = ...,
        logging: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        requested_verify_option: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_provenance_hashes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        substitution_option: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildOptionsVolumeArgs]]]
        ] = ...,
        worker_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicSubstitutions")
    def dynamic_substitutions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dynamic_substitutions.setter
    def dynamic_substitutions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @envs.setter
    def envs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logStreamingOption")
    def log_streaming_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_streaming_option.setter
    def log_streaming_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestedVerifyOption")
    def requested_verify_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requested_verify_option.setter
    def requested_verify_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @secret_envs.setter
    def secret_envs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceProvenanceHashes")
    def source_provenance_hashes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_provenance_hashes.setter
    def source_provenance_hashes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="substitutionOption")
    def substitution_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @substitution_option.setter
    def substitution_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildOptionsVolumeArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildOptionsVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_pool.setter
    def worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildOptionsVolumeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildOptionsVolumeArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildSecretArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    secret_env: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class TriggerBuildSecretArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        secret_env: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretEnv")
    def secret_env(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @secret_env.setter
    def secret_env(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class TriggerBuildSourceArgsDict(TypedDict):
    repo_source: NotRequired[pulumi.Input[TriggerBuildSourceRepoSourceArgsDict]]
    storage_source: NotRequired[pulumi.Input[TriggerBuildSourceStorageSourceArgsDict]]
    ...

@pulumi.input_type
class TriggerBuildSourceArgs:
    def __init__(
        __self__,
        *,
        repo_source: Optional[pulumi.Input[TriggerBuildSourceRepoSourceArgs]] = ...,
        storage_source: Optional[
            pulumi.Input[TriggerBuildSourceStorageSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repoSource")
    def repo_source(
        self,
    ) -> Optional[pulumi.Input[TriggerBuildSourceRepoSourceArgs]]: ...
    @repo_source.setter
    def repo_source(
        self, value: Optional[pulumi.Input[TriggerBuildSourceRepoSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageSource")
    def storage_source(
        self,
    ) -> Optional[pulumi.Input[TriggerBuildSourceStorageSourceArgs]]: ...
    @storage_source.setter
    def storage_source(
        self, value: Optional[pulumi.Input[TriggerBuildSourceStorageSourceArgs]]
    ): ...

class TriggerBuildSourceRepoSourceArgsDict(TypedDict):
    repo_name: pulumi.Input[_builtins.str]
    branch_name: NotRequired[pulumi.Input[_builtins.str]]
    commit_sha: NotRequired[pulumi.Input[_builtins.str]]
    dir: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    substitutions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tag_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildSourceRepoSourceArgs:
    def __init__(
        __self__,
        *,
        repo_name: pulumi.Input[_builtins.str],
        branch_name: Optional[pulumi.Input[_builtins.str]] = ...,
        commit_sha: Optional[pulumi.Input[_builtins.str]] = ...,
        dir: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        substitutions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> pulumi.Input[_builtins.str]: ...
    @repo_name.setter
    def repo_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dir.setter
    def dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_name.setter
    def tag_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildSourceStorageSourceArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerBuildSourceStorageSourceArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerBuildStepArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    allow_exit_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    allow_failure: NotRequired[pulumi.Input[_builtins.bool]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dir: NotRequired[pulumi.Input[_builtins.str]]
    entrypoint: NotRequired[pulumi.Input[_builtins.str]]
    envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    script: NotRequired[pulumi.Input[_builtins.str]]
    secret_envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    timing: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepVolumeArgsDict]]]
    ]
    wait_fors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class TriggerBuildStepArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        allow_exit_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        allow_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        dir: Optional[pulumi.Input[_builtins.str]] = ...,
        entrypoint: Optional[pulumi.Input[_builtins.str]] = ...,
        envs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        script: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        timing: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepVolumeArgs]]]
        ] = ...,
        wait_fors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowExitCodes")
    def allow_exit_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @allow_exit_codes.setter
    def allow_exit_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowFailure")
    def allow_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_failure.setter
    def allow_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dir.setter
    def dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entrypoint.setter
    def entrypoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @envs.setter
    def envs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script.setter
    def script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @secret_envs.setter
    def secret_envs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timing.setter
    def timing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepVolumeArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TriggerBuildStepVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitFors")
    def wait_fors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @wait_fors.setter
    def wait_fors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TriggerBuildStepVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TriggerBuildStepVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class TriggerDeveloperConnectEventConfigArgsDict(TypedDict):
    git_repository_link: pulumi.Input[_builtins.str]
    git_repository_link_type: NotRequired[pulumi.Input[_builtins.str]]
    pull_request: NotRequired[
        pulumi.Input[TriggerDeveloperConnectEventConfigPullRequestArgsDict]
    ]
    push: NotRequired[pulumi.Input[TriggerDeveloperConnectEventConfigPushArgsDict]]
    ...

@pulumi.input_type
class TriggerDeveloperConnectEventConfigArgs:
    def __init__(
        __self__,
        *,
        git_repository_link: pulumi.Input[_builtins.str],
        git_repository_link_type: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request: Optional[
            pulumi.Input[TriggerDeveloperConnectEventConfigPullRequestArgs]
        ] = ...,
        push: Optional[pulumi.Input[TriggerDeveloperConnectEventConfigPushArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLink")
    def git_repository_link(self) -> pulumi.Input[_builtins.str]: ...
    @git_repository_link.setter
    def git_repository_link(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLinkType")
    def git_repository_link_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_repository_link_type.setter
    def git_repository_link_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(
        self,
    ) -> Optional[pulumi.Input[TriggerDeveloperConnectEventConfigPullRequestArgs]]: ...
    @pull_request.setter
    def pull_request(
        self,
        value: Optional[
            pulumi.Input[TriggerDeveloperConnectEventConfigPullRequestArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def push(
        self,
    ) -> Optional[pulumi.Input[TriggerDeveloperConnectEventConfigPushArgs]]: ...
    @push.setter
    def push(
        self, value: Optional[pulumi.Input[TriggerDeveloperConnectEventConfigPushArgs]]
    ): ...

class TriggerDeveloperConnectEventConfigPullRequestArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    comment_control: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TriggerDeveloperConnectEventConfigPullRequestArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        comment_control: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment_control.setter
    def comment_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TriggerDeveloperConnectEventConfigPushArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerDeveloperConnectEventConfigPushArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerGitFileSourceArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    repo_type: pulumi.Input[_builtins.str]
    bitbucket_server_config: NotRequired[pulumi.Input[_builtins.str]]
    github_enterprise_config: NotRequired[pulumi.Input[_builtins.str]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerGitFileSourceArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        repo_type: pulumi.Input[_builtins.str],
        bitbucket_server_config: Optional[pulumi.Input[_builtins.str]] = ...,
        github_enterprise_config: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Input[_builtins.str]: ...
    @repo_type.setter
    def repo_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bitbucket_server_config.setter
    def bitbucket_server_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @github_enterprise_config.setter
    def github_enterprise_config(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerGithubArgsDict(TypedDict):
    enterprise_config_resource_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    pull_request: NotRequired[pulumi.Input[TriggerGithubPullRequestArgsDict]]
    push: NotRequired[pulumi.Input[TriggerGithubPushArgsDict]]
    ...

@pulumi.input_type
class TriggerGithubArgs:
    def __init__(
        __self__,
        *,
        enterprise_config_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request: Optional[pulumi.Input[TriggerGithubPullRequestArgs]] = ...,
        push: Optional[pulumi.Input[TriggerGithubPushArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enterpriseConfigResourceName")
    def enterprise_config_resource_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enterprise_config_resource_name.setter
    def enterprise_config_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[pulumi.Input[TriggerGithubPullRequestArgs]]: ...
    @pull_request.setter
    def pull_request(
        self, value: Optional[pulumi.Input[TriggerGithubPullRequestArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[pulumi.Input[TriggerGithubPushArgs]]: ...
    @push.setter
    def push(self, value: Optional[pulumi.Input[TriggerGithubPushArgs]]): ...

class TriggerGithubPullRequestArgsDict(TypedDict):
    branch: pulumi.Input[_builtins.str]
    comment_control: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TriggerGithubPullRequestArgs:
    def __init__(
        __self__,
        *,
        branch: pulumi.Input[_builtins.str],
        comment_control: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> pulumi.Input[_builtins.str]: ...
    @branch.setter
    def branch(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment_control.setter
    def comment_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TriggerGithubPushArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerGithubPushArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerPubsubConfigArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    subscription: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerPubsubConfigArgs:
    def __init__(
        __self__,
        *,
        topic: pulumi.Input[_builtins.str],
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription.setter
    def subscription(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerRepositoryEventConfigArgsDict(TypedDict):
    pull_request: NotRequired[
        pulumi.Input[TriggerRepositoryEventConfigPullRequestArgsDict]
    ]
    push: NotRequired[pulumi.Input[TriggerRepositoryEventConfigPushArgsDict]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerRepositoryEventConfigArgs:
    def __init__(
        __self__,
        *,
        pull_request: Optional[
            pulumi.Input[TriggerRepositoryEventConfigPullRequestArgs]
        ] = ...,
        push: Optional[pulumi.Input[TriggerRepositoryEventConfigPushArgs]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(
        self,
    ) -> Optional[pulumi.Input[TriggerRepositoryEventConfigPullRequestArgs]]: ...
    @pull_request.setter
    def pull_request(
        self, value: Optional[pulumi.Input[TriggerRepositoryEventConfigPullRequestArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[pulumi.Input[TriggerRepositoryEventConfigPushArgs]]: ...
    @push.setter
    def push(
        self, value: Optional[pulumi.Input[TriggerRepositoryEventConfigPushArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerRepositoryEventConfigPullRequestArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    comment_control: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TriggerRepositoryEventConfigPullRequestArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        comment_control: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commentControl")
    def comment_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment_control.setter
    def comment_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TriggerRepositoryEventConfigPushArgsDict(TypedDict):
    branch: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerRepositoryEventConfigPushArgs:
    def __init__(
        __self__,
        *,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerSourceToBuildArgsDict(TypedDict):
    ref: pulumi.Input[_builtins.str]
    repo_type: pulumi.Input[_builtins.str]
    bitbucket_server_config: NotRequired[pulumi.Input[_builtins.str]]
    github_enterprise_config: NotRequired[pulumi.Input[_builtins.str]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerSourceToBuildArgs:
    def __init__(
        __self__,
        *,
        ref: pulumi.Input[_builtins.str],
        repo_type: pulumi.Input[_builtins.str],
        bitbucket_server_config: Optional[pulumi.Input[_builtins.str]] = ...,
        github_enterprise_config: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> pulumi.Input[_builtins.str]: ...
    @ref.setter
    def ref(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Input[_builtins.str]: ...
    @repo_type.setter
    def repo_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bitbucketServerConfig")
    def bitbucket_server_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bitbucket_server_config.setter
    def bitbucket_server_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @github_enterprise_config.setter
    def github_enterprise_config(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerTriggerTemplateArgsDict(TypedDict):
    branch_name: NotRequired[pulumi.Input[_builtins.str]]
    commit_sha: NotRequired[pulumi.Input[_builtins.str]]
    dir: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    repo_name: NotRequired[pulumi.Input[_builtins.str]]
    tag_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerTriggerTemplateArgs:
    def __init__(
        __self__,
        *,
        branch_name: Optional[pulumi.Input[_builtins.str]] = ...,
        commit_sha: Optional[pulumi.Input[_builtins.str]] = ...,
        dir: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repo_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dir.setter
    def dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repo_name.setter
    def repo_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_name.setter
    def tag_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TriggerWebhookConfigArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TriggerWebhookConfigArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolNetworkConfigArgsDict(TypedDict):
    peered_network: pulumi.Input[_builtins.str]
    peered_network_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkerPoolNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        peered_network: pulumi.Input[_builtins.str],
        peered_network_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peeredNetwork")
    def peered_network(self) -> pulumi.Input[_builtins.str]: ...
    @peered_network.setter
    def peered_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peeredNetworkIpRange")
    def peered_network_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peered_network_ip_range.setter
    def peered_network_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolPrivateServiceConnectArgsDict(TypedDict):
    network_attachment: pulumi.Input[_builtins.str]
    route_all_traffic: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class WorkerPoolPrivateServiceConnectArgs:
    def __init__(
        __self__,
        *,
        network_attachment: pulumi.Input[_builtins.str],
        route_all_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> pulumi.Input[_builtins.str]: ...
    @network_attachment.setter
    def network_attachment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routeAllTraffic")
    def route_all_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @route_all_traffic.setter
    def route_all_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkerPoolWorkerConfigArgsDict(TypedDict):
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    no_external_ip: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class WorkerPoolWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        no_external_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="noExternalIp")
    def no_external_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_external_ip.setter
    def no_external_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
