import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseAccountSqlDatabaseResult",
    "AwaitableGetDatabaseAccountSqlDatabaseResult",
    "get_database_account_sql_database",
    "get_database_account_sql_database_output",
]

@pulumi.output_type
class GetDatabaseAccountSqlDatabaseResult:
    def __init__(
        __self__,
        azure_api_version=...,
        colls=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        rid=...,
        tags=...,
        ts=...,
        type=...,
        users=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def colls(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def ts(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[_builtins.str]: ...

class AwaitableGetDatabaseAccountSqlDatabaseResult(GetDatabaseAccountSqlDatabaseResult):
    def __await__(self): ...

def get_database_account_sql_database(
    account_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseAccountSqlDatabaseResult: ...
def get_database_account_sql_database_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseAccountSqlDatabaseResult]: ...
