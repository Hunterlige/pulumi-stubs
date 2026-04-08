import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkloadNetworkDhcpResult",
    "AwaitableGetWorkloadNetworkDhcpResult",
    "get_workload_network_dhcp",
    "get_workload_network_dhcp_output",
]

@pulumi.output_type
class GetWorkloadNetworkDhcpResult:
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
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWorkloadNetworkDhcpResult(GetWorkloadNetworkDhcpResult):
    def __await__(self): ...

def get_workload_network_dhcp(
    dhcp_id: Optional[_builtins.str] = ...,
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkloadNetworkDhcpResult: ...
def get_workload_network_dhcp_output(
    dhcp_id: Optional[pulumi.Input[_builtins.str]] = ...,
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkloadNetworkDhcpResult]: ...
