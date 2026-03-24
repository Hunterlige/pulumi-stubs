

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpnConnectionInitArgs', 'VpnConnection']
@pulumi.input_type
class VpnConnectionInitArgs:
    def __init__(__self__, *, gateway_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], connection_bandwidth: Optional[pulumi.Input[_builtins.int]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enable_bgp: Optional[pulumi.Input[_builtins.bool]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., enable_rate_limiting: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_policies: Optional[pulumi.Input[Sequence[pulumi.Input[IpsecPolicyArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remote_vpn_site: Optional[pulumi.Input[SubResourceArgs]] = ..., routing_configuration: Optional[pulumi.Input[RoutingConfigurationArgs]] = ..., routing_weight: Optional[pulumi.Input[_builtins.int]] = ..., shared_key: Optional[pulumi.Input[_builtins.str]] = ..., traffic_selector_policies: Optional[pulumi.Input[Sequence[pulumi.Input[TrafficSelectorPolicyArgs]]]] = ..., use_local_azure_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., use_policy_based_traffic_selectors: Optional[pulumi.Input[_builtins.bool]] = ..., vpn_connection_protocol_type: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkGatewayConnectionProtocol]]] = ..., vpn_link_connections: Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkConnectionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionBandwidth")
    def connection_bandwidth(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_bandwidth.setter
    def connection_bandwidth(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpdTimeoutSeconds")
    def dpd_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dpd_timeout_seconds.setter
    def dpd_timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_bgp.setter
    def enable_bgp(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_security.setter
    def enable_internet_security(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRateLimiting")
    def enable_rate_limiting(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_rate_limiting.setter
    def enable_rate_limiting(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipsecPolicies")
    def ipsec_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpsecPolicyArgs]]]]:
        
        ...
    
    @ipsec_policies.setter
    def ipsec_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpsecPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVpnSite")
    def remote_vpn_site(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @remote_vpn_site.setter
    def remote_vpn_site(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[pulumi.Input[RoutingConfigurationArgs]]:
        
        ...
    
    @routing_configuration.setter
    def routing_configuration(self, value: Optional[pulumi.Input[RoutingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @routing_weight.setter
    def routing_weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_key.setter
    def shared_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSelectorPolicies")
    def traffic_selector_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrafficSelectorPolicyArgs]]]]:
        
        ...
    
    @traffic_selector_policies.setter
    def traffic_selector_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TrafficSelectorPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLocalAzureIpAddress")
    def use_local_azure_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_local_azure_ip_address.setter
    def use_local_azure_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePolicyBasedTrafficSelectors")
    def use_policy_based_traffic_selectors(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_policy_based_traffic_selectors.setter
    def use_policy_based_traffic_selectors(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnectionProtocolType")
    def vpn_connection_protocol_type(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkGatewayConnectionProtocol]]]:
        
        ...
    
    @vpn_connection_protocol_type.setter
    def vpn_connection_protocol_type(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkGatewayConnectionProtocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnLinkConnections")
    def vpn_link_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkConnectionArgs]]]]:
        
        ...
    
    @vpn_link_connections.setter
    def vpn_link_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkConnectionArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:VpnConnection")
class VpnConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_bandwidth: Optional[pulumi.Input[_builtins.int]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., dpd_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., enable_bgp: Optional[pulumi.Input[_builtins.bool]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., enable_rate_limiting: Optional[pulumi.Input[_builtins.bool]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IpsecPolicyArgs, IpsecPolicyArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remote_vpn_site: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_configuration: Optional[pulumi.Input[Union[RoutingConfigurationArgs, RoutingConfigurationArgsDict]]] = ..., routing_weight: Optional[pulumi.Input[_builtins.int]] = ..., shared_key: Optional[pulumi.Input[_builtins.str]] = ..., traffic_selector_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TrafficSelectorPolicyArgs, TrafficSelectorPolicyArgsDict]]]]] = ..., use_local_azure_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., use_policy_based_traffic_selectors: Optional[pulumi.Input[_builtins.bool]] = ..., vpn_connection_protocol_type: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkGatewayConnectionProtocol]]] = ..., vpn_link_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpnSiteLinkConnectionArgs, VpnSiteLinkConnectionArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpnConnectionInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VpnConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionBandwidth")
    def connection_bandwidth(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dpdTimeoutSeconds")
    def dpd_timeout_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressBytesTransferred")
    def egress_bytes_transferred(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRateLimiting")
    def enable_rate_limiting(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressBytesTransferred")
    def ingress_bytes_transferred(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipsecPolicies")
    def ipsec_policies(self) -> pulumi.Output[Optional[Sequence[outputs.IpsecPolicyResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVpnSite")
    def remote_vpn_site(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> pulumi.Output[Optional[outputs.RoutingConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSelectorPolicies")
    def traffic_selector_policies(self) -> pulumi.Output[Optional[Sequence[outputs.TrafficSelectorPolicyResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLocalAzureIpAddress")
    def use_local_azure_ip_address(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePolicyBasedTrafficSelectors")
    def use_policy_based_traffic_selectors(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnectionProtocolType")
    def vpn_connection_protocol_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnLinkConnections")
    def vpn_link_connections(self) -> pulumi.Output[Optional[Sequence[outputs.VpnSiteLinkConnectionResponse]]]:
        
        ...
    


