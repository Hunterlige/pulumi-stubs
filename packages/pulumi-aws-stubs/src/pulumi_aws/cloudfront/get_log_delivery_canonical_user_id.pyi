

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLogDeliveryCanonicalUserIdResult', 'AwaitableGetLogDeliveryCanonicalUserIdResult', 'get_log_delivery_canonical_user_id', 'get_log_delivery_canonical_user_id_output']
@pulumi.output_type
class GetLogDeliveryCanonicalUserIdResult:
    
    def __init__(__self__, id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetLogDeliveryCanonicalUserIdResult(GetLogDeliveryCanonicalUserIdResult):
    def __await__(self): # -> Generator[Never, Any, GetLogDeliveryCanonicalUserIdResult]:
        ...
    


def get_log_delivery_canonical_user_id(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLogDeliveryCanonicalUserIdResult:
    
    ...

def get_log_delivery_canonical_user_id_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLogDeliveryCanonicalUserIdResult]:
    
    ...

