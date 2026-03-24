import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StudioLifecycleConfigArgs", "StudioLifecycleConfig"]

@pulumi.input_type
class StudioLifecycleConfigArgs:
    def __init__(
        __self__,
        *,
        studio_lifecycle_config_app_type: pulumi.Input[_builtins.str],
        studio_lifecycle_config_content: pulumi.Input[_builtins.str],
        studio_lifecycle_config_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigAppType")
    def studio_lifecycle_config_app_type(self) -> pulumi.Input[_builtins.str]: ...
    @studio_lifecycle_config_app_type.setter
    def studio_lifecycle_config_app_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigContent")
    def studio_lifecycle_config_content(self) -> pulumi.Input[_builtins.str]: ...
    @studio_lifecycle_config_content.setter
    def studio_lifecycle_config_content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigName")
    def studio_lifecycle_config_name(self) -> pulumi.Input[_builtins.str]: ...
    @studio_lifecycle_config_name.setter
    def studio_lifecycle_config_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _StudioLifecycleConfigState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_content: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigAppType")
    def studio_lifecycle_config_app_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @studio_lifecycle_config_app_type.setter
    def studio_lifecycle_config_app_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigContent")
    def studio_lifecycle_config_content(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @studio_lifecycle_config_content.setter
    def studio_lifecycle_config_content(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigName")
    def studio_lifecycle_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @studio_lifecycle_config_name.setter
    def studio_lifecycle_config_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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

@pulumi.type_token(...)
class StudioLifecycleConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_content: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StudioLifecycleConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_content: Optional[pulumi.Input[_builtins.str]] = ...,
        studio_lifecycle_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> StudioLifecycleConfig: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigAppType")
    def studio_lifecycle_config_app_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigContent")
    def studio_lifecycle_config_content(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="studioLifecycleConfigName")
    def studio_lifecycle_config_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
