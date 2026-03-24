import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSubnetworkResult",
    "AwaitableGetSubnetworkResult",
    "get_subnetwork",
    "get_subnetwork_output",
]

@pulumi.output_type
class GetSubnetworkResult:
    def __init__(
        __self__,
        description=...,
        external_ipv6_prefix=...,
        gateway_address=...,
        id=...,
        internal_ipv6_prefix=...,
        ip_cidr_range=...,
        ipv6_access_type=...,
        name=...,
        network=...,
        private_ip_google_access=...,
        project=...,
        region=...,
        secondary_ip_ranges=...,
        self_link=...,
        stack_type=...,
        subnetwork_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gatewayAddress")
    def gateway_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internalIpv6Prefix")
    def internal_ipv6_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(
        self,
    ) -> Sequence[outputs.GetSubnetworkSecondaryIpRangeResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetworkId")
    def subnetwork_id(self) -> _builtins.int: ...

class AwaitableGetSubnetworkResult(GetSubnetworkResult):
    def __await__(self): ...

def get_subnetwork(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSubnetworkResult: ...
def get_subnetwork_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSubnetworkResult]: ...
