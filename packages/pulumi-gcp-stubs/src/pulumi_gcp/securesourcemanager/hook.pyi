import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HookArgs", "Hook"]

@pulumi.input_type
class HookArgs:
    def __init__(
        __self__,
        *,
        hook_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        repository_id: pulumi.Input[_builtins.str],
        target_uri: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_option: Optional[pulumi.Input[HookPushOptionArgs]] = ...,
        sensitive_query_string: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hookId")
    def hook_id(self) -> pulumi.Input[_builtins.str]: ...
    @hook_id.setter
    def hook_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Input[_builtins.str]: ...
    @repository_id.setter
    def repository_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]: ...
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pushOption")
    def push_option(self) -> Optional[pulumi.Input[HookPushOptionArgs]]: ...
    @push_option.setter
    def push_option(self, value: Optional[pulumi.Input[HookPushOptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitiveQueryString")
    def sensitive_query_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sensitive_query_string.setter
    def sensitive_query_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _HookState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        hook_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_option: Optional[pulumi.Input[HookPushOptionArgs]] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_query_string: Optional[pulumi.Input[_builtins.str]] = ...,
        target_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hookId")
    def hook_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hook_id.setter
    def hook_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="pushOption")
    def push_option(self) -> Optional[pulumi.Input[HookPushOptionArgs]]: ...
    @push_option.setter
    def push_option(self, value: Optional[pulumi.Input[HookPushOptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitiveQueryString")
    def sensitive_query_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sensitive_query_string.setter
    def sensitive_query_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_uri.setter
    def target_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:securesourcemanager/hook:Hook")
class Hook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        hook_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_option: Optional[
            pulumi.Input[Union[HookPushOptionArgs, HookPushOptionArgsDict]]
        ] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_query_string: Optional[pulumi.Input[_builtins.str]] = ...,
        target_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        hook_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_option: Optional[
            pulumi.Input[Union[HookPushOptionArgs, HookPushOptionArgsDict]]
        ] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_query_string: Optional[pulumi.Input[_builtins.str]] = ...,
        target_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Hook: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hookId")
    def hook_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pushOption")
    def push_option(self) -> pulumi.Output[outputs.HookPushOption]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sensitiveQueryString")
    def sensitive_query_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
