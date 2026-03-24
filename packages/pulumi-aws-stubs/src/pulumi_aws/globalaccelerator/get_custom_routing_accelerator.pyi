import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomRoutingAcceleratorResult",
    "AwaitableGetCustomRoutingAcceleratorResult",
    "get_custom_routing_accelerator",
    "get_custom_routing_accelerator_output",
]

@pulumi.output_type
class GetCustomRoutingAcceleratorResult:
    def __init__(
        __self__,
        arn=...,
        attributes=...,
        dns_name=...,
        enabled=...,
        hosted_zone_id=...,
        id=...,
        ip_address_type=...,
        ip_sets=...,
        name=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Sequence[outputs.GetCustomRoutingAcceleratorAttributeResult]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipSets")
    def ip_sets(self) -> Sequence[outputs.GetCustomRoutingAcceleratorIpSetResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetCustomRoutingAcceleratorResult(GetCustomRoutingAcceleratorResult):
    def __await__(self): ...

def get_custom_routing_accelerator(
    arn: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCustomRoutingAcceleratorResult: ...
def get_custom_routing_accelerator_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomRoutingAcceleratorResult]: ...
