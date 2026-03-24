import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectBucketConfigArgs", "ProjectBucketConfig"]

@pulumi.input_type
class ProjectBucketConfigArgs:
    def __init__(
        __self__,
        *,
        bucket_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        project: pulumi.Input[_builtins.str],
        cmek_settings: Optional[
            pulumi.Input[ProjectBucketConfigCmekSettingsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_analytics: Optional[pulumi.Input[_builtins.bool]] = ...,
        index_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
        ] = ...,
        locked: Optional[pulumi.Input[_builtins.bool]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_id.setter
    def bucket_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> Optional[pulumi.Input[ProjectBucketConfigCmekSettingsArgs]]: ...
    @cmek_settings.setter
    def cmek_settings(
        self, value: Optional[pulumi.Input[ProjectBucketConfigCmekSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAnalytics")
    def enable_analytics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_analytics.setter
    def enable_analytics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
    ]: ...
    @index_configs.setter
    def index_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _ProjectBucketConfigState:
    def __init__(
        __self__,
        *,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[ProjectBucketConfigCmekSettingsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_analytics: Optional[pulumi.Input[_builtins.bool]] = ...,
        index_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
        ] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locked: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_id.setter
    def bucket_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> Optional[pulumi.Input[ProjectBucketConfigCmekSettingsArgs]]: ...
    @cmek_settings.setter
    def cmek_settings(
        self, value: Optional[pulumi.Input[ProjectBucketConfigCmekSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAnalytics")
    def enable_analytics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_analytics.setter
    def enable_analytics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
    ]: ...
    @index_configs.setter
    def index_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectBucketConfigIndexConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class ProjectBucketConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[
                Union[
                    ProjectBucketConfigCmekSettingsArgs,
                    ProjectBucketConfigCmekSettingsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_analytics: Optional[pulumi.Input[_builtins.bool]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectBucketConfigIndexConfigArgs,
                            ProjectBucketConfigIndexConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locked: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectBucketConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_settings: Optional[
            pulumi.Input[
                Union[
                    ProjectBucketConfigCmekSettingsArgs,
                    ProjectBucketConfigCmekSettingsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_analytics: Optional[pulumi.Input[_builtins.bool]] = ...,
        index_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProjectBucketConfigIndexConfigArgs,
                            ProjectBucketConfigIndexConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locked: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> ProjectBucketConfig: ...
    @_builtins.property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cmekSettings")
    def cmek_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ProjectBucketConfigCmekSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAnalytics")
    def enable_analytics(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="indexConfigs")
    def index_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectBucketConfigIndexConfig]]]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
