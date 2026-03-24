import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAppCustomizationArgs", "WebAppCustomization"]

@pulumi.input_type
class WebAppCustomizationArgs:
    def __init__(
        __self__,
        *,
        web_app_id: pulumi.Input[_builtins.str],
        favicon_file: Optional[pulumi.Input[_builtins.str]] = ...,
        logo_file: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> pulumi.Input[_builtins.str]: ...
    @web_app_id.setter
    def web_app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="faviconFile")
    def favicon_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @favicon_file.setter
    def favicon_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logoFile")
    def logo_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logo_file.setter
    def logo_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WebAppCustomizationState:
    def __init__(
        __self__,
        *,
        favicon_file: Optional[pulumi.Input[_builtins.str]] = ...,
        logo_file: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faviconFile")
    def favicon_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @favicon_file.setter
    def favicon_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logoFile")
    def logo_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logo_file.setter
    def logo_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_app_id.setter
    def web_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WebAppCustomization(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        favicon_file: Optional[pulumi.Input[_builtins.str]] = ...,
        logo_file: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAppCustomizationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        favicon_file: Optional[pulumi.Input[_builtins.str]] = ...,
        logo_file: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        web_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WebAppCustomization: ...
    @_builtins.property
    @pulumi.getter(name="faviconFile")
    def favicon_file(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logoFile")
    def logo_file(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> pulumi.Output[_builtins.str]: ...
