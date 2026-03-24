

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetSystemTopicEventSubscriptionDeliveryAttributesResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        
        ...
    


class AwaitableGetSystemTopicEventSubscriptionDeliveryAttributesResult(GetSystemTopicEventSubscriptionDeliveryAttributesResult):
    def __await__(self): # -> Generator[Never, Any, GetSystemTopicEventSubscriptionDeliveryAttributesResult]:
        ...
    


def get_system_topic_event_subscription_delivery_attributes(event_subscription_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., system_topic_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSystemTopicEventSubscriptionDeliveryAttributesResult:
    
    ...

def get_system_topic_event_subscription_delivery_attributes_output(event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., system_topic_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSystemTopicEventSubscriptionDeliveryAttributesResult]:
    
    ...

