import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityStandardResult",
    "AwaitableGetSecurityStandardResult",
    "get_security_standard",
    "get_security_standard_output",
]

@pulumi.output_type
class GetSecurityStandardResult:
    def __init__(
        __self__,
        assessments=...,
        azure_api_version=...,
        cloud_providers=...,
        description=...,
        display_name=...,
        id=...,
        metadata=...,
        name=...,
        policy_set_definition_id=...,
        standard_type=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assessments(
        self,
    ) -> Optional[Sequence[outputs.PartialAssessmentPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudProviders")
    def cloud_providers(self) -> Optional[Sequence[_builtins.str]]: ...
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
    def metadata(self) -> Optional[outputs.StandardMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policySetDefinitionId")
    def policy_set_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standardType")
    def standard_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSecurityStandardResult(GetSecurityStandardResult):
    def __await__(self): ...

def get_security_standard(
    scope: Optional[_builtins.str] = ...,
    standard_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityStandardResult: ...
def get_security_standard_output(
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    standard_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityStandardResult]: ...
