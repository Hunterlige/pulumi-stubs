

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
__all__ = ['EndpointInitArgs', 'Endpoint']
@pulumi.input_type
class EndpointInitArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], profile_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], always_serve: Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]] = ..., custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]]] = ..., endpoint_location: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_monitor_status: Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_status: Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]] = ..., geo_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., min_child_endpoints: Optional[pulumi.Input[_builtins.float]] = ..., min_child_endpoints_i_pv4: Optional[pulumi.Input[_builtins.float]] = ..., min_child_endpoints_i_pv6: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.float]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]]:
        
        ...
    
    @always_serve.setter
    def always_serve(self, value: Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]]]:
        
        ...
    
    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_location.setter
    def endpoint_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]]:
        
        ...
    
    @endpoint_monitor_status.setter
    def endpoint_monitor_status(self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]]:
        
        ...
    
    @endpoint_status.setter
    def endpoint_status(self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @geo_mapping.setter
    def geo_mapping(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_child_endpoints.setter
    def min_child_endpoints(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_child_endpoints_i_pv4.setter
    def min_child_endpoints_i_pv4(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_child_endpoints_i_pv6.setter
    def min_child_endpoints_i_pv6(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:trafficmanager:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., always_serve: Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]] = ..., custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointPropertiesCustomHeadersItemArgs, EndpointPropertiesCustomHeadersItemArgsDict]]]]] = ..., endpoint_location: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_monitor_status: Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_status: Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., geo_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., min_child_endpoints: Optional[pulumi.Input[_builtins.float]] = ..., min_child_endpoints_i_pv4: Optional[pulumi.Input[_builtins.float]] = ..., min_child_endpoints_i_pv6: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.float]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointPropertiesSubnetsItemArgs, EndpointPropertiesSubnetsItemArgsDict]]]]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Endpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[Sequence[outputs.EndpointPropertiesCustomHeadersItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence[outputs.EndpointPropertiesSubnetsItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    


