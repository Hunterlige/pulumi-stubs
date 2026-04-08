import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatabaseMigrationsSqlDbArgs", "DatabaseMigrationsSqlDb"]

@pulumi.input_type
class DatabaseMigrationsSqlDbArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sql_db_instance_name: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[DatabaseMigrationPropertiesSqlDbArgs]] = ...,
        target_db_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sqlDbInstanceName")
    def sql_db_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @sql_db_instance_name.setter
    def sql_db_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[DatabaseMigrationPropertiesSqlDbArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[DatabaseMigrationPropertiesSqlDbArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDbName")
    def target_db_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_db_name.setter
    def target_db_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:datamigration:DatabaseMigrationsSqlDb")
class DatabaseMigrationsSqlDb(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    DatabaseMigrationPropertiesSqlDbArgs,
                    DatabaseMigrationPropertiesSqlDbArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_db_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatabaseMigrationsSqlDbArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DatabaseMigrationsSqlDb: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.DatabaseMigrationPropertiesSqlDbResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
