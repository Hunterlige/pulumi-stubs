

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppSyncFunctionTriggersSlotResult', 'AwaitableListWebAppSyncFunctionTriggersSlotResult', 'list_web_app_sync_function_triggers_slot', 'list_web_app_sync_function_triggers_slot_output']
@pulumi.output_type
class ListWebAppSyncFunctionTriggersSlotResult:
    
    def __init__(__self__, key=..., trigger_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListWebAppSyncFunctionTriggersSlotResult(ListWebAppSyncFunctionTriggersSlotResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppSyncFunctionTriggersSlotResult]:
        ...
    


def list_web_app_sync_function_triggers_slot(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppSyncFunctionTriggersSlotResult:
    
    ...

def list_web_app_sync_function_triggers_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppSyncFunctionTriggersSlotResult]:
    
    ...

