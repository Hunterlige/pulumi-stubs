import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContainerAppsAuthConfigArgs", "ContainerAppsAuthConfig"]

@pulumi.input_type
class ContainerAppsAuthConfigArgs:
    def __init__(
        __self__,
        *,
        container_app_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        auth_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_settings: Optional[pulumi.Input[EncryptionSettingsArgs]] = ...,
        global_validation: Optional[pulumi.Input[GlobalValidationArgs]] = ...,
        http_settings: Optional[pulumi.Input[HttpSettingsArgs]] = ...,
        identity_providers: Optional[pulumi.Input[IdentityProvidersArgs]] = ...,
        login: Optional[pulumi.Input[LoginArgs]] = ...,
        platform: Optional[pulumi.Input[AuthPlatformArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerAppName")
    def container_app_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_app_name.setter
    def container_app_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authConfigName")
    def auth_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_config_name.setter
    def auth_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input[EncryptionSettingsArgs]]: ...
    @encryption_settings.setter
    def encryption_settings(
        self, value: Optional[pulumi.Input[EncryptionSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalValidation")
    def global_validation(self) -> Optional[pulumi.Input[GlobalValidationArgs]]: ...
    @global_validation.setter
    def global_validation(
        self, value: Optional[pulumi.Input[GlobalValidationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpSettings")
    def http_settings(self) -> Optional[pulumi.Input[HttpSettingsArgs]]: ...
    @http_settings.setter
    def http_settings(self, value: Optional[pulumi.Input[HttpSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> Optional[pulumi.Input[IdentityProvidersArgs]]: ...
    @identity_providers.setter
    def identity_providers(
        self, value: Optional[pulumi.Input[IdentityProvidersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[LoginArgs]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[LoginArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[AuthPlatformArgs]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[AuthPlatformArgs]]): ...

@pulumi.type_token("azure-native:app:ContainerAppsAuthConfig")
class ContainerAppsAuthConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auth_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_settings: Optional[
            pulumi.Input[Union[EncryptionSettingsArgs, EncryptionSettingsArgsDict]]
        ] = ...,
        global_validation: Optional[
            pulumi.Input[Union[GlobalValidationArgs, GlobalValidationArgsDict]]
        ] = ...,
        http_settings: Optional[
            pulumi.Input[Union[HttpSettingsArgs, HttpSettingsArgsDict]]
        ] = ...,
        identity_providers: Optional[
            pulumi.Input[Union[IdentityProvidersArgs, IdentityProvidersArgsDict]]
        ] = ...,
        login: Optional[pulumi.Input[Union[LoginArgs, LoginArgsDict]]] = ...,
        platform: Optional[
            pulumi.Input[Union[AuthPlatformArgs, AuthPlatformArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContainerAppsAuthConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ContainerAppsAuthConfig: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EncryptionSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="globalValidation")
    def global_validation(
        self,
    ) -> pulumi.Output[Optional[outputs.GlobalValidationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpSettings")
    def http_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.HttpSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="identityProviders")
    def identity_providers(
        self,
    ) -> pulumi.Output[Optional[outputs.IdentityProvidersResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> pulumi.Output[Optional[outputs.LoginResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[Optional[outputs.AuthPlatformResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
