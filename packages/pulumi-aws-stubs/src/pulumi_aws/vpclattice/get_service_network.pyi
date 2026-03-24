import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceNetworkResult",
    "AwaitableGetServiceNetworkResult",
    "get_service_network",
    "get_service_network_output",
]

@pulumi.output_type
class GetServiceNetworkResult:
    def __init__(
        __self__,
        arn=...,
        auth_type=...,
        created_at=...,
        id=...,
        last_updated_at=...,
        name=...,
        number_of_associated_services=...,
        number_of_associated_vpcs=...,
        region=...,
        service_network_identifier=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfAssociatedServices")
    def number_of_associated_services(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="numberOfAssociatedVpcs")
    def number_of_associated_vpcs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetServiceNetworkResult(GetServiceNetworkResult):
    def __await__(self): ...

def get_service_network(
    region: Optional[_builtins.str] = ...,
    service_network_identifier: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceNetworkResult: ...
def get_service_network_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceNetworkResult]: ...
