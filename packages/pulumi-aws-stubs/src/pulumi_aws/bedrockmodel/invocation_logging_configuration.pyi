import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InvocationLoggingConfigurationArgs", "InvocationLoggingConfiguration"]

@pulumi.input_type
class InvocationLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        logging_config: pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs]: ...
    @logging_config.setter
    def logging_config(
        self, value: pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InvocationLoggingConfigurationState:
    def __init__(
        __self__,
        *,
        logging_config: Optional[
            pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[InvocationLoggingConfigurationLoggingConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class InvocationLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    InvocationLoggingConfigurationLoggingConfigArgs,
                    InvocationLoggingConfigurationLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InvocationLoggingConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    InvocationLoggingConfigurationLoggingConfigArgs,
                    InvocationLoggingConfigurationLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InvocationLoggingConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> pulumi.Output[outputs.InvocationLoggingConfigurationLoggingConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
