import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectArgs", "Project"]

@pulumi.input_type
class ProjectArgs:
    def __init__(
        __self__,
        *,
        artifacts: pulumi.Input[ProjectArtifactsArgs],
        environment: pulumi.Input[ProjectEnvironmentArgs],
        service_role: pulumi.Input[_builtins.str],
        source: pulumi.Input[ProjectSourceArgs],
        auto_retry_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        badge_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        build_batch_config: Optional[pulumi.Input[ProjectBuildBatchConfigArgs]] = ...,
        build_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cache: Optional[pulumi.Input[ProjectCacheArgs]] = ...,
        concurrent_build_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
        ] = ...,
        logs_config: Optional[pulumi.Input[ProjectLogsConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
        ] = ...,
        secondary_source_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
        ] = ...,
        secondary_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]
        ] = ...,
        source_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_config: Optional[pulumi.Input[ProjectVpcConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> pulumi.Input[ProjectArtifactsArgs]: ...
    @artifacts.setter
    def artifacts(self, value: pulumi.Input[ProjectArtifactsArgs]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[ProjectEnvironmentArgs]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[ProjectEnvironmentArgs]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Input[_builtins.str]: ...
    @service_role.setter
    def service_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[ProjectSourceArgs]: ...
    @source.setter
    def source(self, value: pulumi.Input[ProjectSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="autoRetryLimit")
    def auto_retry_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auto_retry_limit.setter
    def auto_retry_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="badgeEnabled")
    def badge_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @badge_enabled.setter
    def badge_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="buildBatchConfig")
    def build_batch_config(
        self,
    ) -> Optional[pulumi.Input[ProjectBuildBatchConfigArgs]]: ...
    @build_batch_config.setter
    def build_batch_config(
        self, value: Optional[pulumi.Input[ProjectBuildBatchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildTimeout")
    def build_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @build_timeout.setter
    def build_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> Optional[pulumi.Input[ProjectCacheArgs]]: ...
    @cache.setter
    def cache(self, value: Optional[pulumi.Input[ProjectCacheArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="concurrentBuildLimit")
    def concurrent_build_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @concurrent_build_limit.setter
    def concurrent_build_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemLocations")
    def file_system_locations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
    ]: ...
    @file_system_locations.setter
    def file_system_locations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logsConfig")
    def logs_config(self) -> Optional[pulumi.Input[ProjectLogsConfigArgs]]: ...
    @logs_config.setter
    def logs_config(self, value: Optional[pulumi.Input[ProjectLogsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectVisibility")
    def project_visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_visibility.setter
    def project_visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queuedTimeout")
    def queued_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @queued_timeout.setter
    def queued_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRole")
    def resource_access_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_access_role.setter
    def resource_access_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryArtifacts")
    def secondary_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
    ]: ...
    @secondary_artifacts.setter
    def secondary_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondarySourceVersions")
    def secondary_source_versions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
    ]: ...
    @secondary_source_versions.setter
    def secondary_source_versions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondarySources")
    def secondary_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]]: ...
    @secondary_sources.setter
    def secondary_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ProjectVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ProjectVpcConfigArgs]]): ...

@pulumi.input_type
class _ProjectState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        artifacts: Optional[pulumi.Input[ProjectArtifactsArgs]] = ...,
        auto_retry_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        badge_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        badge_url: Optional[pulumi.Input[_builtins.str]] = ...,
        build_batch_config: Optional[pulumi.Input[ProjectBuildBatchConfigArgs]] = ...,
        build_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cache: Optional[pulumi.Input[ProjectCacheArgs]] = ...,
        concurrent_build_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[ProjectEnvironmentArgs]] = ...,
        file_system_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
        ] = ...,
        logs_config: Optional[pulumi.Input[ProjectLogsConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        public_project_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
        ] = ...,
        secondary_source_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
        ] = ...,
        secondary_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]
        ] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[ProjectSourceArgs]] = ...,
        source_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_config: Optional[pulumi.Input[ProjectVpcConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[pulumi.Input[ProjectArtifactsArgs]]: ...
    @artifacts.setter
    def artifacts(self, value: Optional[pulumi.Input[ProjectArtifactsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="autoRetryLimit")
    def auto_retry_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auto_retry_limit.setter
    def auto_retry_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="badgeEnabled")
    def badge_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @badge_enabled.setter
    def badge_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="badgeUrl")
    def badge_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @badge_url.setter
    def badge_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildBatchConfig")
    def build_batch_config(
        self,
    ) -> Optional[pulumi.Input[ProjectBuildBatchConfigArgs]]: ...
    @build_batch_config.setter
    def build_batch_config(
        self, value: Optional[pulumi.Input[ProjectBuildBatchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildTimeout")
    def build_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @build_timeout.setter
    def build_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> Optional[pulumi.Input[ProjectCacheArgs]]: ...
    @cache.setter
    def cache(self, value: Optional[pulumi.Input[ProjectCacheArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="concurrentBuildLimit")
    def concurrent_build_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @concurrent_build_limit.setter
    def concurrent_build_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[ProjectEnvironmentArgs]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[ProjectEnvironmentArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemLocations")
    def file_system_locations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
    ]: ...
    @file_system_locations.setter
    def file_system_locations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectFileSystemLocationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logsConfig")
    def logs_config(self) -> Optional[pulumi.Input[ProjectLogsConfigArgs]]: ...
    @logs_config.setter
    def logs_config(self, value: Optional[pulumi.Input[ProjectLogsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectVisibility")
    def project_visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_visibility.setter
    def project_visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicProjectAlias")
    def public_project_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_project_alias.setter
    def public_project_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queuedTimeout")
    def queued_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @queued_timeout.setter
    def queued_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRole")
    def resource_access_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_access_role.setter
    def resource_access_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryArtifacts")
    def secondary_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
    ]: ...
    @secondary_artifacts.setter
    def secondary_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondaryArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondarySourceVersions")
    def secondary_source_versions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
    ]: ...
    @secondary_source_versions.setter
    def secondary_source_versions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceVersionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondarySources")
    def secondary_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]]: ...
    @secondary_sources.setter
    def secondary_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSecondarySourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[ProjectSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[ProjectSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ProjectVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ProjectVpcConfigArgs]]): ...

@pulumi.type_token("aws:codebuild/project:Project")
class Project(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        artifacts: Optional[
            pulumi.Input[Union[ProjectArtifactsArgs, ProjectArtifactsArgsDict]]
        ] = ...,
        auto_retry_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        badge_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        build_batch_config: Optional[
            pulumi.Input[
                Union[ProjectBuildBatchConfigArgs, ProjectBuildBatchConfigArgsDict]
            ]
        ] = ...,
        build_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cache: Optional[
            pulumi.Input[Union[ProjectCacheArgs, ProjectCacheArgsDict]]
        ] = ...,
        concurrent_build_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[
            pulumi.Input[Union[ProjectEnvironmentArgs, ProjectEnvironmentArgsDict]]
        ] = ...,
        file_system_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectFileSystemLocationArgs,
                            ProjectFileSystemLocationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        logs_config: Optional[
            pulumi.Input[Union[ProjectLogsConfigArgs, ProjectLogsConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondaryArtifactArgs,
                            ProjectSecondaryArtifactArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        secondary_source_versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondarySourceVersionArgs,
                            ProjectSecondarySourceVersionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        secondary_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondarySourceArgs, ProjectSecondarySourceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[Union[ProjectSourceArgs, ProjectSourceArgsDict]]
        ] = ...,
        source_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_config: Optional[
            pulumi.Input[Union[ProjectVpcConfigArgs, ProjectVpcConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        artifacts: Optional[
            pulumi.Input[Union[ProjectArtifactsArgs, ProjectArtifactsArgsDict]]
        ] = ...,
        auto_retry_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        badge_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        badge_url: Optional[pulumi.Input[_builtins.str]] = ...,
        build_batch_config: Optional[
            pulumi.Input[
                Union[ProjectBuildBatchConfigArgs, ProjectBuildBatchConfigArgsDict]
            ]
        ] = ...,
        build_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        cache: Optional[
            pulumi.Input[Union[ProjectCacheArgs, ProjectCacheArgsDict]]
        ] = ...,
        concurrent_build_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[
            pulumi.Input[Union[ProjectEnvironmentArgs, ProjectEnvironmentArgsDict]]
        ] = ...,
        file_system_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectFileSystemLocationArgs,
                            ProjectFileSystemLocationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        logs_config: Optional[
            pulumi.Input[Union[ProjectLogsConfigArgs, ProjectLogsConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        public_project_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondaryArtifactArgs,
                            ProjectSecondaryArtifactArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        secondary_source_versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondarySourceVersionArgs,
                            ProjectSecondarySourceVersionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        secondary_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectSecondarySourceArgs, ProjectSecondarySourceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[Union[ProjectSourceArgs, ProjectSourceArgsDict]]
        ] = ...,
        source_version: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_config: Optional[
            pulumi.Input[Union[ProjectVpcConfigArgs, ProjectVpcConfigArgsDict]]
        ] = ...,
    ) -> Project: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> pulumi.Output[outputs.ProjectArtifacts]: ...
    @_builtins.property
    @pulumi.getter(name="autoRetryLimit")
    def auto_retry_limit(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="badgeEnabled")
    def badge_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="badgeUrl")
    def badge_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildBatchConfig")
    def build_batch_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ProjectBuildBatchConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="buildTimeout")
    def build_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> pulumi.Output[Optional[outputs.ProjectCache]]: ...
    @_builtins.property
    @pulumi.getter(name="concurrentBuildLimit")
    def concurrent_build_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[outputs.ProjectEnvironment]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemLocations")
    def file_system_locations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectFileSystemLocation]]]: ...
    @_builtins.property
    @pulumi.getter(name="logsConfig")
    def logs_config(self) -> pulumi.Output[Optional[outputs.ProjectLogsConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectVisibility")
    def project_visibility(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicProjectAlias")
    def public_project_alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queuedTimeout")
    def queued_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRole")
    def resource_access_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryArtifacts")
    def secondary_artifacts(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectSecondaryArtifact]]]: ...
    @_builtins.property
    @pulumi.getter(name="secondarySourceVersions")
    def secondary_source_versions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectSecondarySourceVersion]]]: ...
    @_builtins.property
    @pulumi.getter(name="secondarySources")
    def secondary_sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectSecondarySource]]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.ProjectSource]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.ProjectVpcConfig]]: ...
