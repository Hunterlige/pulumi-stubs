import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StorageInsightConfigArgs", "StorageInsightConfig"]

@pulumi.input_type
class StorageInsightConfigArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        storage_account: pulumi.Input[StorageAccountArgs],
        workspace_name: pulumi.Input[_builtins.str],
        containers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_insight_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tables: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Input[StorageAccountArgs]: ...
    @storage_account.setter
    def storage_account(self, value: pulumi.Input[StorageAccountArgs]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @containers.setter
    def containers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageInsightName")
    def storage_insight_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_insight_name.setter
    def storage_insight_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tables.setter
    def tables(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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

@pulumi.type_token(...)
class StorageInsightConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        containers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account: Optional[
            pulumi.Input[Union[StorageAccountArgs, StorageAccountArgsDict]]
        ] = ...,
        storage_insight_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tables: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StorageInsightConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StorageInsightConfig: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.StorageInsightStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output[outputs.StorageAccountResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
