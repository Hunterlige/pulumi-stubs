

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
__all__ = ['EventEndpointArgs', 'EventEndpoint']
@pulumi.input_type
class EventEndpointArgs:
    def __init__(__self__, *, event_buses: pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]], routing_config: pulumi.Input[EventEndpointRoutingConfigArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_config: Optional[pulumi.Input[EventEndpointReplicationConfigArgs]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBuses")
    def event_buses(self) -> pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]]:
        
        ...
    
    @event_buses.setter
    def event_buses(self, value: pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> pulumi.Input[EventEndpointRoutingConfigArgs]:
        
        ...
    
    @routing_config.setter
    def routing_config(self, value: pulumi.Input[EventEndpointRoutingConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfig")
    def replication_config(self) -> Optional[pulumi.Input[EventEndpointReplicationConfigArgs]]:
        
        ...
    
    @replication_config.setter
    def replication_config(self, value: Optional[pulumi.Input[EventEndpointReplicationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EventEndpointState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_url: Optional[pulumi.Input[_builtins.str]] = ..., event_buses: Optional[pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_config: Optional[pulumi.Input[EventEndpointReplicationConfigArgs]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[EventEndpointRoutingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_url.setter
    def endpoint_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBuses")
    def event_buses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]]]:
        
        ...
    
    @event_buses.setter
    def event_buses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EventEndpointEventBusArgs]]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfig")
    def replication_config(self) -> Optional[pulumi.Input[EventEndpointReplicationConfigArgs]]:
        
        ...
    
    @replication_config.setter
    def replication_config(self, value: Optional[pulumi.Input[EventEndpointReplicationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional[pulumi.Input[EventEndpointRoutingConfigArgs]]:
        
        ...
    
    @routing_config.setter
    def routing_config(self, value: Optional[pulumi.Input[EventEndpointRoutingConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/eventEndpoint:EventEndpoint")
class EventEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_buses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventEndpointEventBusArgs, EventEndpointEventBusArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_config: Optional[pulumi.Input[Union[EventEndpointReplicationConfigArgs, EventEndpointReplicationConfigArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[Union[EventEndpointRoutingConfigArgs, EventEndpointRoutingConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_url: Optional[pulumi.Input[_builtins.str]] = ..., event_buses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EventEndpointEventBusArgs, EventEndpointEventBusArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_config: Optional[pulumi.Input[Union[EventEndpointReplicationConfigArgs, EventEndpointReplicationConfigArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[Union[EventEndpointRoutingConfigArgs, EventEndpointRoutingConfigArgsDict]]] = ...) -> EventEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBuses")
    def event_buses(self) -> pulumi.Output[Sequence[outputs.EventEndpointEventBus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfig")
    def replication_config(self) -> pulumi.Output[Optional[outputs.EventEndpointReplicationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> pulumi.Output[outputs.EventEndpointRoutingConfig]:
        
        ...
    


