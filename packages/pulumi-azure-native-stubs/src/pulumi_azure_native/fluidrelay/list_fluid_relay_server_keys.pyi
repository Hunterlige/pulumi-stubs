

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListFluidRelayServerKeysResult', 'AwaitableListFluidRelayServerKeysResult', 'list_fluid_relay_server_keys', 'list_fluid_relay_server_keys_output']
@pulumi.output_type
class ListFluidRelayServerKeysResult:
    
    def __init__(__self__, key1=..., key2=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key1(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key2(self) -> _builtins.str:
        
        ...
    


class AwaitableListFluidRelayServerKeysResult(ListFluidRelayServerKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListFluidRelayServerKeysResult]:
        ...
    


def list_fluid_relay_server_keys(fluid_relay_server_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListFluidRelayServerKeysResult:
    
    ...

def list_fluid_relay_server_keys_output(fluid_relay_server_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListFluidRelayServerKeysResult]:
    
    ...

