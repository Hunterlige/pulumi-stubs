

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueueArgs', 'Queue']
@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], auto_delete_on_idle: Optional[pulumi.Input[_builtins.str]] = ..., dead_lettering_on_message_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., default_message_time_to_live: Optional[pulumi.Input[_builtins.str]] = ..., duplicate_detection_history_time_window: Optional[pulumi.Input[_builtins.str]] = ..., enable_batched_operations: Optional[pulumi.Input[_builtins.bool]] = ..., enable_express: Optional[pulumi.Input[_builtins.bool]] = ..., enable_partitioning: Optional[pulumi.Input[_builtins.bool]] = ..., forward_dead_lettered_messages_to: Optional[pulumi.Input[_builtins.str]] = ..., forward_to: Optional[pulumi.Input[_builtins.str]] = ..., lock_duration: Optional[pulumi.Input[_builtins.str]] = ..., max_delivery_count: Optional[pulumi.Input[_builtins.int]] = ..., max_message_size_in_kilobytes: Optional[pulumi.Input[_builtins.float]] = ..., max_size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ..., requires_duplicate_detection: Optional[pulumi.Input[_builtins.bool]] = ..., requires_session: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[EntityStatus]] = ...) -> None:
        
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
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_delete_on_idle.setter
    def auto_delete_on_idle(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @dead_lettering_on_message_expiration.setter
    def dead_lettering_on_message_expiration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_message_time_to_live.setter
    def default_message_time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duplicate_detection_history_time_window.setter
    def duplicate_detection_history_time_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_batched_operations.setter
    def enable_batched_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_express.setter
    def enable_express(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_partitioning.setter
    def enable_partitioning(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forward_dead_lettered_messages_to.setter
    def forward_dead_lettered_messages_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardTo")
    def forward_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forward_to.setter
    def forward_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lock_duration.setter
    def lock_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_delivery_count.setter
    def max_delivery_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_message_size_in_kilobytes.setter
    def max_message_size_in_kilobytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size_in_megabytes.setter
    def max_size_in_megabytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @requires_duplicate_detection.setter
    def requires_duplicate_detection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @requires_session.setter
    def requires_session(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[EntityStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[EntityStatus]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:servicebus:Queue")
class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_delete_on_idle: Optional[pulumi.Input[_builtins.str]] = ..., dead_lettering_on_message_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., default_message_time_to_live: Optional[pulumi.Input[_builtins.str]] = ..., duplicate_detection_history_time_window: Optional[pulumi.Input[_builtins.str]] = ..., enable_batched_operations: Optional[pulumi.Input[_builtins.bool]] = ..., enable_express: Optional[pulumi.Input[_builtins.bool]] = ..., enable_partitioning: Optional[pulumi.Input[_builtins.bool]] = ..., forward_dead_lettered_messages_to: Optional[pulumi.Input[_builtins.str]] = ..., forward_to: Optional[pulumi.Input[_builtins.str]] = ..., lock_duration: Optional[pulumi.Input[_builtins.str]] = ..., max_delivery_count: Optional[pulumi.Input[_builtins.int]] = ..., max_message_size_in_kilobytes: Optional[pulumi.Input[_builtins.float]] = ..., max_size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ..., requires_duplicate_detection: Optional[pulumi.Input[_builtins.bool]] = ..., requires_session: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[EntityStatus]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: QueueArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Queue:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessedAt")
    def accessed_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> pulumi.Output[outputs.MessageCountDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardTo")
    def forward_to(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageCount")
    def message_count(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[_builtins.float]:
        
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
    


