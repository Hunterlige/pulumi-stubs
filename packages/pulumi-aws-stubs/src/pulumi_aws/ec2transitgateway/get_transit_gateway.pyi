import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTransitGatewayResult",
    "AwaitableGetTransitGatewayResult",
    "get_transit_gateway",
    "get_transit_gateway_output",
]

@pulumi.output_type
class GetTransitGatewayResult:
    def __init__(
        __self__,
        amazon_side_asn=...,
        arn=...,
        association_default_route_table_id=...,
        auto_accept_shared_attachments=...,
        default_route_table_association=...,
        default_route_table_propagation=...,
        description=...,
        dns_support=...,
        encryption_support=...,
        filters=...,
        id=...,
        multicast_support=...,
        owner_id=...,
        propagation_default_route_table_id=...,
        region=...,
        security_group_referencing_support=...,
        tags=...,
        transit_gateway_cidr_blocks=...,
        vpn_ecmp_support=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associationDefaultRouteTableId")
    def association_default_route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableAssociation")
    def default_route_table_association(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTablePropagation")
    def default_route_table_propagation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSupport")
    def encryption_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetTransitGatewayFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multicastSupport")
    def multicast_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="propagationDefaultRouteTableId")
    def propagation_default_route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayCidrBlocks")
    def transit_gateway_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> _builtins.str: ...

class AwaitableGetTransitGatewayResult(GetTransitGatewayResult):
    def __await__(self): ...

def get_transit_gateway(
    filters: Optional[
        Sequence[Union[GetTransitGatewayFilterArgs, GetTransitGatewayFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTransitGatewayResult: ...
def get_transit_gateway_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetTransitGatewayFilterArgs, GetTransitGatewayFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTransitGatewayResult]: ...
