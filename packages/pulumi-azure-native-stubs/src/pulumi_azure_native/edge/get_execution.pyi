import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExecutionResult",
    "AwaitableGetExecutionResult",
    "get_execution",
    "get_execution_output",
]

@pulumi.output_type
class GetExecutionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        extended_location=...,
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
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> Optional[outputs.AzureResourceManagerCommonTypesExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ExecutionPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetExecutionResult(GetExecutionResult):
    def __await__(self): ...

def get_execution(
    context_name: Optional[_builtins.str] = ...,
    execution_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    version_name: Optional[_builtins.str] = ...,
    workflow_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExecutionResult: ...
def get_execution_output(
    context_name: Optional[pulumi.Input[_builtins.str]] = ...,
    execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExecutionResult]: ...
