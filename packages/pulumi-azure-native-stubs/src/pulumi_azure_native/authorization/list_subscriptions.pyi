

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListSubscriptionsResult', 'AwaitableListSubscriptionsResult', 'list_subscriptions', 'list_subscriptions_output']
@pulumi.output_type
class ListSubscriptionsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SubscriptionResponse]]:
        
        ...
    


class AwaitableListSubscriptionsResult(ListSubscriptionsResult):
    def __await__(self): # -> Generator[Never, Any, ListSubscriptionsResult]:
        ...
    


def list_subscriptions(api_version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSubscriptionsResult:
    
    ...

def list_subscriptions_output(api_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSubscriptionsResult]:
    
    ...

