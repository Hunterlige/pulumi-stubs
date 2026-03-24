

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionNetworkEndpointArgs', 'RegionNetworkEndpoint']
@pulumi.input_type
class RegionNetworkEndpointArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], region_network_endpoint_group: pulumi.Input[_builtins.str], client_destination_port: Optional[pulumi.Input[_builtins.int]] = ..., fqdn: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionNetworkEndpointGroup")
    def region_network_endpoint_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_network_endpoint_group.setter
    def region_network_endpoint_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientDestinationPort")
    def client_destination_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @client_destination_port.setter
    def client_destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionNetworkEndpointState:
    def __init__(__self__, *, client_destination_port: Optional[pulumi.Input[_builtins.int]] = ..., fqdn: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., network_endpoint_id: Optional[pulumi.Input[_builtins.int]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientDestinationPort")
    def client_destination_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @client_destination_port.setter
    def client_destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpointId")
    def network_endpoint_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @network_endpoint_id.setter
    def network_endpoint_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionNetworkEndpointGroup")
    def region_network_endpoint_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_network_endpoint_group.setter
    def region_network_endpoint_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionNetworkEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., client_destination_port: Optional[pulumi.Input[_builtins.int]] = ..., fqdn: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionNetworkEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., client_destination_port: Optional[pulumi.Input[_builtins.int]] = ..., fqdn: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., network_endpoint_id: Optional[pulumi.Input[_builtins.int]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., region_network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ...) -> RegionNetworkEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientDestinationPort")
    def client_destination_port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpointId")
    def network_endpoint_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionNetworkEndpointGroup")
    def region_network_endpoint_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


