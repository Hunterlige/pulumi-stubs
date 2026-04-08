import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStandardAssignmentResult",
    "AwaitableGetStandardAssignmentResult",
    "get_standard_assignment",
    "get_standard_assignment_output",
]

@pulumi.output_type
class GetStandardAssignmentResult:
    def __init__(
        __self__,
        assigned_standard=...,
        attestation_data=...,
        azure_api_version=...,
        description=...,
        display_name=...,
        effect=...,
        excluded_scopes=...,
        exemption_data=...,
        expires_on=...,
        id=...,
        metadata=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> Optional[outputs.AssignedStandardItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="attestationData")
    def attestation_data(
        self,
    ) -> Optional[outputs.StandardAssignmentPropertiesResponseAttestationData]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedScopes")
    def excluded_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exemptionData")
    def exemption_data(
        self,
    ) -> Optional[outputs.StandardAssignmentPropertiesResponseExemptionData]: ...
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.StandardAssignmentMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetStandardAssignmentResult(GetStandardAssignmentResult):
    def __await__(self): ...

def get_standard_assignment(
    resource_id: Optional[_builtins.str] = ...,
    standard_assignment_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStandardAssignmentResult: ...
def get_standard_assignment_output(
    resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    standard_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStandardAssignmentResult]: ...
