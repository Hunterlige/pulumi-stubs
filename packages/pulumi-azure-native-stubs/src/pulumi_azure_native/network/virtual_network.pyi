import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualNetworkInitArgs", "VirtualNetwork"]

@pulumi.input_type
class VirtualNetworkInitArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        address_space: Optional[pulumi.Input[AddressSpaceArgs]] = ...,
        bgp_communities: Optional[pulumi.Input[VirtualNetworkBgpCommunitiesArgs]] = ...,
        ddos_protection_plan: Optional[pulumi.Input[SubResourceArgs]] = ...,
        dhcp_options: Optional[pulumi.Input[DhcpOptionsArgs]] = ...,
        enable_ddos_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vm_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[pulumi.Input[VirtualNetworkEncryptionArgs]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        flow_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_allocations: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_v_net_policies: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointVNetPolicies]]
        ] = ...,
        subnets: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_peerings: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPeeringArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[pulumi.Input[AddressSpaceArgs]]: ...
    @address_space.setter
    def address_space(self, value: Optional[pulumi.Input[AddressSpaceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpCommunities")
    def bgp_communities(
        self,
    ) -> Optional[pulumi.Input[VirtualNetworkBgpCommunitiesArgs]]: ...
    @bgp_communities.setter
    def bgp_communities(
        self, value: Optional[pulumi.Input[VirtualNetworkBgpCommunitiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionPlan")
    def ddos_protection_plan(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @ddos_protection_plan.setter
    def ddos_protection_plan(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional[pulumi.Input[DhcpOptionsArgs]]: ...
    @dhcp_options.setter
    def dhcp_options(self, value: Optional[pulumi.Input[DhcpOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDdosProtection")
    def enable_ddos_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ddos_protection.setter
    def enable_ddos_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVmProtection")
    def enable_vm_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vm_protection.setter
    def enable_vm_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[VirtualNetworkEncryptionArgs]]: ...
    @encryption.setter
    def encryption(
        self, value: Optional[pulumi.Input[VirtualNetworkEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flowTimeoutInMinutes")
    def flow_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @flow_timeout_in_minutes.setter
    def flow_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAllocations")
    def ip_allocations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @ip_allocations.setter
    def ip_allocations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointVNetPolicies")
    def private_endpoint_v_net_policies(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointVNetPolicies]]]: ...
    @private_endpoint_v_net_policies.setter
    def private_endpoint_v_net_policies(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointVNetPolicies]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]]: ...
    @subnets.setter
    def subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetArgs]]]]
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
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_name.setter
    def virtual_network_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkPeerings")
    def virtual_network_peerings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPeeringArgs]]]]: ...
    @virtual_network_peerings.setter
    def virtual_network_peerings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkPeeringArgs]]]
        ],
    ): ...

@pulumi.type_token("azure-native:network:VirtualNetwork")
class VirtualNetwork(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_space: Optional[
            pulumi.Input[Union[AddressSpaceArgs, AddressSpaceArgsDict]]
        ] = ...,
        bgp_communities: Optional[
            pulumi.Input[
                Union[
                    VirtualNetworkBgpCommunitiesArgs,
                    VirtualNetworkBgpCommunitiesArgsDict,
                ]
            ]
        ] = ...,
        ddos_protection_plan: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        dhcp_options: Optional[
            pulumi.Input[Union[DhcpOptionsArgs, DhcpOptionsArgsDict]]
        ] = ...,
        enable_ddos_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vm_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[
            pulumi.Input[
                Union[VirtualNetworkEncryptionArgs, VirtualNetworkEncryptionArgsDict]
            ]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        flow_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_allocations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_v_net_policies: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointVNetPolicies]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[SubnetArgs, SubnetArgsDict]]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_peerings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VirtualNetworkPeeringArgs, VirtualNetworkPeeringArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualNetworkInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualNetwork: ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(
        self,
    ) -> pulumi.Output[Optional[outputs.AddressSpaceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpCommunities")
    def bgp_communities(
        self,
    ) -> pulumi.Output[Optional[outputs.VirtualNetworkBgpCommunitiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionPlan")
    def ddos_protection_plan(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> pulumi.Output[Optional[outputs.DhcpOptionsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDdosProtection")
    def enable_ddos_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableVmProtection")
    def enable_vm_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.VirtualNetworkEncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="flowLogs")
    def flow_logs(self) -> pulumi.Output[Sequence[outputs.FlowLogResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="flowTimeoutInMinutes")
    def flow_timeout_in_minutes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAllocations")
    def ip_allocations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SubResourceResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointVNetPolicies")
    def private_endpoint_v_net_policies(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence[outputs.SubnetResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkPeerings")
    def virtual_network_peerings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.VirtualNetworkPeeringResponse]]]: ...
