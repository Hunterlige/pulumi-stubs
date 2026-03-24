import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAddressResult",
    "AwaitableGetAddressResult",
    "get_address",
    "get_address_output",
]

@pulumi.output_type
class GetAddressResult:
    def __init__(
        __self__,
        address=...,
        address_type=...,
        id=...,
        name=...,
        network=...,
        network_tier=...,
        prefix_length=...,
        project=...,
        purpose=...,
        region=...,
        self_link=...,
        status=...,
        subnetwork=...,
        users=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addressType")
    def address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def users(self) -> _builtins.str: ...

class AwaitableGetAddressResult(GetAddressResult):
    def __await__(self): ...

def get_address(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAddressResult: ...
def get_address_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAddressResult]: ...
