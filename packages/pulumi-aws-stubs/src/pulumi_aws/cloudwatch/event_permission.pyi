

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
__all__ = ['EventPermissionArgs', 'EventPermission']
@pulumi.input_type
class EventPermissionArgs:
    def __init__(__self__, *, principal: pulumi.Input[_builtins.str], statement_id: pulumi.Input[_builtins.str], action: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[EventPermissionConditionArgs]] = ..., event_bus_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @statement_id.setter
    def statement_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[EventPermissionConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[EventPermissionConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_bus_name.setter
    def event_bus_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EventPermissionState:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[EventPermissionConditionArgs]] = ..., event_bus_name: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[EventPermissionConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[EventPermissionConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_bus_name.setter
    def event_bus_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_id.setter
    def statement_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudwatch/eventPermission:EventPermission")
class EventPermission(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[EventPermissionConditionArgs, EventPermissionConditionArgsDict]]] = ..., event_bus_name: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventPermissionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[_builtins.str]] = ..., condition: Optional[pulumi.Input[Union[EventPermissionConditionArgs, EventPermissionConditionArgsDict]]] = ..., event_bus_name: Optional[pulumi.Input[_builtins.str]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., statement_id: Optional[pulumi.Input[_builtins.str]] = ...) -> EventPermission:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.EventPermissionCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBusName")
    def event_bus_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementId")
    def statement_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


