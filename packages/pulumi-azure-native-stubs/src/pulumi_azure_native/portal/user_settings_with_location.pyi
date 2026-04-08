import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserSettingsWithLocationArgs", "UserSettingsWithLocation"]

@pulumi.input_type
class UserSettingsWithLocationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        properties: pulumi.Input[UserPropertiesArgs],
        user_settings_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[UserPropertiesArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[UserPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="userSettingsName")
    def user_settings_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_settings_name.setter
    def user_settings_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:portal:UserSettingsWithLocation")
class UserSettingsWithLocation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Union[UserPropertiesArgs, UserPropertiesArgsDict]]
        ] = ...,
        user_settings_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserSettingsWithLocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> UserSettingsWithLocation: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.UserPropertiesResponse]: ...
