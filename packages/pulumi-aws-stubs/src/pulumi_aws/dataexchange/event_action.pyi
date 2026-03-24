

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
__all__ = ['EventActionArgs', 'EventAction']
@pulumi.input_type
class EventActionArgs:
    def __init__(__self__, *, action: pulumi.Input[EventActionActionArgs], event: pulumi.Input[EventActionEventArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[EventActionActionArgs]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[EventActionActionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> pulumi.Input[EventActionEventArgs]:
        
        ...
    
    @event.setter
    def event(self, value: pulumi.Input[EventActionEventArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EventActionState:
    def __init__(__self__, *, action: Optional[pulumi.Input[EventActionActionArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., event: Optional[pulumi.Input[EventActionEventArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[EventActionActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[EventActionActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[EventActionEventArgs]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[EventActionEventArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:dataexchange/eventAction:EventAction")
class EventAction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[EventActionActionArgs, EventActionActionArgsDict]]] = ..., event: Optional[pulumi.Input[Union[EventActionEventArgs, EventActionEventArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventActionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[EventActionActionArgs, EventActionActionArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., event: Optional[pulumi.Input[Union[EventActionEventArgs, EventActionEventArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> EventAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[outputs.EventActionAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> pulumi.Output[outputs.EventActionEvent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


