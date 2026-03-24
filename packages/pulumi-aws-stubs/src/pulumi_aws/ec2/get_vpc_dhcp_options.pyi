import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcDhcpOptionsResult",
    "AwaitableGetVpcDhcpOptionsResult",
    "get_vpc_dhcp_options",
    "get_vpc_dhcp_options_output",
]

@pulumi.output_type
class GetVpcDhcpOptionsResult:
    def __init__(
        __self__,
        arn=...,
        dhcp_options_id=...,
        domain_name=...,
        domain_name_servers=...,
        filters=...,
        id=...,
        ipv6_address_preferred_lease_time=...,
        netbios_name_servers=...,
        netbios_node_type=...,
        ntp_servers=...,
        owner_id=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainNameServers")
    def domain_name_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcDhcpOptionsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AddressPreferredLeaseTime")
    def ipv6_address_preferred_lease_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="netbiosNameServers")
    def netbios_name_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="netbiosNodeType")
    def netbios_node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetVpcDhcpOptionsResult(GetVpcDhcpOptionsResult):
    def __await__(self): ...

def get_vpc_dhcp_options(
    dhcp_options_id: Optional[_builtins.str] = ...,
    filters: Optional[
        Sequence[Union[GetVpcDhcpOptionsFilterArgs, GetVpcDhcpOptionsFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcDhcpOptionsResult: ...
def get_vpc_dhcp_options_output(
    dhcp_options_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetVpcDhcpOptionsFilterArgs, GetVpcDhcpOptionsFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcDhcpOptionsResult]: ...
