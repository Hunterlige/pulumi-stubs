import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiLogicConfigArgs", "AiLogicConfig"]

@pulumi.input_type
class AiLogicConfigArgs:
    def __init__(
        __self__,
        *,
        generative_language_config: Optional[
            pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetry_config: Optional[
            pulumi.Input[AiLogicConfigTelemetryConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="generativeLanguageConfig")
    def generative_language_config(
        self,
    ) -> Optional[pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]]: ...
    @generative_language_config.setter
    def generative_language_config(
        self, value: Optional[pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(
        self,
    ) -> Optional[pulumi.Input[AiLogicConfigTelemetryConfigArgs]]: ...
    @telemetry_config.setter
    def telemetry_config(
        self, value: Optional[pulumi.Input[AiLogicConfigTelemetryConfigArgs]]
    ): ...

@pulumi.input_type
class _AiLogicConfigState:
    def __init__(
        __self__,
        *,
        generative_language_config: Optional[
            pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetry_config: Optional[
            pulumi.Input[AiLogicConfigTelemetryConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="generativeLanguageConfig")
    def generative_language_config(
        self,
    ) -> Optional[pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]]: ...
    @generative_language_config.setter
    def generative_language_config(
        self, value: Optional[pulumi.Input[AiLogicConfigGenerativeLanguageConfigArgs]]
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
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(
        self,
    ) -> Optional[pulumi.Input[AiLogicConfigTelemetryConfigArgs]]: ...
    @telemetry_config.setter
    def telemetry_config(
        self, value: Optional[pulumi.Input[AiLogicConfigTelemetryConfigArgs]]
    ): ...

@pulumi.type_token("gcp:firebase/aiLogicConfig:AiLogicConfig")
class AiLogicConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        generative_language_config: Optional[
            pulumi.Input[
                Union[
                    AiLogicConfigGenerativeLanguageConfigArgs,
                    AiLogicConfigGenerativeLanguageConfigArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetry_config: Optional[
            pulumi.Input[
                Union[
                    AiLogicConfigTelemetryConfigArgs,
                    AiLogicConfigTelemetryConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AiLogicConfigArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        generative_language_config: Optional[
            pulumi.Input[
                Union[
                    AiLogicConfigGenerativeLanguageConfigArgs,
                    AiLogicConfigGenerativeLanguageConfigArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetry_config: Optional[
            pulumi.Input[
                Union[
                    AiLogicConfigTelemetryConfigArgs,
                    AiLogicConfigTelemetryConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> AiLogicConfig: ...
    @_builtins.property
    @pulumi.getter(name="generativeLanguageConfig")
    def generative_language_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AiLogicConfigGenerativeLanguageConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AiLogicConfigTelemetryConfig]]: ...
