import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkloadResult",
    "AwaitableGetWorkloadResult",
    "get_workload",
    "get_workload_output",
]

@pulumi.output_type
class GetWorkloadResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        managed_on_behalf_of_configuration=...,
        name=...,
        provisioning_state=...,
        resource_group_collection=...,
        system_data=...,
        tags=...,
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
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(
        self,
    ) -> outputs.ManagedOnBehalfOfConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupCollection")
    def resource_group_collection(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWorkloadResult(GetWorkloadResult):
    def __await__(self): ...

def get_workload(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_enclave_name: Optional[_builtins.str] = ...,
    workload_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkloadResult: ...
def get_workload_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_enclave_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workload_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkloadResult]: ...
