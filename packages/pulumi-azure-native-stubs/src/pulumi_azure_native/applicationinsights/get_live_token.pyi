

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLiveTokenResult', 'AwaitableGetLiveTokenResult', 'get_live_token', 'get_live_token_output']
@pulumi.output_type
class GetLiveTokenResult:
    
    def __init__(__self__, live_token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveToken")
    def live_token(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLiveTokenResult(GetLiveTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetLiveTokenResult]:
        ...
    


def get_live_token(resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLiveTokenResult:
    
    ...

def get_live_token_output(resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLiveTokenResult]:
    
    ...

