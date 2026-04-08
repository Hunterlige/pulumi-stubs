import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetDomainTopicEventSubscriptionDeliveryAttributesResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]: ...

class AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult(
    GetDomainTopicEventSubscriptionDeliveryAttributesResult
):
    def __await__(self): ...

def get_domain_topic_event_subscription_delivery_attributes(
    domain_name: Optional[_builtins.str] = ...,
    event_subscription_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult: ...
def get_domain_topic_event_subscription_delivery_attributes_output(
    domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDomainTopicEventSubscriptionDeliveryAttributesResult]: ...
