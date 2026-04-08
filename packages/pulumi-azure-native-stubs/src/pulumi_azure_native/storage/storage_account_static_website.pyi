import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StorageAccountStaticWebsiteArgs", "StorageAccountStaticWebsite"]

@pulumi.input_type
class StorageAccountStaticWebsiteArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        error404_document: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="error404Document")
    def error404_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error404_document.setter
    def error404_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:storage:StorageAccountStaticWebsite")
class StorageAccountStaticWebsite(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        error404_document: Optional[pulumi.Input[_builtins.str]] = ...,
        index_document: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StorageAccountStaticWebsiteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StorageAccountStaticWebsite: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="error404Document")
    def error404_document(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> pulumi.Output[Optional[_builtins.str]]: ...
