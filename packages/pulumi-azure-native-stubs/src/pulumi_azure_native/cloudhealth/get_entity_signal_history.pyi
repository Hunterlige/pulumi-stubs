

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntitySignalHistoryResult', 'AwaitableGetEntitySignalHistoryResult', 'get_entity_signal_history', 'get_entity_signal_history_output']
@pulumi.output_type
class GetEntitySignalHistoryResult:
    
    def __init__(__self__, entity_name=..., history=..., signal_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def history(self) -> Sequence[outputs.SignalHistoryDataPointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signalName")
    def signal_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEntitySignalHistoryResult(GetEntitySignalHistoryResult):
    def __await__(self): # -> Generator[Never, Any, GetEntitySignalHistoryResult]:
        ...
    


def get_entity_signal_history(end_at: Optional[_builtins.str] = ..., entity_name: Optional[_builtins.str] = ..., health_model_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., signal_name: Optional[_builtins.str] = ..., start_at: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntitySignalHistoryResult:
    
    ...

def get_entity_signal_history_output(end_at: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., entity_name: Optional[pulumi.Input[_builtins.str]] = ..., health_model_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., signal_name: Optional[pulumi.Input[_builtins.str]] = ..., start_at: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntitySignalHistoryResult]:
    
    ...

