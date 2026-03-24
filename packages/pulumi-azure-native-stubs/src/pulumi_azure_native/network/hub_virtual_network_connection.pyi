

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HubVirtualNetworkConnectionArgs', 'HubVirtualNetworkConnection']
@pulumi.input_type
class HubVirtualNetworkConnectionArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_hub_name: pulumi.Input[_builtins.str], allow_hub_to_remote_vnet_transit: Optional[pulumi.Input[_builtins.bool]] = ..., allow_remote_vnet_to_use_hub_vnet_gateways: Optional[pulumi.Input[_builtins.bool]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remote_virtual_network: Optional[pulumi.Input[SubResourceArgs]] = ..., routing_configuration: Optional[pulumi.Input[RoutingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHubToRemoteVnetTransit")
    def allow_hub_to_remote_vnet_transit(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_hub_to_remote_vnet_transit.setter
    def allow_hub_to_remote_vnet_transit(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVnetToUseHubVnetGateways")
    def allow_remote_vnet_to_use_hub_vnet_gateways(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_remote_vnet_to_use_hub_vnet_gateways.setter
    def allow_remote_vnet_to_use_hub_vnet_gateways(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_security.setter
    def enable_internet_security(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @remote_virtual_network.setter
    def remote_virtual_network(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[pulumi.Input[RoutingConfigurationArgs]]:
        
        ...
    
    @routing_configuration.setter
    def routing_configuration(self, value: Optional[pulumi.Input[RoutingConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:HubVirtualNetworkConnection")
class HubVirtualNetworkConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_hub_to_remote_vnet_transit: Optional[pulumi.Input[_builtins.bool]] = ..., allow_remote_vnet_to_use_hub_vnet_gateways: Optional[pulumi.Input[_builtins.bool]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_internet_security: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remote_virtual_network: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_configuration: Optional[pulumi.Input[Union[RoutingConfigurationArgs, RoutingConfigurationArgsDict]]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HubVirtualNetworkConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> HubVirtualNetworkConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHubToRemoteVnetTransit")
    def allow_hub_to_remote_vnet_transit(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVnetToUseHubVnetGateways")
    def allow_remote_vnet_to_use_hub_vnet_gateways(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> pulumi.Output[Optional[outputs.RoutingConfigurationResponse]]:
        
        ...
    


