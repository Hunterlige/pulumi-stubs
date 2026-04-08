import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetTopicResult", "AwaitableGetTopicResult", "get_topic", "get_topic_output"]

@pulumi.output_type
class GetTopicResult:
    def __init__(
        __self__,
        accessed_at=...,
        auto_delete_on_idle=...,
        azure_api_version=...,
        count_details=...,
        created_at=...,
        default_message_time_to_live=...,
        duplicate_detection_history_time_window=...,
        enable_batched_operations=...,
        enable_express=...,
        enable_partitioning=...,
        id=...,
        location=...,
        max_message_size_in_kilobytes=...,
        max_size_in_megabytes=...,
        name=...,
        requires_duplicate_detection=...,
        size_in_bytes=...,
        status=...,
        subscription_count=...,
        support_ordering=...,
        system_data=...,
        type=...,
        updated_at=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessedAt")
    def accessed_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> outputs.MessageCountDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionCount")
    def subscription_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetTopicResult(GetTopicResult):
    def __await__(self): ...

def get_topic(
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTopicResult: ...
def get_topic_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTopicResult]: ...
