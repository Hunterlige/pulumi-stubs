

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListListPendingFlowResult', 'AwaitableListListPendingFlowResult', 'list_list_pending_flow', 'list_list_pending_flow_output']
@pulumi.output_type
class ListListPendingFlowResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.PendingFlowResponse]]:
        
        ...
    


class AwaitableListListPendingFlowResult(ListListPendingFlowResult):
    def __await__(self): # -> Generator[Never, Any, ListListPendingFlowResult]:
        ...
    


def list_list_pending_flow(connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListListPendingFlowResult:
    
    ...

def list_list_pending_flow_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListListPendingFlowResult]:
    
    ...

