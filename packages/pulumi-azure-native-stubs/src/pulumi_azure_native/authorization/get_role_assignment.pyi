import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoleAssignmentResult",
    "AwaitableGetRoleAssignmentResult",
    "get_role_assignment",
    "get_role_assignment_output",
]

@pulumi.output_type
class GetRoleAssignmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        condition=...,
        condition_version=...,
        created_by=...,
        created_on=...,
        delegated_managed_identity_resource_id=...,
        description=...,
        id=...,
        name=...,
        principal_id=...,
        principal_type=...,
        role_definition_id=...,
        scope=...,
        type=...,
        updated_by=...,
        updated_on=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="delegatedManagedIdentityResourceId")
    def delegated_managed_identity_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> _builtins.str: ...

class AwaitableGetRoleAssignmentResult(GetRoleAssignmentResult):
    def __await__(self): ...

def get_role_assignment(
    role_assignment_name: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    tenant_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleAssignmentResult: ...
def get_role_assignment_output(
    role_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    tenant_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleAssignmentResult]: ...
