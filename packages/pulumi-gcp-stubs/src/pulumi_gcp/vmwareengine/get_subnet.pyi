import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSubnetResult",
    "AwaitableGetSubnetResult",
    "get_subnet",
    "get_subnet_output",
]

@pulumi.output_type
class GetSubnetResult:
    def __init__(
        __self__,
        create_time=...,
        dhcp_address_ranges=...,
        gateway_id=...,
        gateway_ip=...,
        id=...,
        ip_cidr_range=...,
        name=...,
        parent=...,
        standard_config=...,
        state=...,
        type=...,
        uid=...,
        update_time=...,
        vlan_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dhcpAddressRanges")
    def dhcp_address_ranges(
        self,
    ) -> Sequence[outputs.GetSubnetDhcpAddressRangeResult]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standardConfig")
    def standard_config(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> _builtins.int: ...

class AwaitableGetSubnetResult(GetSubnetResult):
    def __await__(self): ...

def get_subnet(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSubnetResult: ...
def get_subnet_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSubnetResult]: ...
