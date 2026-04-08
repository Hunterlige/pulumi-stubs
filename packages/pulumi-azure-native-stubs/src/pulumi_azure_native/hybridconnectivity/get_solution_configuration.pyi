import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSolutionConfigurationResult",
    "AwaitableGetSolutionConfigurationResult",
    "get_solution_configuration",
    "get_solution_configuration_output",
]

@pulumi.output_type
class GetSolutionConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        last_sync_time=...,
        name=...,
        provisioning_state=...,
        solution_settings=...,
        solution_type=...,
        status=...,
        status_details=...,
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
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="solutionSettings")
    def solution_settings(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSolutionConfigurationResult(GetSolutionConfigurationResult):
    def __await__(self): ...

def get_solution_configuration(
    resource_uri: Optional[_builtins.str] = ...,
    solution_configuration: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSolutionConfigurationResult: ...
def get_solution_configuration_output(
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    solution_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSolutionConfigurationResult]: ...
