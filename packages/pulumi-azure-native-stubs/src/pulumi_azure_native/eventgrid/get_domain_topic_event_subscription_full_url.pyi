

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDomainTopicEventSubscriptionFullUrlResult', ..., 'get_domain_topic_event_subscription_full_url', ...]
@pulumi.output_type
class GetDomainTopicEventSubscriptionFullUrlResult:
    
    def __init__(__self__, endpoint_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetDomainTopicEventSubscriptionFullUrlResult(GetDomainTopicEventSubscriptionFullUrlResult):
    def __await__(self): # -> Generator[Never, Any, GetDomainTopicEventSubscriptionFullUrlResult]:
        ...
    


def get_domain_topic_event_subscription_full_url(domain_name: Optional[_builtins.str] = ..., event_subscription_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., topic_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDomainTopicEventSubscriptionFullUrlResult:
    
    ...

def get_domain_topic_event_subscription_full_url_output(domain_name: Optional[pulumi.Input[_builtins.str]] = ..., event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDomainTopicEventSubscriptionFullUrlResult]:
    
    ...

