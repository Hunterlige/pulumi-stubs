import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MediaInsightsPipelineConfigurationArgs",
    "MediaInsightsPipelineConfiguration",
]

@pulumi.input_type
class MediaInsightsPipelineConfigurationArgs:
    def __init__(
        __self__,
        *,
        elements: pulumi.Input[
            Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
        ],
        resource_access_role_arn: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        real_time_alert_configuration: Optional[
            pulumi.Input[
                MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def elements(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
    ]: ...
    @elements.setter
    def elements(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoleArn")
    def resource_access_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_access_role_arn.setter
    def resource_access_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="realTimeAlertConfiguration")
    def real_time_alert_configuration(
        self,
    ) -> Optional[
        pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs]
    ]: ...
    @real_time_alert_configuration.setter
    def real_time_alert_configuration(
        self,
        value: Optional[
            pulumi.Input[
                MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _MediaInsightsPipelineConfigurationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        elements: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        real_time_alert_configuration: Optional[
            pulumi.Input[
                MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elements(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
        ]
    ]: ...
    @elements.setter
    def elements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MediaInsightsPipelineConfigurationElementArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="realTimeAlertConfiguration")
    def real_time_alert_configuration(
        self,
    ) -> Optional[
        pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs]
    ]: ...
    @real_time_alert_configuration.setter
    def real_time_alert_configuration(
        self,
        value: Optional[
            pulumi.Input[
                MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoleArn")
    def resource_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_access_role_arn.setter
    def resource_access_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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

@pulumi.type_token(...)
class MediaInsightsPipelineConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        elements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MediaInsightsPipelineConfigurationElementArgs,
                            MediaInsightsPipelineConfigurationElementArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        real_time_alert_configuration: Optional[
            pulumi.Input[
                Union[
                    MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs,
                    MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MediaInsightsPipelineConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        elements: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MediaInsightsPipelineConfigurationElementArgs,
                            MediaInsightsPipelineConfigurationElementArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        real_time_alert_configuration: Optional[
            pulumi.Input[
                Union[
                    MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs,
                    MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> MediaInsightsPipelineConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elements(
        self,
    ) -> pulumi.Output[Sequence[outputs.MediaInsightsPipelineConfigurationElement]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="realTimeAlertConfiguration")
    def real_time_alert_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoleArn")
    def resource_access_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
