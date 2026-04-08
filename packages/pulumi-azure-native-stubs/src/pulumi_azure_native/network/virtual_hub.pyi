import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualHubArgs", "VirtualHub"]

@pulumi.input_type
class VirtualHubArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_branch_to_branch_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        azure_firewall: Optional[pulumi.Input[SubResourceArgs]] = ...,
        express_route_gateway: Optional[pulumi.Input[SubResourceArgs]] = ...,
        hub_routing_preference: Optional[
            pulumi.Input[Union[_builtins.str, HubRoutingPreference]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        p2_s_vpn_gateway: Optional[pulumi.Input[SubResourceArgs]] = ...,
        preferred_routing_gateway: Optional[
            pulumi.Input[Union[_builtins.str, PreferredRoutingGateway]]
        ] = ...,
        route_table: Optional[pulumi.Input[VirtualHubRouteTableArgs]] = ...,
        security_partner_provider: Optional[pulumi.Input[SubResourceArgs]] = ...,
        security_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_hub_route_table_v2s: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualHubRouteTableV2Args]]]
        ] = ...,
        virtual_router_asn: Optional[pulumi.Input[_builtins.float]] = ...,
        virtual_router_auto_scale_configuration: Optional[
            pulumi.Input[VirtualRouterAutoScaleConfigurationArgs]
        ] = ...,
        virtual_router_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        virtual_wan: Optional[pulumi.Input[SubResourceArgs]] = ...,
        vpn_gateway: Optional[pulumi.Input[SubResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_branch_to_branch_traffic.setter
    def allow_branch_to_branch_traffic(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @azure_firewall.setter
    def azure_firewall(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @express_route_gateway.setter
    def express_route_gateway(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hubRoutingPreference")
    def hub_routing_preference(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HubRoutingPreference]]]: ...
    @hub_routing_preference.setter
    def hub_routing_preference(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HubRoutingPreference]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @p2_s_vpn_gateway.setter
    def p2_s_vpn_gateway(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredRoutingGateway")
    def preferred_routing_gateway(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PreferredRoutingGateway]]]: ...
    @preferred_routing_gateway.setter
    def preferred_routing_gateway(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PreferredRoutingGateway]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional[pulumi.Input[VirtualHubRouteTableArgs]]: ...
    @route_table.setter
    def route_table(self, value: Optional[pulumi.Input[VirtualHubRouteTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPartnerProvider")
    def security_partner_provider(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @security_partner_provider.setter
    def security_partner_provider(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_provider_name.setter
    def security_provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_hub_name.setter
    def virtual_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualHubRouteTableV2Args]]]]: ...
    @virtual_hub_route_table_v2s.setter
    def virtual_hub_route_table_v2s(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualHubRouteTableV2Args]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @virtual_router_asn.setter
    def virtual_router_asn(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAutoScaleConfiguration")
    def virtual_router_auto_scale_configuration(
        self,
    ) -> Optional[pulumi.Input[VirtualRouterAutoScaleConfigurationArgs]]: ...
    @virtual_router_auto_scale_configuration.setter
    def virtual_router_auto_scale_configuration(
        self, value: Optional[pulumi.Input[VirtualRouterAutoScaleConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @virtual_router_ips.setter
    def virtual_router_ips(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @virtual_wan.setter
    def virtual_wan(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @vpn_gateway.setter
    def vpn_gateway(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...

@pulumi.type_token("azure-native:network:VirtualHub")
class VirtualHub(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_branch_to_branch_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        azure_firewall: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        express_route_gateway: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        hub_routing_preference: Optional[
            pulumi.Input[Union[_builtins.str, HubRoutingPreference]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        p2_s_vpn_gateway: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        preferred_routing_gateway: Optional[
            pulumi.Input[Union[_builtins.str, PreferredRoutingGateway]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table: Optional[
            pulumi.Input[Union[VirtualHubRouteTableArgs, VirtualHubRouteTableArgsDict]]
        ] = ...,
        security_partner_provider: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        security_provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_hub_route_table_v2s: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VirtualHubRouteTableV2Args, VirtualHubRouteTableV2ArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        virtual_router_asn: Optional[pulumi.Input[_builtins.float]] = ...,
        virtual_router_auto_scale_configuration: Optional[
            pulumi.Input[
                Union[
                    VirtualRouterAutoScaleConfigurationArgs,
                    VirtualRouterAutoScaleConfigurationArgsDict,
                ]
            ]
        ] = ...,
        virtual_router_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        virtual_wan: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        vpn_gateway: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualHubArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualHub: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="bgpConnections")
    def bgp_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hubRoutingPreference")
    def hub_routing_preference(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="preferredRoutingGateway")
    def preferred_routing_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeMaps")
    def route_maps(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="routeTable")
    def route_table(
        self,
    ) -> pulumi.Output[Optional[outputs.VirtualHubRouteTableResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="routingState")
    def routing_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityPartnerProvider")
    def security_partner_provider(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.VirtualHubRouteTableV2Response]]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAutoScaleConfiguration")
    def virtual_router_auto_scale_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualRouterAutoScaleConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
