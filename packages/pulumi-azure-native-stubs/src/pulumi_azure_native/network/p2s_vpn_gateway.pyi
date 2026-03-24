

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['P2sVpnGatewayArgs', 'P2sVpnGateway']
@pulumi.input_type
class P2sVpnGatewayArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], custom_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., is_routing_preference_internet: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., p2_s_connection_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[P2SConnectionConfigurationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_hub: Optional[pulumi.Input[SubResourceArgs]] = ..., vpn_gateway_scale_unit: Optional[pulumi.Input[_builtins.int]] = ..., vpn_server_configuration: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDnsServers")
    def custom_dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_dns_servers.setter
    def custom_dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_routing_preference_internet.setter
    def is_routing_preference_internet(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[P2SConnectionConfigurationArgs]]]]:
        
        ...
    
    @p2_s_connection_configurations.setter
    def p2_s_connection_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[P2SConnectionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vpn_gateway_scale_unit.setter
    def vpn_gateway_scale_unit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnServerConfiguration")
    def vpn_server_configuration(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @vpn_server_configuration.setter
    def vpn_server_configuration(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:P2sVpnGateway")
class P2sVpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., is_routing_preference_internet: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., p2_s_connection_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[P2SConnectionConfigurationArgs, P2SConnectionConfigurationArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_hub: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., vpn_gateway_scale_unit: Optional[pulumi.Input[_builtins.int]] = ..., vpn_server_configuration: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: P2sVpnGatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> P2sVpnGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDnsServers")
    def custom_dns_servers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.P2SConnectionConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnClientConnectionHealth")
    def vpn_client_connection_health(self) -> pulumi.Output[outputs.VpnClientConnectionHealthResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnServerConfiguration")
    def vpn_server_configuration(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    


