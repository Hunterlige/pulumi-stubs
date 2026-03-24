

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
__all__ = ['GatewayArgs', 'Gateway']
@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *, destination_network: pulumi.Input[NetworkRefArgs], resource_group_name: pulumi.Input[_builtins.str], source_network: pulumi.Input[NetworkRefArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., gateway_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., http: Optional[pulumi.Input[Sequence[pulumi.Input[HttpConfigArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tcp: Optional[pulumi.Input[Sequence[pulumi.Input[TcpConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationNetwork")
    def destination_network(self) -> pulumi.Input[NetworkRefArgs]:
        
        ...
    
    @destination_network.setter
    def destination_network(self, value: pulumi.Input[NetworkRefArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceNetwork")
    def source_network(self) -> pulumi.Input[NetworkRefArgs]:
        
        ...
    
    @source_network.setter
    def source_network(self, value: pulumi.Input[NetworkRefArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayResourceName")
    def gateway_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_resource_name.setter
    def gateway_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpConfigArgs]]]]:
        
        ...
    
    @http.setter
    def http(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpConfigArgs]]]]): # -> None:
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
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TcpConfigArgs]]]]:
        
        ...
    
    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TcpConfigArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:servicefabricmesh:Gateway")
class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_network: Optional[pulumi.Input[Union[NetworkRefArgs, NetworkRefArgsDict]]] = ..., gateway_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., http: Optional[pulumi.Input[Sequence[pulumi.Input[Union[HttpConfigArgs, HttpConfigArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_network: Optional[pulumi.Input[Union[NetworkRefArgs, NetworkRefArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tcp: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TcpConfigArgs, TcpConfigArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Gateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationNetwork")
    def destination_network(self) -> pulumi.Output[outputs.NetworkRefResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> pulumi.Output[Optional[Sequence[outputs.HttpConfigResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceNetwork")
    def source_network(self) -> pulumi.Output[outputs.NetworkRefResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> pulumi.Output[Optional[Sequence[outputs.TcpConfigResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


