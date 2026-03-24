import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PluginInstanceArgs", "PluginInstance"]

@pulumi.input_type
class PluginInstanceArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        plugin: pulumi.Input[_builtins.str],
        plugin_instance_id: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]
        ] = ...,
        auth_config: Optional[pulumi.Input[PluginInstanceAuthConfigArgs]] = ...,
        disable: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def plugin(self) -> pulumi.Input[_builtins.str]: ...
    @plugin.setter
    def plugin(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pluginInstanceId")
    def plugin_instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @plugin_instance_id.setter
    def plugin_instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[pulumi.Input[PluginInstanceAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(
        self, value: Optional[pulumi.Input[PluginInstanceAuthConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable.setter
    def disable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PluginInstanceState:
    def __init__(
        __self__,
        *,
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]
        ] = ...,
        auth_config: Optional[pulumi.Input[PluginInstanceAuthConfigArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disable: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[pulumi.Input[PluginInstanceAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(
        self, value: Optional[pulumi.Input[PluginInstanceAuthConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable.setter
    def disable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def plugin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin.setter
    def plugin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginInstanceId")
    def plugin_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_instance_id.setter
    def plugin_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:apihub/pluginInstance:PluginInstance")
class PluginInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PluginInstanceActionArgs, PluginInstanceActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        auth_config: Optional[
            pulumi.Input[
                Union[PluginInstanceAuthConfigArgs, PluginInstanceAuthConfigArgsDict]
            ]
        ] = ...,
        disable: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PluginInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PluginInstanceActionArgs, PluginInstanceActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        auth_config: Optional[
            pulumi.Input[
                Union[PluginInstanceAuthConfigArgs, PluginInstanceAuthConfigArgsDict]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disable: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PluginInstance: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.PluginInstanceAction]]: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(
        self,
    ) -> pulumi.Output[Optional[outputs.PluginInstanceAuthConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disable(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plugin(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pluginInstanceId")
    def plugin_instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
