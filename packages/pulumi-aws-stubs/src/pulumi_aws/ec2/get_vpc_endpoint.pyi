import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcEndpointResult",
    "AwaitableGetVpcEndpointResult",
    "get_vpc_endpoint",
    "get_vpc_endpoint_output",
]

@pulumi.output_type
class GetVpcEndpointResult:
    def __init__(
        __self__,
        arn=...,
        cidr_blocks=...,
        dns_entries=...,
        dns_options=...,
        filters=...,
        id=...,
        ip_address_type=...,
        network_interface_ids=...,
        owner_id=...,
        policy=...,
        prefix_list_id=...,
        private_dns_enabled=...,
        region=...,
        requester_managed=...,
        route_table_ids=...,
        security_group_ids=...,
        service_name=...,
        service_region=...,
        state=...,
        subnet_ids=...,
        tags=...,
        vpc_endpoint_type=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> Sequence[outputs.GetVpcEndpointDnsEntryResult]: ...
    @_builtins.property
    @pulumi.getter(name="dnsOptions")
    def dns_options(self) -> Sequence[outputs.GetVpcEndpointDnsOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcEndpointFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requesterManaged")
    def requester_managed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRegion")
    def service_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetVpcEndpointResult(GetVpcEndpointResult):
    def __await__(self): ...

def get_vpc_endpoint(
    filters: Optional[
        Sequence[Union[GetVpcEndpointFilterArgs, GetVpcEndpointFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    service_region: Optional[_builtins.str] = ...,
    state: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    vpc_endpoint_type: Optional[_builtins.str] = ...,
    vpc_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcEndpointResult: ...
def get_vpc_endpoint_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetVpcEndpointFilterArgs, GetVpcEndpointFilterArgsDict]]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    state: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    vpc_endpoint_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcEndpointResult]: ...
