import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGremlinResourceGremlinRoleAssignmentResult",
    ...,
    "get_gremlin_resource_gremlin_role_assignment",
    ...,
]

@pulumi.output_type
class GetGremlinResourceGremlinRoleAssignmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        principal_id=...,
        provisioning_state=...,
        role_definition_id=...,
        scope=...,
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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGremlinResourceGremlinRoleAssignmentResult(
    GetGremlinResourceGremlinRoleAssignmentResult
):
    def __await__(self): ...

def get_gremlin_resource_gremlin_role_assignment(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    role_assignment_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGremlinResourceGremlinRoleAssignmentResult: ...
def get_gremlin_resource_gremlin_role_assignment_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    role_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGremlinResourceGremlinRoleAssignmentResult]: ...
