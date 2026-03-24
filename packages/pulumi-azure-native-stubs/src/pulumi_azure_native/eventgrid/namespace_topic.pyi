

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NamespaceTopicArgs', 'NamespaceTopic']
@pulumi.input_type
class NamespaceTopicArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], event_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ..., input_schema: Optional[pulumi.Input[Union[_builtins.str, EventInputSchema]]] = ..., publisher_type: Optional[pulumi.Input[Union[_builtins.str, PublisherType]]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventRetentionInDays")
    def event_retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @event_retention_in_days.setter
    def event_retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[pulumi.Input[Union[_builtins.str, EventInputSchema]]]:
        
        ...
    
    @input_schema.setter
    def input_schema(self, value: Optional[pulumi.Input[Union[_builtins.str, EventInputSchema]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherType")
    def publisher_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PublisherType]]]:
        
        ...
    
    @publisher_type.setter
    def publisher_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PublisherType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventgrid:NamespaceTopic")
class NamespaceTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., event_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ..., input_schema: Optional[pulumi.Input[Union[_builtins.str, EventInputSchema]]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., publisher_type: Optional[pulumi.Input[Union[_builtins.str, PublisherType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceTopicArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NamespaceTopic:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventRetentionInDays")
    def event_retention_in_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherType")
    def publisher_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


