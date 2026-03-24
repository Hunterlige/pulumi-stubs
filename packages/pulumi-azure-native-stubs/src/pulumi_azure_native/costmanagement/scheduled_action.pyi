

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ScheduledActionArgs', 'ScheduledAction']
@pulumi.input_type
class ScheduledActionArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], notification: pulumi.Input[NotificationPropertiesArgs], schedule: pulumi.Input[SchedulePropertiesArgs], status: pulumi.Input[Union[_builtins.str, ScheduledActionStatus]], view_id: pulumi.Input[_builtins.str], file_destination: Optional[pulumi.Input[FileDestinationArgs]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, ScheduledActionKind]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_email: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notification(self) -> pulumi.Input[NotificationPropertiesArgs]:
        
        ...
    
    @notification.setter
    def notification(self, value: pulumi.Input[NotificationPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[SchedulePropertiesArgs]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: pulumi.Input[SchedulePropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, ScheduledActionStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, ScheduledActionStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @view_id.setter
    def view_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileDestination")
    def file_destination(self) -> Optional[pulumi.Input[FileDestinationArgs]]:
        
        ...
    
    @file_destination.setter
    def file_destination(self, value: Optional[pulumi.Input[FileDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, ScheduledActionKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduledActionKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_email.setter
    def notification_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:costmanagement:ScheduledAction")
class ScheduledAction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., file_destination: Optional[pulumi.Input[Union[FileDestinationArgs, FileDestinationArgsDict]]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, ScheduledActionKind]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification: Optional[pulumi.Input[Union[NotificationPropertiesArgs, NotificationPropertiesArgsDict]]] = ..., notification_email: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[Union[SchedulePropertiesArgs, SchedulePropertiesArgsDict]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, ScheduledActionStatus]]] = ..., view_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScheduledActionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ScheduledAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileDestination")
    def file_destination(self) -> pulumi.Output[Optional[outputs.FileDestinationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notification(self) -> pulumi.Output[outputs.NotificationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[outputs.SchedulePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


