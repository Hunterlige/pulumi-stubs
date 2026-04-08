import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlResourceSqlRoleDefinitionResult",
    "AwaitableGetSqlResourceSqlRoleDefinitionResult",
    "get_sql_resource_sql_role_definition",
    "get_sql_resource_sql_role_definition_output",
]

@pulumi.output_type
class GetSqlResourceSqlRoleDefinitionResult:
    def __init__(
        __self__,
        assignable_scopes=...,
        azure_api_version=...,
        id=...,
        name=...,
        permissions=...,
        role_name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
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
    def permissions(self) -> Optional[Sequence[outputs.PermissionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSqlResourceSqlRoleDefinitionResult(
    GetSqlResourceSqlRoleDefinitionResult
):
    def __await__(self): ...

def get_sql_resource_sql_role_definition(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    role_definition_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlResourceSqlRoleDefinitionResult: ...
def get_sql_resource_sql_role_definition_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlResourceSqlRoleDefinitionResult]: ...
