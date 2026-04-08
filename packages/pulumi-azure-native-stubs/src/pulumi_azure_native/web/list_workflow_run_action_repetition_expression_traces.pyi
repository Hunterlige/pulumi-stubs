import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class ListWorkflowRunActionRepetitionExpressionTracesResult:
    def __init__(__self__, inputs=..., next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.ExpressionRootResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

class AwaitableListWorkflowRunActionRepetitionExpressionTracesResult(
    ListWorkflowRunActionRepetitionExpressionTracesResult
):
    def __await__(self): ...

def list_workflow_run_action_repetition_expression_traces(
    action_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    repetition_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    run_name: Optional[_builtins.str] = ...,
    workflow_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWorkflowRunActionRepetitionExpressionTracesResult: ...
def list_workflow_run_action_repetition_expression_traces_output(
    action_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    repetition_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    run_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWorkflowRunActionRepetitionExpressionTracesResult]: ...
