

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDevicesResult', 'AwaitableGetDevicesResult', 'get_devices', 'get_devices_output']
@pulumi.output_type
class GetDevicesResult:
    
    def __init__(__self__, global_network_id=..., id=..., ids=..., site_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetDevicesResult(GetDevicesResult):
    def __await__(self): # -> Generator[Never, Any, GetDevicesResult]:
        ...
    


def get_devices(global_network_id: Optional[_builtins.str] = ..., site_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDevicesResult:
    
    ...

def get_devices_output(global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., site_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDevicesResult]:
    
    ...

