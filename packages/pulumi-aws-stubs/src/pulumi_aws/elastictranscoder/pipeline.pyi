import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipelineArgs", "Pipeline"]

@pulumi.input_type
class PipelineArgs:
    def __init__(
        __self__,
        *,
        input_bucket: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
        aws_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        content_config: Optional[pulumi.Input[PipelineContentConfigArgs]] = ...,
        content_config_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[pulumi.Input[PipelineNotificationsArgs]] = ...,
        output_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbnail_config: Optional[pulumi.Input[PipelineThumbnailConfigArgs]] = ...,
        thumbnail_config_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputBucket")
    def input_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @input_bucket.setter
    def input_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyArn")
    def aws_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_kms_key_arn.setter
    def aws_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> Optional[pulumi.Input[PipelineContentConfigArgs]]: ...
    @content_config.setter
    def content_config(
        self, value: Optional[pulumi.Input[PipelineContentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentConfigPermissions")
    def content_config_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
    ]: ...
    @content_config_permissions.setter
    def content_config_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[PipelineNotificationsArgs]]: ...
    @notifications.setter
    def notifications(
        self, value: Optional[pulumi.Input[PipelineNotificationsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputBucket")
    def output_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_bucket.setter
    def output_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfig")
    def thumbnail_config(
        self,
    ) -> Optional[pulumi.Input[PipelineThumbnailConfigArgs]]: ...
    @thumbnail_config.setter
    def thumbnail_config(
        self, value: Optional[pulumi.Input[PipelineThumbnailConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfigPermissions")
    def thumbnail_config_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
    ]: ...
    @thumbnail_config_permissions.setter
    def thumbnail_config_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
        ],
    ): ...

@pulumi.input_type
class _PipelineState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        content_config: Optional[pulumi.Input[PipelineContentConfigArgs]] = ...,
        content_config_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
        ] = ...,
        input_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[pulumi.Input[PipelineNotificationsArgs]] = ...,
        output_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbnail_config: Optional[pulumi.Input[PipelineThumbnailConfigArgs]] = ...,
        thumbnail_config_permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyArn")
    def aws_kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_kms_key_arn.setter
    def aws_kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> Optional[pulumi.Input[PipelineContentConfigArgs]]: ...
    @content_config.setter
    def content_config(
        self, value: Optional[pulumi.Input[PipelineContentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentConfigPermissions")
    def content_config_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
    ]: ...
    @content_config_permissions.setter
    def content_config_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineContentConfigPermissionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputBucket")
    def input_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_bucket.setter
    def input_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[PipelineNotificationsArgs]]: ...
    @notifications.setter
    def notifications(
        self, value: Optional[pulumi.Input[PipelineNotificationsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputBucket")
    def output_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_bucket.setter
    def output_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfig")
    def thumbnail_config(
        self,
    ) -> Optional[pulumi.Input[PipelineThumbnailConfigArgs]]: ...
    @thumbnail_config.setter
    def thumbnail_config(
        self, value: Optional[pulumi.Input[PipelineThumbnailConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfigPermissions")
    def thumbnail_config_permissions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
    ]: ...
    @thumbnail_config_permissions.setter
    def thumbnail_config_permissions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineThumbnailConfigPermissionArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:elastictranscoder/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        content_config: Optional[
            pulumi.Input[
                Union[PipelineContentConfigArgs, PipelineContentConfigArgsDict]
            ]
        ] = ...,
        content_config_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineContentConfigPermissionArgs,
                            PipelineContentConfigPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[
                Union[PipelineNotificationsArgs, PipelineNotificationsArgsDict]
            ]
        ] = ...,
        output_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbnail_config: Optional[
            pulumi.Input[
                Union[PipelineThumbnailConfigArgs, PipelineThumbnailConfigArgsDict]
            ]
        ] = ...,
        thumbnail_config_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineThumbnailConfigPermissionArgs,
                            PipelineThumbnailConfigPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipelineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        content_config: Optional[
            pulumi.Input[
                Union[PipelineContentConfigArgs, PipelineContentConfigArgsDict]
            ]
        ] = ...,
        content_config_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineContentConfigPermissionArgs,
                            PipelineContentConfigPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[
            pulumi.Input[
                Union[PipelineNotificationsArgs, PipelineNotificationsArgsDict]
            ]
        ] = ...,
        output_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbnail_config: Optional[
            pulumi.Input[
                Union[PipelineThumbnailConfigArgs, PipelineThumbnailConfigArgsDict]
            ]
        ] = ...,
        thumbnail_config_permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PipelineThumbnailConfigPermissionArgs,
                            PipelineThumbnailConfigPermissionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> Pipeline: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyArn")
    def aws_kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentConfig")
    def content_config(self) -> pulumi.Output[outputs.PipelineContentConfig]: ...
    @_builtins.property
    @pulumi.getter(name="contentConfigPermissions")
    def content_config_permissions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PipelineContentConfigPermission]]]: ...
    @_builtins.property
    @pulumi.getter(name="inputBucket")
    def input_bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> pulumi.Output[Optional[outputs.PipelineNotifications]]: ...
    @_builtins.property
    @pulumi.getter(name="outputBucket")
    def output_bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfig")
    def thumbnail_config(self) -> pulumi.Output[outputs.PipelineThumbnailConfig]: ...
    @_builtins.property
    @pulumi.getter(name="thumbnailConfigPermissions")
    def thumbnail_config_permissions(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PipelineThumbnailConfigPermission]]
    ]: ...
