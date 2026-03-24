

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppWorkflowsConnectionsSlotResult', 'AwaitableListWebAppWorkflowsConnectionsSlotResult', 'list_web_app_workflows_connections_slot', 'list_web_app_workflows_connections_slot_output']
@pulumi.output_type
class ListWebAppWorkflowsConnectionsSlotResult:
    
    def __init__(__self__, id=..., kind=..., location=..., name=..., properties=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.WorkflowEnvelopeResponseProperties:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableListWebAppWorkflowsConnectionsSlotResult(ListWebAppWorkflowsConnectionsSlotResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppWorkflowsConnectionsSlotResult]:
        ...
    


def list_web_app_workflows_connections_slot(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppWorkflowsConnectionsSlotResult:
    
    ...

def list_web_app_workflows_connections_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppWorkflowsConnectionsSlotResult]:
    
    ...

