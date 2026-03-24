import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InsightsConfigArgs", "InsightsConfig"]

@pulumi.input_type
class InsightsConfigArgs:
    def __init__(
        __self__,
        *,
        insights_config_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        app_hub_application: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        target_projects: Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsConfigId")
    def insights_config_id(self) -> pulumi.Input[_builtins.str]: ...
    @insights_config_id.setter
    def insights_config_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appHubApplication")
    def app_hub_application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_hub_application.setter
    def app_hub_application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactConfigs")
    def artifact_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
    ]: ...
    @artifact_configs.setter
    def artifact_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetProjects")
    def target_projects(
        self,
    ) -> Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]]: ...
    @target_projects.setter
    def target_projects(
        self, value: Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]]
    ): ...

@pulumi.input_type
class _InsightsConfigState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        app_hub_application: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorArgs]]]
        ] = ...,
        insights_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        runtime_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigRuntimeConfigArgs]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_projects: Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appHubApplication")
    def app_hub_application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_hub_application.setter
    def app_hub_application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactConfigs")
    def artifact_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
    ]: ...
    @artifact_configs.setter
    def artifact_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigArtifactConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorArgs]]]]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="insightsConfigId")
    def insights_config_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insights_config_id.setter
    def insights_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfigs")
    def runtime_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightsConfigRuntimeConfigArgs]]]
    ]: ...
    @runtime_configs.setter
    def runtime_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigRuntimeConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetProjects")
    def target_projects(
        self,
    ) -> Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]]: ...
    @target_projects.setter
    def target_projects(
        self, value: Optional[pulumi.Input[InsightsConfigTargetProjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:developerconnect/insightsConfig:InsightsConfig")
class InsightsConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        app_hub_application: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InsightsConfigArtifactConfigArgs,
                            InsightsConfigArtifactConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        insights_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        target_projects: Optional[
            pulumi.Input[
                Union[
                    InsightsConfigTargetProjectsArgs,
                    InsightsConfigTargetProjectsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InsightsConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        app_hub_application: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InsightsConfigArtifactConfigArgs,
                            InsightsConfigArtifactConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[InsightsConfigErrorArgs, InsightsConfigErrorArgsDict]
                    ]
                ]
            ]
        ] = ...,
        insights_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        runtime_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InsightsConfigRuntimeConfigArgs,
                            InsightsConfigRuntimeConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_projects: Optional[
            pulumi.Input[
                Union[
                    InsightsConfigTargetProjectsArgs,
                    InsightsConfigTargetProjectsArgsDict,
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InsightsConfig: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="appHubApplication")
    def app_hub_application(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="artifactConfigs")
    def artifact_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.InsightsConfigArtifactConfig]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.InsightsConfigError]]: ...
    @_builtins.property
    @pulumi.getter(name="insightsConfigId")
    def insights_config_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfigs")
    def runtime_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.InsightsConfigRuntimeConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetProjects")
    def target_projects(
        self,
    ) -> pulumi.Output[Optional[outputs.InsightsConfigTargetProjects]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
