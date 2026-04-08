import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegistrationAssignmentResult",
    "AwaitableGetRegistrationAssignmentResult",
    "get_registration_assignment",
    "get_registration_assignment_output",
]

@pulumi.output_type
class GetRegistrationAssignmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
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
    @pulumi.getter
    def properties(self) -> outputs.RegistrationAssignmentPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRegistrationAssignmentResult(GetRegistrationAssignmentResult):
    def __await__(self): ...

def get_registration_assignment(
    expand_registration_definition: Optional[_builtins.bool] = ...,
    registration_assignment_id: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegistrationAssignmentResult: ...
def get_registration_assignment_output(
    expand_registration_definition: Optional[
        pulumi.Input[Optional[_builtins.bool]]
    ] = ...,
    registration_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegistrationAssignmentResult]: ...
