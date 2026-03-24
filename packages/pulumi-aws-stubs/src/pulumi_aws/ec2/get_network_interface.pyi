import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkInterfaceResult",
    "AwaitableGetNetworkInterfaceResult",
    "get_network_interface",
    "get_network_interface_output",
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    def __init__(
        __self__,
        arn=...,
        associations=...,
        attachments=...,
        availability_zone=...,
        description=...,
        filters=...,
        id=...,
        interface_type=...,
        ipv6_addresses=...,
        mac_address=...,
        outpost_arn=...,
        owner_id=...,
        private_dns_name=...,
        private_ip=...,
        private_ips=...,
        region=...,
        requester_id=...,
        security_groups=...,
        subnet_id=...,
        tags=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def associations(
        self,
    ) -> Sequence[outputs.GetNetworkInterfaceAssociationResult]: ...
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Sequence[outputs.GetNetworkInterfaceAttachmentResult]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetNetworkInterfaceFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsName")
    def private_dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requesterId")
    def requester_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    def __await__(self): ...

def get_network_interface(
    filters: Optional[
        Sequence[
            Union[GetNetworkInterfaceFilterArgs, GetNetworkInterfaceFilterArgsDict]
        ]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkInterfaceResult: ...
def get_network_interface_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetNetworkInterfaceFilterArgs, GetNetworkInterfaceFilterArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkInterfaceResult]: ...
