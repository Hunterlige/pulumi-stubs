import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoleAssignmentArtifactResult",
    "AwaitableGetRoleAssignmentArtifactResult",
    "get_role_assignment_artifact",
    "get_role_assignment_artifact_output",
]

@pulumi.output_type
class GetRoleAssignmentArtifactResult:
    def __init__(
        __self__,
        azure_api_version=...,
        depends_on=...,
        description=...,
        display_name=...,
        id=...,
        kind=...,
        name=...,
        principal_ids=...,
        resource_group=...,
        role_definition_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalIds")
    def principal_ids(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRoleAssignmentArtifactResult(GetRoleAssignmentArtifactResult):
    def __await__(self): ...

def get_role_assignment_artifact(
    artifact_name: Optional[_builtins.str] = ...,
    blueprint_name: Optional[_builtins.str] = ...,
    resource_scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleAssignmentArtifactResult: ...
def get_role_assignment_artifact_output(
    artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
    blueprint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleAssignmentArtifactResult]: ...
