import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContentItemArgs", "ContentItem"]

@pulumi.input_type
class ContentItemArgs:
    def __init__(
        __self__,
        *,
        content_type_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        content_item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentTypeId")
    def content_type_id(self) -> pulumi.Input[_builtins.str]: ...
    @content_type_id.setter
    def content_type_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentItemId")
    def content_item_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_item_id.setter
    def content_item_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...
    @properties.setter
    def properties(self, value: Optional[Any]): ...

@pulumi.type_token("azure-native:apimanagement:ContentItem")
class ContentItem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        content_item_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[Any] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContentItemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ContentItem: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
