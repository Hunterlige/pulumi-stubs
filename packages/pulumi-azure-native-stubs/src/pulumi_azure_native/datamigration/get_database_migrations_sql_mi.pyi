import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseMigrationsSqlMiResult",
    "AwaitableGetDatabaseMigrationsSqlMiResult",
    "get_database_migrations_sql_mi",
    "get_database_migrations_sql_mi_output",
]

@pulumi.output_type
class GetDatabaseMigrationsSqlMiResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.DatabaseMigrationPropertiesSqlMiResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDatabaseMigrationsSqlMiResult(GetDatabaseMigrationsSqlMiResult):
    def __await__(self): ...

def get_database_migrations_sql_mi(
    expand: Optional[_builtins.str] = ...,
    managed_instance_name: Optional[_builtins.str] = ...,
    migration_operation_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    target_db_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseMigrationsSqlMiResult: ...
def get_database_migrations_sql_mi_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    migration_operation_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    target_db_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseMigrationsSqlMiResult]: ...
