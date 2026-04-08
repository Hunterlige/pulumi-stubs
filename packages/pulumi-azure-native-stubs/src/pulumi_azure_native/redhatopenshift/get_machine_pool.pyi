import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMachinePoolResult",
    "AwaitableGetMachinePoolResult",
    "get_machine_pool",
    "get_machine_pool_output",
]

@pulumi.output_type
class GetMachinePoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        resources=...,
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
    def resources(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMachinePoolResult(GetMachinePoolResult):
    def __await__(self): ...

def get_machine_pool(
    child_resource_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMachinePoolResult: ...
def get_machine_pool_output(
    child_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMachinePoolResult]: ...
