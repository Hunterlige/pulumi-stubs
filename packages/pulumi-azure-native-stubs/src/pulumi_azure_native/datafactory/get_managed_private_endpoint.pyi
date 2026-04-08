import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedPrivateEndpointResult",
    "AwaitableGetManagedPrivateEndpointResult",
    "get_managed_private_endpoint",
    "get_managed_private_endpoint_output",
]

@pulumi.output_type
class GetManagedPrivateEndpointResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        properties=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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
    @pulumi.getter
    def properties(self) -> outputs.ManagedPrivateEndpointResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetManagedPrivateEndpointResult(GetManagedPrivateEndpointResult):
    def __await__(self): ...

def get_managed_private_endpoint(
    factory_name: Optional[_builtins.str] = ...,
    managed_private_endpoint_name: Optional[_builtins.str] = ...,
    managed_virtual_network_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedPrivateEndpointResult: ...
def get_managed_private_endpoint_output(
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedPrivateEndpointResult]: ...
