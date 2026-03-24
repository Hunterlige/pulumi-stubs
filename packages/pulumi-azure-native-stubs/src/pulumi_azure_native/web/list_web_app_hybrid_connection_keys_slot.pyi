

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppHybridConnectionKeysSlotResult', 'AwaitableListWebAppHybridConnectionKeysSlotResult', 'list_web_app_hybrid_connection_keys_slot', 'list_web_app_hybrid_connection_keys_slot_output']
@pulumi.output_type
class ListWebAppHybridConnectionKeysSlotResult:
    
    def __init__(__self__, id=..., kind=..., name=..., send_key_name=..., send_key_value=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendKeyName")
    def send_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendKeyValue")
    def send_key_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableListWebAppHybridConnectionKeysSlotResult(ListWebAppHybridConnectionKeysSlotResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppHybridConnectionKeysSlotResult]:
        ...
    


def list_web_app_hybrid_connection_keys_slot(name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., relay_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppHybridConnectionKeysSlotResult:
    
    ...

def list_web_app_hybrid_connection_keys_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., relay_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppHybridConnectionKeysSlotResult]:
    
    ...

