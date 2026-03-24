

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHostingChannelResult', 'AwaitableGetHostingChannelResult', 'get_hosting_channel', 'get_hosting_channel_output']
@pulumi.output_type
class GetHostingChannelResult:
    
    def __init__(__self__, channel_id=..., effective_labels=..., expire_time=..., id=..., labels=..., name=..., pulumi_labels=..., retained_release_count=..., site_id=..., ttl=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainedReleaseCount")
    def retained_release_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        ...
    


class AwaitableGetHostingChannelResult(GetHostingChannelResult):
    def __await__(self): # -> Generator[Never, Any, GetHostingChannelResult]:
        ...
    


def get_hosting_channel(channel_id: Optional[_builtins.str] = ..., site_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHostingChannelResult:
    
    ...

def get_hosting_channel_output(channel_id: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHostingChannelResult]:
    
    ...

