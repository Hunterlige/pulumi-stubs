

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SubscriberNotificationArgs', 'SubscriberNotification']
@pulumi.input_type
class SubscriberNotificationArgs:
    def __init__(__self__, *, configuration: pulumi.Input[SubscriberNotificationConfigurationArgs], subscriber_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[SubscriberNotificationConfigurationArgs]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: pulumi.Input[SubscriberNotificationConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberId")
    def subscriber_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subscriber_id.setter
    def subscriber_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SubscriberNotificationState:
    def __init__(__self__, *, configuration: Optional[pulumi.Input[SubscriberNotificationConfigurationArgs]] = ..., endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[SubscriberNotificationConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[SubscriberNotificationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    @_utilities.deprecated("""Use subscriber_endpoint instead""")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEndpoint")
    def subscriber_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_endpoint.setter
    def subscriber_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberId")
    def subscriber_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_id.setter
    def subscriber_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SubscriberNotification(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[SubscriberNotificationConfigurationArgs, SubscriberNotificationConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SubscriberNotificationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[SubscriberNotificationConfigurationArgs, SubscriberNotificationConfigurationArgsDict]]] = ..., endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_id: Optional[pulumi.Input[_builtins.str]] = ...) -> SubscriberNotification:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[outputs.SubscriberNotificationConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    @_utilities.deprecated("""Use subscriber_endpoint instead""")
    def endpoint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberEndpoint")
    def subscriber_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberId")
    def subscriber_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


