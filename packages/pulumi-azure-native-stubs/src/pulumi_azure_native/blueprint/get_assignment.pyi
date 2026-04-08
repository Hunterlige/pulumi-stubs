import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAssignmentResult",
    "AwaitableGetAssignmentResult",
    "get_assignment",
    "get_assignment_output",
]

@pulumi.output_type
class GetAssignmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        blueprint_id=...,
        description=...,
        display_name=...,
        id=...,
        identity=...,
        location=...,
        locks=...,
        name=...,
        parameters=...,
        provisioning_state=...,
        resource_groups=...,
        scope=...,
        status=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> Optional[_builtins.str]: ...
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
    def identity(self) -> outputs.ManagedServiceIdentityResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locks(self) -> Optional[outputs.AssignmentLockSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, outputs.ParameterValueResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Mapping[str, outputs.ResourceGroupValueResponse]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.AssignmentStatusResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAssignmentResult(GetAssignmentResult):
    def __await__(self): ...

def get_assignment(
    assignment_name: Optional[_builtins.str] = ...,
    resource_scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAssignmentResult: ...
def get_assignment_output(
    assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAssignmentResult]: ...
