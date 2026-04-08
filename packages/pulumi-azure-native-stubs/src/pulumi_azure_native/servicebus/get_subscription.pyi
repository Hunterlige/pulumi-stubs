import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSubscriptionResult",
    "AwaitableGetSubscriptionResult",
    "get_subscription",
    "get_subscription_output",
]

@pulumi.output_type
class GetSubscriptionResult:
    def __init__(
        __self__,
        accessed_at=...,
        auto_delete_on_idle=...,
        azure_api_version=...,
        client_affine_properties=...,
        count_details=...,
        created_at=...,
        dead_lettering_on_filter_evaluation_exceptions=...,
        dead_lettering_on_message_expiration=...,
        default_message_time_to_live=...,
        duplicate_detection_history_time_window=...,
        enable_batched_operations=...,
        forward_dead_lettered_messages_to=...,
        forward_to=...,
        id=...,
        is_client_affine=...,
        location=...,
        lock_duration=...,
        max_delivery_count=...,
        message_count=...,
        name=...,
        requires_session=...,
        status=...,
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
    @pulumi.getter(name="clientAffineProperties")
    def client_affine_properties(
        self,
    ) -> Optional[outputs.SBClientAffinePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> outputs.MessageCountDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deadLetteringOnFilterEvaluationExceptions")
    def dead_lettering_on_filter_evaluation_exceptions(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> Optional[_builtins.bool]: ...
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
    @pulumi.getter(name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardTo")
    def forward_to(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isClientAffine")
    def is_client_affine(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="messageCount")
    def message_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetSubscriptionResult(GetSubscriptionResult):
    def __await__(self): ...

def get_subscription(
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    subscription_name: Optional[_builtins.str] = ...,
    topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSubscriptionResult: ...
def get_subscription_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSubscriptionResult]: ...
