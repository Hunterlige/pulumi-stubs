import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoleDefinitionResult",
    "AwaitableGetRoleDefinitionResult",
    "get_role_definition",
    "get_role_definition_output",
]

@pulumi.output_type
class GetRoleDefinitionResult:
    def __init__(
        __self__,
        assignable_scopes=...,
        azure_api_version=...,
        created_by=...,
        created_on=...,
        description=...,
        id=...,
        name=...,
        permissions=...,
        role_name=...,
        role_type=...,
        type=...,
        updated_by=...,
        updated_on=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
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
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[outputs.PermissionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> _builtins.str: ...

class AwaitableGetRoleDefinitionResult(GetRoleDefinitionResult):
    def __await__(self): ...

def get_role_definition(
    role_definition_id: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleDefinitionResult: ...
def get_role_definition_output(
    role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleDefinitionResult]: ...
