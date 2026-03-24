

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectionResult', 'AwaitableGetConnectionResult', 'get_connection', 'get_connection_output']
@pulumi.output_type
class GetConnectionResult:
    
    def __init__(__self__, arn=..., connected_device_id=..., connected_link_id=..., connection_id=..., description=..., device_id=..., global_network_id=..., id=..., link_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedDeviceId")
    def connected_device_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedLinkId")
    def connected_link_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="linkId")
    def link_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetConnectionResult(GetConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectionResult]:
        ...
    


def get_connection(connection_id: Optional[_builtins.str] = ..., global_network_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectionResult:
    
    ...

def get_connection_output(connection_id: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectionResult]:
    
    ...

