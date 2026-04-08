import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SettingArgs", "Setting"]

@pulumi.input_type
class SettingArgs:
    def __init__(
        __self__,
        *,
        scope: pulumi.Input[_builtins.str],
        cache: Optional[
            pulumi.Input[Sequence[pulumi.Input[SettingsPropertiesCacheArgs]]]
        ] = ...,
        setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_on: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cache(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SettingsPropertiesCacheArgs]]]
    ]: ...
    @cache.setter
    def cache(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SettingsPropertiesCacheArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @setting_name.setter
    def setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startOn")
    def start_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_on.setter
    def start_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:costmanagement:Setting")
class Setting(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SettingsPropertiesCacheArgs, SettingsPropertiesCacheArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start_on: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SettingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Setting: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cache(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SettingsPropertiesResponseCache]]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startOn")
    def start_on(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
