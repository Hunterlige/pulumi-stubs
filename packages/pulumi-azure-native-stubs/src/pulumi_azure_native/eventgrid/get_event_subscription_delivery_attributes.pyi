import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventSubscriptionDeliveryAttributesResult",
    ...,
    "get_event_subscription_delivery_attributes",
    "get_event_subscription_delivery_attributes_output",
]

@pulumi.output_type
class GetEventSubscriptionDeliveryAttributesResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]: ...

class AwaitableGetEventSubscriptionDeliveryAttributesResult(
    GetEventSubscriptionDeliveryAttributesResult
):
    def __await__(self): ...

def get_event_subscription_delivery_attributes(
    event_subscription_name: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventSubscriptionDeliveryAttributesResult: ...
def get_event_subscription_delivery_attributes_output(
    event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventSubscriptionDeliveryAttributesResult]: ...
