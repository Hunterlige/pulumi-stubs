import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GlobalSettingsArgs", "GlobalSettings"]

@pulumi.input_type
class GlobalSettingsArgs:
    def __init__(
        __self__,
        *,
        global_settings: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalSettings")
    def global_settings(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @global_settings.setter
    def global_settings(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

@pulumi.input_type
class _GlobalSettingsState:
    def __init__(
        __self__,
        *,
        global_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalSettings")
    def global_settings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @global_settings.setter
    def global_settings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:backup/globalSettings:GlobalSettings")
class GlobalSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        global_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GlobalSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        global_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> GlobalSettings: ...
    @_builtins.property
    @pulumi.getter(name="globalSettings")
    def global_settings(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
