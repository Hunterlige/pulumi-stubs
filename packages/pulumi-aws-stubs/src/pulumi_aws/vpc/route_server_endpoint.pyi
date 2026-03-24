

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RouteServerEndpointArgs', 'RouteServerEndpoint']
@pulumi.input_type
class RouteServerEndpointArgs:
    def __init__(__self__, *, route_server_id: pulumi.Input[_builtins.str], subnet_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @route_server_id.setter
    def route_server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RouteServerEndpointState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., eni_address: Optional[pulumi.Input[_builtins.str]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniAddress")
    def eni_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eni_address.setter
    def eni_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniId")
    def eni_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eni_id.setter
    def eni_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerEndpointId")
    def route_server_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_server_endpoint_id.setter
    def route_server_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_server_id.setter
    def route_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RouteServerEndpointTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:vpc/routeServerEndpoint:RouteServerEndpoint")
class RouteServerEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[RouteServerEndpointTimeoutsArgs, RouteServerEndpointTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouteServerEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., eni_address: Optional[pulumi.Input[_builtins.str]] = ..., eni_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., route_server_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., route_server_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[RouteServerEndpointTimeoutsArgs, RouteServerEndpointTimeoutsArgsDict]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> RouteServerEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniAddress")
    def eni_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eniId")
    def eni_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerEndpointId")
    def route_server_endpoint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeServerId")
    def route_server_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.RouteServerEndpointTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


