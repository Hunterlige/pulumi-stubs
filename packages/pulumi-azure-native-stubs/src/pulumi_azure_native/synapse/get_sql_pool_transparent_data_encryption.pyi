import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlPoolTransparentDataEncryptionResult",
    "AwaitableGetSqlPoolTransparentDataEncryptionResult",
    "get_sql_pool_transparent_data_encryption",
    "get_sql_pool_transparent_data_encryption_output",
]

@pulumi.output_type
class GetSqlPoolTransparentDataEncryptionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        status=...,
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
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSqlPoolTransparentDataEncryptionResult(
    GetSqlPoolTransparentDataEncryptionResult
):
    def __await__(self): ...

def get_sql_pool_transparent_data_encryption(
    resource_group_name: Optional[_builtins.str] = ...,
    sql_pool_name: Optional[_builtins.str] = ...,
    transparent_data_encryption_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlPoolTransparentDataEncryptionResult: ...
def get_sql_pool_transparent_data_encryption_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sql_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    transparent_data_encryption_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlPoolTransparentDataEncryptionResult]: ...
