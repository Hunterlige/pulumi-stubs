import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPartnerTopicEventSubscriptionResult",
    "AwaitableGetPartnerTopicEventSubscriptionResult",
    "get_partner_topic_event_subscription",
    "get_partner_topic_event_subscription_output",
]

@pulumi.output_type
class GetPartnerTopicEventSubscriptionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        dead_letter_destination=...,
        dead_letter_with_resource_identity=...,
        delivery_with_resource_identity=...,
        destination=...,
        event_delivery_schema=...,
        expiration_time_utc=...,
        filter=...,
        id=...,
        labels=...,
        name=...,
        provisioning_state=...,
        retry_policy=...,
        system_data=...,
        topic=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(
        self,
    ) -> Optional[outputs.StorageBlobDeadLetterDestinationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterWithResourceIdentity")
    def dead_letter_with_resource_identity(
        self,
    ) -> Optional[outputs.DeadLetterWithResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(
        self,
    ) -> Optional[outputs.DeliveryWithResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.EventSubscriptionFilterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RetryPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPartnerTopicEventSubscriptionResult(
    GetPartnerTopicEventSubscriptionResult
):
    def __await__(self): ...

def get_partner_topic_event_subscription(
    event_subscription_name: Optional[_builtins.str] = ...,
    partner_topic_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPartnerTopicEventSubscriptionResult: ...
def get_partner_topic_event_subscription_output(
    event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    partner_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPartnerTopicEventSubscriptionResult]: ...
