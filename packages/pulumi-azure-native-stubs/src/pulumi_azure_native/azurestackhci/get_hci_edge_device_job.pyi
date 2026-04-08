import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHciEdgeDeviceJobResult",
    "AwaitableGetHciEdgeDeviceJobResult",
    "get_hci_edge_device_job",
    "get_hci_edge_device_job_output",
]

@pulumi.output_type
class GetHciEdgeDeviceJobResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        kind=...,
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
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetHciEdgeDeviceJobResult(GetHciEdgeDeviceJobResult):
    def __await__(self): ...

def get_hci_edge_device_job(
    edge_device_name: Optional[_builtins.str] = ...,
    jobs_name: Optional[_builtins.str] = ...,
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHciEdgeDeviceJobResult: ...
def get_hci_edge_device_job_output(
    edge_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    jobs_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHciEdgeDeviceJobResult]: ...
