import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TransitGatewayArgs", "TransitGateway"]

@pulumi.input_type
class TransitGatewayArgs:
    def __init__(
        __self__,
        *,
        amazon_side_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        auto_accept_shared_attachments: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_association: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_support: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_support: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_support: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpn_ecmp_support: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @amazon_side_asn.setter
    def amazon_side_asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableAssociation")
    def default_route_table_association(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_route_table_association.setter
    def default_route_table_association(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTablePropagation")
    def default_route_table_propagation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_route_table_propagation.setter
    def default_route_table_propagation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_support.setter
    def dns_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSupport")
    def encryption_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_support.setter
    def encryption_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multicastSupport")
    def multicast_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_support.setter
    def multicast_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_group_referencing_support.setter
    def security_group_referencing_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayCidrBlocks")
    def transit_gateway_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @transit_gateway_cidr_blocks.setter
    def transit_gateway_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_ecmp_support.setter
    def vpn_ecmp_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TransitGatewayState:
    def __init__(
        __self__,
        *,
        amazon_side_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_accept_shared_attachments: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_association: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_support: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_support: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_support: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        propagation_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpn_ecmp_support: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @amazon_side_asn.setter
    def amazon_side_asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationDefaultRouteTableId")
    def association_default_route_table_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_default_route_table_id.setter
    def association_default_route_table_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableAssociation")
    def default_route_table_association(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_route_table_association.setter
    def default_route_table_association(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTablePropagation")
    def default_route_table_propagation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_route_table_propagation.setter
    def default_route_table_propagation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_support.setter
    def dns_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSupport")
    def encryption_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_support.setter
    def encryption_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multicastSupport")
    def multicast_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_support.setter
    def multicast_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propagationDefaultRouteTableId")
    def propagation_default_route_table_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagation_default_route_table_id.setter
    def propagation_default_route_table_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_group_referencing_support.setter
    def security_group_referencing_support(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayCidrBlocks")
    def transit_gateway_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @transit_gateway_cidr_blocks.setter
    def transit_gateway_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpn_ecmp_support.setter
    def vpn_ecmp_support(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class TransitGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        amazon_side_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        auto_accept_shared_attachments: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_association: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_support: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_support: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_support: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpn_ecmp_support: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[TransitGatewayArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        amazon_side_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_accept_shared_attachments: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_association: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_support: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_support: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_support: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        propagation_default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_referencing_support: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpn_ecmp_support: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TransitGateway: ...
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationDefaultRouteTableId")
    def association_default_route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableAssociation")
    def default_route_table_association(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTablePropagation")
    def default_route_table_propagation(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSupport")
    def dns_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSupport")
    def encryption_support(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multicastSupport")
    def multicast_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagationDefaultRouteTableId")
    def propagation_default_route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupReferencingSupport")
    def security_group_referencing_support(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayCidrBlocks")
    def transit_gateway_cidr_blocks(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> pulumi.Output[Optional[_builtins.str]]: ...
