import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PublicIPAddressInitArgs", "PublicIPAddress"]

@pulumi.input_type
class PublicIPAddressInitArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        ddos_settings: Optional[pulumi.Input[DdosSettingsArgs]] = ...,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOptions]]
        ] = ...,
        dns_settings: Optional[pulumi.Input[PublicIPAddressDnsSettingsArgs]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]] = ...,
        linked_public_ip_address: Optional[pulumi.Input[PublicIPAddressArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_phase: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressMigrationPhase]]
        ] = ...,
        nat_gateway: Optional[pulumi.Input[NatGatewayArgs]] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
        ] = ...,
        public_ip_prefix: Optional[pulumi.Input[SubResourceArgs]] = ...,
        public_ip_address_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_public_ip_address: Optional[pulumi.Input[PublicIPAddressArgs]] = ...,
        sku: Optional[pulumi.Input[PublicIPAddressSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ddosSettings")
    def ddos_settings(self) -> Optional[pulumi.Input[DdosSettingsArgs]]: ...
    @ddos_settings.setter
    def ddos_settings(self, value: Optional[pulumi.Input[DdosSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]: ...
    @delete_option.setter
    def delete_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DeleteOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> Optional[pulumi.Input[PublicIPAddressDnsSettingsArgs]]: ...
    @dns_settings.setter
    def dns_settings(
        self, value: Optional[pulumi.Input[PublicIPAddressDnsSettingsArgs]]
    ): ...
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
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]: ...
    @ip_tags.setter
    def ip_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedPublicIPAddress")
    def linked_public_ip_address(
        self,
    ) -> Optional[pulumi.Input[PublicIPAddressArgs]]: ...
    @linked_public_ip_address.setter
    def linked_public_ip_address(
        self, value: Optional[pulumi.Input[PublicIPAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrationPhase")
    def migration_phase(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PublicIPAddressMigrationPhase]]
    ]: ...
    @migration_phase.setter
    def migration_phase(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressMigrationPhase]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> Optional[pulumi.Input[NatGatewayArgs]]: ...
    @nat_gateway.setter
    def nat_gateway(self, value: Optional[pulumi.Input[NatGatewayArgs]]): ...
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
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]: ...
    @public_ip_allocation_method.setter
    def public_ip_allocation_method(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @public_ip_prefix.setter
    def public_ip_prefix(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddressName")
    def public_ip_address_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_address_name.setter
    def public_ip_address_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servicePublicIPAddress")
    def service_public_ip_address(
        self,
    ) -> Optional[pulumi.Input[PublicIPAddressArgs]]: ...
    @service_public_ip_address.setter
    def service_public_ip_address(
        self, value: Optional[pulumi.Input[PublicIPAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[PublicIPAddressSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[PublicIPAddressSkuArgs]]): ...
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

@pulumi.type_token("azure-native:network:PublicIPAddress")
class PublicIPAddress(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ddos_settings: Optional[
            pulumi.Input[Union[DdosSettingsArgs, DdosSettingsArgsDict]]
        ] = ...,
        delete_option: Optional[
            pulumi.Input[Union[_builtins.str, DeleteOptions]]
        ] = ...,
        dns_settings: Optional[
            pulumi.Input[
                Union[
                    PublicIPAddressDnsSettingsArgs, PublicIPAddressDnsSettingsArgsDict
                ]
            ]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[IpTagArgs, IpTagArgsDict]]]]
        ] = ...,
        linked_public_ip_address: Optional[
            pulumi.Input[Union[PublicIPAddressArgs, PublicIPAddressArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_phase: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressMigrationPhase]]
        ] = ...,
        nat_gateway: Optional[
            pulumi.Input[Union[NatGatewayArgs, NatGatewayArgsDict]]
        ] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, IPVersion]]
        ] = ...,
        public_ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
        ] = ...,
        public_ip_prefix: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        public_ip_address_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_public_ip_address: Optional[
            pulumi.Input[Union[PublicIPAddressArgs, PublicIPAddressArgsDict]]
        ] = ...,
        sku: Optional[
            pulumi.Input[Union[PublicIPAddressSkuArgs, PublicIPAddressSkuArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PublicIPAddressInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PublicIPAddress: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ddosSettings")
    def ddos_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.DdosSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteOption")
    def delete_option(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.PublicIPAddressDnsSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> pulumi.Output[outputs.IPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> pulumi.Output[Optional[Sequence[outputs.IpTagResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedPublicIPAddress")
    def linked_public_ip_address(
        self,
    ) -> pulumi.Output[Optional[outputs.PublicIPAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationPhase")
    def migration_phase(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Output[Optional[outputs.NatGatewayResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAllocationMethod")
    def public_ip_allocation_method(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPPrefix")
    def public_ip_prefix(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePublicIPAddress")
    def service_public_ip_address(
        self,
    ) -> pulumi.Output[Optional[outputs.PublicIPAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.PublicIPAddressSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
