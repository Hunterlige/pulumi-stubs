

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EventHubArgs', 'EventHub']
@pulumi.input_type
class EventHubArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], capture_description: Optional[pulumi.Input[CaptureDescriptionArgs]] = ..., event_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., message_retention_in_days: Optional[pulumi.Input[_builtins.float]] = ..., partition_count: Optional[pulumi.Input[_builtins.float]] = ..., retention_description: Optional[pulumi.Input[RetentionDescriptionArgs]] = ..., status: Optional[pulumi.Input[EntityStatus]] = ..., user_metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> Optional[pulumi.Input[CaptureDescriptionArgs]]:
        
        ...
    
    @capture_description.setter
    def capture_description(self, value: Optional[pulumi.Input[CaptureDescriptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionInDays")
    def message_retention_in_days(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @message_retention_in_days.setter
    def message_retention_in_days(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDescription")
    def retention_description(self) -> Optional[pulumi.Input[RetentionDescriptionArgs]]:
        
        ...
    
    @retention_description.setter
    def retention_description(self, value: Optional[pulumi.Input[RetentionDescriptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[EntityStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[EntityStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_metadata.setter
    def user_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventhub:EventHub")
class EventHub(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capture_description: Optional[pulumi.Input[Union[CaptureDescriptionArgs, CaptureDescriptionArgsDict]]] = ..., event_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., message_retention_in_days: Optional[pulumi.Input[_builtins.float]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., partition_count: Optional[pulumi.Input[_builtins.float]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., retention_description: Optional[pulumi.Input[Union[RetentionDescriptionArgs, RetentionDescriptionArgsDict]]] = ..., status: Optional[pulumi.Input[EntityStatus]] = ..., user_metadata: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventHubArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> EventHub:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> pulumi.Output[Optional[outputs.CaptureDescriptionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionInDays")
    def message_retention_in_days(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIds")
    def partition_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDescription")
    def retention_description(self) -> pulumi.Output[Optional[outputs.RetentionDescriptionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


