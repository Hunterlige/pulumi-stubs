

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkGatewayResult', 'AwaitableGetVirtualNetworkGatewayResult', 'get_virtual_network_gateway', 'get_virtual_network_gateway_output']
@pulumi.output_type
class GetVirtualNetworkGatewayResult:
    
    def __init__(__self__, active_active=..., admin_state=..., allow_remote_vnet_traffic=..., allow_virtual_wan_traffic=..., auto_scale_configuration=..., azure_api_version=..., bgp_settings=..., custom_routes=..., disable_ip_sec_replay_protection=..., enable_bgp=..., enable_bgp_route_translation_for_nat=..., enable_dns_forwarding=..., enable_private_ip_address=..., etag=..., extended_location=..., gateway_default_site=..., gateway_type=..., id=..., identity=..., inbound_dns_forwarding_endpoint=..., ip_configurations=..., location=..., name=..., nat_rules=..., provisioning_state=..., resiliency_model=..., resource_guid=..., sku=..., tags=..., type=..., v_net_extended_location_resource_id=..., virtual_network_gateway_policy_groups=..., vpn_client_configuration=..., vpn_gateway_generation=..., vpn_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeActive")
    def active_active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminState")
    def admin_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVnetTraffic")
    def allow_remote_vnet_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVirtualWanTraffic")
    def allow_virtual_wan_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> Optional[outputs.VirtualNetworkGatewayAutoScaleConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[outputs.BgpSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRoutes")
    def custom_routes(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableIPSecReplayProtection")
    def disable_ip_sec_replay_protection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBgpRouteTranslationForNat")
    def enable_bgp_route_translation_for_nat(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDnsForwarding")
    def enable_dns_forwarding(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateIpAddress")
    def enable_private_ip_address(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayDefaultSite")
    def gateway_default_site(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundDnsForwardingEndpoint")
    def inbound_dns_forwarding_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence[outputs.VirtualNetworkGatewayIPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natRules")
    def nat_rules(self) -> Optional[Sequence[outputs.VirtualNetworkGatewayNatRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resiliencyModel")
    def resiliency_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.VirtualNetworkGatewaySkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vNetExtendedLocationResourceId")
    def v_net_extended_location_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkGatewayPolicyGroups")
    def virtual_network_gateway_policy_groups(self) -> Optional[Sequence[outputs.VirtualNetworkGatewayPolicyGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnClientConfiguration")
    def vpn_client_configuration(self) -> Optional[outputs.VpnClientConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGatewayGeneration")
    def vpn_gateway_generation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnType")
    def vpn_type(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualNetworkGatewayResult(GetVirtualNetworkGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkGatewayResult]:
        ...
    


def get_virtual_network_gateway(resource_group_name: Optional[_builtins.str] = ..., virtual_network_gateway_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkGatewayResult:
    
    ...

def get_virtual_network_gateway_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkGatewayResult]:
    
    ...

