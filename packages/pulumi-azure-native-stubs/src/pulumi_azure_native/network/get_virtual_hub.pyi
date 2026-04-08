import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualHubResult",
    "AwaitableGetVirtualHubResult",
    "get_virtual_hub",
    "get_virtual_hub_output",
]

@pulumi.output_type
class GetVirtualHubResult:
    def __init__(
        __self__,
        address_prefix=...,
        allow_branch_to_branch_traffic=...,
        azure_api_version=...,
        azure_firewall=...,
        bgp_connections=...,
        etag=...,
        express_route_gateway=...,
        hub_routing_preference=...,
        id=...,
        ip_configurations=...,
        kind=...,
        location=...,
        name=...,
        p2_s_vpn_gateway=...,
        preferred_routing_gateway=...,
        provisioning_state=...,
        route_maps=...,
        route_table=...,
        routing_state=...,
        security_partner_provider=...,
        security_provider_name=...,
        sku=...,
        tags=...,
        type=...,
        virtual_hub_route_table_v2s=...,
        virtual_router_asn=...,
        virtual_router_auto_scale_configuration=...,
        virtual_router_ips=...,
        virtual_wan=...,
        vpn_gateway=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="bgpConnections")
    def bgp_connections(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hubRoutingPreference")
    def hub_routing_preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="preferredRoutingGateway")
    def preferred_routing_gateway(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routeMaps")
    def route_maps(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional[outputs.VirtualHubRouteTableResponse]: ...
    @_builtins.property
    @pulumi.getter(name="routingState")
    def routing_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityPartnerProvider")
    def security_partner_provider(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(
        self,
    ) -> Optional[Sequence[outputs.VirtualHubRouteTableV2Response]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterAutoScaleConfiguration")
    def virtual_router_auto_scale_configuration(
        self,
    ) -> Optional[outputs.VirtualRouterAutoScaleConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional[outputs.SubResourceResponse]: ...

class AwaitableGetVirtualHubResult(GetVirtualHubResult):
    def __await__(self): ...

def get_virtual_hub(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_hub_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualHubResult: ...
def get_virtual_hub_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualHubResult]: ...
