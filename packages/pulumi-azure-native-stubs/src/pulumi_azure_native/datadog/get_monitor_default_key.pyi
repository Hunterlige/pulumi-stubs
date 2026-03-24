

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMonitorDefaultKeyResult', 'AwaitableGetMonitorDefaultKeyResult', 'get_monitor_default_key', 'get_monitor_default_key_output']
@pulumi.output_type
class GetMonitorDefaultKeyResult:
    def __init__(__self__, created=..., created_by=..., key=..., name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetMonitorDefaultKeyResult(GetMonitorDefaultKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetMonitorDefaultKeyResult]:
        ...
    


def get_monitor_default_key(monitor_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMonitorDefaultKeyResult:
    
    ...

def get_monitor_default_key_output(monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMonitorDefaultKeyResult]:
    
    ...

