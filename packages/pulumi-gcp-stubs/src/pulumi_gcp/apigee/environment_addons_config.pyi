import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentAddonsConfigArgs", "EnvironmentAddonsConfig"]

@pulumi.input_type
class EnvironmentAddonsConfigArgs:
    def __init__(
        __self__,
        *,
        env_id: pulumi.Input[_builtins.str],
        analytics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> pulumi.Input[_builtins.str]: ...
    @env_id.setter
    def env_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="analyticsEnabled")
    def analytics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @analytics_enabled.setter
    def analytics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _EnvironmentAddonsConfigState:
    def __init__(
        __self__,
        *,
        analytics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        env_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="analyticsEnabled")
    def analytics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @analytics_enabled.setter
    def analytics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @env_id.setter
    def env_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class EnvironmentAddonsConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        analytics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        env_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentAddonsConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        analytics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        env_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EnvironmentAddonsConfig: ...
    @_builtins.property
    @pulumi.getter(name="analyticsEnabled")
    def analytics_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> pulumi.Output[_builtins.str]: ...
