

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NotificationArgs', 'Notification']
@pulumi.input_type
class NotificationArgs:
    def __init__(__self__, *, group_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], notifications: pulumi.Input[Sequence[pulumi.Input[NotificationType]]], topic_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @group_names.setter
    def group_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> pulumi.Input[Sequence[pulumi.Input[NotificationType]]]:
        
        ...
    
    @notifications.setter
    def notifications(self, value: pulumi.Input[Sequence[pulumi.Input[NotificationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NotificationState:
    def __init__(__self__, *, group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., notifications: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationType]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_names.setter
    def group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NotificationType]]]]:
        
        ...
    
    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationType]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscaling/notification:Notification")
class Notification(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., notifications: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationType]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NotificationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., notifications: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationType]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> Notification:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> pulumi.Output[Sequence[NotificationType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


