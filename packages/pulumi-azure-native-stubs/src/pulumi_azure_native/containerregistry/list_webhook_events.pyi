

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebhookEventsResult', 'AwaitableListWebhookEventsResult', 'list_webhook_events', 'list_webhook_events_output']
@pulumi.output_type
class ListWebhookEventsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.EventResponse]]:
        
        ...
    


class AwaitableListWebhookEventsResult(ListWebhookEventsResult):
    def __await__(self): # -> Generator[Never, Any, ListWebhookEventsResult]:
        ...
    


def list_webhook_events(registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., webhook_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebhookEventsResult:
    
    ...

def list_webhook_events_output(registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., webhook_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebhookEventsResult]:
    
    ...

