

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntityHistoryResult', 'AwaitableGetEntityHistoryResult', 'get_entity_history', 'get_entity_history_output']
@pulumi.output_type
class GetEntityHistoryResult:
    
    def __init__(__self__, entity_name=..., history=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def history(self) -> Sequence[outputs.HealthStateTransitionResponse]:
        
        ...
    


class AwaitableGetEntityHistoryResult(GetEntityHistoryResult):
    def __await__(self): # -> Generator[Never, Any, GetEntityHistoryResult]:
        ...
    


def get_entity_history(end_at: Optional[_builtins.str] = ..., entity_name: Optional[_builtins.str] = ..., health_model_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., start_at: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntityHistoryResult:
    
    ...

def get_entity_history_output(end_at: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., entity_name: Optional[pulumi.Input[_builtins.str]] = ..., health_model_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., start_at: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntityHistoryResult]:
    
    ...

