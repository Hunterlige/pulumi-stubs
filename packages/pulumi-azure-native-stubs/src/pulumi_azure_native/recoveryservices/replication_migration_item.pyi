import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationMigrationItemArgs", "ReplicationMigrationItem"]

@pulumi.input_type
class ReplicationMigrationItemArgs:
    def __init__(
        __self__,
        *,
        fabric_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[EnableMigrationInputPropertiesArgs],
        protection_container_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        migration_item_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_name.setter
    def fabric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[EnableMigrationInputPropertiesArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[EnableMigrationInputPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="protectionContainerName")
    def protection_container_name(self) -> pulumi.Input[_builtins.str]: ...
    @protection_container_name.setter
    def protection_container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="migrationItemName")
    def migration_item_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_item_name.setter
    def migration_item_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ReplicationMigrationItem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_item_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    EnableMigrationInputPropertiesArgs,
                    EnableMigrationInputPropertiesArgsDict,
                ]
            ]
        ] = ...,
        protection_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationMigrationItemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ReplicationMigrationItem: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.MigrationItemPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
