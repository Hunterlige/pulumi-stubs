import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppImageConfigArgs", "AppImageConfig"]

@pulumi.input_type
class AppImageConfigArgs:
    def __init__(
        __self__,
        *,
        app_image_config_name: pulumi.Input[_builtins.str],
        code_editor_app_image_config: Optional[
            pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]
        ] = ...,
        jupyter_lab_image_config: Optional[
            pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]
        ] = ...,
        kernel_gateway_image_config: Optional[
            pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]: ...
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppImageConfig")
    def code_editor_app_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]]: ...
    @code_editor_app_image_config.setter
    def code_editor_app_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabImageConfig")
    def jupyter_lab_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]]: ...
    @jupyter_lab_image_config.setter
    def jupyter_lab_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]]: ...
    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]]
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
class _AppImageConfigState:
    def __init__(
        __self__,
        *,
        app_image_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        code_editor_app_image_config: Optional[
            pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]
        ] = ...,
        jupyter_lab_image_config: Optional[
            pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]
        ] = ...,
        kernel_gateway_image_config: Optional[
            pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_image_config_name.setter
    def app_image_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppImageConfig")
    def code_editor_app_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]]: ...
    @code_editor_app_image_config.setter
    def code_editor_app_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabImageConfig")
    def jupyter_lab_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]]: ...
    @jupyter_lab_image_config.setter
    def jupyter_lab_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(
        self,
    ) -> Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]]: ...
    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(
        self, value: Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigArgs]]
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
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:sagemaker/appImageConfig:AppImageConfig")
class AppImageConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_image_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        code_editor_app_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigCodeEditorAppImageConfigArgs,
                    AppImageConfigCodeEditorAppImageConfigArgsDict,
                ]
            ]
        ] = ...,
        jupyter_lab_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigJupyterLabImageConfigArgs,
                    AppImageConfigJupyterLabImageConfigArgsDict,
                ]
            ]
        ] = ...,
        kernel_gateway_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigKernelGatewayImageConfigArgs,
                    AppImageConfigKernelGatewayImageConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppImageConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_image_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        code_editor_app_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigCodeEditorAppImageConfigArgs,
                    AppImageConfigCodeEditorAppImageConfigArgsDict,
                ]
            ]
        ] = ...,
        jupyter_lab_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigJupyterLabImageConfigArgs,
                    AppImageConfigJupyterLabImageConfigArgsDict,
                ]
            ]
        ] = ...,
        kernel_gateway_image_config: Optional[
            pulumi.Input[
                Union[
                    AppImageConfigKernelGatewayImageConfigArgs,
                    AppImageConfigKernelGatewayImageConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AppImageConfig: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppImageConfig")
    def code_editor_app_image_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AppImageConfigCodeEditorAppImageConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabImageConfig")
    def jupyter_lab_image_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AppImageConfigJupyterLabImageConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AppImageConfigKernelGatewayImageConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
