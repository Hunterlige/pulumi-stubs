

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTriggerEventSubscriptionStatusResult', 'AwaitableGetTriggerEventSubscriptionStatusResult', 'get_trigger_event_subscription_status', 'get_trigger_event_subscription_status_output']
@pulumi.output_type
class GetTriggerEventSubscriptionStatusResult:
    
    def __init__(__self__, status=..., trigger_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTriggerEventSubscriptionStatusResult(GetTriggerEventSubscriptionStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetTriggerEventSubscriptionStatusResult]:
        ...
    


def get_trigger_event_subscription_status(factory_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., trigger_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTriggerEventSubscriptionStatusResult:
    
    ...

def get_trigger_event_subscription_status_output(factory_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., trigger_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTriggerEventSubscriptionStatusResult]:
    
    ...

