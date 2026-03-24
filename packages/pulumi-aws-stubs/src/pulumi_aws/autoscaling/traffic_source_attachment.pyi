

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
__all__ = ['TrafficSourceAttachmentArgs', 'TrafficSourceAttachment']
@pulumi.input_type
class TrafficSourceAttachmentArgs:
    def __init__(__self__, *, autoscaling_group_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_source: Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSource")
    def traffic_source(self) -> Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]]:
        
        ...
    
    @traffic_source.setter
    def traffic_source(self, value: Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TrafficSourceAttachmentState:
    def __init__(__self__, *, autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_source: Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSource")
    def traffic_source(self) -> Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]]:
        
        ...
    
    @traffic_source.setter
    def traffic_source(self, value: Optional[pulumi.Input[TrafficSourceAttachmentTrafficSourceArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TrafficSourceAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_source: Optional[pulumi.Input[Union[TrafficSourceAttachmentTrafficSourceArgs, TrafficSourceAttachmentTrafficSourceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TrafficSourceAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., traffic_source: Optional[pulumi.Input[Union[TrafficSourceAttachmentTrafficSourceArgs, TrafficSourceAttachmentTrafficSourceArgsDict]]] = ...) -> TrafficSourceAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSource")
    def traffic_source(self) -> pulumi.Output[Optional[outputs.TrafficSourceAttachmentTrafficSource]]:
        
        ...
    


