import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPolicyAssignmentArtifactResult",
    "AwaitableGetPolicyAssignmentArtifactResult",
    "get_policy_assignment_artifact",
    "get_policy_assignment_artifact_output",
]

@pulumi.output_type
class GetPolicyAssignmentArtifactResult:
    def __init__(
        __self__,
        azure_api_version=...,
        depends_on=...,
        description=...,
        display_name=...,
        id=...,
        kind=...,
        name=...,
        parameters=...,
        policy_definition_id=...,
        resource_group=...,
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
    @pulumi.getter
    def parameters(self) -> Mapping[str, outputs.ParameterValueResponse]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPolicyAssignmentArtifactResult(GetPolicyAssignmentArtifactResult):
    def __await__(self): ...

def get_policy_assignment_artifact(
    artifact_name: Optional[_builtins.str] = ...,
    blueprint_name: Optional[_builtins.str] = ...,
    resource_scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPolicyAssignmentArtifactResult: ...
def get_policy_assignment_artifact_output(
    artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
    blueprint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPolicyAssignmentArtifactResult]: ...
