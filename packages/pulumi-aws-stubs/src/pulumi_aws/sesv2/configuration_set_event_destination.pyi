

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationSetEventDestinationArgs', 'ConfigurationSetEventDestination']
@pulumi.input_type
class ConfigurationSetEventDestinationArgs:
    def __init__(__self__, *, configuration_set_name: pulumi.Input[_builtins.str], event_destination: pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs], event_destination_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestination")
    def event_destination(self) -> pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs]:
        
        ...
    
    @event_destination.setter
    def event_destination(self, value: pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestinationName")
    def event_destination_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_destination_name.setter
    def event_destination_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ConfigurationSetEventDestinationState:
    def __init__(__self__, *, configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., event_destination: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs]] = ..., event_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestination")
    def event_destination(self) -> Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs]]:
        
        ...
    
    @event_destination.setter
    def event_destination(self, value: Optional[pulumi.Input[ConfigurationSetEventDestinationEventDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestinationName")
    def event_destination_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_destination_name.setter
    def event_destination_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConfigurationSetEventDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., event_destination: Optional[pulumi.Input[Union[ConfigurationSetEventDestinationEventDestinationArgs, ConfigurationSetEventDestinationEventDestinationArgsDict]]] = ..., event_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConfigurationSetEventDestinationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., event_destination: Optional[pulumi.Input[Union[ConfigurationSetEventDestinationEventDestinationArgs, ConfigurationSetEventDestinationEventDestinationArgsDict]]] = ..., event_destination_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ConfigurationSetEventDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestination")
    def event_destination(self) -> pulumi.Output[outputs.ConfigurationSetEventDestinationEventDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDestinationName")
    def event_destination_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


