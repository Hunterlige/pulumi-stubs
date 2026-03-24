import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxWebhookArgs", "CxWebhook"]

@pulumi.input_type
class CxWebhookArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        generic_web_service: Optional[
            pulumi.Input[CxWebhookGenericWebServiceArgs]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_spell_correction.setter
    def enable_spell_correction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> Optional[pulumi.Input[CxWebhookGenericWebServiceArgs]]: ...
    @generic_web_service.setter
    def generic_web_service(
        self, value: Optional[pulumi.Input[CxWebhookGenericWebServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectory")
    def service_directory(
        self,
    ) -> Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]]: ...
    @service_directory.setter
    def service_directory(
        self, value: Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CxWebhookState:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        generic_web_service: Optional[
            pulumi.Input[CxWebhookGenericWebServiceArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]] = ...,
        start_flow: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_spell_correction.setter
    def enable_spell_correction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> Optional[pulumi.Input[CxWebhookGenericWebServiceArgs]]: ...
    @generic_web_service.setter
    def generic_web_service(
        self, value: Optional[pulumi.Input[CxWebhookGenericWebServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectory")
    def service_directory(
        self,
    ) -> Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]]: ...
    @service_directory.setter
    def service_directory(
        self, value: Optional[pulumi.Input[CxWebhookServiceDirectoryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_flow.setter
    def start_flow(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:diagflow/cxWebhook:CxWebhook")
class CxWebhook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        generic_web_service: Optional[
            pulumi.Input[
                Union[
                    CxWebhookGenericWebServiceArgs, CxWebhookGenericWebServiceArgsDict
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[
            pulumi.Input[
                Union[CxWebhookServiceDirectoryArgs, CxWebhookServiceDirectoryArgsDict]
            ]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxWebhookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        generic_web_service: Optional[
            pulumi.Input[
                Union[
                    CxWebhookGenericWebServiceArgs, CxWebhookGenericWebServiceArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[
            pulumi.Input[
                Union[CxWebhookServiceDirectoryArgs, CxWebhookServiceDirectoryArgsDict]
            ]
        ] = ...,
        start_flow: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CxWebhook: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> pulumi.Output[Optional[outputs.CxWebhookGenericWebService]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectory")
    def service_directory(
        self,
    ) -> pulumi.Output[Optional[outputs.CxWebhookServiceDirectory]]: ...
    @_builtins.property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
