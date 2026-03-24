

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetChannelFullUrlResult', 'AwaitableGetChannelFullUrlResult', 'get_channel_full_url', 'get_channel_full_url_output']
@pulumi.output_type
class GetChannelFullUrlResult:
    
    def __init__(__self__, endpoint_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetChannelFullUrlResult(GetChannelFullUrlResult):
    def __await__(self): # -> Generator[Never, Any, GetChannelFullUrlResult]:
        ...
    


def get_channel_full_url(channel_name: Optional[_builtins.str] = ..., partner_namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetChannelFullUrlResult:
    
    ...

def get_channel_full_url_output(channel_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetChannelFullUrlResult]:
    
    ...

