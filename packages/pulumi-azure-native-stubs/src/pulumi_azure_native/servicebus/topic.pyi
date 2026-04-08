import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TopicArgs", "Topic"]

@pulumi.input_type
class TopicArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        auto_delete_on_idle: Optional[pulumi.Input[_builtins.str]] = ...,
        default_message_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        duplicate_detection_history_time_window: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        enable_batched_operations: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_express: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_partitioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_message_size_in_kilobytes: Optional[pulumi.Input[_builtins.float]] = ...,
        max_size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        requires_duplicate_detection: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[EntityStatus]] = ...,
        support_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_delete_on_idle.setter
    def auto_delete_on_idle(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_message_time_to_live.setter
    def default_message_time_to_live(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duplicate_detection_history_time_window.setter
    def duplicate_detection_history_time_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_batched_operations.setter
    def enable_batched_operations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_express.setter
    def enable_express(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_partitioning.setter
    def enable_partitioning(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_message_size_in_kilobytes.setter
    def max_message_size_in_kilobytes(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_size_in_megabytes.setter
    def max_size_in_megabytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requires_duplicate_detection.setter
    def requires_duplicate_detection(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[EntityStatus]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[EntityStatus]]): ...
    @_builtins.property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @support_ordering.setter
    def support_ordering(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:servicebus:Topic")
class Topic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_delete_on_idle: Optional[pulumi.Input[_builtins.str]] = ...,
        default_message_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        duplicate_detection_history_time_window: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        enable_batched_operations: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_express: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_partitioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_message_size_in_kilobytes: Optional[pulumi.Input[_builtins.float]] = ...,
        max_size_in_megabytes: Optional[pulumi.Input[_builtins.int]] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_duplicate_detection: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[EntityStatus]] = ...,
        support_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TopicArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Topic: ...
    @_builtins.property
    @pulumi.getter(name="accessedAt")
    def accessed_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> pulumi.Output[outputs.MessageCountDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionCount")
    def subscription_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]: ...
