

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListLogicAppWorkflowsConnectionsResult', 'AwaitableListLogicAppWorkflowsConnectionsResult', 'list_logic_app_workflows_connections', 'list_logic_app_workflows_connections_output']
@pulumi.output_type
class ListLogicAppWorkflowsConnectionsResult:
    
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
    


class AwaitableListLogicAppWorkflowsConnectionsResult(ListLogicAppWorkflowsConnectionsResult):
    def __await__(self): # -> Generator[Never, Any, ListLogicAppWorkflowsConnectionsResult]:
        ...
    


def list_logic_app_workflows_connections(container_app_name: Optional[_builtins.str] = ..., logic_app_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListLogicAppWorkflowsConnectionsResult:
    
    ...

def list_logic_app_workflows_connections_output(container_app_name: Optional[pulumi.Input[_builtins.str]] = ..., logic_app_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListLogicAppWorkflowsConnectionsResult]:
    
    ...

