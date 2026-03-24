import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppArgs", "App"]

@pulumi.input_type
class AppArgs:
    def __init__(
        __self__,
        *,
        app_name: pulumi.Input[_builtins.str],
        app_type: pulumi.Input[_builtins.str],
        domain_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_spec: Optional[pulumi.Input[AppResourceSpecArgs]] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[_builtins.str]: ...
    @app_name.setter
    def app_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> pulumi.Input[_builtins.str]: ...
    @app_type.setter
    def app_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[_builtins.str]: ...
    @domain_id.setter
    def domain_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional[pulumi.Input[AppResourceSpecArgs]]: ...
    @resource_spec.setter
    def resource_spec(self, value: Optional[pulumi.Input[AppResourceSpecArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_name.setter
    def space_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_profile_name.setter
    def user_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AppState:
    def __init__(
        __self__,
        *,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_spec: Optional[pulumi.Input[AppResourceSpecArgs]] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_name.setter
    def app_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_type.setter
    def app_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional[pulumi.Input[AppResourceSpecArgs]]: ...
    @resource_spec.setter
    def resource_spec(self, value: Optional[pulumi.Input[AppResourceSpecArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_name.setter
    def space_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_profile_name.setter
    def user_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sagemaker/app:App")
class App(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_spec: Optional[
            pulumi.Input[Union[AppResourceSpecArgs, AppResourceSpecArgsDict]]
        ] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_spec: Optional[
            pulumi.Input[Union[AppResourceSpecArgs, AppResourceSpecArgsDict]]
        ] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> App: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Output[outputs.AppResourceSpec]: ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
