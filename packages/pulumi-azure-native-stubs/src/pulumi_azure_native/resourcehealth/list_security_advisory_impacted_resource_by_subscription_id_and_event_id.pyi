

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.EventImpactedResourceResponse]:
        
        ...
    


class AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult(ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult):
    def __await__(self): # -> Generator[Never, Any, ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult]:
        ...
    


def list_security_advisory_impacted_resource_by_subscription_id_and_event_id(event_tracking_id: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult:
    
    ...

def list_security_advisory_impacted_resource_by_subscription_id_and_event_id_output(event_tracking_id: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult]:
    
    ...

