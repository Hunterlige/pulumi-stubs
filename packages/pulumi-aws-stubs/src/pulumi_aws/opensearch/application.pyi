import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        app_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]
        ] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]
        ] = ...,
        iam_identity_center_options: Optional[
            pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ApplicationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appConfigs")
    def app_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]]: ...
    @app_configs.setter
    def app_configs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]]: ...
    @data_sources.setter
    def data_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterOptions")
    def iam_identity_center_options(
        self,
    ) -> Optional[pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]]: ...
    @iam_identity_center_options.setter
    def iam_identity_center_options(
        self, value: Optional[pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ApplicationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ApplicationTimeoutsArgs]]): ...

@pulumi.input_type
class _ApplicationState:
    def __init__(
        __self__,
        *,
        app_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_identity_center_options: Optional[
            pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ApplicationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appConfigs")
    def app_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]]: ...
    @app_configs.setter
    def app_configs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAppConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]]: ...
    @data_sources.setter
    def data_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterOptions")
    def iam_identity_center_options(
        self,
    ) -> Optional[pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]]: ...
    @iam_identity_center_options.setter
    def iam_identity_center_options(
        self, value: Optional[pulumi.Input[ApplicationIamIdentityCenterOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ApplicationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ApplicationTimeoutsArgs]]): ...

@pulumi.type_token("aws:opensearch/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApplicationAppConfigArgs, ApplicationAppConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        data_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApplicationDataSourceArgs, ApplicationDataSourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        iam_identity_center_options: Optional[
            pulumi.Input[
                Union[
                    ApplicationIamIdentityCenterOptionsArgs,
                    ApplicationIamIdentityCenterOptionsArgsDict,
                ]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ApplicationTimeoutsArgs, ApplicationTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ApplicationArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApplicationAppConfigArgs, ApplicationAppConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        data_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ApplicationDataSourceArgs, ApplicationDataSourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_identity_center_options: Optional[
            pulumi.Input[
                Union[
                    ApplicationIamIdentityCenterOptionsArgs,
                    ApplicationIamIdentityCenterOptionsArgsDict,
                ]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ApplicationTimeoutsArgs, ApplicationTimeoutsArgsDict]]
        ] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter(name="appConfigs")
    def app_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationAppConfig]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationDataSource]]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterOptions")
    def iam_identity_center_options(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationIamIdentityCenterOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ApplicationTimeouts]]: ...
