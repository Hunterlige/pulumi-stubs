

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EventConfigurationsArgs', 'EventConfigurations']
@pulumi.input_type
class EventConfigurationsArgs:
    def __init__(__self__, *, event_configurations: pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventConfigurations")
    def event_configurations(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]:
        
        ...
    
    @event_configurations.setter
    def event_configurations(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EventConfigurationsState:
    def __init__(__self__, *, event_configurations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventConfigurations")
    def event_configurations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]:
        
        ...
    
    @event_configurations.setter
    def event_configurations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:iot/eventConfigurations:EventConfigurations")
class EventConfigurations(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., event_configurations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventConfigurationsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., event_configurations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> EventConfigurations:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventConfigurations")
    def event_configurations(self) -> pulumi.Output[Mapping[str, _builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


