

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkEndpointListArgs', 'NetworkEndpointList']
@pulumi.input_type
class NetworkEndpointListArgs:
    def __init__(__self__, *, network_endpoint_group: pulumi.Input[_builtins.str], network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_endpoint_group.setter
    def network_endpoint_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpoints")
    def network_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]]:
        
        ...
    
    @network_endpoints.setter
    def network_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]]): # -> None:
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
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkEndpointListState:
    def __init__(__self__, *, network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ..., network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_endpoint_group.setter
    def network_endpoint_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpoints")
    def network_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]]:
        
        ...
    
    @network_endpoints.setter
    def network_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkEndpointListNetworkEndpointArgs]]]]): # -> None:
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
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class NetworkEndpointList(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ..., network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkEndpointListNetworkEndpointArgs, NetworkEndpointListNetworkEndpointArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkEndpointListArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., network_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ..., network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkEndpointListNetworkEndpointArgs, NetworkEndpointListNetworkEndpointArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> NetworkEndpointList:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpoints")
    def network_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.NetworkEndpointListNetworkEndpoint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


