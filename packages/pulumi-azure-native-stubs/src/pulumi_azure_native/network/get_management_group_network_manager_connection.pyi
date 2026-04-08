import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagementGroupNetworkManagerConnectionResult",
    ...,
    "get_management_group_network_manager_connection",
    ...,
]

@pulumi.output_type
class GetManagementGroupNetworkManagerConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        etag=...,
        id=...,
        name=...,
        network_manager_id=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkManagerId")
    def network_manager_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetManagementGroupNetworkManagerConnectionResult(
    GetManagementGroupNetworkManagerConnectionResult
):
    def __await__(self): ...

def get_management_group_network_manager_connection(
    management_group_id: Optional[_builtins.str] = ...,
    network_manager_connection_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagementGroupNetworkManagerConnectionResult: ...
def get_management_group_network_manager_connection_output(
    management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    network_manager_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagementGroupNetworkManagerConnectionResult]: ...
