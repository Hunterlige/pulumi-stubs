import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryCleanupPolicyArgs",
    "RepositoryCleanupPolicyArgsDict",
    "RepositoryCleanupPolicyConditionArgs",
    "RepositoryCleanupPolicyConditionArgsDict",
    "RepositoryCleanupPolicyMostRecentVersionsArgs",
    "RepositoryCleanupPolicyMostRecentVersionsArgsDict",
    "RepositoryDockerConfigArgs",
    "RepositoryDockerConfigArgsDict",
    "RepositoryIamBindingConditionArgs",
    "RepositoryIamBindingConditionArgsDict",
    "RepositoryIamMemberConditionArgs",
    "RepositoryIamMemberConditionArgsDict",
    "RepositoryMavenConfigArgs",
    "RepositoryMavenConfigArgsDict",
    "RepositoryRemoteRepositoryConfigArgs",
    "RepositoryRemoteRepositoryConfigArgsDict",
    "RepositoryRemoteRepositoryConfigAptRepositoryArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RepositoryRemoteRepositoryConfigNpmRepositoryArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RepositoryRemoteRepositoryConfigYumRepositoryArgs",
    ...,
    ...,
    ...,
    "RepositoryVirtualRepositoryConfigArgs",
    "RepositoryVirtualRepositoryConfigArgsDict",
    ...,
    ...,
    "RepositoryVulnerabilityScanningConfigArgs",
    "RepositoryVulnerabilityScanningConfigArgsDict",
]

class RepositoryCleanupPolicyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[_builtins.str]]
    condition: NotRequired[pulumi.Input[RepositoryCleanupPolicyConditionArgsDict]]
    most_recent_versions: NotRequired[
        pulumi.Input[RepositoryCleanupPolicyMostRecentVersionsArgsDict]
    ]
    ...

@pulumi.input_type
class RepositoryCleanupPolicyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        condition: Optional[pulumi.Input[RepositoryCleanupPolicyConditionArgs]] = ...,
        most_recent_versions: Optional[
            pulumi.Input[RepositoryCleanupPolicyMostRecentVersionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[RepositoryCleanupPolicyConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[RepositoryCleanupPolicyConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mostRecentVersions")
    def most_recent_versions(
        self,
    ) -> Optional[pulumi.Input[RepositoryCleanupPolicyMostRecentVersionsArgs]]: ...
    @most_recent_versions.setter
    def most_recent_versions(
        self,
        value: Optional[pulumi.Input[RepositoryCleanupPolicyMostRecentVersionsArgs]],
    ): ...

class RepositoryCleanupPolicyConditionArgsDict(TypedDict):
    newer_than: NotRequired[pulumi.Input[_builtins.str]]
    older_than: NotRequired[pulumi.Input[_builtins.str]]
    package_name_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tag_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tag_state: NotRequired[pulumi.Input[_builtins.str]]
    version_name_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class RepositoryCleanupPolicyConditionArgs:
    def __init__(
        __self__,
        *,
        newer_than: Optional[pulumi.Input[_builtins.str]] = ...,
        older_than: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_state: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newerThan")
    def newer_than(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @newer_than.setter
    def newer_than(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="olderThan")
    def older_than(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @older_than.setter
    def older_than(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @package_name_prefixes.setter
    def package_name_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagPrefixes")
    def tag_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tag_prefixes.setter
    def tag_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagState")
    def tag_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_state.setter
    def tag_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionNamePrefixes")
    def version_name_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @version_name_prefixes.setter
    def version_name_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RepositoryCleanupPolicyMostRecentVersionsArgsDict(TypedDict):
    keep_count: NotRequired[pulumi.Input[_builtins.int]]
    package_name_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class RepositoryCleanupPolicyMostRecentVersionsArgs:
    def __init__(
        __self__,
        *,
        keep_count: Optional[pulumi.Input[_builtins.int]] = ...,
        package_name_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keepCount")
    def keep_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @keep_count.setter
    def keep_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="packageNamePrefixes")
    def package_name_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @package_name_prefixes.setter
    def package_name_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RepositoryDockerConfigArgsDict(TypedDict):
    immutable_tags: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class RepositoryDockerConfigArgs:
    def __init__(
        __self__, *, immutable_tags: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="immutableTags")
    def immutable_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @immutable_tags.setter
    def immutable_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class RepositoryIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryMavenConfigArgsDict(TypedDict):
    allow_snapshot_overwrites: NotRequired[pulumi.Input[_builtins.bool]]
    version_policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryMavenConfigArgs:
    def __init__(
        __self__,
        *,
        allow_snapshot_overwrites: Optional[pulumi.Input[_builtins.bool]] = ...,
        version_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSnapshotOverwrites")
    def allow_snapshot_overwrites(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_snapshot_overwrites.setter
    def allow_snapshot_overwrites(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionPolicy")
    def version_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_policy.setter
    def version_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigArgsDict(TypedDict):
    apt_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigAptRepositoryArgsDict]
    ]
    common_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigCommonRepositoryArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_upstream_validation: NotRequired[pulumi.Input[_builtins.bool]]
    docker_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigDockerRepositoryArgsDict]
    ]
    maven_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigMavenRepositoryArgsDict]
    ]
    npm_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigNpmRepositoryArgsDict]
    ]
    python_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigPythonRepositoryArgsDict]
    ]
    upstream_credentials: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigUpstreamCredentialsArgsDict]
    ]
    yum_repository: NotRequired[
        pulumi.Input[RepositoryRemoteRepositoryConfigYumRepositoryArgsDict]
    ]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigArgs:
    def __init__(
        __self__,
        *,
        apt_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigAptRepositoryArgs]
        ] = ...,
        common_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigCommonRepositoryArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_upstream_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        docker_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigDockerRepositoryArgs]
        ] = ...,
        maven_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigMavenRepositoryArgs]
        ] = ...,
        npm_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigNpmRepositoryArgs]
        ] = ...,
        python_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigPythonRepositoryArgs]
        ] = ...,
        upstream_credentials: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigUpstreamCredentialsArgs]
        ] = ...,
        yum_repository: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigYumRepositoryArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aptRepository")
    def apt_repository(
        self,
    ) -> Optional[pulumi.Input[RepositoryRemoteRepositoryConfigAptRepositoryArgs]]: ...
    @apt_repository.setter
    def apt_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigAptRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="commonRepository")
    def common_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigCommonRepositoryArgs]
    ]: ...
    @common_repository.setter
    def common_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigCommonRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableUpstreamValidation")
    def disable_upstream_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_upstream_validation.setter
    def disable_upstream_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigDockerRepositoryArgs]
    ]: ...
    @docker_repository.setter
    def docker_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigDockerRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mavenRepository")
    def maven_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigMavenRepositoryArgs]
    ]: ...
    @maven_repository.setter
    def maven_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigMavenRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="npmRepository")
    def npm_repository(
        self,
    ) -> Optional[pulumi.Input[RepositoryRemoteRepositoryConfigNpmRepositoryArgs]]: ...
    @npm_repository.setter
    def npm_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigNpmRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonRepository")
    def python_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigPythonRepositoryArgs]
    ]: ...
    @python_repository.setter
    def python_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigPythonRepositoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upstreamCredentials")
    def upstream_credentials(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigUpstreamCredentialsArgs]
    ]: ...
    @upstream_credentials.setter
    def upstream_credentials(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigUpstreamCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="yumRepository")
    def yum_repository(
        self,
    ) -> Optional[pulumi.Input[RepositoryRemoteRepositoryConfigYumRepositoryArgs]]: ...
    @yum_repository.setter
    def yum_repository(
        self,
        value: Optional[
            pulumi.Input[RepositoryRemoteRepositoryConfigYumRepositoryArgs]
        ],
    ): ...

class RepositoryRemoteRepositoryConfigAptRepositoryArgsDict(TypedDict):
    public_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgsDict
        ]
    ]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigAptRepositoryArgs:
    def __init__(
        __self__,
        *,
        public_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgs]
    ]: ...
    @public_repository.setter
    def public_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgs
            ]
        ],
    ): ...

class RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgsDict(TypedDict):
    repository_base: pulumi.Input[_builtins.str]
    repository_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigAptRepositoryPublicRepositoryArgs:
    def __init__(
        __self__,
        *,
        repository_base: pulumi.Input[_builtins.str],
        repository_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> pulumi.Input[_builtins.str]: ...
    @repository_base.setter
    def repository_base(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> pulumi.Input[_builtins.str]: ...
    @repository_path.setter
    def repository_path(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryRemoteRepositoryConfigCommonRepositoryArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigCommonRepositoryArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryRemoteRepositoryConfigDockerRepositoryArgsDict(TypedDict):
    custom_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgsDict
        ]
    ]
    public_repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigDockerRepositoryArgs:
    def __init__(
        __self__,
        *,
        custom_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgs
            ]
        ] = ...,
        public_repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(
        self,
    ) -> Optional[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgs
        ]
    ]: ...
    @custom_repository.setter
    def custom_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_repository.setter
    def public_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgsDict(
    TypedDict
):
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigDockerRepositoryCustomRepositoryArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigMavenRepositoryArgsDict(TypedDict):
    custom_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgsDict
        ]
    ]
    public_repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigMavenRepositoryArgs:
    def __init__(
        __self__,
        *,
        custom_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgs
            ]
        ] = ...,
        public_repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(
        self,
    ) -> Optional[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgs
        ]
    ]: ...
    @custom_repository.setter
    def custom_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_repository.setter
    def public_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgsDict(
    TypedDict
):
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigMavenRepositoryCustomRepositoryArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigNpmRepositoryArgsDict(TypedDict):
    custom_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgsDict
        ]
    ]
    public_repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigNpmRepositoryArgs:
    def __init__(
        __self__,
        *,
        custom_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgs
            ]
        ] = ...,
        public_repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgs]
    ]: ...
    @custom_repository.setter
    def custom_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_repository.setter
    def public_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigNpmRepositoryCustomRepositoryArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigPythonRepositoryArgsDict(TypedDict):
    custom_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgsDict
        ]
    ]
    public_repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigPythonRepositoryArgs:
    def __init__(
        __self__,
        *,
        custom_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgs
            ]
        ] = ...,
        public_repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRepository")
    def custom_repository(
        self,
    ) -> Optional[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgs
        ]
    ]: ...
    @custom_repository.setter
    def custom_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_repository.setter
    def public_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgsDict(
    TypedDict
):
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigPythonRepositoryCustomRepositoryArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigUpstreamCredentialsArgsDict(TypedDict):
    username_password_credentials: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigUpstreamCredentialsArgs:
    def __init__(
        __self__,
        *,
        username_password_credentials: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(
        self,
    ) -> Optional[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgs
        ]
    ]: ...
    @username_password_credentials.setter
    def username_password_credentials(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgs
            ]
        ],
    ): ...

class RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgsDict(
    TypedDict
):
    password_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigUpstreamCredentialsUsernamePasswordCredentialsArgs:
    def __init__(
        __self__,
        *,
        password_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretVersion")
    def password_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_secret_version.setter
    def password_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryRemoteRepositoryConfigYumRepositoryArgsDict(TypedDict):
    public_repository: NotRequired[
        pulumi.Input[
            RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgsDict
        ]
    ]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigYumRepositoryArgs:
    def __init__(
        __self__,
        *,
        public_repository: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicRepository")
    def public_repository(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgs]
    ]: ...
    @public_repository.setter
    def public_repository(
        self,
        value: Optional[
            pulumi.Input[
                RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgs
            ]
        ],
    ): ...

class RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgsDict(TypedDict):
    repository_base: pulumi.Input[_builtins.str]
    repository_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryRemoteRepositoryConfigYumRepositoryPublicRepositoryArgs:
    def __init__(
        __self__,
        *,
        repository_base: pulumi.Input[_builtins.str],
        repository_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryBase")
    def repository_base(self) -> pulumi.Input[_builtins.str]: ...
    @repository_base.setter
    def repository_base(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryPath")
    def repository_path(self) -> pulumi.Input[_builtins.str]: ...
    @repository_path.setter
    def repository_path(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryVirtualRepositoryConfigArgsDict(TypedDict):
    upstream_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryVirtualRepositoryConfigUpstreamPolicyArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RepositoryVirtualRepositoryConfigArgs:
    def __init__(
        __self__,
        *,
        upstream_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryVirtualRepositoryConfigUpstreamPolicyArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="upstreamPolicies")
    def upstream_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RepositoryVirtualRepositoryConfigUpstreamPolicyArgs]]
        ]
    ]: ...
    @upstream_policies.setter
    def upstream_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryVirtualRepositoryConfigUpstreamPolicyArgs]
                ]
            ]
        ],
    ): ...

class RepositoryVirtualRepositoryConfigUpstreamPolicyArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    repository: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryVirtualRepositoryConfigUpstreamPolicyArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryVulnerabilityScanningConfigArgsDict(TypedDict):
    enablement_config: NotRequired[pulumi.Input[_builtins.str]]
    enablement_state: NotRequired[pulumi.Input[_builtins.str]]
    enablement_state_reason: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryVulnerabilityScanningConfigArgs:
    def __init__(
        __self__,
        *,
        enablement_config: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state: Optional[pulumi.Input[_builtins.str]] = ...,
        enablement_state_reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablementConfig")
    def enablement_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enablement_config.setter
    def enablement_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enablementState")
    def enablement_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enablement_state.setter
    def enablement_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enablementStateReason")
    def enablement_state_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enablement_state_reason.setter
    def enablement_state_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
