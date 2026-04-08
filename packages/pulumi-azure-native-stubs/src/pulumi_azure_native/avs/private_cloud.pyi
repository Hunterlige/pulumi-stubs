import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateCloudArgs", "PrivateCloud"]

@pulumi.input_type
class PrivateCloudArgs:
    def __init__(
        __self__,
        *,
        management_cluster: pulumi.Input[ManagementClusterArgs],
        network_block: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        availability: Optional[pulumi.Input[AvailabilityPropertiesArgs]] = ...,
        dns_zone_type: Optional[pulumi.Input[Union[_builtins.str, DnsZoneType]]] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        extended_network_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        identity: Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]] = ...,
        identity_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[IdentitySourceArgs]]]
        ] = ...,
        internet: Optional[pulumi.Input[Union[_builtins.str, InternetEnum]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        nsxt_password: Optional[pulumi.Input[_builtins.str]] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vcenter_password: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(self) -> pulumi.Input[ManagementClusterArgs]: ...
    @management_cluster.setter
    def management_cluster(self, value: pulumi.Input[ManagementClusterArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkBlock")
    def network_block(self) -> pulumi.Input[_builtins.str]: ...
    @network_block.setter
    def network_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input[AvailabilityPropertiesArgs]]: ...
    @availability.setter
    def availability(
        self, value: Optional[pulumi.Input[AvailabilityPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsZoneType")
    def dns_zone_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DnsZoneType]]]: ...
    @dns_zone_type.setter
    def dns_zone_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DnsZoneType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedNetworkBlocks")
    def extended_network_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @extended_network_blocks.setter
    def extended_network_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySourceArgs]]]]: ...
    @identity_sources.setter
    def identity_sources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def internet(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InternetEnum]]]: ...
    @internet.setter
    def internet(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InternetEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nsxtPassword")
    def nsxt_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nsxt_password.setter
    def nsxt_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_cloud_name.setter
    def private_cloud_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vcenterPassword")
    def vcenter_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vcenter_password.setter
    def vcenter_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:avs:PrivateCloud")
class PrivateCloud(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        availability: Optional[
            pulumi.Input[
                Union[AvailabilityPropertiesArgs, AvailabilityPropertiesArgsDict]
            ]
        ] = ...,
        dns_zone_type: Optional[pulumi.Input[Union[_builtins.str, DnsZoneType]]] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionArgs, EncryptionArgsDict]]
        ] = ...,
        extended_network_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    SystemAssignedServiceIdentityArgs,
                    SystemAssignedServiceIdentityArgsDict,
                ]
            ]
        ] = ...,
        identity_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[IdentitySourceArgs, IdentitySourceArgsDict]]
                ]
            ]
        ] = ...,
        internet: Optional[pulumi.Input[Union[_builtins.str, InternetEnum]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management_cluster: Optional[
            pulumi.Input[Union[ManagementClusterArgs, ManagementClusterArgsDict]]
        ] = ...,
        network_block: Optional[pulumi.Input[_builtins.str]] = ...,
        nsxt_password: Optional[pulumi.Input[_builtins.str]] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vcenter_password: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateCloudArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PrivateCloud: ...
    @_builtins.property
    @pulumi.getter
    def availability(
        self,
    ) -> pulumi.Output[Optional[outputs.AvailabilityPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def circuit(self) -> pulumi.Output[Optional[outputs.CircuitResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsZoneType")
    def dns_zone_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[outputs.EncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[outputs.EndpointsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="extendedNetworkBlocks")
    def extended_network_blocks(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="externalCloudLinks")
    def external_cloud_links(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.SystemAssignedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.IdentitySourceResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def internet(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(
        self,
    ) -> pulumi.Output[outputs.ManagementClusterResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managementNetwork")
    def management_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkBlock")
    def network_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nsxPublicIpQuotaRaised")
    def nsx_public_ip_quota_raised(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nsxtCertificateThumbprint")
    def nsxt_certificate_thumbprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nsxtPassword")
    def nsxt_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningNetwork")
    def provisioning_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryCircuit")
    def secondary_circuit(self) -> pulumi.Output[Optional[outputs.CircuitResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vcenterCertificateThumbprint")
    def vcenter_certificate_thumbprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vcenterPassword")
    def vcenter_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmotionNetwork")
    def vmotion_network(self) -> pulumi.Output[_builtins.str]: ...
