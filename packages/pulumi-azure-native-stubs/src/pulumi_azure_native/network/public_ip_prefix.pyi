import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PublicIPPrefixArgs", "PublicIPPrefix"]

@pulumi.input_type
class PublicIPPrefixArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        custom_ip_prefix: Optional[pulumi.Input[SubResourceArgs]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway: Optional[pulumi.Input[NatGatewayArgs]] = ...,
        prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_prefix_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[PublicIPPrefixSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customIPPrefix")
    def custom_ip_prefix(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @custom_ip_prefix.setter
    def custom_ip_prefix(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]: ...
    @ip_tags.setter
    def ip_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> Optional[pulumi.Input[NatGatewayArgs]]: ...
    @nat_gateway.setter
    def nat_gateway(self, value: Optional[pulumi.Input[NatGatewayArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @prefix_length.setter
    def prefix_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]: ...
    @public_ip_address_version.setter
    def public_ip_address_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIpPrefixName")
    def public_ip_prefix_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_prefix_name.setter
    def public_ip_prefix_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[PublicIPPrefixSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[PublicIPPrefixSkuArgs]]): ...
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
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:PublicIPPrefix")
class PublicIPPrefix(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_ip_prefix: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[IpTagArgs, IpTagArgsDict]]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        nat_gateway: Optional[
            pulumi.Input[Union[NatGatewayArgs, NatGatewayArgsDict]]
        ] = ...,
        prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_prefix_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[
            pulumi.Input[Union[PublicIPPrefixSkuArgs, PublicIPPrefixSkuArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PublicIPPrefixArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PublicIPPrefix: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customIPPrefix")
    def custom_ip_prefix(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipPrefix")
    def ip_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> pulumi.Output[Optional[Sequence[outputs.IpTagResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerFrontendIpConfiguration")
    def load_balancer_frontend_ip_configuration(
        self,
    ) -> pulumi.Output[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Output[Optional[outputs.NatGatewayResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddresses")
    def public_ip_addresses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReferencedPublicIpAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.PublicIPPrefixSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
