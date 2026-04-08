import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlResourceSqlRoleAssignmentResult",
    "AwaitableGetSqlResourceSqlRoleAssignmentResult",
    "get_sql_resource_sql_role_assignment",
    "get_sql_resource_sql_role_assignment_output",
]

@pulumi.output_type
class GetSqlResourceSqlRoleAssignmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        principal_id=...,
        role_definition_id=...,
        scope=...,
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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSqlResourceSqlRoleAssignmentResult(
    GetSqlResourceSqlRoleAssignmentResult
):
    def __await__(self): ...

def get_sql_resource_sql_role_assignment(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    role_assignment_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlResourceSqlRoleAssignmentResult: ...
def get_sql_resource_sql_role_assignment_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    role_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlResourceSqlRoleAssignmentResult]: ...
