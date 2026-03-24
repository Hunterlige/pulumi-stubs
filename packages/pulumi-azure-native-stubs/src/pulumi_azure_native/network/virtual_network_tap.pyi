

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
__all__ = ['VirtualNetworkTapInitArgs', 'VirtualNetworkTap']
@pulumi.input_type
class VirtualNetworkTapInitArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], destination_load_balancer_front_end_ip_configuration: Optional[pulumi.Input[FrontendIPConfigurationArgs]] = ..., destination_network_interface_ip_configuration: Optional[pulumi.Input[NetworkInterfaceIPConfigurationArgs]] = ..., destination_port: Optional[pulumi.Input[_builtins.int]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tap_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLoadBalancerFrontEndIPConfiguration")
    def destination_load_balancer_front_end_ip_configuration(self) -> Optional[pulumi.Input[FrontendIPConfigurationArgs]]:
        
        ...
    
    @destination_load_balancer_front_end_ip_configuration.setter
    def destination_load_balancer_front_end_ip_configuration(self, value: Optional[pulumi.Input[FrontendIPConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationNetworkInterfaceIPConfiguration")
    def destination_network_interface_ip_configuration(self) -> Optional[pulumi.Input[NetworkInterfaceIPConfigurationArgs]]:
        
        ...
    
    @destination_network_interface_ip_configuration.setter
    def destination_network_interface_ip_configuration(self, value: Optional[pulumi.Input[NetworkInterfaceIPConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tapName")
    def tap_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tap_name.setter
    def tap_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:VirtualNetworkTap")
class VirtualNetworkTap(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination_load_balancer_front_end_ip_configuration: Optional[pulumi.Input[Union[FrontendIPConfigurationArgs, FrontendIPConfigurationArgsDict]]] = ..., destination_network_interface_ip_configuration: Optional[pulumi.Input[Union[NetworkInterfaceIPConfigurationArgs, NetworkInterfaceIPConfigurationArgsDict]]] = ..., destination_port: Optional[pulumi.Input[_builtins.int]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tap_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualNetworkTapInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualNetworkTap:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLoadBalancerFrontEndIPConfiguration")
    def destination_load_balancer_front_end_ip_configuration(self) -> pulumi.Output[Optional[outputs.FrontendIPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationNetworkInterfaceIPConfiguration")
    def destination_network_interface_ip_configuration(self) -> pulumi.Output[Optional[outputs.NetworkInterfaceIPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceTapConfigurations")
    def network_interface_tap_configurations(self) -> pulumi.Output[Sequence[outputs.NetworkInterfaceTapConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


