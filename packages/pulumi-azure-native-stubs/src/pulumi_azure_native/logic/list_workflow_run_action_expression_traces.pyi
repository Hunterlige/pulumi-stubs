

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWorkflowRunActionExpressionTracesResult', ..., 'list_workflow_run_action_expression_traces', 'list_workflow_run_action_expression_traces_output']
@pulumi.output_type
class ListWorkflowRunActionExpressionTracesResult:
    
    def __init__(__self__, inputs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.ExpressionRootResponse]]:
        ...
    


class AwaitableListWorkflowRunActionExpressionTracesResult(ListWorkflowRunActionExpressionTracesResult):
    def __await__(self): # -> Generator[Never, Any, ListWorkflowRunActionExpressionTracesResult]:
        ...
    


def list_workflow_run_action_expression_traces(action_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., run_name: Optional[_builtins.str] = ..., workflow_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWorkflowRunActionExpressionTracesResult:
    
    ...

def list_workflow_run_action_expression_traces_output(action_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., run_name: Optional[pulumi.Input[_builtins.str]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWorkflowRunActionExpressionTracesResult]:
    
    ...

