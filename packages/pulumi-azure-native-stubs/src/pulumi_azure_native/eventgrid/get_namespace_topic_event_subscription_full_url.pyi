import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNamespaceTopicEventSubscriptionFullUrlResult",
    ...,
    "get_namespace_topic_event_subscription_full_url",
    ...,
]

@pulumi.output_type
class GetNamespaceTopicEventSubscriptionFullUrlResult:
    def __init__(__self__, endpoint_url=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[_builtins.str]: ...

class AwaitableGetNamespaceTopicEventSubscriptionFullUrlResult(
    GetNamespaceTopicEventSubscriptionFullUrlResult
):
    def __await__(self): ...

def get_namespace_topic_event_subscription_full_url(
    event_subscription_name: Optional[_builtins.str] = ...,
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    topic_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNamespaceTopicEventSubscriptionFullUrlResult: ...
def get_namespace_topic_event_subscription_full_url_output(
    event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNamespaceTopicEventSubscriptionFullUrlResult]: ...
