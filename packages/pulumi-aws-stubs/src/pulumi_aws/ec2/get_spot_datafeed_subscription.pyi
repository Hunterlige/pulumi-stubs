

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSpotDatafeedSubscriptionResult', 'AwaitableGetSpotDatafeedSubscriptionResult', 'get_spot_datafeed_subscription', 'get_spot_datafeed_subscription_output']
@pulumi.output_type
class GetSpotDatafeedSubscriptionResult:
    
    def __init__(__self__, bucket=..., id=..., prefix=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetSpotDatafeedSubscriptionResult(GetSpotDatafeedSubscriptionResult):
    def __await__(self): # -> Generator[Never, Any, GetSpotDatafeedSubscriptionResult]:
        ...
    


def get_spot_datafeed_subscription(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSpotDatafeedSubscriptionResult:
    
    ...

def get_spot_datafeed_subscription_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSpotDatafeedSubscriptionResult]:
    
    ...

