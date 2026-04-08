import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNetworkSubnetResult",
    "AwaitableGetVirtualNetworkSubnetResult",
    "get_virtual_network_subnet",
    "get_virtual_network_subnet_output",
]

@pulumi.output_type
class GetVirtualNetworkSubnetResult:
    def __init__(
        __self__,
        azure_api_version=...,
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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.VirtualNetworkSubnetPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualNetworkSubnetResult(GetVirtualNetworkSubnetResult):
    def __await__(self): ...

def get_virtual_network_subnet(
    resource_group_name: Optional[_builtins.str] = ...,
    subnet_name: Optional[_builtins.str] = ...,
    virtual_network_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkSubnetResult: ...
def get_virtual_network_subnet_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkSubnetResult]: ...
