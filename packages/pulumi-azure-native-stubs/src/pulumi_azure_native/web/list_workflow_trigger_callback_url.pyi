import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWorkflowTriggerCallbackUrlResult",
    "AwaitableListWorkflowTriggerCallbackUrlResult",
    "list_workflow_trigger_callback_url",
    "list_workflow_trigger_callback_url_output",
]

@pulumi.output_type
class ListWorkflowTriggerCallbackUrlResult:
    def __init__(
        __self__,
        base_path=...,
        method=...,
        queries=...,
        relative_path=...,
        relative_path_parameters=...,
        value=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basePath")
    def base_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def queries(
        self,
    ) -> Optional[outputs.WorkflowTriggerListCallbackUrlQueriesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relativePathParameters")
    def relative_path_parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

class AwaitableListWorkflowTriggerCallbackUrlResult(
    ListWorkflowTriggerCallbackUrlResult
):
    def __await__(self): ...

def list_workflow_trigger_callback_url(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    trigger_name: Optional[_builtins.str] = ...,
    workflow_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWorkflowTriggerCallbackUrlResult: ...
def list_workflow_trigger_callback_url_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWorkflowTriggerCallbackUrlResult]: ...
